"""Finite models for AD41/42 and one SQLite version-check statement.

These do not implement an SQL concurrency manager, SSI, or a production runner.
"""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import sqlite3

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite reference model only'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


def view_signature(ops):
    writer = None
    reads = []
    for t, op in ops:
        if op == 'r':
            reads.append((t, writer))
        else:
            writer = t
    return sorted(reads), writer


def conflict_edges(ops):
    return {(a, b) for i, (a, p) in enumerate(ops)
            for b, q in ops[i + 1:] if a != b and (p == 'w' or q == 'w')}


def has_topological_order(nodes, edges):
    return any(all(p.index(a) < p.index(b) for a, b in edges)
               for p in permutations(nodes))


example = [(1, 'r'), (2, 'w'), (1, 'w'), (3, 'w')]
serial = [(1, 'r'), (1, 'w'), (2, 'w'), (3, 'w')]
check('View example preserves initial reader and final writer', view_signature(example) == view_signature(serial))
check('Same example has a conflict cycle', not has_topological_order((1, 2, 3), conflict_edges(example)))


def to_trace(ops, thomas=False):
    rts = wts = 0
    accepted = []
    outcomes = []
    aborted = set()
    for ts, op in ops:
        if ts in aborted:
            continue
        if op == 'r':
            if ts < wts:
                aborted.add(ts); outcomes.append('abort-read')
            else:
                rts = max(rts, ts); accepted.append((ts, op)); outcomes.append('read')
        elif ts < rts:
            aborted.add(ts); outcomes.append('abort-reader-conflict')
        elif ts < wts:
            if thomas:
                outcomes.append('ignored-write')
            else:
                aborted.add(ts); outcomes.append('abort-obsolete-write')
        else:
            wts = ts; accepted.append((ts, op)); outcomes.append('write')
    return accepted, outcomes, (rts, wts)


# Every transaction has two operations in program order; enumerate all90 shuffles.
ops = [(t, op) for t in (1, 2, 3) for op in ('r', 'w')]
valid = [p for p in permutations(ops)
         if all(p.index((t, 'r')) < p.index((t, 'w')) for t in (1, 2, 3))]
assert len(valid) == 90
for p in valid:
    accepted, _, _ = to_trace(p)
    assert all(a < b for a, b in conflict_edges(accepted))
    assert has_topological_order((1, 2, 3), conflict_edges(accepted))
check('Basic TO accepted-operation graph: all90 program-order shuffles', True,
      'Accepted operation prefixes only; recovery/commit dependency is a separate requirement.')
accepted, outcomes, stamps = to_trace([(1, 'r'), (2, 'w'), (1, 'w')], thomas=True)
check('Thomas separates ignored request from executed writer',
      outcomes == ['read', 'write', 'ignored-write'] and stamps == (1, 2)
      and view_signature(accepted)[1] == 2)
_, outcomes, _ = to_trace([(3, 'r'), (2, 'w')], thomas=True)
check('Thomas must test reader conflict before ignoring stale write', outcomes[-1] == 'abort-reader-conflict')


def validate_serial_publish(start, rs, history):
    return all(not (ws & rs) for finish, ws in history if finish > start)


check('OCC disjoint writes do not force abort merely for overlap',
      validate_serial_publish(1, {'A'}, [(4, {'B'})]))
check('OCC detects late published write to read set',
      not validate_serial_publish(1, {'A', 'B'}, [(4, {'B'})]))
check('OCC can ignore writes already present before start',
      validate_serial_publish(5, {'B'}, [(4, {'B'})]))

versions = [{'w': 0, 'r': 0, 'v': 5}, {'w': 12, 'r': 12, 'v': 9}, {'w': 30, 'r': 30, 'v': 20}]
selected = max((x for x in versions if x['w'] <= 20), key=lambda x: x['w'])
selected['r'] = max(selected['r'], 20)
late = max((x for x in versions if x['w'] <= 15), key=lambda x: x['w'])
check('MVTO reader20 and late writer15', selected['v'] == 9 and late['r'] == 20 and 15 < late['r'])
check('MVTO valid intervals have half-open boundaries',
      max(w for w in (0, 12, 30) if w <= 12) == 12
      and max(w for w in (0, 12, 30) if w <= 29) == 12)

