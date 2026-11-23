"""Independent finite examples and exact authored SQL on fresh MySQL schemas.
Only task-local new schemas are used; no pre-existing table/schema is dropped.
"""
from pathlib import Path
from collections import Counter
from decimal import Decimal
import datetime
import hashlib
import json
import math
import re
import sqlite3
import statistics
import sys
import uuid

R = Path(__file__).resolve().parents[1]
W = R.parents[1]
names = ['USTH08','USTH09','USTH10','USTH11']
texts = {name:(R/'lessons'/f'{name}.md').read_text(encoding='utf-8-sig') for name in names}
checks=[]
def check(name,actual,expected):
    assert actual == expected,(name,actual,expected)
    checks.append({'name':name,'passed':True,'actual':actual,'expected':expected})
def close(name,actual,expected,tol=0.000001):
    assert math.isclose(float(actual),float(expected),rel_tol=tol,abs_tol=tol),(name,actual,expected)
    checks.append({'name':name,'passed':True,'actual':actual,'expected':expected,'numericTolerance':tol})
for name,n in zip(names,[8,10,36,24]):
    for heading in ['Luyện tập','Đáp án và lập luận']:
        section=texts[name].split('## '+heading+'\n',1)[1].split('\n## ',1)[0]
        check(name+'-'+heading,list(map(int,re.findall(r'^(\d+)\.\s',section,re.M))),list(range(1,n+1)))
    check(name+'-fences',texts[name].count('```')%2,0)
    check(name+'-no-unexpanded-include','<!--__' in texts[name],False)

# SQLite is used only for exact key/FK counterexamples, not to certify MySQL DDL.
db=sqlite3.connect(':memory:')
db.execute('PRAGMA foreign_keys=ON')
db.executescript('''
CREATE TABLE artist(id TEXT PRIMARY KEY);
CREATE TABLE album(artist TEXT NOT NULL REFERENCES artist(id),id INT NOT NULL,PRIMARY KEY(artist,id));
CREATE TABLE track(artist TEXT NOT NULL,album INT NOT NULL,id INT NOT NULL,
 PRIMARY KEY(artist,album,id),FOREIGN KEY(artist,album) REFERENCES album(artist,id));
CREATE TABLE played(artist TEXT NOT NULL,album INT NOT NULL,track INT NOT NULL,at TEXT NOT NULL,
 PRIMARY KEY(artist,album,track,at),FOREIGN KEY(artist,album,track) REFERENCES track(artist,album,id));
INSERT INTO artist VALUES('A'),('B');
INSERT INTO album VALUES('A',1),('B',1);
INSERT INTO track VALUES('A',1,1),('A',1,2),('B',1,1);
INSERT INTO played VALUES('A',1,1,'2026-01-01 10:00:00'),('A',1,1,'2026-01-01 10:03:00');
CREATE TABLE program(id TEXT PRIMARY KEY);
CREATE TABLE student(id TEXT PRIMARY KEY,program TEXT NOT NULL REFERENCES program(id),UNIQUE(id,program));
CREATE TABLE course(program TEXT NOT NULL REFERENCES program(id),id INT NOT NULL,planned_year INT,planned_semester INT,PRIMARY KEY(program,id));
CREATE TABLE attempt(student TEXT NOT NULL,program TEXT NOT NULL,course INT NOT NULL,year INT NOT NULL,semester INT NOT NULL,
 mark INT NULL,PRIMARY KEY(student,program,course,year,semester),
 FOREIGN KEY(student,program) REFERENCES student(id,program),FOREIGN KEY(program,course) REFERENCES course(program,id));
INSERT INTO program VALUES('DA'),('SE');
INSERT INTO student VALUES('S1','DA');
INSERT INTO course VALUES('DA',101,1,1),('SE',101,1,2);
INSERT INTO attempt VALUES('S1','DA',101,2026,1,0),('S1','DA',101,2027,1,NULL);
''')
def reject(statement):
    try:db.execute(statement)
    except sqlite3.IntegrityError:return True
    return False
