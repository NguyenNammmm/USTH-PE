from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
source = W / 'tmp/database-source/chapter-18.txt'
lines = source.read_text(encoding='utf-8').splitlines()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
texts = {}
for name in ['AD41', 'AD42']:
    path = R / 'lessons' / f'{name}.md'
    assert sha(path) == approved[name], 'Direct source/content rereview required'
    texts[name] = [p.strip() for p in path.read_text(encoding='utf-8-sig').split('\n\n') if p.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(texts[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    i, p = found[0]
    return {'path': f'lessons/{name}.md', 'lessonSha256': approved[name],
            'kind': kind, 'paragraph': i, 'exactOpening': p[:350]}


# Explicit reviewed semantic decisions; this is not a keyword coverage classifier.
items = {
 '18.5': ('AD41', 'Thay vì để transaction', 'Ví dụ 1: R(Q)', '1. Cho R(X)', '1. T25 đọc', 'Timestamp ordering selects serial order in advance, unlike runtime lock conflict ordering.'),
 '18.5.1': ('AD41', 'Timestamp có thể lấy', 'Mỗi transaction Ti có', '1. Cho R(X)', '1. T25 đọc', 'Unique fixed timestamps, clock/counter and restart distinction; per-item maximum read/write timestamps.'),
 '18.5.2': ('AD41', 'Mọi xung đột được basicTO', 'write(T,Q,value):', '6. So ba cách phục hồi', '6. Commit dependency', 'Complete read/write tests and updates, TS-order proof, starvation, all three recovery extensions and metadata/index phantom coverage.'),
 '18.5.3': ('AD41', 'Thomas cho một số lịch', 'Ví dụ 2: R(Q)', '5. Với `r1(Q)', '5. Có T1→T2', 'Ordered Thomas checks, obsolete request versus effective write, view equivalence all three conditions, blind write and non-conflict-serializable example.'),
 '18.6': ('AD41', 'Trong phiên bản hai điều kiện', 'T1 đọcA, tínhB', '7. T1 chỉ đọc;', '7. T1 bỏ write phase', 'Read/private-write, validation, optional write phase; three timestamps; textbook two-condition validator/proof versus explicitly separate parallel-write extension; subset histories, StartTS alternative, cascade/starvation.'),
 '18.7': ('AD42', 'Một phiên bản của item', 'Ví dụ 1: Q có', '1. Versions X:', '1. T20 đọc9', 'Version selection must preserve the intended order; logical metadata separated from physical undo/chain representation.'),
 '18.7.1': ('AD42', 'Nếu version có WTS=t', 'k = argmax version.WTS', '6. Q có version', '6. Snapshot6 cần', 'Content/WTS/RTS, all read/write decisions, interval boundaries, oldest-transaction GC, read metadata costs, no-read-wait scope and recovery limits.'),
 '18.7.2': ('AD42', 'Trong thuật toán §18.7.2', 'Ví dụ MV2PL thứ nhất', '4. Trace MV2PL', '4. U tạo hai version', 'Rigorous update locks, read-only ts-counter, infinity private versions, serialized atomic commit publication/proof, read-only GC and Note18.2 constraints/tombstone/index implications.'),
 '18.8': ('AD42', 'Snapshot isolation thường', 'Fixture on_call có', '2. Dựng write skew', '2. Ví dụ (1,1)', 'Committed snapshot and atomic whole-transaction publication, update validation distinct from serializability.'),
 '18.8.1': ('AD42', 'Trong mô hình SI của sách', 'Ví dụ: U,V cùng snapshot', '7. U,V cùng snapshot', '7. FUW:', 'StartTS/CommitTS, committed version timestamp and own-write workspace, reader visibility and atomic publication.'),
 '18.8.2': ('AD42', 'First-updater-wins xin', 'Ví dụ: U,V cùng snapshot', '7. U,V cùng snapshot', '7. FUW:', 'Concurrency interval and FCW version test, FUW lock/wait/recheck/abort outcomes, same-item lost update protection; disjoint writes limitation.'),
 '18.8.3': ('AD42', 'Trong kết quả mà sách', 'Trong mô hình hai bác sĩ', '8. Người học nói', '8. Chain Tin→P', 'Write skew/nonserializable serial counterexamples, current-state constraints, MAX+1 phantom, benefits/tradeoffs, SSI rw-dangerous structure not iff-cycle, alternative conflict/level strategies and fixed workload assumption.'),
 '18.9': ('AD42', 'Degree-two consistency hoặc', 'Một form web cho', '9. Dựng hai lịch', '9. Gặp hai lần:', 'Weak-consistency and interaction scope; none of the labels alone guarantees a serializable whole-result observation.'),
 '18.9.1': ('AD42', 'Degree-two yêu cầu', 'Một index scan còn', '9. Dựng hai lịch', '9. Gặp hai lần:', 'S read/X write, early S unlock and new locks with X held to outcome; no dirty read but nonrepeatable and duplicate/missed moved-key scan examples.'),
 '18.9.2': ('AD42', 'Cursor stability giữ', 'Một index scan còn', '9. Dựng hai lịch', '9. Gặp hai lần:', 'Current tuple shared protection, modified tuple X until outcome, no2PL serializability guarantee and application consistency responsibility.'),
 '18.9.3': ('AD42', 'Tách thời gian người dùng', 'Đó là optimistic control', '10. Hai form cùng', '10. Dùng dạng', 'Long user-think lock/snapshot retention, split short transactions, atomic compare/version-increment all writes, no read validation/snapshot or serializability guarantee, full read-set extension.')
}
allunits = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '18']
rows = []
for i, u in enumerate(allunits):
    if u['section'] not in items:
        continue
    name, e, x, q, a, judgment = items[u['section']]
    end = allunits[i + 1]['sourceLine'] - 1 if i + 1 < len(allunits) else u['scopeLineEnd']
    body = '\n'.join(lines[u['sourceLine'] - 1:end])
    rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
        'source': {'path': 'tmp/database-source/chapter-18.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256(body.encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[1040, 1349], [1350, 1927]],
                               'figurePagesVisuallyInspected': [893, 894, 898] if name == 'AD41' else [905, 909],
                               'baselineCredit': False, 'proofScope': 'Source protocol and current full lesson compared; finite models supplement explicit conditional proofs, not a formal proof assistant.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-algorithm'),
                     anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 16
result = {'date': '2026-11-05', 'scope': 'Five AD41 and eleven AD42 own-body units. No credit for other chapter18 sections.',
          'counts': {'assigned': 16, 'complete': 16}, 'units': rows,
          'checks': 'qa/timestamp-mvcc-full-checks.json:20 checks,90 TO shuffles,85 GC choices and actual sequential SQLite version-update scenario.',
          'sourceInterpretation': [
              'Figure18.20 accompanying edge prose reverses writer labels; lesson uses independently derived read-old-version to actual writer edges.',
              'Bank example final total arithmetic prose loses minus sign:100+200-200-200=-100. Authored example uses doctors with independently checked invariant.',
              'MVTO write: after excluding TS<RTS and same-version rewrite, TS>=RTS is sufficient for creation; do not omit equality with a reader that has the same transaction timestamp.',
              'Current product statements checked against primary docs; historical isolation-name/version claims not generalized.'
          ],
          'primaryDocsChecked': [
              'https://www.postgresql.org/docs/18/transaction-iso.html',
              'https://dev.mysql.com/doc/refman/8.4/en/innodb-multi-versioning.html'
          ]}
(O / 'semantic-timestamp-mvcc.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Timestamp/MVCCsourceunits', len(rows))
