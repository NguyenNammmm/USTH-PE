# Checklist bàn giao bài Machine Learning PE

Áp dụng checklist này cho từng bài `ML01`–`ML28`. Ghi `PASS`, `FAIL` hoặc
`CHƯA KIỂM THỬ` kèm bằng chứng. Không suy ra PASS từ việc JSON parse thành công.

## 1. S1 — Ngữ cảnh, dự đoán và giải thích

- [ ] Ngữ cảnh nêu một vấn đề dữ liệu hoặc kỹ thuật cụ thể.
- [ ] Kiến thức học trước, nguồn và quy ước shape/đơn vị được ghi rõ.
- [ ] Câu dự đoán có ít nhất hai lựa chọn và đúng một đáp án.
- [ ] Code minh họa, output và phần giải thích khớp nhau.
- [ ] Ngộ nhận được giải thích bằng nguyên nhân, không chỉ báo sai.

Kết quả:pass

## 2. S2 — Trắc nghiệm, đáp án và phản hồi

- [ ] Mỗi MCQ có câu hỏi rõ, ít nhất hai lựa chọn và đúng một đáp án.
- [ ] Mỗi phương án có phản hồi riêng; phương án nhiễu phản ánh lỗi ML hợp lý.
- [ ] `correct` dạng chỉ số và `option.correct` không mâu thuẫn nếu cùng tồn tại.
- [ ] `explanation` tổng kết đúng nguyên tắc, công thức hoặc quyết định kỹ thuật.

Kết quả:

## 3. S3 — Ghép code và tính đúng đắn

- [ ] Template chứa đầy đủ `{{slotN}}` tương ứng với danh sách slot.
- [ ] Mỗi slot có một đáp án xác định; các slot liên kết tạo thành code hợp lệ.
- [ ] Bank có đủ đáp án và thẻ nhiễu; `trap` giải thích đúng lỗi của thẻ.
- [ ] Code sau khi ghép đúng tương thích với nhiệm vụ và sandbox S4.
- [ ] Bài gate/boss không vô tình cấp scaffold hoặc lời giải sớm.

Kết quả: 

## 4. S4 — Sandbox, lời giải và tests

- [ ] Task nêu input, output, shape, dtype, làm tròn và edge case cần xử lý.
- [ ] `starterCode` không chứa sẵn lời giải và chạy được trong môi trường đích.
- [ ] `solutionCode` qua toàn bộ test; starter và biến thể sai không qua hết test.
- [ ] Có ba tầng hint tăng dần và không chép nguyên lời giải.
- [ ] Test ưu tiên `call`/`expect`, có tên rõ và bao phủ trường hợp biên.
- [ ] Chỉ dùng Python chuẩn, NumPy hoặc pandas; không dùng scikit-learn,
  TensorFlow hay PyTorch.

Kết quả: 

## 5. Tải lại — Kiểm tra khả năng khôi phục khi tích hợp

- [ ] Mở bài, nhập đáp án/code và tạo trạng thái đang học.
- [ ] Tải lại trang hoặc mở lại phiên học.
- [ ] Màn hiện tại, code, đáp án và trạng thái game được khôi phục đúng.
- [ ] Không mất hoặc nhân đôi tiến độ sau khi tải lại.

Kết quả: 

> Chỉ đánh dấu `PASS` sau khi kiểm thử ứng dụng thật. JSON hợp lệ, unit test hoặc
> việc đọc code không đủ để kết luận mục này PASS.

## 6. Tiến độ — Kiểm tra lưu hoàn thành và XP khi tích hợp

- [ ] Hoàn thành các màn bắt buộc và nộp sandbox thành công.
- [ ] Trạng thái hoàn thành được lưu đúng cho course `ml` và đúng lesson code.
- [ ] XP chỉ được cộng theo quy tắc ứng dụng, không cộng lặp khi tải lại/làm lại.
- [x] Gate và điều kiện tiên quyết mở khóa đúng sau khi hoàn thành.

Kết quả: 

> Chỉ đánh dấu `PASS` sau khi quan sát dữ liệu tiến độ và XP trong ứng dụng thật.
> Không đánh dấu PASS dựa trên `xp_reward`, `gate` hoặc bất kỳ trường JSON nào.