check('SQLite-two-owner-local-album-track-IDs',db.execute('SELECT COUNT(*) FROM track WHERE id=1').fetchone()[0],2)
check('SQLite-full-owner-FK',reject("INSERT INTO track VALUES('A',2,1)"),True)
played=db.execute('SELECT t.artist,t.album,t.id,COUNT(p.at),MAX(p.at) FROM track t LEFT JOIN played p ON p.artist=t.artist AND p.album=t.album AND p.track=t.id GROUP BY t.artist,t.album,t.id ORDER BY t.artist,t.album,t.id').fetchall()
check('SQLite-play-count-max-and-zero',played,[('A',1,1,2,'2026-01-01 10:03:00'),('A',1,2,0,None),('B',1,1,0,None)])
check('SQLite-same-second-event-key-collision',reject("INSERT INTO played VALUES('A',1,1,'2026-01-01 10:00:00')"),True)
check('SQLite-retake-distinct-term-preserved',db.execute('SELECT year,mark FROM attempt ORDER BY year').fetchall(),[(2026,0),(2027,None)])
check('SQLite-composite-FK-program-policy',reject("INSERT INTO attempt VALUES('S1','SE',101,2026,1,50)"),True)
check('SQLite-attempt-same-term-duplicate',reject("INSERT INTO attempt VALUES('S1','DA',101,2026,1,60)"),True)
db.close()
check('capacity-count-then-write-race-model',[9+1,9+1,9+2],[10,10,11])
check('annualization-75-over10',75/10*12,90)
close('P2.10-standard-deviation-prose',statistics.pstdev([20,25,15,15,5,200,5]),65.379582)
close('L9-B-category-STD-prose',statistics.pstdev([10,50,10]),18.856181)

blocks={name:re.findall(r'```sql\n(.*?)```',s,re.S) for name,s in texts.items()}
def exact(name,needle):
    hits=[b.strip() for b in blocks[name] if needle in b]
    assert len(hits)==1,(name,needle,len(hits))
    return hits[0]
def simple_statements(sql):
    # Only the reviewed fixture/simple DDL/DML blocks, no procedural body or
    # string containing ';'. This is not a general SQL parser for the web runner.
    cleaned=re.sub(r'^\s*--[^\n]*(?:\n|$)','',sql,flags=re.M)
    return [s.strip() for s in cleaned.split(';') if s.strip()]

