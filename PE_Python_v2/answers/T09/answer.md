# T09 - Biểu đồ trong Tk và thay đổi thang đo

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class Chart(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.figure=Figure(figsize=(4,3)); self.axes=self.figure.add_subplot()
        self.line,=self.axes.plot([],[],label="Diem")
        self.axes.set(xlabel="Luot",ylabel="Diem"); self.axes.legend()
        self.canvas=FigureCanvasTkAgg(self.figure,master=self)
        self.canvas.get_tk_widget().pack(fill="both",expand=True)
        self.update_values([])
    def update_values(self,values):
        self.line.set_data(list(range(1,len(values)+1)),values)
        self.axes.set_xlim(0,max(1,len(values)+1))
        self.axes.set_ylim(0,max(1,max(values,default=0)+1))
        self.canvas.draw_idle()
```

## Đáp án kiểm tra hiểu

1. Đổi ylim nhưng không redraw thì màn hình chắc đã cập nhật chưa?

Đáp án: Chưa, cần draw/draw_idle

- Chắc rồi: Model thay đổi chưa bảo đảm ảnh được vẽ lại.
- Chưa, cần draw/draw_idle: Đúng.
- Phải mở Tk mới: Chỉ cần redraw canvas hiện có.

