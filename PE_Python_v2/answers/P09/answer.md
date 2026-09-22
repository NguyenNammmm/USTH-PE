# P09 - While, sentinel và điều kiện dừng

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
i = 0
result = 0
while i < len(values) and values[i] != -1:
    result += values[i]
    i += 1```

## Đáp án kiểm tra hiểu

1. total cuối là gì?

Đáp án: 14

- 23: Bạn đã cộng cả dữ liệu sau dấu kết thúc.
- 14: Đúng: chỉ cộng 6 và 8.
- 13: -1 là dấu kết thúc, không là điểm để cộng.

2. Nếu quên i += 1?

Đáp án: Có thể lặp mãi ở phần tử đầu

- Tự tăng i: while không tự tăng biến chỉ số.
- Luôn dừng ngay: Điều kiện không tự đổi sang False.
- Có thể lặp mãi ở phần tử đầu: Đúng: i không tiến nên vẫn đọc cùng phần tử.

