# A10 - Bộ nhớ dùng chung, GIL và chọn concurrency

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```text
Tải URL: thread hoặc async để xen kẽ I/O, giới hạn đồng thời. CPU Python trên build có GIL: process có thể dùng nhiều core nhưng phải tính overhead. GUI: main loop giữ widget, worker chỉ gửi dữ liệu qua queue. Apache/Chromium là ví dụ phân chia worker/process trong slide, không chứng minh kiến trúc mọi phiên bản. Scalability phải đo khi tăng worker và tải; responsiveness là khả năng trả lời sự kiện.
```

## Đáp án kiểm tra hiểu

1. Bốn thread tính Python thuần trên CPython có GIL có chắc nhanh gấp4 không?

Đáp án: Không

- Có: Còn GIL và chi phí điều phối.
- Không: Đúng: phải đo, không suy từ số core.
- GIL cấm mọi I/O song song: Thread vẫn hữu ích khi chờ I/O.

