from datetime import date
import math
def empty(): return dict(students={},courses={},marks={})
def add_student(state,sid,name,dob):
    if not sid.strip() or not name.strip() or sid in state["students"]: raise ValueError("student")
    date.fromisoformat(dob); state["students"][sid]=dict(name=name,dob=dob)
def add_course(state,cid,name):
    if not cid.strip() or not name.strip() or cid in state["courses"]: raise ValueError("course")
    state["courses"][cid]=dict(name=name)
def set_mark(state,cid,sid,score):
    if cid not in state["courses"] or sid not in state["students"]: raise ValueError("unknown id")
    if type(score) not in (int,float) or not math.isfinite(score) or not 0<=score<=10: raise ValueError("score")
    state["marks"].setdefault(cid,{})[sid]=float(score)
def list_students(state): return [(sid,r["name"],r["dob"]) for sid,r in state["students"].items()]
def list_courses(state): return [(cid,r["name"]) for cid,r in state["courses"].items()]
def course_marks(state,cid):
    if cid not in state["courses"]: raise ValueError("unknown course")
    return [(sid,r["name"],state["marks"].get(cid,{}).get(sid)) for sid,r in state["students"].items()]
def collect(input_fn=input):
    state=empty(); count=int(input_fn("So sinh vien: "))
    if count<0: raise ValueError("count")
    for _ in range(count): add_student(state,input_fn("ID: "),input_fn("Ten: "),input_fn("DoB YYYY-MM-DD: "))
    count=int(input_fn("So mon: "))
    if count<0: raise ValueError("count")
    for _ in range(count): add_course(state,input_fn("Ma mon: "),input_fn("Ten mon: "))
    return state
def main():
    state=collect()
    while True:
        cmd=input("students/courses/marks/input/exit: ")
        if cmd=="exit": return
        if cmd=="students": print(list_students(state))
        elif cmd=="courses": print(list_courses(state))
        elif cmd=="marks": print(course_marks(state,input("Ma mon: ")))
        elif cmd=="input":
            cid=input("Ma mon: ")
            for sid in state["students"]: set_mark(state,cid,sid,float(input(sid+": ")))
if __name__=="__main__": main()
