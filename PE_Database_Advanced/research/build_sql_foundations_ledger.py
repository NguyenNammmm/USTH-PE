"""Freeze the manual80-unit comparison. No keyword-match certification.

The explicit rows below were written after reading every assigned own-body.
This script only resolves exact current paragraphs and computes reproducible hashes.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'output/database-advanced'
INV=BASE/'research/source-section-inventory.json'
inventory=json.loads(INV.read_text(encoding='utf-8'))
sha=lambda b:hashlib.sha256(b).hexdigest()
lesson_ids=['AD01','AD02','AD10']
md={lid:(BASE/'lessons'/f'{lid}.md').read_text(encoding='utf-8').splitlines() for lid in lesson_ids}
lesson_hashes={lid:sha((BASE/'lessons'/f'{lid}.md').read_bytes()) for lid in lesson_ids}
initial_hashes={'AD01':'b722370a79dad863c60bcf514cbd729167c1ebe2bfa232a0a18c22d0764d58e0','AD02':'a814d10e99c8476e60d15c3216eaf66c21d5263a1559a443ad94b681880ffb65','AD10':'8d20e0bd47fb393645064e1655863b48235ecab8e05837e8ced8ceb4f519a6e0'}
ad85='08108aff10abdac7883d5ad965dfc2d6f3a6ffdf3b9218385d73e3f28d3ea4fe'
assert sha((BASE/'lessons/AD85.md').read_bytes())==ad85

def witness(lid,prefix,kind,heading=None):
    lines=md[lid]; current='';found=[]
    for i,line in enumerate(lines):
        if line.startswith('#'):current=line
        if line.startswith(prefix) and (heading is None or heading==current):found.append((i,current))
    assert len(found)==1,(lid,prefix,heading,found)
    i,current=found[0];j=i
    while j+1<len(lines) and lines[j+1].strip() and not lines[j+1].startswith('#'):j+=1
    fragment='\n'.join(lines[i:j+1])
    return {'kind':kind,'path':f'output/database-advanced/lessons/{lid}.md','sha256':lesson_hashes[lid],
            'heading':current,'line':i+1,'lineRange':[i+1,j+1],'paragraphAnchor':prefix,
            'paragraphExcerpt':fragment,'fragmentSha256':sha(fragment.encode()),'baselineActuallyRead':False}

# section | lesson | teaching paragraph | worked paragraph | exercise |
# actual semantic comparison, including assumptions/dialect corrections
mapping=r'''
2.1|AD01|Relation là|Đây là schema riêng|5|Relation/tuple/attribute/domain, instance, unordered set versus SQL bag, atomicity relative to use and NULL meanings are taught with original Room instances.
2.2|AD01|Relation là|Xét `Room|5|Schema versus changing instance and shared attributes linking relations; multi-column Room/Slot/Meeting schema supplies a non-copied counterpart.
2.3|AD01|Superkey là|Xét `Room|5|Superkey, minimal candidate and chosen primary key; stable identifier design, composite keys, FK versus non-key inclusion dependency, nullability and total-reference assumptions.
2.4|AD01|Xét `Room|Foreign key|5|Underlined PK, referencing-to-referenced arrow direction and composite FK grouping are explained; generic inclusion requirement is distinguished from enforceable composite FK and ER notation.
2.5|AD01|Đại số quan hệ là|Ví dụ tự dựng:|6|Imperative state change, functional algebra and declarative calculus/SQL distinctions are explained through temporary expression composition rather than a syntax-only recap.
2.6|AD01|Đại số quan hệ là|Ví dụ tự dựng:|6|Algebra closure, unary/binary operations and formal set semantics versus SQL bag are explained; all child operators receive separate comparisons.
2.6.1|AD01|\u007c `σ_p(R)`|Ví dụ tự dựng:|6|Selection predicates and conjunction/disjunction/negation/comparable fields, with D1/building A selected before join; SQL WHERE correspondence is explicit.
2.6.2|AD01|\u007c `π_A(R)`|Ví dụ tự dựng:|6|Projection schema and duplicate elimination, basic versus generalized projection, and SQL bag projection are contrasted on pay60,90,90.
2.6.3|AD01|Đại số quan hệ là|Ví dụ tự dựng:|6|Composability follows relation-valued outputs; X then Y then name projection supplies concrete intermediate states.
2.6.4|AD01|\u007c `R×S`|Bộ đánh giá mô hình|6|Concatenated tuple product, qualified duplicate names, product cardinality and exhaustive finite nested-loop semantics are taught, with3-by2 producing6.
2.6.5|AD01|\u007c `R ⋈_θ S`|Ví dụ tự dựng:|6|Theta join equals selection over product; equality predicate retains related pairs only, with schema naming and missing unjoined rows explicit.
2.6.6|AD01|\u007c `R∪S`|Cho A(x)|8|Union/intersection/directed difference require compatible arity/domains; original multiset example also contrasts set and ALL meanings.
2.6.7|AD01|\u007c `T ← E`|Ví dụ tự dựng:|6|Temporary assignment names intermediate relations without displaying/mutating persistent data or adding expressive power.
2.6.8|AD01|Để tìm nhân viên|Để tìm nhân viên|6|Rename relation/attribute and two aliases for self-join, including reference-salary restriction and projected schema; positional naming is replaced by readable explicit names.
2.6.9|AD01|Quy tắc bag có thể|Một điều kiện là null-rejecting|4|Inner selection-pushdown preserves value and multiplicity under attribute-local predicate; outer-join rewrite requires explicit null-rejection and counterexample testing is not proof.
3.1|AD01|Đây là schema riêng|Đây là schema riêng|5|SQL parts DDL/DML/integrity/views/authorization/transaction/program embedding and dialect dependence are explained. Historical version sequence is context, not a current feature oracle.
3.2|AD01|Đây là schema riêng|Xét `Room|5|DDL defines schema, types and constraints and affects stored objects; original two-table PK/FK DDL is supplied with index/security/storage separated conceptually.
3.2.1|AD01|`INT/SMALLINT`|`INT/SMALLINT`|5|Integer bounds, fixed decimal precision/scale versus float, CHAR/VARCHAR, nullability and Unicode/collation sensitivity are explained with exact decimal fit/non-fit examples.
3.2.2|AD01|Foreign key|Đây là schema riêng|5|CREATE initially-empty tables, composite PK/FK/NOT NULL with explicit referenced columns, rejected missing parent and DELETE versus DROP/ALTER are covered.
3.3|AD01|Bộ đánh giá mô hình|Ví dụ tự dựng:|6|SELECT-FROM-WHERE relational result is defined through product/filter/projection; output schema and engine optimization are separated.
3.3.1|AD01|Quy tắc bag có thể|Ví dụ tự dựng:|6|SQL duplicate retention, DISTINCT, projected arithmetic versus stored update and Boolean row predicates are grounded in original Emp/Room data.
3.3.2|AD01|Bộ đánh giá mô hình|Bộ đánh giá mô hình|6|Qualified field names, multi-table matching and finite nested-loop product semantics/cardinality are explained with an explicit correctness argument; no physical-plan claim.
3.4|AD01|Chuỗi SQL dùng|Để tìm nhân viên|7|Rename, strings, attribute selection, ordering and predicates are introduced as contract-sensitive operations, with individual subsections audited separately.
3.4.1|AD01|Để tìm nhân viên|Để tìm nhân viên|6|Output aliases and relation aliases/self-join separate roles of one table; alias does not create persistent copies.
3.4.2|AD01|Chuỗi SQL dùng|Chuỗi SQL dùng|7|Quoted literal escaping, concatenation/case/substring/length/trim, LIKE percent/underscore/explicit escape and collation sensitivity are covered with MySQL-specific CONCAT.
3.4.3|AD01|Để tìm nhân viên|Để tìm nhân viên|6|SELECT star versus alias-star and explicit column projection, preserving two role IDs versus selected schema and migration impact.
3.4.4|AD01|`ORDER BY pay|`ORDER BY pay|7|Ascending/descending multi-key ordering, absent-order non-guarantee and deterministic top-k ties are taught; output order differs from index/insert order.
3.4.5|AD01|`BETWEEN lo|`BETWEEN lo|7|Inclusive BETWEEN, row equality and lexicographic comparison; original tuple1,100 versus2,0 corrects the source's inconsistent componentwise explanation using official MySQL reference.
3.5|AD01|Hai nhánh UNION|Cho A(x)|8|Compatible output arity/types/meanings, set DISTINCT defaults and ALL counts, NULL duplicate comparison and current MySQL8.4 support are explained.
3.5.1|AD01|Cho A(x)|Cho A(x)|8|UNION versus UNION ALL multiplicities m+n, original a/b/c/NULL example, output column names and overall ORDER BY contract.
3.5.2|AD01|Cho A(x)|Cho A(x)|8|INTERSECT DISTINCT versus min(m,n) ALL, original duplicate/NULL values, historical MySQL omission explicitly corrected for8.4.
3.5.3|AD01|Cho A(x)|Cho A(x)|8|EXCEPT set difference versus max(m-n,0) ALL, directed behavior and prior DISTINCT changing meaning; current engine support differs from2019 footnote.
3.6|AD01|Phép so trùng|`NOT U=U`|8|NULL arithmetic, IS NULL, three-valued AND/OR/NOT, WHERE TRUE-only and different DISTINCT/set-operation duplicate treatment are taught with explicit truth cases.
3.9|AD01|INSERT phải|UPDATE có cùng|10|DML is a transition of an instance under schema constraints, distinct from querying and from arbitrary procedural row order.
3.9.1|AD01|DELETE chọn|DELETE chọn|10|Whole-row deletion, omitted-WHERE meaning and initial-instance subquery selection, illustrated by20/40/100 below-average IDs; MySQL target-read restrictions acknowledged.
3.9.2|AD01|INSERT phải|INSERT phải|10|Column mapping, domains/arity/default/NULL, INSERT SELECT finite source and PK violation, self-insert3-to6 and bulk-upload web counterpart are explained.
3.9.3|AD01|UPDATE có cùng|UPDATE có cùng|10|One statement versus two threshold updates, first-TRUE CASE, NULL branch behavior, scalar SET and explicit COALESCE policy are worked through98-to102.90 versus105.99.
4.1|AD01|NATURAL JOIN so|NATURAL JOIN so|9|Join expressions produce relations, common names and original cross-department example motivate explicit join conditions.
4.1.1|AD01|NATURAL JOIN so|NATURAL JOIN so|9|Natural equality on every common attribute, single common output column, schema-evolution risk and USING subset condition are taught and tested by Student1/D1 taking CourseC2/D2.
4.1.2|AD01|NATURAL JOIN so|Để tìm nhân viên|9|ON admits arbitrary predicate and distinct qualified output columns; its placement differs from WHERE for outer joins, explained in original zero-paid-child case.
4.1.3|AD01|LEFT giữ mọi|Kết quả bag là|9|Matched then null-extension algorithm, left/right/full, real NULL versus unmatched, correct bag-preserving MySQL FULL reconstruction and ON/WHERE distinction receive examples/proof.
4.1.4|AD01|Kết quả bag là|Kết quả bag là|9|Join type preserves sides while condition syntax selects matches: independent axes; default INNER versus natural/USING/ON and unsupported MySQL FULL spelling are separated.
4.2|AD01|View lưu định nghĩa|Ví dụ `CREATE VIEW d1_staff|12|Virtual user interface/security projection and reusable business definitions, view versus CTE persistence and base-data changes are taught; base privileges remain material.
4.2.1|AD01|View lưu định nghĩa|Ví dụ `CREATE VIEW d1_staff|12|CREATE VIEW stores a named query until dropped, hides projected pay only through interface, and is distinguished from cached stored results.
4.2.2|AD01|View lưu định nghĩa|Ví dụ `CREATE VIEW d1_staff|12|Query through nested views can substitute definitions while preserving schema/filters; optimizer realization is not mandatory, and dependencies/base changes affect result validity.
4.2.3|AD01|Materialized view lưu|Materialized view lưu|12|Stored results, immediate/lazy/periodic maintenance and staleness/storage/write costs, original sum150-to180 and AVG sum/count example; no native MySQL materialized-view claim.
4.2.4|AD01|Ví dụ `CREATE VIEW d1_staff|Để thấy vấn đề ngược|12|Updateability versus insertability, hidden mandatory columns, ambiguous aggregate/join inverse updates and CHECK OPTION are explained; exact engine rules differ from textbook sufficient criteria.
4.3|AD01|Với Account|SELECT trước ROLLBACK|11|Explicit transaction boundary, commit/rollback/atomic transfer, autocommit, statement-versus-transaction failure, non-reversible commit and MySQL DDL implicit commits are covered.
4.6|AD01|Index giúp|`CREATE UNIQUE INDEX|13|Physical auxiliary search key versus logical candidate key, index storage/write cost and optimizer choice; CREATE/DROP MySQL syntax and UNIQUE constraints/NULL are distinguished.
3.7|AD10|Aggregate nhận|Aggregate nhận|5|Five aggregate families and collection-to-value meaning, numeric versus ordered inputs, GROUP BY versus window are explained with Measure.
3.7.1|AD10|Aggregate nhận|Aggregate nhận|5|Duplicate-sensitive SUM/AVG and COUNT star/column/distinct, original same-value events and NULL inputs, rather than keyword-only coverage.
3.7.2|AD10|Một cột không aggregate|Expected là (A,3|5|Grouping key equalities/NULL, one row per group and grouping versus global empty-input behavior; functional-dependency/ONLY_FULL_GROUP_BY nuance included.
3.7.3|AD10|WHERE lọc|WHERE lọc|5|HAVING group condition after WHERE and aggregate, logical pipeline versus plan, extended gamma representation and original COUNT threshold counterexample.
3.7.4|AD10|Expected là (A,3|Aggregate nhận|5|Null ignoring/count exceptions, empty collections and NULL group equality; standard Boolean aggregate mention separated from MySQL policy and quantified SOME.
3.8|AD10|Một subquery trả|Một subquery trả|6|Subquery result remains relational; use context imposes membership/quantifier/cardinality and correlation scope requirements.
3.8.1|AD10|`IN` tương đương|`IN` tương đương|6|IN/NOT IN with scalar and composite rows, =ANY versus <>ALL, projection duplicates and NULL trap; complete section keys are required.
3.8.2|AD10|Ví dụ x=10|Ví dụ x=10|6|ANY/SOME/ALL semantics including empty input and NULL, <>SOME counterexample and why MAX or NOT EXISTS rewrites need assumptions.
3.8.3|AD10|Một subquery trả|“Đã hoàn thành mọi môn|6|EXISTS nonemptiness, correlated alias scope/shadowing, double NOT EXISTS for containment and semijoin/antijoin bag grain are covered.
3.8.4|AD10|Predicate UNIQUE|Predicate UNIQUE|7|UNIQUE query predicate versus constraint/COUNT and DISTINCT, vacuous empty case, multiple different rows and NULL equality caveat; MySQL-compatible explicit check supplied.
3.8.5|AD10|Derived table trong|LATERAL cho phép|8|FROM subquery relation composition, aliases/named aggregate columns, nested max-of-sums and LATERAL same-FROM dependency plus left-retained zero-child example.
3.8.6|AD10|Derived table trong|Derived table trong|8|CTE statement-local name, dependent definitions/reuse and no forced physical materialization, illustrated by grouped sums then max.
3.8.7|AD10|Scalar subquery dùng|Scalar subquery dùng|8|One-column cardinality0/1/>1 rules, correlated COUNT guarantee, empty aggregate versus zero-row subquery and runtime errors; no LIMIT workaround hiding non-uniqueness.
3.8.8|AD10|MySQL cho phép SELECT|MySQL cho phép SELECT|8|Scalar calculation without FROM, ratio with zero-child denominator, NULLIF zero policy, MySQL slash versus DIV rather than generic integer-division assumption.
5.4|AD10|Ví dụ reach ban đầu|Ví dụ reach ban đầu|9|Direct/indirect dependency and hierarchy reachability, positive closure versus reflexive reach from a start and original cycle behavior are taught.
5.4.1|AD10|Thuật toán tổng quát|Mô hình reachability đã|4|Accumulated/frontier/next iteration, subtract visited before reuse, cycle-safe termination, per-session state and BFS cost/invariant are supplied without unsupported stored-function syntax.
5.4.2|AD10|Từ R0=E|Ví dụ reach ban đầu|9|Anchor/recursive union, fixpoint and leastness, monotonicity/restrictions, finite state requirement, positive all-pairs closure and difference counterexample with proof.
5.5|AD10|ROLLUP(item,color)|Với scores theo thứ tự|12|Advanced aggregate roles separated: ranking/partition/window, pivot shape and multiple grouping levels; each child has independent worked evidence.
5.5.1|AD10|Với partition có n|Với scores theo thứ tự|10|Ties/rank/dense/row_number, partition/top-n, percent/cume/ntile, null placement and sort-scan versus quadratic correlated count with correctness invariant. Singleton MySQL0 checked in official8.4 implementation.
5.5.2|AD10|ROWS BETWEEN|RANGE dựa giá trị|11|Partition versus overlapping frames, ROWS/RANGE and peers, missing dates, preceding/following/boundaries and correction that3 PRECEDING includes current plus3 are worked explicitly.
5.5.3|AD10|Pivot chuyển|Expected Book|12|Pivot attribute values become columns, retained grain and aggregate cell collisions, missing-cell NULL versus0, fixed label domain and MySQL conditional aggregation example.
5.5.4|AD10|ROLLUP(item,color)|Expected theo nội dung|12|Rollup prefixes/cube subsets/grouping sets and product of grouping choices, GROUPING flags distinguish stored NULL, UNION ALL masks preserve levels; MySQL implementation separated from standard syntax.
27.1|AD02|Trong tuple relational calculus|Với s=(1)|1|Declarative result predicate over tuples with explicit output schema/set semantics, contrasted with algorithmic algebra and SQL bag.
27.1.1|AD02|Sinh viên đạt yêu cầu|Đây là dạng|4|Projection/existential joins, OR/AND/difference, universal implication and empty required-set behavior are covered by original Student/Passed/Required examples and exercises.
27.1.2|AD02|Một atom của tuple calculus|Trong logic hai giá trị|5|Free/bound variables, relation/field/constant atoms, comparable domains, formula constructors, scope/alpha-renaming and three logic equivalences are explicit.
27.1.3|AD02|Gọi `dom(P)`|Xét biểu thức một cột|2|dom includes relation values and constants; unsafe complement can return outside/infinite domain; safe finite output and practical sufficient restriction versus semantic definition are distinguished.
27.2|AD02|Trong domain calculus|Trong domain calculus|3|Domain variables bind individual attribute values rather than tuple objects; arity/type-bound membership and close relationship to tuple calculus are explained; QBE historical connection is not a learner prerequisite.
27.2.1|AD02|Nếu quan hệ Student thực tế|Trong domain calculus|3|Ordered domain-variable output, exact relational atom arity, comparison/Boolean/quantifier constructors and free-variable scope, including expanded Student id/name example.
27.2.2|AD02|Tuple calculus và domain calculus|Trong domain calculus|3|Packing/unpacking tuple fields into domain variables preserves membership and existential/universal conditions; explicit every-required and DB-not-OS queries have answers and SQL.
27.2.3|AD02|Safety của domain calculus|Với domain calculus, cần|8|All three safety conditions including internal existential witness and universal domain sufficiency, output-bounded-but-unsafe counterexample and guarded Need reformulation are explained.
27.3|AD02|Trong fragment an toàn|6. Đặt D=π_id|6|Basic algebra/safe tuple/safe domain expressive equivalence, exclusion of generalized arithmetic/aggregate, structural translation for explicitly bounded fragment and explicit limit that full general theorem is stated not proved by source.
'''
manual={}
for row in mapping.strip().splitlines():
    sec,lid,teach,example,exercise,comparison=row.split('|',5)
    assert sec not in manual
    manual[sec]=(lid,teach.replace(r'\u007c','|'),example.replace(r'\u007c','|'),int(exercise),comparison)

proofs={
 '2.6.4':('AD01','Bộ đánh giá mô hình'),
 '2.6.5':('AD01','Quy tắc bag có thể'),
 '2.6.9':('AD01','Quy trình dừng khi'),
 '3.3.2':('AD01','Bộ đánh giá mô hình'),
 '4.1.3':('AD01','Kết quả bag là'),
 '5.4.1':('AD10','Bất biến: sau k vòng'),
 '5.4.2':('AD10','Từ R0=E'),
 '5.5.1':('AD10','Với partition có n'),
 '5.5.4':('AD10','Để thêm grouping(color)'),
 '27.1.2':('AD02','Trong logic hai giá trị'),
 '27.3':('AD02','Trong một fragment đã được'),
}
algorithm_sections={'3.3.2','4.1.3','5.4.1','5.4.2','5.5.1','5.5.4'}
sources={}
units=[]
for u in inventory['bookSections']:
    if not set(u['plannedAdvancedLessonIds'])&set(lesson_ids):continue
    sec=u['section'];lid,teach,example,n,comparison=manual[sec]
    sp=u['sourcePath'].replace('\\','/');p=ROOT/sp
    if sp not in sources:sources[sp]=(p.read_text(encoding='utf-8').splitlines(),sha(p.read_bytes()))
    lines,source_sha=sources[sp];start=u['sourceLine']
    next_lines=[x['sourceLine'] for x in inventory['bookSections'] if x['sourcePath']==u['sourcePath'] and x['sourceLine']>start]
    end=min(next_lines)-1 if next_lines else u['scopeLineEnd']
    body='\n'.join(lines[start-1:end]);scope='\n'.join(lines[start-1:u['scopeLineEnd']])
    evidence=[witness(lid,teach,'teaching'),witness(lid,example,'worked-example'),
              witness(lid,f'{n}.','activity','## Luyện tập'),witness(lid,f'{n}.','answer-rubric','## Đáp án và lập luận')]
    proof=[witness(*proofs[sec],'algorithm-proof')] if sec in proofs else []
    units.append({'section':sec,'title':u['title'],'owners':[lid],
       'source':{'path':sp,'sha256':source_sha,'ownBodyLines':[start,end],'scopeLines':[start,u['scopeLineEnd']],
                 'ownBodySha256':sha(body.encode()),'scopeSha256':sha(scope.encode()),'hashNormalization':'UTF-8 LF-joined splitlines, no terminal LF'},
       'sourceReadStatus':'full-assigned-own-body-read','semanticStatus':'complete','baselineCreditApplied':False,
       'semanticComparison':comparison,'evidence':evidence,'algorithmProofEvidence':proof,
       'sourceAlgorithmProofReview':{'inventoryAlgorithmSignals':u['algorithmSignals'],'inventoryProofSignals':u['proofSignals'],
          'sourceAlgorithmPresent':sec in algorithm_sections,'formalSourceProofPresent':False,
          'conclusion':('Explicit counterpart algorithm/invariant/proof is witnessed; source has operational explanation rather than a full formal theorem proof.' if proof else 'Full own-body read contains definitions/examples/semantics rather than an additional formal source proof. Concrete teaching, worked input/output and practice/answer witnesses are supplied; no keyword-match proof credit.' )},
       'pending':[]})
assert len(units)==len(manual)==80

read_ranges={'tmp/database-source/chapter-2.txt':[[22,1791]],'tmp/database-source/chapter-3.txt':[[17,2450]],
 'tmp/database-source/chapter-4.txt':[[8,1718],[2549,2623]],'tmp/database-source/chapter-5.txt':[[1393,2485]],'tmp/database-source/online-27.txt':[[16,404]]}
for u in units:
    lo,hi=u['source']['ownBodyLines']
    assert any(a<=lo and hi<=b for a,b in read_ranges[u['source']['path']]),u['section']
pdfpath=Path(inventory['sourceBook']['path'])
pdfsha=sha(pdfpath.read_bytes());assert pdfsha==inventory['sourceBook']['sha256']
figure_notes={76:'Figure2.9 visually checked: underlined composite PK and arrows from referencing to referenced; special slot inclusion is distinct from FK.',
242:'Figure5.13 visually checked: prerequisite pairs include both direct and multi-hop paths, with same destination reachable through different paths.',
244:'Figure5.14 algorithm visually checked: accumulated/frontier/temp tables, subtract accumulated, replace frontier, clear temp and stop on empty frontier.',
246:'Figure5.16 recursive SQL visually checked: anchor edge relation plus recursive composition by intermediate endpoint, UNION and fixpoint explanation.',
253:'Printedpage224 window exposition visually checked against prior code: three preceding rows plus current is four; own lesson states correction and explicit examples.',
259:'Printedpage230 visually checked: product of two rollups generates six groupings, selected grouping sets and GROUPING distinguish generated NULL.'}
figure_review=[]
for n,note in figure_notes.items():
    im=ROOT/f'tmp/database-source/sql-foundations-figures/book-{n}.png'
    figure_review.append({'sourcePdf':str(pdfpath),'sourcePdfSha256':pdfsha,'pdfPage':n,
      'renderedPath':str(im.relative_to(ROOT)).replace('\\','/'),'renderedSha256':sha(im.read_bytes()),'visuallyInspected':True,'semanticObservation':note})
ledger={'date':'2026-11-05','scope':'Full80 assigned own-body source units for AD01/AD02/AD10, with manual semantic comparison and exact current MD witnesses. No baseline lesson credit; other lessons, manifest, build and PDF are not authored here.',
 'ownedLessonIds':lesson_ids,'inventorySha256':sha(INV.read_bytes()),'initialLessonHashes':initial_hashes,'lessonHashes':lesson_hashes,
 'sourceHashes':{sp:v[1] for sp,v in sources.items()},
 'readBatches':[{'id':sp.rsplit('/',1)[-1]+'-full-assigned-own-body','sourcePath':sp,'sourceSha256':sources[sp][1],
   'readLineRanges':ranges,'baselineRead':[],'baselineCreditApplied':False,'readMethod':'Full displayed text read; any truncated middle was requested again in bounded ranges. Parent introductions read only to next numbered heading for own-body accounting, not credited by descendant scope.'} for sp,ranges in read_ranges.items()],
 'figureReview':figure_review,
 'primaryEngineDefinitionReview':[{'url':'https://dev.mysql.com/doc/refman/8.4/en/comparison-operators.html','observation':'Lexicographic row comparison and NULL-safe equality checked; source componentwise explanation corrected.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/set-operations.html','observation':'MySQL8.4 supports UNION/INTERSECT/EXCEPT; source2019 footnotes do not describe this runner.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/with.html','observation':'Recursive UNION DISTINCT permitted; recursive SELECT DISTINCT/window/aggregate/group/order restricted; anchor determines types.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/window-functions-frames.html','observation':'Current-row inclusion, ROWS/RANGE/default frame and boundary semantics checked.'},
 {'url':'https://raw.githubusercontent.com/mysql/mysql-server/8.4/sql/item_sum.cc','observation':'Item_percent_rank::val_real at inspected web lines4652-4674 returns0 for rank1, including singleton; source code review is not engine execution.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/view-updatability.html','observation':'Updateability differs from insertability and textbook simplified sufficient rule; aggregate/group/union restrictions checked.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/view-check-option.html','observation':'Check-option blocks writes making view predicate not TRUE.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/faqs-views.html','observation':'No native materialized-view object in MySQL8.4.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html','observation':'DDL implicit commit and temporary-table creation rollback exception checked.'},
 {'url':'https://dev.mysql.com/doc/refman/8.4/en/lateral-derived-tables.html','observation':'Same-FROM preceding-table dependencies and permitted lateral join forms checked.'}],
 'validation':{'script':'output/database-advanced/research/check_sql_foundations.py','report':'output/database-advanced/research/semantic-sql-foundations-checks.json','mysqlExecuted':False},
 'units':units,'totals':{'assignedUnits':80,'fullyReadOwnBodies':80,'manualSemanticComplete':80,'pendingSourceUnits':0,'baselineCredits':0},
 'status':'complete-source-semantic-comparison-with-runtime-limitations',
 'remainingGaps':['MySQL runtime acceptance remains pending: this environment has no running MySQL. Portable SQLite/model checks are labeled and cannot establish MySQL-specific DDL, transaction, view, scalar-cardinality-error, LATERAL, ROLLUP or collation behavior.','This ledger covers only80 assigned book units; it does not assert the full947-unit book and all slide pages are complete.'],
 'frozen':{'AD85':{'path':'output/database-advanced/lessons/AD85.md','initialSha256':ad85,'currentSha256':sha((BASE/'lessons/AD85.md').read_bytes()),'unchanged':True}},
 'regeneration':'Root owner must regenerate aggregate MD/PDF/HTML after merging all semantic shards. This agent edited no shared build/manifest/publication files.'}
dest=BASE/'research/semantic-sql-foundations.json';dest.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'ledger':str(dest),'units':len(units),'lessonHashes':lesson_hashes},ensure_ascii=False))
