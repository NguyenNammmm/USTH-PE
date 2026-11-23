"""Freeze manually reviewed own-body correspondence; never classify by keywords.

The fixed hashes require a fresh content review before any later lesson edit can
receive credit. The integrity checks validate the record, not pedagogical truth.
"""
from pathlib import Path
import collections
import hashlib
import json
import re

R = Path(__file__).resolve().parents[1]
W = R.parents[1]
O = R / 'research'
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
FROZEN = {
    'AD46': '12a430da36f455ccb65b7080d9e8b4208114b88805bf954f7590118e58e5a789',
    'AD47': '8c03e85c7454c59fd34e17cacee9bacd48dd98c281fad0e8f9b28c0ce0c61eb5',
    'AD48': '4fdd391de1234ff09d6840c62d9e512a50a5603b3770e7ee539364bdcf05090e',
    'AD49': '13495eb217719044e6efa1329a47160e0c9030a80e527c7b659f0521b5676472',
    'AD64': 'edf885f1fd83521b8ec3d07a3afd0c105a3d7fb597cd756f36ac40aafabda752',
    'AD79': 'bc0a04bba28b11d1247268e296a7aff34c8ec80aca97ebc59461698dd616348e',
    'AD80': '5720687413dcd750995bd0234c65af78f0fb4172d8dcd4b456be6cc9ea47e10b',
}
texts, paragraphs = {}, {}
for name, digest in FROZEN.items():
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == digest, f'{name}: direct source/content rereview required'
    texts[name] = p.read_text(encoding='utf-8-sig')
    paragraphs[name] = [p.strip() for p in texts[name].split('\n\n') if p.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(paragraphs[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    paragraph, p = found[0]
    start = texts[name].index(p)
    return {'path': f'lessons/{name}.md', 'lessonSha256': FROZEN[name],
            'kind': kind, 'paragraph': paragraph,
            'lineStart': texts[name][:start].count('\n') + 1,
            'lineEnd': texts[name][:start + len(p)].count('\n') + 1,
            'exactOpening': p[:350], 'exactFragment': p}


def practice(name, number, answer=False):
    lo = texts[name].index('## Đáp án và lập luận' if answer else '## Luyện tập')
    hi = texts[name].index('## Biến thể và cách kiểm' if answer else '## Gợi ý', lo)
    found = list(re.finditer(rf'^{number}\. .+$', texts[name][lo:hi], re.M))
    assert len(found) == 1, (name, number, answer)
    m = found[0]
    fragment = m.group()
    return {'path': f'lessons/{name}.md', 'lessonSha256': FROZEN[name],
            'kind': 'answer' if answer else 'activity',
            'lineStart': texts[name][:lo + m.start()].count('\n') + 1,
            'lineEnd': texts[name][:lo + m.end()].count('\n') + 1,
            'exactOpening': fragment[:350], 'exactFragment': fragment}


# Each group names actual reviewed teaching, example/algorithm and reasoning.
# Reuse is intentional where the source splits one concept across parent/children.
G = {
 'central': ('AD46', 'Centralized database có', 'Ví dụ thứ nhất:', 'Centralized ở đây nghĩa', 9),
 'server': ('AD46', 'Trong kiến trúc transaction server', 'Ví dụ T1 cập nhật', 'Điểm bất biến là chỉ một thread', 5),
 'client': ('AD46', 'Data server phù hợp', 'Prefetch gửi thêm', 'Adaptive granularity có thể', 6),
 'parallel': ('AD46', 'Shared-nothing chia memory', 'Một công thức công việc đều hơn', 'Hierarchical/hybrid có thể', 4),
 'performance': ('AD46', 'Speedup giữ workload', 'Ví dụ thứ hai:', 'Lập luận đến từ việc', 1),
 'scale': ('AD46', 'Đặt f là tỷ lệ serial', 'Batch scaleup tăng', 'Superlinear speedup có thể', 8),
 'topology': ('AD46', 'Bus chia băng thông', 'Tree mạng cơ bản', 'Không có đường ngắn hơn số bit', 7),
 'architectures': ('AD46', 'Shared-memory có nhiều', 'Với shared disk, SAN', 'Hierarchical/hybrid có thể', 2),
 'memory': ('AD46', 'Shared-memory có nhiều', 'NUMA vẫn cho mọi core', 'Còn cần memory ordering:', 9),
 'coherence': ('AD46', '§20.4.5.2 phân tích', 'Còn cần memory ordering:', 'Ca biên false sharing:', 10),
 'disk': ('AD46', 'Shared-disk cho các node', 'Với shared disk, SAN', 'RAID chịu một số disk faults', 2),
 'nothing': ('AD46', 'Shared-nothing chia memory', 'Một công thức công việc đều hơn', 'Một node giữ khóa', 4),
 'hybrid': ('AD46', 'Hierarchical/hybrid có thể', 'NUMA vẫn cho mọi core', 'Hệ hierarchical cần ghi', 9),
 'distributed': ('AD79', 'Parallel database thường', 'Ví dụ 1 giả định', 'Local/global được xét', 5),
 'distributed-tx': ('AD79', 'Đối với atomic commit,', 'chuyển 10 từ A sang B', 'Ready không phải commit', 5),
 'cloud': ('AD79', 'IaaS cấp hạ tầng', 'Ví dụ 2:', 'Cloud giảm đầu tư ban đầu', 6),
 'cloud-models': ('AD79', 'Một storage service có thể', 'Trong một deployment có ba service', 'Ví dụ một API stateless', 7),
 'cloud-limits': ('AD79', 'Cloud giảm đầu tư ban đầu', 'Cost model có thể gồm', 'Ví dụ yêu cầu nội bộ', 6),
 'partition-overview': ('AD47', 'Phân vùng ngang chia row', 'Ví dụ thứ nhất có', 'Bất biến migration là', 5),
 'partition': ('AD47', 'Round-robin phân lần lượt', 'Cho row `(id=7,k=9)`', 'Range partition dùng', 1),
 'partition-compare': ('AD47', 'Query trên thuộc tính', 'Với bảng chỉ có 12 rows', 'Không cố tối đa số partition', 5),
 'skew': ('AD47', 'Hot key là vấn đề khác', 'Ví dụ thứ hai:', 'cận dưới không phải250', 2),
 'vector': ('AD47', 'Sort mẫu key, chọn quantile', 'Với 12 key phân biệt', 'boundary trùng không tạo', 6),
 'virtual': ('AD47', 'Virtual nodes chia một máy', 'Virtual partition có thể', 'một key bất khả chia', 6),
 'dynamic': ('AD47', 'Tablet là một virtual range', 'Một consistent-hash ring', 'Bất biến migration là', 7),
 'replication': ('AD47', 'Partitioning chia tập dữ liệu', 'Nhiều node làm sự kiện', 'Cache có thể bị evict', 8),
 'replica-place': ('AD47', 'Nếu A có 9 tablets', 'mỗi nơi thêm 30 request/s', 'Placement tối ưu lúc bình thường', 8),
 'replica-consistency': ('AD47', 'Khi replica được update atomic', 'primary ACK update u11', 'Owner mới phải có mọi update', 9),
 'index': ('AD64', 'Global primary index trong', 'Ví dụ: R partition theo city', 'Mỗi base tuple có một entry', 11),
 'dfs': ('AD64', 'Thiết kế HDFS/GFS được', 'Ví dụ model file 160 MiB', 'Write model gồm NameNode', 5),
 'kv': ('AD64', 'Key có encoding, ordering', 'Ví dụ 3: hai client', 'Batch API có thể chỉ batch', 4),
 'representation': ('AD64', 'KV có thể giữ bytes', 'Sắp key theo rowID', 'Timestamp client không tự', 6),
 'routing': ('AD64', 'Master/controller giữ', 'Nếu mapping cũ', 'PUT retry cần dedup', 7),
 'geographic': ('AD64', 'Geographic replicas có hai', 'model RTT remote 70 ms', 'Nếu local update ACK trước', 7),
 'lsm': ('AD64', 'B+ tree thường sửa page', 'LSM ghi memtable', 'không sửa run cũ', 6),
 'row-scope': ('AD64', 'Atomic batch nhiều cột', 'Giả sử hai rows', 'Không tồn tại thứ tự serial', 9),
 'cas': ('AD64', 'CAS nhận expected', 'Ví dụ 3: hai client', 'Version đơn điệu tránh', 3),
 'atomic-index': ('AD64', 'Synchronous secondary-index maintenance', 'Đổi email user10', 'Verify chỉ loại ghost', 2),
 'kv-recovery': ('AD64', 'Model recovery của một tablet', 'balance 100, record 41', 'Mất log của một tablet', 8),
 'app-join': ('AD64', 'Một mạng xã hội có U', 'Ví dụ A có 1.000 followers', 'Unfollow/delete/privacy change', 10),
 'kv-performance': ('AD64', 'Colocate các rows cùng entity', 'Stored function chạy gần', 'TTL/version retention', 10),
 'query-parallelism': ('AD48', 'Interquery parallelism chạy', 'Ví dụ bốn reports', 'số operators thường nhỏ hơn', 4),
 'sort': ('AD48', 'Range-partitioning sort chọn', 'Với keys [8,1,6,2,9,3]', 'Để output là sorted toàn cục', 5),
 'external-sort': ('AD48', 'Hai sort plans đặt exchange', 'runs_i = external_sort', 'Đích phải đợi head', 5),
 'join': ('AD48', 'Với R⋈S theo', 'Ví dụ 1: R có', 'Chứng minh đủ cặp:', 1),
 'partition-join': ('AD48', 'Partitioned join cũng có thể', 'h0(k)=k mod 2', 'Với partitioned right outer join', 10),
 'fragment': ('AD48', 'Nếu S nhỏ, giữ R', 'Ví dụ 2: bốn worker', 'Mỗi cặp r,s thuộc đúng một ô', 3),
 'join-skew': ('AD48', 'Nếu keyA chiếm phần lớn', 'Số output có thể chính', 'Task claim/ownership phải atomic', 8),
 'relational': ('AD48', 'Equality selection trên partition key', 'Nếu R(A,B) có', 'Partition theo toàn tuple projected', 9),
 'aggregate': ('AD48', 'SUM vàCOUNT cho partial', 'Ví dụ 3: workerA', 'State merge phải có tính kết hợp', 2),
 'mapreduce': ('AD48', 'Map nhận một input record', 'Ví dụ hai input records', 'không dùng combiner chỉ vì', 9),
 'plan': ('AD80', 'Một plan có thể chia', 'Ví dụ 1 có scan', 'Bất biến: task chỉ bắt đầu', 1),
 'interoperation': ('AD80', 'Pipeline có thể chồng', 'Ví dụ 3 có ba task', 'Pipeline dài ít operators', 1),
 'pipeline': ('AD80', 'Trong một call stack pull', 'Trong fluid model ví dụ 2', 'Producer không thể duy trì', 10),
 'independent': ('AD80', 'Ví dụ 3 có ba task', 'Ví dụ 1 có scan', 'Bất biến: task chỉ bắt đầu', 3),
 'exchange': ('AD80', 'Exchange nhận row/batch', 'Nếu có hai stream sorted', 'Random merge ở destination', 2),
 'whole-plan': ('AD80', 'Theo §22.5.3, xét', 'Hai output thuộc **cùng group', 'E3 phải định tuyến theo', 5),
 'query-fault': ('AD80', 'MapReduce fault model', 'Ví dụ M0 tạo a,b', 'Lineage giữ phép toán', 6),
 'shared-query': ('AD80', 'Với broadcast join trong một node', 'Ví dụ build state 120 MiB', 'Probe read-only sau build barrier', 7),
 'parallel-optimizer': ('AD80', 'Một optimizer cần lưu', 'Ví dụ A=X', 'Chọn mỗi operator nhanh nhất', 8),
 'parallel-cost': ('AD80', 'Resource cost cộng CPU', 'CPU c=6', 'không chia tổng cost cho n', 8),
 'parallel-choice': ('AD80', 'Có hai cách giảm search space', 'Cách 1 chọn sequential', 'Hai heuristic chỉ là', 9),
 'colocation': ('AD80', 'Colocation giữ dữ liệu', 'Nếu student và takes', 'Giữ một bản sao partition', 9),
 'parallel-view': ('AD80', '§22.7.5 materialize input', 'Insert `S(1,Y,3)`', 'Bất biến theo từng cạnh:', 5),
 'stream': ('AD49', 'Luồng tốc độ lớn', 'Lambda architecture fork input', 'retention hết trước recovery', 5),
 'stream-routing': ('AD49', 'Mỗi logical operator còn', 'Ví dụ topic có P0', 'Topic retention giữ events', 5),
 'stream-operation': ('AD49', 'Selection/projection stateless', 'Với sliding windows độ rộng', 'Watermark/late policy quyết định', 6),
 'stream-fault': ('AD49', 'Checkpoint streaming cần', 'Với checkpoint `state count=12', 'Một operator có state window lớn', 6),
 'integration': ('AD49', 'Federation có thể dựng', 'Warehouse nhập/làm sạch', 'Query qua nhiều nguồn không tự', 7),
 'schema': ('AD49', 'Nguồn A có `PersonA', 'Fixture A có PersonA', 'Local-as-view (LAV) diễn đạt', 8),
 'cross-source': ('AD49', 'Optimizer phân tán còn', 'Xét R ở A 2 MiB', 'connector capability là ràng buộc', 9),
 'join-location': ('AD49', 'Xét R ở A 2 MiB', 'Chuỗi ship R tới B', 'Index ở B không tự', 9),
 'semijoin': ('AD49', 'Giả sử kết quả R⋈S', 'Ví dụ 1: R có', 'Chứng minh: nếu (r,s)', 1),
 'distributed-optimizer': ('AD49', 'Optimizer vì thế giữ location', 'query campus=\'West\' chỉ cần West', 'Hai replicas cùng logical data', 9),
 'directory': ('AD49', 'Directory có thể tra object', 'DNS minh họa naming', 'Protocol directory đơn giản', 10),
}

# Explicit source-unit judgments, after reading each own body and the complete MD.
ITEMS = [
 ('20.1','parallel','Architecture overview distinguishes centralized, parallel DB, key-oriented storage and integrated distributed systems; later chapters separated rather than credited by the overview.'),
 ('20.2','central','Single computer may have multicore shared memory; embedded versus multiuser features are contract-dependent; interleaving and throughput distinguished from single-query speedup.'),
 ('20.3','server','Transaction/query shipping versus item/page/object API and where computation runs; recovery and indexing responsibilities stated.'),
 ('20.3.1','server','All server/lock/writer/checkpoint/monitor roles and shared structures taught; atomic TAS/CAS, latch grant/release protocol, WAL example and non-lost notification trace.'),
 ('20.3.2','client','CPU-heavy client computation, object/item APIs and partial large-item access distinguished from historical page shipping.'),
 ('20.3.3','client','Prefetch, data validity/phantoms, cached lock callbacks and failure authority, adaptive granularity/de-escalation order with RTT calculation and answer.'),
 ('20.4','parallel','Coarse/massively parallel nodes, separate local resources, data-center fabric and work/resource bottlenecks contextualized by the architecture model.'),
 ('20.4.1','parallel','Large data/transaction demand and set-oriented work motivate scale; application-server parallelism separated from database bottlenecks.'),
 ('20.4.2','scale','Throughput/response, speedup/efficiency, batch/transaction scaleup, Amdahl and serial-scaling formula derived; startup/interference/skew/superlinear caveats and numerical practice.'),
 ('20.4.3','topology','Bus/ring/mesh/hypercube/tree-like routing and hop bounds, bandwidth bottleneck, link technologies, OS bypass and RDMA roles explained without historical speeds asserted as current.'),
 ('20.4.4','architectures','Shared-memory, shared-disk, shared-nothing and hierarchical resource boundaries compared; schematic lines not assumed to be one shared bus.'),
 ('20.4.5','memory','Common memory communication, multicore and Moore observation versus clock/query speed; memory/cache locality used instead of automatic core-count speedup.'),
 ('20.4.5.1','memory','NUMA banks/interconnects, cache levels/lines/misses and SMT shared execution resources explained; local cost model and centralized classification exercise.'),
 ('20.4.5.2','coherence','MESI line states/revocation, publication ordering, synchronization/barriers and false sharing; language/CPU-specific fence prose not generalized into unsafe code.'),
 ('20.4.6','disk','Independent memory/shared disk, SAN logical storage, RAID/node/link fault distinctions, access bottlenecks and coordinated write/recovery requirements.'),
 ('20.4.7','nothing','Local I/O ownership improves scalability while remote transfer/software, skew and distributed coordination remain costs.'),
 ('20.4.8','hybrid','Shared-memory nodes within a shared-nothing outer system; possible shared-disk middle and need to analyze both local and remote failure/resource layers.'),
 ('20.5','distributed','Geography/WAN latency, network and site failures, autonomy/heterogeneity, homogeneous/federated administration and local/global definitions with concrete counterexamples.'),
 ('20.6','distributed-tx','Ready/coordinator all-YES commit and any-NO abort, recovery obligation, distributed deadlocks, replication, persistent messaging and human workflows distinguished.'),
 ('20.7','cloud','Outsourced infrastructure/service operation, elasticity and state-management responsibilities contextualize cost and capacity models.'),
 ('20.7.1','cloud-models','IaaS/PaaS storage/database/SaaS, VM guest OS/hypervisor, container userspace/shared kernel, microservice APIs, orchestration/pods/load balancing and stateful scaling taught.'),
 ('20.7.2','cloud-limits','Capital/operations/elasticity benefits balanced with actual data/replica/backup geography, security/control and responsibility inputs; no obsolete jurisdiction conclusion or live prices claimed.'),
 ('21.1','partition-overview','Storage overview covers row placement, indexing, DFS and many small KV items; query/transaction roles distinguished with explicit lesson bridges.'),
 ('21.2','partition-overview','Horizontal versus orthogonal vertical division, tuple placement versus RAID blocks and intra-node partitions; key-changing update must relocate safely.'),
 ('21.2.1','partition','Round-robin/hash/range routing including half-open boundaries and insert/delete/key-changing update behavior; equality/hash encoding assumptions clear.'),
 ('21.2.2','partition-compare','Scan/point/range and nonpartition-key access compared, throughput versus range hotspots, local indexes/fanout and small/medium relation degree choices.'),
 ('21.3','skew','Attribute-frequency skew, boundary/hash bucket skew and query execution skew distinguished; max-load bound, hot-key limits and salting correctness/cost.'),
 ('21.3.1','vector','Sort-based quantile boundaries, histogram/sampling alternative, repeated-key impossibility and dynamic workload drift with explicit worked vector/answer.'),
 ('21.3.2','virtual','More virtual than physical nodes, mapping array/round-robin versus load-aware assignment, elasticity/migration and indivisible-hot-key limit.'),
 ('21.3.3','dynamic','Tablet range/ID/owner metadata, split versus move, cached routing refresh, consistent-hash predecessor/wrap and changed interval demonstrated; live migration invariant explicit.'),
 ('21.4','replication','Partition-level durable replicas and metadata, failover routing, node-count failure-rate assumptions and evictable cache distinction.'),
 ('21.4.1','replica-place','Node/rack/site failure domains and locality versus WAN cost; distribute backup workload and reserve capacity after failure, with rate/load arithmetic.'),
 ('21.4.2','replica-consistency','Atomic locking reads versus asynchronous lag/master routing; promotion needs committed history/propagation/fencing; 2PC, persistent messaging and consensus roles separated.'),
 ('21.5','index','Global primary routing+local index and partition key not necessarily unique; global secondary I(Ki,Kp,Ku) two-hop algorithm, identity/bag proof and synchronous/asynchronous maintenance limits.'),
 ('21.6','dfs','Namespace/block replica metadata versus direct data path; NameNode RAM/small-file limit, DataNode reads/retry, write pipeline/ACK and historical append/write-once visibility model.'),
 ('21.7','kv','GET/PUT/DELETE and optional range/partial schema versus bytes/document/wide columns; tablet elasticity and capability/transaction/constraint scope explicit, historical vendor lists not generalized.'),
 ('21.7.1','representation','Sparse attributes and row-column-version keys, ordered prefix/URL layout, latest-version semantics, columnar access and column-family locality/bytes tradeoff.'),
 ('21.7.2','routing','Master/controller partition metadata and health/reassignment; tablet server data path, cached-client or router routing, stale split/move retry and write idempotency limits.'),
 ('21.7.2.1','geographic','Cross-site failure tolerance and read locality; synchronous remote confirmation versus asynchronous RPO risk with worked latency and answer.'),
 ('21.7.2.2','lsm','Ordered/clustered tablet indexes support ranges; B+ in-place pages conflict with immutable file API while LSM creates/merges new sorted runs.'),
 ('21.7.3','row-scope','Single-item atomic serialized operations do not imply multi-item transaction serializability; doctors schedule and serial-order contradiction prove the limit.'),
 ('21.7.3.1','cas','Atomic conditional version check/update, retry and ABA versus unconditional GET/PUT; atomic increment/stored-operation scope separated from multirow guards.'),
 ('21.7.3.2','atomic-index','Single-row multi-column atomicity versus multirow/base-index commit; deferred secondary/view lag and ghost/missing asymmetry explicit; full transaction capability must be declared.'),
 ('21.7.3.3','kv-recovery','Failure detection/reassignment plus replicated log recovery before service; checkpoint/log replay/idempotency, partial append sequence cleanup, DFS-owned versus KV-owned replication and authority limits.'),
 ('21.7.4','app-join','Application read-time join versus write-time feed materialization with fanout/storage/read costs and privacy/delete maintenance.'),
 ('21.7.5','kv-performance','Related tuples/entity groups colocated, stored computation reduces transfer under scope constraints, old-version/item TTL needs retention for queries/replay.'),
 ('22.1','query-parallelism','Interquery/intraquery and intraoperation/interoperation definitions, composability and scalability limits, shared-nothing explicit data movement and hierarchical local optimization context.'),
 ('22.2','sort','Already range-partitioned input can local-sort then concatenate; alternative redistribution-first and local-sort-first plans distinguished.'),
 ('22.2.1','sort','Common balanced range vector, all-source redistribution, independent local sorts, ordered range concatenation and ties/skew correctness argument.'),
 ('22.2.2','external-sort','Local external sort then common-range ordered stream merge; per-stream order/head/EOS invariant, block interleaving avoids serialized receivers, finite termination and memory/pass costs.'),
 ('22.3','join','Parallel join splits candidate pairs with local exact predicate; final bag union must preserve pair identity and multiplicity.'),
 ('22.3.1','partition-join','Common hash or range equality routing, reuse existing colocation, local Grace/hybrid/merge/nested-loop choices; complete inner/right/left/full outer and natural join handling with NULL identities.'),
 ('22.3.2','fragment','Broadcast/asymmetric and p-by-q symmetric fragment grid, exact pair ownership proof and traffic, theta capability and safe/unsafe outer-join orientation.'),
 ('22.3.3','join-skew','Join work/output multiplicity rather than row count, heavy-key salting, virtual tasks and dynamic stealing of unprocessed work, snapshot/claim/output ownership conditions.'),
 ('22.4','relational','Other relational operators and general user-defined map/reduce use data-parallel local operations with exchange, not a claim that every operator is one cheap scan.'),
 ('22.4.1','aggregate','Selection pruning, bag projection versus global DISTINCT, group routing, partial SUM/COUNT/MIN/MAX/AVG states and exact distinct/combiner/skew limitations.'),
 ('22.4.2','mapreduce','Map zero/many keyed outputs, intermediate repartition/group, reduce call per key within tasks, scheduler tasks/workers and distributed I/O; combiner requires lawful state merge.'),
 ('22.5','plan','Whole plans combine intra/interoperator execution with exchange/local stages, resource/dependency scheduling and failure/output-commit boundaries.'),
 ('22.5.1','interoperation','Independent and pipelined operator concurrency separated, useful alongside data parallelism but bounded by operator count, blocking stages and rate bottlenecks.'),
 ('22.5.1.1','pipeline','Push versus one-call-stack pull, local versus network queues, batching/synchronization/backpressure, blocking limits and primary avoidance of intermediate I/O.'),
 ('22.5.1.2','independent','DAG-independent tasks can share workers before dependent join stage; critical-path/max-work lower bounds and explicit two-worker schedule.'),
 ('22.5.2','exchange','Outgoing hash/range/broadcast/gather plus incoming random/ordered merge, local operator reuse and pull-local/push-remote batch bridge; sorted-head and multiplicity conditions.'),
 ('22.5.3','whole-plan','Complete join/group E1/E2 join-key, optional local hash partition, E3 group-key and E4 gather trace; partial aggregation changes traffic/pipeline barrier.'),
 ('22.5.4','query-fault','Full restart versus local recovery; map local files/reduce input barrier/replicated result, failed and speculative attempt commit, stragglers, lineage/checkpoints/shuffle state and duplicate-safe pipelining.'),
 ('22.6','shared-query','One shared broadcast build, cheap descriptor stealing, private-partition versus shared hash build/probe morsels, latches/publication, NUMA affinity/locality, cache races and SIMD/GPU costs.'),
 ('22.7','parallel-optimizer','Larger physical-property and scheduling search space, exchange traffic/skew/resource overlap, no sequential-cost plan guarantee.'),
 ('22.7.1','parallel-optimizer','Parallel algorithms, partition key/function/degree, stage schedule and A/B versus (A,B) join followed by group A demonstrate whole-plan property tradeoff.'),
 ('22.7.2','parallel-cost','Resource sums versus response-time overlap/critical path, local and exchange costs, startup/max worker/skew and statistics; pipeline/sequential CPU-I/O examples and assumptions.'),
 ('22.7.3','parallel-choice','Sequential-first parallelization versus property-aware data-parallel heuristic, exchange enforcers, optimization-cost tradeoff and alternate replica layouts/freshness.'),
 ('22.7.4','colocation','Student/takes by ID and replicated dimension enable local point query; course-key query needs different layout, maintained alternate copy or materialized result.'),
 ('22.7.5','parallel-view','Materialize operator inputs/outputs, route signed base and output deltas through original exchanges, identity-preserving index key changes and root induction versus full recompute; concurrent batch consistency separate.'),
 ('22.8','stream','Multiple ingress points, operator routing/state and lambda fork into stored/stream branches with duplicated logic versus unified processing.'),
 ('22.8.1','stream-routing','Logical source/operator/sink DAG and pub-sub topics, fanout per logical subscriber, physical keyed instances, topic partitions/consumer groups and retention/reassignment.'),
 ('22.8.2','stream-operation','Stateless selection/projection versus keyed state/UDF/aggregate; overlapping windows use group routing and local memberships, watermark finality and local/remote state costs.'),
 ('22.8.3','stream-fault','At-most/at-least/exact logical effect distinctions, genuine duplicate identities, durable stream positions+state checkpoint, replay/retention, replicated checkpoint, producer retention and hot-spare authority; external sink boundary explicit.'),
 ('22.9','integration','Distributed source queries arise from geography and heterogeneous existing stores; integration layer does not imply common transaction snapshot.'),
 ('22.9.1','integration','Federated global schema/mediator, virtualization, external foreign tables/SQL-MED wrappers, warehouse lag/source load and data-lake preparation choices.'),
 ('22.9.2','schema','Concrete GAV local join/union rewriting and LAV complete/disjoint predicate pruning; view-update ambiguity, NULL coverage, types/units/identity equivalence and virtual versus materialized freshness.'),
 ('22.9.3','cross-source','Capabilities constrain feasible pushdown and required parameters; local CPU/indexes plus transfer/output site and collation semantics determine plan.'),
 ('22.9.3.1','join-location','Ship-all versus staged joins at original sites with intermediate/output byte costs; relative execution/index/latency costs may reverse preferred join order/location.'),
 ('22.9.3.2','semijoin','Distinct join-key shipping then bag-preserving candidate S and final exact join, two-inclusion/multiplicity proof, cost disadvantage case, Bloom conservative overapproximation and no-false-negative condition.'),
 ('22.9.3.3','distributed-optimizer','Location as physical property, operator site/exchange, restricted semijoin search, complete LAV site pruning and one snapshot-valid replica selection.'),
 ('22.9.4','directory','Forward/reverse lookup, DNS hierarchical delegation and LDAP standardized organizational entries/protocol with replicated/cached authority; relational backend and authentication bridge separated from general query interface.'),
]

inv = load(O / 'source-section-inventory.json')['bookSections']
assigned = [u for u in inv if set(u['plannedAdvancedLessonIds']) & set(FROZEN)]
assert len(assigned) == 83
assert {u['section'] for u in assigned} == {s for s, _, _ in ITEMS}
assert len(ITEMS) == 83
by_section = {u['section']: u for u in assigned}
pages = {
 '20': [993,995,1001,1002,1004,1008,1010,1011,1014,1016,1020,1023],
 '21': [1034,1038,1040,1041,1043,1047,1050,1056],
 '22': [1071,1073,1076,1080,1083,1084,1087,1100],
}
rows = []
for section, group, judgment in ITEMS:
    u = by_section[section]
    name, teaching, example, argument, q = G[group]
    assert name in u['plannedAdvancedLessonIds'], (section, name)
    chapter_units = [v for v in inv if v['chapter'] == u['chapter']]
    i = next(i for i, v in enumerate(chapter_units) if v['section'] == section)
    end = chapter_units[i + 1]['sourceLine'] - 1 if i + 1 < len(chapter_units) else u['scopeLineEnd']
    source_path = u['sourcePath'].replace('\\', '/')
    lines = (W / source_path).read_text(encoding='utf-8').splitlines()
    body = '\n'.join(lines[u['sourceLine'] - 1:end])
    assert body.startswith(section + ' '), (section, body[:70])
    rows.append({'section': section, 'title': u['title'], 'owners': [name],
        'source': {'path': source_path, 'sha256': sha(W / source_path),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256(body.encode('utf-8')).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True,
            'readBatches': {'20': [[1,576],[577,1054],[1055,1340],[1301,1418]],
                            '21': [[1,455],[456,910],[911,1120],[1121,1268]],
                            '22': [[1,432],[433,810],[811,1115],[1116,1409],[1410,1730],[1731,2072]]}[u['chapter']],
            'figurePagesVisuallyInspected': pages[u['chapter']],
            'fullCurrentLessonRead': True, 'baselineCredit': False,
            'proofScope': 'Explicit conditional correctness arguments and counterexamples in Vietnamese; finite Python models supplement them. No engine or cluster execution claimed.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, teaching, 'teaching'),
                     anchor(name, example, 'worked-example-or-algorithm'),
                     anchor(name, argument, 'proof-or-argument'),
                     practice(name, q), practice(name, q, True)], 'gaps': []})

result = {'date': '2026-11-05',
 'scope': '83 assigned own-body units in DSC7e chapters20–22; seven current complete Vietnamese self-study lessons AD46/47/48/49/64/79/80. Other book/slide/USTH units receive no credit here.',
 'counts': {'assigned': 83, 'complete': 83, 'pending': 0},
 'reviewMethod': 'Reviewer read actual full own bodies in raw chapter files and all seven current lessons; inspected relevant source figures; kept useful earlier repairs, corrected remaining gaps, then froze hashes and exact witnesses. Matching strings below only locate reviewed content.',
 'ownBodyHashConvention': 'UTF-8 SHA256 of LF-joined splitlines from inclusive ownBodyLines, including numbered heading; own end is next numbered heading minus one, even when it is a child.',
 'lessonSnapshots': {name: {'path': f'lessons/{name}.md', 'lessonSha256': digest} for name, digest in FROZEN.items()},
 'figureReview': {'pdfPageNumbersOneBased': pages,
                 'images': 'tmp/pdfs/architecture-parallel-source/source-<PDFpage>.png; sheets0–6 personally inspected plus source1001/1002/1016.',
                 'interpretation': 'All relevant figures20.1–20.11,21.1–21.8,22.1–22.8 and Note20.1 inspected. Labels/arrows and table boundaries compared, not OCR-only credit.'},
 'sourceInterpretation': [
   'Historical hardware speeds, vendor feature lists and cloud legal examples are not asserted as current facts; lessons teach declared API/architecture models.',
   'Source consistent-hash prose uses predecessor direction and an inequality that leaves equality convention implicit; lesson explicitly uses inclusive predecessor tokens consistently, with boundary/wrap tests.',
   'Source cache-coherence/fence simplifications are not copied as portable CPU/compiler code; acquire/release publication and declared synchronization semantics are used.',
   'Source streaming prose repeats without state where context requires stateful recovery; lesson explicitly restores keyed/window state with source offsets.',
   'Finite tests are not a proof of distributed liveness, consensus or real-engine performance. All learner tasks remain specified as web models/editors/design submissions.'
 ],
 'validation': {'models': 'research/semantic-architecture-parallel-checks.json',
                'integrity': 'qa/architecture-parallel-ledger-integrity.json'},
 'units': rows}
dest = O / 'semantic-architecture-parallel.json'
dest.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Reopen the frozen ledger and independently verify every literal and source body.
saved = load(dest)
checked = 0
for row in saved['units']:
    s = row['source']
    assert sha(W / s['path']) == s['sha256']
    lo, hi = s['ownBodyLines']
    own = '\n'.join((W / s['path']).read_text(encoding='utf-8').splitlines()[lo - 1:hi])
    assert hashlib.sha256(own.encode('utf-8')).hexdigest() == s['ownBodySha256']
    for e in row['evidence']:
        p = R / e['path']
        assert sha(p) == e['lessonSha256']
        md = p.read_text(encoding='utf-8-sig')
        assert e['exactFragment'] in md and md.splitlines()[e['lineStart'] - 1].startswith(e['exactFragment'].splitlines()[0])
        checked += 1
    questions = re.findall(r'^\d+\. ', texts[row['owners'][0]].split('## Luyện tập')[1].split('## Gợi ý')[0], re.M)
    answers = re.findall(r'^\d+\. ', texts[row['owners'][0]].split('## Đáp án và lập luận')[1].split('## Biến thể và cách kiểm')[0], re.M)
    assert questions == answers
    assert all(k in {e['kind'] for e in row['evidence']} for k in ['teaching','worked-example-or-algorithm','proof-or-argument','activity','answer'])
model = load(O / 'semantic-architecture-parallel-checks.json')
assert model['status'] == 'pass' and model['lessonSha256'] == FROZEN
report = {'status': 'pass', 'assignedUnits': len(rows), 'completeUnits': len(rows),
          'exactWitnessesVerified': checked, 'ownBodyRangesVerified': len(rows),
          'perLessonUnits': dict(collections.Counter(r['owners'][0] for r in rows)),
          'lessonSha256': FROZEN, 'ledgerSha256': sha(dest),
          'models': model['cases'],
          'limits': 'Integrity and finite reference checks do not replace reviewer semantic judgments or certify any other book/slide/practice unit.'}
(R / 'qa' / 'architecture-parallel-ledger-integrity.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
