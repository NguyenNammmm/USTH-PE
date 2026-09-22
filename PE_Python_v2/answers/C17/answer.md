# C17 - Tên file thành hồ sơ người bơi

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import re
def parse_filename(filename):
    if not filename.endswith(".txt"):
        raise ValueError("extension")
    parts=filename.removesuffix(".txt").split("-")
    if len(parts)!=4:
        raise ValueError("fields")
    name,age_text,distance,stroke=parts
    if not name or not stroke or not age_text.isdecimal():
        raise ValueError("metadata")
    if not re.fullmatch(r"[1-9]\d*m",distance):
        raise ValueError("distance")
    return dict(name=name,age=int(age_text),distance=distance,stroke=stroke)
```

## Đáp án kiểm tra hiểu

1. Tên An-19-50m-Free.txt có lỗi tuổi thì sửa ở bước nào?

Đáp án: Phân tích metadata

- Tính trung bình lượt bơi: Bước tính lượt không đọc tuổi.
- Phân tích metadata: Đúng: xác thực từng trường ngay sau tách tên file.
- Vẽ biểu đồ: Biểu đồ không sửa metadata.

