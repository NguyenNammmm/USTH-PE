# Lab đã chọn từ repo và cách biên tập lên web

Các lab dưới đây là phần được chọn sau kiểm định trong research/repo-quality.md. Chúng nối với bài Advanced, không phải một khóa khác buộc học viên clone repo. Backend dựng snapshot/connection; người học dự đoán, sửa hoặc viết query ngay trên web. Nguồn, commit, license và thay đổi phải mở được ở màn nguồn của từng lab.

## REPO-H01 — Một read có thấy write bị abort không?

Bài liên quan: AD42. Nguồn lịch: Hermitage mysql.md, các ca G1a, được biên tập và chạy lại trên MySQL8.4.13. Giữ attribution Martin Kleppmann, CC BY4.0 và notice thay đổi theo registry.

Fixture hai row `test(id,value)` là(1,10),(2,20). A bắt đầu và UPDATE row1 thành101 nhưng chưa commit. B bắt đầu ở READ UNCOMMITTED hoặc READ COMMITTED rồi SELECT row1. Người học dự đoán giá trị, chạy đúng các bước do backend xác nhận, sau đó A rollback và B đọc lại. Trong ca đã kiểm, RU thấy101 rồi10, RC thấy10 rồi10.

Luyện hỗ trợ là ghép giá trị với visibility rule; bài tự làm đổi isolation/row và nêu vì sao một result không đủ chứng minh mọi anomaly. Oracle kiểm giá trị trong khi A chưa kết thúc và sau rollback, cùng trạng thái transaction. Không chấm từ một ảnh101 nếu thiếu evidence rằng A chưa commit. Registry capability là `mysql84.two-session.innodb`; lỗi dựng sandbox không tính người học sai.

## REPO-H02 — Snapshot và predicate read

Bài liên quan: AD42, AD65. Fixture ban đầu không có row value30. A mở transaction và SELECT predicate value30. B insert row mới value30 rồi commit. A lặp lại SELECT. Trong các ca plain consistent read đã kiểm, READ COMMITTED thấy sốrow0→1, REPEATABLE READ thấy0→0. Không suy kết quả này cho locking read hoặc mọi phantom definition.

Tình huống mới cho A chuyển từ plain read sang locking read và yêu cầu nêu loại bằng chứng cần kiểm; không tự cho kết quả mẫu của bài cũ là engine đã chạy câu mới. Mọi lần đổi isolation/reset phải đóng transaction trước đó và dựng lại fixture. SQL mới phải được thực thi trên backend thật trước khi gọi là engine-execution.

## REPO-H03 — Mất cập nhật và bản sửa có giới hạn

Bài liên quan: AD40–AD42. A,B cùng đọc10. A ghi giá trị client đã tính11, B cũng gửi UPDATE value=11. Backend xác nhận B đang chờ lock A bằng observer trước khi cho A commit. Sau B tiếp tục, kết quả11. Đổi hai statement thành `value=value+1` cho12 trong ca đã kiểm.

Nhiệm vụ tự làm dùng giá trị đầu20 với các delta khác và yêu cầu giữ đủ tổng. Một câu hỏi mở tiếp theo yêu cầu dựng invariant hai row mà atomic increment một item chưa đủ bảo vệ. Chấm post-state, schedule preconditions và lý do; không chấp nhận kết luận bản sửa giải mọi lost update/write skew trên mọi engine. Lịch ban đầu phải được đánh dấu đã dùng hỗ trợ nếu người học mở đáp án.

## REPO-E01 — Test xanh có kiểm được query không?

Bài liên quan: AD01, AD30, AD35, AD53. Nguồn: ecommerce-query-optimizer-demo, MIT. Bản gốc dùng SQLite. Năm test gốc vẫn pass khi ba helper bị thay để luôn trả `[]`, nên checker upstream nguyên trạng không được đưa vào khóa.

Bản PE có fixture nhỏ gồm: một sản phẩm hợp lệ; một sản phẩm sai category nhưng đạt giá/rating; một sản phẩm đúng category/giá nhưng rating thấp; một sản phẩm nằm đúng biên giá; và các row ngoài khoảng. Brief quy định category, giá inclusive, rating tối thiểu, output cột và tie-breaker `price,id`. Oracle exact result bắt ba mutant đã thử: trả rỗng, bỏ category và bỏ rating.

Lượt web có thể luân phiên: dự đoán output của query sai, điền phần expected cần để bắt rỗng, hoặc chọn và giải thích một counterexample tối thiểu. Sau đó người học tự viết query trên fixture mới. Các bài hỗ trợ ấy không được tự nâng thành đạt độc lập. Bộ test mới cần chạy cả query đúng lẫn những mutant đã định danh, không chỉ có một test của lời giải chuẩn.

## REPO-E02 — Composite index phải giữ kết quả trước/sau

