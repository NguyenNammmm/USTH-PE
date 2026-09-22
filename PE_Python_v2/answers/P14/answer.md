# P14 - Lưu cấu trúc dữ liệu bằng JSON

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import json

def save_state(path, state):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False)

def load_state(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"students": []}```

## Đáp án kiểm tra hiểu

1. json.load(file) phục vụ việc gì?

Đáp án: Đọc lại cấu trúc dữ liệu

- Chỉ trả nguyên văn mọi ký tự: Đó là cách đọc text thuần, chưa parse.
- Chạy mã Python trong file: JSON không phải lệnh chạy mã Python.
- Đọc lại cấu trúc dữ liệu: Đúng: parse văn bản JSON thành kiểu phù hợp.

2. Có tự lưu mọi đối tượng Python vào JSON không?

Đáp án: Không, phải chuyển sang dữ liệu được hỗ trợ

- Không, phải chuyển sang dữ liệu được hỗ trợ: Đúng: bài dùng list/dict với kiểu đơn giản.
- Chỉ cần đổi đuôi file: Đổi tên không đổi định dạng.
- Có: Đối tượng tự định nghĩa cần chuyển biểu diễn.

