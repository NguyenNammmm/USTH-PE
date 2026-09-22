# T03 - Bố cục: Frame, padding và co giãn

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk
def build(root):
    outer=ttk.Frame(root,padding=12); outer.pack(fill="both",expand=True)
    outer.columnconfigure(0,weight=1); outer.rowconfigure(0,weight=1)
    group=ttk.LabelFrame(outer,text="Ho so",padding=12); group.grid(row=0,column=0,sticky="nsew")
    group.columnconfigure(1,weight=1)
    ttk.Label(group,text="Ten").grid(row=0,column=0,padx=6,pady=6)
    entry=ttk.Entry(group); entry.grid(row=0,column=1,sticky="ew",padx=6,pady=6)
    area=ttk.Frame(outer,height=40); area.grid(row=1,column=0,sticky="ew")
    badge=ttk.Label(area,text="PE"); badge.place(relx=1,x=-8,y=8,anchor="ne")
    return dict(outer=outer,group=group,entry=entry,badge=badge)
```

## Đáp án kiểm tra hiểu

1. Entry sticky="ew" nhưng cột weight=0 có chắc giãn hết khi cửa sổ lớn lên không?

Đáp án: Không, cột cần được phân chia phần dư

- Có: sticky chỉ lấp ô đã được cấp.
- Không, cột cần được phân chia phần dư: Đúng: weight quyết định phân chia phần dư cho cột.
- Entry tự đổi parent: Parent không đổi.

