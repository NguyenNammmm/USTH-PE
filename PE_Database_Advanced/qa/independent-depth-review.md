# Rà soát độc lập độ sâu, tính đúng và khả năng tự học

Ngày 2026-11-05. Đã đọc toàn văn 24 bài được giao: AD38–AD54 và AD61–AD67; đối chiếu nội dung gốc ở các đoạn nguồn nêu trong bảng. Các sửa trực tiếp chỉ nằm trong 24 ID này và thư mục QA. Không chỉnh các bài còn thiếu của tác giả khác hoặc bộ85 bài nền.

Đây là rà soát nguồn và lập luận, không lấy việc có heading/manifest làm bằng chứng đã dạy đủ. source-section-inventory.json giữ945 mục làm bản đồ vị trí; bảng dưới chỉ rõ các đoạn gốc thực đã đọc kỹ. Báo cáo này không ký nhận toàn bộ945 mục,448 trang lecture hay10 trang practical đã hoàn thành tự học. Các scope lớn cần giữ nguồn evidence của những reviewer khác.

## Kết quả kiểm

- 32/32 kiểm hữu hạn bằng model/reference arithmetic đạt; 24/24 bài có đủ sáu phần, fences cân bằng và số câu hỏi/đáp án liên tiếp, tối thiểu4 câu. Script `independent_model_checks.py` và kết quả `independent-model-checks.json` lưu bằng chứng. Đây không phải chứng minh thuật toán tổng quát.
- Không chạy SQL/native cluster, crash engine, restore hoặc compile PostgreSQL extension trong lượt này. Native MySQL/repo evidence do root quản lý riêng; không cộng32 model checks này vào số SQL checks.
- Chuỗi tiếng Việt dính được sửa bằng viết lại đoạn đã đọc và thay cụm chính xác có review. Không chạy generic word segmentation hoặc tách số mù; code fences/inline code được bảo vệ trong phase thay cụm. `independent-manual-spacing-changes.json` lưu104 nhóm thay cụm; các đoạn viết lại được mô tả trong flags.
- Reviewer PostgreSQL đã đọc lại các block mới MV2PL/logical undo/distributed validation/clock so với nguồn gốc và không thấy lỗi chắc chắn. Hai điểm precision về timestamp bounds và safe time đã sửa. Proof tree protocol là lập luận biên soạn theo mô hình sách, chưa có kiểm chứng hình thức hoặc peer certification riêng.

## Các lỗi và lỗ hổng đã sửa

- **AD39 §18.1.3 (P1)**: Acyclic fixed lock placement was incorrectly too weak to establish converse for read/write schedules. → Added r1(X),w2(X),r3(Y),w1(Y), acyclic graph3→1→2, and lock-interval contradiction for all2PL placements.
- **AD41 §18.6 (P2)**: Third parallel-write validation case was attributed to supplied section, whose text gives two serialized-write cases. → Labeled source cases versus pedagogical extension; made abort mutex cleanup explicit.
- **AD42 §18.7.2 (P1)**: MV2PL was a paragraph without counter,∞ versions or commit-publication procedure. → Added algorithm, reader-before/after trace, conflicting updater and GC boundary, serial-order argument, fifth exercise/answer.
- **AD43 §19.4.1–19.4.2 (P1)**: Redo every ordinary update could resurrect a transaction that already finished rollback before crash. → Scoped toy history and added completed-abort counterexample plus source redo-only rollback records/undo-list handling.
- **AD44 §19.9.2 (P2)**: Second crash stated storage pageLSN60 without a flush between redo and crash. → Added explicit WAL-valid P flush at60 while log60 durable.
- **AD44 §19.8.2–19.8.3 (P1)**: Logical undo discussion omitted begin/end/abort/skip protocol and risked conflating ordinary physical logging with ARIES CLR. → Added separate algorithm, incomplete-operation and interrupted-inverse behavior, numeric successor-preserving compensation and solved task.
- **AD51 §23.4.2.2–23.4.2.4,23.4.3.2 (P1)**: Quorum intersection/register explanation did not teach source majority locks, biased/weighted quorum or chain replication. → Added all protocol rules, weight example, single-item deadlock and chain read-tail/failure cases; preserved distinction from register.
- **AD52 §23.7.2,23.8.2 (P1)**: Election mechanisms were omitted and Paxos proof could be read as induction over real-time acceptance after chosen event. → Added source election cases and induction on smallest higher-numbered proposal sending another value.
- **AD53 §25.1.4.4 (P1)**: Tuning narrative omitted workload compression and greedy index/view search with recomputation. → Added weighted cost, pseudocode, finite termination/cost, interaction trace, greedy counterexample, maintenance case and exercise.
- **AD63 §18.10.1 (P1)**: Online build was named without final catch-up/publication barrier. → Added snapshot/log/build/replay/final shared-lock/catalog algorithm, insertion/deletion/boundary cases and solved task.
- **AD64 §21.5 (P1)**: Global index narrative lacked concrete partitioned secondary-index construction and duplicate partition-key identity. → Added(Ki,Kp,Ku),two-hop routing, exact two-hit trace and update atomicity/freshness choice.
- **AD65 §23.3.7,23.5.1 (P1)**: Distributed validation and global clock snapshot lacked source rejection/commit-wait/read-wait mechanisms. → Added late-old timestamp abort, StartTS≤TS≤FinishTS, interval model, numeric trace, pending≤r/safe-time guard and ticket model.
- **AD61 §27.4.3–27.4.7 (P2)**: Nonrecursive operation semantics and stratification direction were too compressed; broad negative-rules rubric could be vague. → Added join/projection/union/difference mapping, explicit stratum inequalities and a guarded eligiblepath solution.
- **AD43 §19.2.1 (P2)**: Two-copy storage was mentioned without controlled write/recovery cases. → Added write1/check/write2/ACK plus equal/invalid/differing-copy recovery and three failure cases.
- **AD46 §20.4.5.2 (P2)**: Shared-memory discussion named coherence without illustrating cache-line ownership and ordering. → Added MESI model, data/flag visibility countercase and false sharing; avoided claiming universal assembly recipe.
- **AD38–AD54,AD61–AD67 §prose (P1)**: Many Vietnamese tails were concatenated and unreadable even though headings existed. → Manual paragraph rewrites and explicit reviewed phrase replacements; fenced/inline code excluded from phrase substitutions; no generic numeric splitting.