# Independently compare every remaining reader's chosen timestamp before/after GC.
gc_cases = 0
timeline = [0, 5, 7, 8]
for oldest in range(10):
    eligible = [v for v in timeline if v <= oldest]
    removable = eligible[:-1]
    kept = [v for v in timeline if v not in removable]
    for reader in range(oldest, 13):
        assert max(v for v in timeline if v <= reader) == max(v for v in kept if v <= reader)
        gc_cases += 1
check('MV2PL GC preserves all modeled active/future reader choices', True,
      f'{gc_cases} timestamp choices; no retention, uncommitted version or crash recovery modeled.')

counter = 7
committed = {7: (100, 100)}
private = (90, 110)
before = committed[counter]
committed[8] = private
counter = 8
check('MV2PL prefix publication: old and new reader', before == (100, 100) and committed[counter] == (90, 110))


def fcw_allows(start, proposed_keys, committed_versions):
    return not any(key in proposed_keys and ts > start for key, ts in committed_versions)


check('FCW detects concurrent same-item committed writer', not fcw_allows(10, {'Q'}, [('Q', 12)]))
check('FCW permits already-visible or disjoint writer',
      fcw_allows(10, {'Q'}, [('Q', 9)]) and fcw_allows(10, {'R'}, [('Q', 12)]))
fuw_after_outcome = {'abort': 'recheck-and-proceed-if-clean', 'commit': 'abort-waiter'}
check('FUW outcome distinguishes holder abort and commit',
      fuw_after_outcome['abort'] != fuw_after_outcome['commit'])


def serial_doctors(order):
    active = {1: 1, 2: 1}
    for t in order:
        if sum(active.values()) > 1:
            active[t] = 0
    return active


check('Write-skew counterexample disagrees with both serial orders',
      all(sum(serial_doctors(order).values()) == 1 for order in [(1, 2), (2, 1)])
      and sum({1: 0, 2: 0}.values()) == 0)
check('Two-edge rw chain is not itself a cycle',
      has_topological_order((1, 2, 3), {(1, 2), (2, 3)}))
check('Doctor rw dependencies form a two-way cycle',
      not has_topological_order((1, 2), {(1, 2), (2, 1)}))

# Concrete observation sequences for the two scan anomalies in AD42.
double_observed = [(10, 7), (90, 7)]
miss_observed = []  # key10 visited before move; key90 visited after move.
check('Degree-two moved-key scan examples',
      [row for _, row in double_observed].count(7) == 2 and 7 not in miss_observed,
      'Specific possible observation schedules, not a claim about all RC SQL engines.')

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE item(id INTEGER PRIMARY KEY,value INTEGER,version INTEGER)')
db.execute('INSERT INTO item VALUES(1,10,7)')
first = db.execute('UPDATE item SET value=?,version=version+1 WHERE id=? AND version=?', (11, 1, 7)).rowcount
second = db.execute('UPDATE item SET value=?,version=version+1 WHERE id=? AND version=?', (12, 1, 7)).rowcount
state = db.execute('SELECT value,version FROM item WHERE id=1').fetchone()
check('Actual SQLite conditional version update: stale attempt affects0 rows',
      (first, second, state) == (1, 0, (11, 8)),
      f'SQLite{sqlite3.sqlite_version}; sequential stale-version scenario only; not MySQL/concurrent runner execution.')
db.close()

result = {'date': '2026-11-05', 'status': 'passed', 'count': len(checks), 'checks': checks,
          'lessons': {name: hashlib.sha256((R / 'lessons' / f'{name}.md').read_bytes()).hexdigest()
                      for name in ['AD41', 'AD42']},
          'limits': 'Finite reference models and one actual SQLite version-update scenario; no new MySQL/PostgreSQL, SSI engine, production runner or browser execution.'}
(R / 'qa/timestamp-mvcc-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'TOShuffles': len(valid), 'gcReaderChoices': gc_cases, 'status': 'passed'}))
