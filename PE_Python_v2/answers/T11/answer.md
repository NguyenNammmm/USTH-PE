# T11 - Debug watch và mức log

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def save_message(text,logger):
    if not text.strip():
        logger.warning("empty"); return False
    logger.debug("validated"); logger.info("saved"); return True
```

## Đáp án kiểm tra hiểu

1. Logger ở mức WARNING có hiện INFO không?

Đáp án: Không

- Có: INFO thấp hơn ngưỡng.
- Không: Đúng: WARNING và mức cao hơn mới qua.
- Chỉ hiện INFO: Ngược cơ chế lọc.

