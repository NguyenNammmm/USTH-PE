# T01 - Cửa sổ, focus và trạng thái nút

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk
def build(root):
    root.title("Ho so"); root.geometry("420x240"); root.resizable(False,False)
    icon=tk.PhotoImage(master=root,width=16,height=16)
    icon.put("#087e86",to=(0,0,16,16)); root.iconphoto(True,icon); root._icon=icon
    entry=ttk.Entry(root); entry.grid(row=0,column=0); entry.focus_set()
    save=ttk.Button(root,text="Luu")
    save.configure(command=lambda:save.configure(text="Da luu",state="disabled"))
    save.grid(row=1,column=0)
    def help_window():
        child=tk.Toplevel(root); child.title("Huong dan")
        ttk.Label(child,text="Nhap ten roi bam Luu").pack(padx=12,pady=12)
    help_button=ttk.Button(root,text="Tro giup",command=help_window)
    help_button.grid(row=2,column=0)
    return dict(entry=entry,save=save,help=help_button)
```

## Đáp án kiểm tra hiểu

1. Đổi text của nút thành Da luu có tự vô hiệu hóa nút không?

Đáp án: Không, phải đổi state

- Có: Text và state độc lập.
- Không, phải đổi state: Đúng: cần state disabled.
- Nút tự biến mất: Đổi text không xóa widget.

