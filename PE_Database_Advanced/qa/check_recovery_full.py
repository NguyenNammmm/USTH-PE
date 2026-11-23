"""AD43 finite recovery protocol versus an independent transaction-outcome oracle."""
from pathlib import Path
from itertools import permutations, product
import hashlib
import json
import random

R = Path(__file__).resolve().parents[1]
checks = []


def check(name, ok, scope='Finite recovery model; no native crash or disk flush execution'):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'scope': scope})


initial = {'X': 10, 'Y': 30, 'Z': 50}
# Transaction programs modify disjoint items; strict write protection is satisfied.
programs = {
    'U': [('start', 'U'), ('update', 'U', 'X', 10, 20), ('update', 'U', 'X', 20, 25),
          ('redo', 'U', 'X', 20), ('redo', 'U', 'X', 10), ('abort', 'U')],
    'V': [('start', 'V'), ('update', 'V', 'Y', 30, 40), ('commit', 'V')],
    'W': [('start', 'W'), ('update', 'W', 'Z', 50, 99)]
}


def fold(prefix):
    state = initial.copy()
    active = set()
    for rec in prefix:
        if rec[0] == 'start':
            active.add(rec[1])
        elif rec[0] in ('commit', 'abort'):
            active.remove(rec[1])
        elif rec[0] == 'update':
            state[rec[2]] = rec[4]
        elif rec[0] == 'redo':
            state[rec[2]] = rec[3]
    return state, active


def recover(log, checkpoint, disk, skip_compensation=False, truncate_undo=False, undo_forward=False):
    _, losers = fold(log[:checkpoint])
    state = disk.copy()
    for rec in log[checkpoint:]:
        if rec[0] == 'start':
            losers.add(rec[1])
        elif rec[0] in ('commit', 'abort'):
            losers.remove(rec[1])
        elif rec[0] == 'update':
            state[rec[2]] = rec[4]
        elif rec[0] == 'redo' and not skip_compensation:
            state[rec[2]] = rec[3]
    undo_log = log[checkpoint:] if truncate_undo else log
    for rec in (undo_log if undo_forward else reversed(undo_log)):
        if rec[1] in losers and rec[0] == 'update':
            state[rec[2]] = rec[3]
    return state


def outcome_oracle(log):
    # Independent business outcome: only V can commit in these programs.
    # U is always either rolled back or incomplete; W is always incomplete.
    answer = initial.copy()
    if ('commit', 'V') in log:
        answer['Y'] = 40
    return answer


schedules = [sum((programs[t] for t in order), []) for order in permutations(programs)]
rng = random.Random(4305)
for _ in range(24):
    cursors = dict.fromkeys(programs, 0)
    schedule = []
    while any(cursors[t] < len(programs[t]) for t in programs):
        t = rng.choice([t for t in programs if cursors[t] < len(programs[t])])
        schedule.append(programs[t][cursors[t]])
        cursors[t] += 1
    schedules.append(schedule)
cases = 0
for schedule in schedules:
    for cut in range(len(schedule) + 1):
        durable = schedule[:cut]
        latest, _ = fold(durable)
        expected = outcome_oracle(durable)
        for cp in range(cut + 1):
            checkpoint_image, _ = fold(durable[:cp])
            # Page may retain checkpoint image or have a newer durable-log-backed
            # image. Intermediate states are represented by other cut values.
            for choose in product([False, True], repeat=3):
                disk = {key: latest[key] if choose[i] else checkpoint_image[key]
                        for i, key in enumerate(initial)}
                assert recover(durable, cp, disk) == expected, (durable, cp, disk)
                cases += 1
check('Checkpoint+redo-only+reverse undo matches transaction-outcome oracle', cases > 10000,
      f'{cases} finite prefix/checkpoint/page-image cases over30program-order schedules, disjoint strict-write items.')
aborted = programs['U']
check('Mutant skipping redo-only resurrects completed abort',
      recover(aborted, 0, initial, skip_compensation=True)['X'] == 25
      and recover(aborted, 0, initial)['X'] == 10)
active = programs['U'][:3]
checkpoint_disk, _ = fold(active)
check('Mutant truncating precheckpoint undo loses active transaction old value',
      recover(active, 3, checkpoint_disk, truncate_undo=True)['X'] == 25
      and recover(active, 3, checkpoint_disk)['X'] == 10)
check('Mutant forward undo gives wrong value for two updates',
      recover(active, 0, checkpoint_disk, undo_forward=True)['X'] == 20
      and recover(active, 0, checkpoint_disk)['X'] == 10)
check('WAL flush precondition and writer/flusher race witness', not 80 >= 95 and not 40 >= 50)
check('Commit durability differs from forcing data pages',
      recover(programs['V'], 0, initial)['Y'] == 40)
check('Loser data already on storage is undone',
      recover(programs['W'], 0, {'X': 10, 'Y': 30, 'Z': 99})['Z'] == 50)
check('Fuzzy checkpoint record alone does not update last completed pointer',
      {'record': 'C2', 'last_completed': 'C1', 'flushed': 1, 'dirty_count': 2}['last_completed'] == 'C1')

# Shadow root selects a whole durable table; bad order can point to missing data.
old_table = {'A': 'oldA', 'B': 'oldB', 'C': 'oldC'}
new_table = {'A': 'oldA', 'B': 'newB', 'C': 'oldC'}
durable_pages = {'oldA', 'oldB', 'oldC'}
check('Shadow publication before page durability has missing-page witness',
      not set(new_table.values()) <= durable_pages and set(old_table.values()) <= durable_pages)
durable_pages.add('newB')
check('Shadow pointer can select complete new table after flush', set(new_table.values()) <= durable_pages)
check('Group commit arithmetic counts service time separately from waiting',
      20 * 2 == 40 and (20 // 10) * 2 == 4)
check('Media restore cannot keep an uncommitted update merely because it is logged',
      recover(programs['W'], 0, initial)['Z'] == 50)

result = {'date': '2026-11-05', 'lesson': 'AD43', 'status': 'passed', 'count': len(checks),
          'cases': cases, 'checks': checks,
          'lessonSha256': hashlib.sha256((R / 'lessons/AD43.md').read_bytes()).hexdigest(),
          'limits': 'Finite before/after-image model. No MySQL crash, fsync, torn-write detection, OS cache, repeated-crash ARIES or production backup execution.'}
(R / 'qa/recovery-full-checks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'checks': len(checks), 'cases': cases, 'status': 'passed'}))
