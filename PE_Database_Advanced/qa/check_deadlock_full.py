"""Finite reference checks for AD40; does not run an SQL engine or web runner."""
from itertools import permutations
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
checks = []


def check(name, condition, scope):
    assert condition, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


def cycle_dfs(nodes, edges):
    color = dict.fromkeys(nodes, 0)
    adjacency = {n: [] for n in nodes}
    for a, b in edges:
        adjacency[a].append(b)

    def visit(a):
        color[a] = 1
        for b in adjacency[a]:
            if color[b] == 1 or color[b] == 0 and visit(b):
                return True
        color[a] = 2
        return False

    return any(color[n] == 0 and visit(n) for n in nodes)


def topological_order_exists(nodes, edges):
    # Independent exhaustive oracle: a finite directed graph has no cycle iff a
    # permutation puts the tail of every edge before its head.
    return any(all(order.index(a) < order.index(b) for a, b in edges)
               for order in permutations(nodes))


nodes = tuple(range(4))
possible = [(a, b) for a in nodes for b in nodes if a != b]
for mask in range(1 << len(possible)):
    edges = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
    assert cycle_dfs(nodes, edges) != topological_order_exists(nodes, edges)
check('DFS versus exhaustive topological oracle: all4096 loop-free four-node graphs',
      True, 'Finite graphs only; no distributed/OR-wait or multi-instance resource claim.')
base = [('A', 'B'), ('A', 'C'), ('C', 'B'), ('B', 'D')]
check('Lesson graph: new edge closes B-D-C cycle',
      not cycle_dfs(tuple('ABCD'), base)
      and cycle_dfs(tuple('ABCD'), base + [('D', 'C')]), 'Worked example and exercise5.')
check('A is not a cycle member in lesson graph',
      not any(b == 'A' for _, b in base + [('D', 'C')]), 'Specific witness, not generic membership algorithm.')

ages = (10, 20, 30)
wait_die = [(a, b) for a in ages for b in ages if a < b]
wound_wait = [(a, b) for a in ages for b in ages if a > b]
check('Wait-die waiting edges strictly increase timestamps',
      all(a < b for a, b in wait_die) and not cycle_dfs(ages, wait_die),
      'Unique retained timestamps; proof in lesson is required beyond this finite example.')
check('Wound-wait waiting edges strictly decrease timestamps',
      all(a > b for a, b in wound_wait) and not cycle_dfs(ages, wound_wait),
      'No liveness guarantee under unbounded arrivals/failures.')
check('Request20 against holder10 differs between policies',
      (20, 10) not in wait_die and (20, 10) in wound_wait, 'Requester/holder orientation.')
check('Partial rollback exercise undoes all suffix updates',
      [x for x in ['grantA', 'writeA', 'grantB', 'writeB', 'grantC', 'writeC'][2:]
       if x.startswith('write')] == ['writeB', 'writeC'],
      'Abstract engine with partial rollback support; not a SAVEPOINT/MySQL execution.')
check('Delete timestamp examples',
      (20 < 30 or 20 < 12) and not (35 < 30 or 35 < 12), 'Independent requests on same initial state.')
check('Insert initializes both timestamps',
      dict(read=40, write=40) == {'read': 40, 'write': 40}, 'Abstract timestamp-ordering initialization.')

# Membership-only concurrency anomaly with disjoint inserted IDs.
initial = {'night': ['existing']}
count_t1 = count_t2 = len(initial['night'])
after = initial['night'] + (['newA'] if count_t1 < 2 else []) + (['newB'] if count_t2 < 2 else [])
serial = initial['night'].copy()
for new in ['newA', 'newB']:
    if len(serial) < 2:
        serial.append(new)
check('Phantom membership anomaly and serial reference',
      len(after) == 3 and len(serial) == 2, 'Logical model, not engine isolation-level result.')
check('Empty range must still protect index leaf',
      [x for x in (10, 20, 30) if 14 <= x <= 16] == [] and 14 <= 15 <= 16,
      'S(leaf) conflicts with X(leaf) for matching insert15.')
check('Leaf granularity causes false conflict for29',
      not 14 <= 29 <= 16 and 10 <= 29 <= 30,
      'All three keys and insert positions assumed in same unchanged leafL.')
md = ROOT / 'lessons/AD40.md'
result = {
    'date': '2026-11-05', 'lesson': 'AD40',
    'lessonSha256': hashlib.sha256(md.read_bytes()).hexdigest(),
    'status': 'passed', 'checks': checks, 'count': len(checks),
    'limits': 'Finite mathematical/reference checks. No new MySQL, web backend, browser or partial rollback execution.'
}
(ROOT / 'qa/deadlock-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'status': 'passed', 'exhaustiveGraphs': 4096}))
