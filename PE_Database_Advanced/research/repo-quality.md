# Kiểm định repo cho phần Database Advanced

Ngày kiểm: 05/11/2026. Phần này nối tiếp 85 bài Database PE. Người học dùng web; repo được dùng làm nguồn để chọn và biên tập lab, không yêu cầu học viên clone/cài database. Đầu ra hiện tại là đặc tả và tài liệu cho dev, chưa có runner web được triển khai.

Đã tìm nguồn qua GitHub connector và web, đọc license/README/source rồi clone bốn repository công khai vào `tmp/database-advanced-repos/`. Mỗi bản được khóa bằng commit và hash file trong `repo-registry.json`. Không chạy script cài đặt của repo hoặc dùng số sao để quyết định chất lượng. Báo cáo này duyệt **phần được chọn**, không chứng nhận toàn bộ repository.

## Cổng kiểm định

Một phần nguồn được đưa vào khi xác định được tác giả/quyền dùng, có mục tiêu học phù hợp sau 85 bài, chạy lại được trên hệ được ghi, có oracle kiểm hành vi và có cách chuyển sang web. Với bài hệ thống, kết quả mô hình khác kết quả chạy hai kết nối thật. Nếu một cổng chưa đạt, phần đó phải được sửa và kiểm lại hoặc để ngoài đường học.

Khóa thu phí vẫn phải giữ các notice/quyền của phần nguồn được dùng. MIT và CC BY 4.0 được xem xét theo văn bản grant cụ thể, không suy từ việc repo công khai. Phần tài liệu/ảnh/assessment của bên thứ ba không tự nhận license chỉ vì nằm gần code MIT. Quyền dùng repo cũng không làm cho một autograder yếu trở thành đủ tin cậy.

## Kết quả chọn nguồn

| Repo | Quyết định | Phần dùng trong khóa | Bằng chứng chính |
|---|---|---|---|
| ept/hermitage | Nhận các ca đã biên tập và chạy lại | Isolation trên hai session: dirty read, snapshot/predicate read, lost update | 8 ca MySQL 8.4.13; quan sát lock wait thật |
| jsengun/ecommerce-query-optimizer-demo | Chỉ nhận phần đã sửa và thêm oracle | Thí nghiệm composite index, kiểm kết quả trước/sau và đọc plan | 5 test gốc pass nhưng không phát hiện helper trả rỗng; oracle PE bắt 3 mutant và đối chiếu MySQL độc lập |
| lerocha/chinook-database | Nhận fixture MySQL được chọn | Đối soát doanh thu, grain, window và bài SQL mới của PE | Load script; kiểm số dòng/FK/DECIMAL; 412 running totals so với Python Decimal |
| cmu-db/bustub | Chưa tích hợp vào bài bắt buộc | Tài liệu tham khảo cho nhánh triển khai DBMS sau này | Chỉ đọc source; chưa build/test C++, skeleton còn TODO và test bị disable |

Ba nguồn đầu không đồng nghĩa ba ngân hàng đề đã hoàn chỉnh. Hermitage cung cấp lịch kiểm isolation; Chinook cung cấp dữ liệu; bài index được sửa về oracle và ngữ nghĩa hệ. Câu hỏi, gợi ý, fixture chuyển giao và rubric của khóa được biên soạn riêng.

## Hermitage: tên isolation không đủ mô tả hành vi

