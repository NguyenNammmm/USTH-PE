"""Freeze manually reviewed source/body correspondence; do not infer coverage from keywords.

The needles below locate already selected semantic witnesses in the reviewed text.
They are not a classifier, and a successful lookup does not establish adequacy.
"""
from pathlib import Path
import hashlib
import json

COURSE = Path(__file__).resolve().parents[1]
WORK = COURSE.parents[1]
RESEARCH = COURSE/'research'
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
owned = {'AD15','AD20','AD21','AD22','AD35','AD36','AD37','AD61','AD73'}
texts = {n:[p.strip() for p in (COURSE/'lessons'/f'{n}.md').read_text(encoding='utf-8').split('\n\n') if p.strip()]
         for n in owned}
hashes = {n:sha(COURSE/'lessons'/f'{n}.md') for n in owned}


def anchor(name, needle, kind):
    found = [(i+1,p) for i,p in enumerate(texts[name]) if needle in p]
    assert len(found)==1,(name,needle,len(found))
    i,p = found[0]
    return {'path':f'lessons/{name}.md','lessonSha256':hashes[name],
            'kind':kind,'paragraph':i,'exactOpening':p[:500]}


# section | lesson | teaching witness | concrete example/algorithm | activity | answer | manual comparison
DATA = '''
8.4|AD15|Spatial query thường có hai pha|Vùng phục vụ là tam giác|1. Vẽ tam giác|1. (9,9):|Geographic versus Euclidean geometry, filter/refine contract and a false-positive/boundary example.
8.4.1|AD15|Một segment chỉ cần hai endpoints|Polygon có thể lưu vòng vertices|5. Lưu rectangle|5. Hai triangle|Ordered vertices, curve approximation, normalized segment/triangle representation, collections and 3D faces/tetrahedra; shared-boundary identity accounted for.
8.4.2|AD15|Trong 3D, point thêm z|constraint như “hai ống|8. Region quadtree có|8. Không: giải nén|CAD partial-object access, component relationships, solid union/intersection/difference and collision constraints require exact 3D geometry.
8.4.3|AD15|GIS gắn geometry với vị trí|Bản đồ utilities còn phải|8. Region quadtree có|8. Không: giải nén|Geography combines spatial location with elevation, land use, rainfall and ownership; utility projection versus real 3D collision distinguished.
8.4.3.1|AD15|GIS gắn geometry với vị trí|Hai roads giao nhau trên hình|7. Shops A distance1|7. Sai: trả rỗng|Navigation and underground utility applications use connectivity/elevation, not merely planar overlap; constrained nearest-query example supplied.
8.4.3.2|AD15|Raster là array pixels/cells|Topographic surface có thể lưu|6. TIN triangle có|6. Tại x=1|Raster georeference/resolution/tiles, vector tradeoffs, TIN interpolation and bottom-to-top map layers explained with calculations.
8.4.4|AD15|Spatial join nối hai tập|Nearest-neighbor search dùng lower bound|4. Tự làm: thiết kế nearest|4. Distances5|Region, nearness, nearest neighbor, road paths, spatial joins and combined business predicates; valid lower-bound stopping and ties.
24.4|AD15|Partition-based tree có thể cắt|Spatial join nối hai tập|5. Lưu rectangle|5. Hai triangle|Partition splits replicate object pieces; R-tree stores one object entry with overlapping grouping bounds; query identity/dedup semantics retained.
24.4.1|AD15|PR quadtree (point-region|Raster 2×2 có các hàng|2. Trace quadtree|2. Chia root|PR buckets versus homogeneous raster region leaves, insertion/search invariants, duplicate stopping and lossless raster example.
24.4.2|AD15|Quadratic split ở §24.4.2|Trace M=3|3. Debug R-tree|3. Nếu geometry đúng|Search all overlapping children; distinguish textbook insertion heuristic; complete quadratic split with minimum occupancy, deletion and bound invariants.
10.1|AD73|Volume là dung lượng|Một triệu files mỗi file|5.100impressions|5.8%|Volume/velocity/variety linked to parallel workload requirements rather than a fixed size threshold; tiny-file metadata example.
10.1.1|AD73|Web/app interactions có thể dùng|click-through rate=8/100|5.100impressions|5.8%|Web/app, transaction, sensor, network and social sources connected to uses and precise click/conversion denominators.
10.1.2|AD73|Có hai kiểu workload|Newsfeed minh họa hai cách|5.100impressions|5.8%|Short key-based transactions versus long analytics/code operators; application join replaced by read fanout or materialized write fanout with costs.
10.2|AD73|Parallel database còn có query operators|DFS không tự cung cấp relational|4. Tự làm: thiết kế storage|4. Rubric: tách file|DFS, application sharding, managed key-value/document storage and parallel DB responsibilities separated; mixed-workload design activity.
10.2.1|AD73|DFS giữ namespace/directories|Model trace: `/logs/day1`|6. Cell(u7, dept|6. Latest=AI|Filename-to-ordered-block and block-to-location metadata, NameNode/DataNode paths, write placement and API/mount abstraction; assembly order and failures.
10.2.2|AD73|Chọn customer_id giúp|Orders có keys1..8|2. So hash/range|2. Hash hợp key|Range/hash sharding, client routing and cross-shard work, skew, rebalancing, replica failures and ownership cutover responsibilities.
10.2.3|AD73|Một document collection có thể giữ|Bigtable-style model phân biệt|8. Collection có ba students|8. Find mọi document|GET/PUT plus document CRUD and internal identity; sorted wide-column prefix/JSON path/version encodings, including delimiter and latest/snapshot examples.
10.2.4|AD73|Parallel DB hỗ trợ operators|Restart toàn query có thể đủ|4. Tự làm: thiết kế storage|4. Rubric: tách file|Parallel DB interface/operators distinguished from storage API; longer/larger jobs encounter more failures, with query restart versus finer retry overhead.
10.2.5|AD73|Network partition là hai nhóm|Một lập luận bất khả thi nhỏ|7. Viết hai lịch|7. B thấy state|Atomic multi-shard update versus replica consistency, majority conditions, partition indistinguishability proof, divergence reconciliation, replicas and cache races.
10.3|AD20|Input là một multiset records|Ba documents:|1. Trace map/shuffle|1. Local counts|Map emits key/value occurrences, shuffle groups equal keys and reduce computes each group under an explicit snapshot/equality contract.
10.3.1|AD20|Ngoài map và reduce|Một kho log lớn được chia|1. Trace map/shuffle|1. Local counts|Framework centralizes task scheduling, routing, parallel input/output and recovery plumbing while application retains function/key/state correctness obligations.
10.3.2|AD20|Bất biến của map|map(docId,text)|1. Trace map/shuffle|1. Local counts|Full occurrence-based word count, grouping and sum proof; tokenizer, duplicates, finite input and shuffle costs identified.
10.3.3|AD20|Log fixture mới gồm|Mapper parse vàfilter|7. Tính log bytes|7. Tháng1/slides|Parse/filter/log-key/reduce pipeline has a concrete half-open date fixture; access-count versus byte-sum metric differs explicitly.
10.3.4|AD20|Trong mô hình Hadoop của nguồn|Ví dụ hai map tasks|5. Trace intermediate partition|5. Reducer0 thiếu C|Map-local partition files fetched from all maps, reduce-group merge, parallel I/O, skew and local-intermediate loss traced concretely.
10.3.5|AD20|Hadoop Java API trong nguồn|Job:|6. Với lines=|6. Map=|Four-parameter Mapper/Reducer contract, offset and wrapper types, context/Iterable, driver registrations, input/output formats, compression, combining and multijob materialization.
10.3.6|AD20|Selection chỉ cần map filter|R có (k=A|3. Thêm S=|3. r1s1|Selection, grouping and tagged equijoin implemented by map/reduce, with complete cross-product proof; SQL-on-files compiler and semantics described.
10.4|AD20|Algebraic framework cho phép|Một query SQL thường có nhiều|7. Tính log bytes|7. Tháng1/slides|General complex-record algebraic operators avoid repeatedly encoding joins via map/reduce and expose DAG implementation choices.
10.4.1|AD20|Algebraic framework cho phép|DAG cho phép một output|7. Tính log bytes|7. Tháng1/slides|Unary/multiple-input operators cover database and machine-learning tasks, with low-level Tez versus application-oriented Spark context.
10.4.2|AD20|RDD là collection records|Dataset có schema với named|6. Với lines=|6. Map=|Concrete map/flatMap/pair/reduce dataflow, lazy actions/collect/save, schema and typed Dataset/Row representations, lineage and partition costs.
10.5|AD21|Stream có thể không kết thúc|Count toàn lịch sử có thể phát|3. Thiết kế replay test|3. Sink effect đã commit|Unbounded input lacks a final total; continuous updates and finite windows define when useful outputs can be produced.
10.5.1|AD21|Các ứng dụng streaming có deadlines|Gộp packets thành flow totals|4. Tự làm: viết brief stream|4. Rubric: gán time|Trading, e-commerce, sensor, network and social workloads need different latency/grain contracts; finite event/flow and CEP cases illustrate this.
10.5.2|AD21|Continuous query coi stream|Sách §10.5.2 còn có complex|3. Thiết kế replay test|3. Sink effect đã commit|Four query approaches, punctuations versus heuristic watermark, unbounded/final distinction, CEP state and lambda dual-path correction/duplication risks.
10.5.2.1|AD21|Stream SQL cần tách window|Hopping windows width10|1. Gán năm events|1. Tumbling totals|Tumbling/hopping/sliding/session definitions, boundary arithmetic, stream-to-relation and output timestamps, temporal relation joins and bounded stream joins.
10.5.3|AD21|Publish-subscribe biểu diễn graph|Retention giữ data trong một khoảng|5. Viết danh sách edges|5. Edges là|Static DAG/source/operator/sink routing and topic/subscription equivalent traced; fanout, retention/replay and discretized versus direct stream processing distinguished.
10.6|AD22|Sách §10.6 phân biệt|Fixture có Student=|5. Trên fixture Student|5. t1 ghép|Typed relational graph and identity, directed/variable-length patterns, join/group bindings, iterative joins versus BSP, supersteps/messages/vote-halt and graph operator APIs.
16.1|AD35|Một cây logic ghi|Ví dụ bảng Employee|5. Với `filter R.keep|5. Có thể push|Logical rewrite, physical operator annotations, pipelined/materialized coordination and cost estimation are interleaved; accidental natural-join columns avoided.
16.2|AD35|Theo §16.2, optimizer|Nếu predicate p chỉ dùng|5. Với `filter R.keep|5. Có thể push|Equivalence quantified over every legal instance and correct set/bag/output-schema semantics, separate from low estimate cost.
16.2.1|AD35|Các ký hiệu dưới đây dùng|Projection không tùy ý phân phối|7. R(A, B)=|7. R−S=R|All source rule families and guards taught with tuple-membership proofs, projection/outer-join counterexamples and null-rejecting replacement.
16.2.2|AD35|Hai chuỗi rewrite có thể|Ví dụ R(id, keep)|5. Với `filter R.keep|5. Có thể push|Selection decomposition/push and projection column retention shown as rewrite chains; derivable rule versus minimal rule set and duplicate derivations explained.
16.2.3|AD35|Ví dụ bảng Employee|Nối Assignment với Project trước|5. Với `filter R.keep|5. Có thể push|Join associativity/commutativity permit different intermediate sizes; selective join versus large prior join and cross-product risk tied to concrete fixture.
16.2.4|AD35|Bất biến: mọi biểu thức seen|seen = {syntax_key|5. Với `filter R.keep|5. Có thể push|Full worklist applies rules at every subtree, dedups, shares expressions and reaches closure only under a finite grammar; heuristic/budget limits explicit.
16.3|AD35|Estimate distinct sau filter/join|Ví dụ V(A, R)=100|6. V(A, R)=80|6. Estimate min(80,25)|Intermediate statistics propagated bottom-up, with cardinality and distinct errors influencing higher costs; approximate statistics remain distinct from constraints.
16.3.1|AD35|Catalog còn giữ lR|Một bucket có n_b|8. Page hữu dụng|8. f=floor|Catalog row/page/tuple/blocking/index statistics, collection lag/sampling, equi-width/depth and frequent-value histogram use with explicit calculations.
16.3.2|AD35|Với range A≤v|Với k predicates độc lập|1. R có 20.000|1. Estimate 100|Equality/range/histogram/unknown-bound estimates and AND/OR/NOT formulas include distribution, independence and SQL UNKNOWN assumptions and counterexamples.
16.3.3|AD35|Một FK non-NULL|fR = frequency|3. Rkey=|3. Key 1 tạo|Unique/FK join bounds, uniform/domain-containment formula, histogram buckets and exact frequency-product oracle separate assumptions from actual NULL-aware counts.
16.3.4|AD35|Các size estimates đơn giản|Nếu hai set inputs là selections|9. Dùng phản ví dụ outer|9. Hai cây cho|Projection/group/set/outer sizes, same-base predicate rewrites and guarded upper-bound versus estimated-input distinction with NULL caveat.
16.3.5|AD35|Distinct nhiều cột cũng phải|Ví dụ V(A, R)=100|6. V(A, R)=80|6. Estimate min(80,25)|Every source distinct-propagation case including empty equality, lists/ranges, cross-input sets, projections/group keys and aggregate-value estimates.
16.4|AD36|Đầu tiên bỏ qua physical properties|Một bảng cost làm lộ lỗi greedy|1. Trong ví dụ 1|1. R+ST|Evaluation-plan choice combines logical alternatives, physical implementations and declared estimated costs rather than treating tree shape as a full plan.
16.4.1|AD36|Giả sử chi phí của phép ghép|for mỗi quan hệ r|3. Với plan unordered|3. Unordered 18|Complete subset DP including indexed inner lookup cost, both directions, optimum proof, interesting-order state, tree counts and complexity/restrictions.
16.4.2|AD36|Một optimizer equivalence-rule dùng|group G_RS chứa|4. Tự lập một model|4. Rubric cần|Memo equivalence groups versus physical property alternatives, shared representation, duplicate detection, memoization and guarded dominance/pruning.
16.4.3|AD36|Chi phí optimize cũng là công việc|Đẩy selection xuống s|6. Trong ví dụ r3keys|6. Lookup30|Early filters/projections, left-deep restriction, ranked-prefix heuristic, blocks, dynamic budget and bind-sensitive plan caching taught with counterexamples.
16.5|AD37|View thường giữ định nghĩa|Ví dụ 1 có Orders|1. Từ summary|1. Sau insert A|Materialized derived rows save repeated query work but add maintenance/storage/freshness responsibilities; explicit running total trace.
16.5.1|AD37|Immediate maintenance cập nhật|Sửa mọi điểm trong application|5. Group K có|5. Ban đầu|Manual application maintenance, triggers, recompute versus incremental and immediate/deferred publication contracts compared; no native MySQL MV claim.
16.5.2|AD37|Với expression nhiều tầng|Nếu chỉ R thay đổi|6. πkey DISTINCT|6. Counter K|Differentials represent insertion/deletion and update as delete+insert; operator-by-operator state and expression-level proof rather than mere maintenance labels.
16.5.2.1|AD37|Nếu R, S là bag|Nếu chỉ R thay đổi|2. R, S cũ mỗi bên|2. Cũ 4|One-sided insert/delete formulas, two-input cross term and sequential batch method preserve bag pair counts; explicit deletion trace prevents double subtraction.
16.5.2.2|AD37|Selection v=σp(R)|R={(A,1)|6. πkey DISTINCT|6. Counter K|Selection filters signed deltas; set projection uses witness counts and removes output only after final support disappears; bag projection distinguished.
16.5.2.3|AD37|§16.5.2.3 còn cần biết|Chẳng hạn group A|5. Group K có|5. Ban đầu|COUNT/SUM/AVG sufficient row/non-NULL/sum state, zero versus empty group, all-NULL case and MIN/MAX deletion/index needs explained.
16.5.2.4|AD37|Các set operations có thể|Outer join cần theo dõi|7. Trace left-join view|7. Count0|Intersection/union/difference presence-count transitions and preserved-row match counts handle first/last outer match including NULL-extended rows.
16.5.2.5|AD37|Với expression nhiều tầng|Ví dụ `V=πcustomer|7. Trace left-join view|7. Count0|Bottom-up differential composition and structural induction require consistent child versions and additional cross terms when more than one branch changes.
16.5.3|AD37|Một materialized view chỉ thay|Giả sử V=Orders⋈Customer|11. Query order_id|11. Lookup theo|MV substitution and expansion back to defining query both considered; columns, grain, aggregates, uniqueness and freshness guard equivalence.
16.5.4|AD37|View/index selection đánh giá|nếu một view tiết kiệm40|8. Top3 nhỏ nhất|8. Threshold5|Weighted read/update workload includes refresh and storage/freshness constraints; candidate interactions defeat independent-benefit selection.
16.6|AD37|Multiquery optimization có thể|Multiquery optimization không chỉ|9. Q1 và Q2|9. Chọn riêng|Additional optimization opportunities beyond join enumeration have mechanisms, assumptions and concrete comparison activities.
16.6.1|AD37|Không thể dừng ngay khi|Top-K tăng dần có thể|3. Chạy top K=2|3. Top 2 gồm|Heap invariant and ordered pipelines contrasted with threshold estimation/re-execution; stopping safety, insufficient candidates and ties explicit.
16.6.2|AD37|Join elimination có proof|Nếu FK NULL|10. Orders.customer_id có|10. Không: order có|Non-NULL FK plus uniqueness and no remaining dimension use prove one copy per row; nullable/orphan/duplicate/filter counterconditions.
16.6.3|AD37|Halloween protection có thể|Halloween problem xảy ra|10. Orders.customer_id có|10. Không: order có|Index-key update can reencounter rows; RID materialization, safe direction conditions, affected subqueries and batch index-order updates explained.
16.6.4|AD37|Multiquery optimization không chỉ|Q1 plan riêngA|9. Q1 và Q2|9. Chọn riêng|Joint plan choice can create more sharing than independent cheapest plans; shared scan plus residual branches cost16 versus20 with consumer constraints.
16.6.5|AD37|Parametric optimization có thể|C_i(p)=10+2p|8. Top3 nhỏ nhất|8. Threshold5|Keep parameter-domain optimal alternatives and choose cheaply at execution; crossing at p45, estimated-match mapping and caching difference explicit.
16.6.6|AD37|Adaptive join có thể|Tổng cost gồm phần thử sai|9. Q1 và Q2|9. Chọn riêng|Runtime join choice or stats-driven abort/replan/restart requires prefix/output preservation, sunk work accounting and a safeguard against repeated restarts.
27.4|AD61|edge là quan hệ đầu vào|reach(X,Y) :- edge|5. Với accounts|5. Chỉ Id=a1|Declarative rules define views/facts rather than procedural ordered assignment; rule/query syntax tied to concrete bindings and closure.
27.4.1|AD61|Một fact như|Xét `account(Id,Branch,Balance)`|5. Với accounts|5. Chỉ Id=a1|Facts, head/body, shared variables/constants, query bindings, multi-rule union and positive/negative examples teach basic program structure.
27.4.2|AD61|Atom `account(Id,west,B)`|Một **ground instantiation**|5. Với accounts|5. Chỉ Id=a1|Literal arity/position/variable conventions, arithmetic-as-relations and direct/indirect dependency layering versus recursive cycles.
27.4.3|AD61|Về hình thức, `infer(R,I)`|Ví dụ `rich` ở tầng 1|5. Với accounts|5. Chỉ Id=a1|Nonrecursive semantics built from satisfied ground rules and dependency-ordered completed views, not arbitrary rule order.
27.4.3.1|AD61|Một **ground instantiation**|Thay Id=a1 và B=900|5. Với accounts|5. Chỉ Id=a1|Repeated variables have one substitution; all positive/negative/comparison literals determine whether the instantiated head can be inferred.
27.4.3.2|AD61|Về hình thức, `infer(R,I)`|Ii=Ii−1 ∪ infer|5. Với accounts|5. Chỉ Id=a1|Minimal dependency layers compute each view after its inputs, with explicit input-plus-layer-inference recurrence and induction.
27.4.4|AD61|Điều kiện an toàn đủ dùng|`bad(X,Y):-X>Y`|6. So `p(A)|6. Nonrecursive p|Both safety restrictions, infinite arithmetic/negation/head examples, finite guarded correction and conservative-condition versus terminating extension distinction.
27.4.5|AD61|Chiều ngược lại, dịch|Với set relations R(A)|7. Dịch `pair|7. Pair là R×S|Basic algebra translations both directions include product, shared-variable renaming, union and guarded difference; update/aggregation syntax treated as extensions.
27.4.6|AD61|Completeness đối với least model|Ví dụ 1: edge=|1. Trace naive|1. R đầu có|Naive and semi-naive algorithms, monotonicity/finite-domain termination and soundness/least-model completeness proofs, cycle trace and negation limitation.
27.4.7|AD61|Một relational-algebra expression hữu hạn|Các operators selection|2. Chứng minh termination|2. Ground facts|Unbounded reachability needs recursion or an external fixpoint loop; arithmetic can break finite-domain termination; difference and grouped aggregation are nonmonotone.
'''
items = {}
for line in DATA.strip().splitlines():
    parts=line.split('|')
    assert len(parts)==7,(line,len(parts))
    sec,name,t,e,q,a,judgment=parts
    assert sec not in items
    items[sec]=(name,t,e,q,a,judgment)

