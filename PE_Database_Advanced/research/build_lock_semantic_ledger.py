from pathlib import Path
import hashlib,json,re
O=Path(__file__).resolve().parent;R=O.parent;W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
source=W/'tmp/database-source/chapter-18.txt';lines=source.read_text(encoding='utf-8').splitlines();lesson=R/'lessons/AD39.md';text=lesson.read_text(encoding='utf-8-sig');paras=[p.strip() for p in text.split('\n\n') if p.strip()]
assert sha(lesson)==load(O/'root-reviewed-snapshots.json')['lessons']['AD39'],'Changed lesson needs direct rereview'
inv=load(O/'source-section-inventory.json');allunits=[s for s in inv['bookSections'] if s['chapter']=='18'];target={'18.1','18.1.1','18.1.2','18.1.3','18.1.4','18.1.5','18.3'}
def anchor(needle,kind):
 found=[(i+1,p) for i,p in enumerate(paras) if needle in p];assert len(found)==1,(needle,len(found))
 i,p=found[0];return {'path':'lessons/AD39.md','lessonSha256':sha(lesson),'kind':kind,'paragraph':i,'exactOpening':p[:350]}
decisions={
 '18.1':('S lock cho đọc','Ví dụ số: A=B=100','1. Kiểm chuỗi của T:','1. Không: xin X(B)', 'Lock-basedisolationparentintroduction; permissionbeforeoperation.'),
 '18.1.1':('X lock cho phép cả đọc','Ví dụ số: A=B=100','2. T1,T2 cùng S(A)','2. T1 chờ T2', 'S/Xsemantics/compatibility/requestgrant/earlyrelease inconsistency/deadlock/legalprotocol.'),
 '18.1.2':('Quy tắc FIFO đơn giản','Quy tắc FIFO đơn giản','5. T1 giữ S(A)','5. T3/T4 chờ', 'FIFO no-bypass starvationpreventionandassumptions;abortheadrescan.'),
 '18.1.3':('Trong 2PL cơ bản','Basic2PL vẫn có thể cascade','4. Chứng minh 2PL⇒','4. Chứng minh 2PL dùng', 'Growing/shrinking/lockpointproof, strict/rigorous, conversions, automaticlockgeneration, non2PLserializablewitness.'),
 '18.1.4':('Lock table có thể là hash map','```text\nrequest(T,Q,mode):','5. T1 giữ S(A)','5. T3/T4 chờ', 'Hashitemqueue+transactionindex,granted/wait flags,request/unlock/abort algorithm,compatibility/FIFOinvariants andcleanupordering.'),
 '18.1.5':('Một protocol trên cây rooted','Để thấy ý nghĩa thứ tự','6. Dựng tree model','6. T2 commit chỉ', 'Allfourtreerules,serializability/deadlockproof,earlyrelease/extraancestorcost,protocolincomparability andcommitdependencyrecovery.'),
 '18.3':('Trong hierarchy này','Ví dụ đọc row7:','3. Một transaction giữ IX','3. S(T) bị IX', 'Implicitcoarsesubtree/intentionhierarchy,all5modescompatibility,root/topdown/bottomup/2PLrules,escalation/deadlocktradeoff.')}
rows=[]
for i,s in enumerate(allunits):
 if s['section'] not in target:continue
 end=allunits[i+1]['sourceLine']-1 if i+1<len(allunits) else s['scopeLineEnd'];body='\n'.join(lines[s['sourceLine']-1:end]);e,x,q,a,judgment=decisions[s['section']]
 rows.append({'section':s['section'],'title':s['title'],'owners':['AD39'],'source':{'path':'tmp/database-source/chapter-18.txt','sha256':sha(source),'ownBodyLines':[s['sourceLine'],end],'ownBodySha256':hashlib.sha256(body.encode()).hexdigest()},'sourceReadEvidence':{'ownBodyRead':True,'readBatches':[[1,535],[711,858]],'figurePagesVisuallyInspected':[874,876,884],'proofScope':'Read actual source algorithm/protocol and full currentAD39. Proofs supplied beyond finite examples; no formal proof assistant/native engine claim.'},'semanticStatus':'complete','contentComparison':judgment,'evidence':[anchor(e,'teaching'),anchor(x,'worked-example-or-algorithm'),anchor(q,'activity'),anchor(a,'answer')],'gaps':[]})
result={'date':'2026-11-05','scope':'Seven exact own-body units for AD39. Otherchapter18unitsnotcredited.','units':rows,'counts':{'assigned':7,'complete':len(rows)},'checks':'qa/lock-full-checks.json finite reference states only'}
(O/'semantic-locks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print('Locksourceunits',len(rows));assert len(rows)==7
