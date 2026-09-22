# P21 - Thread và queue: nhận kết quả việc nền

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from threading import Thread
from queue import Queue

def run_job(values):
    q = Queue()
    def work():
        q.put([value * value for value in values])
    thread = Thread(target=work)
    thread.start()
    thread.join()
    return q.get()```

## Đáp án kiểm tra hiểu

1. Lệnh nào khởi động thread mới?

Đáp án: t.start()

- t.run(): run trực tiếp chạy như lời gọi thường.
- t.start(): Đúng: start khởi động luồng.
- q.get(): get lấy dữ liệu từ queue.

2. Worker nên cập nhật UI của app theo thiết kế này bằng cách nào?

Đáp án: Gửi message, UI thread nhận và cập nhật

- Gọi widget tùy ý từ worker: Không coi đây là cơ chế an toàn mặc định.
- Dùng sleep thật lâu trong click: sleep trong click làm UI bị chặn.
- Gửi message, UI thread nhận và cập nhật: Đúng: tách kết quả worker và cập nhật UI.

