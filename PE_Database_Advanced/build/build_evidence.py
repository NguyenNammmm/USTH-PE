"""Produce traceable coverage, integration records and portable selected inputs.

Assignment is never promoted to semantic certification by this script.
"""
from pathlib import Path
import collections,hashlib,json,re,shutil
R=Path(__file__).resolve().parents[1];W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
save=lambda p,x:Path(p).write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding='utf-8')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
proposal=load(R/'research/proposed-lessons.json');inventory=load(R/'research/source-section-inventory.json')
by={x['id']:x for x in proposal['lessons']}
# Correct source ownership from actual subject matter, leaving the audit state separate.
corrections=[]
for s in inventory['bookSections']:
 old=s['plannedAdvancedLessonIds'][:]
 if s['section']=='8.3' or s['section'].startswith('8.3.'):
  s['plannedAdvancedLessonIds']=['AD17','AD69']
 if s['section'] in ['30.4.1','30.4.2']:
  s['plannedAdvancedLessonIds']=['AD68']
 if s['section']=='10.3' or s['section'].startswith('10.3.'):
  s['plannedAdvancedLessonIds']=['AD20']
 if any(s['section']==p or s['section'].startswith(p+'.') for p in ['16.5.1','16.5.2']):
  s['plannedAdvancedLessonIds']=['AD18','AD37']
 if old!=s['plannedAdvancedLessonIds']:corrections.append({'section':s['section'],'before':old,'after':s['plannedAdvancedLessonIds']})
for l in by.values():l['sectionIds']=[]
for s in inventory['bookSections']:
 for lid in s['plannedAdvancedLessonIds']:by[lid]['sectionIds'].append(s['section'])

lab_definitions=[
 ('REPO-H01',['AD42'],'ept/hermitage','mysql84.two-session.innodb','Đọc dữ liệu chưa commit rồi rollback','Hai session và observer; giá trị trước/sau abort cùng trạng thái giao dịch.'),
 ('REPO-H02',['AD42','AD65'],'ept/hermitage','mysql84.two-session.innodb','Snapshot và predicate read','Phân biệt plain consistent read với locking read; reset giữa các isolation.'),
 ('REPO-H03',['AD40','AD41','AD42'],'ept/hermitage','mysql84.two-session.innodb','Mất cập nhật và atomic increment','Đủ precondition cùng đọc giá trị cũ; observer xác nhận lock wait; kiểm post-state.'),
 ('REPO-E01',['AD01','AD30','AD35','AD53'],'jsengun/ecommerce-query-optimizer-demo','mysql84.query.fixture','Oracle phải bắt query trả rỗng và bỏ điều kiện','Exact ID/order, nonempty witness, ba mutant định danh; fixture mới khi tự làm.'),
 ('REPO-E02',['AD30','AD35','AD36','AD37','AD53'],'jsengun/ecommerce-query-optimizer-demo','mysql84.measurement.isolated','Composite index trên cùng hợp đồng kết quả','Query/index/result hash, plan thật, version/configuration; không chấm ngưỡng ms cố định.'),
 ('REPO-C01',['AD01','AD10','AD18','AD60'],'lerocha/chinook-database','mysql84.query.chinook','Đối soát doanh thu theo grain','Decimal oracle, aggregate độc lập, fanout counterexample; ca chuyển giao zero-child.'),
 ('REPO-C02',['AD10','AD53'],'lerocha/chinook-database','mysql84.query.chinook','Running total có peers','InvoiceDate,InvoiceId và frame; fixture đổi tie/insert order; so Decimal từng dòng.'),
]
registry=load(R/'research/repo-registry.json');repos={r['repository']:r for r in registry['repos']}
activities=[]
for id,ids,repo,cap,title,oracle in lab_definitions:
 activities.append({'id':id,'lessonIds':ids,'title':title,'repository':repo,'upstreamCommit':repos[repo]['commit'],'license':repos[repo]['license'],'licenseNotice':'research/licenses/THIRD-PARTY-NOTICES.md','adaptationVersion':'pe-2026-11-05-v1','capabilityId':cap,'contractPath':'docs/repo-labs.md','sourceRegistryPath':'research/repo-registry.json','supportPolicy':'Rotate formats suited to skill; support history retained; support pass is not independent mastery.','independentTask':'Change data/constraints and write or repair the query/schedule on backend engine; submit explanation.','oracle':oracle,'expectedEvidence':['attemptId','activityVersion','fixtureVersion','seed','supportHistory','capabilityVersion','engineArtifactOrExplicitModelMode'],'status':'authored-contract-and-selected-inputs; production-runner-not-deployed'})
