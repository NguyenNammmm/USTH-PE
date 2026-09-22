# A26 - Hoạt ảnh OpenGL: chuyển động theo thời gian

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
def advance(x,v,dt,limit):
    if limit<=0 or dt<0: raise ValueError("bounds")
    if v==0: return x,0
    phase=(x+v*dt)%(2*limit)
    if phase==0: return 0,abs(v)
    if phase==limit: return limit,-abs(v)
    return (phase,v) if phase<limit else (2*limit-phase,-v)
```

## Đáp án kiểm tra hiểu

1. Cập nhật x+=1 mỗi frame trên30FPS và60FPS có cùng tốc độ không?

Đáp án: Không,60FPS nhanh gấp đôi

- Có: Mỗi giây có số bước khác nhau.
- Không,60FPS nhanh gấp đôi: Đúng: dùng velocity*dt.
- Chỉ phụ thuộc màu: Màu không quyết định vận tốc.

