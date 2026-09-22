# C01 - Chọn công cụ và dựng môi trường học

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
python -m venv .venv
.venv\Scripts\python -m pip install matplotlib
.venv\Scripts\python -m pip freeze > requirements.txt
.venv\Scripts\python -c "import sys; print(sys.executable)"
.venv\Scripts\python hello.py
# hello.py: print("Hello PE")
```

## Đáp án kiểm tra hiểu

1. Hai dự án cần hai phiên bản thư viện khác nhau. Cách nào phù hợp?

Đáp án: Mỗi dự án có môi trường ảo

- Mỗi dự án có môi trường ảo: Đúng: mỗi môi trường giữ bộ package riêng.
- Cài đè liên tục vào một Python chung: Dự án kia có thể bị đổi dependency.
- Đổi tên file .py: Tên file không tách thư viện.

