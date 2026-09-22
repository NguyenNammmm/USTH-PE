# C07 - Index và slice: chọn đúng phần dữ liệu

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def select_parts(text,items):
    return text[:3],text[::-1],items[-3:],items[1::2]
def replace_middle(items):
    result=items.copy()
    result[1:3]=[99]
    return result
```

## Đáp án kiểm tra hiểu

1. "Python"[1:4] là gì?

Đáp án: yth

- yth: Đúng: các index 1,2,3.
- ytho: Index 4 bị loại bởi stop.
- Pyt: Start là 1, không phải 0.

