"""Trusted authored answers only. This is NOT a learner-code sandbox."""
import json,sys,os,uuid,traceback,contextlib,io,importlib,importlib.util
from pathlib import Path
BASE=Path(__file__).resolve().parent
if not (BASE/'lesson_bank.json').exists():
    BASE=BASE.parents[2]/'output/pdf/PE_Python_v2'
if os.environ.get('PE_QA_DEPS'): sys.path.insert(0,os.environ['PE_QA_DEPS'])
os.environ['MPLCONFIGDIR']=str(BASE/'qa_scratch/mpl_config')
bank=json.loads((BASE/'lesson_bank.json').read_text(encoding='utf8'))
answers=json.loads((BASE/'instructor_answers.json').read_text(encoding='utf8'))
criteria=json.loads((BASE/'test_criteria.json').read_text(encoding='utf8'))

def run(lesson):
    ident=lesson['lesson_id']; answer=answers[ident]; spec=criteria[ident]
    if ident.startswith('P'): return dict(lesson=ident,status='USE_LEGACY_RUNNER')
    reference=BASE/'answers'/ident/'reference.py'
    if reference.exists(): compile(reference.read_text(encoding='utf8'),str(reference),'exec')
    if answer['answer_kind']!='python':
        return dict(lesson=ident,status='MANUAL_REQUIRED',protocols=len(spec['checks']))
    for check in spec['checks']: compile(check['body'],check['id'],'exec')
    scratch=BASE/'qa_scratch'/uuid.uuid4().hex; scratch.mkdir(parents=True)
    previous=Path.cwd(); os.chdir(scratch); sys.path.insert(0,str(scratch))
    try:
        for source in (BASE/'answers'/ident).iterdir():
            if source.name not in ('reference.py','answer.md') and source.is_file():
                (scratch/source.name).write_bytes(source.read_bytes()); sys.modules.pop(source.stem,None)
        ns={'__name__':'trusted_reference'}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(answer['solution'],ns)
            for check in spec['checks']: exec(check['body'],ns)
        return dict(lesson=ident,status='PASS',checks=[c['id'] for c in spec['checks']],
                    manual_remaining=spec['manual_checks'])
    finally:
        os.chdir(previous);sys.path.remove(str(scratch))

if __name__=='__main__':
    results=[]
    for lesson in bank['lessons']:
        try: result=run(lesson)
        except (ModuleNotFoundError,ImportError) as error:
            result=dict(lesson=lesson['lesson_id'],status='ENVIRONMENT_NOT_RUN',error=str(error))
        except Exception:
            result=dict(lesson=lesson['lesson_id'],status='FAIL',error=traceback.format_exc())
        results.append(result)
        if result['status']=='FAIL': print(json.dumps(result,ensure_ascii=False))
    (BASE/'QA_new_results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
    from collections import Counter
    print(json.dumps(dict(Counter(r['status'] for r in results))))
    sys.exit(any(r['status']=='FAIL' for r in results))
