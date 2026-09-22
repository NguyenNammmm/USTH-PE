# A07 - Mô phỏng FCFS, SJF, priority và round-robin

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from collections import deque
def schedule(jobs,policy,quantum=2):
    if policy not in ("fcfs","sjf","priority","rr") or quantum<=0:
        raise ValueError("policy/quantum")
    ordered=list(jobs)
    if policy=="sjf": ordered.sort(key=lambda row:row[1])
    if policy=="priority": ordered.sort(key=lambda row:row[2])
    queue=deque((sid,burst) for sid,burst,_ in ordered)
    time=0; trace=[]
    while queue:
        sid,remaining=queue.popleft()
        duration=min(quantum,remaining) if policy=="rr" else remaining
        trace.append((sid,time,time+duration)); time+=duration
        if remaining>duration: queue.append((sid,remaining-duration))
    return trace
```

## Đáp án kiểm tra hiểu

1. RR khác FCFS ở điểm nào trong mô hình này?

Đáp án: Có thể thu hồi CPU khi hết quantum

- Có thể thu hồi CPU khi hết quantum: Đúng: job chưa xong về cuối ready queue.
- Luôn chạy job ngắn nhất: Đó là ý tưởng SJF.
- Không có hàng đợi: RR dùng hàng đợi.

