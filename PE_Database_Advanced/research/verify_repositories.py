"""Selected-source quality checks. Only task-local DB schemas pa_repo_* are modified.
No claim that all upstream tests or all isolation schedules are verified.
"""
from pathlib import Path
import collections,concurrent.futures,contextlib,hashlib,importlib.util,json,random,sqlite3,subprocess,sys,time
from decimal import Decimal
HERE=Path(__file__).resolve().parent;WORK=HERE.parents[2];CLONES=WORK/'tmp/database-advanced-repos'
sys.path.insert(0,str(CLONES/'vendor'))
import pymysql
OUT=HERE/'repo-checks';OUT.mkdir(exist_ok=True)
checks=[]
def note(repo,label,actual,expected=None,passed=None,**extra):
 ok=actual==expected if passed is None else passed
 checks.append(dict(repo=repo,label=label,passed=bool(ok),actual=actual,expected=expected,**extra))
 if not ok:print('FAIL',repo,label,repr(actual),repr(expected))
def connect(schema=None):return pymysql.connect(host='127.0.0.1',port=33374,user='root',database=schema,charset='utf8mb4',autocommit=True,read_timeout=12,write_timeout=12)
def q(c,sql,args=None):
 with c.cursor() as cur:cur.execute(sql,args);return [list(x) for x in cur.fetchall()]
admin=connect();engine=q(admin,'SELECT VERSION(),@@sql_mode,@@transaction_isolation,@@default_storage_engine;')
note('runtime','MySQL8.4 actual version',engine,passed=engine[0][0].startswith('8.4.') and engine[0][3]=='InnoDB')

# Hermitage source: mysql.md G1a, PMP, P4. Keep two live connections and record outcomes.
DB='pa_repo_hermitage';q(admin,f'CREATE DATABASE IF NOT EXISTS `{DB}`')
a=connect(DB);b=connect(DB)
def reset():
 a.rollback();b.rollback();q(a,'DROP TABLE IF EXISTS test');q(a,'CREATE TABLE test(id INT PRIMARY KEY,value INT) ENGINE=InnoDB');q(a,'INSERT INTO test VALUES(1,10),(2,20)')
def begin(level):
 for c in [a,b]:q(c,'SET SESSION TRANSACTION ISOLATION LEVEL '+level);q(c,'SET SESSION innodb_lock_wait_timeout=8');c.begin()
try:
 for level,expected in [('READ UNCOMMITTED',101),('READ COMMITTED',10)]:
  reset();begin(level);q(a,'UPDATE test SET value=101 WHERE id=1');during=q(b,'SELECT value FROM test WHERE id=1')[0][0];a.rollback();after=q(b,'SELECT value FROM test WHERE id=1')[0][0];b.commit()
  note('hermitage','G1a '+level,{'during':during,'afterRollback':after},{'during':expected,'afterRollback':10})
 for level,expected in [('READ COMMITTED',11),('REPEATABLE READ',10)]:
  reset();begin(level);first=q(a,'SELECT value FROM test WHERE id=1')[0][0];q(b,'UPDATE test SET value=11 WHERE id=1');b.commit();second=q(a,'SELECT value FROM test WHERE id=1')[0][0];a.commit()
  note('hermitage','Snapshot repeat read '+level,[first,second],[10,expected])
 for level,expected in [('READ COMMITTED',1),('REPEATABLE READ',0)]:
  reset();begin(level);first=q(a,'SELECT id FROM test WHERE value=30');q(b,'INSERT INTO test VALUES(3,30)');b.commit();second=q(a,'SELECT id FROM test WHERE value=30');a.commit()
  note('hermitage','PMP read predicate '+level,[len(first),len(second)],[0,expected])
 for update,expected in [('UPDATE test SET value=11 WHERE id=1',11),('UPDATE test SET value=value+1 WHERE id=1',12)]:
  reset();begin('REPEATABLE READ');reads=[q(a,'SELECT value FROM test WHERE id=1')[0][0],q(b,'SELECT value FROM test WHERE id=1')[0][0]]
  q(a,update)
  with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
   future=pool.submit(q,b,update)
   # Observe a real lock-wait edge instead of assuming sleep means blocked.
   deadline=time.monotonic()+4;waits=0
   while time.monotonic()<deadline:
    waits=q(admin,'SELECT COUNT(*) FROM performance_schema.data_lock_waits w JOIN performance_schema.threads t ON t.THREAD_ID=w.REQUESTING_THREAD_ID WHERE t.PROCESSLIST_ID=%s',(b.thread_id(),))[0][0]
    if waits:break
    if future.done():break
    time.sleep(.02)
   a.commit();future.result(timeout=10);b.commit()
  value=q(a,'SELECT value FROM test WHERE id=1')[0][0]
  note('hermitage','P4 stale assignment' if expected==11 else 'PE repair atomic increment',{'reads':reads,'waitObserved':waits>0,'final':value},{'reads':[10,10],'waitObserved':True,'final':expected})
