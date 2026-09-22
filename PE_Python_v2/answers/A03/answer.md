# A03 - Curses: menu bàn phím cho quản lý điểm

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
import curses
def main(screen):
    selected=0; message=""; choices=["Students","Courses","Exit"]
    while True:
        screen.erase(); height,width=screen.getmaxyx()
        for row,text in enumerate(choices+[message]):
            if row<height-1 and width>1:
                screen.addnstr(row,0,text,width-1,curses.A_REVERSE if row==selected else curses.A_NORMAL)
        screen.refresh(); key=screen.getch()
        if key==ord("q"): break
        if key==curses.KEY_UP: selected=(selected-1)%3
        elif key==curses.KEY_DOWN: selected=(selected+1)%3
        elif key in (10,13,curses.KEY_ENTER):
            if selected==2: break
            message="An, Binh" if selected==0 else "Python"
if __name__=="__main__": curses.wrapper(main)
```

## Đáp án kiểm tra hiểu

1. Vì sao dùng wrapper thay tự gọi main(None)?

Đáp án: Để quản lý môi trường terminal

- Để quản lý môi trường terminal: Đúng: screen và chế độ terminal phải được chuẩn bị và dọn.
- Để chạy nhanh hơn mọi GUI: Không có bảo đảm tốc độ đó.
- Để tự tạo database: Curses chỉ lo UI terminal.

