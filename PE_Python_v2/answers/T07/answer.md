# T07 - Event loop, after và thanh tiến độ

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from tkinter import ttk
class ProgressJob:
    def __init__(self,root):
        self.root=root; self.pending=None
        self.bar=ttk.Progressbar(root,maximum=100,mode="determinate"); self.bar.pack()
    def start(self):
        self.cancel(); self.bar["value"]=0
        self.pending=self.root.after(100,self.tick)
    def tick(self):
        self.pending=None
        self.bar["value"]=min(100,self.bar["value"]+10)
        if self.bar["value"]<100:
            self.pending=self.root.after(100,self.tick)
    def cancel(self):
        if self.pending is not None:
            self.root.after_cancel(self.pending); self.pending=None
```

## Đáp án kiểm tra hiểu

1. root.after(100,tick()) có đúng không?

Đáp án: Không: tick chạy ngay

- Có: Cần truyền hàm, không gọi ngay.
- Không: tick chạy ngay: Đúng: dùng tick.
- Giống sleep: after với callback không khóa như sleep.

