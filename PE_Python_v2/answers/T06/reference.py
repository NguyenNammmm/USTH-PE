import tkinter as tk
from tkinter import ttk
def build(root):
    canvas=tk.Canvas(root,width=240,height=120); canvas.pack()
    item=canvas.create_rectangle(10,10,50,50,fill="teal")
    tk.Label(root,text="Vi tri",relief="sunken").pack()
    tip=None
    def move():
        x1,y1,x2,y2=canvas.coords(item)
        canvas.move(item,min(20,240-x2),0)
    button=ttk.Button(root,text="Phai",command=move); button.pack()
    def hide_tip(event=None):
        nonlocal tip
        if tip is not None: tip.destroy(); tip=None
    def show_tip(event=None):
        nonlocal tip
        hide_tip(); tip=tk.Toplevel(root); tip.overrideredirect(True)
        tip.geometry(f"+{button.winfo_rootx()}+{button.winfo_rooty()+28}")
        ttk.Label(tip,text="Dich sang phai",padding=4).pack()
    for event in ("<Enter>","<FocusIn>"): button.bind(event,show_tip)
    for event in ("<Leave>","<FocusOut>"): button.bind(event,hide_tip)
    return dict(canvas=canvas,item=item,move=move,show_tip=show_tip,hide_tip=hide_tip)
