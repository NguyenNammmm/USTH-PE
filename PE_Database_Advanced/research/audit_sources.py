"""Read-only source inventory. Lexical evidence is discovery, not a depth verdict."""
from pathlib import Path
from pypdf import PdfReader
import collections,hashlib,json,re,unicodedata
R=Path(__file__).resolve().parents[3]; O=Path(__file__).resolve().parent
S=R/'tmp/database-source'; OLD=R/'output/database-pe'; load=lambda p:json.loads(p.read_text(encoding='utf-8'))
manifest=load(OLD/'manifest.json');inventory=load(OLD/'docs/source-inventory.json');old={x['id']:{**x,'text':(OLD/x['path']).read_text(encoding='utf-8')} for x in manifest['lessons']}
def normal(s):return unicodedata.normalize('NFKC',s).replace('\u00ad','').strip()
def stem(t):return [x.lower() for x in re.findall(r'[A-Za-z][A-Za-z-]+',normal(t)) if x.lower() not in {'of','the','a','an','and','or','for','in','to','on','using','with','database','databases','systems','system','data'}]
def declared(refs,section):
 c=section.split('.')[0];parts=section.split('.');major=parts[1] if len(parts)>1 else ''
 for ref in refs:
  ref=str(ref).replace('–','-')
  if ref==c or ref==section or section.startswith(ref+'.'):return True
  if re.match(r'^\d+-\d+$',ref):
   a,b=map(int,ref.split('-'))
   if c.isdigit() and a<=int(c)<=b:return True
  m=re.match(r'^(\d+)\.(\d+)-(\d+)\.(\d+)$',ref)
  if m and c==m[1]==m[3] and major and int(m[2])<=int(major)<=int(m[4]):return True
 return False

bookfile=next(Path(x['path']) for x in inventory['provided_sources'] if 'Database-System-Concepts' in x['name']);pdf=PdfReader(bookfile)
outlines=[]
def walk(items):
 for item in items:
  if isinstance(item,list):walk(item)
  else:
   title=normal(item.title)
   if re.match(r'^\d+\.\d+\s',title) and 'Summary' not in title:outlines.append({'section':title.split()[0],'title':title.split(' ',1)[1],'pdfPage':pdf.get_destination_page_number(item)+1})
walk(pdf.outline)
outline_map={x['section']:x for x in outlines}
sections=[];chapterstats=[]
for ch in [*map(str,range(1,33)),'A']:
 file=S/('appendix-a.txt' if ch=='A' else ('chapter-' if int(ch)<=26 else 'online-')+ch+'.txt')
 lines=file.read_text(encoding='utf-8').splitlines();page=None;starts={};candidates=[];stop=len(lines)
 for i,line in enumerate(lines):
  n=normal(line);pm=re.match(r'^\[PDF PAGE (\d+)\]$',n)
  if pm:page=int(pm[1]);continue
  m=re.match(r'^('+re.escape(ch)+r'(?:\.\d+){1,6})\s+([A-Z0-9][^\n]{2,180})$',n)
  if not m:continue
  ident,title=m.groups()
  if re.search(r'\s+\d{1,4}$',title):continue # repeated page header, not body heading
  title=title.strip()
  if title=='Summary':stop=i;break
  if ident in starts:continue
  # Body references such as "7.1 We ..." are excluded when not plausible headings.
  if re.search(r'\b(?:we|you|the|is|was|are|were|shown|Suppose|Explain|Consider|List|Find|Write|Show|Give|What)\b',title) and ident in outline_map and title!=outline_map[ident]['title']:continue
  starts[ident]=i;candidates.append({'section':ident,'title':title,'sourcePath':str(file.relative_to(R)),'sourceLine':i+1,'sourcePdfPage':page,'chapter':ch})
 # The actual PDF outline corrects extraction/OCR for every print top-level section.
 for item in candidates:
  if item['section'] in outline_map:item['title']=outline_map[item['section']]['title'];item['sourcePdfPage']=outline_map[item['section']]['pdfPage']
 candidates.sort(key=lambda x:x['sourceLine'])
 for pos,item in enumerate(candidates):
  start=item['sourceLine']-1;end=candidates[pos+1]['sourceLine']-1 if pos+1<len(candidates) else stop
  # Parent scope includes descendants until next same-or-higher depth.
  depth=item['section'].count('.')
  parentend=next((x['sourceLine']-1 for x in candidates[pos+1:] if x['section'].count('.')<=depth),stop)
  body='\n'.join(lines[start:end]);whole='\n'.join(lines[start:parentend]);tokens=stem(item['title'])
  declaredids=[lid for lid,l in old.items() if declared(l['book_sections'],item['section'])]
  evidence=[]
  for lid in declaredids:
   text=old[lid]['text'];lt=normal(text).lower();matched=[x for x in tokens if x in lt]
   relevant=[]
   for no,line in enumerate(text.splitlines(),1):
    if any(x in normal(line).lower() for x in tokens) and len(relevant)<3:relevant.append({'line':no,'heading':line[:180] if line.startswith('#') else None})
   evidence.append({'lesson':lid,'matchedEnglishTitleTerms':matched,'candidateLines':relevant,'caution':'Lexical matches locate text; they do not establish self-study depth or correctness.'})
  item.update({'parentSection':item['section'].rsplit('.',1)[0] if depth>1 else None,'depth':depth,'bodyWordCount':len(body.split()),'scopeWordCount':len(whole.split()),'scopeLineEnd':parentend,'declaredOldLessonIds':declaredids,'oldEvidenceCandidates':evidence,'algorithmSignals':sorted(set(re.findall(r'\b(?:algorithm|pseudocode|procedure|invariant|termination|recursive|dynamic programming)\b',normal(whole).lower()))),'proofSignals':sorted(set(re.findall(r'\b(?:proof|prove|theorem|lemma|soundness|completeness|correctness|induction)\b',normal(whole).lower()))),'depthVerdict':'requires-content-review','plannedAdvancedLessonIds':[]})
  sections.append(item)
 chapterstats.append({'chapter':ch,'numberedUnits':len(candidates),'topLevel':sum(x['depth']==1 for x in candidates),'sourceSha256':hashlib.sha256(file.read_bytes()).hexdigest()})
