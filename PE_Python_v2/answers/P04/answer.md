# P04 - Điều kiện và giá trị ở ranh giới

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
if fee >= 100:
    result = "Free"
else:
    result = "Paid"```

## Đáp án kiểm tra hiểu

1. score=5 cho nhãn gì?

Đáp án: Dat

- Dat: Đúng: >= có bao gồm dấu bằng.
- Chua dat: Bạn đã bỏ qua trường hợp bằng ngưỡng.
- Cả hai: if/else chọn một nhánh ở lần chạy này.

2. Muốn chỉ số lớn hơn 5, dùng gì?

Đáp án: > 5

- >= 5: >= còn nhận cả số 5.
- > 5: Đúng: > loại giá trị bằng 5.
- = 5: = dùng cho phép gán, không phải so sánh này.