Nguồn: [repository](https://github.com/ept/hermitage), [mysql.md tại bản đã khóa](https://github.com/ept/hermitage/blob/f029bec8e32af6a9506508638fdf74ef61286225/mysql.md). License: CC BY 4.0, tác giả Martin Kleppmann. Bản `mysql.md` ghi kết quả trên MySQL 5.6.21, nên khóa mới không dùng nguyên bảng kết quả đó để khẳng định MySQL hiện tại. Biến cũ `@@tx_isolation` được thay bằng `@@transaction_isolation`; từng ca được chạy lại trên 8.4.13/InnoDB.

Tám ca được kiểm: aborted read ở READ UNCOMMITTED/READ COMMITTED; đọc lặp lại sau commit ở READ COMMITTED/REPEATABLE READ; predicate read sau insert ở hai mức đó; stale assignment gây lost update; bản PE sửa bằng phép cộng tại server. Hai kết nối là hai transaction thật. Với cập nhật bị chặn, script quan sát đúng requesting connection trong `performance_schema.data_lock_waits`, rồi commit transaction giữ khóa để cho bên chờ tiếp tục. Không dùng một lệnh sleep để tự kết luận có khóa.

Kết quả chọn: stale assignment từ hai lượt đọc 10 cho giá trị cuối 11; `value=value+1` cho 12. Điều này kiểm một lịch cụ thể. Chưa kiểm toàn ma trận Hermitage, PostgreSQL, mọi anomaly hay mọi lịch của InnoDB. Bản sửa atomic increment giải bài cộng một item này, không tự bảo vệ mọi invariant nhiều hàng.

Đưa lên web thành hai editor A/B và một timeline sự kiện đo thật. Người học dự đoán, chạy từng bước rồi sửa query. Runner giữ hai connections cùng attempt và bảo đảm thứ tự/barrier; khi reset phải rollback, đóng connections và tái tạo schema. Animation có thể dùng trước để hiểu, nhưng nhãn “đã chạy” chỉ xuất hiện khi có event từ engine. Attribution và mô tả thay đổi được giữ trong màn nguồn của bài.

## Repo index: test xanh vẫn có thể bỏ sót query sai

Nguồn: [repository tại commit](https://github.com/jsengun/ecommerce-query-optimizer-demo/tree/c594df3824a82db731946a3fa106ccd679eb1848), [test gốc](https://github.com/jsengun/ecommerce-query-optimizer-demo/blob/c594df3824a82db731946a3fa106ccd679eb1848/tests/test_queries.py). License MIT, Jennifer Sengun.

Năm test gốc đã chạy và pass. Sau đó giữ source nguyên vẹn nhưng tạm thay ba helper query trong bộ nhớ để chúng luôn trả `[]`. Cả năm test vẫn pass: các phép `all(...)`, kiểm list đã sort và `isinstance(...,list)` không buộc có đúng dòng. Test plan còn chạy trực tiếp hằng SQL đúng nên không nhìn thấy helper bị hỏng. Đây là lý do bộ checker gốc không được đưa thẳng vào khóa.

Phần được nhận đã có kiểm bổ sung: fixture nhỏ chứa giá đúng hai biên, sai category, rating thiếu ngưỡng và giá ở ngoài khoảng; oracle cụ thể bắt ba hành vi sai gồm bỏ category, bỏ rating và trả rỗng. Bản MySQL dùng 10.000 sản phẩm, so ID/thứ tự với lọc Python Decimal độc lập, rồi đối chiếu kết quả trước/sau index. EXPLAIN thực tế đổi từ ALL sang dùng index đã tạo trên bộ dữ liệu đó. Thứ tự `price,id` được ghi rõ để xử lý tie. Không nhập các số “tăng tốc” từ README hoặc khẳng định mọi range query chỉ tốn O(log N).

Trên web, người học giữ cùng query/fixture, đề xuất index, xem plan và chứng minh kết quả không đổi. Chấm theo đúng dữ liệu, chỉ số/plan được quan sát và lời giải thích về equality/range; thời gian là số đo có bối cảnh, không phải ngưỡng điểm cố định. SQLite gốc chỉ là bằng chứng của repo SQLite, không được gắn nhãn MySQL.

## Chinook: fixture tốt cần câu hỏi và oracle riêng

Nguồn: [repository](https://github.com/lerocha/chinook-database), [script MySQL tại commit](https://github.com/lerocha/chinook-database/blob/7f67772503d71ba90f19283c38e93923addb43fa/ChinookDatabase/DataSources/Chinook_MySql.sql), [license](https://github.com/lerocha/chinook-database/blob/7f67772503d71ba90f19283c38e93923addb43fa/LICENSE.md). Grant MIT ghi Luis Rocha. Header script cũng dẫn license đó; README phân biệt metadata âm nhạc, danh tính giả và sales sinh ngẫu nhiên. Không có audio được dùng.

Script được đọc trước khi chạy và chỉ đổi tên database sang `pa_repo_chinook`; không chạy lệnh reset vào schema học cũ. Bản đã kiểm có 275 artists, 347 albums, 3.503 tracks, 59 customers, 412 invoices, 2.240 invoice lines và 8.715 playlist-track pairs. InvoiceLine không có invoice/track mồ côi trong phép kiểm. Tổng từng invoice khớp DECIMAL của line; tổng theo customer đi qua hai đường aggregate độc lập khớp; toàn bộ running total theo thứ tự `InvoiceDate,InvoiceId` khớp oracle Python Decimal.

Đề mới có thể yêu cầu giữ đúng grain khi nối nhiều bảng, so totals trước/sau, hoặc phân biệt window và GROUP BY. Không ghi các câu này là bài tập do tác giả Chinook cung cấp. Snapshot cố định cần thêm fixture nhỏ có NULL/ties/zero-child và biến thể mới khi đánh giá chuyển giao; trả đúng vài số thuộc dataset không chứng minh query tổng quát.

Trên web, server chuẩn bị snapshot và chỉ hiện schema/cột cần dùng. SELECT dùng role đọc; DDL/DML dùng bản cô lập. Không hiển thị các trường trông như thông tin liên hệ chỉ để trang trí câu hỏi. Script upstream có DROP DATABASE nên không gửi nguyên cho một tài khoản learner có quyền rộng.

## BusTub: giữ ngoài đường bắt buộc ở lần này

Nguồn: [BusTub](https://github.com/cmu-db/bustub/tree/e42a66f171093c138464b8302f5c3677a08e2ce4). MIT core license rõ; README yêu cầu không phát tán lời giải course, giới thiệu môi trường Ubuntu 24.04 và kỹ năng C++/systems. Source hiện có `UNIMPLEMENTED` ở buffer pool/B+ tree và nhiều test mang tiền tố `DISABLED_`. Clone không tạo một engine đã hoàn thành.

Chưa build hoặc chạy test BusTub trong lượt này, nên không lấy uy tín khóa CMU hoặc số sao để ghi PASS. 85 bài database không tự cung cấp toàn bộ kỹ năng C++ cần cho nhánh này. Nếu thêm sau, dev cần workspace compile cô lập, test riêng, quotas và đối chiếu dependency notices. Hiện chỉ giữ registry/notice tham khảo; không đưa implementation/solution công khai của sinh viên vào khóa.

## Tệp bằng chứng và giới hạn

`repo-checks/selected-repo-verification.json` có **21/21 kiểm đạt**, gồm một kiểm runtime, tám Hermitage, sáu Chinook và sáu e-commerce. `repo-checks/upstream-ecommerce-mutation.json` giữ kết quả mutation. Script `verify_repositories.py` dùng đúng ba schema `pa_repo_hermitage`, `pa_repo_chinook`, `pa_repo_index`; `mutate_upstream_ecommerce.py` không sửa clone upstream. Cả bốn clone đều có commit/hash ở registry. Notice được giữ trong `licenses/`.

Đây là kiểm kỹ thuật trên một môi trường và các ca được chọn. Chưa chạy learner runner trên web, chưa đo khả năng tiếp cận và chưa có pilot học tập. Chỉ phần đạt cổng tương ứng mới được chuyển sang activity spec; các phần chưa kiểm không được mang nhãn đã chạy chỉ vì ở chung repo.
