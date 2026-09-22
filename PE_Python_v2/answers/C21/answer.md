# C21 - File modes, buffering và lỗi I/O

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def append_line(path,text):
    with open(path,"a",encoding="utf8") as stream:
        stream.write(text+"\n")
        stream.flush()
def read_status(path):
    try:
        with open(path,encoding="utf8") as stream:
            return "ok",stream.read()
    except FileNotFoundError:
        return "missing",None
    except PermissionError:
        return "denied",None
```

## Đáp án kiểm tra hiểu

1. Mở log đang có bằng w để thêm một dòng sẽ thế nào?

Đáp án: Xóa nội dung cũ lúc mở

- Giữ toàn bộ và nối: a mới là nối.
- Xóa nội dung cũ lúc mở: Đúng: lựa chọn mode là một phần hợp đồng dữ liệu.
- Chỉ đọc: r mới chỉ đọc.

