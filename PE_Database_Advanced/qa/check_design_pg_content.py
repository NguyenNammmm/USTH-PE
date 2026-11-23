"""Bounded checks of explicitly named examples; no PostgreSQL/C execution claim."""
from pathlib import Path
from itertools import combinations, product
from decimal import Decimal
import copy
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parents[1]
sys.path.insert(0, str(WORK / 'tmp/database-advanced-vendor'))
import pymysql

checks = []
def check(name, actual, expected):
    passed = actual == expected
    checks.append({'name':name,'passed':passed,'actual':actual,'expected':expected})
    if not passed:
        raise AssertionError((name,actual,expected))

def blocks(lesson):
    return re.findall(r'```sql\n(.*?)```', (ROOT/'lessons'/f'{lesson}.md').read_text(encoding='utf-8'), re.S)

def satisfies_fd(rows, lhs, rhs):
    return all(any(a[i]!=b[i] for i in lhs) or all(a[j]==b[j] for j in rhs)
               for a in rows for b in rows)

def project(rows, positions):
    return {tuple(t[i] for i in positions) for t in rows}

def join_projections(rows, schemas):
    if not rows:
        return set()
    domains = [sorted({t[i] for t in rows}) for i in range(len(next(iter(rows))))]
    projections = [project(rows,s) for s in schemas]
    return {t for t in product(*domains)
            if all(tuple(t[i] for i in s) in p for s,p in zip(schemas,projections))}

def model_checks():
    universe=list(product((0,1), repeat=3))
    relations=[{universe[i] for i in range(8) if mask&(1<<i)} for mask in range(256)]
    legal=[r for r in relations if satisfies_fd(r,[0],[1])]
    check('AD05 AB/AC lossless for every binary-domain instance satisfying A->B',
          all(join_projections(r,[(0,1),(0,2)])==r for r in legal), True)
    witness={(1,7,9),(2,7,10)}
    check('AD05 wrong AB/BC decomposition adds exact witness tuples',
          sorted(join_projections(witness,[(0,1),(1,2)])-witness),[(1,7,10),(2,7,9)])
    r={(0,0,0),(1,0,0),(0,1,0),(0,0,1)}
    schemas=[(0,1),(0,2),(1,2)]
    check('AD08 JD holds on four-row instance',join_projections(r,schemas)==r,True)
    r2=r-{(0,0,0)}
    check('AD08 deleting 000 preserves projections but violates JD',
          sorted(join_projections(r2,schemas)-r2),[(0,0,0)])
    rows={(1,s,o) for s in ['SQL','Python'] for o in ['Hanoi','Hue','Danang']}
    check('AD07 2x3 independence reconstructs six tuples',len(join_projections(rows,[(0,1),(0,2)])),6)
    missing=(1,'Python','Hue')
    check('AD07 missing combination detected by exact tuple witness',
          sorted(join_projections(rows-{missing},[(0,1),(0,2)])-(rows-{missing})),[missing])
    def closure(seed,fds):
        result=set(seed)
        while True:
            updated=result|set().union(*(v for u,v in fds if u<=result))
            if updated==result:return result
            result=updated
    fds=[(set('A'),set('B')),(set('B'),set('A')),(set('C'),set('D')),
         (set('D'),set('C')),(set('AC'),set('E'))]
    keys=[]
    for size in range(6):
        for t in combinations('ABCDE',size):
            s=set(t)
            if not any(k<=s for k in keys) and closure(s,fds)==set('ABCDE'):keys.append(s)
    check('AD04 all keys for independent transfer exercise',sorted(''.join(sorted(k)) for k in keys),['AC','AD','BC','BD'])
    check('AD55 deterministic generator counts',
          [sum(i%100==0 for i in range(1,20001)),sum(i%100!=0 for i in range(1,20001))],[200,19800])
    tree={'tag':'mul','children':[{'tag':'add','children':[{'tag':'literal','value':1},{'tag':'literal','value':2}]},
                                  {'tag':'neg','children':[{'tag':'literal','value':4}]}]}
    def evaluate(t):
        if t['tag']=='literal':return t['value']
        values=[evaluate(c) for c in t['children']]
        return values[0]+values[1] if t['tag']=='add' else values[0]*values[1] if t['tag']=='mul' else -values[0]
    cloned=copy.deepcopy(tree)
    tree['children'][0]['children'][0]['value']=5
    check('AD84 transfer deep-copy arithmetic/alias example',[evaluate(tree),evaluate(cloned)],[-28,-12])
    labels=['ab','CD','long','tail','x']
    check('AD83 stable top-two ownership-model answer order',sorted(enumerate(labels),key=lambda p:(-len(p[1]),p[0]))[:2],[(2,'long'),(3,'tail')])

