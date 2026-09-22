# A14 - Đọc bảng số bằng NumPy

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import numpy as np
def load_scores(path):
    return np.loadtxt(path,delimiter=",",skiprows=1,usecols=[1,2],ndmin=2)
def load_missing(path):
    return np.genfromtxt(path,delimiter=",",skip_header=1,filling_values=-1,ndmin=2)
```

## Đáp án kiểm tra hiểu

1. usecols=[1,2] chọn cột thứ mấy?

Đáp án: Thứ2 và3

- Thứ1 và2: Index cột bắt đầu từ0.
- Thứ2 và3: Đúng.
- Hai dòng đầu: usecols là cột, không phải dòng.

