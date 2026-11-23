# Cách học phần Advanced sau 85 bài Database PE

Phần này dành cho người đã học bộ 85 bài, nối kiến thức SQL, thiết kế và hệ thống với các bước suy luận/thuật toán sâu hơn. Có85 bài Advanced mới trong11 nhóm; số85 trùng bộ nền nhưng đây là các mãAD riêng. Các bài con được tách để XML, data mining, indexes, distributed protocols và PostgreSQL internals có đủ chỗ giải thích, không bị gộp thành vài bullet của một chương dài.

## Chọn điểm vào theo kỹ năng

Mỗi bài ghi oldPrereqs và newPrereqs. Nếu người học mắc một ý như NULL, lossless decomposition hoặc graph, mở đúng bài nền/đoạn nhắc rồi quay lại nhiệm vụ. Không buộc học lại cả 85 bài hoặc đi theo thứ tự mãAD. Manifest có một topological order để dev đối chiếu; nó là thứ tự hợp lệ về tiên quyết, không phải lịch học duy nhất.

Các chương giúp tìm nội dung: lập luận query; thiết kế và proof; ứng dụng/kiểu dữ liệu; analytics/dataflow; storage/indexes; query execution/optimization; transaction/recovery; distributed systems; vận hành; PostgreSQL internals; project. Một hoạt động có thể kết hợp nhiều chương nhưng phải nêu prerequisite đúng trước khi lấy bằng chứng độc lập.

## Lượt học và tài liệu tra cứu

Mở bằng dữ liệu hoặc một lỗi thật sự cần khái niệm. Ví dụ hai khoản thanh toán bị nhân khi join; hai giao dịch làm mất invariant; một pageLSN quyết định bỏ redo. Lời giảng giải thích các trạng thái vừa xuất hiện, rồi đi tới quy tắc tổng quát và điều kiện áp dụng. Khi nguồn có thuật toán/chứng minh, người học phải thấy input, pseudocode, invariant, dừng, tính đúng và một ca phản ví dụ cho việc bỏ điều kiện.

PDF và Markdown giữ lời giảng, mọi ví dụ, bài tập, hints và đáp án để tự học/tra cứu. Website chỉ đưa lượng thông tin giúp thực hiện tác vụ hiện tại, vẫn mở được phần đầy đủ. Không biến toàn bộ tài liệu thành số màn bắt buộc đọc và không tính xem hết đáp án là học xong kỹ năng.

Ba mức hỗ trợ là: ví dụ có giải thích; hoàn thiện/sửa/trace một phần; tự làm trên tình huống mới. Có thể bỏ phần hỗ trợ nếu đã có bằng chứng ở kỹ năng tương đương. Mở hint hoặc solution vẫn có giá trị học nhưng phải lưu dấu; lượt độc lập sau dùng fixture hoặc yêu cầu khác, không lấy kết quả đã nhìn đáp án làm mastery.

## Luân phiên bài theo kỹ năng

Chọn format theo điều cần quan sát: FD dùng trace, proof và countermodel; optimizer dùng tính chi phí và phản bác assumptions; transaction dùng lịch sự kiện/invariant và query; dữ liệu mở rộng dùng mapping/query/schema; project dùng sản phẩm và bảo vệ quyết định. Không ép mọi bài thành MCQ→drag→fill hoặc đổi game chỉ vì ID chẵn/lẻ.

Seed chỉ thay biến thể trong tập tương đương đã biên soạn, với tiên quyết, dialect, schema và oracle hợp lệ. Reload giữ đề và support history; đổi seed tạo lượt khác. Những ca chuyển giao dùng NULL, duplicates, zero-child, ties, skew, stale versions hoặc failure theo mục tiêu. Một câu giống nhau chỉ đổi tên/số chưa đủ chứng minh chuyển giao.

## Bằng chứng theo mục tiêu

SQL dùng engine đúng hệ ở backend và checker theo result/schema/post-state, có ca đúng và sai điển hình. Model hữu hạn tính lại thuật toán và giữ assumptions; proof/rubric đánh giá lập luận tổng quát, không bị thay bằng vài model test. Thí nghiệm performance có dữ liệu/config/plan/time thật, không bịa benchmark từ công thức. Recovery/consensus có thể học bằng model trên web; crash/replication engine thật cần capability tách biệt.

Tất cả thao tác bắt buộc của người học ở web. Dev có thể dùng container/VM/compiler/DBMS ở backend; người học không clone repo, cài Docker hoặc mở terminal máy riêng để hoàn thành chặng. Các tài liệu nền85 bài được giữ như snapshot tham khảo; những hướng dẫn native cũ là lịch sử đầu vào, không đưa nguyên thành yêu cầu vận hành của chặng web mới. Khi cần ôn một bài cũ trong sản phẩm, dev giữ ý kiến thức và chuyển thao tác thực hành sang capability web tương ứng.

## Repo và project

Ba nguồn được nhận theo phần đã kiểm: Hermitage cho lịch isolation, Chinook cho fixture và thí nghiệm index từ repo e-commerce sau khi sửa oracle. Không coi cả repo đạt hoặc gọi dữ liệu là một ngân hàng đề hoàn chỉnh. Source/commit/license/notice và thay đổi được gắn activity; phần CC BY phải giữ quyền tương ứng khi đưa vào khóa thu phí.

AD59 vàAD60 là project tích hợp: University vàCompany/Northwind. Người học cần nêu assumptions, thiết kế/test constraints, query/report đúng grain, lý do plan và ca concurrency/failure theo brief. Các topic hệ thống còn có nhiệm vụ triển khai mô hình, không bắt xây trọn DBMS C++ khi đầu vào chưa có systems programming.

Rubric đề xuất ghi riêng: đúng hành vi và invariant; lập luận/assumptions; ca kiểm và tái lập; giải thích tradeoff/giới hạn. Trọng số/điểm đỗ do nhóm pilot xác lập, không nhận một con số là mastery tối ưu chỉ từ thiết kế. Bài nhóm cần có nhiệm vụ cá nhân với input mới; sản phẩm nhóm không tự chứng minh từng thành viên làm được.

## Thứ tự triển khai cho dev

P0 là renderer/brief/schema đúng, runner cô lập theo capability, checker đúng NULL/bag/order/Decimal, attempt/version/seed/support history và feedback có counterexample. P1 là các model FD/optimizer/transaction/recovery, project và author preview. P2 là adaptive sequencing hoặc dashboard sau khi có dữ liệu pilot đủ; không đặt chatbot làm điều kiện để sửa lỗi runner/cách chấm.

Handoff có nội dung và mô hình tương tác đại diện, không có dịch vụ SQL production. Acceptance của sản phẩm phải thử các error path, cancellation/reset/session lifetime và accessibility thật. Kiểm code và tài liệu không thay kết quả pilot học tập.
