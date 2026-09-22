# P10 - Hàm trả về giá trị

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def mean_score(scores):
    if not scores:
        return None
    return sum(scores) / len(scores)```

## Đáp án kiểm tra hiểu

1. answer là gì?

Đáp án: 7.0

- 7.0: Đúng: hàm trả số trung bình.
- None: Hàm chỉ trả None với list rỗng.
- Chuỗi "7.0": Không có bước chuyển sang chuỗi.

2. Thay return bằng print ở cuối thì nơi gọi nhận gì?

Đáp án: None

- Số vừa in: In ra không chuyển số thành return.
- None: Đúng: hàm kết thúc không return giá trị sẽ trả None.
- List ban đầu: Tham số không tự được trả về.

