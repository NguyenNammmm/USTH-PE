"""Additional end-to-end checks for trusted handoff reference code."""
import os,sys,json,time,traceback,importlib.util,subprocess,threading,socket,contextlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
BASE=HERE if (HERE/'lesson_bank.json').exists() else HERE.parents[2]/'output/pdf/PE_Python_v2'
if os.environ.get('PE_QA_DEPS'): sys.path.insert(0,os.environ['PE_QA_DEPS'])
results=[]
def check(name,fn):
    try:
        detail=fn(); results.append(dict(name=name,status='PASS',detail=detail))
    except Exception:
        results.append(dict(name=name,status='FAIL',error=traceback.format_exc()))
    print(results[-1]['name'],results[-1]['status'])
def load(ident):
    path=BASE/'answers'/ident/'reference.py'
    spec=importlib.util.spec_from_file_location('answer_'+ident,path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module);return module

def sas():
    import pandas as pd
    a=load('A16'); actual=a.read_science(BASE/'fixtures/test1.sas7bdat','sas7bdat')
    expected=pd.read_csv(BASE/'fixtures/test_sas7bdat_1.csv')
    for c in ['Column4','Column12']: expected[c]=pd.Timestamp('1960-01-01')+pd.to_timedelta(expected[c],unit='D')
    pd.testing.assert_frame_equal(actual,expected,check_dtype=False)
    return dict(shape=list(actual.shape),columns=list(actual.columns))
check('SAS7BDAT actual format',sas)

def network():
    from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
    from urllib.error import HTTPError
    a=load('A13')
    with socket.socket() as server:
        server.bind(('127.0.0.1',0));server.listen(1);port=server.getsockname()[1]
        def serve_tcp():
            conn,_=server.accept()
            with conn,conn.makefile('rb') as stream:
                assert stream.readline()==b'An\n'
                for part in [b'A',b'N',b'\n']:conn.sendall(part)
        worker=threading.Thread(target=serve_tcp);worker.start()
        assert a.tcp_line('127.0.0.1',port,'An')=='AN';worker.join(2);assert not worker.is_alive()
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path=='/missing':self.send_error(404);return
            self.send_response(200);self.end_headers();self.wfile.write(b'X'*4097 if self.path=='/large' else 'PE tiếng Việt'.encode())
        def log_message(self,*args):pass
    server=ThreadingHTTPServer(('127.0.0.1',0),Handler);thread=threading.Thread(target=server.serve_forever);thread.start()
    try:
        url='http://127.0.0.1:'+str(server.server_port)
        assert a.fetch_text(url+'/ok')=='PE tiếng Việt'
        try:a.fetch_text(url+'/missing')
        except HTTPError as e:assert e.code==404
        else:raise AssertionError('HTTP error missing')
        try:a.fetch_text(url+'/large')
        except ValueError:pass
        else:raise AssertionError('body limit absent')
    finally:server.shutdown();server.server_close();thread.join(2)
    return 'TCP framing across chunks; HTTP UTF-8/404/body size; loopback only. Timeout UI protocol remains manual.'
check('Loopback TCP and HTTP',network)

def capstone():
    import tkinter as tk
    folder=BASE/'capstone_pw9';sys.path.insert(0,str(folder))
    spec=importlib.util.spec_from_file_location('capstone_main',folder/'main.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    scratch=BASE/'qa_scratch/capstone';scratch.mkdir(parents=True,exist_ok=True)
    import uuid
    path=scratch/(uuid.uuid4().hex+'.dat')
    root=tk.Tk();root.withdraw()
    def fill(entries,values):
        for entry,value in zip(entries,values):entry.delete(0,'end');entry.insert(0,value)
    try:
        app=m.App(root,path)
        fill(app.student_entries,['A','An','2005-01-02']);app.add_student()
        fill(app.student_entries,['B','An','2005-02-03']);app.add_student()
        fill(app.course_entries,['PY','Python','3']);app.add_course()
        fill(app.course_entries,['DB','Database','1']);app.add_course()
        for sid,cid,value in [('A','PY','8.79'),('A','DB','6.29'),('B','PY','9.09')]:
            app.sid.set(sid);app.cid.set(cid);app.score.delete(0,'end');app.score.insert(0,value);app.set_mark()
        assert app.registry.ranking()==[('B',9.0),('A',8.075)]
        app.score.delete(0,'end');app.score.insert(0,'nan');app.set_mark();assert app.registry.marks['B','PY']==9.0
        app.save();assert app.busy and app.save_button.instate(['disabled'])
        deadline=time.monotonic()+5
        while app.busy and time.monotonic()<deadline:root.update();time.sleep(.01)
        assert not app.busy and not app.dirty and path.exists()
    finally:root.destroy()
    root=tk.Tk();root.withdraw()
    try:
        again=m.App(root,path);assert again.registry.ranking()==[('B',9.0),('A',8.075)]
        assert again.registry.students['A'].dob=='2005-01-02'
    finally:root.destroy()
    env=os.environ.copy();env['PYTHONPATH']=os.pathsep.join([str(folder),os.environ.get('PE_QA_DEPS','')])
    process=subprocess.run([sys.executable,'-c','from persistence import load_pickle; import sys; r=load_pickle(sys.argv[1]); print(r.students["A"].dob); print(r.ranking())',str(path)],env=env,capture_output=True,text=True,timeout=10)
    assert process.returncode==0,process.stderr
    assert '2005-01-02' in process.stdout and '8.075' in process.stdout
    return 'Native Tk callbacks, validation, background save, UI lock, reopen and separate-process unpickle passed.'
check('PW9 integrated journey',capstone)

def mysql_mock():
    from unittest.mock import Mock
    a=load('A19');connection=Mock();cursor=connection.cursor.return_value;cursor.rowcount=1
    repository=a.Students(connection);assert repository.add('S01',"O'Neil",'2005-01-02')==1
    sql,params=cursor.execute.call_args.args;assert '%s' in sql and "O'Neil" not in sql and params[1]=="O'Neil"
    cursor.execute.side_effect=RuntimeError('DB unavailable')
    try:repository.rename('S01','An')
    except RuntimeError:pass
    else:raise AssertionError('hidden failure')
    connection.rollback.assert_called_once();assert cursor.close.call_count==2
    return 'Parameter binding and rollback/close unit tests only; MySQL server integration NOT_RUN.'
check('MySQL repository contract mock',mysql_mock)

def compile_all():
    paths=list((BASE/'answers').rglob('*.py'))+list((BASE/'capstone_pw9').rglob('*.py'))+list((BASE/'package_pw4').rglob('*.py'))
    for path in paths:compile(path.read_text(encoding='utf8'),str(path),'exec')
    return len(paths)
check('All delivered Python source compiles',compile_all)
(BASE/'QA_extra_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
sys.exit(any(r['status']=='FAIL' for r in results))
