"""Record actual source/current-lesson review for the 107 Lecture 6/7 pages.
Mappings are manual judgments; text extraction and hashes give no semantic credit.
"""
from pathlib import Path
import hashlib
import json
import unicodedata
from pypdf import PdfReader

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
read = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest = lambda s: hashlib.sha256(s.encode()).hexdigest()
approved = read(O/'root-reviewed-snapshots.json')['lessons']
texts = {}
for name in ['USTH06','USTH07']:
    assert sha(R/'lessons'/f'{name}.md') == approved[name], 'Source/current MD rereview required before changing approved hashes'
    texts[name] = (R/'lessons'/f'{name}.md').read_text(encoding='utf-8-sig').splitlines()

def witness(name, needle, kind, heading=None):
    lines = texts[name]
    hits = []
    current = ''
    excluded = ['## Luyện tập','## Đáp án và lập luận','## Gợi ý','## Biến thể và cách kiểm','## Học trên web','## Nguồn và đối chiếu']
    for i,line in enumerate(lines):
        if line.startswith('## '):
            current = line
        if heading:
            if current == heading and line.startswith(needle):
                hits.append(i)
        elif needle in line and current not in excluded:
            hits.append(i)
    assert len(hits) == 1, (name,needle,hits)
    a = b = hits[0]
    while a > 0 and lines[a-1].strip():
        a -= 1
    while b+1 < len(lines) and lines[b+1].strip():
        b += 1
    fragment = '\n'.join(lines[a:b+1])
    return {'kind':kind,'path':f'lessons/{name}.md','lessonSha256':approved[name],
            'lineRange':[a+1,b+1],'paragraphExcerpt':fragment,'fragmentSha256':digest(fragment),'baselineActuallyRead':False}