Bài liên quan: AD30, AD35–AD37, AD53. Phần được nhận biên tập query sang MySQL, dùng10.000 sản phẩm và oracle Python Decimal độc lập. Ca đã kiểm so exact ID/order, tạo index và so plan/result trước/sau; không nhập các số tăng tốc từ README gốc.

Người học đề xuất index, giải thích equality/range/order và thử trên backend sandbox tài nguyên đã khai báo. Bài làm nộp query, index DDL, output hash, plan artifact, fixture hash, cấu hình và nhận xét giới hạn. Không chấm một threshold milliseconds cố định hoặc yêu cầu index luôn được chọn trên mọi dataset. Fixture chuyển giao đổi skew/selectivity và thêm ties/NULL theo hợp đồng.

Một lượt plan phải phân biệt EXPLAIN estimate với EXPLAIN ANALYZE thực thi. Khi hủy, backend dừng đúng query rồi rollback/đóng connection/reset theo spec, không chỉ ẩn spinner. Khi chưa có backend, HTML chỉ cho đọc artifact đã ghi và tính model riêng.

## REPO-C01 — Chinook: đối soát grain thay vì nhớ một tổng

Bài liên quan: AD01, AD10, AD18, AD60. Nguồn fixture: Chinook MySQL script tại commit trong registry, MIT; không dùng audio. Bản đóng gói bỏ DROP/CREATE/USE database. Backend chỉ nạp table/data payload vào schema mới, rỗng đã được cấp cho attempt; từ chối schema tồn tại và dừng ngay khi có lỗi SQL. Quyền quản lý vòng đời sandbox nằm ở backend.

Fixture đã kiểm có412 invoice và2.240 invoice line. Nhiệm vụ mới của PE yêu cầu tổng line theo invoice khớp tiền hóa đơn, tổng theo customer đi qua hai cách aggregate độc lập và một counterexample cho join làm nhân tiền. Không gọi những câu này là ngân hàng đề do tác giả Chinook cung cấp.

Chấm exact DECIMAL theo brief, grain và trường hợp hóa đơn không line/khách không invoice trong fixture chuyển giao. Không lấy việc trả một tổng thuộc snapshot cố định làm bằng chứng query tổng quát. Student role chỉ hiện các trường cần cho bài; không hiển thị trường liên hệ để trang trí.

## REPO-C02 — Running total và thứ tự đồng hạng

Bài liên quan: AD10, AD53. Người học tính tổng tích lũy theo customer và `InvoiceDate,InvoiceId`, phân biệt GROUP BY với window và ROWS với RANGE khi có peers. Bộ kiểm đã đối chiếu412 running totals với Python Decimal trên snapshot đã chọn.

Bài chuyển giao thêm hai invoice cùng ngày, đổi ID và thứ tự insert. Output order chỉ được chấm khi brief yêu cầu; frame/order bên trong window và order của output là hai điều kiện riêng. Một query đúng tình cờ vì snapshot không có ties phải bị fixture mới làm lộ. Không dùng float hoặc format thành chuỗi để che chênh tiền.

## Bộ activity record cho dev

Mỗi lab có `id`, `lessonIds`, `upstreamCommit`, `sourceFiles`, `licenseNotice`, `adaptationVersion`, `capabilityId`, `fixtureVersion`, `seedPolicy`, `prompt`, `supportActivities`, `independentTask`, `oracle`, `adversarialCases`, `expectedEvidence` và `limits`. Repo registry là đầu vào provenance; không phải một cờ passed cho mọi activity tương lai.

Expected result của mỗi fixture chạy trên engine đúng hệ, có đối chiếu độc lập cho ca nhỏ. Reference query và student query chạy trong state tách biệt. Attempt giữ version/seed/support history; sửa code làm kết quả cũ hết hiệu lực. Các acceptance cases cần có đúng, sai, rỗng, NULL, duplicate, ties và reset phù hợp kỹ năng; không nhất thiết mọi ca có mặt trong mọi bài.

## Phần chưa được đưa vào bài bắt buộc

BusTub được clone và đọc license/source, nhưng chưa build/test C++; skeleton có TODO/disabled tests và cần kỹ năng systems/C++ ngoài giả định đầu vào của khóa. Nó ở registry tham khảo, không mang nhãn lab đã đạt. Không lấy implementation/solution công khai của sinh viên để phân phối như nội dung PE.

## Quyền dùng và kiểm chứng

Đọc research/licenses/THIRD-PARTY-NOTICES.md cùng repo-registry.json. Giữ attribution, grant và notice theo đúng phần được dùng; không áp điều khoản/technical restriction mới cản quyền với phần CC BY được cấp. Bộ kiểm21 ca là phạm vi được chọn trên một môi trường; không chứng nhận toàn repo, mọi engine hoặc hiệu quả học tập.
