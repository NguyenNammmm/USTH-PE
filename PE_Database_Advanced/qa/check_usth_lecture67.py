"""Computed ER/search oracles, selected SQLite reads, optional exact MySQL blocks.
No SQL Server execution is claimed. Native mode creates only a fresh task schema.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from decimal import Decimal
import hashlib
import json
import re
import sqlite3
import sys
import uuid

R = Path(__file__).resolve().parents[1]
W = R.parents[1]
checks = []
sources = {name: (R / 'lessons' / (name + '.md')).read_text(encoding='utf-8-sig') for name in ['USTH06', 'USTH07']}

def check(name, actual, expected, detail=''):
    assert actual == expected, (name, actual, expected)
    checks.append({'name': name, 'passed': True, 'actual': actual, 'expected': expected, 'detail': detail})

for name, text in sources.items():
    for heading in ['Luyện tập', 'Đáp án và lập luận']:
        section = text.split('## ' + heading + '\n', 1)[1].split('\n## ', 1)[0]
        check(name + '-' + heading, list(map(int, re.findall(r'^(\d+)\.\s', section, re.M))), list(range(1, 11)))
    check(name + '-fences', text.count('```') % 2, 0)

permission = {('Lan', 'A', 'M1'), ('Lan', 'B', 'C1'), ('Minh', 'A', 'C1')}
def reconstructed(rows):
    mr = {(m, r) for m, r, d in rows}
    md = {(m, d) for m, r, d in rows}
    rd = {(r, d) for m, r, d in rows}
    return {(m, r, d) for m, r in mr for m2, d in md if m == m2 and (r, d) in rd}
check('ternary-original-counterexample', sorted(reconstructed(permission) - permission), [('Lan', 'A', 'C1')])
universe = list(product(range(2), repeat=3))
lossy = 0
for mask in range(256):
    rel = {t for i, t in enumerate(universe) if mask & (1 << i)}
    rebuilt = reconstructed(rel)
    assert rel <= rebuilt
    lossy += rel != rebuilt
check('ternary-projection-finite-oracle', lossy > 0, True, 'All 256 relations over a 2x2x2 universe; this finite check is not a general proof.')

assignments = list(product(range(3), repeat=2))
valid_one_one = [a for a in assignments if len(set(a)) == len(a)]
check('maker-exactly-one-device-at-most-one', len(valid_one_one), 6, 'Two mandatory Makers inject into three optional Devices; one Device may remain unfeatured.')
check('roles-not-symmetry', ('B', 'A') in {('A', 'B')}, False)
check('canonical-friendship', sorted({tuple(sorted(pair)) for pair in [('A', 'B'), ('B', 'A'), ('A', 'C')]}), [('A', 'B'), ('A', 'C')])

subtype_cases = 0
for states in product(['basic', 'known-camera', 'unknown-camera'], repeat=3):
    logical = {i: (s != 'basic', 24 if s == 'known-camera' else None) for i, s in enumerate(states)}
    root = set(logical)
    camera = {i: res for i, (is_cam, res) in logical.items() if is_cam}
    concrete_basic = {i for i, (is_cam, res) in logical.items() if not is_cam}
    single = {i: ('camera' if is_cam else 'basic', res) for i, (is_cam, res) in logical.items()}
    assert {i: (i in camera, camera.get(i)) for i in root} == logical
    assert set(camera).isdisjoint(concrete_basic) and set(camera) | concrete_basic == root
    assert {i: (kind == 'camera', res) for i, (kind, res) in single.items()} == logical
    subtype_cases += 1
check('three-subtype-mappings-with-unknown-resolution', subtype_cases, 27, 'Disjoint partial specialization, stable identity; NULL alone cannot encode subtype membership.')

db = sqlite3.connect(':memory:')
db.execute('PRAGMA foreign_keys=ON')
db.executescript('''
CREATE TABLE room(id TEXT PRIMARY KEY);
CREATE TABLE device(id TEXT PRIMARY KEY, room_id TEXT NOT NULL REFERENCES room(id));
CREATE TABLE port(device_id TEXT NOT NULL REFERENCES device(id), port_number INT NOT NULL,
 label TEXT, PRIMARY KEY(device_id,port_number));
CREATE TABLE member(id TEXT PRIMARY KEY);
CREATE TABLE favorite(member_id TEXT PRIMARY KEY REFERENCES member(id),device_id TEXT REFERENCES device(id));
CREATE TABLE camera(id TEXT PRIMARY KEY REFERENCES device(id),resolution INT);
INSERT INTO room VALUES('A'),('B'),('Empty');
INSERT INTO device VALUES('M1','A'),('C1','B');
INSERT INTO member VALUES('Lan');
INSERT INTO port VALUES('M1',1,'p'),('C1',1,'p');
INSERT INTO camera VALUES('C1',24);
''')
def reject_sqlite(statement):
    try:
        db.execute(statement)
    except sqlite3.IntegrityError:
        return True
    return False
check('actual-SQLite-weak-key-owner-qualified', db.execute('SELECT COUNT(*) FROM port').fetchone()[0], 2)
check('actual-SQLite-weak-duplicate-key-rejected', reject_sqlite("INSERT INTO port VALUES('M1',1,'again')"), True)
check('actual-SQLite-weak-missing-owner-rejected', reject_sqlite("INSERT INTO port VALUES('absent',1,'p')"), True)
check('actual-SQLite-FK-does-not-force-parent-participation', db.execute('SELECT r.id FROM room r LEFT JOIN device d ON d.room_id=r.id WHERE d.id IS NULL').fetchall(), [('Empty',)])
db.execute("INSERT INTO favorite VALUES('Lan','M1')")
check('actual-SQLite-one-favorite-per-member', reject_sqlite("INSERT INTO favorite VALUES('Lan','C1')"), True)
check('actual-SQLite-root-subclass-identity', db.execute('SELECT d.id,c.resolution FROM device d JOIN camera c ON c.id=d.id').fetchall(), [('C1', 24)])

blocks = re.findall(r'```sql\n(.*?)```', sources['USTH07'], re.S)
def block(needle):
    found = [b for b in blocks if needle in b]
    assert len(found) == 1, (needle, len(found))
    return found[0].strip()

fixture = block('CREATE TABLE u7_product')
db.executescript(fixture)
db.executescript(block('CREATE VIEW u7_sales'))
db.executescript(block('CREATE VIEW u7_large_sales'))
check('actual-SQLite-three-view-queries', [db.execute('SELECT * FROM ' + v + ' ORDER BY 1').fetchall() for v in ['u7_sales', 'u7_large_sales', 'u7_above_average']], [[(501,70),(502,10)],[(501,70)],[(2,20)]], 'Exact fixture/read-only view SQL; no MySQL updatability or trigger inference.')
db.execute('INSERT INTO u7_line VALUES(9,502,2,2,20)')
check('actual-SQLite-view-reads-new-base-data', db.execute('SELECT total FROM u7_sales WHERE order_id=502').fetchone()[0], 50)
db.close()

depths = []
for wanted in range(22):
    lo, hi, comparisons = 0, 21, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comparisons += 1
        if mid == wanted:
            break
        if wanted < mid:
            hi = mid - 1
        else:
            lo = mid + 1
    depths.append(comparisons)
check('binary-search-22-depths', dict(Counter(depths)), {1:1,2:2,3:4,4:8,5:7})
check('binary-search-22-total-and-maximum', [sum(depths),max(depths)], [84,5])
check('uniform-linear-search-22', [sum(range(1,23))/22,22], [11.5,22])
check('nullable-price-audit-truth-table', [a != b for a,b in [(10,12),(10,10),(None,12),(12,None),(None,None)]], [True,False,True,True,False], 'Finite value-level oracle; SQL NULL-safe predicate checked separately in native mode.')
check('grouped-stock-versus-first-row-mutant', [10-sum([3,4]),10-[3,4][0]], [3,7])
check('statement-row-limit-model', [n <= 2 for n in [0,1,2,3]], [True,True,True,False], 'No SQL Server process was run.')

engine = None
schema = None
if '--mysql' in sys.argv:
    sys.path.insert(0, str(W / 'tmp/database-advanced-vendor'))
    import pymysql
    schema = 'pe_usth67_' + uuid.uuid4().hex[:12]
    cn = pymysql.connect(host='127.0.0.1',port=33374,user='root',charset='utf8mb4',autocommit=True,connect_timeout=5,read_timeout=10)
    try:
        with cn.cursor() as cur:
            def execute(sql, params=None):
                cur.execute(sql, params)
                result = cur.fetchall()
                while cur.nextset():
                    cur.fetchall()
                return result
            def rejected(sql, code):
                try:
                    execute(sql)
                except pymysql.MySQLError as ex:
                    return ex.args[0] == code
                return False
            engine = execute('SELECT VERSION()')[0][0]
            assert engine.startswith('8.4.')
            assert execute('SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME=%s',(schema,)) == ()
            execute('CREATE DATABASE `' + schema + '`')
            cn.select_db(schema)
            # Only the known fixture has simple top-level statements; never split routine bodies.
            for statement in fixture.split(';'):
                if statement.strip():
                    execute(statement)
            for statement in block('CREATE INDEX u7_price_ix').split(';'):
                if statement.strip():
                    execute(statement)
            check('MySQL-index-exists', len(execute("SHOW INDEX FROM u7_product WHERE Key_name='u7_price_ix'")), 1)
            sales = block('CREATE VIEW u7_sales').split(';')[0]
            execute(sales)
            for statement in block('CREATE VIEW u7_large_sales').split(';'):
                if statement.strip():
                    execute(statement)
            check('MySQL-exact-three-views', [execute('SELECT * FROM '+v+' ORDER BY 1') for v in ['u7_sales','u7_large_sales','u7_above_average']], [((501,Decimal('70.00')),(502,Decimal('10.00'))),((501,Decimal('70.00')),),((2,Decimal('20.00')),)])
            execute(block('CREATE PROCEDURE u7_count_city'))
            execute("CALL u7_count_city('Hue',@n)")
            check('MySQL-procedure-IN-OUT-Hue', execute('SELECT @n'), ((2,),))
            execute("CALL u7_count_city('Danang',@n)")
            check('MySQL-procedure-IN-OUT-empty', execute('SELECT @n'), ((0,),))
            execute(block('CREATE VIEW u7_hue_customers'))
            execute("INSERT INTO u7_hue_customers VALUES(4,'Hue')")
            check('MySQL-check-option-insert-hidden-rejected', rejected("INSERT INTO u7_hue_customers VALUES(5,'Danang')",1369), True)
            check('MySQL-check-option-update-hidden-rejected', rejected("UPDATE u7_hue_customers SET city='Danang' WHERE id=4",1369), True)
            execute("INSERT INTO u7_customer VALUES(5,'Danang')")
            check('MySQL-base-write-not-filtered-by-view', [execute('SELECT city FROM u7_customer WHERE id=5'),execute('SELECT * FROM u7_hue_customers WHERE id=5')], [ (('Danang',),), () ])
            execute(block('CREATE TRIGGER u7_take_stock'))
            execute('INSERT INTO u7_line VALUES(4,503,1,3,10),(5,503,1,4,10)')
            check('MySQL-multirow-same-product-stock', execute('SELECT stock FROM u7_product WHERE id=1'), ((3,),))
            check('MySQL-insufficient-stock-statement-fails', rejected('INSERT INTO u7_line VALUES(6,504,1,2,10),(7,504,1,2,10)',3819), True)
            check('MySQL-failed-multirow-line-and-stock-rollback', [execute('SELECT COUNT(*) FROM u7_line WHERE line_id IN(6,7)'),execute('SELECT stock FROM u7_product WHERE id=1')], [((0,),),((3,),)])
            execute(block('CREATE TABLE u7_price_audit'))
            execute(block('CREATE TRIGGER u7_audit_price'))
            execute('UPDATE u7_product SET price=12 WHERE id IN(1,3)')
            check('MySQL-audit-multirow-including-NULL', execute('SELECT product_id,old_price,new_price FROM u7_price_audit ORDER BY product_id'), ((1,Decimal('10.00'),Decimal('12.00')),(3,None,Decimal('12.00'))))
            execute('UPDATE u7_product SET price=price WHERE id IN(1,3)')
            check('MySQL-no-audit-for-unchanged-price', execute('SELECT COUNT(*) FROM u7_price_audit'), ((2,),))
            execute('UPDATE u7_product SET price=NULL WHERE id=1')
            check('MySQL-audit-new-NULL', execute('SELECT COUNT(*) FROM u7_price_audit WHERE product_id=1 AND old_price=12 AND new_price IS NULL'), ((1,),))
            check('MySQL-trigger-DDL-outside-statement-count-branch', len(execute('SHOW TRIGGERS')), 2, 'MySQL row triggers only. SQL Server trigger code remains engine acceptance work.')
            check('MySQL-fixture-InnoDB', set(row[0] for row in execute('SELECT ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA=%s AND TABLE_TYPE=%s',(schema,'BASE TABLE'))), {'InnoDB'})
    finally:
        cn.close()

def safe(value):
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, set):
        return sorted(value)
    raise TypeError(type(value).__name__)

report = {'date':'2026-11-06','scope':'USTH06/07 independent finite examples and selected actual SQLite queries; native MySQL checks explicitly named when --mysql is supplied; no SQL Server engine, production backend, or all-workload guarantee.',
          'lessonSha256':{name:hashlib.sha256((R/'lessons'/f'{name}.md').read_bytes()).hexdigest() for name in sources},
          'engine':engine,'schemaCreatedFresh':schema,'cleanup':'Fresh task-local schema retained; no DROP. Task server shutdown handled separately.',
          'sqliteVersion':sqlite3.sqlite_version,'finiteTernaryRelations':256,'subtypeCases':subtype_cases,'checks':checks,'passed':len(checks),'total':len(checks)}
(R/'qa/usth-lecture67-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=safe),encoding='utf-8')
print(json.dumps({'passed':len(checks),'total':len(checks),'engine':engine,'schema':schema}))