missing_outline=[x for x in outlines if x['section'] not in {s['section'] for s in sections}]
lectures=[];labs=[];oldlecture={str(n):[x['id'] for x in manifest['lessons'] if str(n) in x['usth_lectures']] for n in range(1,10)}
for src in inventory['provided_sources']:
 if not src['name'].endswith('.pdf') or 'Database-System-Concepts' in src['name']:continue
 path=Path(src['path']);reader=PdfReader(path);kind='lecture' if src['name'].startswith('Lecture') else 'practice';num=re.search(r'\d+',src['name']).group()
 for i,page in enumerate(reader.pages,1):
  txt=normal(page.extract_text() or '');lines=[normal(x) for x in txt.splitlines() if x.strip()];meaningful=[x for x in lines if not re.fullmatch(r'\d+|USTH|Advanced Database|Database',x)]
  item={'source':src['name'],'sourcePath':str(path),'pdfPage':i,'titleCandidates':meaningful[:3],'textWordCount':len(txt.split()),'sha256':src['sha256'],'declaredOldLessonIds':oldlecture[num] if kind=='lecture' else ['Z01'] if num=='1' else ['Z02'],'status':'review-page-against-new-activity-before-completion'}
  (lectures if kind=='lecture' else labs).append(item)
result={'date':'2026-11-05','scope':'Advanced continuation after85 lessons. Inventory of every extracted numbered section/subsection plus every supplied lecture/lab PDF page. No assertion of complete teaching depth.','sourceBook':{'path':str(bookfile),'sha256':hashlib.sha256(bookfile.read_bytes()).hexdigest(),'edition':'7e','pages':len(pdf.pages)},'extractionPolicy':{'include':'Numbered body headings up to four numeric components, before chapter Summary. Print top-level titles/pages corrected against PDF outline. Appendix A and online27–32 included.','exclude':'Summary, exercises, practice exercises, further reading, unnumbered index/glossary. Source exercises remain source requirements for skill selection, not copied proprietary answer bank.','depth':'Language matching locates candidate evidence only. Human comparison needed for each algorithm/proof and activity.'},'counts':{'bookUnits':len(sections),'printTopLevelOutlineUnits':len(outlines),'missingPrintOutlineUnits':len(missing_outline),'lecturePages':len(lectures),'practicePages':len(labs)},'chapterStats':chapterstats,'missingPrintOutlineUnits':missing_outline,'bookSections':sections,'lecturePages':lectures,'practicePages':labs}
(O/'source-section-inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'counts':result['counts'],'chapters':chapterstats,'missingOutline':missing_outline},ensure_ascii=False,indent=2))
