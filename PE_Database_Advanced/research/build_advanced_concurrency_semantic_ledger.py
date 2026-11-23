from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
source = W / 'tmp/database-source/chapter-18.txt'
lines = source.read_text(encoding='utf-8').splitlines()
texts = {}
for name in ['AD28', 'AD63']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct rereview required'
    texts[name] = [x.strip() for x in p.read_text(encoding='utf-8-sig').split('\n\n') if x.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(texts[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    i, p = found[0]
    return {'path': f'lessons/{name}.md', 'lessonSha256': approved[name],
            'kind': kind, 'paragraph': i, 'exactOpening': p[:350]}


decisions = {
 '18.10': ('AD63', 'Với dữ liệu trên disk', 'Head trỏ A.', '1. Trace hai insert_head', '1. N1 thắng', 'Advanced control options motivated by index operation semantics, RAM costs, user interaction and deadlines; descendants assessed separately.'),
 '18.10.1': ('AD63', '§18.10.1 đưa một thuật toán', 'Ca1: snapshot có row1=A', '4. Với snapshot row1=A', '4. Sau replay index', 'All3online-build stages, final lock/catalog gap-free transition, delta invariant/termination assumptions, materialized view construction, tuple schema-version migration and online constraint validation.'),
 '18.10.2': ('AD28', 'Crabbing ở §18.10.2', 'B-link tree thêm right-sibling', '12. Index[10,20,30]', '12. Query14–16', 'Index operation serializability separate from transactions; exact source crabbing ascent/deadlock/restart, B-link all-level right links/changed parent handling, key-value/next-key including empty/end range, insert and delete successors.'),
 '18.10.3': ('AD63', 'Với dữ liệu trên disk', 'Một pop đơn giản đọc old head', '2. Dựng ABA', '2. ABA làm CAS', 'RAM latch cost/coarse granularity tradeoff, atomic CAS semantics and insertion algorithm, unsafe deletion ABA trace, tagged pointer/wrap and reclamation limits; library-use rationale and no native memory-order claim.'),
 '18.10.4': ('AD63', 'Năm yêu cầu trong sách', 'Ví dụ 3: hai người chỉnh', '5. Thiết kế workflow', '5. Rubric có autosave', 'All5long-duration properties, predictable response and recovery of human work, uncommitted draft exchange/subtasks, SI/optimistic-no-read-validation partial solutions and higher long-duration conflicts.'),
 '18.10.5': ('AD63', 'I ở bảng này là', 'Với tổng100, T1 cộng7', '6. Summary100', '6. Tổng lần lượt', 'Correctness versus selected invariant, daily summary commutative increment with atomic local step and I-mode compatibility, logical inverse versus physical restore/index shape, noncommuting conditional reservation and compensation.'),
 '18.10.6': ('AD63', 'Hard deadline bị trễ', 'Ví dụ 4: Tlow giữ lock', '5. Thiết kế workflow', '5. Rubric có autosave', 'Hard/firm/soft value semantics, deadline versus consistency, preemption rollback costs, RAM still variable, deadline-aware priority and conditional empirical OCC findings.')
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '18']
rows = []
for i, u in enumerate(units):
    if u['section'] not in decisions:
        continue
    name, e, x, q, a, judgment = decisions[u['section']]
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
        'source': {'path': 'tmp/database-source/chapter-18.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[1928, 2087], [2088, 2200], [2201, 2385], [2386, 2414]],
                               'figurePagesVisuallyInspected': [917, 918, 920, 922],
                               'baselineCredit': False, 'scope': 'Full own bodies and full current AD63 reviewed; full AD28 chapter14 content retained with79 exact old witnesses revalidated after concurrency-only additions.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-algorithm'),
                     anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 7
result = {'date': '2026-11-05', 'scope': 'Seven18.10own-body units only, distinct from48chapter14/index units.',
          'counts': {'assigned': 7, 'complete': 7}, 'units': rows,
          'checks': 'qa/advanced-concurrency-full-checks.json:15finite witnesses,24online-build schedules/cuts,49increment pairs; no native/SQL/real-time execution.'}
(O / 'semantic-advanced-concurrency.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Advanced concurrency source units', len(rows))