for l in by.values():l['repoActivityIds']=[a['id'] for a in activities if l['id'] in a['lessonIds']]
save(R/'activities.json',{'schemaVersion':1,'activities':activities})
save(R/'research/proposed-lessons.json',proposal);save(R/'research/source-section-inventory.json',inventory)
history_path=R/'qa/source-owner-corrections.json'
history=load(history_path).get('corrections',[]) if history_path.exists() else []
# Retain first-pass corrections previously observed in the authoring run.
if not history:
 history=[{'section':s['section'],'before':['AD14'],'after':['AD17','AD69']} for s in inventory['bookSections'] if s['section']=='8.3' or s['section'].startswith('8.3.')]
 history += [{'section':id,'before':['AD16'],'after':['AD68']} for id in ['30.4.1','30.4.2']]
for c in corrections:
 if c not in history:history.append(c)
save(history_path,{'policy':'Actual instructional location; not semantic certification','corrections':history})

# Only an explicitly licensed, selected fixture is redistributed. No book or raw clone.
up=W/'tmp/database-advanced-repos/chinook-database'
source=up/'ChinookDatabase/DataSources/Chinook_MySql.sql'
target=R/'fixtures/chinook_advanced.sql'
original=source.read_text(encoding='utf-8-sig')
assert original.count('`Chinook`')==3
header='-- PE adaptation: database DROP/CREATE/USE directives removed.\n-- Caller must allocate a NEW empty validated sandbox, select it on the connection,\n-- abort on any SQL error, and refuse a pre-existing schema. No reset authority here.\n-- Source commit: '+repos['lerocha/chinook-database']['commit']+'\n-- Author Luis Rocha; MIT grant retained in chinook-MIT.txt. No audio included.\n'
payload=original
for directive in ['DROP DATABASE IF EXISTS `Chinook`;','CREATE DATABASE `Chinook`;','USE `Chinook`;']:
 assert payload.count(directive)==1
 payload=payload.replace(directive,'-- Database management removed by PE; sandbox lifecycle belongs to backend.')
assert not re.search(r'^(?:DROP|CREATE) DATABASE|^USE ',payload,re.M)
target.write_text(header+payload,encoding='utf-8')
shutil.copy2(up/'LICENSE.md',R/'research/licenses/chinook-MIT.txt')
save(R/'fixtures/selected-inputs.json',{'inputs':[{'path':'fixtures/chinook_advanced.sql','sha256':sha(target),'source':'ChinookDatabase/DataSources/Chinook_MySql.sql','upstreamSha256':sha(source),'commit':repos['lerocha/chinook-database']['commit'],'license':'MIT','change':'Upstream database DROP/CREATE/USE removed. Backend must allocate a new empty validated sandbox and select it before loading; abort on any SQL error and refuse existing schema. Table/data payload retained.'}],'otherLabs':'Hermitage schedules and ecommerce PE fixtures/oracles are in repo-labs.md and research/verify_repositories.py; learner never clones upstream.'})

old=load(R/'baseline/manifest.json');oldby={x['id']:x for x in old['lessons']}
rows=['# Bản đồ nguồn, bài nền và bài Advanced','','Bản đồ này giữ cả địa chỉ sách và trang lecture/practice. Có 947 mục/tiểu mục sách, trong đó 746 mục lá; parent và child có thể cùng mô tả một nội dung. Việc có địa chỉ không chứng minh nội dung đã đạt độ sâu tự học. Trạng thái rà được lưu riêng; không tự cấp tín chỉ từ một phép tìm từ khóa.','','Nguồn raw không được phát hành trong gói. `research/source-section-inventory.json` giữ đường dẫn đầu vào, source line, PDF page và hash. Những địa chỉ đó dùng đối chiếu tại workspace biên soạn; người học không cần các đường dẫn D: để mở khóa.','','## Cách đọc quan hệ với 85 bài nền','','Các bài mới là phần học sâu hơn. Khi nguồn nhắc lại nhập môn, người học mở đúng bài nền qua prerequisite; không phải làm lại cả85 bài. Snapshot nền giữ nguyên để truy vết. Một mục sách có thể vừa có kiến thức nền ở bài cũ vừa có thuật toán, phản ví dụ hoặc lab ở bài mới.','','| Bài nền | Tên bài | Bài Advanced dùng làm điều kiện trước |','|---|---|---|']
for lid,l in oldby.items():
 users=[x['id'] for x in by.values() if lid in x['oldPrereqs']]
 rows.append('| '+lid+' | '+l['title']+' | '+(', '.join(users) if users else 'Tra cứu theo chủ đề; không bắt học lại')+' |')
