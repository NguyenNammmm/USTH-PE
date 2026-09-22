# C15 - Ngẫu nhiên có thể kiểm thử

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import random
def sample(deck,seed):
    if not deck:
        return None
    rng=random.Random(seed)
    return rng.choice(deck),rng.randint(0,10),rng.random()
```

## Đáp án kiểm tra hiểu

1. randint(0,10) có thể trả 10 không?

Đáp án: Có

- Có: Đúng: cả hai đầu đều được bao gồm.
- Không: Đừng nhầm với stop của range.
- Chỉ khi seed=10: Seed không quy định biên như vậy.

