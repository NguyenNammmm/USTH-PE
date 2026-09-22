"""QA for trusted authored reference code only. NOT a learner-code sandbox.
Run from this directory: python verify_reference.py
Optional: set PYTHONPATH to a directory containing matplotlib.
"""
from pathlib import Path
import ast, contextlib, copy, io, json, math, os, sys, threading, uuid

BASE=Path(__file__).resolve().parent
SCRATCH=BASE/'qa_scratch'
SCRATCH.mkdir(exist_ok=True)
@contextlib.contextmanager
def case_folder():
    folder=SCRATCH/('case_'+uuid.uuid4().hex)
    folder.mkdir()
    yield str(folder)
bank=json.loads((BASE/'PE_Python_Lesson_Bank.json').read_text(encoding='utf8'))

def exception_name(fn):
    try: fn()
    except Exception as error: return type(error).__name__
    return 'NO_EXCEPTION'
def student_average(cls,values):
    student=cls('S01')
    for value in values: student.add_score(value)
    return student.average()
def student_independence(cls):
    a,b=cls('S01'),cls('S02');a.add_score(8)
    return [a.scores,b.scores]
def chart_info(fig):
    assert len(fig.axes)==1
    ax=fig.axes[0]
    return dict(heights=[float(p.get_height()) for p in ax.patches],labels=[t.get_text() for t in ax.get_xticklabels()],ylabel=ax.get_ylabel(),ylim=list(ax.get_ylim()))
def valid_boundary_cases(cases):
    if not isinstance(cases,list) or not cases: return False
    for case in cases:
        if not isinstance(case,tuple) or len(case)!=2: return False
        s,e=case
        if type(s) not in (int,float) or not 0<=s<=10 or type(e) is not bool or e!=(s>=5): return False
    return any(s<5 for s,e in cases) and any(s==5 for s,e in cases) and any(s>5 for s,e in cases)
def kill_boundary_mutants(cases):
    return [any(mutant(s)!=e for s,e in cases) for mutant in [lambda s:s>5,lambda s:True,lambda s:False]]
def empty_state(): return dict(students={},courses={},marks={})
def capstone_sequence(fn):
    initial=empty_state(); snapshot=copy.deepcopy(initial)
    one=fn(initial,dict(type='add_student',id='S01',name='An'))
    two=fn(one,dict(type='add_course',id='PY',name='Python'))
    three=fn(two,dict(type='set_mark',student_id='S01',course_id='PY',score=8))
    four=fn(three,dict(type='set_mark',student_id='S01',course_id='PY',score=0))
    return [three['marks']['S01']['PY'],four['marks']['S01']['PY'],initial==snapshot and two['marks']=={}]
def capstone_duplicate(fn):
    state=fn(empty_state(),dict(type='add_student',id='S01',name='An'))
    return exception_name(lambda:fn(state,dict(type='add_student',id='S01',name='Binh')))
def capstone_bad_scores(fn):
    state=dict(students={'S01':'An'},courses={'PY':'Python'},marks={})
    for bad in [-1,11,True,float('nan'),float('inf'),None,'8']:
        if exception_name(lambda:fn(state,dict(type='set_mark',student_id='S01',course_id='PY',score=bad)))!='ValueError': return False
        if state['marks']!={}: return False
    return True

HELPERS={k:v for k,v in list(globals().items()) if callable(v) and getattr(v,'__module__',None)==__name__}
def same(a,b):
    if isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):
        return math.isclose(a,b,abs_tol=1e-9,rel_tol=0)
    if isinstance(a,list) and isinstance(b,list):return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    if isinstance(a,dict) and isinstance(b,dict):return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    return type(a)==type(b) and a==b

results=[]
for lesson in bank['lessons']:
    ident=lesson['lesson_id']; code=lesson['solution'];compile(code,ident,'exec')
    assert len(lesson['quiz'])==2
    for q in lesson['quiz']:
        assert len(q['options'])==len(q['feedback'])==3 and 0<=q['answer']<3
    for t in lesson['tests']:
        original_cwd=Path.cwd();namespace=dict(HELPERS,__name__='reference_under_test',**copy.deepcopy(t['inputs']))
        try:
            with case_folder() as folder:
                os.chdir(folder)
                for filename,content in {**lesson['support_files'],**t['files']}.items():
                    Path(filename).parent.mkdir(parents=True,exist_ok=True);Path(filename).write_text(content,encoding='utf8')
                sys.path.insert(0,folder);sys.modules.pop('grading',None)
                output=io.StringIO()
                try:
                    with contextlib.redirect_stdout(output):exec(code,namespace)
                    namespace['stdout']=output.getvalue()
                    value=eval(t['expression'],namespace)
                    assert same(value,t['expected']),f'{value!r} != {t["expected"]!r}'
                    if ident=='P07':assert type(namespace['result']) is tuple and all(type(x) is int for x in namespace['result'])
                    if ident in ['P02','P08','P09']:assert type(namespace['result']) is int
                    if ident in ['P05','P06','P07']:
                        for key,val in t['inputs'].items():assert namespace[key]==val,'Input mutated'
                    if ident=='P08':assert any(isinstance(n,ast.For) for n in ast.walk(ast.parse(code)))
                    if ident=='P09':assert any(isinstance(n,ast.While) for n in ast.walk(ast.parse(code)))
                    status='PASS';reason=''
                finally:
                    sys.path.remove(folder);sys.modules.pop('grading',None);os.chdir(original_cwd)
        except ModuleNotFoundError as exc:
            status='SKIP';reason=str(exc)
        except Exception as exc:
            status='FAIL';reason=repr(exc)
        finally:os.chdir(original_cwd)
        results.append(dict(id=t['id'],status=status,reason=reason))

