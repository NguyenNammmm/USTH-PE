# C10 - Tuple, unpacking và lựa chọn collection

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def birthday(record):
    name,age,distance=record
    return name,age+1,distance
```

## Đáp án kiểm tra hiểu

1. Tuple chứa một list thì list bên trong có thể append không?

Đáp án: Có

- Có: Đúng: tuple cố định tham chiếu phần tử, không làm mọi đối tượng bên trong bất biến.
- Không vì tuple bất biến: Bất biến không tự lan vào list lồng.
- Chỉ được nếu tuple dài 1: Độ dài tuple không quyết định.

