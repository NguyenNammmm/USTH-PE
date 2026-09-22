# C08 - Thêm, xóa và đảo list

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def edit(values,extras,target):
    result=values.copy()
    result.extend(extras)
    if target in result:
        result.remove(target)
    removed=result.pop() if result else None
    result.reverse()
    return result,removed
```

## Đáp án kiểm tra hiểu

1. remove(2) trên [2,5,2] để lại gì?

Đáp án: [5,2]

- [5]: remove chỉ xóa lần xuất hiện đầu.
- [5,2]: Đúng.
- [2,5]: Đây là kết quả pop cuối, không phải remove(2).

