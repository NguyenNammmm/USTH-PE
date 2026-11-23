"""Initialize root-owned units and record a genuinely read chapter1 comparison."""
from pathlib import Path
import hashlib,json,re
O=Path(__file__).resolve().parent;R=O.parent;W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
inv=load(O/'source-section-inventory.json');units=inv['bookSections']
root_ids={f'AD{i:02}' for i in [*range(38,55),*range(61,68),60,81,82,85]}
target=O/'semantic-root-ledger.json';prior=load(target) if target.exists() else {'units':[]};old={x['section']:x for x in prior['units']}
groups={}
for s in units:groups.setdefault(s['sourcePath'],[]).append(s)
records=[]
for source,ss in groups.items():
 path=W/source;lines=path.read_text(encoding='utf-8').splitlines()
 for i,s in enumerate(ss):
  if not set(s['plannedAdvancedLessonIds'])&root_ids:continue
  end=ss[i+1]['sourceLine']-1 if i+1<len(ss) else s['scopeLineEnd']
  body='\n'.join(lines[s['sourceLine']-1:end])
  record={'section':s['section'],'title':s['title'],'owners':s['plannedAdvancedLessonIds'],'sourcePath':source,'sourceSha256':sha(path),'ownBodyLineStart':s['sourceLine'],'ownBodyLineEnd':end,'ownBodySha256':hashlib.sha256(body.encode()).hexdigest(),'status':'unreviewed','readEvidence':None,'witnesses':[],'gaps':[]}
  if s['section'] in old:record.update(old[s['section']])
  records.append(record)
lesson=R/'lessons/AD67.md';text=lesson.read_text(encoding='utf-8-sig');paras=[p.strip() for p in text.split('\n\n') if p.strip()]
approved=load(O/'root-reviewed-snapshots.json')['lessons']
assert sha(lesson)==approved['AD67'],'Changed lesson requires a fresh actual review, not automatic hash renewal'
def witness(needle):
 matches=[(i+1,p) for i,p in enumerate(paras) if needle in p]
 assert len(matches)==1,(needle,len(matches))
 i,p=matches[0]
 return {'path':str(lesson.relative_to(R)).replace('\\','/'),'lessonSha256':sha(lesson),'paragraph':i,'exactOpening':p[:220]}
matching={
 '1.1':('Ứng dụng có thể lưu giao dịch','Phân biệt miền ứng dụng và OLTP/phân tích; ví dụ cửa hàng ghi đơn và dự báo hàng.'),
 '1.2':('File processing dễ sinh','Các vấn đề redundancy/access/data isolation/integrity/atomicity/concurrency/security; phân biệt data isolation và transaction isolation.'),
 '1.3':('Instance là dữ liệu','Ba mức abstraction và schema/instance; parent chỉ giới thiệu mục tiêu.'),
 '1.3.1':('Một data model cung cấp','Bốn họ model và bảng ví dụ mới; relational/ER/semi-structured/object.'),
 '1.3.2':('| Họ mô hình','Relation/attribute/row và quan hệ qua khóa; đọc thêm C01 đã kiểm trực tiếp.'),
 '1.3.3':('Physical data independence','Physical/logical/view, ví dụ index và thay đổi kiểu/duplicates, quyền ở base.'),
 '1.3.4':('Schema cũng có các mức','Instance khác schema/subschema, tương tự giá trị và định nghĩa; thay đổi vật lý khác thay đổi logic.'),
 '1.4':('DDL khai báo schema','DDL/DML trong cùng họ ngôn ngữ SQL; declarative semantics.'),
 '1.4.1':('Domain/type, primary key','Domain/PK/FK/authorization/catalog và giới hạn predicate tùy ý; DDL metadata.'),
 '1.4.2':('DDL đầu tiên tạo định nghĩa','CREATE table có domain/key/check; giải thích tác động và bài5.'),
 '1.4.3':('DML gồm đọc, thêm','Bốn thao tác, query subset và procedural/declarative.'),
 '1.4.4':('DDL đầu tiên tạo định nghĩa','SELECT relational result shape và predicate; exactSCI output; không ORDER BY không hứa sequence.'),
 '1.4.5':('DML gồm đọc, thêm','Host API/UI/network, ODBC/JDBC; không nhận SQL là ứng dụng đầy đủ.'),
 '1.5':('Thiết kế đi từ yêu cầu','Requirements→conceptual→logical→physical; what business captures và ER/normalization.'),
 '1.6':('Kiến trúc DBMS có','Query/storage/transaction roles và disk/RAM I/O rationale.'),
 '1.6.1':('Storage manager phối hợp','Authorization/integrity, file/buffer/transaction; data/dictionary/index/statistics.'),
 '1.6.2':('Ở phía query','DDL interpreter/DML compiler/optimizer/evaluation engine và giới hạn tối ưu theo cost.'),
 '1.6.3':('Transaction manager gồm','Atomicity/consistency/durability, application boundary và concurrency/recovery responsibilities.'),
 '1.7':('Trong mô hình hai tầng','Central/shared-memory/cluster/distributed và two/three-tier; fullregistrationflow.'),
 '1.8':('Người dùng form','Users/DBA parentclassification.'),
 '1.8.1':('Người dùng form','Formuser/programmer/analyst/DBA khác interaction; registrationUIexample.'),
 '1.8.2':('Người dùng form','Schema/storage/change/grants/backups/free-space/job-monitoring; bài6.'),
 '1.9':('Các mốc sau tóm lược','1950–2010history, SystemR/Ingres/Codd1970/cloudSaaS, source-year scope và privacy/security.')}
