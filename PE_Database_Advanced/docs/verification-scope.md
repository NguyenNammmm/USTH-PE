# Phạm vi kiểm chứng và giới hạn triển khai

Ngày 06/11/2026. Đây là nội dung và đặc tả để đội dev triển khai khóa trên web. Hai cổng đối chiếu sách và slide đã đóng; backend production chưa được triển khai. Các bằng chứng dưới đây không thay thế nhau: một kết quả mô hình không phải SQL engine, một trace engine không phải chứng minh tổng quát, và kiểm cấu trúc file không phải kiểm đủ kiến thức của giáo trình.

## Engine MySQL

| Báo cáo | Phạm vi thực sự đã kiểm | Giới hạn |
|---|---|---|
| `qa/mysql-advanced-verification.json` | 32 ca PE trên MySQL8.4.13/InnoDB, gồm snapshot/current read, stale update, write skew, lock wait, NOWAIT/SKIP LOCKED, deadlock, timeout, DDL implicit commit và plan/result trên20.000 hàng | Không phải mọi SQL trong85 bài; không kiểm PostgreSQL, cluster hoặc native crash |
| `research/repo-checks/selected-repo-verification.json` | 21 kiểm của phần chọn: runtime, tám lịch Hermitage, sáu kiểm Chinook và sáu kiểm e-commerce/oracle/plan | Không chứng nhận toàn bộ repo hoặc ma trận isolation; kết quả timing chỉ có ý nghĩa ở môi trường đã ghi |
| `qa/apps-mysql-verification.json` | 33 ca routine/cursor/trigger/transaction, Company Minit/PK/FK/cycle và Northwind grain/fanout | Không thực thi blockchain, C extension, benchmark hoặc lịch hai session của mọi capstone |

Các JSON giữ actual/expected, version, SQL mode và phạm vi schema. Báo cáo là bằng chứng của lượt đã chạy, không phải lời hứa hoạt động CMS tương lai tự nhiên đúng. Dev cần chạy acceptance trên đúng image/version và fixture được phát hành.

## Mô hình và nội dung

`qa/model-verification.json` kiểm chín nhóm hàm JavaScript thuần: closure so với tập đóng, conflict graph, external sort, DP so với mọi parenthesization nhỏ, ROWS/RANGE, Merkle teaching oracle, G-counter và các trạng thái ARIES hữu hạn. Merkle helper này so trực tiếp lá để dạy cơ chế, không thực hiện hash mật mã. Mô hình DP chỉ xét parenthesization theo thứ tự cho trước của CROSS PRODUCT và cost đã nêu; nó không là optimizer thật.

`qa/independent-model-checks.json` giữ32 kiểm tính toán hữu hạn của lượt rà độc lập. `qa/independent-depth-review.md` ghi24 bài AD38–54 và AD61–67, excerpt nguồn đã đọc, các lỗi đã sửa và hash nội dung. Các báo cáo source-aware khác trong `qa/` chỉ xác nhận phạm vi nêu trong chính báo cáo. Không suy việc một bài được đọc thành chứng nhận riêng cho mọi tiểu mục của một chương.

Inventory có 947 địa chỉ sách, gồm cả parent và child; nguồn USTH có 448 trang lecture và 10 trang practice. Các ledger hiện hành đối chiếu toàn thân mục sách và từng trang slide với lời giảng, ví dụ, bài tập và đáp án tương ứng. Hai cổng đã đóng và `manifest.allContentComplete` là true. Cờ này xác nhận phạm vi nội dung đã đối chiếu; số bài, kiểm cấu trúc hoặc một lượt chạy engine riêng lẻ không thay cho bằng chứng đó.

