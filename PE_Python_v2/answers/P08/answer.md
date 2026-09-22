# P08 - Vòng for và biến tích lũy

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = 0
for stock in stocks:
    if stock >= 10:
        result += 1```

## Đáp án kiểm tra hiểu

1. count cuối bằng bao nhiêu?

Đáp án: 2

- 1: Bạn có thể đã quên tính đúng bằng 5.
- 3: 3 là số phần tử, không phải số điểm đạt.
- 2: Đúng: 5 và 8 đạt.

2. Đặt count=0 bên trong for gây gì?

Đáp án: Xóa kết quả trước mỗi lượt

- Xóa kết quả trước mỗi lượt: Đúng: bộ đếm không còn cộng dồn.
- Không ảnh hưởng: Vị trí khởi tạo ảnh hưởng kết quả.
- Luôn nhanh hơn: Tốc độ không sửa được lỗi logic.

