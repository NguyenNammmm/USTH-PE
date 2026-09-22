# C06 - Chuỗi: chuẩn hóa, định dạng và không sửa tại chỗ

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def labels(text):
    names=[line.strip().lower().title() for line in text.splitlines() if line.strip()]
    return [str(i).zfill(3)+": "+name for i,name in enumerate(names,1)]
def score_label(name,score):
    return "{}: {:.1f}".format(name,score)
```

## Đáp án kiểm tra hiểu

1. raw.upper() không gán lại. raw có đổi không?

Đáp án: Không

- Có: str là immutable.
- Không: Đúng: cần dùng chuỗi được trả về.
- Chỉ ký tự đầu đổi: upper không phải title, và vẫn trả chuỗi mới.