# Each tuple names a teaching paragraph, a worked example/counterexample, an
# answered task, and the substantive comparison made after reading the source.
groups = {
 'workflow':('USTH06','Quy trình trong slide','Lan có thể dùng',1,'Ideas/high-level/schema/DBMS stages, ERD versus UML scope, and requirements ambiguity before keys; new context and answered identification/design question.'),
 'entity':('USTH06','Entity là một đối tượng','Trong ký pháp của Lecture 6',1,'Entity/entity set/attribute distinctions, simple-domain assumption and rectangle/oval/diamond notation with original typed examples; class analogy limited.'),
 'relationship':('USTH06','Một relationship set','Quan hệ cùng nối một cặp',1,'Relationship roles and tuple meaning, multiple relationships between identical sets retain distinct meanings; original Permission rows.'),
 'ternary':('USTH06','Chiếu Permission thành','Với dữ liệu {(Lan,A,M1)',2,'Ternary relationship cannot generally be replaced by binary projections; explicit three-row spurious tuple, table/key and stronger FD variant.'),
 'card':('USTH06','Mũi tên thường','Many–many: một Member',3,'Many/many-one/one-one maximums, zero participation and rounded exactly-one arrows, asymmetric mandatory Maker/optional Device; multiway determinant is all other roles together.'),
 'price':('USTH06','Slide 26–27 nêu','Quote(room,device,price)',4,'Relationship attribute depends on pair, current/history grain; converting price to value entity preserves functional arrow/equality/currency and does not silently add new participation constraints.'),
 'roles':('USTH06','Mentors nối Member','Một thiết kế lưu cặp không thứ tự',5,'Recursive role labels preserve direction; directed mentoring distinguished from symmetric/canonical friendship; same endpoints/FKs do not enforce symmetry or cross-role partnership policy.'),
 'isa':('USTH06','Camera là subclass','Slide dùng cây isa',6,'Subclass shares inherited identity, attributes and relationships; subset not necessarily strictly smaller, source tree/no-multiple-inheritance assumption explicitly scoped.'),
 'keys':('USTH06','Key có thể composite','Course(dept,number,hours,room)',7,'Underlined root/composite keys and inherited identity preserved; source alternate hours/room key requires business assumption, not inference from one sample.'),
 'weak':('USTH06','Port(port_number,label)','Weak entity có thể liên hệ',7,'Weak identification includes owner plus partial key, mandatory supporting arrow and double symbols; not every relationship supports key; global IDs and dependence do not make every entity weak.'),
 'design':('USTH06','Nếu chỉ lưu tên Maker','Maker.address lặp',8,'All three design heuristics explained with original lifecycle/update/delete anomalies, entity-versus-attribute choice and limits of overusing weak entities.'),
 'redundancy':('USTH06','Maker.address lặp','Trong conceptual ERD',8,'Redundant conceptual facts and repeated manufacturer address cause inconsistency/loss; physical FK encoding a relationship is distinguished from duplicate independent facts.'),
 'entityattr':('USTH06','Nếu chỉ lưu tên Maker','Nếu cần địa chỉ',8,'Source nonkey/many heuristic explained but not asserted as universal theorem; independent catalog lifecycle/validation may justify key-only entity.'),
 'account':('USTH06','Slide52 có yêu cầu','Nếu cho joint ownership',10,'Source account exercise fully answered for both single owner and customer(s) wording; source rounded-arrow answer conflicts with joint ownership. Keys/FKs/parent existence check and assumption explicit.'),
 'mapping':('USTH06','Entity set thành bảng','| Member dùng nhiều Device',9,'Entity/attribute/relationship mapping includes composite role keys and relationship attributes; explicit Uses/Favorite/StoredAt/Mentors/weak examples with PK/FK/NULL/UNIQUE semantics.'),
 'merge':('USTH06','Không merge Member với Uses','Many–one có thể merge',9,'Many-one FK merge respects optionality, many-many merge duplicates facts/loss of nonparticipants; constraint consequences and answered transfer task.'),
 'weakmap':('USTH06','Owner FK đã nằm trong key Port','Nếu supporting relationship có attribute',7,'Full weak key retained, identifying relation is redundant; source unless-attributes shortcut qualified because a one-occurrence relationship attribute can merge into weak row.'),
 'submap':('USTH06','Với nhiều subclass overlap','| E/R style',6,'All three subclass mappings show same original entities, inherited attributes and query tradeoffs; concrete combinations, identity, discriminator/unknown NULL and source space generalization corrected.'),
 'indexwhy':('USTH07','Index có thể chứa','CREATE INDEX u7_price_ix',2,'Index search purpose, single/composite keys, actual CREATE/EXPLAIN example and distinction between index creation, plan selection and measured speed.'),
 'linear':('USTH07','Nếu dò một danh sách','trung bình là (1+2+',1,'Uniform successful linear-search assumption, (n+1)/2 and worst n count inspections rather than milliseconds; absent key scan scoped.'),
 'binary':('USTH07','Với danh sách đã sắp xếp','Trung bình là 84/22',1,'Source noninteger exact-comparison formulas corrected by full n22 binary-search depth distribution and explicit mid-floor algorithm; log growth separated from exact counts.'),
 'btree':('USTH07','B-tree/B+ tree','Một node chứa nhiều key',2,'Source root/intermediate/leaf figures read, range navigation and multiway fanout distinct from binary array search; AD28 extension linked without using its source assignment as proof.'),
 'locator':('USTH07','Index có thể chứa','Với InnoDB, clustered index',2,'Source row ordinal locator is simplified; InnoDB clustered leaf rows/secondary PK locator and one clustered tree/fallback choice explicit, output order still requires ORDER BY.'),
 'types':('USTH07','Các tên `ntext`','Với MySQL, phải kiểm',2,'SQL Server LOB/MAX datatype restrictions labeled dialect-specific rather than mechanically transferred to MySQL; type/key-length/prefix/index method qualifications.'),
 'cost':('USTH07','Index cần chỗ lưu','10,000 key, mỗi key 8 byte',2,'Payload estimate versus actual index size, maintenance cost and workload-based selection; duplicates not blanket useless and many indexes not automatically optimal.'),
 'view':('USTH07','Kết quả là `(501,70)`','CREATE VIEW u7_sales',3,'Virtual view from base queries, definitions versus transient result and transaction semantics; actual sales fixture/output, not materialized fixed report.'),
 'viewpros':('USTH07','View giúp rút gọn','Một view có thể dựa',3,'Query simplification, computed columns, schema compatibility and permission-dependent filtering, dependencies/performance tradeoffs; original nested/subquery views have exact outputs.'),
 'algorithm':('USTH07','MySQL có `ALGORITHM=MERGE`','TEMPTABLE dùng kết quả tạm',4,'MERGE/TEMPTABLE/UNDEFINED mechanisms, blocking constructs and blanket subquery ban qualified; temporary execution result not persistent materialized view.'),
 'viewexamples':('USTH07','View thứ nhất cho','CREATE VIEW u7_above_average',3,'Computed sales aggregation, view-on-view and above-average subquery rewritten on new fixture; NULL AVG and final ORDER BY semantics explained.'),
 'updatable':('USTH07','View có aggregate','Một số inner-join view',4,'Row correspondence and aggregate non-updatability, expression columns versus other base columns, join exceptions and insertability distinct from metadata flag.'),
 'checkopt':('USTH07','`INSERT INTO u7_hue_customers',"WHERE city='Hue'",4,'WITH CHECK OPTION allows visible writes/rejects hidden inserted/updated rows; direct base write and nested LOCAL/CASCADED distinctions; named native error cases passed.'),
 'manage':('USTH07','Để quản lý, dùng','SELECT table_name,is_updatable',4,'SHOW CREATE/ALTER/OR REPLACE/DROP VIEW and schema-filtered information_schema query, distinct from permissions/insertability guarantees.'),
 'proc':('USTH07','Procedure lưu định nghĩa','CREATE PROCEDURE u7_count_city',5,'Stored catalog program/input/output/resultset, city count fixture with exact IN/OUT same-connection calls; MySQL AS typo corrected, delimiter client versus server split explicit.'),
 'cache':('USTH07','Procedure có thể giảm','Sơ đồ “SQL thường luôn compile lại',6,'Reuse/roundtrip/rights benefits and maintenance/CPU costs, cached prepared SQL and metadata reparsing invalidate source always-compile/never-compile comparison.'),
 'tsqlproc':('USTH07','Ở nhánh SQL Server',"EXEC dbo.pe_find @min_id=2, @city=N'Hue';",6,'CREATE OR ALTER/@param/AS/EXEC/default/named/positional concepts labeled SQL Server; system/local/master convention scoped and sp_ prefix not self-created system status.'),
 'trigger':('USTH07','Trigger được gắn','| MySQL |',7,'Automatic table event/timing and trigger object distinct from explicit CALL; row versus statement scope and OLD/NEW versus transition rowsets spelled out.'),
 'triggeruses':('USTH07','Ứng dụng trigger gồm','Trigger làm việc trong transaction',10,'Audit/derived-data/validation/default/cascade motivations, declarative constraints preferred when sufficient; cross-database/concurrency guarantee not automatic and extra work/locks matter.'),
 'limit':('USTH07','Bài ở slide 39','CREATE OR ALTER TRIGGER dbo.pe_limit_update',9,'Source asked >2 UPDATE task answered with SQL Server transition COUNT and rollback semantics; 0/1/2/3 affected rows and no-value-change cases, not fake translation to row counter.'),
 'stock':('USTH07','Thêm hai dòng mới','CREATE OR ALTER TRIGGER dbo.pe_take_stock',7,'Original MySQL row-trigger stock result and SQL Server grouped SUM for duplicate product batch; source single-row example limitation, positive qty/FK/check and failed statement state scoped.'),
 'audit':('USTH07','`<=>` là phép so bằng','CREATE TRIGGER u7_audit_price',8,'Original audit DDL/body, exact old/new NULL cases and stable key join for SQL Server rowsets; source <> NULL omission repaired with named native checks.'),
 'integrity':('USTH07','Slide 42 còn dùng','Nếu chỉ cần chặn xóa sản phẩm',10,'Scalar deleted subquery multirow failure, set-based EXISTS alternative and native FK choice, AFTER ordering/concurrency limits; source cache shortcut not a performance proof.'),
}
L6 = {2:'workflow',3:'workflow',5:'entity',6:'workflow',7:'entity',8:'entity',9:'entity',10:'relationship',11:'relationship',12:'ternary',13:'ternary',14:'ternary',15:'card',16:'card',17:'card',18:'card',19:'card',20:'card',21:'card',22:'card',23:'card',24:'price',25:'price',26:'price',27:'price',28:'roles',29:'roles',30:'roles',31:'isa',32:'isa',33:'isa',34:'isa',35:'keys',36:'keys',37:'keys',38:'weak',39:'weak',40:'weak',41:'weak',42:'design',43:'redundancy',44:'redundancy',45:'redundancy',46:'redundancy',47:'entityattr',48:'entityattr',49:'entityattr',50:'entityattr',51:'weak',52:'account',53:'mapping',54:'mapping',55:'mapping',56:'merge',57:'merge',58:'weakmap',59:'weakmap',60:'submap',61:'submap',62:'submap',63:'submap',64:'submap'}
L7 = {4:'indexwhy',5:'linear',6:'binary',7:'locator',8:'types',9:'cost',10:'btree',11:'btree',12:'locator',13:'locator',14:'cost',16:'view',17:'view',18:'viewpros',19:'algorithm',20:'viewexamples',21:'updatable',22:'checkopt',23:'manage',25:'proc',26:'cache',27:'tsqlproc',28:'cache',29:'tsqlproc',30:'tsqlproc',31:'cache',32:'proc',33:'proc',35:'trigger',36:'trigger',37:'trigger',38:'triggeruses',39:'limit',40:'stock',41:'audit',42:'integrity',43:'triggeruses'}
inventory = read(O/'slide-page-map.json')['pages']
pages = []
for lecture,mapping,basename in [(6,L6,'Lecture 6 ERD.pdf'),(7,L7,'Lecture 7 View-SP-Ix.pdf')]:
    assigned = [row for row in inventory if row['source'] == basename]
    path = Path(assigned[0]['sourcePath'])
    reader = PdfReader(path)
    sourcehash = sha(path)
    for source in assigned:
        n = source['pdfPage']
        raw = reader.pages[n-1].extract_text()
        rendered = f'tmp/database-source/slides-lecture67/L{lecture}-page-{n:02}.png'
        row = {'source':{'path':str(path),'sha256':sourcehash,'pdfPage':n,
               'pageTextSha256':digest(unicodedata.normalize('NFKC',raw).replace('\u00ad','').strip()),
               'normalization':'pypdfextract_text,NFKC,removeU+00AD,strip,UTF8SHA256'},
               'sourceReadStatus':'Every page body read in full; all 11 L6 and 8 L7 six-page contact sheets visually inspected; selected arrow/key/mapping/Account and index figures also inspected at full size.',
               'observedContent':raw[:1000],'pendingGaps':[],'baselineCreditApplied':False,
               'sourceFiguresRead':[{'renderedPath':rendered,'renderedSha256':sha(W/rendered),
                 'visuallyInspected':True,'inspectionMode':'Six-page contact sheet; full extracted text read separately.'}],
               'engineEvidence':'qa/usth-lecture67-checks.json: 41 named checks including 15 actual MySQL 8.4.13 cases, selected actual SQLite reads and finite ER/search oracles; no SQL Server execution.'}
        if n not in mapping:
            row.update(status='non-instructional',semanticComparison='Cover/agenda/objectives/section divider only; substantive topics reviewed on following teaching pages.',evidence=[],practiceCoverage='not-applicable-non-instructional')
        else:
            name,teaching,example,q,judgment = groups[mapping[n]]
            row.update(status='complete-current-evidence',semanticComparison=judgment,
              evidence=[witness(name,teaching,'teaching'),witness(name,example,'worked-example-or-counterexample'),
                witness(name,f'{q}.','activity','## Luyện tập'),witness(name,f'{q}.','answer-rubric','## Đáp án và lập luận')],
              practiceCoverage='Original/equivalent skill task answered; source Account ownership ambiguity and UPDATE >2 task explicitly resolved. Not keyword/source-address credit.')
        pages.append(row)
assert len(pages) == 107
assert sum(row['status']=='complete-current-evidence' for row in pages) == 99
out = {'date':'2026-11-06','scope':'Manual full-body/figure/current-MD comparison of all 64 Lecture6 and 43 Lecture7 pages. Excludes Lecture8/9 and Practice1/2/3 until separately reviewed.',
       'pages':pages,'counts':{'complete-current-evidence':99,'non-instructional':8},
       'sourceErrata':['Account customer(s) versus exactly-one diagram; both stated variants kept.',
          'E/R hours-room key, subclass strictness, entity heuristics and storage savings require assumptions.',
          'Binary-search exact comparison counts and ordinal-row locator simplified in source.',
          'MySQL and SQL Server procedure/trigger syntax and row-versus-statement scope are distinct.',
          'MySQL AS typo, blanket view subquery ban, never-recompile, stock multirow join, NULL audit and scalar deleted example repaired.'],
       'checks':'qa/usth-lecture67-checks.json: 41 named checks; 256 finite ternary relations, 27 subtype cases, actual SQLite and 15 actual MySQL checks. No SQL Server runtime.'}
(O/'semantic-slides-lecture67-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(pages),'complete':99,'nonInstructional':8}))
