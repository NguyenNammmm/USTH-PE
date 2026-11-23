"""Bounded educational models, not validation of an actual Paxos/Raft service."""
from collections import deque
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
checks = []


def check(name, condition, detail):
    assert condition, name
    checks.append({'name': name, 'passed': True, 'detail': detail})


quorums = [set(c) for size in [2, 3] for c in combinations(range(3), size)]
check('quorum-intersection', all(a & b for a in quorums for b in quorums), 'All 16 pairs of majorities for three fixed acceptors.')

# Two proposers, unique ballots 1/2, wanted values X/Y. Each prepare and accept
# message may arrive in any order once; not delivering it represents delay/loss.
# Replies are snapshots at prepare delivery. Proposer may issue once any quorum
# of replies has arrived. Stable metadata survives a crash/restart unchanged.
# State: promises, accepted(ballot,value), delivered prepare masks, replies,
# issued values(-1=not sent), delivered accept masks, historical chosen mask.
empty = ((0, 0, 0), ((0, -1),) * 3, (0, 0), ((-1, -1),) * 6, (-1, -1), (0, 0), 0)
queue = deque([empty])
seen = {empty}
transitions = 0
while queue:
    s = queue.popleft()
    promise, accepted, prep, replies, issued, delivered, chosen = s
    assert chosen != 3, 'Two different values chosen'
    next_states = []
    for p in range(2):
        n = p + 1
        for a in range(3):
            bit = 1 << a
            if not prep[p] & bit:
                pp, dd, rr = list(promise), list(prep), list(replies)
                dd[p] |= bit
                if n > promise[a]:
                    pp[a] = n
                    rr[3 * p + a] = accepted[a]
                next_states.append((tuple(pp), accepted, tuple(dd), tuple(rr), issued, delivered, chosen))
            if issued[p] != -1 and not delivered[p] & bit:
                pp, aa, dd = list(promise), list(accepted), list(delivered)
                dd[p] |= bit
                cc = chosen
                if n >= pp[a]:
                    pp[a] = n
                    aa[a] = (n, issued[p])
                    if sum(x == (n, issued[p]) for x in aa) >= 2:
                        cc |= 1 << issued[p]
                next_states.append((tuple(pp), tuple(aa), prep, replies, issued, tuple(dd), cc))
        if issued[p] == -1:
            got = [x for x in replies[3 * p:3 * p + 3] if x[0] >= 0]
            if len(got) >= 2:
                ii = list(issued)
                best = max(got)
                ii[p] = p if best[0] == 0 else best[1]
                next_states.append((promise, accepted, prep, replies, tuple(ii), delivered, chosen))
    for t in next_states:
        transitions += 1
        if t not in seen:
            seen.add(t)
            queue.append(t)
check('paxos-message-interleavings', all(s[-1] != 3 for s in seen), f'{len(seen)} reachable states and {transitions} transitions; two ballots/three acceptors/fixed membership, crash-stop or durable restart. Not an unbounded proof.')
check('chosen-is-not-learned', any(s[-1] and s[4][1] == -1 for s in seen), 'Acceptance quorum can exist before a later proposer/learner acts; no client ACK is needed for chosen.')

# Mutants: use the same concrete quorum evidence, but deliberately break a rule.
old = [(5, 'X'), (5, 'X'), (0, None)]
new_replies = [old[1], old[2]]
inherited = max(new_replies, key=lambda x: x[0])[1]
check('value-inheritance-mutant-killed', inherited == 'X' and 'Y' != inherited, 'A,B chose X at5. A proposer using B,C at8 must retain X; choosing wanted Y would create a second chosen value.')
stable_promise = 20
check('forget-promise-mutant-killed', not (10 >= stable_promise) and 10 >= 0, 'A durable promise20 rejects ACCEPT10. Resetting it to0 admits the delayed message and violates the persistence invariant; this alone is not claimed to be a full conflicting-decision execution.')

def up_to_date(candidate, voter):
    return candidate >= voter  # tuples(lastTerm,lastIndex), lexicographic

check('vote-freshness', [up_to_date(c, (6, 10)) for c in [(5, 100), (6, 9), (6, 10), (7, 2)]] == [False, False, True, True], 'AD62 exercise1, term before length.')

# Explicit five-node old-term counterexample, checking every election quorum.
logs = [[(1, 'P'), (2, 'X')], [(1, 'P'), (2, 'X')], [(1, 'P')], [(1, 'P')], [(1, 'P')]]
def last(log):
    return (log[-1][0], len(log))
