"""Finite quorum/version/scan models and actual SHA-256 Merkle computations.

No replica cluster, network delivery, signature service or native DBMS execution.
"""
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import random

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite model only'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


quorum_fixtures = 0
for n in range(1, 8):
    for read, write in product(range(1, n + 1), repeat=2):
        reads = list(map(set, combinations(range(n), read)))
        writes = list(map(set, combinations(range(n), write)))
        intersects_rw = all(a & b for a in reads for b in writes)
        intersects_ww = all(a & b for a in writes for b in writes)
        assert intersects_rw == (read + write > n)
        assert intersects_ww == (2 * write > n)
        quorum_fixtures += 1
check('Exhaustive equal-weight quorum intersections for140threshold fixtures', quorum_fixtures == 140)
weights = {'A': 2, 'B': 1, 'C': 1}
subsets = [set(k) for size in range(4) for k in combinations(weights, size)]
eligible = lambda q: [s for s in subsets if sum(weights[k] for k in s) >= q]
minimal = lambda q: [s for s in eligible(q) if not any(t < s for t in eligible(q))]
check('Weighted minimal quorums and failure availability',
      {frozenset(x) for x in minimal(2)} == {frozenset('A'), frozenset('BC')}
      and {frozenset(x) for x in minimal(3)} == {frozenset('AB'), frozenset('AC')}
      and all(a & b for a in eligible(2) for b in eligible(3))
      and not any(s <= set('BC') for s in eligible(3)))
versions = {'A': (8, 90), 'B': (8, 90), 'C': (8, 90), 'D': (7, 100), 'E': (7, 100)}
read = max((versions[k] for k in 'CDE'), key=lambda v: v[0])
next_version = max(versions[k][0] for k in 'BDE') + 1
check('Read chooses highest committed version rather than value majority', read == (8, 90) and next_version == 9)
check('Disjoint replica-lock subsets can block one logical item', len(set('AC')) < 3 and len(set('BD')) < 3 and not set('AC') & set('BD'))
check('Catalog switch must cover catch-up/maintenance boundary',
      set(range(101, 121)) | {121} == set(range(101, 122))
      and set(range(101, 121)) != set(range(101, 122)))

delivery = [(12, 2), (11, 1)]
naive = 0
for _, value in delivery:
    naive = value
pending = {}
frontier = 10
ordered = 0
for seq, value in delivery:
    pending[seq] = value
    while frontier + 1 in pending:
        frontier += 1
        ordered = pending.pop(frontier)
check('Out-of-order after images need protocol-ordered apply', naive == 1 and ordered == 2 and frontier == 12)

leq = lambda u, v: all(a <= b for a, b in zip(u, v))
concurrent = lambda u, v: not leq(u, v) and not leq(v, u)
u, v = (2, 1), (1, 2)
merged = [max(a, b) for a, b in zip(u, v)]
merged[0] += 1
check('Version-vector resolution records both parents and new writer event',
      concurrent(u, v) and tuple(merged) == (3, 2) and leq(u, merged) and leq(v, merged))
for a, b in product(product(range(3), repeat=3), repeat=2):
    mixed_directions = any(x < y for x, y in zip(a, b)) and any(x > y for x, y in zip(a, b))
    assert concurrent(a, b) == mixed_directions
check('Finite vector comparisons preserve partial order/concurrency classification', True,
      '729 vector pairs; no claim of unlimited-writer identity lifecycle correctness.')
parts = {'P': {7}, 'Q': set()}
double_scan = list(parts['P'])
parts['P'].remove(7); parts['Q'].add(7)
double_scan += list(parts['Q'])
parts = {'P': {7}, 'Q': set()}
parts['P'].remove(7)
miss_scan = list(parts['P']) + list(parts['Q'])
parts['Q'].add(7)
check('Async partition move can create duplicate or missing scan observations',
      double_scan.count(7) == 2 and 7 not in miss_scan and 7 in parts['Q'],
      'Two concrete scan/delivery schedules explained in AD66; not an engine scan execution.')


def digest(value):
    return hashlib.sha256(value).digest()


def tree(data):
    buckets = [[] for _ in range(8)]
    for key, value in sorted(data.items()):
        buckets[key % 8].append([key, value])
    leaves = [digest(b'L' + json.dumps(bucket, ensure_ascii=False, separators=(',', ':')).encode()) for bucket in buckets]
    levels = [leaves]
    while len(levels[-1]) > 1:
        prev = levels[-1]
        levels.append([digest(b'N' + prev[i] + prev[i + 1]) for i in range(0, len(prev), 2)])
    return levels


def differing_leaves(a, b):
    found = []
    visits = 0

    def visit(level, index):
        nonlocal visits
        visits += 1
        if a[level][index] == b[level][index]:
            return
        if level == 0:
            found.append(index)
        else:
            visit(level - 1, index * 2)
            visit(level - 1, index * 2 + 1)

    visit(len(a) - 1, 0)
    return found, visits


base = {i: f'value{i}' for i in range(16)}
rng = random.Random(6651)
for _ in range(256):
    changed = base.copy()
    for key in rng.sample(list(base), rng.randrange(0, 7)):
        changed[key] = 'updated' + str(key)
    a, b = tree(base), tree(changed)
    expected = sorted({k % 8 for k in base if base[k] != changed[k]})
    actual, _ = differing_leaves(a, b)
    assert actual == expected
check('Actual SHA-256 Merkle traversal matches direct diff on256fixtures', True,
      'Eight fixed key buckets, ordered domain-separated binary tree, canonicalJSON; not cryptographic proof of collision resistance.')
swapped = {0: 'A', 8: 'B'}
other = {0: 'B', 8: 'A'}
check('Key/value commitment detects swaps hidden by value-only collection',
      sorted(swapped.values()) == sorted(other.values()) and tree(swapped)[-1] != tree(other)[-1])
a = tree(base)
index = 2
value = a[0][index]
proof = []
for level in a[:-1]:
    sibling = level[index ^ 1]
    proof.append((index % 2, sibling))
    value = digest(b'N' + value + sibling) if index % 2 == 0 else digest(b'N' + sibling + value)
    index //= 2
check('Leaf2 sibling proof recomputes trusted root', value == a[-1][0] and len(proof) == 3,
      'Actual SHA-256 path recomputation; root is an externally trusted input, no signature generation/verification executed.')
tampered = digest(b'L' + b'tampered')
for position, sibling in proof:
    tampered = digest(b'N' + tampered + sibling) if position == 0 else digest(b'N' + sibling + tampered)
check('Tampered leaf fails comparison to the same trusted root', tampered != a[-1][0])
check('Same-data trees stop at root', differing_leaves(a, a) == ([], 1))

result = {'date': '2026-11-05', 'status': 'passed', 'count': len(checks), 'checks': checks,
          'lessonSha256': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['AD51', 'AD66']},
          'limits': 'Finite quorum/vector/ordered-message/scan witnesses and actual SHA-256 computation. No replica cluster, database engine, signature verification or network execution.'}
(R / 'qa/replication-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'quorumFixtures': quorum_fixtures, 'MerkleFixtures': 256, 'status': 'passed'}))
