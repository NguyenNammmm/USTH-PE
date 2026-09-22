# P11 - Module và trung bình có trọng số

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from grading import weighted_mean

def report(marks, credits):
    return weighted_mean(marks, credits)```

## Đáp án kiểm tra hiểu

1. Kết quả mẫu là gì?

Đáp án: 7.5

- 14: 14 là tổng điểm, chưa chia.
- 7: 7 là trung bình không trọng số.
- 7.5: Đúng: môn8 có trọng số3.

2. Cách import nào đúng ở đây?

Đáp án: from grading import weighted_mean

- from grading import weighted_mean: Đúng: gọi hàm đã được module cung cấp.
- import "grading.py": import không nhận chuỗi tên file như vậy.
- from grading.py import weighted_mean: Tên module không có đuôi .py trong cú pháp này.

