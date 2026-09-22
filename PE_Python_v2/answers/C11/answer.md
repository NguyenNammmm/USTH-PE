# C11 - range, break và continue

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def collect(start,stop,step,blocked):
    result=[]
    for n in range(start,stop,step):
        if n==blocked:
            break
        if n%3==0:
            continue
        result.append(n)
    return result
```

## Đáp án kiểm tra hiểu

1. list(range(5,0,-2)) là gì?

Đáp án: [5,3,1]

- [5,3,1]: Đúng: bước âm đi về stop nhưng không chứa stop.
- [5,3,1,0]: Bước -2 không chạm 0, stop cũng bị loại.
- []: Start lớn hơn stop phù hợp bước âm.

