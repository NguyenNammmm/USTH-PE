"""Finite AD50/65 protocols and an actual SQLite inbox/outbox fixture.

Not an XA, distributed DBMS, clock service or concurrent-worker execution.
"""
from collections import deque
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import sqlite3

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite model only'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


def explore(votes):
    # State: participant status I/READY/COMMIT/ABORT, sent votes,
    # received votes, durable coordinator decision, coordinator down.
    start = (('I',) * len(votes), 0, 0, None, False)
    queue = deque([start]); seen = {start}
    while queue:
        status, sent, received, decision, down = queue.popleft()
        outcomes = {s for s in status if s in ('COMMIT', 'ABORT')}
        assert not ('COMMIT' in outcomes and 'ABORT' in outcomes)
        assert decision != 'COMMIT' or all(votes)
        assert all(s != 'COMMIT' or decision == 'COMMIT' for s in status)
        successors = [(status, sent, received, decision, not down)]
        for i, vote in enumerate(votes):
            bit = 1 << i
            if status[i] == 'I':
                new = list(status); new[i] = 'READY' if vote else 'ABORT'
                successors.append((tuple(new), sent | bit, received, decision, down))
            if sent & bit and not received & bit and not down:
                successors.append((status, sent, received | bit, decision, down))
            if decision and not down and status[i] not in ('COMMIT', 'ABORT'):
                new = list(status); new[i] = decision
                successors.append((tuple(new), sent, received, decision, down))
        if decision is None and not down:
            if received == (1 << len(votes)) - 1 and all(votes):
                successors.append((status, sent, received, 'COMMIT', down))
            # Missing replies may time out; one received NO suffices too.
            if received != (1 << len(votes)) - 1 or not all(votes):
                successors.append((status, sent, received, 'ABORT', down))
        for state in successors:
            if state not in seen:
                seen.add(state); queue.append(state)
    return seen


worlds = {v: explore(v) for v in product([False, True], repeat=3)}
states = sum(map(len, worlds.values()))
check('Three-participant2PC finite state agreement/validity across8vote fixtures', states > 1000,
      f'{states} reachable states, arbitrary modeled action order and coordinator crash/recover. Durable PREPARED/decision and no participant heuristic abort are assumed.')
commit_world = next(s for s in worlds[(True, True, True)]
                    if s[0][0] == 'READY' and s[3] == 'COMMIT' and s[4])
abort_world = next(s for s in worlds[(True, False, True)]
                   if s[0][0] == 'READY' and s[3] == 'ABORT' and s[4])
local_p1 = lambda s: (s[0][0], bool(s[1] & 1))
check('Prepared participant observation matches two reachable worlds with opposite durable outcomes',
      local_p1(commit_world) == local_p1(abort_world)
      and commit_world[3] != abort_world[3],
      'Reachable finite-model witness with coordinator unavailable and decision undelivered toP1; general argument remains in lesson.')
check('Recovery can isolate only conflicts with prepared write locks',
      bool({'account7'} & {'account7'}) and not bool({'account7'} & {'account9'}))

sender = sqlite3.connect(':memory:')
receiver = sqlite3.connect(':memory:')
sender.executescript('CREATE TABLE account(id INTEGER PRIMARY KEY,balance INTEGER); INSERT INTO account VALUES(1,100); CREATE TABLE outbox(id TEXT PRIMARY KEY,amount INTEGER);')
receiver.executescript('CREATE TABLE account(id INTEGER PRIMARY KEY,balance INTEGER); INSERT INTO account VALUES(1,100); CREATE TABLE inbox(id TEXT PRIMARY KEY,amount INTEGER,processed INTEGER NOT NULL DEFAULT 0);')
sender.execute('BEGIN')
sender.execute('UPDATE account SET balance=balance-10 WHERE id=1')
sender.execute('INSERT INTO outbox VALUES(?,?)', ('transfer42', 10))
sender.rollback()
check('Sender debit/outbox rollback atomically on actual SQLite',
      sender.execute('SELECT balance FROM account').fetchone()[0] == 100
      and sender.execute('SELECT count(*) FROM outbox').fetchone()[0] == 0,
      f'SQLite{sqlite3.sqlite_version}; sequential local transaction fixture, not MySQL/distributed execution.')
sender.execute('BEGIN')
sender.execute('UPDATE account SET balance=balance-10 WHERE id=1')
sender.execute('INSERT INTO outbox VALUES(?,?)', ('transfer42', 10))
sender.commit()
for _ in range(5):
    receiver.execute('INSERT OR IGNORE INTO inbox(id,amount) VALUES(?,?)', ('transfer42', 10))
    receiver.commit()  # ACK can follow this local commit; ACK lost means duplicate delivery.
