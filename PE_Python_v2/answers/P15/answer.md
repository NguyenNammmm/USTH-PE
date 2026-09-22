# P15 - Class và trạng thái riêng từng đối tượng

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def average(self):
        if not self.scores:
            return None
        return sum(self.scores) / len(self.scores)```

## Đáp án kiểm tra hiểu

1. Tạo a,b rồi a.add_score(8): điểm của b là gì?

Đáp án: []

- Không thể có hai instance: Một lớp có thể tạo nhiều đối tượng.
- []: Đúng: mỗi lần __init__ tạo list riêng.
- [8]: Chỉ đúng nếu bạn dùng chung list ngoài ý muốn.

2. self trong add_score là gì?

Đáp án: Đối tượng nhận lời gọi

- Điểm đang thêm: Điểm là tham số score riêng.
- Tên lớp cố định: Tên class và instance khác nhau.
- Đối tượng nhận lời gọi: Đúng: a.add_score dùng a làm self.

