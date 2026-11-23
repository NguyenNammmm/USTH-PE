"""Verify authored advanced labs on real task-local MySQL. No learner runner here."""
from pathlib import Path
import concurrent.futures as futures,hashlib,json,sys,time
from decimal import Decimal
ROOT=Path(__file__).resolve().parents[1];WORK=ROOT.parents[1]
sys.path.insert(0,str(WORK/'tmp/database-advanced-vendor'))
import pymysql
checks=[];observations={};created=[]
def conn(schema=True):
 return pymysql.connect(host='127.0.0.1',port=33374,user='root',database='pe_advanced_core' if schema else None,autocommit=True,charset='utf8mb4',connect_timeout=5,read_timeout=8,write_timeout=8)
def sql(c,text,args=None):
 with c.cursor() as cur:cur.execute(text,args);return cur.fetchall()
def check(name,actual,expected=None,ok=None,detail=''):
 passed=actual==expected if ok is None else bool(ok)
 checks.append({'name':name,'passed':passed,'actual':actual,'expected':expected,'detail':detail})
 if not passed:raise AssertionError(name+': '+repr(actual)+' expected '+repr(expected))
def error(c,text,code):
 try:sql(c,text)
 except pymysql.MySQLError as ex:check(text+' error',ex.args[0],code);return
 raise AssertionError('Expected error '+str(code)+' for '+text)
def reset_rows():
 with conn() as c:
  sql(c,'UPDATE accounts SET balance=100');sql(c,'UPDATE on_call SET active=1')
def fresh_pair(level):
 a=conn();b=conn();created.extend([a,b])
 for c in [a,b]:sql(c,'SET SESSION TRANSACTION ISOLATION LEVEL '+level);sql(c,'SET SESSION innodb_lock_wait_timeout=3');sql(c,'START TRANSACTION')
 return a,b
def close_pair(*cs):
 for c in cs:
  if c.open:
   c.rollback();c.close()
def until_waiting(observer,thread_id):
 deadline=time.monotonic()+4
 while time.monotonic()<deadline:
  result=sql(observer,'SELECT COUNT(*) FROM performance_schema.data_lock_waits w JOIN performance_schema.threads t ON t.THREAD_ID=w.REQUESTING_THREAD_ID WHERE t.PROCESSLIST_ID=%s',(thread_id,))
  if result[0][0]:return True
  time.sleep(.01)
 return False
def default(x):
 if isinstance(x,Decimal):return str(x)
 raise TypeError(type(x).__name__)
