import importlib
reader=importlib.import_module("input")
from output import show_rows
def main():
    registry=reader.collect()
    while True:
        cmd=input("students/courses/input/marks/ranking/exit: ")
        if cmd=="exit": return
        try:
            if cmd=="students": show_rows([s.list() for s in registry.students.values()])
            elif cmd=="courses": show_rows([c.list() for c in registry.courses.values()])
            elif cmd=="input": reader.marks(registry)
            elif cmd=="marks": show_rows(registry.course_marks(input("Ma mon: ")))
            elif cmd=="ranking": show_rows(registry.ranking())
        except ValueError as error: print("Loi:",error)
if __name__=="__main__": main()
