# P05 - List và việc hai tên dùng chung dữ liệu

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = scores.copy()
result.append(extra)```

## Đáp án kiểm tra hiểu

1. scores sau ba dòng là gì?

Đáp án: [6,8]

- [6,8,9]: Đó là draft; scores được giữ nguyên.
- None: append trả None nhưng không gán nó vào scores.
- [6,8]: Đúng: append tác động lên bản sao.

2. Nếu draft = scores thì append sẽ ảnh hưởng gì?

Đáp án: Cả hai tên thấy thay đổi

- Cả hai tên thấy thay đổi: Đúng: hai tên cùng tham chiếu đối tượng.
- Không tên nào: append thay đổi list đó.
- Chỉ draft: Hai tên đang dùng chung một list.

