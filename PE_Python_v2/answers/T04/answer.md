# T04 - Menu và nhiều Notebook

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk
def build(root):
    tabs=ttk.Notebook(root); tabs.pack(fill="both",expand=True)
    student=ttk.Frame(tabs); report=ttk.Frame(tabs)
    tabs.add(student,text="Sinh vien"); tabs.add(report,text="Bao cao")
    entry=ttk.Entry(student); entry.pack()
    nested=ttk.Notebook(report); nested.pack(fill="both",expand=True)
    for title in ("Bang","Bieu do"):
        frame=ttk.Frame(nested); nested.add(frame,text=title)
    menu=tk.Menu(root); root.configure(menu=menu)
    file_menu=tk.Menu(menu,tearoff=False); menu.add_cascade(label="Tep",menu=file_menu)
    file_menu.add_command(label="Moi",command=lambda:entry.delete(0,"end"))
    view=tk.Menu(menu,tearoff=False); menu.add_cascade(label="Xem",menu=view)
    view.add_command(label="Bao cao",command=lambda:tabs.select(report))
    return dict(tabs=tabs,nested=nested,entry=entry,menu_file=file_menu,menu_view=view,report=report)
```

## Đáp án kiểm tra hiểu

1. command=reset_form() có đúng khi gắn menu không?

Đáp án: Không, hàm bị gọi ngay

- Có: Cần truyền hàm.
- Không, hàm bị gọi ngay: Đúng: dùng command=reset_form.
- Đúng nếu tab đầu: Tab không quyết định thời điểm gọi.

