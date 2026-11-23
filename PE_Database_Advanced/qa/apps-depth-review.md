# Rà soát nguồn và độ sâu — 20 bài ứng dụng

Ngày 2026-11-05. Phạm vi chính xác: AD01, AD10–AD22 và AD68–AD73. Đã đọc nội dung hiện hành của cả 20 bài, kiểm mạch ví dụ, thuật toán/lập luận, bài tập/đáp án và phân biệt model với engine. Đối chiếu nguồn tập trung vào các đoạn trong bảng dưới. Đây là lượt kết thúc audit có giới hạn; không chứng nhận ngữ nghĩa toàn bộ 945 mục inventory, toàn bộ sách hoặc toàn bộ các bài nền.

Chỉ sửa 20 ID được giao và các file QA riêng ở đây. Không sửa proposal/inventory/manifest, AD60/AD81/AD82/AD85 hoặc bộ85 bài nền. Những sửa đã có trước lượt này ở AD13/AD14/AD16/AD17/AD21/AD69/AD71 được kiểm lại, không nhận là toàn bộ do lượt này tạo ra.

## Kết quả và các sửa cụ thể

- **AD22 — IQ17, P1:** toàn bài còn những đoạn tiếng Việt ghép liền, gây khó tự học. Đã viết lại mạch bài, giữ BFS, weights, graph identity, bài tập và lời giải; thêm transfer graph có dữ liệu cụ thể. Source header/footer được sửa: graph/BSP ở §10.6; §22.8 là parallel streaming.
- **AD22 — P1:** bất biến Bellman–Ford “sau k vòng là paths không quá k cạnh” đòi snapshot vòng trước. Thêm pseudocode đồng bộ với copy/read-old/write-next, induction, hai trạng thái số, early stop và negative-cycle flag. Phân biệt vùng chịu ảnh hưởng negative cycle với những đỉnh còn shortest distance hữu hạn. BSP thêm vote-to-halt, message chưa giao, trace qua hai partitions và MIN-idempotence khác SUM-replay.
- **AD15 — P1:** point bucket quadtree bị gọi là region quadtree. Sửa thành PR quadtree, giải riêng region quadtree cho raster. §24.4.2 có quadratic split nhưng bài chỉ nêu tên split heuristic: thêm seed/preference/occupancy algorithm, coverage invariant, dừng/chi phí O(M²) và trace bốn boxes. Phân biệt heuristic chọn child trong đoạn sách với heuristic mở rộng area nhỏ nhất thường dùng; không nhận là cùng quy tắc.
- **AD18 — P2:** thêm cơ chế nguồn §16.5.2 cho projection witness count, selection, first/last match của outer join và propagation qua expression; có ca không được giữ hàng bù khi match đầu xuất hiện. Thêm hai hướng rewrite dùng view hoặc mở lại định nghĩa theo §16.5.3. Các delta laws, NULL/count state và cross term đã có được giữ và kiểm lại.
- **AD21 — P2:** §10.5.2 còn có CEP và lambda architecture chưa được giải. Thêm pattern fail/fail/success với state/thời hạn, ca hết hạn, và hai nhánh stream/batch có report10/18 cần replacement theo version. Giữ đúng hopping/sliding và late-final policy đã sửa trước lượt này. Viết lại những đoạn luyện tập/đáp án/feedback/web còn ghép liền.
- **AD71 — P2:** ngoài k-means, §11.4.5 còn có hierarchical clustering và collaborative filtering. Thêm agglomerative single-link algorithm, invariant/dừng/chi phí, merge heights2,2,6 so complete-link10; ratings fixture có missing khác0 và cold-start/holdout. Bài tập thứ5 và đáp án đi kèm. Apriori prefix-generation/prune trước counting đã có được kiểm lại.
- **AD72 — P2:** thêm combined ROLLUP và GROUPING SETS theo §11.3.3, các grouping cụ thể, totals30/5/15/20 và cách diễn bằng UNION ALL trên MySQL. Sửa những đoạn đáp án/web/footer còn ghép liền.
- **AD16 — kiểm lại, không phát hiện lỗi số mới:** interval DFS/path-index ở §30.6.2.5 đã có ví dụ, predicate ancestor/child, proof và giới hạn insert; SQL/XML có NULL/empty/constructor example. Các phần mới này là mô hình PE có nhãn, không được gắn là engine XML đã chạy.
- **Các bài còn lại:** không phát hiện lỗi số/counterexample chắc chắn trong phạm vi đọc này. Giữ cơ chế cụ thể: AD01 bag/NULL/outer join; AD10 recursion/window; AD11 transaction/retry; AD12 grant graph; AD13 RDF event identity; AD14 nested collection cross product; AD17 postings/top-k; AD19 evaluation; AD20 combine/retry; AD68 schema/XPath; AD69 TF-IDF/HITS/PageRank; AD70 classifiers/regression; AD73 metadata/shard/CAS.

Đã sửa thêm153 occurrences bằng các cặp thay thế chính xác có review ở17 bài, ngoài các đoạn viết lại nêu trên. `apps-depth-spacing-changes.json` ghi từng cặp/count; fenced code, inline code và URLs được bảo vệ. Không chạy generic word segmentation. Diagnostic hiện có của `check_spacing.py` không còn đề xuất tách từ trong20 bài; điều này chỉ là kiểm hỗ trợ, không phải chứng nhận toàn bộ tiếng Việt hoàn hảo.

## Đoạn nguồn đã đọc trực tiếp trong lượt này