def main():
 with conn(False) as admin:
  observations['engine']=sql(admin,'SELECT VERSION(),@@sql_mode,@@transaction_isolation,@@innodb_rollback_on_timeout')
  fixture=(ROOT/'fixtures/advanced_core.sql').read_text(encoding='utf-8')
  for _ in range(2):
   # Authored fixture contains no procedures, delimiters or semicolons inside strings.
   for statement in fixture.split(';'):
    if statement.strip():sql(admin,statement)
  check('fixture reset twice',sql(admin,'SELECT COUNT(*) FROM pe_advanced_core.purchases'),((4,),))
 with conn() as c:
  wrong=sql(c,'SELECT SUM(l.amount),SUM(p.amount) FROM purchases o JOIN purchase_lines l ON l.order_id=o.id JOIN payments p ON p.order_id=o.id')
  correct=sql(c,'WITH l AS(SELECT order_id,SUM(amount) total FROM purchase_lines GROUP BY order_id),p AS(SELECT order_id,SUM(amount) total FROM payments GROUP BY order_id) SELECT SUM(l.total),SUM(p.total) FROM purchases o LEFT JOIN l ON o.id=l.order_id LEFT JOIN p ON o.id=p.order_id WHERE o.status=\'paid\'')
  check('fanout exposes wrong report',wrong,((Decimal('250'),Decimal('250')),))
  check('aggregate each grain before join',correct,((Decimal('150'),Decimal('150')),))
  check('bag projection keeps duplicates',sql(c,'SELECT customer_id FROM purchases ORDER BY id'),((1,),(1,),(2,),(3,)))
  check('ROWS with explicit tie breaker',sql(c,'SELECT id,SUM(value) OVER(ORDER BY day_no,id ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM metrics ORDER BY day_no,id'),((1,10),(2,30),(3,35),(4,42)))
  check('RANGE includes peer group',sql(c,'SELECT id,SUM(value) OVER(ORDER BY day_no RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) FROM metrics ORDER BY day_no,id'),((1,30),(2,30),(3,35),(4,42)))
  check('window population before output filtering',sql(c,'WITH numbered AS(SELECT id,value,ROW_NUMBER() OVER(ORDER BY value DESC,id) rn FROM metrics) SELECT id,value FROM numbered WHERE rn<=2 ORDER BY rn'),((2,20),(1,10)))
 # Two levels, two fresh sessions, one observed statement order.
 for level,new_value in [('REPEATABLE READ',100),('READ COMMITTED',120)]:
  reset_rows();a,b=fresh_pair(level)
  try:
   check(level+' first snapshot',sql(a,'SELECT balance FROM accounts WHERE id=1'),((100,),))
   sql(b,'UPDATE accounts SET balance=120 WHERE id=1');b.commit()
   check(level+' second plain read',sql(a,'SELECT balance FROM accounts WHERE id=1'),((new_value,),))
   check(level+' locking current read',sql(a,'SELECT balance FROM accounts WHERE id=1 FOR UPDATE'),((120,),))
  finally:close_pair(a,b)
 reset_rows();a,b=fresh_pair('REPEATABLE READ')
 try:
  av=sql(a,'SELECT balance FROM accounts WHERE id=1')[0][0];bv=sql(b,'SELECT balance FROM accounts WHERE id=1')[0][0]
  sql(a,'UPDATE accounts SET balance=%s WHERE id=1',(av+10,));a.commit()
  sql(b,'UPDATE accounts SET balance=%s WHERE id=1',(bv+20,));b.commit()
  with conn() as c:check('stale absolute writes lose update under this schedule',sql(c,'SELECT balance FROM accounts WHERE id=1'),((120,),))
 finally:close_pair(a,b)
 reset_rows();a,b=fresh_pair('REPEATABLE READ')
 try:
  sql(a,'UPDATE accounts SET balance=balance+10 WHERE id=1');a.commit()
  sql(b,'UPDATE accounts SET balance=balance+20 WHERE id=1');b.commit()
  with conn() as c:check('atomic relative writes preserve both additions',sql(c,'SELECT balance FROM accounts WHERE id=1'),((130,),))
 finally:close_pair(a,b)
 reset_rows();a,b=fresh_pair('REPEATABLE READ')
 try:
  check('A reads on-call invariant',sql(a,'SELECT SUM(active) FROM on_call'),((2,),))
  check('B reads same on-call snapshot',sql(b,'SELECT SUM(active) FROM on_call'),((2,),))
  sql(a,'UPDATE on_call SET active=0 WHERE id=1');sql(b,'UPDATE on_call SET active=0 WHERE id=2');a.commit();b.commit()
  with conn() as c:check('write skew violates cross-row invariant',sql(c,'SELECT SUM(active) FROM on_call'),((0,),))
 finally:close_pair(a,b)
 a,b=fresh_pair('READ COMMITTED')
 try:
  check('A leases first job',sql(a,"SELECT id FROM jobs WHERE state='ready' ORDER BY id LIMIT 1 FOR UPDATE"),((1,),))
  error(b,'SELECT id FROM jobs WHERE id=1 FOR UPDATE NOWAIT',3572)
  check('SKIP LOCKED selects different available job',sql(b,"SELECT id FROM jobs WHERE state='ready' ORDER BY id LIMIT 1 FOR UPDATE SKIP LOCKED"),((2,),))
 finally:close_pair(a,b)
 # Wait readiness comes from the engine lock table, not a fixed SLEEP guessed schedule.
 reset_rows();a,b=fresh_pair('REPEATABLE READ');observer=conn();pool=futures.ThreadPoolExecutor(max_workers=1)
 try:
  sql(a,'UPDATE accounts SET balance=balance+1 WHERE id=1');sql(b,'UPDATE accounts SET balance=balance+2 WHERE id=2')
  blocked=pool.submit(sql,a,'UPDATE accounts SET balance=balance+1 WHERE id=2')
  check('engine confirms A waiting for B',until_waiting(observer,a.thread_id()),True)
  outcomes=[]
  try:sql(b,'UPDATE accounts SET balance=balance+2 WHERE id=1');outcomes.append('B-statement-ok')
  except pymysql.MySQLError as ex:outcomes.append(('B',ex.args[0]));b.rollback()
  # A can be victim or survivor. Release B when it is still active so A cannot hang.
  if b.open:b.rollback()
  try:blocked.result(timeout=5);outcomes.append('A-statement-ok')
  except pymysql.MySQLError as ex:outcomes.append(('A',ex.args[0]));a.rollback()
  victims=[x for x in outcomes if isinstance(x,tuple) and x[1]==1213]
  check('deadlock chooses exactly one victim',len(victims),1,detail='Victim identity deliberately not pinned; whole transaction rolled back by engine.')
  observations['deadlockOutcomes']=outcomes
 finally:
  close_pair(a,b);observer.close();pool.shutdown(wait=True,cancel_futures=True)
 # Timeout rolls back current statement by default, unlike the complete deadlock transaction.
 reset_rows();a,b=fresh_pair('READ COMMITTED')
 try:
  sql(a,'UPDATE accounts SET balance=balance+1 WHERE id=1');sql(b,'UPDATE accounts SET balance=balance+2 WHERE id=2');sql(b,'SET SESSION innodb_lock_wait_timeout=1')
  error(b,'UPDATE accounts SET balance=balance+2 WHERE id=1',1205);b.commit();a.rollback()
  with conn() as c:check('earlier B statement survives default lock timeout',sql(c,'SELECT id,balance FROM accounts ORDER BY id'),((1,100),(2,102)))
 finally:close_pair(a,b)
 reset_rows()
 with conn() as c:
  sql(c,'START TRANSACTION');sql(c,'UPDATE accounts SET balance=101 WHERE id=1');sql(c,'CREATE TABLE ddl_probe(id INT PRIMARY KEY)');c.rollback()
  check('DDL implicit commit persists previous DML',sql(c,'SELECT balance FROM accounts WHERE id=1'),((101,),))
  check('DDL object persists rollback',sql(c,"SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='pe_advanced_core' AND table_name='ddl_probe'"),((1,),))
  sql(c,'DROP TABLE ddl_probe');sql(c,'UPDATE accounts SET balance=100')
  with c.cursor() as cur:cur.executemany('INSERT INTO plan_orders(id,customer_id,status,amount,payload) VALUES(%s,%s,%s,%s,%s)',[(i,i%1000,'paid' if i%10 else 'pending',i%100+1,'x'*80) for i in range(1,20001)])
  check('plan fixture population',sql(c,'SELECT COUNT(*) FROM plan_orders'),((20000,),))
  target='SELECT COUNT(*) FROM plan_orders WHERE customer_id=777 AND status=\'paid\''
  plain=sql(c,target);before=sql(c,'EXPLAIN ANALYZE '+target)
  sql(c,'CREATE INDEX ix_customer_status ON plan_orders(customer_id,status)');sql(c,'ANALYZE TABLE plan_orders')
  after=sql(c,'EXPLAIN ANALYZE '+target)
  check('index does not change result',sql(c,target),plain)
  check('selectivity chosen yields twenty qualifying rows',plain,((20,),))
  check('before plan actually executed',any('actual time=' in str(row[0]) for row in before),True)
  check('after plan actually executed',any('actual time=' in str(row[0]) for row in after),True)
  observations['plan']={'rows':20000,'before':[x[0] for x in before],'after':[x[0] for x in after],'result':plain,'scope':'One authored workload, observed plans. Timings are not promised speedups or universal index selection.'}
 finally_cleanup()
 result={'date':'2026-11-05','status':'pass','engine':observations.get('engine'),'fixtureSha256':hashlib.sha256((ROOT/'fixtures/advanced_core.sql').read_bytes()).hexdigest(),'checks':checks,'observations':observations,'scope':'Authored advanced lab subsets, real MySQL8.4.13; not allcourseSQL or webbackend. No Pgengine claimed.','limitations':['Real concurrency test validates these controlled schedules only.','No crash injected into native engine. Recovery activities need separately labeled model or disposableserver.','This verifier is instructor tooling, not an untrusted-code sandbox or learner install requirement.']}
 (ROOT/'qa/mysql-advanced-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=default),encoding='utf-8');print(json.dumps({'checks':len(checks),'passed':sum(x['passed'] for x in checks),'engine':observations['engine']},ensure_ascii=False))
def finally_cleanup():
 for c in created:
  if c.open:
   try:c.rollback();c.close()
   except Exception:pass
if __name__=='__main__':
 try:main()
 finally:finally_cleanup()