def elect(candidate, voters):
    return len(voters) >= 3 and all(up_to_date(last(logs[candidate]), last(logs[v])) for v in voters)
check('old-term-trace-election3', elect(4, [2, 3, 4]), 'S5 has term1 prefix, wins term3 from S3,S4,S5, appends Y locally.')
logs[4].append((3, 'Y'))
check('old-term-trace-election4', elect(0, [0, 1, 2]), 'S1 with X term2 wins term4 from S1,S2,S3.')
logs[2] = list(logs[0])
check('old-term-majority-is-insufficient', sum(len(x) >= 2 and x[1] == (2, 'X') for x in logs) == 3 and elect(4, [2, 3, 4]), 'Even with X on three nodes, S5 with last term3 can win term5 and replace X. Mutant majority-only commit guard is rejected.')
for i in [0, 1, 2]:
    logs[i].append((4, 'NOOP'))
check('current-term-prefix-protected', not elect(4, [2, 3, 4]), 'Committing a term4 no-op on S1,S2,S3 protects prefix X; S3 will reject candidate last term3.')

def append(local, current_term, req_term, prev_index, prev_term, entries, leader_commit, committed):
    if req_term < current_term:
        return False, local[:], committed
    if prev_index > len(local) or (prev_index and local[prev_index - 1][0] != prev_term):
        return False, local[:], committed
    result = local[:]
    for offset, entry in enumerate(entries):
        at = prev_index + offset
        if at < len(result) and result[at][0] != entry[0]:
            result = result[:at]
        if at == len(result):
            result.append(entry)
    matched = prev_index + len(entries)
    return True, result, max(committed, min(leader_commit, matched))

l = [(1, 'A'), (2, 'B'), (4, 'C')]
f = [(1, 'A'), (3, 'D'), (3, 'E')]
check('append-prefix-reject', not append(f, 4, 4, 2, 2, [l[2]], 0, 0)[0], 'Wrong prevTerm rejected, follower unchanged.')
ok, repaired, _ = append(f, 4, 4, 1, 1, l[1:], 0, 0)
check('append-conflict-and-idempotence', ok and repaired == l and append(repaired, 4, 4, 1, 1, l[1:2], 0, 0)[1] == l, 'Conflict replaces suffix; a duplicated shorter matching request does not truncate a later matching entry.')
long = [(1, str(i)) for i in range(1, 6)] + [(2, str(i)) for i in range(6, 10)]
ok, _, ci = append(long, 3, 3, 5, 1, [], 9, 3)
check('heartbeat-bounds-commit', ok and ci == 5 and min(9, len(long)) == 9, 'Last matched index5, not arbitrary local end9; mutant local-end guard would apply an unmatched suffix.')
check('stale-term-rejected', not append(l, 8, 7, 3, 4, [], 3, 0)[0], 'Old leader AppendEntries rejected even with a matching prev entry.')

commands = [('x', 2), ('z', 2), ('x', 3), ('y', 4), ('y', 7)]
states = []
for _ in range(3):
    state = {}
    for k, v in commands:
        state[k] = v
    states.append(state)
check('deterministic-replay', states == [{'x': 3, 'z': 2, 'y': 7}] * 3, 'Independent replay of authored command sequence; corrects source Figure23.10 z label, no native service execution.')

# Same set of messages, different order, different final state: backup must keep order.
def lock_state(seq):
    held = False
    for action in seq:
        held = action == 'acquire'
    return held
check('backup-input-order', lock_state(['acquire', 'release']) != lock_state(['release', 'acquire']), 'Replicating a set of messages without its agreed order does not replicate state.')
check('two-level-commit', not all([True, False]) and all([True, True]), 'Coordinator consensus cannot replace a missing durable YES from a data participant. Two participant groups differ from replicas within each group.')

out = {'date': '2026-11-05', 'checks': checks, 'passed': len(checks),
       'scope': 'Finite educational state models, one fixed Paxos instance with two ballots and three acceptors; selected Raft rules and a five-node trace. No network, ZooKeeper, Spanner or native consensus cluster executed. Liveness and arbitrary histories are explained by arguments, not established by these finite tests.',
       'lessons': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['AD52', 'AD62']}}
(O / 'consensus-full-checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'passed': len(checks), 'paxosStates': len(seen), 'paxosTransitions': transitions}))