def mysql_checks():
    with pymysql.connect(host='127.0.0.1',port=33374,user='root',autocommit=True,charset='utf8mb4',read_timeout=8) as c:
        def sql(statement):
            with c.cursor() as cur:
                cur.execute(statement)
                return list(cur.fetchall())
        engine=sql('SELECT VERSION(),@@sql_mode')
        schema='pe_design_pg_review_'+str(sql('SELECT CONNECTION_ID()')[0][0])
        sql('CREATE DATABASE '+schema)
        sql('USE '+schema)
        def run_block(block):
            result=[]
            for statement in block.split(';'):
                if statement.strip():result=sql(statement)
            return result
        def expected_error(statement,number):
            try:sql(statement)
            except pymysql.MySQLError as e:
                check('expected MySQL error '+str(number),e.args[0],number)
            else:raise AssertionError('Expected error '+str(number))
        try:
            sql('CREATE TABLE Student(id INT PRIMARY KEY)')
            sql('CREATE TABLE Passed(id INT NOT NULL,course VARCHAR(8) NOT NULL)')
            sql('CREATE TABLE Required(course VARCHAR(8) PRIMARY KEY)')
            sql('INSERT INTO Student VALUES(1),(2),(3)')
            sql("INSERT INTO Passed VALUES(1,'DB'),(1,'OS'),(2,'DB')")
            sql("INSERT INTO Required VALUES('DB'),('OS')")
            check('AD02 all required-course SQL',run_block(blocks('AD02')[0]),[(1,)])
            sql('DELETE FROM Required')
            check('AD02 empty requirements vacuous truth',sorted(run_block(blocks('AD02')[0])),[(1,),(2,),(3,)])
            sql('DELETE FROM Student');sql('DELETE FROM Passed')
            sql('INSERT INTO Student VALUES(4),(5),(6)')
            sql("INSERT INTO Passed VALUES(4,'OS'),(5,'DB'),(6,'DB'),(6,'OS')")
            check('AD02 transfer answer exact SQL',run_block(blocks('AD02')[1]),[(5,)])
            ad09=blocks('AD09')
            run_block(ad09[0])
            sql("INSERT INTO ad_course VALUES('DB','Databases')")
            sql("INSERT INTO ad_student VALUES(1,'An')")
            sql("INSERT INTO ad_offering VALUES('DB','2026A',1,NULL),('DB','2026B',1,NULL)")
            expected_error("INSERT INTO ad_enrollment VALUES(1,'DB','2026A',2,NULL)",1452)
            check('AD09 bitemporal Feb6',run_block(ad09[1]),[(Decimal('3500.00'),)])
            query=ad09[1].split('SELECT amount',1)[1]
            check('AD09 bitemporal Feb12',sql(('SELECT amount'+query).replace('2026-02-06','2026-02-12')),[(Decimal('3600.00'),)])
            check('AD09 valid history overlap empty',run_block(ad09[2]),[])
            sql("INSERT INTO ad_salary_history VALUES(4,1,'2026-02-01',NULL,3700,'2026-02-15',NULL)")
            check('AD09 overlap detector catches bad correction',run_block(ad09[2]),[(3,4)])
            sql("UPDATE ad_salary_history SET system_to='2026-02-15' WHERE version_id=3")
            check('AD09 corrected history removes conflict',run_block(ad09[2]),[])
            ad59=blocks('AD59')
            run_block(ad59[0])
            check('AD59 zero-registration preserving report',run_block(ad59[1]),[('S1',2),('S2',1),('S3',1),('S4',0)])
            check('AD59 transitive prerequisite eligibility',run_block(ad59[2]),[('S1',)])
            check('AD59 complete-key capacity detector',run_block(ad59[3]),[('DB','1','Fall',2026,3,2)])
            conflicts=run_block(ad59[4])
            check('AD59 detailed timetable conflict row',[[*r[:6],str(r[6]),str(r[7])] for r in conflicts],
                  [['S1','DB','OS','Fall',2026,'M','9:30:00','10:00:00']])
            sql("UPDATE ad_u_time_slot SET start_time='10:00:00',end_time='11:00:00' WHERE time_slot_id='T2'")
            check('AD59 half-open touching boundary has no conflict',run_block(ad59[4]),[])
            check('AD59 original prerequisite graph acyclic',run_block(ad59[5]),[])
            sql("INSERT INTO ad_u_prereq VALUES('DB','AI')")
            check('AD59 cycle detector exact participating courses',run_block(ad59[5]),[('AI',),('DB',),('OS',)])
        finally:
            sql('DROP DATABASE '+schema)
        return engine

model_checks()
engine=mysql_checks()
hashes={lesson:hashlib.sha256((ROOT/'lessons'/f'{lesson}.md').read_bytes()).hexdigest()
        for lesson in ['AD02','AD04','AD05','AD07','AD08','AD09','AD55','AD57','AD59','AD83','AD84']}
result={'scope':'Only checks explicitly named below. Finite model checks are not general proofs; MySQL checks are real engine checks on an isolated disposable schema. No PostgreSQL, FDW, extension build/load or C memory test was run.',
        'mysqlEngine':engine,'lessonSha256':hashes,'checks':checks,'passed':all(x['passed'] for x in checks)}
(ROOT/'qa/design-pg-content-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,default=str)+'\n',encoding='utf-8')
print(json.dumps({'passed':result['passed'],'checks':len(checks),'mysqlVersion':engine[0][0]}))
