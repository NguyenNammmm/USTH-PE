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
