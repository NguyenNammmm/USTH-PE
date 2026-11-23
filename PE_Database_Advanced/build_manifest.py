"""Prepare versioned course metadata and an unchanged reference snapshot of old85."""
from pathlib import Path
import collections,hashlib,json,re,shutil
ROOT=Path(__file__).resolve().parent;BASE=ROOT.parent/'database-pe'
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
proposal=load(ROOT/'research/proposed-lessons.json');items=proposal['lessons'];old=load(BASE/'manifest.json')
snapshot=ROOT/'baseline';snapshot.mkdir(exist_ok=True)
for folder in ['lessons','fixtures','assets']:
 shutil.copytree(BASE/folder,snapshot/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
shutil.copy2(BASE/'manifest.json',snapshot/'manifest.json')
hashes=[{'path':l['path'],'sha256':sha(BASE/l['path']),'snapshotSha256':sha(snapshot/l['path'])} for l in old['lessons']]
assert all(x['sha256']==x['snapshotSha256'] for x in hashes)
(snapshot/'snapshot-provenance.json').write_text(json.dumps({'scope':'Unchanged85 previousPE lessons, not a claim of independent complete new-depth coverage.','sourceManifestSha256':sha(BASE/'manifest.json'),'files':hashes},ensure_ascii=False,indent=2),encoding='utf-8')
for x in items:
 x['path']='lessons/'+x['id']+'.md'
 x['status']='authored-pending-review' if (ROOT/x['path']).exists() else 'not-yet-authored'
 x['baselinePaths']={id:'baseline/'+next(o['path'] for o in old['lessons'] if o['id']==id) for id in x['oldPrereqs']}
modules=[]
for title in dict.fromkeys(x['module'] for x in items):modules.append({'id':'AM'+str(len(modules)+1).zfill(2),'title':title,'lessonIds':[x['id'] for x in items if x['module']==title]})
by={x['id']:x for x in items};oldids={x['id'] for x in old['lessons']}
for x in items:
 assert set(x['oldPrereqs'])<=oldids,(x['id'],x['oldPrereqs'])
 assert set(x['newPrereqs'])<=by.keys(),(x['id'],x['newPrereqs'])
visiting=set();done=set();order=[]
def visit(id):
 if id in done:return
 assert id not in visiting,('cycle',id)
 visiting.add(id)
 for dep in by[id]['newPrereqs']:visit(dep)
 visiting.remove(id);done.add(id);order.append(id)
for id in by:visit(id)
result={'title':'Database Advanced · Sau85 bàiPE','date':'2026-11-05','scope':'Advancedcontinuation, paidcourse, alllearnerpracticeweb; fourhandoffartifacts, notproductiondeployment.','baseline':'MySQL8.4/InnoDB; otherengines explicitlyversionedwhenneeded','modules':modules,'recommendedTopologicalOrder':order,'lessons':items,'baselineLessons':[{'id':x['id'],'title':x['title'],'path':'baseline/'+x['path']} for x in old['lessons']],'authoredCount':sum(x['status']!='not-yet-authored' for x in items),'plannedCount':len(items),'keyCount':sum(bool(x['key']) for x in items),'allContentComplete':False}
(ROOT/'manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'planned':len(items),'authored':result['authoredCount'],'keys':result['keyCount'],'modules':len(modules),'baseline':len(old['lessons']),'graph':'no missing IDs or cycles'},ensure_ascii=False))
