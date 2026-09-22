# A06 - Tiến trình, trạng thái và PCB

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
TRANSITIONS={("new","admit"):"ready",("ready","dispatch"):"running",
             ("running","io"):"waiting",("waiting","complete"):"ready",
             ("running","preempt"):"ready",("running","exit"):"terminated"}
def next_state(state,event):
    try: return TRANSITIONS[state,event]
    except KeyError: raise ValueError("invalid transition") from None
```

## Đáp án kiểm tra hiểu

1. Tiến trình chờ dữ liệu từ đĩa nằm ở ready hay waiting?

Đáp án: waiting

- ready: Ready nghĩa là chỉ còn chờ CPU.
- waiting: Đúng: chờ sự kiện I/O.
- terminated: Chờ I/O chưa phải kết thúc.

