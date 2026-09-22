# C22 - Duyệt thư mục và thao tác file trong vùng bài tập

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import os
from pathlib import Path
def text_files(root):
    root=Path(root)
    result=[]
    for folder,dirs,files in os.walk(root,followlinks=False):
        for name in files:
            if name.endswith(".txt"):
                result.append((Path(folder)/name).relative_to(root).as_posix())
    return sorted(result)
```

## Đáp án kiểm tra hiểu

1. os.chdir thay đổi gì?

Đáp án: Working directory của tiến trình

- Di chuyển file: File không bị di chuyển.
- Working directory của tiến trình: Đúng: đường dẫn tương đối sau đó được giải từ nơi mới.
- Tên module: Module không tự đổi tên.

