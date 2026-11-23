"""Finite semantic checks for AD01/02/10; no MySQL server is used or implied.

Run from workspace root. Only the report is written. SQLite is used for portable
SELECT fragments, not for MySQL-specific scalar cardinality, DDL, LATERAL or ROLLUP.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import math
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / 'output/database-advanced/research/semantic-sql-foundations-checks.json'
checks = []


def check(name, actual, expected, scope):
    assert actual == expected, (name, actual, expected)
    checks.append({'name': name, 'status': 'pass', 'scope': scope,
                   'actual': actual, 'expected': expected})


db = sqlite3.connect(':memory:')
db.set_progress_handler(lambda: 1, 500000)


def rows(sql):
    return [list(r) for r in db.execute(sql).fetchall()]


measure = "WITH Measure AS (SELECT 'A' team,10 val UNION ALL SELECT 'A',10 UNION ALL SELECT 'A',NULL UNION ALL SELECT 'B',NULL) "
check('aggregate duplicates, NULL, grouping', rows(measure + 'SELECT team,COUNT(*),COUNT(val),COUNT(DISTINCT val),SUM(val),AVG(val),MIN(val),MAX(val) FROM Measure GROUP BY team ORDER BY team'),
      [['A',3,2,1,20,10.0,10,10],['B',1,0,0,None,None,None,None]], 'Portable SQLite SELECT, four input rows; not MySQL execution')
check('empty global aggregate', rows(measure + 'SELECT COUNT(*),SUM(val) FROM Measure WHERE 0'), [[0,None]], 'Portable SQLite SELECT')
check('empty grouped aggregate', rows(measure + 'SELECT team,COUNT(*) FROM Measure WHERE 0 GROUP BY team'), [], 'Portable SQLite SELECT')
check('HAVING group predicate', rows(measure + 'SELECT team,SUM(val) FROM Measure GROUP BY team HAVING COUNT(*)>=2'), [['A',20]], 'Portable SQLite SELECT')
metric = 'WITH metrics(day_no,id,value) AS (VALUES(1,1,10),(1,2,20),(2,3,5),(4,4,7)) '
check('window frame examples', rows(metric + '''SELECT id,
SUM(value) OVER(ORDER BY day_no),
SUM(value) OVER(ORDER BY day_no,id ROWS UNBOUNDED PRECEDING),
SUM(value) OVER(ORDER BY day_no,id ROWS 1 PRECEDING),
SUM(value) OVER(ORDER BY day_no,id ROWS 2 PRECEDING),
SUM(value) OVER(ORDER BY day_no RANGE BETWEEN 1 PRECEDING AND CURRENT ROW),
SUM(value) OVER(ORDER BY day_no,id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
FROM metrics ORDER BY day_no,id'''),
      [[1,30,10,10,10,30,30],[2,30,30,30,30,30,35],[3,35,35,25,35,35,32],[4,42,42,12,32,7,12]],
      'Portable SQLite numeric ROWS/RANGE on exactly four rows')
ranked = rows('WITH scores(id,s) AS (VALUES(1,10),(2,10),(3,20),(4,40)) SELECT ROW_NUMBER() OVER(ORDER BY s,id),RANK() OVER(ORDER BY s),DENSE_RANK() OVER(ORDER BY s),PERCENT_RANK() OVER(ORDER BY s),CUME_DIST() OVER(ORDER BY s),NTILE(3) OVER(ORDER BY s,id) FROM scores ORDER BY s,id')
check('rank functions and ties', ranked,
      [[1,1,1,0.0,0.5,1],[2,1,1,0.0,0.5,1],[3,3,2,2/3,0.75,2],[4,4,3,1.0,1.0,3]], 'Portable SQLite rank model; singleton MySQL additionally checked from official source, not run')
check('singleton percent/cumulative model', rows('SELECT PERCENT_RANK() OVER(ORDER BY x),CUME_DIST() OVER(ORDER BY x) FROM (SELECT 10 x)'), [[0.0,1.0]], 'SQLite model only')
check('NULL comparison versus DISTINCT', rows('WITH t(x) AS (VALUES(NULL),(NULL)) SELECT COUNT(*) FROM (SELECT DISTINCT x FROM t)'), [[1]], 'Portable SQLite SELECT')
check('NOT IN NULL trap', rows('SELECT 2 NOT IN (1,NULL),NOT EXISTS(SELECT 1 FROM (SELECT 1 id UNION ALL SELECT NULL) y WHERE y.id=2)'), [[None,1]], 'Portable SQLite SELECT')
check('row comparison and literal LIKE', rows("SELECT (1,100)<(2,0),10 BETWEEN 10 AND 20,'sale%off' LIKE 'sale!%%' ESCAPE '!'"), [[1,1,1]], 'Portable numeric row comparison and explicit-escape LIKE; no MySQL collation assertion')
check('full outer reconstruction', rows('''WITH L(id) AS (VALUES(1),(2)),R(rid,lid) AS (VALUES(10,1),(11,1),(12,3))
SELECT l.id,r.rid,r.lid FROM L l LEFT JOIN R r ON r.lid=l.id
UNION ALL SELECT NULL,r.rid,r.lid FROM R r WHERE NOT EXISTS(SELECT 1 FROM L l WHERE l.id=r.lid)'''),
      [[1,10,1],[1,11,1],[2,None,None],[None,12,3]], 'Portable SQLite anti-branch query; four expected bag rows')
sales = "WITH Sales(item,color,qty) AS (VALUES('Pen','red',2),('Pen','red',3),('Pen','blue',4),('Book','red',1),('Book',NULL,6)) "
check('pivot conditional aggregation', rows(sales + "SELECT item,SUM(CASE WHEN color='red' THEN qty END),SUM(CASE WHEN color='blue' THEN qty END) FROM Sales GROUP BY item ORDER BY item"), [['Book',1,None],['Pen',5,4]], 'Portable SQLite SELECT, five input rows')
check('cube explicit grouping branches', rows(sales + '''SELECT item,color,SUM(qty),0,0 FROM Sales GROUP BY item,color
UNION ALL SELECT item,NULL,SUM(qty),0,1 FROM Sales GROUP BY item
UNION ALL SELECT NULL,color,SUM(qty),1,0 FROM Sales GROUP BY color
UNION ALL SELECT NULL,NULL,SUM(qty),1,1 FROM Sales'''),
      [['Book',None,6,0,0],['Book','red',1,0,0],['Pen','blue',4,0,0],['Pen','red',5,0,0],['Book',None,7,0,1],['Pen',None,9,0,1],[None,None,6,1,0],[None,'blue',4,1,0],[None,'red',6,1,0],[None,None,16,1,1]],
      'Portable SQLite explicit grouping branches, no claim that SQLite implements MySQL WITH ROLLUP')

# Every possible Passed on two students x two courses, every Required subset:64.
db.executescript('CREATE TABLE Student(id INTEGER PRIMARY KEY); INSERT INTO Student VALUES(1),(2); CREATE TABLE Passed(id INTEGER,course TEXT); CREATE TABLE Required(course TEXT);')
calculus_cases = 0
pairs = list(itertools.product((1,2),('DB','OS')))
for pmask in range(16):
    passed = {p for j,p in enumerate(pairs) if pmask & (1<<j)}
    for rmask in range(4):
        required = {c for j,c in enumerate(('DB','OS')) if rmask & (1<<j)}
        db.execute('DELETE FROM Passed'); db.execute('DELETE FROM Required')
        db.executemany('INSERT INTO Passed VALUES(?,?)', sorted(passed))
        db.executemany('INSERT INTO Required VALUES(?)', [(c,) for c in sorted(required)])
        actual = rows('SELECT s.id FROM Student s WHERE NOT EXISTS(SELECT 1 FROM Required r WHERE NOT EXISTS(SELECT 1 FROM Passed p WHERE p.id=s.id AND p.course=r.course)) ORDER BY s.id')
        expected = [[i] for i in (1,2) if all((i,c) in passed for c in required)]
        assert actual == expected
        calculus_cases += 1
check('double NOT EXISTS versus bounded universal calculus', calculus_cases, 64, 'Exhaustive two students/two courses; no NULL, set membership, all16 Passed and4 Required instances')

# Compare frontier algorithm against an independent Floyd-Warshall closure on
# every directed graph on three vertices:512 graphs, cycles and self-loops included.
vertices = range(3)
edges_possible = list(itertools.product(vertices,repeat=2))
graph_cases = 0
for mask in range(512):
    edges = {e for j,e in enumerate(edges_possible) if mask & (1<<j)}
    floyd = set(edges)
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if (i,k) in floyd and (k,j) in floyd: floyd.add((i,j))
    for start in vertices:
        found,frontier={start},{start}
        rounds=0
        while frontier:
            nxt={v for u,v in edges if u in frontier}-found
            found |= nxt;frontier=nxt;rounds+=1
            assert rounds<=4
        assert found == {start}|{v for u,v in floyd if u==start}
    graph_cases += 1
check('frontier versus independent positive closure', graph_cases,512,'Finite exhaustive three-vertex graphs; three starts each; model proof support, not universal proof')
check('positive closure cycle example', rows('''WITH RECURSIVE edge(src,dst) AS (VALUES('A','B'),('B','A'),('B','C')),
closure(src,dst) AS (SELECT src,dst FROM edge UNION SELECT c.src,e.dst FROM closure c JOIN edge e ON c.dst=e.src)
SELECT src,dst FROM closure ORDER BY src,dst'''), [['A','A'],['A','B'],['A','C'],['B','A'],['B','B'],['B','C']], 'SQLite UNION replaces spelling UNION DISTINCT only; three-vertex positive closure')

A=Counter(['a','a','a','b',None]); B=Counter(['a','a','c',None])
check('set ALL multiplicity formulas', {'union':dict(A+B),'intersect':dict(A&B),'except':dict(A-B)},
      {'union':{'a':5,'b':1,None:2,'c':1},'intersect':{'a':2,None:1},'except':{'a':1,'b':1}}, 'Counter model; NULL represented by same sentinel for duplicate comparison')
q=lambda x: x.quantize(Decimal('.01'),rounding=ROUND_HALF_UP)
case=q(Decimal(98)*Decimal('1.05')); twice=q(case*Decimal('1.03'))
check('CASE versus two-statement threshold', [str(case),str(twice)],['102.90','105.99'],'Exact Decimal model; no MySQL UPDATE execution')
check('summary AVG maintenance', str((Decimal(60)+90+30)/3),'60','Exact Decimal sum/count model')
check('bounded safety counterexample', [[i for i in D if i not in {1,2,3}] for D in [{1,2,3},{1,2,3,4}]], [[],[4]],'Two explicit trial domains; counterexample only, no safety decision algorithm')
check('universal quantifier hidden domain', [all(c in {2} for c in D) for D in [{2},{2,3}]], [True,False],'Two explicit trial domains')

ledger_path=OUT.with_name('semantic-sql-foundations.json')
if ledger_path.exists():
    ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
    checked=0
    for u in ledger['units']:
        sp=ROOT/u['source']['path'];lines=sp.read_text(encoding='utf-8').splitlines();a,b=u['source']['ownBodyLines']
        assert hashlib.sha256(sp.read_bytes()).hexdigest()==u['source']['sha256']
        assert hashlib.sha256('\n'.join(lines[a-1:b]).encode()).hexdigest()==u['source']['ownBodySha256']
        for ev in u['evidence']+u.get('algorithmProofEvidence',[]):
            p=ROOT/ev['path'];md=p.read_text(encoding='utf-8').splitlines();lo,hi=ev['lineRange'];fragment='\n'.join(md[lo-1:hi])
            assert hashlib.sha256(p.read_bytes()).hexdigest()==ev['sha256']
            assert fragment==ev['paragraphExcerpt']
            assert hashlib.sha256(fragment.encode()).hexdigest()==ev['fragmentSha256']
        checked+=1
    check('ledger exact source and lesson witnesses',checked,80,'All80 assigned own-body units; cryptographic reproducibility, not automatic semantic judgement')

report={'status':'pass','engine':'Python finite models + SQLite '+sqlite3.sqlite_version,
        'mysqlExecuted':False,'limits':{'sqliteProgressAbortAfterVmInstructions':500000,'calculusCases':64,'graphs':512,'graphVertices':3,'maximumModelRounds':4},
        'checks':checks,'limitations':['No MySQL server available; DDL/view updatability/LATERAL/ROLLUP/scalar-cardinality-error/collation/transaction behavior is documented and expected, not executed here.','Finite checks support worked examples; written proofs carry the general claims.','Hash validation checks references, never substitutes for the full source read and semantic comparison.']}
OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','checks':len(checks),'report':str(OUT),'mysqlExecuted':False},ensure_ascii=False))
