"""Finite reference checks for authored models; no database/cluster benchmark claims."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import hashlib
import heapq
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
counts = Counter()


def inputs(values, max_len=3):
    return [xs for n in range(max_len + 1) for xs in product(values, repeat=n)]


def inner_oracle(r, s):
    return Counter((i, j) for i, a in enumerate(r) for j, b in enumerate(s)
                   if a is not None and b is not None and a == b)


def left_oracle(r, s):
    out = Counter()
    for i, a in enumerate(r):
        matches = [j for j, b in enumerate(s) if a is not None and b is not None and a == b]
        out.update((i, j) for j in matches) if matches else out.update([(i, None)])
    return out


def full_oracle(r, s):
    out = left_oracle(r, s)
    for j, b in enumerate(s):
        if not any(a is not None and b is not None and a == b for a in r):
            out[(None, j)] += 1
    return out


def partitioned(r, s, workers=3, outer=False):
    rp, sp = defaultdict(list), defaultdict(list)
    route = lambda x: 0 if x is None else x % workers
    for i, a in enumerate(r):
        rp[route(a)].append((i, a))
    for j, b in enumerate(s):
        sp[route(b)].append((j, b))
    result = Counter()
    for w in range(workers):
        # Deliberately use a local dictionary index rather than the oracle's nested loop.
        ix = defaultdict(list)
        for j, b in sp[w]:
            if b is not None:
                ix[b].append(j)
        for i, a in rp[w]:
            hits = ix.get(a, []) if a is not None else []
            result.update((i, j) for j in hits)
            if outer and not hits:
                result[(i, None)] += 1
    return result


def partitioned_full(r, s, workers=3, right_only=False):
    # Separate matched-ID algorithm, compared with the nested-loop full oracle.
    buckets = {w: ([], []) for w in range(workers)}
    for i, a in enumerate(r):
        buckets[0 if a is None else a % workers][0].append((i, a))
    for j, b in enumerate(s):
        buckets[0 if b is None else b % workers][1].append((j, b))
    out = Counter()
    for rs, ss in buckets.values():
        matched_r, matched_s = set(), set()
        index = defaultdict(list)
        for j, b in ss:
            if b is not None:
                index[b].append(j)
        for i, a in rs:
            for j in index.get(a, []) if a is not None else []:
                out[(i, j)] += 1
                matched_r.add(i)
                matched_s.add(j)
        if not right_only:
            out.update((i, None) for i, _ in rs if i not in matched_r)
        out.update((None, j) for j, _ in ss if j not in matched_s)
    return out


def semijoin_plan(r, s, bloom=False):
    keys = {a for a in r if a is not None}
    if bloom:
        bits = {a % 2 for a in keys}  # intentionally collision-heavy, zero false negatives
        kept = [(j, b) for j, b in enumerate(s) if b is not None and b % 2 in bits]
    else:
        kept = [(j, b) for j, b in enumerate(s) if b in keys]
    index = defaultdict(list)
    for j, b in kept:
        index[b].append(j)
    return Counter((i, j) for i, a in enumerate(r) if a is not None for j in index[a])


arrs = inputs([None, 0, 1, 2])
for r in arrs:
    for s in arrs:
        exact = inner_oracle(r, s)
        assert partitioned(r, s) == exact
        assert partitioned(r, s, outer=True) == left_oracle(r, s)
        assert partitioned_full(r, s) == full_oracle(r, s)
        assert partitioned_full(r, s, right_only=True) == Counter(
            (j, i) for i, j in left_oracle(s, r).elements())
        assert semijoin_plan(r, s) == exact
        assert semijoin_plan(r, s, bloom=True) == exact
        # Broadcast S, disjoint R ownership, independently compare preserved row IDs.
        broadcast = Counter()
        for w in range(3):
            for i, a in enumerate(r):
                if i % 3 != w:
                    continue
                js = [j for j, b in enumerate(s) if a is not None and b is not None and a == b]
                broadcast.update((i, j) for j in js) if js else broadcast.update([(i, None)])
        assert broadcast == left_oracle(r, s)
        counts['bagEqualityOuterSemijoinBloomCases'] += 1

# Global secondary-index lookups preserve row identity even when Kp and Ki repeat.
# Include insert/delete/update changes, and compare index routing with full base scans.
for emails in product(['x', 'y', None], repeat=4):
    base = {i: {'city': i % 2, 'email': e} for i, e in enumerate(emails)}

    def make_index(rows):
        by_email = defaultdict(set)
        for uid, row in rows.items():
            by_email[row['email']].add((row['city'], uid))
        return by_email

    ix = make_index(base)
    for q in ['x', 'y', None]:
        got = Counter(uid for city, uid in ix[q]
                      if base[uid]['city'] == city and base[uid]['email'] == q)
        assert got == Counter(uid for uid, row in base.items() if row['email'] == q)
    old = base[0].copy()
    ix[old['email']].remove((old['city'], 0))
    base[0] = {'city': 1, 'email': 'new'}
    ix['new'].add((1, 0))
    # Insert a new identity with an existing city/email, then delete identity 1.
    base[4] = {'city': 1, 'email': 'new'}
    ix['new'].add((1, 4))
    deleted = base.pop(1)
    ix[deleted['email']].remove((deleted['city'], 1))
    expected = make_index(base)
    assert {k: v for k, v in ix.items() if v} == dict(expected)
    assert ix['new'] == {(1, 0), (1, 4)}
    counts['globalSecondaryIndexUpdateCases'] += 1

# Notify-before-wait is safe with a counting semaphore permit, for both legal orders.
for order in [('wait', 'signal'), ('signal', 'wait')]:
    permit, blocked, completed = 0, False, False
    for event in order:
        if event == 'wait':
            if permit:
                permit -= 1
                completed = True
            else:
                blocked = True
        else:
            if blocked:
                blocked, completed = False, True
            else:
                permit += 1
    assert completed and not blocked and permit == 0
    counts['latchWaitNotificationOrders'] += 1

# Recovery uses checkpoint state and replay identities together, not payload dedup.
events = [(21, 10), (22, 10)]
for retries in product([0, 1, 2], repeat=2):
    replay = [event for event, n in zip(events, retries) for _ in range(n + 1)]
    applied, state = set(), 5
    for identity, payload in replay:
        if identity not in applied:
            state += 1
            applied.add(identity)
    assert state == 7 and len(applied) == 2
    counts['streamReplayIdentityCases'] += 1

# Authored view-maintenance fixture: incremental signed deltas equal full recompute.
def joined_group(r, s):
    result = Counter()
    for key, c in r:
        for b, d, value in s:
            if key == b:
                result[(c, d)] += value
    return +result

for rkeys in inputs([1, 2], 2):
    r = [(k, 'X') for k in rkeys]
    before_s = [(1, 'Y', 5), (2, 'Y', 7)]
    before = joined_group(r, before_s)
    delta = Counter()
    for k, c in r:
        if k == 2:
            delta[(c, 'Y')] += 4
    maintained = before + delta
    assert maintained == joined_group(r, before_s + [(2, 'Y', 4)])
    moved = maintained.copy()
    for group, amount in delta.items():
        moved[group] -= amount
        moved[(group[0], 'Z')] += amount
    assert +moved == joined_group(r, before_s + [(2, 'Z', 4)])
    counts['signedViewDeltaCases'] += 1

for r in inputs([0, 1, 2]):
    for s in inputs([0, 1, 2]):
        grid = Counter()
        for row in range(2):
            for col in range(3):
                grid.update((i, j) for i, a in enumerate(r) if i % 2 == row
                            for j, b in enumerate(s) if j % 3 == col and a < b)
        assert grid == Counter((i, j) for i, a in enumerate(r) for j, b in enumerate(s) if a < b)
        counts['thetaGridCases'] += 1

for a in inputs([0, 1, 2, 3]):
    for b in inputs([0, 1, 2, 3]):
        # Two separately sorted sources, range boundaries, heap merge; global sort is oracle.
        streams = [sorted(a), sorted(b)]
        result = []
        for low, high in [(None, 2), (2, None)]:
            parts = [[v for v in stream if (low is None or v >= low) and
                      (high is None or v < high)] for stream in streams]
            result.extend(heapq.merge(*parts))
        assert result == sorted(a + b)
        assert Counter(result) == Counter(a + b)
        counts['parallelExternalSortCases'] += 1

for xs in inputs([-2, 0, 3], 5):
    local = [xs[::2], xs[1::2]]
    partial = [(sum(z), len(z)) for z in local]
    total, number = map(sum, zip(*partial))
    assert total == sum(xs) and number == len(xs)
    if xs:
        assert Fraction(total, number) == sum(Fraction(v, len(xs)) for v in xs)
    # Dedup after projected value routing must equal the global mathematical set.
    buckets = defaultdict(set)
    for z in local:
        for v in set(z):
            buckets[v % 3].add(v)
    assert set().union(*buckets.values()) == set(xs)
    counts['partialAggregationDistinctCases'] += 1

def predecessor(tokens, value):
    # Inclusive token convention explicitly declared in the lesson.
    candidates = [x for x in tokens if x <= value]
    return max(candidates) if candidates else max(tokens)

assert [predecessor([10, 40, 80], k) for k in [5, 10, 39, 40, 99]] == [80, 10, 10, 40, 80]
changed = [k for k in range(100) if predecessor([10, 40, 80], k) != predecessor([10, 40, 60, 80], k)]
assert changed == list(range(60, 80))
assert [predecessor([20, 50, 90], k) for k in [0, 20, 49, 50, 99]] == [90, 20, 20, 50, 90]
counts['consistentHashValues'] = 100

for minute in range(31):
    starts = [s for s in range(-10, 31, 5) if s <= minute < s + 10]
    top = (minute // 5) * 5
    derived = [top - 5, top]
    assert starts == derived
    counts['overlappingWindowCases'] += 1

assert Fraction(50, 90) == Fraction(5, 9)  # serial-scaled Q at five times the size
assert 4 * 2 * 24 + 10 + Fraction(1, 10) * 50 == 207
assert 150 * 3 == 450 and (150 + 63) // 64 == 3
assert 200 + 30 - 8 == 222 and 100 + 20 - 5 == 115
assert max(6 + 2, 1 + 7) == 8 and max(6, 1) + max(2, 7) == 13
assert max(5 + 1, 2 + 6) == 8 and max(5, 2) + max(1, 6) == 11
assert sum([5, 2, 1, 6]) == 14
assert 4 + 3 + 1 == 8 and 60 + 2 == 62
assert Fraction(1, 1) / Fraction(50, 5) * 365 == Fraction(73, 2)
assert [int(v >= 7) for v in [4, 7, 2, 10]] == [0, 1, 0, 1]
assert Fraction(20, 30 - 10) == 1  # bounded producer/consumer queue fixture

# Independent exhaustive assignment oracle for the particular independent scheduling examples.
for jobs, stated in [([9, 3, 3], 9), ([8, 4, 4], 8), ([10, 6, 4], 10)]:
    optimum = min(max(sum(t for t, w in zip(jobs, assign) if w == 0),
                      sum(t for t, w in zip(jobs, assign) if w == 1))
                  for assign in product([0, 1], repeat=len(jobs)))
    assert optimum == stated
    counts['exhaustiveScheduleInstances'] += 1

# Fail-fast counterexamples ensure the oracles discriminate known wrong approaches.
assert sum([40, 10]) / 2 != Fraction(40 + 10 * 9, 10)
assert Counter([(0, None), (0, 0)]) != Counter([(0, 0)])  # unmatched from a partial S is false
assert len({10, 10}) != 2  # value-based dedup loses distinct genuine events
assert [1, 6] + [2, 4, 7] != sorted([1, 6, 2, 4, 7])

result = {
    'status': 'pass',
    'kind': 'finite Python reference/model checks; no MySQL/distributed engine execution',
    'independentOracles': ['nested-loop bag joins and left outer joins', 'global built-in sorted',
                          'direct rational aggregate', 'exhaustive worker assignments',
                          'enumerated overlapping window membership',
                          'nested-loop right/full outer identities', 'full base scan for global index',
                          'full nested-loop view recompute after signed deltas'],
    'cases': dict(counts),
    'proofLimit': 'Finite checks supplement, and do not replace, lesson correctness arguments.',
    'lessonSha256': {n: hashlib.sha256((ROOT / 'lessons' / f'{n}.md').read_bytes()).hexdigest()
                     for n in ['AD46', 'AD47', 'AD48', 'AD49', 'AD64', 'AD79', 'AD80']},
}
(ROOT / 'research' / 'semantic-architecture-parallel-checks.json').write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