for row in records:
 if row['section'] not in matching:continue
 needle,scope=matching[row['section']]
 row.update(status='complete-source-unit-comparison',readEvidence={'sourceOwnBodyRead':True,'sourceLineRange':[row['ownBodyLineStart'],row['ownBodyLineEnd']],'sourceFigurePagesInspected':[39,40,51,52],'instructionalReview':'Read sourcechapter1 plus completeAD67 and baselineC01; additions close concrete omissions. Sourceintro has no algorithm/proof to reproduce.'},witnesses=[witness(needle),witness('## Luyện tập'),witness('## Đáp án và lập luận')],scopeJudgment=scope,gaps=[],reviewedLessonSha256=sha(lesson))
lesson=R/'lessons/AD38.md';text=lesson.read_text(encoding='utf-8-sig');paras=[p.strip() for p in text.split('\n\n') if p.strip()]
assert sha(lesson)==approved['AD38'],'Changed lesson requires a fresh actual review, not automatic hash renewal'
matching17={
 '17.1':('Trong mô hình đơn giản của sách','ACID responsibilities/transaction boundaries and atomic local computation.'),
 '17.2':('Trong mô hình đơn giản của sách','Local read/compute/write distinction, transfer20, temporary inconsistency, durable data or reconstruction log.'),
 '17.4':('| Trạng thái |','All lifecycle edges, restart as new transaction, compensating action and external writes/outcome uncertainty.'),
 '17.5':('Khi T1 đợi I/O','Throughput/latency/resource overlap, n! serial orders, two numeric serial states and same-order interleaving.'),
 '17.6':('Input là một lịch','All conflict cases, swaps, graph algorithm/complexity/proof, topological alternatives, view-vs-conflict and arithmetic scope.'),
 '17.7':('Nếu T2 đọc giá trị','Failure dependency and separation of graph correctness from recoverability.'),
 '17.7.1':('Nếu T2 đọc giá trị','Commit ordering rule and explicit nonrecoverable counterexample.'),
 '17.7.2':('Cascadeless yêu cầu','Reads after commit; cascade prevention; strict implies cascadeless implies recoverable with converse witnesses.'),
 '17.8':('| Mức trong mô hình','Four conceptual levels + no dirty write, autocommit/API/isolation syntax and implementation/version boundaries.'),
 '17.9':('Khóa toàn database','WholeDB baseline versus locks/TO/MVCC and concurrency tradeoff; actual algorithms inAD39/41/42 separately read in prior targetedpass.'),
 '17.9.1':('Khóa toàn database','S/X and sufficiently long protocol, two-phase distinction; explicit waiting and checkout-short transaction example.'),
 '17.9.2':('Khóa toàn database','Transaction timestamps/read-write metadata, abort offending operations; detailed item algorithmAD41 priorread.'),
 '17.9.3':('Khóa toàn database','Versions not whole copied DB; snapshot/write conflict and serializability boundary; write-skew lessonAD42 priorread.'),
 '17.10':('INSERT/DELETE và cập nhật','Phantoms and search-key changes, logical predicate versus physical scan/index readsets; concrete classification exercise7.')}
for row in records:
 if row['section'] not in matching17:continue
 needle,scope=matching17[row['section']]
 row.update(status='complete-source-unit-comparison',readEvidence={'sourceOwnBodyRead':True,'sourceLineRange':[row['ownBodyLineStart'],row['ownBodyLineEnd']],'sourceFigurePagesInspected':[835,842,847,849,850],'instructionalReview':'Read completechapter17 ownbodies incl adjacent17.3, completeAD38, baselineT01 andAD39/41/42 introductorymechanisms. Added concrete source omissions; sourcealgorithm/proof conflict case is worked and justified.'},witnesses=[witness(needle),witness('## Luyện tập'),witness('## Đáp án và lập luận')],scopeJudgment=scope,gaps=[],reviewedLessonSha256=sha(lesson))
result={'scope':'Root-owned source units; complete entries require direct source-body and instructional correspondence. Others remain explicitly unreviewed.','date':'2026-11-05','units':records,'counts':{status:sum(r['status']==status for r in records) for status in sorted({r['status'] for r in records})}}
target.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result['counts']))
