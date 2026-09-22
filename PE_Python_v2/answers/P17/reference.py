import tkinter as tk
from tkinter import ttk

def build_form(root):
    root.title("So hoc tap")
    ttk.Label(root, text="Ma SV").grid(row=0, column=0)
    sid_entry = ttk.Entry(root)
    sid_entry.grid(row=0, column=1)
    ttk.Label(root, text="Diem").grid(row=1, column=0)
    score_entry = ttk.Entry(root)
    score_entry.grid(row=1, column=1)
    return {"sid_entry": sid_entry, "score_entry": score_entry}

if __name__ == "__main__":
    root = tk.Tk()
    build_form(root)
    root.mainloop()