inventory=load(RESEARCH/'source-section-inventory.json')['bookSections']
assigned=[u for u in inventory if owned.intersection(u['plannedAdvancedLessonIds'])]
assert set(items)=={u['section'] for u in assigned},(set(items)-{u['section'] for u in assigned},{u['section'] for u in assigned}-set(items))
batches={'8':[[953,1243]],'24':[[489,640]],'27':[[405,718],[719,990]],
         '16':[[20,621],[622,1002],[915,1321],[1478,1829]],
         '10':[[11,367],[368,701],[702,1100],[1101,1406],[1407,1755],[1756,1886]]}
pages={'AD15':[418,420,1215,1217,1218], 'AD35':[773,774,777,782,785,788],
       'AD36':[797,802], 'AD37':[], 'AD61':[17,21], 'AD73':[503,507],
       'AD20':[517,518,520,526], 'AD21':[535], 'AD22':[]}
rows=[]
for unit in assigned:
    sec=unit['section'];name,t,e,q,a,judgment=items[sec]
    same_source=[u for u in inventory if u['sourcePath']==unit['sourcePath']]
    i=next(i for i,u in enumerate(same_source) if u['section']==sec)
    end=same_source[i+1]['sourceLine']-1 if i+1<len(same_source) else unit['scopeLineEnd']
    path=Path(unit['sourcePath']);lines=(WORK/path).read_text(encoding='utf-8').splitlines()
    body='\n'.join(lines[unit['sourceLine']-1:end])
    rows.append({'section':sec,'title':unit['title'],'owners':[name],
                 'source':{'path':str(path).replace('\\','/'),'sha256':sha(WORK/path),
                           'ownBodyLines':[unit['sourceLine'],end],
                           'ownBodySha256':hashlib.sha256(body.encode('utf-8')).hexdigest()},
                 'sourceReadEvidence':{'ownBodyRead':True,'readBatches':batches[unit['chapter']],
                     'figurePagesVisuallyInspected':pages[name],
                     'figurePdf':'online-27.pdf' if name=='AD61' else 'DSC7e print PDF',
                     'baselineCredit':False,
                     'proofScope':'Personally compared full source own-body and full current lesson; conditional written proofs plus finite independent Python/SQLite checks. No proof-assistant or distributed-engine claim.'},
                 'semanticStatus':'complete','contentComparison':judgment,
                 'evidence':[anchor(name,t,'teaching'),anchor(name,e,'worked-example-or-algorithm'),
                             anchor(name,q,'activity'),anchor(name,a,'answer')],
                 'gaps':[]})

