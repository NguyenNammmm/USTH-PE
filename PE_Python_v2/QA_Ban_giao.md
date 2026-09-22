# Kiểm tra cuối bản bàn giao

Ngày 22/09/2026. Kết quả dưới đây là kiểm thử đáp án tham chiếu, không là kết quả học viên hoặc ứng dụng production.

- P01-P24: 74 ca seed, 5 ca bổ sung và 2 ca Tk đều PASS. Đã sửa P19 để biểu đồ rỗng không phát sinh tick số mặc định và chạy lại thành công.
- Bài mới: 51 bài có các check tự động PASS; 17 bài cần protocol thủ công. 24 bài P dùng runner gốc. Không có FAIL trong lượt chạy cuối.
- Bổ sung: SAS7BDAT thật đối chiếu CSV; TCP/HTTP loopback; luồng tích hợp PW9 Tk gồm validate/GPA/lưu nền/mở lại và unpickle từ process mới; contract repository MySQL bằng mock; biên dịch các file Python: PASS.
- Pyglet: native shader compile/link, uniform/attribute và draw trong cửa sổ ẩn PASS. Đây là smoke test, chưa thay thế kiểm tra cube, điều khiển và hoạt ảnh đầy đủ.
- MySQL mock PASS không chứng minh server MySQL, transaction hoặc GUI đã hoạt động với database thật.
- Các check PASS của Tk không thay việc xem resize, focus, timer, ngôn ngữ, accessibility và vòng đời trên máy đích.
- PDF cuối: 97 trang đã render; đã xem toàn bộ contact sheet và xem riêng trang dày/P24/A18/X02, không phát hiện tràn lề, mất chữ hoặc lỗi bố cục.

17 bài cần nghiệm thu quy trình: C01, C02, C03, C19, A03, A18, A19, A20, A21, A23, A24, A25, A08, A10, A13, A22, X06.

## Gate còn mở trước khi phát hành khóa học

| Gate | Bài | Bằng chứng cần thu |
|---|---|---|
| Setup, notebook, Git | C01-C03,X01-X02,X06 | Môi trường dựng lại, Restart/Run All, fork/push thực trên repo do giảng viên chỉ định |
| Package và IDE | C19,T10-T11 | Chạy package, import yên lặng, mutation test, ảnh runner/watch |
| Curses/POSIX | A03,A08,X02,X04 | Terminal thật, fork/exec, ls/bc/pipe/redirect, thu dọn process |
| MySQL | A18-A20 | Server/version, schema/FK, Workbench, commit/rollback và GUI với DB thật |
| wx và hai GUI | A21-A24 | Controls/bitmap, IPC hai chiều, cả hai vai host, đóng peer/host, GL compatibility |
| Hoạt ảnh native | A25-A26 | Cube màu, input, resize, dt, pause/resume trên GPU đích |
| File qua mạng | T05 | Share lab, hủy dialog, lỗi quyền, đối chiếu byte |
| Chất lượng học | Mọi bài | Manual rubric, giải thích 2/2, pilot và thời gian thực |

Thử wx smoke ở giai đoạn trước không tạo kết quả xác nhận; trạng thái wx vẫn NOT_VERIFIED. Không chuyển thành PASS từ việc import/compile hoặc từ test pyglet.

## Kiểm tra lại phạm vi

Đã rà danh sách thiếu, đối chiếu hợp đồng và tiêu chí mới, rồi chạy lại verifier trên tệp phát hành. 237/237 mục có bài và đánh giá được thiết kế; adaptation cụ thể trong ma trận. Không dùng độ phủ nội dung thay độ sẵn sàng triển khai. Các ca manual có protocol/đáp án để dev nghiệm thu tiếp.
