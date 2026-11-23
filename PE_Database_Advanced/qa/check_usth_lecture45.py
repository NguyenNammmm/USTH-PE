from pathlib import Path
from itertools import product
from collections import Counter
import hashlib
import json
import math
import re
import sqlite3

O = Path(__file__).resolve().parent
R = O.parent
checks = []
def check(name, ok, detail):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'detail': detail})

md = (R / 'lessons/USTH04.md').read_text(encoding='utf-8-sig')
blocks = re.findall(r'```sql\n(.*?)```', md, re.S)
def block(needle):
    found = [b for b in blocks if needle in b]
    assert len(found) == 1, needle
    return found[0]
db = sqlite3.connect(':memory:')
db.executescript(block('CREATE TABLE u4_room'))
inner = db.execute(block('INNER JOIN u4_member')).fetchall()
full = db.execute(block('UNION ALL')).fetchall()
check('actual-inner-and-full-emulation', len(inner) == 3 and set(full) == {(1, 'Blue', 10, 'An'), (1, 'Blue', 11, 'Binh'), (2, 'Green', 12, 'Chi'), (3, 'Quiet', None, None), (None, None, 13, 'Dung')}, f'Actual SQLite{sqlite3.sqlite_version} executes exact lesson SQL; not native MySQL validation.')
check('actual-cross-cardinality', db.execute('SELECT COUNT(*) FROM u4_room CROSS JOIN u4_member').fetchone()[0] == 12, '3x4 row pairs.')
on = db.execute("SELECT r.id,m.id FROM u4_room r LEFT JOIN u4_member m ON m.room_id=r.id AND m.name='An' ORDER BY r.id").fetchall()
where = db.execute("SELECT r.id,m.id FROM u4_room r LEFT JOIN u4_member m ON m.room_id=r.id WHERE m.name='An'").fetchall()
check('on-versus-where', on == [(1, 10), (2, None), (3, None)] and where == [(1, 10)], 'Actual two SQL executions show NULL-extended row preservation difference.')
db.executescript('CREATE TABLE u4_mark(id INTEGER,mark INTEGER); CREATE TABLE u4_band(label TEXT,lo INTEGER,hi INTEGER);')
db.executemany('INSERT INTO u4_mark VALUES(?,?)', enumerate([49, 50, 80, 100], 1))
db.executemany('INSERT INTO u4_band VALUES(?,?,?)', [('one', 0, 50), ('two', 50, 80), ('three', 80, 101)])
valid = db.execute('SELECT s.id,b.label FROM u4_mark s JOIN u4_band b ON s.mark>=b.lo AND s.mark<b.hi ORDER BY s.id').fetchall()
wrong = db.execute('SELECT s.id,b.label FROM u4_mark s JOIN u4_band b ON s.mark>=b.lo AND s.mark<=b.hi').fetchall()
check('range-join-boundaries', valid == [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'three')] and len(wrong) == 6, 'Non-equijoin is inner; inclusive upper-bound mutant creates two extra witnesses.')

pay = block('CREATE TABLE u4_pay')
db.executescript(pay[:pay.index('SELECT dept,COUNT')])
groups = db.execute(pay[pay.index('SELECT dept,COUNT'):]).fetchall()
check('group-null-count-sum', set(groups) == {(None, 1, 0, None, None, None, None), ('A', 3, 2, 30, 15, 10, 20), ('B', 2, 2, 10, 5, 5, 5)}, 'Exact lesson aggregation executes with NULL group and all-NULL group inputs.')
check('aggregate-distinct', db.execute("SELECT SUM(amount),SUM(DISTINCT amount) FROM u4_pay WHERE dept='B'").fetchone() == (10, 5) and db.execute('SELECT COUNT(DISTINCT dept) FROM u4_pay').fetchone()[0] == 2, 'Actual numeric bag and NULL-distinct examples.')
check('empty-group-versus-empty-input', db.execute('SELECT COUNT(*),SUM(amount) FROM u4_pay WHERE 0').fetchall() == [(0, None)] and db.execute('SELECT dept,COUNT(*) FROM u4_pay WHERE 0 GROUP BY dept').fetchall() == [], 'No-GROUP-BY implicit aggregate row versus no groups.')
check('where-group-having', db.execute(block("WHERE job='dev'")).fetchall() == [('A', 30)], 'Exact lesson filter/group/HAVING/ORDER BY query.')
check('nested-aggregate-rewrite', db.execute(block('SELECT MAX(dept_mean)')).fetchone()[0] == 15, 'Derived-table query avoids invalid same-query-block nested aggregation.')
db.close()
a, b = Counter('xxy'), Counter('xz')
check('bag-set-operations', a + b == Counter({'x': 3, 'y': 1, 'z': 1}) and a & b == Counter('x') and a - b == Counter('xy'), 'Python multiset oracle, not SQL ALL syntax execution.')
check('population-versus-sample', math.isclose(sum((v - 4)**2 for v in [2, 4, 6]) / 3, 8 / 3) and sum((v - 4)**2 for v in [2, 4, 6]) / 2 == 4, 'Actual arithmetic, no engine variance-function execution.')

def closure(x, f):
    result = set(x)
    while True:
        old = set(result)
        for left, right in f:
            if set(left) <= result:
                result.update(right)
        if result == old:
            return result
def subsets(attrs):
    return [frozenset(a for i, a in enumerate(attrs) if mask & (1 << i)) for mask in range(1 << len(attrs))]
