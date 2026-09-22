# A05 - Pickle, JSON và dữ liệu có kiểu

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import pickle,gzip
def dump_state(state):
    return gzip.compress(pickle.dumps(state,protocol=pickle.HIGHEST_PROTOCOL))
def load_state(blob):
    return pickle.loads(gzip.decompress(blob))
```

## Đáp án kiểm tra hiểu

1. Có thể dùng pickle.load cho file người lạ tải lên không?

Đáp án: Không, quá trình unpickle có thể chạy mã

- Có vì chỉ là dữ liệu: Pickle không chỉ là parser dữ liệu thuần.
- Không, quá trình unpickle có thể chạy mã: Đúng: chỉ lab file tự tạo và tin cậy.
- Có nếu đuôi .dat: Đuôi file không xác định mức tin cậy.