finally:a.rollback();b.rollback();a.close();b.close()

# Chinook single SQL script, inspected before execution. Only rename its DB to task schema.
src=CLONES/'chinook-database/ChinookDatabase/DataSources/Chinook_MySql.sql';original=src.read_text(encoding='utf-8-sig');sql=original.replace('`Chinook`','`pa_repo_chinook`')
assert sql.count('`pa_repo_chinook`')==3 and 'SOURCE ' not in sql and 'LOAD DATA' not in sql
mysql=WORK/'tmp/database-source/mysql-runtime/mysql-8.4.13-winx64/bin/mysql.exe'
args=[str(mysql),'--protocol=TCP','--host=127.0.0.1','--port=33374','--user=root','--default-character-set=utf8mb4']
loaded=subprocess.run(args,input=sql,capture_output=True,encoding='utf-8',timeout=60)
note('chinook','MySQL source script load',loaded.returncode,0,stderr=loaded.stderr.strip(),sourceSha256=hashlib.sha256(src.read_bytes()).hexdigest())
c=connect('pa_repo_chinook')
try:
 counts={t:q(c,'SELECT COUNT(*) FROM `'+t+'`')[0][0] for t in ['Artist','Album','Track','Customer','Invoice','InvoiceLine','PlaylistTrack']}
 note('chinook','Canonical subset row counts',counts,{'Artist':275,'Album':347,'Track':3503,'Customer':59,'Invoice':412,'InvoiceLine':2240,'PlaylistTrack':8715})
 orphan=q(c,'SELECT COUNT(*) FROM InvoiceLine l LEFT JOIN Invoice i ON i.InvoiceId=l.InvoiceId LEFT JOIN Track t ON t.TrackId=l.TrackId WHERE i.InvoiceId IS NULL OR t.TrackId IS NULL')[0][0]
 note('chinook','InvoiceLine invoice/track referential integrity',orphan,0)
 amount=q(c,'SELECT COUNT(*) FROM (SELECT i.InvoiceId FROM Invoice i JOIN InvoiceLine l USING(InvoiceId) GROUP BY i.InvoiceId,i.Total HAVING SUM(l.UnitPrice*l.Quantity)<>i.Total) bad')[0][0]
 note('chinook','Exact DECIMAL invoice reconciliation',amount,0)
 # Independent aggregation path: invoice totals vs invoice-line totals per customer.
 left=q(c,'SELECT CustomerId,CAST(SUM(Total) AS CHAR) FROM Invoice GROUP BY CustomerId ORDER BY CustomerId')
 right=q(c,'SELECT i.CustomerId,CAST(SUM(l.UnitPrice*l.Quantity) AS CHAR) FROM Invoice i JOIN InvoiceLine l USING(InvoiceId) GROUP BY i.CustomerId ORDER BY i.CustomerId')
 note('chinook','Independent aggregate routes preserve customer totals',left, right)
 # Default frame vs ROWS can differ on ties; using same full ordering removes ambiguity for this new lab.
 invoices=q(c,'SELECT InvoiceId,CustomerId,InvoiceDate,Total FROM Invoice ORDER BY CustomerId,InvoiceDate,InvoiceId')
 running=collections.defaultdict(int);oracle=[]
 for iid,cid,date,total in invoices:running[cid]+=total;oracle.append([iid,cid,str(running[cid])])
 window=q(c,'SELECT InvoiceId,CustomerId,SUM(Total) OVER (PARTITION BY CustomerId ORDER BY InvoiceDate,InvoiceId ROWS UNBOUNDED PRECEDING) r FROM Invoice ORDER BY CustomerId,InvoiceDate,InvoiceId')
 note('chinook','Running total window vs independent Python DECIMAL oracle',[[iid,cid,str(total)] for iid,cid,total in window],oracle)
finally:c.close()

