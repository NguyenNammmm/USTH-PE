import curses
def show_rows(rows):
    lines=[" | ".join(map(str,row)) for row in rows] or ["Khong co du lieu"]
    def screen(stdscr):
        offset=0
        while True:
            stdscr.erase(); h,w=stdscr.getmaxyx()
            for y,text in enumerate(lines[offset:offset+max(0,h-2)]):
                if w>1: stdscr.addnstr(y,0,text,w-1)
            if h>1 and w>1: stdscr.addnstr(h-1,0,"q: quay lai; up/down: cuon",w-1)
            stdscr.refresh(); key=stdscr.getch()
            if key==ord("q"): break
            if key==curses.KEY_DOWN: offset=min(max(0,len(lines)-1),offset+1)
            if key==curses.KEY_UP: offset=max(0,offset-1)
    curses.wrapper(screen)
