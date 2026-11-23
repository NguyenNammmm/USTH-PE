from pathlib import Path
import collections,json,re
O=Path(__file__).resolve().parent;W=O.parents[2]
path=O/'source-section-inventory.json';inv=json.loads(path.read_text(encoding='utf-8'))
known={s['section'] for s in inv['bookSections']};units=inv['bookSections'];inserted=[]
for id,title,line,owner in [('7.5.2','3NF Decomposition',1444,'AD06'),('7.6.3','4NF Decomposition',1744,'AD07')]:
 if id in known:continue
 parent=next(s for s in units if s['section']==id.rsplit('.',1)[0]);source=parent['sourcePath'];lines=(W/source).read_text(encoding='utf-8').splitlines()
 assert lines[line-1].strip()==id+' '+title
 pages=[int(m[1]) for l in lines[:line] if (m:=re.match(r'^\[PDF PAGE (\d+)\]$',l))]
 item={'section':id,'title':title,'sourcePath':source,'sourceLine':line,'sourcePdfPage':pages[-1],'chapter':'7','parentSection':id.rsplit('.',1)[0],'depth':id.count('.'),'declaredOldLessonIds':parent['declaredOldLessonIds'][:],'oldEvidenceCandidates':[],'depthVerdict':'authoring-assigned-not-semantic-complete','plannedAdvancedLessonIds':[owner],'completionEvidenceRequired':'Actual source-body to instructional/example/proof/activity/answer correspondence','baselineCreditAllowed':False,'extractionRecovery':'Initial uppercase-only title parser omitted a numeric normal-form heading; source body directly inspected.'}
 units.append(item);inserted.append(id)
chapter_order={c:i for i,c in enumerate([*map(str,range(1,33)),'A'])}
units.sort(key=lambda x:(chapter_order[x['chapter']],x['sourceLine']))
for chapter in {'7'}:
 part=[s for s in units if s['chapter']==chapter];lines=(W/part[0]['sourcePath']).read_text(encoding='utf-8').splitlines();stop=max(s.get('scopeLineEnd',0) for s in part)
 for i,s in enumerate(part):
  start=s['sourceLine']-1;end=part[i+1]['sourceLine']-1 if i+1<len(part) else stop
  parent_end=next((v['sourceLine']-1 for v in part[i+1:] if v['depth']<=s['depth']),stop)
  body='\n'.join(lines[start:end]);scope='\n'.join(lines[start:parent_end])
  s.update(bodyWordCount=len(body.split()),scopeWordCount=len(scope.split()),scopeLineEnd=parent_end)
  s['algorithmSignals']=sorted(set(re.findall(r'\b(?:algorithm|pseudocode|procedure|invariant|termination|recursive|dynamic programming)\b',scope.lower())))
  s['proofSignals']=sorted(set(re.findall(r'\b(?:proof|prove|theorem|lemma|soundness|completeness|correctness|induction)\b',scope.lower())))
inv['counts']['bookUnits']=len(units)
for row in inv['chapterStats']:
 if row['chapter']=='7':row['numberedUnits']=sum(s['chapter']=='7' for s in units)
inv['extractionPolicy']['recovery']='Numeric-leading normal-form titles7.5.2/7.6.3 recovered from actual body text; candidate diagnostic also checks up to seven numbering components.'
path.write_text(json.dumps(inv,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'inserted':inserted,'bookUnits':len(units),'leafUnits':sum(not any(t['section'].startswith(s['section']+'.') for t in units) for s in units)}))
