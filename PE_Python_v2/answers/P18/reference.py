import tkinter as tk
from tkinter import ttk

def build_form(root):
    saved = []
    status = tk.StringVar(master=root, value="Chua luu")
    entry = ttk.Entry(root)
    entry.grid(row=0, column=0)
    def on_save():
        try:
            score = float(entry.get())
        except ValueError:
            score = None
        if score is None or not (0 <= score <= 10):
            status.set("Diem khong hop le")
            entry.focus_set()
            return
        saved.append(score)
        status.set("Da luu")
    button = ttk.Button(root, text="Luu", command=on_save)
    button.grid(row=0, column=1)
    ttk.Label(root, textvariable=status).grid(row=1, column=0)
    return dict(entry=entry, button=button, status=status, saved=saved)

if __name__ == "__main__":
    root = tk.Tk()
    build_form(root)
    root.mainloop()