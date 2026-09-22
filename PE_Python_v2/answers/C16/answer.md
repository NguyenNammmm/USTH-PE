# C16 - Ngày giờ và tìm mẫu bằng regex

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from datetime import datetime,timedelta
import re
def due_date(text,days):
    return (datetime.strptime(text,"%Y-%m-%d")+timedelta(days=days)).strftime("%Y-%m-%d")
def extract_id(text):
    match=re.search(r"\bS\d{3}\b",text)
    return match.group(0) if match else None
def clean_spaces(text):
    return re.sub(r"\s+"," ",text).strip()
```

## Đáp án kiểm tra hiểu

1. Regex khớp 2024-02-31 chứng minh ngày đó hợp lệ chưa?

Đáp án: Chưa

- Rồi: Regex cấu trúc không xác nhận lịch.
- Chưa: Đúng: strptime sẽ bác ngày không tồn tại.
- Chỉ cần đúng 10 ký tự: Độ dài không đủ.

