# X03 - PW5-PW6: ba file, archive và pickle có nén

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from pathlib import Path
import json,zipfile,gzip,pickle
KEYS=("students","courses","marks")
def save_text_bundle(folder,state):
    folder=Path(folder); folder.mkdir(parents=True,exist_ok=True)
    for key in KEYS: (folder/(key+".txt")).write_text(json.dumps(state[key],ensure_ascii=False),encoding="utf8")
    with zipfile.ZipFile(folder/"students.dat","w",zipfile.ZIP_DEFLATED) as archive:
        for key in KEYS: archive.write(folder/(key+".txt"),arcname=key+".txt")
def load_text_bundle(folder):
    path=Path(folder)/"students.dat"
    if not path.exists(): return {key:{} for key in KEYS}
    with zipfile.ZipFile(path) as archive:
        return {key:json.loads(archive.read(key+".txt").decode("utf8")) for key in KEYS}
def save_pickle(path,registry):
    with gzip.open(path,"wb") as stream: pickle.dump(registry,stream,pickle.HIGHEST_PROTOCOL)
def load_pickle(path):
    if not Path(path).exists(): return None
    with gzip.open(path,"rb") as stream: return pickle.load(stream)
```

## Đáp án kiểm tra hiểu

1. Đọc file nén hỏng rồi coi như lớp rỗng có phù hợp không?

Đáp án: Không, phải báo lỗi để tránh mất dữ liệu

- Có: Có thể ghi đè lên dữ liệu cần phục hồi.
- Không, phải báo lỗi để tránh mất dữ liệu: Đúng.
- Chỉ khi có UI: Nguyên tắc áp dụng cả CLI và GUI.

