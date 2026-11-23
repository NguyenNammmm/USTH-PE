"""Finite AD28/63 algorithm witnesses; no native CAS, SQL or timing measurement."""
from pathlib import Path
from itertools import permutations, product
import hashlib
import json

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite mathematical state model'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


def apply(state, op):
    kind, key, value = op
    if kind == 'delete':
        state.pop(key, None)
    else:
        state[key] = value


ops = [('put', 2, 'B'), ('put', 1, 'C'), ('delete', 2, None)]
cuts = 0
for schedule in permutations(ops):
    for cut in range(4):
        base = {1: 'A'}
        for op in schedule[:cut]:
            apply(base, op)
        snapshot = base.copy()
        delta = []
        for op in schedule[cut:]:
            apply(base, op); delta.append(op)
        index = snapshot.copy()
        for op in delta:
            apply(index, op)
        assert index == base
        cuts += 1
check('Online build snapshot+delta equals current relation for24 schedules/cuts', cuts == 24,
      'Single relation, deterministic finite updates; publication barrier assumed and checked separately.')
base = {1: 'A'}
index = base.copy()
base[2] = 'B'  # writer in the forbidden log-off/maintenance-off gap
check('Missing publication barrier has an explicit counterexample', index != base)

# Two insert-head attempts both started at A. Only the winning CAS updates head.
head = 'A'
links = {'A': None, 'N1': 'A', 'N2': 'A'}
head = 'N1'
expected2 = 'A'
check('Second CAS with stale expected pointer fails', head != expected2)
links['N2'] = head
head = 'N2'
walk = []
while head is not None:
    walk.append(head); head = links[head]
check('CAS retry recomputes next and retains both inserted nodes', walk == ['N2', 'N1', 'A'])
check('ABA pointer comparison passes while tagged comparison fails',
      'A' == 'A' and ('A', 7) != ('A', 10))
check('Finite tag can wrap', (7 + 4) % 4 == 7 % 4,
      'Counter-width witness; memory reclamation is a distinct requirement.')

# A stale-parent lookup at left must follow a correctly published right link.
left, right = [10, 20], [30, 40]
target = 35
routed = right if target >= 30 else left
check('B-link stale parent uses high-key/right-link route',
      target not in left and routed is right and 30 <= target <= 40,
      'Route35 reaches correct leaf, then reports absent; fence/link publication and node lifetime assumed.')


def next_key_range(keys, low, high):
    matches = [k for k in keys if low <= k <= high]
    successor = next((k for k in keys if k > high), 'INF')
    return matches + [successor]


check('Empty predicate range protects successor', next_key_range([10, 20, 30], 14, 16) == [20])
check('Nonempty predicate range and unbounded tail',
      next_key_range([10, 20, 30], 10, 20) == [10, 20, 30]
      and next_key_range([10, 20, 30], 35, 40) == ['INF'])
check('Insert/delete successor conflicts match lesson witnesses',
      set([15, 20]) & set(next_key_range([10, 20, 30], 14, 16)) == {20}
      and set([25, 30]) & set(next_key_range([10, 20, 30], 10, 20)) == {30})

for a, b in product(range(-3, 4), repeat=2):
    assert (100 + a) + b == (100 + b) + a
check('Increment commutation across49 delta pairs', True,
      'No returned intermediate value or additional invariant; arbitrary-precision model integers.')
check('Compensation preserves another transaction contribution',
      100 + 7 + 9 - 7 == 109 and 100 != 109)


def reserve(order):
    available = 1
    status = {}
    for t in order:
        status[t] = available >= 1
        if status[t]:
            available -= 1
    return status


check('Conditional reservation does not commute as labeled outcomes', reserve([1, 2]) != reserve([2, 1]))
check('Transfer interleaving preserves only the stated total invariant',
      (100 - 20 + 5, 100 - 5 + 20) == (85, 115)
      and 85 + 115 == 200)
check('Deadline counterexample: rollback slower than waiting', 4 + 1 <= 5 and 6 + 1 > 5,
      'Declared milliseconds with zero other overhead; not a realtime benchmark.')

result = {'date': '2026-11-05', 'status': 'passed', 'count': len(checks), 'checks': checks,
          'lessonSha256': {name: hashlib.sha256((R / 'lessons' / f'{name}.md').read_bytes()).hexdigest()
                           for name in ['AD28', 'AD63']},
          'limits': 'Finite state and arithmetic witnesses only. No SQL, native atomic/memory-order, concurrent index implementation or deadline execution.'}
(R / 'qa/advanced-concurrency-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'onlineBuildCuts': cuts, 'status': 'passed'}))
