# P07 - Chọn tuple và set đúng mục đích

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = (len(ids), len(set(ids)))```

## Đáp án kiểm tra hiểu

1. report là gì?

Đáp án: (3,2)

- (3,2): Đúng: số lượt trước, số mã khác nhau sau.
- (2,3): Bạn đã đổi thứ tự hai trường.
- (3,3): Set loại mã lặp.

2. Có nên lấy “mã đầu tiên” của set để xếp hạng?

Đáp án: Không, set không là thứ tự xếp hạng

- Có, luôn ổn định: Không dựa vào thứ tự set cho hợp đồng.
- Không, set không là thứ tự xếp hạng: Đúng: xếp hạng cần thứ tự được quy định.
- Chỉ khi có 2 phần tử: Số phần tử không tạo ý nghĩa thứ tự.

