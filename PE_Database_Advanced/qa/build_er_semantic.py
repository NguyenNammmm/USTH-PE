"""Freeze the manually completed AD09 comparison; anchors are locators, not a semantic test."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'output/database-advanced'
LESSON = BASE / 'lessons/AD09.md'
INVENTORY = BASE / 'research/source-section-inventory.json'

def sha(data):
    return hashlib.sha256(data).hexdigest()

# Each judgment below was authored after directly reading its entire source own
# body, the full current lesson, and the relevant rendered figures. No lexical
# match, parent-section scope, or prior-agent intent supplies completion credit.
# section, explanation paragraph locator, worked/trace locator, activity, judgment
REVIEWS = [
('6.1','Thiết kế khái niệm mô tả','Một quy trình có các đầu ra cần kiểm',5,'The application includes schema, programs, interfaces and authorization; user/domain requirements and separate conceptual/logical/physical outputs are taught and exercised.'),
('6.1.1','Một quy trình có các đầu ra cần kiểm','Ví dụ design alternative:',5,'All phases and their review outputs are compared, including user operations and the greater application impact of logical schema changes. The Course/Offering example connects requirements to phase decisions.'),
('6.1.2','Ví dụ design alternative:','Một trường có khóa học',5,'Both redundancy/inconsistency and incompleteness are demonstrated with original Course/Offering facts; Sale identity is a genuine modeling choice, not a rule that every action must be an entity.'),
('6.2','Entity là một đối tượng','Formally, R⊆',6,'Entity sets, relationship sets, attributes and their conceptual purpose are explained before mapping; formal relationship semantics and original Person/Prereq examples are used.'),
('6.2.1','Entity có thể là người/vật','P1 có thể đồng thời thuộc Student',6,'Concrete/abstract identity, extension versus schema, overlapping sets, values and stable internal identity are explained; equal names do not imply equal entities.'),
('6.2.2','Formally, R⊆','Prereq(C1,C2)',6,'The whole source body was compared: degree/roles, repeated entity sets, descriptive attributes, same-endpoint different predicates, set uniqueness, multiple grades and split diagrams. Recursive here means a relationship role pattern, not a recursive evaluation algorithm.'),
('6.3','Domain là tập giá trị','Composite attribute được tách',6,'Domains, simple/composite hierarchies, zero/one/many values, derived attributes and all three NULL interpretations have original examples and notation. Derived counts may depend on relationships.'),
('6.4','Với R(A,B), 1:1 nghĩa','Ví dụ Advisor có Teacher',7,'All four binary maximum cardinalities and independent minimum participation are explicit; arrows/double lines and source minmax positions are correctly read with a complete valid/invalid instance trace. Nonbinary arrows are qualified.'),
('6.5','Một **superkey**','Với n-ary relationship không có constraint khác',12,'Entity and relationship distinguishability lead to keys; minimality and selection are separated, not inferred from sample uniqueness. Parent introduction only is credited here.'),
('6.5.1','Một **superkey**','Student(id,email,name)',1,'Attribute-based identity, superkey, candidate key and primary key are taught explicitly; sample-only name uniqueness is rejected and natural/surrogate key repair is exercised.'),
('6.5.2','Khóa của relationship phụ thuộc cardinality.','Hai arrow trong R(A,B,C,D)',12,'Full endpoint union is a superkey regardless of descriptive attributes; binary M:N/many-to-one/1:1 keys, repeated-role renaming and nonbinary ambiguity are explained. An original two-row counterexample distinguishes the two multiple-arrow interpretations and their candidate keys.'),
('6.5.3','Dùng Course(course_id,title)','Existence dependence là một quyết định',12,'Weak identity includes owner plus discriminator, total many-to-one identifying participation, no identifying descriptive attributes, notation, other relationships, weak-owner chains and multiple owners. Global surrogate identity does not remove semantic existence dependence.'),
('6.6','Trước hết, chốt identity','Teacher.id unique là identity rule',8,'The conceptual relationship replaces duplicated owner-key attributes, while relational FK columns may reappear after mapping. Multiple affiliations and premature single-department assumptions are addressed; entity and relational views are distinguished.'),
('6.7','Một strong entity với scalar/composite','Có thể mô tả tính đúng của mapping',13,'The own introduction is compared and mapping purpose/constraint preservation is taught through an explicit algorithm and encode/decode correctness argument. Parent coverage does not credit descendants.'),
('6.7.1','1. Với mỗi strong entity','PK strong entity cho song ánh',13,'One entity maps to one row and its entity key becomes the relation PK. The strong Slot registry demonstrates why entity existence must survive even without multivalued rows.'),
('6.7.2','2. Với mỗi multivalued attribute','Ví dụ chạy bước 2:',13,'Composite flattening, computed derived attributes, separate multivalue relations with owner FK/value key, multivalued composite additional FD, and the dropped-key-only-table tradeoff are taught. Keeping zero-value owners and a unique FK target avoids silent loss of facts.'),
('6.7.3','3. Với mỗi weak entity','Mapping MySQL minh họa:',1,'Weak relation includes complete owner key and discriminator, PK/FK constraints and total owner reference; a concrete DDL/fixture shows allowed repeated section_no across owners/terms and rejected nonexistent references. No SQL runtime is claimed.'),
('6.7.4','4. Với mỗi relationship còn lại','Enrollment tham chiếu',13,'Relationship tables contain endpoint keys plus descriptive attributes, role names, PK by cardinality, and endpoint FKs. Advisor and Enrollment give distinct key choices; the Slot FK target limitation is explained rather than following the source typo about sec_course/classroom.'),
('6.7.5','Identifying relationship không cần một bảng riêng','Nếu thay bằng offering_id tự tăng',12,'The identifying relationship is already represented by the weak entity owner-key columns and has no independent descriptive attributes. Duplicating the same mapping is redundant; other relationships of a weak entity are not deleted.'),
('6.7.6','5. Có thể gộp một binary','6. So từng constraint chưa được',13,'Many-to-one merges into the many side with the same entity key, foreign endpoint reference and descriptive columns; partial uses presence via nullable FK, total uses NOT NULL, 1:1 also UNIQUE. The converse state argument and uncovered opposite-side participation are explicit.'),
('6.8','Person có thể specialize','Ví dụ Person1 đồng thời',15,'Extended features are introduced with specialization/generalization/inheritance/aggregation, followed by original examples and reduction choices. The source parent body is only an introduction.'),
('6.8.1','Person có thể specialize','Nhiều specialization có thể cùng tồn tại',15,'Top-down distinctions, repeated specialization, additional attributes/relationships, orthogonal specializations and disjoint/overlap source notation are covered. Group scope prevents falsely making all subtypes disjoint.'),
('6.8.2','Ví dụ đi từ dưới lên:','Teacher(teacher_id,teacher_name',15,'A bottom-up original Teacher/Administrator example unifies common names/identity into Employee. Specialization is the reverse design direction; common versus distinctive features justify whether subtype structure adds meaning.'),
('6.8.3','Inheritance đi qua mọi tầng','Ví dụ TeachingAssistant là subtype',15,'Transitive attribute and relationship-participation inheritance are explicit; single-inheritance hierarchy versus multiple-inheritance lattice is explained and TA shares one Person identity along both paths.'),
('6.8.4','Nhiều specialization có thể cùng tồn tại','Total specialization ảnh hưởng operations:',15,'Completeness is independent of disjointness, giving four combinations. Source total-group labeling and insert/delete consequences are included; subset FKs alone do not enforce union coverage or cross-table disjointness.'),
('6.8.5','Aggregation dùng khi','Assignment chưa được review vẫn là fact',3,'A relationship becomes an endpoint for another relationship; existing assignments without reviews remain representable. Separate endpoint FKs are shown insufficient and a composite reference preserves the precise original relationship instance.'),
('6.8.6','Cách map supertype plus subtype:','Với cách chỉ có subtype tables',15,'The source own introduction to reducing extensions is covered through explicit mappings for subtype and aggregation cases. Introductory completion is not used as descendant evidence.'),
('6.8.6.1','Với cách chỉ có subtype tables','Passport(person_id)',15,'Both source mappings are taught: supertype+subtype keys/FKs, and subtype-only with its total/disjoint conditions. Partial loses unspecialized people, overlap duplicates common attributes, and an ordinary FK cannot reference a UNION. The one-wide-table variant is marked as an additional choice.'),
('6.8.6.2','Aggregation dùng khi','relation Assignment đang có đã đại diện',3,'The aggregation key is the defining relationship key; Review uses it plus manager identity/descriptive data, applies usual relationship PK/FK rules and needs no redundant aggregation table.'),
('6.9','Một tên có thể là attribute','Một lỗi khác là thêm hai scalar',17,'Design decisions depend on real-world semantics rather than one mandatory entity/relationship interpretation. The full own introduction is matched to the alternatives developed below.'),
('6.9.1','Trước hết, chốt identity','Một lỗi khác là thêm hai scalar',17,'All source mistake classes are repaired: conceptual key columns versus relationships, endpoints versus descriptive attributes, single relationship attributes where many assessments are needed, and one authoritative attribute declaration for a split diagram.'),
('6.9.2','Một tên có thể là attribute','Nếu nhiều Person dùng chung một Address',6,'Attribute versus entity is chosen by identity, additional facts and other relationships; scalar, multivalued and shared entity needs are distinguished. The original Address and Assessment examples supply the reasoning rather than copying source phone prose.'),
('6.9.3','Tương tự, có thể thay Enrollment bằng Registration','Registration có identity riêng',14,'Relationship versus registration entity alternatives keep total links to endpoints and retain pair uniqueness when required. Additional lifecycle/relations can justify an entity; adding an ID does not authorize duplicate registrations.'),
('6.9.4','Có một phép đổi khác giữ n-ary facts','Encode ba tuples ở trên thành cases',14,'Pairwise projection is distinguished from a correct intermediary-entity binary representation. The construction, total endpoint links, encode/decode proof, extra uniqueness/FD constraints and clarity/storage tradeoffs are included; independent partial facts can instead favor separate binary relationships.'),
('6.10','Diagram là phương tiện','Bảng dưới chỉ đổi cách ghi',16,'Notation serves communication between domain and modeling experts; source symbols have been inspected visually, and entity/table views plus legend are explicit. No assumption of a universal ER notation is made.'),
('6.10.1','Diagram là phương tiện','Crow\'s-foot dạng endpoint',16,'Oval versus inline attributes, keys, multivalues/derived attributes, arrow/1/*/crow-foot alternatives and specialization symbols are compared. Correct opposite-end versus same-edge cardinality positions are demonstrated with one invariant requirement.'),
('6.10.2','Trong phần UML đối chiếu','UML gọi relationship là association;',16,'Objects/classes/methods/access marks, associations and roles, association classes, n-ary diamonds, opposite-end UML multiplicity, generalization and composition versus UML/ER aggregation are taught. Source simplified notation is presented without asserting obsolete current DBMS/UML limitations.'),
('6.11','Khi phỏng vấn, ghi yêu cầu','Functional requirement gồm operations',8,'The source own introduction says schema is not the entire design; the lesson explicitly adds functional interfaces, authorization, workflow and evolution with original operations and traces.'),
('6.11.1','Functional requirement gồm operations','Ví dụ hỏi ai được sửa course title',5,'Queries/updates/interfaces and who may use them are part of requirements. Database authorization and higher-level function authorization are not reduced to table existence or class access marks.'),
('6.11.2','Functional requirement gồm operations','Trace C7 được submit',8,'Workflow combines business data, tasks and routing across users/applications and may store its own metadata. Original claim transitions include actor permissions, audit/state and forbidden traces.'),
('6.11.3','Schema evolution là thay đổi hợp đồng','Cần phân biệt invariant nhận diện bền',8,'Evolution can affect conceptual/logical/physical levels and application interfaces; stable identity constraints are separated from a changeable one-department policy. Secondary affiliations and several primary affiliations require different changes.'),
('7.8','“Atomic” của 1NF','Ví dụ mã nhân viên CS0042:',9,'Formal 1NF/atomic-domain meaning is explicit; encoded ID parsing, opaque ID use, symmetric set duplication and useful structured-value tradeoffs are covered. Classical atomic/set interpretation is stated rather than making an unqualified JSON claim.'),
('7.9','Schema đầu vào có thể đến','Normal form chưa chọn grain/schema evolution',10,'All three design starting points and the limits of normalization are covered: ER-derived, universal relation, and ad hoc schemas. Logical universal view is not mandated as a physical giant table.'),
('7.9.1','Schema đầu vào có thể đến','Tách multivalued attributes độc lập',9,'ER mapping often separates M:N/multivalue facts, yet residual FD/MVDs require normalization and can reveal conceptual mistakes. Department/address repair, 4NF tendency and universal relation interaction contract are explicit.'),
('7.9.2','Unique-role naming nghĩa','Employee(number) là phone',9,'Unique meaning per attribute name avoids accidental joins of incompatible domains; shared meaning can use common names before generalization. Key-first ordering, role-specific relationship names and consistent singular/plural naming are taught as conventions, not constraints.'),
('7.9.3','Ví dụ denormalization:','Đổi title phải cập nhật cả hai',10,'Original Course/prerequisite copy demonstrates repeated data and update/insert/delete maintenance. Normalized base plus stored result moves maintenance only under a real DBMS contract and still incurs storage/update costs; no unmeasured speedup is asserted.'),
('7.9.4','Normal form chưa chọn grain/schema evolution','Headcount(department,year,count)',10,'BCNF does not reject one-table-per-year or one-column-per-year designs. A next-year insertion and multi-year query exercise shows schema/query churn, while crosstab is retained as a display transformation.'),
('7.10','Trong mô hình valid-time của §7.10','Temporal FK cho phép **union**',11,'The complete source body is matched: time-varying attributes/entities/relationships, non-temporal-first design, half-open intervals/updates, all-snapshot temporal FD, nonoverlap key, union-covering temporal FK, transcript date policy, history limitation, standard period/key notation, exclusion logic and temporal algebra. Bitemporal salary is labeled an original extension of the valid/transaction-time distinction; historical source DBMS support assertions are not repeated as current facts. Coverage pseudocode has an invariant, termination/cost and counterexamples.')
]

def paragraph_witness(lines, locator, low=0, high=None):
    high = len(lines) if high is None else high
    matches = [i for i in range(low, high) if locator in lines[i]]
    if not matches:
        raise ValueError(f'Missing exact locator: {locator!r}')
    i = matches[0]
    a = i
    b = i + 1
    # One numbered item/table row is the precise witness; do not turn every
    # activity into a witness for the entire adjacent list.
    numbered = lines[i].split('. ',1)[0].isdigit()
    if not numbered and not lines[i].startswith('|'):
        while a > low and lines[a-1].strip():
            a -= 1
        while b < high and lines[b].strip():
            b += 1
    paragraph = '\n'.join(lines[a:b])
    return {'path':'output/database-advanced/lessons/AD09.md',
            'lineStart':a+1,'lineEnd':b,'exactParagraph':paragraph,
            'paragraphSha256':sha(paragraph.encode('utf-8')),
            'locator':locator}

def main():
    raw_lesson = LESSON.read_bytes()
    lines = raw_lesson.decode('utf-8-sig').splitlines()
    inventory_raw = INVENTORY.read_bytes()
    inventory = json.loads(inventory_raw)
    validation_path = BASE/'qa/er-full-checks.json'
    validation = json.loads(validation_path.read_text(encoding='utf-8'))
    if not validation['allPassed'] or validation['lessonSha256'] != sha(raw_lesson):
        raise ValueError('Complete semantic freeze requires current approved finite/integrity QA.')
    all_units = inventory['bookSections']
    assigned = [u for u in all_units if 'AD09' in u.get('plannedAdvancedLessonIds',[])]
    assert len(REVIEWS) == len(assigned) == 48
    assert {r[0] for r in REVIEWS} == {u['section'] for u in assigned}
    p_start = lines.index('## Luyện tập') + 1
    p_end = lines.index('## Gợi ý')
    a_start = lines.index('## Đáp án và lập luận') + 1
    a_end = lines.index('Một schema cụ thể cho câu 3 dùng `Person(id PK,name)`, `Student(id PK/FK→Person,program)`, `Employee(id PK/FK→Person,salary)`, `Phone(person_id FK→Person,phone,PK(person_id,phone))`, `Project(project_id PK)`, `Assignment(employee_id FK→Employee,project_id FK→Project,role,PK(employee_id,project_id))` và `Review(manager_id FK→Employee,employee_id,project_id,decision,PK(manager_id,employee_id,project_id),FK(employee_id,project_id)→Assignment)`. Ở đây manager là một Employee và mỗi manager review một Assignment nhiều nhất một lần; nếu cần review lại phải đổi key như đã giải thích. Không có constraint loại overlap hoặc buộc mỗi Person có subtype, nên ba trạng thái Person 1 chưa subtype, Person 2 có cả Student/Employee, Person 2 có hai phone đều được biểu diễn. Subtype trỏ Person không tồn tại bị FK chặn; phone lặp đúng cặp bị PK chặn; review một Assignment chưa có bị FK composite chặn. Nếu thêm quy tắc “manager không review chính mình”, CHECK(manager_id<>employee_id) giữ trường hợp này; nó chưa kiểm manager có quyền trên project đó.')
    units = []
    sources = {}
    for section, explanation, worked, activity, judgment in REVIEWS:
        u = next(u for u in assigned if u['section'] == section)
        source_rel = u['sourcePath'].replace('\\','/')
        if source_rel not in sources:
            data = (ROOT / source_rel).read_bytes()
            sources[source_rel] = (data,data.splitlines(keepends=True))
        data, raw_lines = sources[source_rel]
        start = u['sourceLine']
        following = [x['sourceLine'] for x in all_units if x['chapter']==u['chapter'] and x['sourceLine']>start]
        end = min(following)-1 if following else u['scopeLineEnd']
        body = b''.join(raw_lines[start-1:end])
        row = {
            'section':section,'title':u['title'],'owners':['AD09'],
            'status':'covered-after-fix','semanticStatus':'complete','baselineCreditApplied':False,
            'source':{'path':source_rel,'sha256':sha(data),'rawSha256':sha(data),
                      'ownLineStart':start,'ownLineEnd':end,'ownBodySha256':sha(body),
                      'ownBodyWordCount':len(body.decode('utf-8-sig').split()),
                      'sourcePdfPage':u['sourcePdfPage'],
                      'readInFull':True,
                      'rangePolicy':'Ends before the next numbered inventory heading in this chapter; final own body uses the reviewed pre-Summary boundary.'},
            'lessonSha256':sha(raw_lesson),
            'explanation':paragraph_witness(lines,explanation),
            'workedExampleOrTrace':paragraph_witness(lines,worked),
            'activity':paragraph_witness(lines,f'{activity}. ',p_start,p_end),
            'answer':paragraph_witness(lines,f'{activity}. ',a_start,a_end),
            'semanticJudgment':judgment,
            'algorithmProofAssessment':('Mapping constructor and reverse-state reasoning; keys/cardinality are already supplied.' if section.startswith('6.7') else
              'Temporal coverage scan includes invariant, gap impossibility, termination, complexity and boundary cases; model checks supplement these arguments.' if section=='7.10' else
              'Intermediary entity construction has an encode/decode argument and explicit missing-constraint counterexample.' if section=='6.9.4' else
              'No standalone source algorithm/proof in this own body; definitions and constraints are checked through original examples and answered activities. Lexical algorithm signals are not automatic algorithm requirements.')
        }
        for kind in ('explanation','workedExampleOrTrace','activity','answer'):
            row[kind]['lessonSha256'] = sha(raw_lesson)
            row[kind]['lessonHashPath'] = 'output/database-advanced/lessons/AD09.md'
        units.append(row)
    sheets = [f'tmp/pdfs/er-source/own-contact-{i}.png' for i in range(1,6)] + [f'tmp/pdfs/er-child-source/contact-{i}.png' for i in range(1,5)]
    ledger = {
        'auditType':'Full assigned-source semantic continuation for ER design, mapping and temporal modeling',
        'date':'2026-11-05','scopeLessonIds':['AD09'],'status':'complete','semanticStatus':'complete',
        'scopeNote':'All 48 assigned own bodies directly read in this continuation; complete current AD09 compared and relevant source figures visually inspected. No baseline lesson or prior-agent intent is credited. This ledger covers the book units assigned to AD09; USTH page coverage is coordinated separately by the root audit.',
        'inventorySha256':sha(inventory_raw),
        'sourceBookSha256FromInventory':inventory['sourceBook']['sha256'],
        'lessonSha256':sha(raw_lesson),
        'counts':{'assignedUnits':48,'coveredAfterFix':48,'partial':0,'pending':0,
                  'sourceOwnBodyWords':sum(u['source']['ownBodyWordCount'] for u in units)},
        'readRangesByReviewer':{'reviewer':'er_full_gate_complete',
            'sourceFullContiguousRanges':{'tmp/database-source/chapter-6.txt':[[1,2572]],
                                          'tmp/database-source/chapter-7.txt':[[1823,2268]]},
            'fullLessonRead':'output/database-advanced/lessons/AD09.md',
            'figuresInspected':['6.'+str(i) for i in range(1,29)]+['7.17'],
            'sourcePdfPagesInspected':[275,276,277,279,281,282,283,284,285,289,293,294,298,302,305,306,309,310,311,312,313,315,316,319,377],
            'renderedContactSheets':[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'visuallyInspected':True} for p in sheets]},
        'changesThisContinuation':[
            'Completed strong/weak/relationship mapping algorithm with constructor-level encode/decode argument and precise constraints.',
            'Repaired identifying-relationship descriptive-attribute wording; added weak-owner chains and multi-owner identity.',
            'Added multivalue zero-owner preservation and the dropped-Slot-table FK target tradeoff.',
            'Added multiple-arrow interpretations and original FD/candidate-key counterexample.',
            'Added n-ary reification construction, total endpoint links, uniqueness/FD constraints and inverse proof.',
            'Added assessment modeling repair and aggregation counterexamples without reviews.',
            'Added bottom-up generalization, inherited relationship participation, single/multiple inheritance, orthogonal subtype groups and operation constraints.',
            'Completed both source inheritance mappings, total/disjoint caveats and FK-to-union limitation.',
            'Added full source/Chen/crow-foot/UML notation comparison with multiplicity positions, methods/access marks, association classes and distinct aggregation/composition meanings.',
            'Added explicit 1NF definition, ER/4NF relationship and temporal coverage pseudocode/proof/cost.',
            'Added six original multi-part activities with complete reasoned answers; retained and reviewed all prior current-lesson material.'
        ],
        'sourceCaveats':[
            'Source chapter6 section6.7.4 says sec_course references section and classroom; context/schema show the second target is course. Lesson uses the correct Course FK.',
            'Historical book claims about DBMS temporal support are not presented as current facts; standard-like syntax is explanatory and is not MySQL runner DDL.',
            'Source optional deletion of a key-only relation is explained with its loss-of-zero-values/FK-target tradeoffs; the lesson retains a registry when identity/FK is required.',
            'Bitemporal salary is an original extension; section7.10 mainly teaches valid time and mentions transaction time only briefly.'
        ],
        'validation':{'path':'output/database-advanced/qa/er-full-checks.json',
                      'sqlRuntimeUsed':False,'allPassed':True,'checkCount':len(validation['checks']),
                      'reportSha256':sha(validation_path.read_bytes()),
                      'claimLimit':'Finite model checks verify fixtures/answers and cryptographic freshness; they do not infer semantic completeness or replace full source comparison and universal reasoning.'},
        'units':units
    }
    output = BASE/'research/semantic-er.json'
    output.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'path':str(output),'counts':ledger['counts'],'lessonSha256':ledger['lessonSha256']},ensure_ascii=False))

if __name__=='__main__':
    main()
