# C05 - Toán tử, thứ tự tính và làm tròn xuống

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import math
def arithmetic(a,b):
    return dict(add=a+b, sub=a-b, mul=a*b, div=a/b,
                quot=a//b, rem=a%b, power=a**b)
def floor_tenth(x):
    return math.floor(x*10)/10
```

## Đáp án kiểm tra hiểu

1. 17 // 5 và 17 % 5 lần lượt là gì?

Đáp án: 3 và 2

- 3 và 2: Đúng: thương nguyên và phần dư.
- 3.4 và 0: / mới cho thương thực.
- 2 và 3: 17 = 5*3+2.

