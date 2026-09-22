import tkinter as tk
from tkinter import ttk
def build(root):
    root.title("Ho so"); root.geometry("420x240"); root.resizable(False,False)
    icon=tk.PhotoImage(master=root,width=16,height=16)
    icon.put("#087e86",to=(0,0,16,16)); root.iconphoto(True,icon); root._icon=icon
    entry=ttk.Entry(root); entry.grid(row=0,column=0); entry.focus_set()
    save=ttk.Button(root,text="Luu")
    save.configure(command=lambda:save.configure(text="Da luu",state="disabled"))
    save.grid(row=1,column=0)
    def help_window():
        child=tk.Toplevel(root); child.title("Huong dan")
        ttk.Label(child,text="Nhap ten roi bam Luu").pack(padx=12,pady=12)
    help_button=ttk.Button(root,text="Tro giup",command=help_window)
    help_button.grid(row=2,column=0)
    return dict(entry=entry,save=save,help=help_button)
