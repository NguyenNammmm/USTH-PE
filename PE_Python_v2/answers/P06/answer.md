# P06 - Dictionary và tra cứu theo khóa

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = marks.get(student_id, None)```

## Đáp án kiểm tra hiểu

1. score bằng gì?

Đáp án: None

- 0: Chưa có điểm không đồng nghĩa điểm 0.
- None: Đúng: trả mặc định vì khóa không tồn tại.
- 5: Không tự lấy giá trị cuối cùng.

2. marks có S01:0; get("S01",None) trả gì?

Đáp án: 0

- Lỗi: get đọc được khóa này.
- None: Khóa tồn tại nên không dùng mặc định.
- 0: Đúng: 0 là giá trị hợp lệ.

