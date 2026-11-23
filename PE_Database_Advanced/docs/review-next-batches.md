# Đối chiếu nguồn và kiểm bản xuất

Ngày 06/11/2026. Đã chốt đủ 947 thân mục sách và 458 trang USTH bằng đối chiếu nguồn/Markdown hiện hành. Bản ZIP Review2026-11-05 giữ như mốc lịch sử. Bản xuất mới chỉ được bàn giao khi hash inputs, PDF/HTML và các kiểm tương ứng còn khớp.

## Bằng chứng mới sau bản Review

- AD05–AD08: ledger normal forms đã đóng33 mục nguồn, sửa điều kiện JD/MVD và trình bày PJNF/DKNF cùng caveat/nguồn nghiên cứu. Có15 kiểm hữu hạn và219 witness được kiểm hash.
- AD85: đã đọc đủ tám thân mục5.2–5.3.3, bổ sung function/table function/PSM/external ABI/triggers/replay;18 kiểm mới gồm16 model/structure và2 ca MySQL8.4.13. `research/semantic-routines.json` giữ witnesses hiện hành.
- AD27/28/29/30/74: đã đối chiếu 48 mục index; AD28 bổ sung concurrency theo đúng §18.10.2 và giữ nguyên 79 đoạn bằng chứng cũ khi cập nhật hash. Nhóm query operators đã đối chiếu thêm 54 mục.
- AD16/68: đã đối chiếu 30 mục XML, có 28 kiểm thực trên .NET/DTD/XSD/XPath 1.0; không tính thành chạy XQuery hoặc SQL/XML. AD17/69 bổ sung 27 mục information retrieval và 24 kiểm, trong đó một query PageRank chạy trên SQLite.
- AD01/02/10: đã đối chiếu 80 mục SQL/calculus, bổ sung 33 câu luyện và lời giải; 22 kiểm hữu hạn/SQLite. AD11/12: 85 mục application/SQL schema/security, có 34 kiểm hữu hạn/SQLite; không suy thành kiểm framework hoặc security production.
- AD09: 48 mục ER/design, 21 kiểm mô hình, gồm 10.240 ca coverage của khoảng thời gian.
- AD38–42, AD63 và AD67: các phần transaction, lock, deadlock, timestamp, MVCC và advanced concurrency có ledger riêng. AD40 có 4.096 graph nhỏ được so với oracle; AD41/42 có 20 kiểm mô hình và một ca version update SQLite. Không dùng số ca hữu hạn thay chứng minh tổng quát.
- AD43–45: đã đối chiếu toàn bộ 35 mục recovery của chương 19. AD43 có 18.720 ca prefix/checkpoint/page-image, AD44/45 có 16 kiểm với 12 biến thể crash/CLR. Đây là mô hình; chưa làm crash/restore/failover engine thật. §17.3 được đối chiếu riêng qua phần storage trong AD43.

## Mốc mới: hoàn tất sách, tiếp tục từng trang USTH

Đã đóng ledger cho toàn bộ947 own-body sách bằng đối chiếu nguồn/Markdown hiện hành: các nhóm architecture/parallel83,optimizer/big-data78 (gồm7 mục chia sẻ đã được đối chiếu lại),PG/tuning91 và phần distributed/replication/consensus/blockchain/University do root hoàn thiện. Mốc này không tự đóng slide hoặc chứng minh mọi engine đã chạy.

Slide đã chốt 458/458 trang: Lecture 1–3 gồm 180 trang, Lecture 4–5 thêm 92, Lecture 6–7 thêm 107, Lecture 8–9 và Practice 1–3 thêm 79. Tổng 409 trang có nội dung giảng và 49 trang bìa/mục lục/chia phần. Các trang cuối được đọc/so sánh trực tiếp; không lấy file render hoặc keyword làm tín chỉ hoàn tất.

Mười một phần bổ sung có 151 câu hỏi/đáp án. USTH06/07 có 41 ca kiểm, trong đó 15 ca MySQL; USTH08–11 có 106 ca, trong đó 78 ca MySQL 8.4.13. Chưa kiểm SQL Server. Manifest giữ đủ các phần này để đưa vào HTML/PDF; không dùng kiểm của snapshot 619 trang cũ thay cho bản xuất mới.

## Những phần còn phải chốt

Lấy `research/semantic-gate-summary.json` và `research/semantic-slides-gate-summary.json` làm chỉ mục hiện hành. Hai cổng nguồn đã đóng; bốn đầu ra phải được kiểm đồng bộ bằng reports của bản xuất. Việc chưa triển khai runner production không là deliverable thiếu: mục tiêu đã chốt là đặc tả đầy đủ và demo tương tác cho dev.

Đọc source theo own-body với parent introduction riêng. Với một mục cần sửa, phải có lời giảng, ca làm việc, thuật toán/lập luận nếu nguồn có, hoạt động và lời giải thật. Có thể dùng kiến thức nền đã đọc kiểm trực tiếp, không dùng nhãn chapter hoặc keyword để suy đủ.

Sau mỗi batch: kiểm source/lesson witness hashes, trộn ledger, kiểm lại hoạt động bị thay, tạo lại24 sơ đồ nếu Markdown đổi, rồi rebuild bốn đầu ra và kiểm PDF render. Không cần lặp toàn bộ engine QA cũ nếu code/fixture và kết luận của nó không đổi; ca mới có bằng chứng riêng.

## Môi trường tạm

Lượt kiểm AD85 đã dùng server task-local MySQL8.4.13, chỉ tạo schema mới ngẫu nhiên; không có DROP. Kiểm process từ sandbox mặc định từng không thấy các process ở quyền cao hơn, nên bước cleanup đã dùng kiểm quyền phù hợp để xác minh đúng executable/config. Sau graceful shutdown port33374, kiểm quyền phù hợp xác nhận không còn process MySQL của tác vụ. Không dừng dịch vụ khác.
