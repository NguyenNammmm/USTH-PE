# P16 - Kế thừa và ghi đè hành vi

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
class Course:
    def passed(self, score):
        return score >= 5

class HonorsCourse(Course):
    def passed(self, score):
        return score >= 8```

## Đáp án kiểm tra hiểu

1. HonorsCourse().passed(7) là gì?

Đáp án: False

- False: Đúng: phương thức lớp con được dùng.
- 7: Phương thức trả bool, không trả điểm.
- True: Lớp con đã đổi ngưỡng thành8.

2. Để thay hành vi, lớp con cần gì?

Đáp án: Phương thức cùng tên phù hợp giao diện

- Sao chép toàn bộ app: Sao chép app không phải mục tiêu kế thừa.
- Phương thức cùng tên phù hợp giao diện: Đúng: override giữ nơi gọi ổn định.
- Đổi mọi nơi gọi: Không cần nếu giao diện vẫn phù hợp.