Hai tiêu đề bắt đầu bằng số, §7.5.2 “3NF Decomposition” và §7.6.3 “4NF Decomposition”, đã được khôi phục sau khi đọc nguồn. Các báo cáo cũ dùng inventory 945 giữ nguyên dấu vết thời điểm của chúng. [Trạng thái đối chiếu hiện hành](semantic-coverage-status.md) gộp các ledger đã đọc toàn thân mục và kiểm hash: 947/947 địa chỉ có bằng chứng hiện hành. [Cổng slide](slide-semantic-coverage-status.md) ghi riêng 409 trang giảng và 49 trang không có nội dung giảng.

Lượt bổ sung `qa/design-pg-content-checks.json` có26 kiểm, gồm10 tính toán mô hình và16 ca MySQL thật. `qa/packaged-chinook-verification.json` có13 kiểm trên chính hash fixture đang đóng gói, gồm412 Invoice,2.240 InvoiceLine và11 foreign key không có orphan. Những nhóm bổ sung không làm thay đổi phạm vi các báo cáo cũ.

Các lượt đọc toàn thân mục sau đó có ledger `semantic-*.json` riêng, giữ địa chỉ nguồn, hash và đoạn giảng/bài tập/lời giải dùng để đối chiếu. Script gộp chỉ kiểm bằng chứng còn đúng phiên bản, không tự đánh giá chất lượng lời giảng. Những báo cáo dưới đây bổ sung cho nội dung mới:

| Báo cáo | Đã kiểm | Giới hạn |
|---|---|---|
| `qa/routine-full-checks.json` | 18 kiểm, gồm 2 ca MySQL 8.4.13 mới và 16 kiểm mô hình/cấu trúc cho AD85 | Không chạy mọi routine/native interface/trigger concurrent trong bài |
| `qa/lock-full-checks.json`, `qa/deadlock-full-checks.json` | FIFO/tree/abort và 4.096 graph bốn đỉnh so với oracle thứ tự topo | Mô hình hữu hạn; không là trace lock manager sản phẩm |
| `qa/timestamp-mvcc-full-checks.json` | 20 kiểm, 90 lịch TO nhỏ, 85 lựa chọn GC và một UPDATE kiểm version chạy trên SQLite | Không chạy PostgreSQL SSI hoặc MySQL cho nội dung mới này |
| `qa/advanced-concurrency-full-checks.json` | 15 kiểm, 24 lịch/cut build index và các ví dụ CAS/next-key/compensation/deadline | Không chạy atomic primitive native hoặc đo deadline |
| `qa/recovery-full-checks.json` | 12 nhóm kiểm, 18.720 ca log prefix/checkpoint/page-image và ba cách sửa sai bị phản ví dụ bắt | Mô hình before/after image với các giả định đã công bố; không crash engine |
| `qa/aries-backup-full-checks.json` | 16 kiểm, gồm 12 biến thể CLR/crash và các phản ví dụ về durability/redo-only | Không kiểm failover, fsync, NVRAM hoặc restore drill thật |
| `research/semantic-sql-foundations-checks.json`, `qa/semantic-apps-full-checks.json` | Query SQLite và mô hình hữu hạn cho phần SQL/calculus/application đã biên tập | SQLite không chứng minh cú pháp MySQL, framework web, SSO hay cryptography chạy đúng |

Các số đo thuộc các nhóm khác nhau, có thể dùng chung ví dụ; không cộng thành một con số chứng nhận toàn khóa. Sau một sửa Markdown, hash cũ có thể chỉ còn là bằng chứng lịch sử. Các kiểm trực tiếp trên fixture/code chỉ cần chạy lại khi phần liên quan hoặc kết luận đổi.

## Giao diện và PDF

Các lượt mới sau ZIPv2 gồm:

