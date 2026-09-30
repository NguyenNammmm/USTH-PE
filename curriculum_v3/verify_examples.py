"""Verify authored examples; not a sandbox for learner submissions."""
from pathlib import Path
import sys,io,contextlib,threading,json
from unittest.mock import patch
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'examples'))
from palindrome_basic import is_palindrome
from language_base import ProgrammingLanguage
from inheritance_intermediate import C
from threads_advanced import C as ThreadC
from compression_beginner import compress_data,restore_data
results=[]
for text,wanted in [('level',True),('python',False),('',False),('a',True),('Level',False),(' a ',True)]:
    output=io.StringIO()
    with contextlib.redirect_stdout(output):actual=is_palindrome(text)
    assert actual is wanted and output.getvalue()==''
results.append('B09: palindrome boundaries and return without print PASS')
seed=['procedural'];a=ProgrammingLanguage('C',1972,seed);b=ProgrammingLanguage('Python',1991,seed)
a.add_paradigms('functional');assert b.paradigms==seed==['procedural']
c=C('C',1972,['procedural'],'C17')
assert isinstance(c,ProgrammingLanguage)
assert str(c)=="Language[C], Year created[1972], Paradigms['procedural'], Standard version[C17]"
output=io.StringIO()
with contextlib.redirect_stdout(output):assert c.compile() is None
assert output.getvalue()=='Compiling C code using standard version C17\n'
results.append('I12: inheritance, state, string and compile PASS')
for data in [b'',b'Hello',bytes(range(256))]:assert restore_data(compress_data(data))==data
results.append('A04 sample: exact byte round-trip PASS')
real_start=threading.Thread.start;real_join=threading.Thread.join
events=[];seen=[];lock=threading.Lock();barrier=threading.Barrier(3)
def record_start(worker):events.append('start');return real_start(worker)
def record_join(worker,*args,**kwargs):events.append('join');return real_join(worker,*args,**kwargs)
obj=ThreadC('C',1972,['procedural'],'C17')
def probe(n):
    barrier.wait(timeout=3)
    with lock:seen.append((threading.get_ident(),n))
obj._compile_worker=probe
with patch.object(threading.Thread,'start',record_start),patch.object(threading.Thread,'join',record_join):obj.parallel_compile(3)
assert events==['start']*3+['join']*3
assert len(seen)==3 and len({p[0] for p in seen})==3
assert all(p[0]!=threading.get_ident() and p[1]==3 for p in seen)
obj=ThreadC('C',1972,['procedural'],'C17')
output=io.StringIO()
with contextlib.redirect_stdout(output):obj.parallel_compile(1)
assert output.getvalue()=='Compiling C code using 1 threads with standard version C17\n'
for bad in [0,-1,True,1.5]:
    try:obj.parallel_compile(bad)
    except ValueError:pass
    else:raise AssertionError(bad)
results.append('N03: real worker overlap, start-before-join, complete-on-return, output and invalid n PASS')
(HERE/'QA_examples.json').write_text(json.dumps(dict(results=results,limits='Only delivered examples tested; 40-task blueprint is not a complete implemented bank. POSIX N05-N08 not implemented/tested here.'),ensure_ascii=False,indent=2),encoding='utf8')
print('\n'.join(results))