## Evidence theo bài

| ID | Phạm vi nguồn | Đoạn gốc đã đọc kỹ | Nội dung cụ thể đã kiểm/sửa |
|---|---|---|---|
| AD38 | §17.1–17.10 | `chapter-17.txt:549–860` | Conflict graph, acyclicity theorem, view equivalence and recoverability separated; three counterexamples and witnessed edges. |
| AD39 | §18.1,18.3 | `chapter-18.txt:238–361;422–531;711–868` | Lock-point proof, explicit 2PL converse counterexample, tree auxiliary lock-order graph, intention compatibility. |
| AD40 | §18.2,18.4 | `chapter-18.txt:532–710;869–1039` | Wait graph differs from conflict graph; wait-die/wound-wait age proof, timeout/deadlock distinction and web barriers. |
| AD41 | §18.5–18.6 | `chapter-18.txt:1040–1349` | TO and Thomas guard precedence; source two validation cases separated from parallel-phase extension; abort releases publication mutex. |
| AD42 | §18.7–18.9 | `chapter-18.txt:1365–1480;1503–1585` | MVTO plus actual MV2PL counter/infinity-version/rigorous2PL algorithm, three cases and solved exercise; SI/write skew kept distinct. |
| AD43 | §19.1–19.6 | `chapter-19.txt:68–128;584–715` | Stable-storage two-copy transfer/recovery; WAL proof and undo ordering; toy restart scope excludes earlier rollbacks and shows redo-only compensation fix. |
| AD44 | §19.8–19.9 | `chapter-19.txt:1173–1255;1434–1638` | ARIES redo/undo/CLR trace and repeated crash; operation-begin/end/abort logical rollback explicitly separate from ARIES CLRs. |
| AD45 | §19.7,19.10 | `chapter-19.txt:983–1123;1674–1721` | Remote receive/durable/apply distinction, fencing, backup/PITR and deterministic command recovery; no native restore claim. |
| AD46 | §20.1–20.4 | `chapter-20.txt:438–575;795–975` | Architecture, Amdahl and traffic bounds; cache coherence/ordering and false-sharing cases added with hardware-model scope. |
| AD47 | §21.1–21.4 | `chapter-21.txt:67–454;511–616` | Half-open routing, key skew/salting correctness, ownership epochs and snapshot/delta cutover invariant. |
| AD48 | §22.1–22.4 | `chapter-22.txt:99–431;440–492` | Bag-correct repartition/broadcast/grid join proofs, range sort and aggregate partial states; explicit cost-model labels. |
| AD49 | §22.8–22.9 | `chapter-22.txt:1566–1637;1875–2013` | Semijoin shipping algorithm keeps duplicate identities; proof/termination/cost and counterexample; integration/stream checkpoint contracts readable. |
| AD50 | §23.1–23.2 | `chapter-23.txt:148–419` | Durable prepared/decision ordering, indistinguishability in-doubt example, blocking and retry identity; not presented as native XA. |
| AD51 | §23.4 | `chapter-23.txt:1039–1100;1175–1219` | Source majority/biased/weighted lock protocols and chain added; register/tag/write-back model clearly separate. |
| AD52 | §23.7–23.8 except Raft | `chapter-23.txt:2038–2168;2272–2370` | Election withdrawal/re-entry/partition cases separated from Paxos; Paxos proof now induction over proposal numbers rather than chronology. |
| AD53 | §25.1–25.5 | `chapter-25.txt:339–415;961–1112;1407–1505` | Compressed weighted workload, what-if cost and greedy recomputation algorithm with optimality counterexample; LDAP identity/scope readable. |
| AD54 | §26.4 | `chapter-26.txt:503–682` | Toy PoW probability, honest quorum intersection, honest locking assumptions and double-spend validity distinct from consensus. |
| AD61 | §27.4 | `online-27.txt:562–758;759–990` | Set fixpoint proof, nonrecursive operations, linear semi-naive versus two-IDB counterexample, explicit stratum inequalities and guarded negation. |
| AD62 | §23.8.3–23.8.5 | `chapter-23.txt:2371–2569` | Old-term majority counterexample, current-term commit rule, up-to-date voting, matching-prefix and membership/read limitations. |
| AD63 | §18.10 | `chapter-18.txt:1941–1993;2088–2414` | Online index snapshot/delta/final barrier algorithm and boundary cases added; CAS/ABA, operation semantics and deadline models readable. |
| AD64 | §21.5–21.7 | `chapter-21.txt:617–792;793–909;1120–1219` | Global secondary relation(Ki,Kp,Ku), two-hop lookup, duplicate-key identity trace; DFS snapshot/API/CAS scope explicit. |
| AD65 | §23.3,23.5 | `chapter-23.txt:859–936;1267–1453` | Late-old validation timestamp abort, local timestamp inequalities, interval commit-wait and safe-time read rule, ticket capability scope. |
| AD66 | §23.6 | `chapter-23.txt:1465–1999` | CAP indistinguishability, version concurrency, proved grow-only counter and Merkle canonical/range assumptions; merge metadata not business resolution. |
| AD67 | §1.1–1.9 | `chapter-1.txt:167–286;287–549;760–1193` | Continuation framing, abstraction/data-independence semantics and historical architectural tradeoffs; concrete contracts rather than product rankings. |