# E-commerce selected query: independent oracle against tiny adversarial rows.
sys.path.insert(0,str(CLONES/'ecommerce-query-optimizer-demo/src'))
import queries
small=[(1,'High boundary',3,500.0,4.0),(2,'Other category',4,100.0,5.0),(3,'Low rating',3,100.0,3.9),(4,'Too cheap',3,49.99,5.0),(5,'Low boundary',3,50.0,4.0),(6,'Too dear',3,500.01,5.0)]
s=sqlite3.connect(':memory:');s.execute('CREATE TABLE products(id INTEGER PRIMARY KEY,name TEXT,category_id INT,price REAL,rating REAL)');s.executemany('INSERT INTO products VALUES(?,?,?,?,?)',small)
actual=queries.filter_products(s,3,50.0,500.0,4.0)
note('ecommerce','Boundary/category/rating independent oracle',actual,[(5,'Low boundary',50.0,4.0),(1,'High boundary',500.0,4.0)])
note('ecommerce','Empty category actually empty',queries.filter_products(s,99,50,500,4),[])
mutants={'dropCategory':queries.FILTER_PRODUCTS.replace('category_id = ?','? IS NOT NULL'),'dropRating':queries.FILTER_PRODUCTS.replace('rating >= ?','? IS NOT NULL'),'emptyAlways':'SELECT id,name,price,rating FROM products WHERE 0 AND ? AND ? AND ? AND ?'}
expected=actual;killed=[]
for name,query in mutants.items():
 result=s.execute(query,(3,50,500,4)).fetchall();killed.append(name) if result!=expected else None
note('ecommerce','Independent fixture kills3 wrong query behaviors',sorted(killed),sorted(mutants))
s.close()

# MySQL adaptation of equality + range + ORDER BY. Tie breaker deliberately added.
q(admin,'CREATE DATABASE IF NOT EXISTS pa_repo_index');c=connect('pa_repo_index')
try:
 q(c,'DROP TABLE IF EXISTS products');q(c,'CREATE TABLE products(id INT PRIMARY KEY,name VARCHAR(80),category_id INT,price DECIMAL(10,2),rating DECIMAL(3,1),stock INT) ENGINE=InnoDB')
 rng=random.Random(20261105);rows=[(i,'Product '+str(i),rng.randint(1,20),str(rng.randint(500,200000)/100),str(rng.randint(10,50)/10),rng.randint(0,100)) for i in range(1,10001)]
 with c.cursor() as cur:cur.executemany('INSERT INTO products VALUES(%s,%s,%s,%s,%s,%s)',rows)
 query='SELECT id,name,price,rating FROM products WHERE category_id=%s AND price BETWEEN %s AND %s AND rating>=%s ORDER BY price,id LIMIT 20';params=(3,50,500,4)
 before=q(c,query,params);plan_before=q(c,'EXPLAIN '+query,params)
 oracle_ids=[r[0] for r in sorted((r for r in rows if r[2]==3 and Decimal('50')<=Decimal(r[3])<=Decimal('500') and Decimal(r[4])>=4),key=lambda r:(Decimal(r[3]),r[0]))[:20]]
 note('ecommerce','MySQL filter vs independent Python predicate/order oracle',[r[0] for r in before],oracle_ids)
 q(c,'CREATE INDEX idx_products_cat_price_rating ON products(category_id,price,rating)');q(c,'ANALYZE TABLE products')
 after=q(c,query,params);plan_after=q(c,'EXPLAIN '+query,params)
 note('ecommerce','MySQL adaptation preserves ordered results',[[str(x) for x in row] for row in after],[[str(x) for x in row] for row in before])
 note('ecommerce','MySQL index access observed',{'beforeType':plan_before[0][4],'afterType':plan_after[0][4],'afterKey':plan_after[0][6]},passed=plan_before[0][4]=='ALL' and plan_after[0][6]=='idx_products_cat_price_rating',plans={'before':[[str(x) for x in row] for row in plan_before],'after':[[str(x) for x in row] for row in plan_after]})
finally:c.close();admin.close()

result={'date':'2026-11-05','engine':engine,'checks':checks,'passed':sum(x['passed'] for x in checks),'total':len(checks),'schemas':['pa_repo_hermitage','pa_repo_chinook','pa_repo_index'],'limits':['Selected source cases only, not full Hermitage isolation matrix.','Chinook is a fixture, not an exercise bank; course tasks are new.','SQLite upstream pass is not a MySQL compatibility claim.','Plan access observed on this dataset, no fixed speedup or all-size complexity promise.','No learner-facing web runner was deployed or browser-tested by this script.']}
(OUT/'selected-repo-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str),encoding='utf-8')
print(json.dumps({'passed':result['passed'],'total':result['total']},ensure_ascii=False));assert result['passed']==result['total']
