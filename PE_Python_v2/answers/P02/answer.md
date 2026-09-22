# P02 - Chuỗi nhập vào và phép tính số

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = int(quantity_text) * price```

## Đáp án kiểm tra hiểu

1. "3" * 2 cho giá trị nào?

Đáp án: "33"

- "5": Phép nhân không cộng nội dung chuỗi.
- 6: Đây là kết quả nhân hai số, nhưng đầu vào là chuỗi.
- "33": Đúng: nhân chuỗi lặp lại chuỗi.

2. int("3") + 2 bằng bao nhiêu?

Đáp án: 5

- 5: Đúng: sau chuyển kiểu là phép cộng số.
- "32": Nối chuỗi không xảy ra sau int.
- Lỗi: Chuỗi "3" là đầu vào hợp lệ của int.