| Báo cáo | Đã kiểm | Giới hạn |
|---|---|---|
| `qa/distributed-commit-lock-full-checks.json` | 18 kiểm và2.448 trạng thái2PC nhỏ;local outbox/inbox SQLite | Không chạy XA/distributed cluster |
| `qa/replication-full-checks.json` | 14 kiểm;140 quorum fixtures,729 vector pairs,256 Merkle fixtures SHA256 | Không chạy replica cluster hoặc signature service |
| `qa/consensus-full-checks.json` | 17 kiểm;8.953 Paxos states,29.878 transitions và các Raft counterexamples | Hai ballot/ba acceptor hữu hạn;không là service Paxos/Raft native |
| `qa/blockchain-full-checks.json` | 16 kiểm;648 UTXO fixtures,14.858 BFT quorum pairs,SHA256/Ed25519 và SQLite | Không chạy chain,EVM,oracle hay token |
| `qa/university-full-checks.json` | 17 kiểm;đọc/parse mọi bảng mẫu AppendixA và query/FK SQLite chọn lọc | Không chứng minh MySQL two-session capacity protocol |
| `qa/usth-foundations-supplement-checks.json` | 21 kiểm;256 instance khóa nhỏ,35 câu/đáp án,query SQLite | Không kiểm MySQL collation/DDL/native runner |
| `qa/usth-lecture45-checks.json` | 19 kiểm;128 closure so oracle độc lập,năm FD systems,18 câu/đáp án,query SQLite | Không kiểm MySQL ALL variants,ONLY_FULL_GROUP_BY hoặc mọi SQL tương đương |
| `qa/usth-lecture67-checks.json` | 41 kiểm: 256 quan hệ ba ngôi nhỏ, 27 ca subtype, query SQLite và 15 ca MySQL 8.4.13 chạy thật; 20 câu có đáp án | Không chạy SQL Server; kiểm hữu hạn không thay chứng minh tổng quát; server task-local đã tắt êm |
| `qa/usth-final-sources-checks.json` | 106 kiểm: Music/University key/FK và số học, đủ SQL 36 nhiệm vụ practice cùng nhóm report/chart; 78 ca MySQL 8.4.13 | Chỉ fixture và biến thể được ghi; không suy mọi query tương đương trên mọi database hoặc runner production đã nghiệm thu |

Sách có 947/947 mục hiện hành; slide có 458/458 trang đã chốt, gồm 409 trang có nội dung giảng và 49 trang bìa/mục lục/chia phần. Hai cổng độc lập và kiểm hash hiện hành. Báo cáo PDF/release ghi hash của bản xuất; không dùng kiểm của snapshot Review-v2 cho PDF mới.

`qa/ui-dom-verification.json`, khi có, là kiểm logic DOM bằng jsdom: tìm/lọc bài, mở nội dung, đổi mô hình, các dạng đáp ứng theo seed và lịch sử dùng hỗ trợ. Đây không phải kiểm layout bằng trình duyệt thật. Lượt mở HTML qua browser bị chính sách URL chặn giao thức file; không dùng đường vòng hoặc đổi bề mặt để vượt giới hạn đó.

`qa/pdf-build.json` và báo cáo render ghi số trang,85 bài,24 bài trọng tâm, glyph và mẫu trang đã xem. Kiểm trích text không thay kiểm hình ảnh. Các minh họa trạng thái là nội dung biên soạn từ ví dụ, không mang nhãn lượt engine mới chạy.

## Dev còn phải kiểm khi triển khai

Runner cần kiểm end-to-end ở browser thật: cấp và thu hồi sandbox, credential/quota, hai session/barrier/observer, cancel query và cleanup transaction, reset idempotent, trạng thái lỗi hạ tầng, attempt version/seed và history hỗ trợ. DDL/performance/crash/cluster cần mức cô lập riêng theo `web-runner-spec.md`; schema riêng không tự cô lập mọi tác động.

Native PostgreSQL/C ABI, extension build, failover/crash/restore và hệ phân tán chưa có engine artifact trong gói. Các hoạt động này có đặc tả và bài đọc/model; chỉ mở nhãn engine-execution khi capability tương ứng đã được triển khai và chạy acceptance. Chưa có pilot chứng minh hiệu quả học tập hay ngưỡng mastery tối ưu.
