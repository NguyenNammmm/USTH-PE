# T05 - Hộp thoại và lựa chọn file

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from pathlib import Path
import shutil
from tkinter import filedialog,messagebox
def copy_file(source,destination_dir):
    target=Path(destination_dir)/Path(source).name
    shutil.copy2(source,target)
    return str(target)
def choose_and_copy(root):
    source=filedialog.askopenfilename(parent=root)
    if not source: return None
    folder=filedialog.askdirectory(parent=root)
    if not folder: return None
    try:
        result=copy_file(source,folder)
    except OSError as error:
        messagebox.showerror("Khong sao chep",str(error),parent=root)
        return None
    messagebox.showinfo("Da sao chep",result,parent=root)
    return result
```

## Đáp án kiểm tra hiểu

1. Hủy file dialog nên được báo là lỗi đọc file không?

Đáp án: Không, người dùng chưa yêu cầu đọc file

- Có: Hủy là một hành động bình thường.
- Không, người dùng chưa yêu cầu đọc file: Đúng: không đọc và không ghi gì.
- Luôn đóng app: Không có yêu cầu thoát app.

