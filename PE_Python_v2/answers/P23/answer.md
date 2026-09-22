# P23 - Chuyển giao: báo cáo thời gian bơi

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def swim_report(line):
    if not line.strip():
        return {"count": 0, "mean": None}
    values = []
    for part in line.split(","):
        minutes, rest = part.strip().split(":")
        seconds, hundredths = rest.split(".")
        values.append(int(minutes)*6000 + int(seconds)*100 + int(hundredths))
    n = len(values)
    average = (2*sum(values) + n) // (2*n)
    minutes, remainder = divmod(average, 6000)
    seconds, hundredths = divmod(remainder, 100)
    return {"count": n, "mean": f"{minutes}:{seconds:02d}.{hundredths:02d}"}```

## Đáp án kiểm tra hiểu

1. 1:02.50 đổi thành bao nhiêu?

Đáp án: 6250

- 10250: Phút không bằng100 giây.
- 62.50 phút: Đơn vị mục tiêu là phần trăm giây.
- 6250: Đúng: 6000+200+50.

2. 6000 phần trăm giây phải định dạng gì?

Đáp án: 1:00.00

- 1:00.00: Đúng: giây và phần trăm có hai chữ số.
- 1:0.0: Thiếu số0 theo định dạng đề.
- 0:60.00: Cần chuyển đủ60 giây thành1 phút.

