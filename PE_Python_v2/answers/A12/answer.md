# A12 - Nhiều worker, dừng hợp tác và queue qua module

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from threading import Thread,Event
from queue import Queue
class SquareWorker(Thread):
    def __init__(self,job_id,value,output,stop_event):
        super().__init__(); self.job_id=job_id; self.value=value; self.output=output; self.stop_event=stop_event
    def run(self):
        if not self.stop_event.is_set(): self.output.put((self.job_id,self.value**2))
def run_many(values):
    output=Queue(); stop=Event()
    workers=[SquareWorker(i,value,output,stop) for i,value in enumerate(values)]
    for worker in workers: worker.start()
    for worker in workers: worker.join()
    result={}
    while not output.empty():
        i,value=output.get(); result[i]=value
    return [result[i] for i in range(len(values))]
```

## Đáp án kiểm tra hiểu

1. Muốn worker nhận queue của controller, nên làm gì?

Đáp án: Truyền cùng queue qua constructor

- Tạo queue riêng không trả ra: Controller không đọc được queue riêng.
- Truyền cùng queue qua constructor: Đúng: dependency được truyền tường minh.
- Dùng sleep để đọc biến global: Sleep không là giao thức kết quả.

