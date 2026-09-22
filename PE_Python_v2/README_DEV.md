# Bàn giao ProgrammingEdu Python v2

Ngày 22/09/2026. 92 bài: 59 lộ trình chính, 33 nâng cao; bổ sung 68 bài sau kiểm toán P01-P24 và E01-E06. Đây là nội dung để đội dev triển khai, không phải ứng dụng học tập đã triển khai.

## Tệp cần dùng

- PE_Python_v2_Bai_hoc_huong_dan_dev.pdf: bài học, mục lục và quy ước chung. Không chứa báo cáo phân tích nguồn.
- lesson_bank.json: nội dung S1-S4, nhiệm vụ, prerequisite, runtime, gợi ý, tương tác và source_rows; thứ tự theo order.
- instructor_answers.json và answers/: đáp án, khóa quiz/phản hồi, code tham chiếu và file hỗ trợ. Chỉ dùng phía giảng viên/dịch vụ chấm.
- test_criteria.json: ca tự động, protocol manual, rubric giải thích và môi trường.
- Thieu_truoc_bo_sung.md: toàn bộ 189 mục thiếu/một phần của baseline; ghi cả điểm P và P+E outline.
- Ma_tran_sau_bo_sung.md và coverage_after.json: truy vết đủ 237 mục tới bài, trang PDF và đánh giá.
- package_pw4/, capstone_pw9/: package tham chiếu chạy riêng. Chạy main.py từ thư mục tương ứng.
- QA_Ban_giao.md, QA_*_results.json, legacy/QA_reference_results.json: kết quả thật và gate chưa nghiệm thu.
- manifest.json: SHA-256 của các tệp phát hành; không chứa chính manifest để tránh đệ quy.

## Thứ tự học và cách dựng màn hình

Dùng order và prerequisites, không sort đơn giản P rồi C rồi T. Học core trước, mở advanced khi đạt điều kiện; một số bài nền tảng nâng cao là điều kiện của capstone. Mỗi lesson là một cụm học, không nhất thiết một phiên 5 phút. duration_minutes chỉ là ước tính thiết kế; chia phiên theo checkpoint và hiệu chỉnh sau pilot.

S1: tình huống + ví dụ + dự đoán. S2: quiz và phản hồi riêng cho từng lựa chọn. S3: thực hành có hỗ trợ rồi thay dữ liệu. S4: giải nhiệm vụ mới và giải thích. Chấp nhận lời giải khác đúng hợp đồng; chỉ bắt buộc API khi đề nêu đó là mục tiêu học. Lưu riêng attempt có gợi ý và tự làm.

Ghép quiz_keys theo vị trí câu hỏi, answer là chỉ số bắt đầu từ 0. Không tải trước instructor_answers, hidden tests hoặc đáp án challenge vào client. worked_example/public_tests là dữ liệu học công khai. Các support_files trong ngân hàng có thể chứa mã trợ giúp có chủ ý; cấp đúng bài.

Tự động PASS là điều kiện cần cho bài có check code. Hoàn thành bài còn cần manual_checks và self_explanation đạt 2/2. NOT_RUN, lỗi môi trường hoặc mở đáp án không được xem là hoàn thành. Người chấm xét cơ chế và phản ví dụ, không chỉ so nguyên văn lời giải.

## Dựng môi trường và chạy kiểm tra

Môi trường đã kiểm: Windows, Python 3.12.14, Tk desktop. Tạo venv riêng. Cài requirements-core.txt; nhóm dữ liệu dùng requirements-data.txt; nhóm wx/OpenGL/MySQL dùng requirements-native.txt theo khả năng máy lab. Cài đặt MySQL server/Workbench và POSIX/curses là bước riêng, không phải pip đã đủ.

Từ thư mục gói, với python của venv:

```text
python verify_new.py
python legacy/verify_reference.py
python verify_extra.py
python verify_graphics.py --pyglet
```

PE_QA_DEPS chỉ là tùy chọn đường dẫn thư viện bổ sung khi tái kiểm; venv bình thường không cần biến này. verify_reference dùng import từ interpreter/PYTHONPATH. Cần desktop session để tạo Tk. Trên Windows curses cần bản hỗ trợ phù hợp hoặc lab POSIX; chưa khóa phiên bản curses được kiểm vì chưa chạy terminal lab.

Các verifier dùng exec cho đáp án do người biên soạn kiểm soát. **Không dùng chúng để chạy mã học viên không tin cậy.** Đội dev cần runner cách ly, giới hạn thời gian/tài nguyên/quyền file/mạng và dữ liệu fixture riêng cho từng lần chấm. Pickle chỉ đọc artifact lab tin cậy; không dùng pickle làm định dạng nộp bài từ người học.

Mỗi answers/<id>/answer.md ghi đáp án; reference.py có khi đáp án là Python. Bài setup/IDE/Git/kiến trúc có đáp án quy trình và protocol chấm, không giả lập thành test tự động. Với A22 lưu reference.py thành dual_gui.py khi làm theo lệnh trong đề, hoặc dùng tên reference.py tương ứng. Với A08 tách hai snippet theo OS như đáp án chỉ rõ.

## Nguồn và giới hạn

SL: All_slide_one_file.pdf, 330 trang; HF: Head First Python Third Edition Early Release 2023-02-08, 271 trang thực nhận (phần mở đầu và chương 1-2); GUI: Python GUI Programming Cookbook 2e 2017, 596 trang. Không suy ra đã bao phủ phần còn lại của bản Head First xuất bản đầy đủ. PE_Thuyet_minh_phuong_phap_giao_duc.pdf là tham khảo thiết kế học, không là nguồn kiến thức Python để cộng vào mẫu số.

Số trang nguồn là số trang PDF, có thể khác số in trong sách; một số recipe cùng dẫn khoảng trang chương. Danh sách 237 mục là kiểm kê biên tập, không phải mọi câu hoặc API. Kiến thức trùng nhau giữa ba nguồn được dạy chung rồi truy vết nhiều hàng. Dữ liệu và tình huống mới được biên soạn; fixture SAS có giấy phép riêng trong fixtures/.

PE được dùng cho chuỗi dự đoán, phản hồi, sửa đổi, tự giải và giải thích. Không coi kéo-thả tự động là tương tác học tập sâu, không xem test PASS là bằng chứng hiệu quả sư phạm. Trước mở khóa đại trà cần pilot người học, ghi khó hiểu, lỗi và thời gian thực.

Các cập nhật kỹ thuật tham khảo tài liệu chính thức:
- https://docs.python.org/3.15/howto/free-threading-python.html
- https://wxpython.org/Phoenix/docs/html/wx.App.html
- https://wiki.wxpython.org/MainLoopAsThread
- https://docs.pyglet.org/en/latest/programming_guide/rendering.html

Những trang này giúp giải thích khác biệt với nguồn cũ; không có nghĩa runtime bàn giao đã kiểm trên Python 3.15.
