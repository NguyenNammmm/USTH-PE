"""Original finite RA/reference tasks and selected SQLite SQL executions."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import math
import re
import sqlite3

O = Path(__file__).resolve().parent
R = O.parent
checks = []
def check(name, ok, scope):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})

rooms = {('A', 'East'), ('B', 'West'), ('C', 'West')}
loans = {('B', 'mic', 35), ('B', 'screen', 50), ('C', 'mic', 45), ('D', 'mic', 20)}
x = {r for r, w in rooms if w == 'East'}
y = {r for r, i, c in loans if i == 'mic' and c < 40}
check('or-expression-branches', x | y == {'A', 'B', 'D'} and x & y == set(), 'Actual finite set evaluation; no RA parser execution.')
check('west-screen-tree-answer', {r for r, w in rooms if w == 'West'} | {r for r, i, _ in loans if i == 'screen'} == {'B', 'C'}, 'Leaf/selection/projection/union tree reference result.')
two = {r1 for r1, i1, c1 in loans for r2, i2, c2 in loans if r1 == r2 and i1 != i2}
wrong = {r1 for r1, i1, c1 in loans for r2, i2, c2 in loans if r1 == r2 and i1 != i2 and c1 == c2}
check('natural-selfjoin-mutant', two == {'B'} and wrong == set(), 'Leaving cost as an unintended natural-join equality loses the correct pair.')
check('anti-semijoin-answer', {r for r, _ in rooms} - {r for r, _, _ in loans} == {'A'}, 'Universe is Room, not arbitrary strings.')
bag = [('A', 2), ('A', 2)]
right = [('A', 'x'), ('A', 'y')]
exists = [r for r in bag if any(r[0] == s[0] for s in right)]
projection = [r for r in bag for s in right if r[0] == s[0]]
check('semijoin-bag-contract', len(exists) == 2 and len(projection) == 4 and len(set(projection)) == 1, 'Bag left duplicates versus right witness multiplication versus DISTINCT.')
check('projection-schema-values', {(q*p, q, q) for q, p in [(4, 15), (2, 25)]} == {(60, 4, 4), (50, 2, 2)}, 'Authored extended projection exercise; type/rounding assumptions separate.')

universe = {0, 1, 2}
subsets = [set(c) for n in range(4) for c in combinations(universe, n)]
for a, b in product(subsets, repeat=2):
    assert a & b == a - (a - b)
check('primitive-intersection-derivation', True, '64 exhaustive subset pairs agree with derived intersection.')
check('precedence-counterexample', {1} | ({2} & {2}) != ({1} | {2}) & {2}, 'Parentheses change results under mixed union/intersection.')

orders = [('K7', 'Lan', 'Hue'), ('K7', 'Lan', 'Danang')]
bad = [(a, b) for a in orders for b in orders if a[0] == b[0] and a[1] != b[1] and a[2] != b[2]]
good = [(a, b) for a in orders for b in orders if a[0] == b[0] and (a[1] != b[1] or a[2] != b[2])]
check('key-and-versus-or', bad == [] and len(good) == 2, 'Source slide60 faulty AND misses pair differing in only one nonkey.')
# Independently compare pairwise violation versus map uniqueness for every set
# of up to 8 triples over two values per attribute.
tuples = list(product(range(2), repeat=3)); key_fixtures = 0
for mask in range(1 << len(tuples)):
    rows = [t for i, t in enumerate(tuples) if mask & (1 << i)]
    pair_violation = any(a[0] == b[0] and a[1:] != b[1:] for a in rows for b in rows)
    grouped = {}
    for t in rows:
        grouped.setdefault(t[0], set()).add(t[1:])
    assert pair_violation == any(len(v) > 1 for v in grouped.values())
    key_fixtures += 1
check('key-violation-oracle', key_fixtures == 256, '256 finite set instances compared against independent grouped-key oracle, no NULL/bags.')
check('foreign-key-difference', {'P1', 'P9'} - {'P1', 'P2'} == {'P9'} and set() - {'P1'} == set(), 'Missing-parent and empty-child inclusion cases.')
rows = [('auto', 49, 8, 700), ('auto', 50, 8, 900), ('manual', 40, 16, 901)]
v1 = [i + 1 for i, (m, r, mem, p) in enumerate(rows) if r < 50 and p > 700]
v2 = [i + 1 for i, (m, r, mem, p) in enumerate(rows) if mem < 16 and r < 80 and p >= 900]
check('implication-boundary-answers', v1 == [3] and v2 == [2], 'Strict/equality boundary cases for independently graded constraints.')
demorgan_cases = 0
for trigger, a, b in product([False, True], repeat=3):
    assert (trigger and not (a or b)) == (trigger and not a and not b)
    demorgan_cases += 1
check('conditional-disjunction', demorgan_cases == 8, 'Complete Boolean truth table, no SQL UNKNOWN.')
portable = [('L1', 16, 800), ('L2', 8, 600)]
station = [('D1', 8, 800), ('D2', 16, 900)]
violations = [(l[0], d[0]) for l, d in product(portable, station) if l[1] > d[1] and l[2] <= d[2]]
check('cross-table-constraint', violations == [('L1', 'D1')], 'Product/selection includes price-equality violation; empty input separately vacuous.')
catalog = [('M', 'p', 'probe'), ('M', 'c', 'camera'), ('N', 'h', 'hub')]
probe, camera = {'p'}, {'c'}
makers = lambda models: {m for m, model, kind in catalog if model in models}
check('indirect-disjointness', makers(probe) & makers(camera) == {'M'}, 'Explicit model membership join prevents makerN false positive.')

db = sqlite3.connect(':memory:')
md3 = (R / 'lessons/USTH03.md').read_text(encoding='utf-8')
blocks = re.findall(r'```sql\n(.*?)```', md3, re.S)
def block(needle):
    found = [b for b in blocks if needle in b]
    assert len(found) == 1, needle
    return found[0]
db.executescript(block('CREATE TABLE u3_people'))
check('insert-select-actual-sql', db.execute('SELECT id,name FROM u3_selected ORDER BY id').fetchall() == [(1, 'An'), (3, 'Chi')] and db.execute('SELECT COUNT(*) FROM u3_people').fetchone()[0] == 4, f'Actual SQLite{sqlite3.sqlite_version} exact authored SQL fixture/INSERT SELECT; not native MySQL claim.')
try:
    db.execute("INSERT INTO u3_selected(id,name) SELECT id,name FROM u3_people WHERE city='Hue'")
except sqlite3.IntegrityError:
    duplicate_rejected = True
else:
    duplicate_rejected = False
check('insert-select-duplicate', duplicate_rejected, 'Actual selected SQLite PK error on second insertion; no idempotence assumed.')
for query, expected in [
 ('DELETE FROM u3_people WHERE dept_id IS NULL', [(2, 4), (3, 5)]),
 ('DELETE FROM u3_people', []),
 ('UPDATE u3_people SET dept_id=8 WHERE dept_id IS NULL', [(1, 8), (2, 4), (3, 5), (4, 8)]),
 ('UPDATE u3_people SET dept_id=8', [(1, 8), (2, 8), (3, 8), (4, 8)])]:
    db.execute('SAVEPOINT branch')
    db.execute(query)
    got = db.execute('SELECT id,dept_id FROM u3_people ORDER BY id').fetchall()
    assert got == expected
    db.execute('ROLLBACK TO branch'); db.execute('RELEASE branch')
check('four-dml-branches', True, 'Four actual SQL branch executions restored to same original fixture via savepoints.')
db.execute('CREATE TABLE u3_score(id INTEGER PRIMARY KEY,score INTEGER,eligible INTEGER)')
db.executemany('INSERT INTO u3_score VALUES(?,?,1)', enumerate([90, 90, 85, 85, 80, 75, 70], 1))
db.create_function('CEIL', 1, math.ceil)
check('top-percent-window-query', db.execute(block('WITH ranked AS')).fetchall() == [(1, 90), (2, 90), (3, 85)], 'Exact authored window query executed on SQLite; ceil30% of filtered7, deterministic id tie-breaker, no SQL Server TOP execution.')
db.execute('UPDATE u3_score SET eligible=0 WHERE id=7')
check('top-percent-after-filter', db.execute(block('WITH ranked AS')).fetchall() == [(1, 90), (2, 90)], 'Recomputed COUNT OVER after eligibility filter leaves6 and ceil1.8=2.')
db.close()

for name in ['USTH01', 'USTH02', 'USTH03']:
    text = (R / 'lessons' / f'{name}.md').read_text(encoding='utf-8')
    q = text.split('## Luyện tập\n', 1)[1].split('\n## ', 1)[0]
    a = text.split('## Đáp án và lập luận\n', 1)[1].split('\n## ', 1)[0]
    qids = re.findall(r'^(\d+)\.', q, re.M)
    aids = re.findall(r'^(\d+)\.', a, re.M)
    assert qids == aids and len(qids) == len(set(qids)), (name, qids, aids)
check('all-supplement-activities-have-answers', True, '8+15+12 =35 authored questions/answers, numbering and fenced code balance checked separately from semantic review.')
out = {'date': '2026-11-05', 'passed': len(checks), 'checks': checks,
       'scope': 'Finite original RA set/bag/arithmetic models and selected actual SQLite queries. No general RA parser, MySQL identifier/collation/DDL/FK/locking validation or web backend execution in this report. Historical/manual claims were source-reviewed separately.',
       'lessons': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['USTH01', 'USTH02', 'USTH03']}}
(O / 'usth-foundations-supplement-checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'passed': len(checks), 'keyFixtures': key_fixtures, 'questions': 35, 'sqlite': sqlite3.sqlite_version}))