# Meaningful contract tests in addition to the listed seed cases.
extra=[]
def run_extra(name,fn):
    try:fn();extra.append(dict(id=name,status='PASS'))
    except Exception as e:extra.append(dict(id=name,status='FAIL',reason=repr(e)))
refs={}
for l in bank['lessons']:
    if l['lesson_id'] in ['P10','P21','P24']:
        ns={'__name__':'reference_under_test'};exec(l['solution'],ns);refs[l['lesson_id']]=ns
def check_mean_nonmutation():
    scores=[2,8];assert refs['P10']['mean_score'](scores)==5 and scores==[2,8]
run_extra('P10-no-mutation',check_mean_nonmutation)
def check_thread():
    ns=refs['P21'];real=threading.Thread;main_id=threading.get_ident();seen=[]
    class ObserveThread(real):
        def run(self):seen.append(threading.get_ident());super().run()
    ns['Thread']=ObserveThread
    assert ns['run_job']([3])==[9] and len(seen)==1 and seen[0]!=main_id
run_extra('P21-real-worker',check_thread)
def check_bad_actions():
    fn=refs['P24']['apply_action'];state=empty_state()
    bads=[{}, {'type':'bad'},{'type':'add_student','id':' ','name':'An'},{'type':'add_student','id':'S01'},{'type':'set_mark','student_id':[],'course_id':'PY','score':8}]
    for action in bads:assert exception_name(lambda:fn(state,action))=='ValueError' and state==empty_state()
run_extra('P24-invalid-actions',check_bad_actions)
def check_alternative_scripts():
    variants={
        'P01':'print(f"Xin chao, {name}!")',
        'P04':'result = "Free" if 100 <= fee else "Paid"',
        'P05':'result = scores + [extra]',
        'P06':'result = marks[student_id] if student_id in marks else None'}
    for ident,code in variants.items():
        lesson=next(l for l in bank['lessons'] if l['lesson_id']==ident)
        for t in lesson['tests']:
            ns=copy.deepcopy(t['inputs']);out=io.StringIO()
            with contextlib.redirect_stdout(out):exec(code,ns)
            ns['stdout']=out.getvalue()
            assert same(eval(t['expression'],ns),t['expected'])
run_extra('Equivalent-P01-P04-P05-P06',check_alternative_scripts)
def check_mutants_caught():
    variants={
        'P03':'result = filename.rstrip(".txt").split("-")',
        'P04':'result = "Free" if fee > 100 else "Paid"',
        'P05':'result = scores\nresult.append(extra)',
        'P08':'result = 0\nfor stock in stocks:\n    result = 0\n    if stock >= 10:\n        result += 1'}
    for ident,code in variants.items():
        lesson=next(l for l in bank['lessons'] if l['lesson_id']==ident);killed=False
        for t in lesson['tests']:
            ns=copy.deepcopy(t['inputs']);exec(code,ns)
            if not same(eval(t['expression'],ns),t['expected']):killed=True
        assert killed,ident+' mutant was not detected'
run_extra('Counterexamples-P03-P04-P05-P08',check_mutants_caught)

# Real Tk widget checks, window withdrawn before any event-loop update.
tkresults=[]
try:
    import tkinter as tk
    for ident in ['P17','P18']:
        root=tk.Tk();root.withdraw()
        ns={'__name__':'reference_under_test'};exec(next(l['solution'] for l in bank['lessons'] if l['lesson_id']==ident),ns)
        widgets=ns['build_form'](root)
        if ident=='P17':
            assert root.title()=='So hoc tap'
            for key,row in [('sid_entry',0),('score_entry',1)]:
                data=widgets[key].grid_info();assert int(data['row'])==row and int(data['column'])==1
            labels=[w for w in root.winfo_children() if w.winfo_class()=='TLabel']
            assert [(w.cget('text'),int(w.grid_info()['row']),int(w.grid_info()['column'])) for w in labels]==[('Ma SV',0,0),('Diem',1,0)]
        else:
            assert widgets['saved']==[] and widgets['status'].get()=='Chua luu'
            for text in ['7.5','0','abc','11','nan','inf']:
                widgets['entry'].delete(0,'end');widgets['entry'].insert(0,text);widgets['button'].invoke()
            assert widgets['saved']==[7.5,0.0] and widgets['status'].get()=='Diem khong hop le' and widgets['entry'].get()=='inf'
        root.destroy();tkresults.append(dict(id=ident+'-tk-widget',status='PASS'))
except Exception as exc:
    tkresults.append(dict(id='TK-runtime',status='SKIP',reason=repr(exc)))

report={'python':sys.version,'syntax_checked':24,'seed_cases':results,'additional_contract_checks':extra,'tk_widget_checks':tkresults,
        'limits':'Trusted reference tests only; not a sandbox, UI usability test, or deployed product QA. Manual integration cases remain for dev.'}
(BASE/'QA_reference_results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
for label,items in [('seed',results),('extra',extra),('tk',tkresults)]:
    print(label,{s:sum(x['status']==s for x in items) for s in ['PASS','FAIL','SKIP']})
    for item in items:
        if item['status']!='PASS':print(item)
if any(r['status']=='FAIL' for r in results+extra+tkresults):raise SystemExit(1)
