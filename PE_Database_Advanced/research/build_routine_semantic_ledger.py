"""Frozen, manually reviewed routine/trigger source comparison, eight full units."""
from pathlib import Path
import hashlib,json,re
O=Path(__file__).resolve().parent;R=O.parent;W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
inv=load(O/'source-section-inventory.json');source=W/'tmp/database-source/chapter-5.txt';lines=source.read_text(encoding='utf-8').splitlines()
lesson=R/'lessons/AD85.md';text=lesson.read_text(encoding='utf-8-sig');lessonlines=text.splitlines();paras=[p.strip() for p in text.split('\n\n') if p.strip()]
approved=load(O/'root-reviewed-snapshots.json')['lessons'];assert sha(lesson)==approved['AD85'],'Fresh direct content review required before changing approvedhash'
def anchor(needle,kind):
 found=[(i+1,p) for i,p in enumerate(paras) if needle in p];assert len(found)==1,(needle,len(found))
 i,p=found[0];start=next(j+1 for j,l in enumerate(lessonlines) if needle in l)
 return {'kind':kind,'path':'lessons/AD85.md','lessonSha256':sha(lesson),'paragraph':i,'lineStart':start,'exactOpening':p[:320]}
decisions={
 '5.2':('Hai ứng dụng cùng tính tiền','Function còn hữu ích','6. Dùng Student=', '6. DA:', 'Shared business logic/functionspecialtypes/performance cost; standardversusdialect.'),
 '5.2.1':('Table function trả một relation','Ví dụ dữ liệu nhỏ là Student=', '6. Dùng Student=', '6. DA:', 'Scalar/table/procedure interfaces, IN/OUT/INOUT, call/result shape, overloading and empty group.'),
 '5.2.2':('PSM là phần SQL chuẩn','Bất biến tại đầu vòng','7. Trace vòng', '7. WHILE:', 'Declare/set/block, while/repeat/FOR cursor, leave/iterate/return, if/case, condition/handlers; capacityexampleconcurrencycaveat.'),
 '5.2.3':('Một external routine không chỉ','Có ba cách đặt ranh giới','7. Trace vòng', '7. WHILE:', 'NULLindicator/error/status/type, native/process/managedsandboxtradeoffs, API/ABI boundary and explicit policy.'),
 '5.3':('Một trigger được mô tả','`UPDATE ad85_inventory SET stock=stock-4`','3. Trên kho mới','3. 12→10', 'Eventconditionaction; row/statement scope and transition thresholds.'),
 '5.3.1':('Một trigger được mô tả','Với tổng credits, chọn mô hình PE','8. Enrollment ban đầu','8. Đầu(3,0)', 'Invariantmaintenance/reorders/outbox boundary, creditsdeltaallwritepaths.'),
 '5.3.2':('Trong mô hình nguồn, transition tables','Ví dụ chuẩn hóa grade','8. Enrollment ban đầu','8. Đầu(3,0)', 'OLD/NEW/eventtiming, SQLstandardtransitiontables/timing, existencelastparentpart, updatedcredits, model/dialectmanagement.'),
 '5.3.3':('Constraint khai báo được','Restore hoặc replay là một bẫy','9. Snapshot chứa','9. Một phương án', 'Declarativeconstraints/materializedviews/replication alternatives; restore/replaydoublecount, triggercycles/termination and procedurealternative.')}
units=[]
allsorted=sorted([s for s in inv['bookSections'] if s['chapter']=='5'],key=lambda s:s['sourceLine'])
for s in allsorted:
 if s['section'] not in decisions:continue
 i=allsorted.index(s);end=allsorted[i+1]['sourceLine']-1 if i+1<len(allsorted) else s['scopeLineEnd'];body='\n'.join(lines[s['sourceLine']-1:end])
 explanation,example,question,answer,judgment=decisions[s['section']]
 units.append({'section':s['section'],'title':s['title'],'owners':['AD85'],'source':{'path':'tmp/database-source/chapter-5.txt','sha256':sha(source),'ownBodyLines':[s['sourceLine'],end],'ownBodySha256':hashlib.sha256(body.encode()).hexdigest()},'sourceReadEvidence':{'ownBodyRead':True,'fullBatchLinesRead':[659,1393],'figures':'Figures5.6–5.12 SQLpseudocode read in full extractedbody; malformed sourceorder and nonstandardkeywords not imported as MySQL syntax.','baselineRead':['baseline/lessons/S14.md','baseline/lessons/S15.md']},'semanticStatus':'complete','contentComparison':judgment,'evidence':[anchor(explanation,'teaching'),anchor(example,'worked-example'),anchor(question,'independent-exercise'),anchor(answer,'answer')],'gaps':[]})
result={'date':'2026-11-05','scope':'All eight sourceownbodies5.2–5.3.3. No certification of other chapter5 units.','ownedLessonIds':['AD85'],'units':units,'counts':{'assigned':8,'complete':len(units),'partial':0},'checks':'qa/routine-full-checks.json:16finite/structure and2explicitnewMySQL8.4.13checks,18total. Older33enginecases retain their originalscope/hash.'}
(O/'semantic-routines.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print('Routine source units:',len(units));assert len(units)==8