checks=load(COURSE/'qa/optimizer-bigdata-checks.json')
assert checks['status']=='pass' and checks['lessonSha256']==dict(sorted(hashes.items())), 'QA hashes changed; rerun meaningful checks after edits'
report={'date':'2026-11-05','scope':'Nine owned advanced lessons. 71 exclusive source units plus seven shared AD18/AD37 maintenance units independently rechecked using AD37 only; AD18 remains frozen. Every numbered own-body is bounded by the next numbered heading, not its parent scope end.',
        'counts':{'assigned':len(rows),'complete':len(rows),'exclusiveUnits':71,'sharedAD18UnitsRechecked':7},
        'units':rows,'lessonSha256':dict(sorted(hashes.items())),
        'checks':{'path':'qa/optimizer-bigdata-checks.json','sha256':sha(COURSE/'qa/optimizer-bigdata-checks.json'),**checks['counts']},
        'sourceInterpretation':[
            'Corrected evident source equivalence typos by deriving joins from row membership; outer join reassociation is rejected by explicit counterexample.',
            'Set-algebra same-base difference-to-NOT rewrite requires two-valued predicates; SQL UNKNOWN exception is taught explicitly.',
            'R-tree textbook maximum-overlap child selection is distinguished from minimum-enlargement variants; quadratic split proof concerns coverage/occupancy, not a global area optimum.',
            'Textbook product capabilities and code are historical context; authored web exercises use typed/model contracts without asserting current service capability.',
            'Safe recursion termination assumes a fixed finite domain; no-function-symbol syntax alone is insufficient if arithmetic generates new constants.'],
        'notExecuted':checks['notExecuted'],
        'limitations':checks['limitations'],
        'frozen':True}
