# P20 - Test trường hợp thường và trường hợp biên

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def make_cases():
    return [(4, False), (5, True), (8, True)]```

## Đáp án kiểm tra hiểu

1. Test nào bắt lỗi viết >5?

Đáp án: 5

- 8: 8 True ở cả hai.
- 4: 4 vẫn False với cả hai cách.
- 5: Đúng: hai cách khác nhau tại5.

2. Một hàm qua ba test có chắc không còn lỗi?

Đáp án: Không; test chỉ kiểm tra trường hợp đã bao phủ

- Không; test chỉ kiểm tra trường hợp đã bao phủ: Đúng: test là bằng chứng có phạm vi.
- Không cần test nữa: Cần chọn thêm test khi có rủi ro chưa bao phủ.
- Có: Vẫn có thể có đầu vào khác hoặc vi phạm hợp đồng.