rows+=['','## Lecture và practice USTH','','Địa chỉ dưới đây là ánh xạ chủ đề. Phần rà từng trang vẫn cần bằng chứng ngữ nghĩa và hoạt động tương ứng; không gán nhãn đủ chỉ vì lecture có trong bảng.','','| Nguồn | Trang PDF | Chủ đề nền được khai báo | Phần Advanced đối chiếu |','|---|---|---|---|']
lecture_owner={1:['AD67'],2:['AD01','AD02','AD03'],3:['AD01','AD10'],4:['AD01','AD10'],5:['AD03','AD04','AD05','AD06','AD07','AD08'],6:['AD09','AD59'],7:['AD01','AD12','AD30','AD85'],8:['AD09','AD59','AD60'],9:['AD09','AD11','AD12','AD18','AD19','AD59']}
groups=collections.defaultdict(list)
for p in inventory['lecturePages']+inventory['practicePages']:groups[p['source']].append(p)
page_records=[]
for name,pages in groups.items():
 if name.startswith('Lecture'):ids=lecture_owner[int(re.search(r'Lecture (\d+)',name)[1])]
 else:ids=['AD60','AD85'] if '1.' not in name else ['AD59','AD60']
 declared=sorted({id for p in pages for id in p['declaredOldLessonIds']})
 rows.append('| '+name+' | 1–'+str(len(pages))+' | '+', '.join(declared)+' | '+', '.join(ids)+' |')
 for p in pages:page_records.append({**p,'plannedAdvancedLessonIds':ids,'semanticReviewStatus':'Page-level substantive correspondence not yet independently certified'})
rows+=['','Practice1 có trường EMPLOYEE.Minit. Fixture mới bổ sung nó bằng overlay, giữ sáu primary key và tám foreign key gốc, rồi có một FK mở rộng riêng của PE. Ví dụ Company/Northwind là dữ liệu PE dựng lại; không gọi là đáp án hoặc dump gốc USTH. Các kiểm engine tương ứng nằm trong `qa/apps-mysql-verification.json`.','','## Địa chỉ từng mục sách','','Trong HTML có thể lọc toàn bộ947 địa chỉ và mở bài liên quan. Bảng dưới dùng `sectionIds` chính xác thay cho chỉ đánh dấu một chương lớn. “Đã gán” vẫn là trạng thái cần rà; các lượt source-aware độc lập trong `qa/` chỉ chứng minh phạm vi excerpt được nêu trong từng báo cáo.','','| Mục | Tên trong nguồn | Bài Advanced | Trang PDF nguồn | Trạng thái |','|---|---|---|---|']
for s in inventory['bookSections']:
 rows.append('| '+s['section']+' | '+s['title'].replace('|','/')+' | '+', '.join(s['plannedAdvancedLessonIds'])+' | '+str(s.get('sourcePdfPage') or 'online')+' | Đã gán; xem phạm vi rà nội dung |')
rows+=['','## Cổng xác nhận đủ kiến thức','','Để xác nhận một mục đạt: người rà phải mở nội dung nguồn, chỉ đúng đoạn giảng ở bài, kiểm ví dụ và điều kiện thuật toán/chứng minh khi nguồn có, rồi kiểm bài tập/đáp án. Một source hash, parser hoặc số file không thay được bước này. `manifest.allContentComplete` giữ false cho tới khi có bằng chứng phủ toàn bộ phạm vi.','','Các báo cáo engine, model và render chỉ mang phạm vi riêng của chúng. Việc chưa có PostgreSQL native, crash/cluster runner hoặc pilot không được che bằng output mẫu.']
(R/'docs/coverage-map.md').write_text('\n'.join(rows)+'\n',encoding='utf-8')
save(R/'research/slide-page-map.json',{'scope':'448 lecture +10 practice pages; assignments not semantic certification','pages':page_records})
print(json.dumps({'bookUnits':len(inventory['bookSections']),'slidePages':len(page_records),'activities':len(activities),'selectedFixtureBytes':target.stat().st_size,'ownerCorrections':len(corrections)}))
