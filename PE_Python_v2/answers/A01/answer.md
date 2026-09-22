# A01 - Đa kế thừa, MRO và lớp trừu tượng

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from abc import ABC,abstractmethod
class Exporter(ABC):
    @abstractmethod
    def export(self,rows): pass
class TextExporter(Exporter):
    def export(self,rows): return ",".join(rows)
class UpperMixin:
    def export(self,rows): return super().export(rows).upper()
class LoudExporter(UpperMixin,TextExporter): pass
```

## Đáp án kiểm tra hiểu

1. Subclass chưa cài abstractmethod có tạo instance được không?

Đáp án: Không, TypeError

- Được: ABC theo dõi phương thức trừu tượng chưa cài.
- Không, TypeError: Đúng.
- Chỉ cần đổi tên class: Tên class không đáp ứng hợp đồng.

