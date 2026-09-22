# A11 - Race condition và Lock

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from threading import Thread,Lock
def count_parallel(workers,iterations):
    count=0; lock=Lock()
    def work():
        nonlocal count
        for _ in range(iterations):
            with lock: count+=1
    threads=[Thread(target=work) for _ in range(workers)]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    return count
```

## Đáp án kiểm tra hiểu

1. Chỉ khóa bước write nhưng read nằm ngoài lock có đủ không?

Đáp án: Không

- Đủ: Hai worker vẫn có thể đọc cùng giá trị cũ.
- Không: Đúng: bảo vệ toàn bộ thao tác logic.
- GIL luôn giải quyết: GIL không thay thế hợp đồng đồng bộ.

