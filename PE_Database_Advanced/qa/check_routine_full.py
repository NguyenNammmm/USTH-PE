"""New AD85 example/model checks. Native mode only creates a fresh random schema."""
from pathlib import Path
import hashlib,json,re,sys,uuid
R=Path(__file__).resolve().parents[1];W=R.parents[1]
text=(R/'lessons/AD85.md').read_text(encoding='utf-8-sig');checks=[]
def check(name,actual,expected):
 checks.append({'name':name,'actual':actual,'expected':expected,'passed':actual==expected})
 assert actual==expected,(name,actual,expected)
def sum_loop(n):
 i,total=1,0
 while i<=n:
  assert total==(i-1)*i//2
  total+=i;i+=1
 return total
for n in [0,1,3,20]:check('WHILE invariant and output n='+str(n),sum_loop(n),n*(n+1)//2)
def naive_repeat(n):
 i,total=1,0
 while True:
  total+=i;i+=1
  if i>n:return total
check('naive REPEAT computed counterexample n0',naive_repeat(0),1)
check('naive REPEAT still works on positive sample',naive_repeat(3),6)
def odds(n):
 i,total=1,0
 while i<=n:
  current=i;i+=1
  if current%2==0:continue
  total+=current
 return total
check('ITERATE-style skip increments control',odds(6),9)
student=[(1,'An','DA'),(2,'Binh','SE'),(3,'Chi','DA')]
check('table/scalar DA shape',[len([r for r in student if r[2]=='DA']),[r[0] for r in student if r[2]=='DA']],[2,[1,3]])
check('empty relation not oneNULLrow',[r for r in student if r[2]=='missing'],[])
contribution=lambda grade,credits: credits if grade is not None and grade!='F' else 0
check('grade transitions delta',[contribution(n,3)-contribution(o,3) for o,n in [(None,'A'),('A','B'),('B','F'),('F',None)]],[3,0,-3,0])
totals=[3,0];trace=[totals[:]]
totals[0]+=2;trace.append(totals[:]);totals[0]-=3;totals[1]+=3;trace.append(totals[:]);totals[0]-=2;trace.append(totals[:])
check('enrollment move/delete trace',trace,[[3,0],[5,0],[2,3],[0,3]])
check('statement transition grouped deltas',{'A':-sum([3,5]),'B':sum([3,5])},{'A':-8,'B':8})
check('snapshot replays derived contribution twice',6+6,12)
for heading in ['Luyện tập','Đáp án và lập luận']:
 block=text.split('## '+heading+'\n',1)[1].split('\n## ',1)[0]
 nums=[int(v) for v in re.findall(r'^(\d+)\.\s',block,re.M)]
 check(heading+' numbering',nums,list(range(1,10)))
check('balanced code fences',text.count(chr(96)*3)%2,0)
engine=None;schema=None
if '--mysql' in sys.argv:
 sys.path.insert(0,str(W/'tmp/database-advanced-vendor'))
 import pymysql
 schema='pe_advanced_routine_full_'+uuid.uuid4().hex[:10]
 conn=pymysql.connect(host='127.0.0.1',port=33374,user='root',charset='utf8mb4',autocommit=True)
 try:
  with conn.cursor() as c:
   c.execute('SELECT VERSION()');engine=c.fetchone()[0];assert engine.startswith('8.4.')
   c.execute('SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME=%s',(schema,));assert c.fetchone() is None
   c.execute('CREATE DATABASE `'+schema+'`');conn.select_db(schema)
   c.execute('CREATE FUNCTION ad85_line_points(p_qty INT,p_unit INT) RETURNS BIGINT DETERMINISTIC NO SQL RETURN CAST(p_qty AS SIGNED)*CAST(p_unit AS SIGNED)')
   c.execute('SELECT ad85_line_points(3,7),ad85_line_points(NULL,7),ad85_line_points(-2147483648,-2147483648)')
   check('actualMySQL scalarfunction normalNULLINTboundary',list(c.fetchone()),[21,None,4611686018427387904])
   c.execute("SELECT NULLIF('', ''),NULLIF('A', ''),NULLIF(NULL,'')")
   check('actualMySQL normalize expression',list(c.fetchone()),[None,'A',None])
 finally:conn.close()
result={'scope':'New AD85 finite examples/invariants and optional explicitly named nativechecks only. Does not rerun/certify every old routine/trigger.','engine':engine,'schemaCreatedFresh':schema,'schemaCleanup':'Retained task-local schema; no DROP issued','lessonSha256':hashlib.sha256((R/'lessons/AD85.md').read_bytes()).hexdigest(),'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks)}
(R/'qa/routine-full-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'passed':result['passed'],'total':result['total'],'engine':engine}))
