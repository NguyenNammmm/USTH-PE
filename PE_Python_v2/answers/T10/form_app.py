import tkinter as tk
from tkinter import ttk
def passed(score): return score>=5
def build(root):
    entry=ttk.Entry(root); entry.pack()
    status=ttk.Label(root,text="Chua nhap"); status.pack()
    button=ttk.Button(root,text="Kiem tra",command=lambda:status.configure(text="Dat" if passed(float(entry.get())) else "Chua dat")); button.pack()
    return dict(entry=entry,status=status,button=button)
