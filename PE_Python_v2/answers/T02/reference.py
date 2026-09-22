import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
def build(root):
    for row,title in enumerate(["Mon","Trinh do","Nhac","Xac nhan","Sinh vien","Ghi chu","So buoi"]):
        ttk.Label(root,text=title).grid(row=row,column=0)
    course=ttk.Combobox(root,values=("PY","DB"),state="readonly"); course.set("PY"); course.grid(row=0,column=1)
    level=tk.StringVar(root,value="basic"); box=ttk.Frame(root); box.grid(row=1,column=1)
    for value in ("basic","advanced"):
        ttk.Radiobutton(box,text=value,value=value,variable=level).pack(side="left")
    reminder=tk.BooleanVar(root,value=False); confirmed=tk.BooleanVar(root,value=True)
    ttk.Checkbutton(root,variable=reminder).grid(row=2,column=1)
    ttk.Checkbutton(root,variable=confirmed,state="disabled").grid(row=3,column=1)
    students=tk.Listbox(root,exportselection=False,height=3); students.insert("end","A","B","C"); students.grid(row=4,column=1)
    notes=ScrolledText(root,width=24,height=3); notes.grid(row=5,column=1)
    sessions=ttk.Spinbox(root,from_=1,to=7); sessions.set("1"); sessions.grid(row=6,column=1)
    def collect():
        n=int(sessions.get())
        if not 1<=n<=7: raise ValueError("sessions")
        selected=students.curselection()
        return dict(course=course.get(),level=level.get(),reminder=reminder.get(),
                    student=students.get(selected[0]) if selected else None,
                    notes=notes.get("1.0","end-1c"),sessions=n)
    return dict(course=course,level=level,reminder=reminder,confirmed=confirmed,
                students=students,notes=notes,sessions=sessions,collect=collect)
