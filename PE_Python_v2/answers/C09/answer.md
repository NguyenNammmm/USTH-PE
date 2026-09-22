# C09 - Dictionary: duyệt, xóa và tìm cực trị

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def summarize(marks,remove_id):
    remaining=marks.copy()
    removed=remaining.pop(remove_id,None)
    best=min(remaining,key=lambda k:(-remaining[k],k)) if remaining else None
    worst=min(remaining,key=lambda k:(remaining[k],k)) if remaining else None
    return dict(remaining=remaining,removed=removed,best=best,worst=worst)
```

## Đáp án kiểm tra hiểu

1. max(marks) có chắc là mã có điểm cao nhất không?

Đáp án: Không, mặc định so khóa

- Có: max chưa nhận key để so theo điểm.
- Không, mặc định so khóa: Đúng: dùng key=marks.get nếu muốn so giá trị.
- Luôn trả điểm: Kết quả vẫn là một khóa.

