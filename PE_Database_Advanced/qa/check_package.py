"""Structural, provenance and link checks; no semantic completeness promotion."""
from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=load(R/'manifest.json');inventory=load(R/'research/source-section-inventory.json')
checks=[];broken=[];structures=[]
def check(name,passed,detail=None):
 checks.append({'name':name,'passed':bool(passed),'detail':detail})
by={x['id']:x for x in m['lessons']}
for l in m['lessons']:
 p=R/l['path'];text=p.read_text(encoding='utf-8-sig')
 headings=re.findall(r'^## (.+)',text,re.M)
 required=['Luyện tập','Gợi ý','Đáp án','Biến thể','Học trên web','Nguồn']
 missing=[s for s in required if not any(h.startswith(s) for h in headings)]
 structures.append({'id':l['id'],'sha256':sha(p),'words':len(text.split()),'codeFencesBalanced':len(re.findall(r'^```',text,re.M))%2==0,'missingHeadings':missing})
 for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
  if re.match(r'^(https?:|#|mailto:)',target):continue
  resolved=(p.parent/target.split('#')[0]).resolve()
  if not resolved.exists():broken.append({'file':l['path'],'target':target})
check('85 new lessons exist and required learning sections are present',len(structures)==85 and all(not x['missingHeadings'] and x['codeFencesBalanced'] for x in structures),structures)
check('all lesson Markdown relative links resolve',not broken,broken)
supp=m.get('supplementalLessons',[])
check('eleven USTH supplements and151 answered activity records are included',len(supp)==11 and sum(x['practiceQuestions'] for x in supp)==151 and all((R/x['path']).exists() and '## Đáp án và lập luận' in (R/x['path']).read_text(encoding='utf-8-sig') for x in supp))
snap=load(R/'baseline/snapshot-provenance.json')
check('85 baseline lesson hashes remain unchanged',len(snap['files'])==85 and all(sha(R/'baseline'/x['path'])==x['sha256']==x['snapshotSha256'] for x in snap['files']))
check('947 source units have valid owner IDs',len(inventory['bookSections'])==947 and all(s['plannedAdvancedLessonIds'] and set(s['plannedAdvancedLessonIds'])<=by.keys() for s in inventory['bookSections']))
bookgate=load(R/'research/semantic-gate-summary.json');slidegate=load(R/'research/semantic-slides-gate-summary.json')
check('source-content flag requires complete current book and page evidence',m['allContentComplete'] is True and bookgate['allBookUnitsProven'] and slidegate['allSlidePagesProven'] and bookgate['counts']=={'complete-current-evidence':947} and slidegate['counts']=={'non-instructional':49,'complete-current-evidence':409})
positions={id:i for i,id in enumerate(m['recommendedTopologicalOrder'])}
check('recommended order respects all new prerequisites',len(positions)==85 and all(positions[d]<positions[l['id']] for l in by.values() for d in l['newPrereqs']))
activities=load(R/'activities.json')['activities'];check('seven selected adapted repo labs linked to actual lesson IDs',len(activities)==7 and all(set(a['lessonIds'])<=by.keys() for a in activities))
inputs=load(R/'fixtures/selected-inputs.json')['inputs'];check('selected redistributed input hash and license exist',all(sha(R/x['path'])==x['sha256'] for x in inputs) and (R/'research/licenses/chinook-MIT.txt').exists())
boards=load(R/'qa/state-boards.json')['boards'];check('all24 key illustrations match current lesson content',len(boards)==24 and all(sha(R/'lessons'/(x['id']+'.md'))==x['lessonSha256'] and sha(R/x['path'])==x['imageSha256'] for x in boards))
result={'scope':'Structure, file provenance, link and assignment checks only. Not an all-source semantic certificate.','passed':sum(x['passed'] for x in checks),'total':len(checks),'checks':checks}
(R/'qa/package-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':result['passed'],'total':result['total'],'failures':[x['name'] for x in checks if not x['passed']]},ensure_ascii=False));assert result['passed']==result['total']
