# C02 - REPL, script và notebook: trạng thái đến từ đâu?

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
Cell 1: base = 7
Cell 2: total = base + 5
Cell 3: print(total)
Script chứa ba câu theo đúng thứ tự.
Sau restart, cell 2 trước cell 1 phát sinh NameError. Kết quả đúng sau Run All là 12.
```

## Đáp án kiểm tra hiểu

1. Sau Restart Kernel, chạy ngay cell 2 thì sao?

Đáp án: NameError

- In 4: Giá trị cũ đã mất.
- NameError: Đúng: count chưa tồn tại trong kernel mới.
- Tự chạy cell 1: Kernel không tự sắp thứ tự cell.

