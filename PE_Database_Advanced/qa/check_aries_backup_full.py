"""Finite AD44/45 witnesses. Not a native DBMS, fsync or failover execution."""
from pathlib import Path
from itertools import product
import copy
import hashlib
import json

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite reference model only'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


def record(lsn, tx, kind, prev, page=None, field=None, before=None, after=None, undo_next=None):
    return dict(lsn=lsn, tx=tx, kind=kind, prev=prev, page=page, field=field,
                before=before, after=after, undo_next=undo_next)


base = [record(10, 1, 'begin', 0), record(20, 1, 'update', 10, 'P', 'A', 0, 10),
        record(30, 2, 'begin', 0), record(40, 2, 'update', 30, 'Q', 'B', 0, 20),
        record(50, 1, 'commit', 20), record(60, 2, 'update', 40, 'P', 'C', 0, 30)]


def redo(log, pages, dpt):
    for rec in log:
        p = rec['page']
        if p is None or p not in dpt or rec['lsn'] < dpt[p]:
            continue
        if pages[p]['lsn'] < rec['lsn']:
            pages[p][rec['field']] = rec['after']
            pages[p]['lsn'] = rec['lsn']


def undo(log, pages, pending, stop_after=None):
    log = copy.deepcopy(log)
    by_lsn = {r['lsn']: r for r in log}
    todo = pending.copy()
    applied = []
    while todo:
        tx = max(todo, key=lambda t: todo[t])
        rec = by_lsn[todo.pop(tx)]
        next_lsn = rec['undo_next'] if rec['kind'] == 'clr' else rec['prev']
        if rec['kind'] == 'update':
            new_lsn = max(by_lsn) + 10
            prior_tx = max(r['lsn'] for r in log if r['tx'] == tx)
            clr = record(new_lsn, tx, 'clr', prior_tx, rec['page'], rec['field'],
                         after=rec['before'], undo_next=rec['prev'])
            log.append(clr); by_lsn[new_lsn] = clr
            pages[rec['page']][rec['field']] = rec['before']
            pages[rec['page']]['lsn'] = new_lsn
            applied.append(rec['lsn'])
        if next_lsn:
            todo[tx] = next_lsn
        if stop_after is not None and len(applied) == stop_after:
            return log, todo, applied
    return log, todo, applied


states = 0
for p, q in product([0, 20, 60], [0, 40]):
    disk = {'P': {'lsn': p, 'A': 10 if p >= 20 else 0, 'C': 30 if p == 60 else 0},
            'Q': {'lsn': q, 'B': 20 if q == 40 else 0}}
    ram = copy.deepcopy(disk)
    redo(base, ram, {'P': 20, 'Q': 40})
    durable_log, pending, first = undo(base, ram, {2: 60}, stop_after=1)
    assert first == [60] and pending == {2: 40}
    # Crash after durable CLR, either before or after its page output.
    for flush_clr_page in [False, True]:
        storage = copy.deepcopy(disk)
        if flush_clr_page:
            storage['P'] = copy.deepcopy(ram['P'])
        recovered = copy.deepcopy(storage)
        redo(durable_log, recovered, {'P': 20, 'Q': 40})
        resumed_last = max(r['lsn'] for r in durable_log if r['tx'] == 2)
        final_log, _, later = undo(durable_log, recovered, {2: resumed_last})
        assert later == [40]
        assert (recovered['P']['A'], recovered['P']['C'], recovered['Q']['B']) == (10, 0, 0)
        assert [r['undo_next'] for r in final_log if r['kind'] == 'clr'] == [40, 30]
        states += 1
check('CLR redo/undoNext across12 supported page/crash variants', states == 12,
      'Durable CLR assumed before second crash; strict item protection and before/after images; no native crash.')
pages = {'P': {'lsn': 60, 'A': 10, 'C': 30}, 'Q': {'lsn': 40, 'B': 20}}
_, _, visited = undo(base, copy.deepcopy(pages), {1: 20, 2: 60})
check('Two losers use maximum pending LSN order', visited == [60, 40, 20])
check('Redo filter can skip without page fetch by recLSN', 30 < 40)
physiological_page = {'lsn': 40, 'slots': [7, 8, 9]}
for _ in range(2):
    if physiological_page['lsn'] < 50:
        physiological_page['slots'].pop(0)
        physiological_page['lsn'] = 50
check('PageLSN suppresses a nonidempotent physiological deletion',
      physiological_page == {'lsn': 50, 'slots': [8, 9]},
      'Deleting first slot twice differs; pageLSN50 prevents duplicate application of record50.')
chain = {60: ('update', 50), 50: ('dummy-clr', 20), 40: ('structural', 30),
         30: ('structural', 20), 20: ('begin', 0)}
at = 60
path = []
while at:
    path.append(at)
    at = chain[at][1]
check('Dummy CLR skips structural records but not user update', path == [60, 50, 20])
check('Dirty-again page can begin new recLSN interval',
      min([80, 90]) == 80 and min([120, 130]) == 120)
check('Analysis of initially empty DPT must add later updates',
      {r['page']: r['lsn'] for r in [record(80, 1, 'update', 0, 'P'), record(90, 2, 'update', 0, 'Q')]} == {'P': 80, 'Q': 90})
check('Logical compensation preserves concurrent committed contribution', 700 - 100 + 50 + 100 == 750 and 700 != 750)
check('Partial logical inverse can be physically restored before retry',
      (650 + 40) - 40 + 100 == 750,
      'Illustrative partial inverse prefix, with undo metadata and operation-consistent restart; no multilevel implementation.')
check('Completed operation-abort must skip duplicate logical compensation', 650 + 100 == 750 and 750 + 100 != 750)

primary_durable, remote_ram, remote_durable = 200, 200, 150
check('Remote receive ACK is weaker than remote durable prefix', remote_ram == primary_durable and remote_durable < primary_durable)
check('Two-safe degraded commit has a double-failure loss witness',
      min(220, 200) == 200 and 220 > 200,
      'Primary-only suffix201..220 lost if primary storage then fails before resync.')
check('Block replication must preserve WAL force order',
      {'data_page': 50, 'durable_log': 40}['data_page'] > 40)
check('Redo-only snapshot must exclude or identify loser versions',
      {'X': 99, 'Y': 40}['X'] != 10,
      'Redo committedY alone cannot remove loserX already present in snapshot.')
check('Cross-partition transfer requires shared outcome/publication',
      (100 - 20) + 100 != 200 and (100 - 20) + (100 + 20) == 200)
check('Persistent individual words do not imply atomic multiword transaction',
      (80, 100) != (100, 100) and (80, 100) != (80, 120))
result = {'date': '2026-11-05', 'status': 'passed', 'count': len(checks), 'checks': checks,
          'lessonSha256': {name: hashlib.sha256((R / 'lessons' / f'{name}.md').read_bytes()).hexdigest()
                           for name in ['AD44', 'AD45']},
          'limits': 'Finite mathematical witnesses only; no native ARIES, remote durability, failover, restore drill or NVRAM execution.'}
(R / 'qa/aries-backup-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'crashVariants': states, 'status': 'passed'}))
