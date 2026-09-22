# P13 - Ngoại lệ và dữ liệu nhập không hợp lệ

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def parse_score(text):
    try:
        score = float(text)
    except ValueError:
        return None
    if 0 <= score <= 10:
        return score
    return None```

## Đáp án kiểm tra hiểu

1. parse_score("abc") trả gì?

Đáp án: None

- None: Đúng: ValueError được xử lý.
- Chương trình luôn dừng: except xử lý lỗi chuyển số này.
- 0: Sai nhập không có nghĩa điểm0.

2. parse_score("11") đi qua nhánh nào?

Đáp án: Chuyển số thành công rồi bị loại ngoài khoảng

- except ValueError: 11 chuyển sang float được.
- Chuyển số thành công rồi bị loại ngoài khoảng: Đúng: lỗi quy tắc khác lỗi chuyển kiểu.
- Trả11: Đề chỉ nhận từ0 đến10.