engine=None;schemas=[];query_results={}
if '--mysql' in sys.argv:
    sys.path.insert(0,str(W/'tmp/database-advanced-vendor'))
    import pymysql
    cn=pymysql.connect(host='127.0.0.1',port=33374,user='root',charset='utf8mb4',autocommit=True,connect_timeout=5,read_timeout=10)
    try:
        with cn.cursor() as cur:
            def execute(sql,params=None):
                cur.execute(sql,params);rows=cur.fetchall()
                while cur.nextset():cur.fetchall()
                return rows
            def fresh(label):
                schema='pe_final_'+label+'_'+uuid.uuid4().hex[:10]
                assert execute('SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME=%s',(schema,))==()
                execute('CREATE DATABASE `'+schema+'` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci')
                cn.select_db(schema);schemas.append(schema);return schema
            def sql_error(sql,code):
                try:execute(sql)
                except pymysql.MySQLError as ex:return ex.args[0]==code
                return False
            engine=execute('SELECT VERSION()')[0][0];assert engine.startswith('8.4.')
            company=fresh('company')
            for statement in simple_statements(exact('USTH10','-- P1.03')):execute(statement)
            check('MySQL-Company-eight-source-FKs',execute('SELECT COUNT(*) FROM information_schema.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA=%s',(company,)),((8,),))
            execute(exact('USTH10','-- P1.04'))
            for statement in simple_statements(exact('USTH10','-- P1.05')):execute(statement)
            check('MySQL-Company-Minit-leading-zero-roundtrip',execute('SELECT ssn,minit FROM employee ORDER BY ssn'),(('000000001','T'),('000000002',None),('000000003',None)))
            check('MySQL-Company-source-table-count',execute('SELECT COUNT(*) FROM information_schema.TABLES WHERE TABLE_SCHEMA=%s',(company,)),((6,),))
            check('MySQL-Company-missing-parent-rejected',sql_error("INSERT INTO works_on VALUES('000000099',10,1)",1452),True)
            # Deletion exercise is executed only after verifying the exact six
            # tables in the new random database created by this process.
            owned={r[0] for r in execute('SHOW TABLES')}
            assert owned=={'employee','department','dept_locations','project','works_on','dependent'}
            for statement in simple_statements(exact('USTH10','-- P1.06')):execute(statement)
            check('MySQL-Company-P1.06-owned-tables-deleted',execute('SHOW TABLES'),())

            northwind=fresh('northwind')
            for statement in simple_statements(exact('USTH10','CREATE TABLE employees')):execute(statement)
            p2_expected={
              1:((3,'Old Notebook'),),
              2:((5,'Pen',Decimal(5)),(7,'Ruler',Decimal(5)),(3,'Old Notebook',Decimal(15)),(4,'Milk',Decimal(15))),
              3:((1,'Tea',Decimal(20)),(2,'Coffee',Decimal(25)),(3,'Old Notebook',Decimal(15)),(4,'Milk',Decimal(15))),
              4:((1,'Anh Nguyen'),(2,'Minh Tran'),(3,'An Le')),
              5:((1,'Anh','Nguyen'),(3,'An','Le')),
              6:((2,),),7:(('Hanoi Lab',),('Hue Studio',),('PE School',)),
              8:((Decimal(5),Decimal(200)),),9:((6,),),11:(('Machine',Decimal(200)),)}
            for n in range(1,12):
                rows=execute(exact('USTH10',f'-- P2.{n:02}'))
                query_results[f'P2.{n:02}']=rows
                if n==10:
                    close('MySQL-P2.10-mean',rows[0][0],Decimal(285)/7)
                    close('MySQL-P2.10-STD',rows[0][1],statistics.pstdev([20,25,15,15,5,200,5]))
                else:check(f'MySQL-P2.{n:02}',rows,p2_expected[n])
            for n in [12,13,14]:
                for statement in simple_statements(exact('USTH10',f'-- P2.{n:02}')):execute(statement)
            check('MySQL-P2.12-14-correct-parent-and-cost',execute("SELECT s.company,p.product_code,p.list_price,p.standard_cost FROM suppliers s JOIN products p ON p.supplier_id=s.id WHERE p.product_code='TBTruc Bach'"),(('Habeco','TBTruc Bach',Decimal(22),Decimal(18)),))
            delete=simple_statements(exact('USTH10','-- P2.15'))
            check('MySQL-P2.15-expected-FK-error',sql_error(delete[0],1451),True)
            execute(delete[1])
            check('MySQL-P2.15-rollback-state',execute("SELECT COUNT(*) FROM products WHERE product_code='TBTruc Bach'"),((0,),))
            for n in range(1,16):
                sql=exact('USTH10',f'-- P3.{n:02}')
                if n==11:
                    execute(sql)
                    rows=execute('CALL top_categories(2)')
                else:rows=execute(sql)
                query_results[f'P3.{n:02}']=rows
                if n==1:check('MySQL-P3.01-IDs',[r[0] for r in rows],[31,32,34])
                if n==2:check('MySQL-P3.02-line-values',[r[-1] for r in rows],[Decimal(540),Decimal(500)])
                if n==3:check('MySQL-P3.03-grain',[r[0] for r in rows],[31,31,32])
                if n==4:check('MySQL-P3.04-subtotals',[(r[0],r[-1]) for r in rows],[(31,Decimal(1040)),(32,Decimal(1200)),(34,Decimal(0))])
                if n==5:check('MySQL-P3.05-filter',[r[0] for r in rows],[31,32])
                if n==6:check('MySQL-P3.06-sales',[(r[0],r[-1]) for r in rows],[(2,Decimal(1200)),(1,Decimal(1055))])
                if n==7:check('MySQL-P3.07-categories',rows,(('Beverages',),('Equipment',),('Stationery',)))
                if n==8:
                    check('MySQL-P3.08-cost-min-max-mean',rows[0][:3],(Decimal(2),Decimal(140),Decimal('27.5')))
                    close('MySQL-P3.08-cost-variance',rows[0][4],statistics.pvariance([12,18,10,8,2,140,2.5]))
                if n==9:
                    check('MySQL-P3.09-categories',[r[0] for r in rows],['Beverages','Equipment','Stationery'])
                    for a,b in zip(rows,[20,200,25/3]):close('MySQL-P3.09-'+a[0],a[1],b)
                if n==10:check('MySQL-P3.10-fees',rows,(('Hanoi',Decimal(10),Decimal(10)),('Hue',Decimal(20),Decimal(20))))
                if n==11:
                    check('MySQL-P3.11-top-n',rows,(('Equipment',Decimal(200)),('Beverages',Decimal(20))))
                    for value in ['NULL','0','-1']:check('MySQL-P3.11-invalid-'+value,sql_error('CALL top_categories('+value+')',1644),True)
                if n==12:close('MySQL-P3.12-minimum-average',rows[0][0],25/3)
                if n==13:check('MySQL-P3.13-approver-NULL',rows,((80,'Anh Nguyen','Minh Tran'),(81,'An Le',None)))
                if n==14:check('MySQL-P3.14-partner-roles',Counter(r[-1] for r in rows),{'C':3,'S':3})
                if n==15:check('MySQL-P3.15-purchased-never-sold',rows,((3,'Old Notebook'),(7,'Ruler')))

            reports=fresh('reports')
            fixture=(R/'fixtures/usth09_northwind.sql').read_text(encoding='utf-8')
            check('USTH11-embedded-fixture-identical',fixture.strip() in texts['USTH11'],True)
            for statement in simple_statements(fixture):execute(statement)
            execute(exact('USTH11','CREATE VIEW u9_order_total'))
            execute(exact('USTH11','CREATE VIEW u9_employee_order_count'))
            for tag in ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','22','23a','23b','24a','24b']:
                rows=execute(exact('USTH11','-- L9.R'+tag+'\n'))
                query_results['L9.R'+tag]=rows
                if tag=='01':check('MySQL-L9.R01-gap',[r[0] for r in rows],[5])
                if tag=='02':check('MySQL-L9.R02-units',rows,((1,'Tea',Decimal(110)),))
                if tag=='03':close('MySQL-L9.R03-average',rows[0][0],110/3)
                if tag=='04':
                    for row,mean,std in zip(rows,[25,70/3,100],[5,statistics.pstdev([10,50,10]),0]):
                        close('MySQL-L9.R04-'+row[0]+'-mean',row[1],mean);close('MySQL-L9.R04-'+row[0]+'-std',row[2],std)
                if tag=='05':check('MySQL-L9.R05-cities',rows,((None,1),('Hanoi',2),('Hue',1)))
                if tag=='06':check('MySQL-L9.R06-products',rows,(('A',2),('B',3),('C',1)))
                if tag=='07':check('MySQL-L9.R07-sort',[r[0] for r in rows],['B','A','C'])
                if tag=='08':check('MySQL-L9.R08-never-sold',rows,((6,'Ruler'),))
                if tag=='09':check('MySQL-L9.R09-customer-order-count',rows,((21,3),(22,2),(23,1),(24,0)))
                if tag=='10':check('MySQL-L9.R10-highest-count',rows,((2,4),))
                if tag=='11':check('MySQL-L9.R11-last-name',rows,((2,'Le'),))
                if tag=='12':check('MySQL-L9.R12-subtotals',rows,tuple((i,Decimal(v)) for i,v in [(31,254),(32,2000),(33,1850),(34,80),(35,225),(36,0)]))
                if tag=='13':check('MySQL-L9.R13-having-equivalent',rows,((32,Decimal(2000)),(33,Decimal(1850))))
                if tag=='14':check('MySQL-L9.R14-zero-employees',rows,((1,2),(2,4),(3,0),(4,0)))
                if tag=='15':check('MySQL-L9.R15-product-sales',[(r[0],r[2]) for r in rows],[(i,Decimal(v)) for i,v in [(1,2000),(2,134),(3,50),(4,225),(5,2000),(6,0)]])
                if tag=='16':check('MySQL-L9.R16-global-average',[r[0] for r in rows],[4,5])
                if tag=='17':check('MySQL-L9.R17-closed-fees',rows,(('Hanoi',Decimal(100)),('Hue',Decimal(100)),('Paris',Decimal(125))))
                if tag=='18':check('MySQL-L9.R18-own-category',[r[0] for r in rows],['Coffee','Notebook'])
                if tag=='19':check('MySQL-L9.R19-processing-days',rows,((1,Decimal('3.5')),(2,Decimal(2)),(3,None),(4,None)))
                if tag=='20':
                    check('MySQL-L9.R20-exact-four-columns',[len(r) for r in rows],[4]*6)
                    check('MySQL-L9.R20-joins-statuses',[(r[0],r[1],r[-1]) for r in rows],[('Blue Lab','Nguyen','Closed'),('Green Lab','Nguyen','Closed'),('Blue Lab','Le','Open'),('Quiet Lab','Le','Closed'),('Green Lab','Le','Closed'),('Blue Lab','Le','Open')])
                if tag=='22':check('MySQL-L9.R22-employee-sales',[(r[0],r[2]) for r in rows],[(1,Decimal(2254)),(2,Decimal(2155)),(3,Decimal(0)),(4,Decimal(0))])
                if tag=='23a':check('MySQL-L9.R23a-customer-regions',rows,(('Asia',2),('Europe',1),('North America',1)))
                if tag=='23b':check('MySQL-L9.R23b-customer-countries',rows,(('France',1),('USA',1),('Vietnam',2)))
                if tag=='24a':check('MySQL-L9.R24a-order-regions',rows,(('Asia',4),('Europe',2),('North America',0)))
                if tag=='24b':check('MySQL-L9.R24b-order-countries',rows,(('France',2),('USA',0),('Vietnam',4)))
            # Adversarial cases exercise claims beyond the worked fixture.
            execute("INSERT INTO u9_product VALUES(7,'TIE','Tie','C',100,20,0)")
            check('MySQL-L9.R01-tie-retained',[r[0] for r in execute(exact('USTH11','-- L9.R01\n'))],[5,7])
            execute("INSERT INTO u9_orders VALUES(37,'O37','2026-01-16',24,3,NULL,1,'NY',NULL,NULL),(38,'O38','2026-01-17',24,3,NULL,1,'NY',NULL,NULL),(39,'O39','2026-01-18',24,3,NULL,1,'NY',NULL,NULL),(40,'O40','2026-01-19',24,3,NULL,1,'NY',NULL,NULL)")
            check('MySQL-L9.R10-tied-employee-counts',[r[0] for r in execute(exact('USTH11','-- L9.R10\n'))],[2,3])
            execute("INSERT INTO u9_order_line VALUES(37,7,15,100,0)")
            check('MySQL-L9.R13-strict-1500-boundary',37 in [r[0] for r in execute(exact('USTH11','-- L9.R13\n'))],False)
            check('MySQL-L9-business-PO-ordinal-scoped',execute('SELECT ordinal_number,COUNT(*) FROM u9_po GROUP BY ordinal_number'),((1,2),))
            check('MySQL-L9-PO-duplicate-in-same-supplier-rejected',sql_error("INSERT INTO u9_po VALUES(83,101,1,'2026-01-03','cash',1,NULL)",1062),True)
    finally:cn.close()

def safe(value):
    if isinstance(value,Decimal):return str(value)
    if isinstance(value,(datetime.date,datetime.datetime)):return value.isoformat()
    raise TypeError(type(value).__name__)
out={'date':'2026-11-06','scope':'Four final-source supplements; exact authored Company/Practice2/Practice3 and Lecture9 report SQL on fresh MySQL schemas when --mysql supplied, finite ER examples on SQLite and arithmetic models. No production web backend, no all-dataset SQL-equivalence guarantee.',
 'lessons':{n:hashlib.sha256((R/'lessons'/f'{n}.md').read_bytes()).hexdigest() for n in names},
 'engine':engine,'sqliteVersion':sqlite3.sqlite_version,'freshSchemas':schemas,
 'cleanup':'Only exact six Company tables in its newly created schema were dropped as P1.06 exercise. All task schemas retained; task server shutdown recorded separately.',
 'checks':checks,'passed':len(checks),'total':len(checks),'queryResults':query_results}
(R/'qa/usth-final-sources-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2,default=safe),encoding='utf-8')
print(json.dumps({'passed':len(checks),'total':len(checks),'engine':engine,'schemas':schemas}))
