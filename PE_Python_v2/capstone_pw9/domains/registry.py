from dataclasses import dataclass
from datetime import date
import math
import numpy as np

class Registry:
    def __init__(self): self.students={}; self.courses={}; self.marks={}
    def add_student(self,student):
        if student.sid in self.students: raise ValueError("duplicate")
        self.students[student.sid]=student
    def add_course(self,course):
        if course.cid in self.courses: raise ValueError("duplicate")
        self.courses[course.cid]=course
    def set_mark(self,sid,cid,score):
        if sid not in self.students or cid not in self.courses: raise ValueError("id")
        if type(score) not in (int,float) or not math.isfinite(score) or not 0<=score<=10: raise ValueError("score")
        self.marks[sid,cid]=math.floor(score*10)/10
    def gpa(self,sid):
        if sid not in self.students: raise ValueError("id")
        rows=[(score,self.courses[cid].credits) for (student,cid),score in self.marks.items() if student==sid]
        if not rows: return None
        a=np.asarray(rows,dtype=float); return float(np.dot(a[:,0],a[:,1])/a[:,1].sum())
    def ranking(self):
        rows=[(sid,self.gpa(sid)) for sid in self.students]
        return sorted(rows,key=lambda r:(r[1] is None,-r[1] if r[1] is not None else 0,r[0]))
    def course_marks(self,cid):
        if cid not in self.courses: raise ValueError("id")
        return [(sid,s.name,self.marks.get((sid,cid))) for sid,s in self.students.items()]