def keys(attrs, f):
    found = []
    for x in sorted(subsets(attrs), key=lambda x: (len(x), sorted(x))):
        if any(k <= x for k in found):
            continue
        if closure(x, f) == set(attrs):
            found.append(x)
    return set(found)
def normal_forms(attrs, f):
    ks = keys(attrs, f); prime = set().union(*ks)
    third = bcnf = True
    for x in subsets(attrs):
        reach = closure(x, f)
        for a in reach - set(x):
            if reach != set(attrs):
                bcnf = False
                if a not in prime:
                    third = False
    return third, bcnf
specs = [
 ('ABCDEF', [('AB', 'C'), ('BC', 'AD'), ('D', 'E'), ('CF', 'B')], {'CF', 'ABF'}, 18, (False, False)),
 ('ABCD', [('BC', 'D'), ('D', 'A'), ('A', 'B')], {'AC', 'BC', 'CD'}, 4, (True, False)),
 ('ABCD', [('A', 'B'), ('A', 'C'), ('C', 'D')], {'A'}, 7, (False, False)),
 ('ABCD', [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')], {'A', 'B', 'C', 'D'}, 11, (True, True)),
 ('ABCD', [('AD', 'B'), ('AB', 'C'), ('BC', 'D'), ('CD', 'A')], {'AB', 'AD', 'BC', 'CD'}, 5, (True, True)),
]
closure_oracles = 0
for attrs, f, wanted, nonminimal, forms in specs:
    kk = keys(attrs, f)
    assert kk == {frozenset(x) for x in wanted}
    supers = [x for x in subsets(attrs) if closure(x, f) == set(attrs)]
    assert len(supers) - len(kk) == nonminimal
    assert normal_forms(attrs, f) == forms
    # Independent two-tuple binary equality oracle: tuple0 is all zero;
    # tuple1 differs exactly outside an agreement set. A FD is satisfied iff
    # agreement on its LHS implies agreement on its RHS.
    agreement_models = [agree for agree in subsets(attrs) if all(not set(l) <= agree or set(r) <= agree for l, r in f)]
    for x in subsets(attrs):
        models = [agree for agree in agreement_models if x <= agree]
        implied = set.intersection(*(set(m) for m in models))
        assert implied == closure(x, f)
        closure_oracles += 1
check('all-five-fd-systems', True, 'Exact full candidate-key sets, nonminimal-superkey counts and all implied singleton FD normal-form conditions for five teaching systems, not just source answer strings.')
check('closure-independent-oracle', closure_oracles == 128, '128 closures compared with independent enumeration of two-tuple binary agreement models satisfying each input FD set; unbounded argument provided in lesson.')
complex_f = specs[0][1]
check('closure-exercise-AB-CF', closure('AB', complex_f) == set('ABCDE') and closure('CF', complex_f) == set('ABCDEF'), 'Explicit source exercise and missing-F distinction.')
mixed = [('A', 'BCD'), ('BC', 'A'), ('C', 'D')]
check('single-PK-does-not-prove-2NF', keys('ABCD', mixed) == {frozenset('A'), frozenset('BC')} and 'D' in closure('C', mixed), 'D is nonprime, C proper subset of alternate candidate keyBC; counterexample to primary-key-only claim.')
check('right-side-pruning-counterexample', keys('ABC', [('A', 'B'), ('B', 'C'), ('C', 'A')]) == {frozenset('A'), frozenset('B'), frozenset('C')}, 'All attributes appear on RHS yet each is a candidate key.')
r = {(1, 2, 3), (4, 2, 5)}
ab = {(a, b) for a, b, c in r}; bc = {(b, c) for a, b, c in r}
joined = {(a, b, c) for a, b in ab for b2, c in bc if b == b2}
check('lossy-projection-join', joined - r == {(1, 2, 5), (4, 2, 3)}, 'Exact new tuple identities, not just larger cardinality.')
ac = {('a', 'c1'), ('a', 'c2')}; bc = {('c1', 'b'), ('c2', 'b')}
joined = {(a, b, c) for a, c in ac for c2, b in bc if c == c2}
check('preservation-versus-lossless', len({c for a, b, c in joined}) == 2 and len({(a, b) for a, b, c in joined}) == 1, 'Local C->B holds but reconstructed equalAB has twoC values.')

for name, count in [('USTH04', 8), ('USTH05', 10)]:
    text = (R / 'lessons' / f'{name}.md').read_text(encoding='utf-8-sig')
    q = text.split('## Luyện tập\n', 1)[1].split('\n## ', 1)[0]
    a = text.split('## Đáp án và lập luận\n', 1)[1].split('\n## ', 1)[0]
    assert re.findall(r'^(\d+)\.', q, re.M) == re.findall(r'^(\d+)\.', a, re.M) == list(map(str, range(1, count + 1)))
check('eighteen-questions-answered', True, 'Full lesson activity/answer sequence matches; semantic answers separately manually compared with sources and finite models.')
out = {'date': '2026-11-05', 'passed': len(checks), 'checks': checks,
       'scope': 'Selected actual SQLite execution plus finite multiset/arithmetic/FD models. No native MySQL join/ALL/collation/ONLY_FULL_GROUP_BY execution, general SQL equivalence certification, or deployed web runner. Source pages manually read separately.',
       'lessons': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['USTH04', 'USTH05']}}
(O / 'usth-lecture45-checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'passed': len(checks), 'closureOracles': closure_oracles, 'questions': 18, 'sqlite': sqlite3.sqlite_version}))
