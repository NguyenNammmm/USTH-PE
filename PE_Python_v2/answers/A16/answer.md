# A16 - SAS, Stata, HDF5 và MATLAB

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import pandas as pd
import h5py
from scipy.io import loadmat
def read_science(path,kind):
    if kind=="stata": return pd.read_stata(path)
    if kind in ("sas7bdat","xport"): return pd.read_sas(path,format=kind,encoding="utf8")
    if kind=="hdf5":
        with h5py.File(path,"r") as handle: return handle["scores"][()]
    if kind=="mat": return loadmat(path)["scores"]
    raise ValueError("kind")
```

## Đáp án kiểm tra hiểu

1. Có thể đổi đuôi CSV thành .h5 để h5py đọc không?

Đáp án: Không, nội dung nhị phân phải đúng format

- Có: Đổi tên không đổi cấu trúc file.
- Không, nội dung nhị phân phải đúng format: Đúng.
- Chỉ cần encode UTF-8: HDF5 có cấu trúc riêng, không là CSV text.

