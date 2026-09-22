# P19 - Biểu đồ phải khớp dữ liệu

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from matplotlib.figure import Figure

def build_chart(labels, values):
    fig = Figure()
    ax = fig.subplots()
    positions = list(range(len(labels)))
    ax.bar(positions, values)
    ax.set_xticks(positions, labels)
    ax.set_ylabel("Diem")
    ax.set_ylim(0, 10)
    return fig```

## Đáp án kiểm tra hiểu

1. Cột DB cao bao nhiêu?

Đáp án: 6

- 6: Đúng: dữ liệu của DB là6.
- 10: 10 là giới hạn trục, không phải điểm DB.
- 8: 8 thuộc PY.

2. Chấm hình biểu đồ bằng cách nào tốt hơn ở đây?

Đáp án: Kiểm tra nhãn, dữ liệu cột, giới hạn trục

- Chỉ so ảnh pixel: Font/backend có thể làm khác pixel dù cùng dữ liệu.
- Kiểm tra nhãn, dữ liệu cột, giới hạn trục: Đúng: chấm điều có ý nghĩa trong hợp đồng.
- Chỉ thấy có hình là đạt: Có hình chưa bảo đảm thể hiện đúng dữ liệu.

