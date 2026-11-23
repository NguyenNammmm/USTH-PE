# Rà soát practice model trên HTML spec

Phạm vi thay đổi: chỉ block practice bắt đầu `const options=` đến trước `$('#repo-cards')` trong `build/spec-ui.js`. Ngày: 05/11/2026. Không thay runner SQL, catalog, các model khác hoặc các file lesson.

## Ba hình thức trả lời

| Seed modulo 3 | Hoạt động | Input của người học | Cách đối chiếu |
|---|---|---|---|
| 0 | Dự đoán query thiếu category | Dãy ID tự nhập, comma/space | Tính predicate price/rating trên bốn hàng; so đúng giá trị, số lượng, thứ tự |
| 1 | Điền blank `expected` | Literal JSON array trong textarea | Exact oracle nhận model output đúng và bác mutant `[]`; không eval code người học |
| 2 | Phản ví dụ thiếu rating | Checkbox chọn subset hàng và textarea giải thích | Tính hai kết quả trên subset; kiểm khác nhau và cardinality một hàng; giải thích chờ rubric |

Fixture gồm một hàng đạt cả ba điều kiện đúng tại biên price/rating, một hàng sai category, một hàng rating thấp và một hàng price cao. Schema, đơn vị price và giả định không NULL được hiện trên UI. ID, category và thresholds phụ thuộc seed; expected/result/witness đều suy từ fixture/predicate, không dùng vị trí lựa chọn hard-code làm đáp án.

Các sample tính được: seed 18, dạng dự đoán, query thiếu category trả `[181,182]`; seed 16, dạng code blank, expected `[161]` nên exact oracle bác `[]`; seed 17, dạng phản ví dụ, chỉ hàng 173 cho hợp đồng `[]` và mutant `[173]`. Tập rỗng cho hai kết quả rỗng, nên không là witness. Những sample này là suy luận mô hình, không ghi là output engine.

## State và hỗ trợ

- Giữ seed và cờ hint/answer của từng seed trong localStorage; validate dữ liệu khôi phục, không nạp HTML/code từ storage.
- Nếu localStorage bị chặn hoặc đầy, practice vẫn hoạt động trong bộ nhớ và hiện thông tin chưa lưu; nội dung JSON hỏng không làm trang crash. Một lần lưu thành công có thể phục hồi trạng thái khả dụng.
- Mở gợi ý hoặc đáp án ghi cờ hỗ trợ trước khi trả feedback. Reload/đổi seed rồi quay lại không xóa lịch sử hỗ trợ.
- Input/change của đáp án hoặc seed xóa `lastResult`; đổi seed cần tạo lại trước khi check/hint/answer. Answer reveal/hint cũng xóa kết quả đối chiếu trước.
- State dùng `lastResult.modelCheckPassed`, không tạo trạng thái đạt độc lập hoặc đạt engine. Với bài giải thích, `explanationReview='pending'`; việc có nội dung không tự chứng minh lập luận đúng.

## Loại bằng chứng và kiểm đã chạy

Mọi prompt/feedback có nhãn mô hình SQL trong browser, chưa chạy engine và không ghi nhận đạt độc lập. Phần explanation không dùng keyword matching để giả chấm ngữ nghĩa. Đáp án của ca phản ví dụ hiện rubric category/price, rating và kết quả khác nhau.

Đã chạy `node --check output/database-advanced/build/spec-ui.js`: exit 0, không có lỗi cú pháp. Chưa thực hiện browser acceptance hoặc engine SQL; root sẽ kiểm DOM, biến thể và localStorage trên artifact HTML đã build. Giới hạn: demo chỉ mô hình selection trên fixture bốn hàng không NULL; không phải SQL parser hoặc general-purpose runner.