## Spot checks ngoài phạm vi chỉnh sửa

AD03: proof Armstrong/closure có soundness, dừng, completeness bằng phản mô hình và assumption domain đủ hai giá trị. AD31: tombstone, retention và publication invariant có ca làm lộ phục sinh key. Không thấy lỗi cụ thể qua lần đọc này; đây không thay một audit từng subsection nguồn của hai bài ấy.

AD22 hiện có BFS/relaxation/graph identity/message invariant thực chất, nhưng còn nhiều chuỗi tiếng Việt dính ở snapshot đã đọc. Đã chuyển cho owner advanced_finish_apps để sửa; cần dùng hash sau sửa để đóng flag IQ17. Không sửa file ngoài quyền sở hữu.

AD83/AD84 chỉ được spot-read phần mở đầu tới lifetime/slot: Reset/Delete, assertion-only castNode, Datum cần type/isnull ngoài payload, heap không phải Datum[] và alias versus owned copy đều được nói rõ. Chưa chứng nhận ABI hay toàn bộ bài.

## Giới hạn cần giữ khi đóng gói

Model, proof và native execution là ba loại bằng chứng riêng. Các bài mới giữ nhãn model và capability backend; không được chuyển chúng thành thông báo đã triển khai runner. Luyện tập của các bài đã sửa dùng editor/canvas/proof hoặc sessions do backend giữ, không bắt learner cài engine/terminal.

Cần rebuild các PDF/HTML/slide-derived artifacts từ Markdown sau các sửa này và QA layout ở cấp đóng gói. Báo cáo độc lập này chưa xem render cuối. `independent-depth-review.json` có source ranges, line headings và hashes để biết snapshot được kiểm; đổi bài sau đây làm hash evidence cũ hết hiệu lực.
