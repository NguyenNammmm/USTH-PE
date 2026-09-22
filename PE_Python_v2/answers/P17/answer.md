# P17 - Tkinter: cửa sổ, widget và grid

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk

def build_form(root):
    root.title("So hoc tap")
    ttk.Label(root, text="Ma SV").grid(row=0, column=0)
    sid_entry = ttk.Entry(root)
    sid_entry.grid(row=0, column=1)
    ttk.Label(root, text="Diem").grid(row=1, column=0)
    score_entry = ttk.Entry(root)
    score_entry.grid(row=1, column=1)
    return {"sid_entry": sid_entry, "score_entry": score_entry}

if __name__ == "__main__":
    root = tk.Tk()
    build_form(root)
    root.mainloop()```

## Đáp án kiểm tra hiểu

1. Ô nhập ở đâu so với nhãn?

Đáp án: Cùng hàng, bên phải

- Bên dưới: Muốn bên dưới cần đổi row.
- Không xác định vì column: grid dùng row/column để đặt widget.
- Cùng hàng, bên phải: Đúng: row bằng nhau, column1 sau column0.

2. Muốn nhãn mới ở hàng tiếp theo dùng gì?

Đáp án: row=1

- row=1: Đúng: hàng đếm từ0.
- row=0: row0 là hàng đang có.
- column=-1: Đây không phải cách chọn hàng tiếp theo.