Số dòng tính từ các TXT trích sách trong `tmp/database-source`; các phạm vi là targeted source reads, không ngụ ý đã audit mọi subsection được metadata gán.

| Bài | Đoạn nguồn đã đọc | Nội dung đối chiếu |
|---|---|---|
| AD01 | chapter-2:1770–1801; chapter-3:1322–1403; chapter-4:605–664 | Equivalent queries; NULL/UNKNOWN/duplicates; outer-join rows bù. |
| AD10 | chapter-5:1393–1464,1874–1938 | Closure iteration, finite visited state; window order/ranges. |
| AD11 | chapter-5:444–503 | Python parameter/commit/rollback; phân biệt driver/API, còn request-id protocol là PE bổ sung. |
| AD12 | chapter-4:2840–2927; chapter-9:1679–1726 | Grant path/cycle/revoke/role; end-user identity và application authorization. |
| AD13 | chapter-8:451–517 | Shared-variable SPARQL joins, predicate variable, n-ary event representation. |
| AD14 | chapter-8:518–577; online-29:529–653 | Object-relational/ORM khác nhau; flatten nhiều collections và nesting. |
| AD15 | chapter-8:980–1061; chapter-24:489–653 | Geometry representation; PR/raster quadtrees, R-tree overlap, quadratic split. |
| AD16 | online-30:1201–1280,1301–1390,1471–1615 | FLWOR/functions/types; DOM/SAX; relational mapping/native XML/SQL/XML. |
| AD17 | chapter-8:745–804; online-31:557–661 | Keywords, inverted/positional postings, top-k conditions, precision/recall. |
| AD18 | chapter-16:1478–1689; chapter-11:209–273 | Maintenance operations, expression delta, view rewrites/selection; fact/dimension context. |
| AD19 | chapter-11:1263–1642 | Mining tasks, classifiers, regression, association, clustering, text mining; leakage protocol is PE extension. |
| AD20 | chapter-10:703–752,882–941 | Word-count contributions; map/shuffle/reduce task flow. |
| AD21 | chapter-10:1501–1640 | Continuous query, punctuations/windows, CEP/lambda, hopping/sliding/session/stream joins. |
| AD22 | chapter-10:1756–1875 | Graph representations/path queries; MapReduce-style processing versus BSP, messages and halt. |
| AD68 | online-30:741–860,864–953 | Schema types/keys/namespaces; XML tree and XPath context/order. |
| AD69 | online-31:126–305,311–448 | Exact1/df variant, cosine, random walk/PageRank, clicks/anchor text/HITS/spam. |
| AD70 | chapter-11:1320–1502 | Tree/Bayes/SVM/neural/regression; detailed fitting proofs are PE extension. |
| AD71 | chapter-11:1503–1642 | Association/confidence; hierarchical clustering and collaborative filtering. |
| AD72 | chapter-11:209–273,1141–1210 | Fact/star/snowflake; combined ROLLUP, GROUPING SETS, reporting. |
| AD73 | chapter-10:257–331 | DFS metadata/block replicas/read path; CAS/cutover examples are PE extensions. |

## Kiểm và giới hạn bằng chứng

`python qa/apps_depth_checks.py` đạt32/32 finite reference checks. Chúng kiểm BFS bằng queue reference, hai bounded-walk states của weighted example, quadratic split arithmetic, delta/witness cases, TF-IDF/cosine/PageRank/HITS/AP, window/watermark/CEP, confusion/Gini/association/clustering/cube/DFS-label calculations. Cả20 bài có đủ sáu phần, fences cân bằng và ít nhất4 câu hỏi với đáp án đánh số khớp; AD71 hiện có5 câu.

Không chạy SQL/XML/RDF/native graph/cluster trong lượt này. Không cộng32 checks này vào số SQL/engine checks của root. Proof tổng quát nằm trong lời giảng và được đọc theo giả định; finite checks không thay proof. Chưa xem render PDF/HTML cuối; root cần rebuild và QA layout từ hashes cuối. Hashes của20 bài nằm trong `apps-depth-review.json` và `apps-depth-model-checks.json`; sửa tiếp làm snapshot này cũ.

## Mapping corrections giao root

Reviewer không sửa metadata. Root đã báo cập nhật các ownership dưới đây sau khi nhận phát hiện; danh sách giữ lại mismatch đã phát hiện và đích đề xuất để truy vết, không phải trạng thái lỗi còn mở.

1. §8.3/8.3.1/8.3.3/8.3.4 thuộc AD17; §8.3.2/8.3.2.1/8.3.2.2 thuộc AD69. Proposal trước đây gom chúng vào AD14, trong khi AD14 dạy §8.2/online29.
2. §30.4.1–30.4.2 được dạy ở AD68, trước đây primary gán AD16. AD16 tiếp tục §30.4.3–30.7.
3. §10.3 và §10.3.1–10.3.6 thuộc AD20; proposal trước đây primary gán AD73, trong khi AD73 dạy §10.1–10.2.
4. AD18 trước đây có sectionIds rỗng dù dạy §16.5.1–16.5.2.5. Đề xuất primary maintenance ở AD18, secondary ở AD37; AD37 giữ primary optimization/selection §16.5.3–16.5.4. Việc chọn primary cuối thuộc root.

IQ17 về readability của AD22 được xử lý ở snapshot có hash trong JSON. Không còn lỗi cụ thể đã xác định mà reviewer này để nguyên trong20 bài; đó không phải tuyên bố mọi kiến thức nguồn đã hoàn thiện hay mọi hoạt động web đã triển khai.
