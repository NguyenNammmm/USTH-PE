"""Text/bookmark/bounds checks plus render samples; visual review remains separate."""
from pathlib import Path
import hashlib,json,re
from pypdf import PdfReader
import pypdfium2 as pdfium
R=Path(__file__).resolve().parents[1];OUT=R/'qa/pdf-render';OUT.mkdir(exist_ok=True)
meta=json.loads((R/'qa/pdf-build.json').read_text(encoding='utf-8'))
manifest=json.loads((R/'manifest.json').read_text(encoding='utf-8'))
reader=PdfReader(R/'Database-Advanced-PE.pdf');bookmarks=meta['bookmarks']
texts=[]
for n,page in enumerate(reader.pages,1):
 lines=(page.extract_text() or '').splitlines()
 assert lines[:4]==['DATABASE ADVANCED / USTH + DSC7e','06/11/2026','Bài giảng Advanced và đặc tả web - MySQL baseline',str(n)],('Running header/footer structure changed',n,lines[:4])
 texts.append('\n'.join(lines[4:]))
norm=lambda s:re.sub(r'[^\w]+','',s,flags=re.U).lower()
checks=[]
all_lessons=manifest['lessons']+manifest.get('supplementalLessons',[])
for lesson in all_lessons:
 start=bookmarks[lesson['id']]-1
 other=[p-1 for name,p in bookmarks.items() if name!=lesson['id'] and p-1>start and not name.endswith('-states')]
 end=min(other) if other else len(texts)
 text='\n'.join(texts[start:end]);source=(R/lesson['path']).read_text(encoding='utf-8-sig')
 headings=re.findall(r'^## (.+)',source,re.M)
 missing=[h for h in headings if norm(h) not in norm(text)]
 assert not missing,(lesson['id'],missing,start,end)
 # Check the actual opening and closing prose too, not only headings.
 paras=[p.strip() for p in source.split('\n\n') if p.strip() and not p.lstrip().startswith(('#','```','|','1.','- ')) and len(p.split())>15]
 plain=lambda p:re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',p).replace('`','').replace('**','')
 witnesses=[norm(' '.join(plain(p).split()[:18])) for p in (paras[:1]+paras[-1:])]
 normalized=norm(text)
 line_witnesses=[]
 for line in source.splitlines()[1:]:
  if not line.strip() or line.startswith('```'):continue
  candidates=line.strip('|').split('|') if line.startswith('|') else [line]
  for value in candidates:
   candidate=norm(plain(value))
   if len(candidate)>=12:line_witnesses.append(candidate)
 absent=[value for value in line_witnesses if value not in normalized]
 checks.append({'lesson':lesson['id'],'pageStart':start+1,'pageEnd':end,'allHeadingsPresent':not missing,'openingClosingWitnessesPresent':all(w in normalized for w in witnesses),'lineWitnessesChecked':len(line_witnesses),'missingLineWitnesses':absent})
assert all(c['openingClosingWitnessesPresent'] for c in checks),[c for c in checks if not c['openingClosingWitnessesPresent']]
(R/'qa/pdf-text-witness-checks.json').write_text(json.dumps({'scope':'All lesson/source line witnesses after removing the four verified running header/footer text lines on every page; independent of layout/render review.','checks':checks},ensure_ascii=False,indent=2),encoding='utf-8')
assert all(not c['missingLineWitnesses'] for c in checks),[(c['lesson'],len(c['missingLineWitnesses']),[v[:100] for v in c['missingLineWitnesses'][:2]]) for c in checks if c['missingLineWitnesses']]
assert len(checks)==96 and meta['key_lessons']==24 and meta['supplemental_lessons']==11 and meta['supplemental_questions']==151 and not meta['unsupported_characters']
selected={1,2,3,len(texts)}
for name,p in bookmarks.items():
 if name.startswith('module-') or name.endswith('-states') or name.startswith('appendix-'):selected.add(p)
for lesson in all_lessons:selected.add(bookmarks[lesson['id']])
for check in checks:
 if check['lesson'].startswith('USTH'):
  selected.update([check['pageStart'],(check['pageStart']+check['pageEnd'])//2,check['pageEnd']])
for id in ['AD03','AD09','AD15','AD22','AD28','AD36','AD43','AD59','AD75','AD77','AD82','AD83','AD84','AD85']:
 selected.add(bookmarks[id]);selected.add(min(len(texts),bookmarks[id]+2))
pdf=pdfium.PdfDocument(str(R/'Database-Advanced-PE.pdf'))
rendered=[]
for n in sorted(selected):
 page=pdf[n-1];im=page.render(scale=1.25).to_pil();target=OUT/('page-'+str(n).zfill(4)+'.png');im.save(target)
 rendered.append({'page':n,'path':str(target.relative_to(R)).replace('\\','/')});page.close()
pdf.close()
result={'scope':'All96 lesson headings plus opening/closing prose witnesses,11 supplements/151 questions and24 illustration bookmarks; all lesson openings and selected middle/end renders require visual review.','pages':len(reader.pages),'checks':checks,'rendered':rendered,'pdfSha256':hashlib.sha256((R/'Database-Advanced-PE.pdf').read_bytes()).hexdigest(),'visualReview':'pending'}
(R/'qa/pdf-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(reader.pages),'lessonsChecked':len(checks),'rendered':len(rendered)}))
