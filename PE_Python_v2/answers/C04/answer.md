# C04 - Tên biến, kiểu động và ghi chú có ích

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import keyword
def valid_name(name):
    """Kiểm tra tên Python hợp lệ và không thuộc từ khóa."""
    return name.isidentifier() and not keyword.iskeyword(name)
def type_trace():
    value = "8"
    before = type(value).__name__
    value = int(value)
    return before, type(value).__name__
```

## Đáp án kiểm tra hiểu

1. Tên nào hợp lệ và dễ hiểu cho điểm trung bình?

Đáp án: mean_score

- 2score: Tên không bắt đầu bằng chữ số.
- class: class là từ khóa.
- mean_score: Đúng: snake_case diễn đạt ý nghĩa.

