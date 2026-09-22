import tkinter as tk
from tkinter import ttk
def normalize_name(text):
    return text.strip().title()
class NameForm(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent,padding=8)
        self.name=tk.StringVar(self,value="")
        self.entry=ttk.Entry(self,textvariable=self.name); self.entry.pack()
        self.label=ttk.Label(self,textvariable=self.name); self.label.pack()
        self.button=ttk.Button(self,text="Chuan hoa",command=self.normalize); self.button.pack()
    def normalize(self):
        self.name.set(normalize_name(self.name.get()))
