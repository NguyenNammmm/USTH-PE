# C19 - Module, alias và package lồng nhau

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
domains/grades.py: def passed(score): return score >= 5
domains/reports/__init__.py: để trống
domains/reports/summary.py:
    from ..grades import passed
    def count_passed(scores): return sum(passed(s) for s in scores)
domains/__init__.py:
    from .reports.summary import count_passed
main.py:
    import domains as dm
    if __name__ == "__main__": print(dm.count_passed([4,5,8]))
```

## Đáp án kiểm tra hiểu

1. domains/__init__.py tự tạo Student object mỗi khi gọi hàm không?

Đáp án: Không

- Có: Đừng nhầm file package với constructor class.
- Không: Đúng: nội dung file chạy khi module được nạp, không phải mỗi lời gọi hàm.
- Chỉ khi có alias: Alias không làm đổi cơ chế đó.

