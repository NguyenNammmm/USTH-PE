# A15 - DataFrame từ CSV, Excel và database

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import pandas as pd
from sqlalchemy import text
def read_csv_scores(path): return pd.read_csv(path,na_values=[""])
def read_excel_scores(path): return pd.read_excel(path,sheet_name="Scores",usecols=["id","score"])
def read_database(engine):
    with engine.connect() as connection:
        return pd.read_sql_query(text("SELECT id,score FROM scores ORDER BY id"),connection)
```

## Đáp án kiểm tra hiểu

1. DataFrame.info() có trả một DataFrame mới không?

Đáp án: Không, chủ yếu in thông tin và trả None

- Có: Không dùng kết quả info để thay frame.
- Không, chủ yếu in thông tin và trả None: Đúng.
- Trả list điểm: Đó không phải phép tổng hợp điểm.

