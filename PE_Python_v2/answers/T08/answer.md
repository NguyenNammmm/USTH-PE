# T08 - StringVar, scope và component tái sử dụng

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import tkinter as tk
from tkinter import ttk
def normalize_name(text):
    return text.strip().title()
class NameForm(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,padding=8)
        self.name=tk.StringVar(self,value="")
        self.entry=ttk.Entry(self,textvariable=self.name); self.entry.pack()
        self.label=ttk.Label(self,textvariable=self.name); self.label.pack()
        self.button=ttk.Button(self,text="Chuan hoa",command=self.normalize); self.button.pack()
    def normalize(self):
        self.name.set(normalize_name(self.name.get()))
```

## Đáp án kiểm tra hiểu

1. Hai form dùng chung một StringVar, nhập một form thì sao?

Đáp án: Form kia đổi theo

- Form kia đổi theo: Đúng: cả hai cùng binding.
- Hoàn toàn độc lập: Phải có biến riêng mới độc lập.
- Luôn lỗi: Dùng chung hợp lệ, nhưng có thể sai thiết kế.

