from tkinter import ttk
from PIL import Image,ImageTk
class SlideShow:
    def __init__(self,root,paths):
        self.root=root; self.paths=list(paths); self.index=0; self.pending=None; self.photo=None
        self.label=ttk.Label(root); self.label.pack(); self.show()
    def show(self):
        if not self.paths:
            self.label.configure(text="Khong co anh",image=""); return
        with Image.open(self.paths[self.index]) as image:
            image.thumbnail((320,200)); self.photo=ImageTk.PhotoImage(image,master=self.root)
        self.label.configure(image=self.photo,text="")
    def next(self):
        if self.paths: self.index=(self.index+1)%len(self.paths)
        self.show()
    def start(self):
        self.stop(); self.pending=self.root.after(1000,self.tick)
    def tick(self):
        self.pending=None; self.next(); self.pending=self.root.after(1000,self.tick)
    def stop(self):
        if self.pending is not None: self.root.after_cancel(self.pending); self.pending=None
