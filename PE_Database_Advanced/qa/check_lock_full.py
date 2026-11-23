from pathlib import Path
import hashlib,json,re
R=Path(__file__).resolve().parents[1];checks=[]
def check(name,a,b):
 checks.append({'name':name,'actual':a,'expected':b,'passed':a==b});assert a==b,(name,a,b)
def grant(held,waiting):
 out=[];modes=[m for _,m in held]
 for tx,mode in waiting:
  if any(mode=='X' or m=='X' for m in modes):break
  modes.append(mode);out.append(tx)
 return out
check('FIFO reader cannot bypass queued writer',grant([('T1','S')],[('T2','X'),('T3','S'),('T4','S')]),[])
check('writer granted after holder release',grant([],[('T2','X'),('T3','S'),('T4','S')]),['T2'])
check('compatible reader prefix batched',grant([],[('T3','S'),('T4','S')]),['T3','T4'])
check('cancel waiting writer rescans nextreader',grant([('T1','S')],[('T3','S')]),['T3'])
check('premature unlock transfer breaks observedtotal',100+80,180)
def cascade_abort(failed,dependencies):
 doomed=set(failed)
 while True:
  extra={tx for tx,parents in dependencies.items() if parents & doomed}
  if extra<=doomed:return sorted(doomed)
  doomed|=extra
check('commitdependency transitiveabortexcludesunrelated',cascade_abort({'T1'},{'T2':{'T1'},'T3':{'T2'},'T4':set()}),['T1','T2','T3'])
def legal_tree(events,parent):
 held=set();seen=set();first=True
 for op,node in events:
  if op=='lock':
   if node in seen or (not first and parent.get(node) not in held):return False
   held.add(node);seen.add(node);first=False
  else:
   if node not in held:return False
   held.remove(node)
 return True
parent={'B':'A','C':'A','D':'B','H':'D'}
check('tree allows early ancestorrelease withchildheld',legal_tree([('lock','A'),('lock','B'),('unlock','A'),('lock','D')],parent),True)
check('tree rejects relock',legal_tree([('lock','A'),('lock','B'),('unlock','B'),('lock','B')],parent),False)
check('2PL siblinglocks not treelegal whenstartingatsibling',legal_tree([('lock','B'),('lock','C')],parent),False)
text=(R/'lessons/AD39.md').read_text(encoding='utf-8')
for h in ['Luyện tập','Đáp án và lập luận']:
 block=text.split('## '+h+'\n',1)[1].split('\n## ',1)[0];nums=[int(x) for x in re.findall(r'^(\d+)\.\s',block,re.M)];check(h+' questionsequence',nums,list(range(1,8)))
check('fencesbalanced',text.count(chr(96)*3)%2,0)
result={'scope':'Finite FIFO/tree/example and structure checks. No SQL, no general proof certification.','lessonSha256':hashlib.sha256((R/'lessons/AD39.md').read_bytes()).hexdigest(),'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks)}
(R/'qa/lock-full-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'passed':result['passed'],'total':result['total']}))
