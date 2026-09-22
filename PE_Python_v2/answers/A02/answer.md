# A02 - NumPy và xếp hạng GPA có trọng số

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import numpy as np
def gpa(marks,credits):
    m=np.asarray(marks,dtype=float); c=np.asarray(credits,dtype=float)
    if m.ndim!=1 or c.ndim!=1 or m.shape!=c.shape:
        raise ValueError("shape")
    if not (np.isfinite(m).all() and np.isfinite(c).all()) or (m<0).any() or (m>10).any() or (c<=0).any():
        raise ValueError("values")
    return float(np.dot(m,c)/c.sum()) if len(m) else None
def ranking(records):
    rows=[(sid,gpa(*pair)) for sid,pair in records.items()]
    return sorted(rows,key=lambda row:(row[1] is None,-row[1] if row[1] is not None else 0,row[0]))
```

## Đáp án kiểm tra hiểu

1. Có nên chia tổng điểm có trọng số cho số môn không?

Đáp án: Không, chia tổng tín chỉ

- Có: Sẽ sai khi tín chỉ khác nhau.
- Không, chia tổng tín chỉ: Đúng.
- Chia số sinh viên: Số sinh viên không tham gia công thức GPA.

