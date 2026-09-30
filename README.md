# USTH-PE: ProgrammingEdu Python

Bản bàn giao nội dung v2 cho đội phát triển: **92 bài học** gồm 59 bài lộ trình chính và 33 bài nâng cao; bổ sung 68 bài sau kiểm toán bản đầu.

## Roadmap v3 theo phản hồi về độ khó

Bản v3 thiết kế đường học hướng tới năm dạng bài trong `final-2026.docx`: **40 nhiệm vụ viết code bắt buộc**, gồm 20 cơ bản (50%), 12 trung cấp (30%) và 8 nâng cao (20%). Mỗi nhiệm vụ có yêu cầu và tiêu chí chấm; các ví dụ được tách nhỏ và giải thích theo bước.

- [Xem roadmap tương tác](curriculum_v3/roadmap_visualization.html)
- [Đọc roadmap và quy cách bài học](curriculum_v3/ROADMAP_VA_FORMAT_V3.md)
- [JSON 40 nhiệm vụ](curriculum_v3/roadmap_50_30_20.json) và [schema bài học](curriculum_v3/lesson_format_v3.json)
- [Mẫu bài cơ bản, trung cấp, nâng cao và A04](curriculum_v3/examples/README.md)
- [Tải gói v3](downloads/PE_Python_v3_Roadmap_50_30_20.zip)

V3 là **roadmap, hợp đồng bài tập và mẫu định dạng**, chưa phải ngân hàng bài hoàn chỉnh thay thế v2. Chuẩn điểm qua môn và phạm vi đề thi chính thức cần đối chiếu với giảng viên; báo cáo kiểm tra nằm trong [QA roadmap](curriculum_v3/QA_roadmap.json).

## Bắt đầu

- [Hướng dẫn đội dev](PE_Python_v2/README_DEV.md)
- [PDF bài học, 97 trang](PE_Python_v2/PE_Python_v2_Bai_hoc_huong_dan_dev.pdf)
- [Tải trọn gói ZIP](downloads/PE_Python_v2_Goi_ban_giao_dev.zip)
- [Ngân hàng bài tập JSON](PE_Python_v2/lesson_bank.json)
- [Đáp án](PE_Python_v2/instructor_answers.json) và [tiêu chí kiểm thử](PE_Python_v2/test_criteria.json)
- [Danh sách thiếu trước bổ sung](PE_Python_v2/Thieu_truoc_bo_sung.md)
- [Ma trận kiểm tra sau bổ sung](PE_Python_v2/Ma_tran_sau_bo_sung.md)
- [Kết quả kiểm tra và phần cần nghiệm thu tiếp](PE_Python_v2/QA_Ban_giao.md)

## Phạm vi

237/237 mục đã kiểm kê từ slide và hai file sách có bài học và tiêu chí đánh giá được thiết kế. Tỷ lệ này không có nghĩa bao phủ mọi chi tiết của sách, học viên đã thành thạo hay mọi runtime đã được nghiệm thu. Các phần cần MySQL thật, POSIX/curses, wx và kiểm tra thủ công được ghi trong báo cáo QA.

Gói bao gồm mã tham chiếu, fixture, verifier và checksum; không bao gồm bản sách nguồn. Đây là nội dung bàn giao để xây dựng sản phẩm học tập, chưa phải ứng dụng production. Đáp án và kiểm thử nội bộ dành cho đội dev/giảng viên; không tải trước vào client học viên.