(RESEARCH/'semantic-optimizer-bigdata.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')

# Validate all frozen witnesses and own-body hashes again, independently of selection.
for row in report['units']:
    source=row['source'];path=WORK/source['path'];assert sha(path)==source['sha256']
    first,last=source['ownBodyLines'];body='\n'.join(path.read_text(encoding='utf-8').splitlines()[first-1:last])
    assert hashlib.sha256(body.encode()).hexdigest()==source['ownBodySha256']
    for witness in row['evidence']:
        path=COURSE/witness['path'];assert sha(path)==witness['lessonSha256']
        assert witness['exactOpening'] in path.read_text(encoding='utf-8')
integrity={'status':'pass','units':len(rows),'exactWitnesses':sum(len(r['evidence']) for r in rows),
           'sourceFiles':len({r['source']['path'] for r in rows}),
           'sourceBounds':'next numbered heading minus one; source scopeLineEnd only for last numbered unit',
           'ledgerSha256':sha(RESEARCH/'semantic-optimizer-bigdata.json'),
           'lessonSha256':dict(sorted(hashes.items()))}
(COURSE/'qa/optimizer-bigdata-integrity.json').write_text(json.dumps(integrity,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'counts':report['counts'],'checks':checks['counts'],'integrity':integrity},ensure_ascii=False))
