# P22 - Tiến trình con và mã kết thúc

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import subprocess
import sys

def launch_report():
    completed = subprocess.run(
        [sys.executable, "report_child.py"],
        capture_output=True, text=True, timeout=2,
        shell=False
    )
    return {"stdout": completed.stdout.strip(),
            "returncode": completed.returncode}```

## Đáp án kiểm tra hiểu

1. report là gì khi chạy thành công?

Đáp án: ("7",0)

- ("7",0): Đúng: dữ liệu và mã trạng thái khác nhau.
- (0,7): Bạn đã đổi ý nghĩa hai trường.
- ("7",7): Giá trị chương trình in không thành mã thoát.

2. Vì sao phải có timeout?

Đáp án: Để kiểm soát tiến trình không kết thúc

- Để luôn chạy nhanh hơn: Timeout giới hạn chờ, không làm thuật toán nhanh hơn.
- Để kiểm soát tiến trình không kết thúc: Đúng: có giới hạn cho tình huống bị treo.
- Để tự sửa cú pháp: Nó không sửa code.

