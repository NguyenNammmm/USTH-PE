# C20 - So sánh đối tượng, biểu diễn và đóng gói

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import math
class Grade:
    def __init__(self,value):
        self.value=value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,value):
        if type(value) not in (int,float) or not math.isfinite(value) or not 0<=value<=10:
            raise ValueError("score")
        self._value=value
    def __str__(self):
        return f"Grade({self.value})"
    def __lt__(self,other):
        if not isinstance(other,Grade):
            return NotImplemented
        return self.value<other.value
```

## Đáp án kiểm tra hiểu

1. isinstance(x,Grade) và issubclass(Child,Grade) nhận cùng loại đối số không?

Đáp án: Không: object so với class

- Có: Đối số đầu có vai trò khác nhau.
- Không: object so với class: Đúng: một cái xét instance, một cái xét quan hệ lớp.
- Cả hai chỉ nhận chuỗi: Chúng không nhận tên class dưới dạng chuỗi.

