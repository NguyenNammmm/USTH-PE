# Cấu trúc nguồn và ánh xạ

Tham chiếu: `Giao_Trinh_PE/PE_Python_DA/source/course.json`,
`source/practice.json`; đối chiếu bộ dựng Python DA hiện có trong bản ứng dụng
local. Không sửa repository tham chiếu và không tự đặt schema website mới.

## course.json

`groups`: `id`, `title`, `ids`. `lessons`: `id`, `title`, `level`, `before`,
`topics`, `reading`, `drills`, `reviewExercises`, `strand`, `provenance`.
`reading` sử dụng các type có thật `paragraph` và `code`.
Lý thuyết, ngữ cảnh, giải thích, ngộ nhận và dự đoán S1 chuyển thành bài đọc;
code S1 giữ mã nguồn và expected. Tự luận S2 chuyển sang `drills`;
lời giải code/đầu ra được giữ trong phần answer, chưa biến thành runner tự luận.
Mức và tiên quyết lấy MAP_ML.md; module không đổi.

## practice.json

`schemaVersion: 1`, `sourceCourseSha256`, `lessons`.
MCQ có `id`, `type: mcq`, `title`, `prompt`, `options`, `correctOption`,
`explanation`, `hints`; option có `id`, `text`, `feedback`.
Chỉ số đáp án cũ chuyển sang ID option; không đổi đáp án.
Code có `id`, `type: code`, `title`, `prompt`, `starter`, `referenceSolution`,
`tests`, `hints`. Các test `call/expect` được bảo toàn; nhánh xử lý biểu thức
có thật trong bộ dựng Python DA. Không ép sang `input/expected` gây mất nghĩa.

## Chưa ánh xạ tương đương hoàn toàn

- S3 scaffold, play/games và packages/runtime nằm nguyên trong bundle reference.
  Không gán cho chúng một type mới trong practice.json. Cần kiểm tra pipeline
  chính thức có giữ tương tác tương ứng trước khi nhập bộ nguồn mới.
- Phản hồi dự đoán S1 còn trong bài đọc và bundle gốc; không tuyên bố dự đoán
  tương tác được dựng tự động từ các paragraph.
- NumPy/pandas vẫn cần kiểm chứng bằng runtime/pipeline đích. Không giả định
  chỉ sao chép source là builder có thể chạy đầy đủ.
- Không thêm các trường trạng thái nghiệm thu của Python DA để tạo cảm giác
  đã được tác giả hoặc hệ thống của sếp duyệt.

Bundle reference là bản đầy đủ để đối chiếu và khôi phục mọi trường; gói source
là bản chuẩn hóa cách tổ chức biên soạn, chưa phải chứng nhận build tương đương.
