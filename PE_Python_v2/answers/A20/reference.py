import tkinter as tk
from tkinter import ttk,messagebox
from datetime import date
def build(root,repository):
    entries={}
    for row,key in enumerate(("id","name","dob")):
        ttk.Label(root,text=key).grid(row=row,column=0)
        entries[key]=ttk.Entry(root); entries[key].grid(row=row,column=1)
    records=tk.Listbox(root); records.grid(row=3,column=0,columnspan=2)
    current_rows=[]
    status=ttk.Label(root,text="San sang"); status.grid(row=5,column=0,columnspan=2)
    def refresh():
        nonlocal current_rows
        rows=repository.all(); records.delete(0,"end")
        current_rows=rows
        for sid,name,dob in rows: records.insert("end",f"{sid} | {name} | {dob}")
    def select_record(event):
        selection=records.curselection()
        if not selection: return
        for key,value in zip(("id","name","dob"),current_rows[selection[0]]):
            entries[key].delete(0,"end"); entries[key].insert(0,str(value))
    records.bind("<<ListboxSelect>>",select_record)
    def act(kind):
        try:
            sid=entries["id"].get().strip(); name=entries["name"].get().strip(); dob=entries["dob"].get().strip()
            if kind!="Refresh" and not sid: raise ValueError("ID rong")
            if kind in ("Add","Rename") and not name: raise ValueError("Ten rong")
            if kind=="Add": date.fromisoformat(dob); repository.add(sid,name,dob)
            elif kind=="Rename": repository.rename(sid,name)
            elif kind=="Delete":
                if not messagebox.askyesno("Xoa",f"Xoa {sid}?",parent=root): return
                repository.delete(sid)
            refresh(); status.configure(text="Da cap nhat")
        except Exception as error: status.configure(text=f"Loi: {error}")
    buttons={}
    panel=ttk.Frame(root); panel.grid(row=4,column=0,columnspan=2)
    for kind in ("Add","Rename","Delete","Refresh"):
        buttons[kind]=ttk.Button(panel,text=kind,command=lambda k=kind:act(k)); buttons[kind].pack(side="left")
    return dict(entries=entries,records=records,status=status,buttons=buttons)
