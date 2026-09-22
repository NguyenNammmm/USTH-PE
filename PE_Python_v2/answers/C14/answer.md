# C14 - Comprehension, enumerate, zip và Counter

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from collections import Counter
def report(ids,scores):
    if len(ids)!=len(scores):
        raise ValueError("length mismatch")
    pairs=[(sid,score) for sid,score in zip(ids,scores) if score>=5]
    return [(i,sid,score) for i,(sid,score) in enumerate(pairs,1)]
def top_votes(ids,k):
    return Counter(ids).most_common(k)
```

## Đáp án kiểm tra hiểu

1. zip hai list độ dài 3 và 2 mặc định tạo bao nhiêu cặp?

Đáp án: 2

- 2: Đúng: dừng ở iterable ngắn hơn.
- 3: Không tự thêm phần tử thiếu.
- Báo lỗi: Muốn bắt mismatch có thể dùng strict, nhưng mặc định không lỗi.

