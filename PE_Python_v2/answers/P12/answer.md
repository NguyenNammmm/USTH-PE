# P12 - Đọc file với with và UTF-8

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def load_names(path):
    names = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            name = line.strip()
            if name:
                names.append(name)
    return names```

## Đáp án kiểm tra hiểu

1. Với ba dòng đã nêu, names là gì?

Đáp án: ["An","Binh"]

- ["AnBinh"]: Mỗi dòng có tên là một phần tử riêng.
- ["An","Binh"]: Đúng: dòng trắng bị bỏ, hai tên giữ riêng.
- [" An ","","Binh"]: Bạn chưa áp dụng strip và kiểm tra rỗng.

2. File được đóng khi nào trong with?

Đáp án: Khi rời khối with

- Chỉ khi tắt máy: with không cần đợi đến lúc tắt máy.
- Chỉ khi gọi print: print không quản lý vòng đời file.
- Khi rời khối with: Đúng: context manager quản lý đóng file.

