# T14 - Thiết kế lặp và factory cho thành phần GUI

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import math
def score_valid(text):
    try: value=float(text)
    except ValueError: return False
    return math.isfinite(value) and 0<=value<=10
def make_validator(kind):
    if kind=="name": return lambda text: bool(text.strip())
    if kind=="score": return score_valid
    raise ValueError(kind)
```

## Đáp án kiểm tra hiểu

1. Có cần biến mọi hàm thành factory để code tốt hơn không?

Đáp án: Không, chỉ dùng khi cần chọn nhiều biến thể

- Có: Pattern có chi phí và không là mục tiêu tự thân.
- Không, chỉ dùng khi cần chọn nhiều biến thể: Đúng: lý do sử dụng phải xuất phát từ yêu cầu.
- Factory thay thế test: Vẫn cần kiểm tra hành vi.

