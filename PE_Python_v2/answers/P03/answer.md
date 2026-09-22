# P03 - Tách dữ liệu từ tên tệp

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
result = filename.removesuffix(".txt").split("-")```

## Đáp án kiểm tra hiểu

1. parts có giá trị nào?

Đáp án: ["An", "swim"]

- ["An-swim.txt"]: Khi chỉ định -, chuỗi này được chia.
- ["An", "swim"]: Đúng: hậu tố đã bỏ và dấu - chia hai phần.
- "An-swim": Đó là stem, trước khi split.

2. Để bỏ đúng .txt, chọn gì?

Đáp án: removesuffix(".txt")

- split(".") luôn chỉ có hai phần: Tên có thể có thêm dấu chấm; không giả định chỉ một.
- rstrip(".txt"): rstrip xử lý tập ký tự, có thể bỏ nhiều hơn hậu tố.
- removesuffix(".txt"): Đúng: ý định là bỏ hậu tố nguyên vẹn.

