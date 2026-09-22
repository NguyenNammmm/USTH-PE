# P18 - Callback: nối thao tác và trạng thái

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk

def build_form(root):
    saved = []
    status = tk.StringVar(master=root, value="Chua luu")
    entry = ttk.Entry(root)
    entry.grid(row=0, column=0)
    def on_save():
        try:
            score = float(entry.get())
        except ValueError:
            score = None
        if score is None or not (0 <= score <= 10):
            status.set("Diem khong hop le")
            entry.focus_set()
            return
        saved.append(score)
        status.set("Da luu")
    button = ttk.Button(root, text="Luu", command=on_save)
    button.grid(row=0, column=1)
    ttk.Label(root, textvariable=status).grid(row=1, column=0)
    return dict(entry=entry, button=button, status=status, saved=saved)

if __name__ == "__main__":
    root = tk.Tk()
    build_form(root)
    root.mainloop()```

## Đáp án kiểm tra hiểu

1. command=on_save() có vấn đề gì?

Đáp án: Gọi ngay khi tạo nút

- Luôn tạo hai nút: Lỗi này không liên quan số nút.
- Gọi ngay khi tạo nút: Đúng: dấu () thực hiện lời gọi ngay.
- Chỉ chạy sau click: Để truyền callback dùng tên hàm chưa gọi.

2. Nhập điểm abc rồi Luu nên thế nào?

Đáp án: Báo lỗi, giữ dữ liệu để sửa

- Xóa cả form: Xóa dữ liệu làm người học mất ngữ cảnh.
- Lưu0: Không đổi lỗi nhập thành điểm0.
- Báo lỗi, giữ dữ liệu để sửa: Đúng: phản hồi giúp sửa và chưa lưu.

