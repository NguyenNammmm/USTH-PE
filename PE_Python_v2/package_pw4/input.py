from domains import Registry,Student,Course
def collect(ask=input):
    registry=Registry()
    n=int(ask("So sinh vien: "))
    if n<0: raise ValueError("count")
    for _ in range(n): registry.add_student(Student.input(ask))
    n=int(ask("So mon: "))
    if n<0: raise ValueError("count")
    for _ in range(n): registry.add_course(Course.input(ask))
    return registry
def marks(registry,ask=input):
    cid=ask("Ma mon: ")
    for sid in registry.students: registry.set_mark(sid,cid,float(ask(sid+": ")))
