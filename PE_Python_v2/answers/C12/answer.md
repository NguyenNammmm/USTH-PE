# C12 - Nhánh elif và input trong chương trình CLI

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import math
def classify(text):
    try:
        score=float(text)
    except ValueError:
        return "Invalid"
    if math.isfinite(score) and 0<=score<=10:
        if score>=8:
            return "Gioi"
        elif score>=5:
            return "Dat"
        else:
            return "Chua dat"
    return "Invalid"
def main():
    print(classify(input("Diem: ")))
if __name__=="__main__":
    main()
```

## Đáp án kiểm tra hiểu

1. Nếu kiểm tra >=5 trước >=8 thì điểm 9 ra gì?

Đáp án: Dat

- Gioi: Nhánh đầu đã nhận điểm 9.
- Dat: Đúng: thứ tự điều kiện làm thay đổi kết quả.
- Cả hai: elif không chạy tiếp sau nhánh đúng.

