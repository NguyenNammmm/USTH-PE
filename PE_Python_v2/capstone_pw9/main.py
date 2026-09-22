"""Reference PW9. Run with a desktop Tk environment and NumPy installed."""
from pathlib import Path
import tkinter as tk
from tkinter import ttk,messagebox
from domains import Registry,Student,Course
from persistence import load_pickle
from background import start_save

class App:
    def __init__(self,root,path):
        self.root=root; self.path=Path(path); self.busy=False; self.dirty=False
        self.worker=None; self.results=None; self.closing=False; self.edit_controls=[]
        loaded=load_pickle(self.path)
        self.registry=loaded if loaded is not None else Registry()
        if not isinstance(self.registry,Registry): raise ValueError('File does not contain Registry')
        root.title('PE - So hoc tap'); root.geometry('760x560')
        self.tabs=ttk.Notebook(root); self.tabs.pack(fill='both',expand=True,padx=12,pady=12)
        self.frames={}
        for key,title in [('students','Sinh vien'),('courses','Mon hoc'),('marks','Diem'),('report','Bao cao')]:
            frame=ttk.Frame(self.tabs,padding=12); self.tabs.add(frame,text=title); self.frames[key]=frame
        self.student_entries=self.fields(self.frames['students'],['ID','Ten','DoB YYYY-MM-DD'])
        self.add_button(self.frames['students'],'Them sinh vien',self.add_student,3)
        self.student_list=tk.Listbox(self.frames['students'],height=12,width=70); self.student_list.grid(row=4,column=0,columnspan=2,sticky='nsew')
        self.course_entries=self.fields(self.frames['courses'],['ID','Ten','Tin chi'])
        self.add_button(self.frames['courses'],'Them mon',self.add_course,3)
        self.course_list=tk.Listbox(self.frames['courses'],height=12,width=70); self.course_list.grid(row=4,column=0,columnspan=2,sticky='nsew')
        frame=self.frames['marks']
        self.sid=ttk.Combobox(frame,state='readonly'); self.cid=ttk.Combobox(frame,state='readonly')
        self.score=ttk.Entry(frame)
        for row,(title,widget) in enumerate([('Ma sinh vien',self.sid),('Ma mon',self.cid),('Diem',self.score)]):
            ttk.Label(frame,text=title).grid(row=row,column=0,pady=5)
            widget.grid(row=row,column=1,sticky='ew',pady=5); self.edit_controls.append(widget)
        self.add_button(frame,'Luu diem',self.set_mark,3)
        self.cid.bind('<<ComboboxSelected>>',lambda event:self.refresh_marks())
        self.mark_list=tk.Listbox(frame,height=12,width=70); self.mark_list.grid(row=4,column=0,columnspan=2,sticky='nsew')
        self.report=tk.Listbox(self.frames['report'],height=16,width=70); self.report.pack(fill='both',expand=True)
        footer=ttk.Frame(root,padding=12); footer.pack(fill='x')
        self.status=ttk.Label(footer,text='San sang'); self.status.pack(side='left')
        self.save_button=ttk.Button(footer,text='Luu file',command=self.save); self.save_button.pack(side='right')
        self.refresh(); root.protocol('WM_DELETE_WINDOW',self.close)

    def fields(self,parent,titles):
        entries=[]; parent.columnconfigure(1,weight=1); parent.rowconfigure(4,weight=1)
        for row,title in enumerate(titles):
            ttk.Label(parent,text=title).grid(row=row,column=0,padx=5,pady=5)
            entry=ttk.Entry(parent); entry.grid(row=row,column=1,padx=5,pady=5,sticky='ew')
            entries.append(entry); self.edit_controls.append(entry)
        return entries

    def add_button(self,parent,title,command,row):
        button=ttk.Button(parent,text=title,command=command); button.grid(row=row,column=1,pady=6)
        self.edit_controls.append(button); return button

    def change(self,action):
        if self.busy: return
        try: action()
        except (ValueError,TypeError,KeyError) as error:
            self.status.configure(text='Loi: '+str(error)); return
        self.dirty=True; self.status.configure(text='Chua luu'); self.refresh()

    def add_student(self):
        values=[entry.get().strip() for entry in self.student_entries]
        self.change(lambda:self.registry.add_student(Student(*values)))

    def add_course(self):
        values=[entry.get().strip() for entry in self.course_entries]
        def action(): self.registry.add_course(Course(values[0],values[1],int(values[2])))
        self.change(action)

    def set_mark(self):
        self.change(lambda:self.registry.set_mark(self.sid.get(),self.cid.get(),float(self.score.get())))

    def refresh(self):
        self.student_list.delete(0,'end'); self.course_list.delete(0,'end'); self.report.delete(0,'end')
        for student in self.registry.students.values(): self.student_list.insert('end',' | '.join(map(str,student.list())))
        for course in self.registry.courses.values(): self.course_list.insert('end',' | '.join(map(str,course.list())))
        self.sid.configure(values=list(self.registry.students)); self.cid.configure(values=list(self.registry.courses))
        for sid,gpa in self.registry.ranking():
            text='Chua co diem' if gpa is None else str(round(gpa,3))
            self.report.insert('end',f'{sid} | {self.registry.students[sid].name} | {text}')
        self.refresh_marks()

    def refresh_marks(self):
        self.mark_list.delete(0,'end'); cid=self.cid.get()
        if cid in self.registry.courses:
            for sid,name,score in self.registry.course_marks(cid):
                self.mark_list.insert('end',f'{sid} | {name} | {score if score is not None else "Chua co diem"}')

    def set_busy(self,value):
        self.busy=value
        for widget in self.edit_controls:
            if value: widget.state(['disabled'])
            else: widget.state(['!disabled'])
        self.save_button.state(['disabled'] if value else ['!disabled'])

    def save(self):
        if self.busy: return
        self.set_busy(True); self.status.configure(text='Dang luu')
        self.worker,self.results=start_save(self.registry,self.path)
        self.root.after(30,self.poll)

    def poll(self):
        if self.worker.is_alive(): self.root.after(30,self.poll); return
        status,value=self.results.get_nowait(); self.set_busy(False)
        if status=='ok':
            self.dirty=False; self.status.configure(text='Da luu')
            if self.closing: self.root.destroy()
        else:
            self.closing=False; self.status.configure(text='Loi luu: '+value)

    def close(self):
        if self.busy:
            self.closing=True; self.status.configure(text='Cho luu xong de dong'); return
        if not self.dirty: self.root.destroy(); return
        answer=messagebox.askyesnocancel('Dong','Luu thay doi truoc khi dong?',parent=self.root)
        if answer is None: return
        if answer: self.closing=True; self.save()
        else: self.root.destroy()

def main():
    root=tk.Tk(); root.withdraw()
    try: App(root,Path(__file__).with_name('students.dat'))
    except Exception as error:
        messagebox.showerror('Khong nap duoc du lieu',str(error),parent=root); root.destroy(); return
    root.deiconify(); root.mainloop()

if __name__=='__main__': main()
