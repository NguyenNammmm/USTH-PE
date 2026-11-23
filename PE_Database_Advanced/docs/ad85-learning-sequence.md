# AD85 trên web: chia nội dung tham khảo thành các lượt làm

File AD85 chứa đầy đủ lời giảng để tự tra cứu. Giao diện học không nên dồn toàn bộ file dài vào một màn hình bắt đọc. Mỗi lượt dưới đây mở đúng một ví dụ, phần giải thích cần cho hành động kế tiếp và vùng luyện tương ứng. Người học luôn có thể mở bản đầy đủ. Phần thử độc lập dùng dữ liệu khác, giữ dấu đã xem gợi ý/đáp án.

| Lượt | Tình huống mở đầu | Luyện hỗ trợ phù hợp | Việc tự làm và bằng chứng cần nhận |
|---|---|---|---|
| Scalar và bảng kết quả | Nhóm DA có An,Chi; cần số lượng hay danh sách? | Ghép ba output với scalar/table function/result set procedure; giải thích vì sao relation rỗng khác một row NULL | Thiết kế giao diện cho một nhóm mới, ghi shape/NULL/empty; viết scalar MySQL thuần trên input mới |
| Ai commit? | Debit đã chạy nhưng credit tràn kiểu | Chọn statement còn pending trong timeline; sửa handler đang nuốt lỗi | Viết hợp đồng caller-owned và kiểm state sau lỗi, sau rollback; nộp query và engine artifact |
| Cursor có dùng giá trị cũ không? | Balance là0,7,13; FETCH cuối không trả dòng | Dự đoán prefix sum; kéo kiểm done về trước phép cộng rồi giải thích lỗi | Tự viết/sửa cursor cho fixture có hàng0 và bảng rỗng; phải giữ invariant prefix sum, không nhận một số tổng thuộc lòng |
| Chọn vòng lặp | n=0 nhưng REPEAT vẫn chạy một lần | Điền i/total sau từng lượt cho n0/n3; chọn nhánh ITERATE gây mất bước tăng | Viết vòng cho yêu cầu mới, nêu variant dừng và ca rỗng. Nếu SQL thì runner đúng dialect; pseudocode có nhãn model |
| NULL qua biên native | value0 có thể là số0 hoặc NULL | Ghép value/is_null/status với kết quả được phép dùng; sửa interface thiếu cờ | Viết contract input/output/error/ownership và chọn miền cô lập, bảo vệ lựa chọn; không giả lập load extension bằng output mẫu |
| Trigger chỉ khi qua ngưỡng | Stock12/min10 giảm tới10 rồi9 | So OLD/NEW và chọn lần tạo request; dự đoán multi-row statement có một row lỗi | Viết trigger/transaction cho fixture mới có equality và lỗi; kiểm số request, post-state và rollback scope |
| Credits phải trừ cả giá trị cũ | S1 có3 credits, sửa grade rồi chuyển enrollment | Ghép delta old/new với nhóm sinh viên; tìm write path bị bỏ sót | Dựng invariant và lời giải cho INSERT/DELETE/UPDATE/chuyển nhóm; ca cạnh tranh phải có khóa/protocol phù hợp |
| Restore có cộng hai lần không? | Snapshot chứa cả enrollment và totals đã tính | Chọn một counterexample cho replay trigger; vẽ cycle hai trigger | Viết trình tự restore/recompute/enable theo capability đã chọn và kế hoạch kiểm lại invariant; không chạy reset trên dữ liệu thật |
| Giới hạn40 giờ | Hai session cùng muốn thêm8 khi hiện có30 | Chỉ mở reminder về current read, khóa hàng cha và thứ tự khóa nếu cần | Tự thiết kế trước khi mở lời giải: sau lượt đầu38 thì lượt sau bị từ chối; nộp lịch/quan sát hoặc lập luận đúng loại bằng chứng |

Không luân phiên dạng bài bằng cách bốc thăm mù. Kỹ năng về shape dùng ghép output; kỹ năng vòng lặp dùng trace/debug; invariant liên hàng cần counterexample và code/lập luận. Trong cùng một kỹ năng có thể chọn biến thể hoặc dạng hỗ trợ tương đương, giữ mục tiêu và độ khó đã biên tập. Seed khóa fixture của attempt; sửa input/code làm kết quả trước hết hiệu lực.

MCQ hoặc kéo thả giúp làm quen một bước, không thay cho tự viết code hay lập luận. Checker phản hồi đúng phần vừa kiểm: đáp án model, hành vi engine hoặc lập luận được reviewer xem. Bài về type/caller/error phải kiểm cả success và failure; một trạng thái đúng sau COMMIT không chứng minh lỗi giữa hai update được xử lý đúng.

Dev dùng các record trong teaching-contract/web-runner-spec cho attempt, support history, version, capability và rubric. Chưa có backend thật thì màn hình chỉ mở lời giảng/model; không gắn nút Run trả một kết quả đã chuẩn bị thành lượt thực thi mới.
