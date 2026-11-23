from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
source = W / 'tmp/database-source/chapter-18.txt'
lines = source.read_text(encoding='utf-8').splitlines()
lesson = R / 'lessons/AD40.md'
assert sha(lesson) == load(O / 'root-reviewed-snapshots.json')['lessons']['AD40'], 'Direct rereview needed'
paras = [p.strip() for p in lesson.read_text(encoding='utf-8-sig').split('\n\n') if p.strip()]


def anchor(needle, kind):
    matches = [(i + 1, p) for i, p in enumerate(paras) if needle in p]
    assert len(matches) == 1, (needle, len(matches))
    i, p = matches[0]
    return {'path': 'lessons/AD40.md', 'lessonSha256': sha(lesson), 'kind': kind,
            'paragraph': i, 'exactOpening': p[:350]}


decisions = {
    '18.2': ('Để xử lý, hệ thống có thể', 'T1 đang sửa tài khoản 1', '4. Thiết kế ca web', '4. Ca chờ dài',
             'Deadlock cycle definition; prevention versus detection/recovery with overhead and rollback tradeoffs.'),
    '18.2.1': ('Timestamp trong hai cách trên', 'Ví dụ ba: timestamps', '2. Timestamps10', '2. Wait-die:',
               'All-or-none lock acquisition, total resource ordering, wait-die/wound-wait roles, proofs, retained timestamps, timeout and starvation limits.'),
    '18.2.2': ('Manager thêm cạnh khi', 'Một snapshot lớn hơn', '1. Dựng graph', '1. T1→T2',
               'Maintain allocations/pending requests; detect cycle and perform recovery/queue recomputation.'),
    '18.2.2.1': ('Trong mô hình mỗi request', 'Một snapshot lớn hơn', '5. Graph có', '5. Cycle là',
                 'Directed wait-for graph versus conflict graph; exact cycle membership, detection cadence and DFS algorithm/complexity.'),
    '18.2.2.2': ('Có hai mức rollback', 'Chi phí còn gồm', '6. Lịch grant/update', '6. Quay về',
                 'Victim cost factors, total/partial rollback suffix and resumability requirements, starvation/rollback-count mitigation.'),
    '18.4': ('Trước hết xét `insert(Q)`', '`delete(Q)` xung đột', '7. Q tồn tại', '7. T20 bị',
             'Existence semantics for abstract insert/delete, distinct from SQL zero-row statement behavior.'),
    '18.4.1': ('`delete(Q)` xung đột', 'Với 2PL, delete cần', '7. Q tồn tại', '7. T20 bị',
               'Delete conflicts with read/write/delete/insert; X-lock and both timestamp rejection tests.'),
    '18.4.2': ('Với 2PL, delete cần', 'Q ban đầu chưa tồn tại', '7. Q tồn tại', '7. T20 bị',
               'Insert conflicts/existence, new-item exclusive lock, initialize both timestamps.'),
    '18.4.3': ('Giao thức index-leaf', 'Phantom cũng có thể', '8. Leaf L có key', '8. T1 giữ',
               'Predicate/membership conflicts from insert/update, metadata-item distinction, all index-leaf 2PL rules, empty range and false conflict, old/new update predicate checks; structural-index concurrency deferred explicitly.')
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '18']
rows = []
for i, u in enumerate(units):
    if u['section'] not in decisions:
        continue
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    body = '\n'.join(lines[u['sourceLine'] - 1:end])
    e, x, q, a, judgment = decisions[u['section']]
    rows.append({
        'section': u['section'], 'title': u['title'], 'owners': ['AD40'],
        'source': {'path': 'tmp/database-source/chapter-18.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256(body.encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[532, 710], [869, 1039]],
                               'figurePagesVisuallyInspected': [881],
                               'scope': 'Actual full own-body comparison and complete current AD40; no source credit outside these9 units.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(e, 'teaching'), anchor(x, 'worked-example-or-algorithm'),
                     anchor(q, 'activity'), anchor(a, 'answer')], 'gaps': []
    })
assert len(rows) == 9
result = {'date': '2026-11-05', 'scope': 'Nine AD40 own-body units; finite model checks plus previously recorded selected engine examples.',
          'units': rows, 'counts': {'assigned': 9, 'complete': 9},
          'checks': 'qa/deadlock-full-checks.json:12 finite checks including4096 graph states; no new engine execution.'}
(O / 'semantic-deadlocks.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Deadlock source units', len(rows))