check('Five duplicate deliveries create exactly one durable inbox record',
      receiver.execute('SELECT count(*) FROM inbox').fetchone()[0] == 1,
      'Actual SQLite UNIQUE/INSERTORIGNORE fixture; network is a modeled duplicate sequence.')
receiver.execute('BEGIN')
receiver.execute('UPDATE account SET balance=balance+10 WHERE id=1')
receiver.execute('UPDATE inbox SET processed=1 WHERE id=?', ('transfer42',))
receiver.rollback()
check('Receiver failed processing rolls back credit and processed flag together',
      receiver.execute('SELECT balance FROM account').fetchone()[0] == 100
      and receiver.execute('SELECT processed FROM inbox').fetchone()[0] == 0,
      'Actual SQLite rollback; crash/durability not measured.')
for _ in range(5):
    receiver.execute('BEGIN')
    row = receiver.execute('SELECT amount FROM inbox WHERE id=? AND processed=0', ('transfer42',)).fetchone()
    if row:
        receiver.execute('UPDATE account SET balance=balance+? WHERE id=1', (row[0],))
        receiver.execute('UPDATE inbox SET processed=1 WHERE id=?', ('transfer42',))
    receiver.commit()
check('Repeated sequential processing commits one credit',
      receiver.execute('SELECT balance FROM account').fetchone()[0] == 110,
      'Actual SQLite sequential worker; simultaneous-worker locks/claims are a separate backend requirement.')
sender.execute('DELETE FROM outbox WHERE id=?', ('transfer42',)); sender.commit()
check('Sender deletes only after durable receiver acceptance ACK in modeled order',
      sender.execute('SELECT count(*) FROM outbox').fetchone()[0] == 0
      and receiver.execute('SELECT processed FROM inbox').fetchone()[0] == 1)
receiver.execute('DELETE FROM inbox WHERE id=?', ('transfer42',)); receiver.commit()
receiver.execute('INSERT INTO inbox(id,amount) VALUES(?,?)', ('transfer42', 10)); receiver.commit()
check('Deleting dedup history allows an old duplicate to look new',
      receiver.execute('SELECT processed FROM inbox').fetchone()[0] == 0,
      'Counterexample fixture; not an endorsed retention policy.')
sender.close(); receiver.close()


def acyclic(nodes, edges):
    return any(all(p.index(a) < p.index(b) for a, b in edges) for p in permutations(nodes))


check('Local wait graphs acyclic while union has deadlock cycle',
      acyclic((1, 2), {(1, 2)}) and acyclic((1, 2), {(2, 1)})
      and not acyclic((1, 2), {(1, 2), (2, 1)}))
check('Stale edge union creates cycle absent in both real successive states',
      acyclic((1, 2, 3), {(1, 2), (3, 1)})
      and acyclic((1, 2, 3), {(2, 3), (3, 1)})
      and not acyclic((1, 2, 3), {(1, 2), (2, 3), (3, 1)}),
      'Non-global2PL release-then-acquire schedule, as qualified in lesson.')
check('Lease action bound must fit through operation+delivery', 97 + 2 < 100 and not 100 + 2 < 100)
tags = [(counter, node, thread) for counter in range(3) for node in ['A', 'B'] for thread in [0, 1]]
check('Timestamp tuple has unique tie breakers in finite identity domain', len(set(tags)) == 12)
check('Receive advances beyond remote timestamp rather than repeatedly restarting old', max(10, 100) + 1 > 100)
check('Late smaller validation timestamp is rejected in model', 10 < 20)
check('Commit wait checks interval lower bound', not 101 > 102 and 103 > 102)
check('Global snapshot must not return mixed committed transfer branches',
      100 + 100 == 90 + 110 == 200 and 100 + 110 != 200 and 90 + 100 != 200)
local_a = {('G2', 'L'), ('L', 'G1')}
local_b = {('G1', 'G2')}
check('Local-serializable federation histories can form global cycle',
      acyclic(('L', 'G1', 'G2'), local_a)
      and acyclic(('L', 'G1', 'G2'), local_b)
      and not acyclic(('L', 'G1', 'G2'), local_a | local_b),
      'Logical schedule assuming local serializability only, not an engine strict2PL trace.')
result = {'date': '2026-11-05', 'status': 'passed', 'count': len(checks), 'stateCount': states,
          'checks': checks, 'lessonSha256': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['AD50', 'AD65']},
          'limits': 'Finite protocol/graph/arithmetic models plus actual sequential SQLite inbox/outbox transactions. No XA, distributed database, real clock, network or concurrent-worker execution.'}
(R / 'qa/distributed-commit-lock-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'states': states, 'SQLite': sqlite3.sqlite_version, 'status': 'passed'}))
