from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
lesson = R / 'lessons/AD43.md'
assert sha(lesson) == load(O / 'root-reviewed-snapshots.json')['lessons']['AD43'], 'Direct rereview required'
paras = [x.strip() for x in lesson.read_text(encoding='utf-8-sig').split('\n\n') if x.strip()]
source = W / 'tmp/database-source/chapter-19.txt'
lines = source.read_text(encoding='utf-8').splitlines()


def anchor(needle, kind):
    found = [(i + 1, p) for i, p in enumerate(paras) if needle in p]
    assert len(found) == 1, (needle, len(found))
    i, p = found[0]
    return {'path': 'lessons/AD43.md', 'lessonSha256': sha(lesson), 'kind': kind,
            'paragraph': i, 'exactOpening': p[:350]}


items = {
 '19.1': ('Transaction failure có thể', 'Recovery có hai phần:', '9. Dump chứa X10', '9. U là loser', 'Logical versus system transaction error; fail-stop crash versus disk/media failure; prevention-time evidence and recovery-time actions.'),
 '19.2': ('Volatile storage như', 'Stable storage trong mô hình', '1. DurableLSN=80', '1. Không: durableLSN80', 'Three storage categories, independent failure modes and stable-storage approximation; descendants separate.'),
 '19.2.1': ('Trong mô hình hai bản', 'Ba ca: crash trước', '8. Shadow paging có', '8. Tạo B\'', 'Sequential two-copy write and checksum recovery outcomes, no double-loss guarantee, inflight-write nonvolatile metadata optimization; stable publication comparison activity.'),
 '19.2.2': ('Mô hình chia dữ liệu', 'Ví dụ disk có X=10', '5. Disk X10', '5. Sau tính local', 'Blocks, input/output, transaction workspace, read/write buffer transitions, dirty eviction versus durable output.'),
 '19.3': ('Recovery có hai phần:', 'Một giao dịch đã báo', '2. Ban đầu A=5', '2. Redo cho A7', 'Atomicity cannot be reconstructed from datafiles alone; log old/new evidence and shadow alternative covered under detailed descendant.'),
 '19.3.1': ('Sách biểu diễn update bằng', 'Note19.1 dùng một root', '8. Shadow paging có', '8. Tạo B\'', 'Log fields/start/commit/completed-abort, create before data modification; full Note19.1 shadow copy/paging, durable pages before atomic root, costs/concurrency limits.'),
 '19.3.2': ('Trong **immediate modification**', 'Ví dụ disk có X=10', '5. Disk X10', '5. Sau tính local', 'Local computation versus shared-buffer modification, immediate/deferred read-your-writes, old/new-image undo/redo and no-force/steal needs.'),
 '19.3.3': ('Để viết thuật toán rõ', 'Redo history đưa các item', '3. Một người đề xuất', '3. Undo thuận đặt', 'Write protection to outcome prevents physical undo overwriting committed successor; conceptual deferred SI/validation not a physical storage mandate.'),
 '19.3.4': ('WAL yêu cầu log cần', 'Đổi ví dụ thành log bền', '1. DurableLSN=80', '1. Không: durableLSN80', 'Durable commit record plus preceding required log, data page need not flush; missing durable outcome means rollback.'),
 '19.3.5': ('Phần redo lặp lại', 'Ban đầu X=10,Y=20.', '2. Ban đầu A=5', '2. Redo cho A7', 'Forward globally ordered redo including completed abort compensation; reverse undo, durable lifecycle classification and three crash-cut winner/loser cases.'),
 '19.3.6': ('Trình tự checkpoint đơn giản', 'Ví dụ checkpoint có L={U}', '6. Checkpoint hoàn tất', '6. Undo list khởi đầu', 'Stop updates, force log/pages then checkpointL; active/after transactions, precheckpoint loser start retention and conservative truncation; fuzzy distinguished.'),
 '19.4': ('Để theo sát §19.4', 'Ví dụ checkpoint có L={U}', '6. Checkpoint hoàn tất', '6. Undo list khởi đầu', 'Full textbook algorithm under held-write protection, normal and redo-only record types, precise completed checkpoint assumptions.'),
 '19.4.1': ('Để theo sát §19.4', 'Giả định về rollback trước', '3. Một người đề xuất', '3. Undo thuận đặt', 'Reverse normal-update undo, append restored-value redo-only, append abort at start, never undo compensation itself.'),
 '19.4.2': ('restart từ checkpoint hoàn tất:', 'Ví dụ checkpoint có L={U}', '6. Checkpoint hoàn tất', '6. Undo list khởi đầu', 'Initialize activeL; add starts/remove completed outcomes during redo; all histories replayed; reverse loser undo may cross checkpoint; compensation logging and finite termination proof.'),
 '19.4.3': ('Commit processing có thể group', 'Ví dụ mô hình một lần force', '9. Dump chứa X10', '9. U là loser', 'Group size/maxwait tradeoff and one-force ACK condition, flash-write reduction, sequential-client limit versus batching atomicity.'),
 '19.5': ('Log buffer giúp gom', 'Giả sử flusher đã thấy', '7. Fuzzy checkpoint C2', '7. Dùng C1', 'Implementation details of log/data buffering and checkpoint interplay, not a new recovery correctness assumption.'),
 '19.5.1': ('Với record kết hợp undo/redo', 'Ví dụ thứ nhất: log buffer', '1. DurableLSN=80', '1. Không: durableLSN80', 'Block aggregation preserving ordered durable prefix, all3log force requirements, undo-only minimal WAL nuance for separated streams and commit redo durability.'),
 '19.5.2': ('Giả sử flusher đã thấy', 'Background writer chủ động', '7. Fuzzy checkpoint C2', '7. Dùng C1', 'Force/no-force and steal/no-steal buffer capacity costs, page write/output latch-force-log-output-release protocol, transaction locks distinct and background dirty flushing.'),
 '19.5.3': ('Database quản lý buffer riêng', 'Đặt buffer trong virtual memory', '5. Disk X10', '5. Sau tính local', 'DB-owned buffer versus OS virtual memory flexibility, swap not database durability, possible swapout/swapin/DBoutput extra I/O; original state activity distinguishes output domains.'),
 '19.5.4': ('Đây là mô hình checkpoint có', 'Ví dụ thứ ba: checkpoint', '7. Fuzzy checkpoint C2', '7. Dùng C1', 'Textbook fuzzy dirty-list capture and last-completed checkpoint pointer only after all listed pages output; per-page WAL exclusion, distinct from ARIES no-force checkpoint.'),
 '19.6': ('Trong dump quiescent đơn giản', 'Sách mô tả đường restore', '9. Dump chứa X10', '9. U là loser', 'Quiescent dump force/copy/marker, partial block restore, archived log, SQL versus physical dump, online fuzzy costs; explicitly prevent uncommitted-redo/no-undo overgeneralization.')
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '19']
rows = []
for i, u in enumerate(units):
    if u['section'] not in items:
        continue
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    e, x, q, a, judgment = items[u['section']]
    rows.append({'section': u['section'], 'title': u['title'], 'owners': ['AD43'],
        'source': {'path': 'tmp/database-source/chapter-19.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[1, 155], [156, 340], [341, 518], [519, 661], [662, 801], [802, 982]],
                               'figurePagesVisuallyInspected': [940, 947, 949, 953], 'baselineCredit': False,
                               'scope': 'Direct full AD43 and every source own body through19.6. No19.7+credit.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(e, 'teaching'), anchor(x, 'worked-example-or-algorithm'),
                     anchor(q, 'activity'), anchor(a, 'answer')], 'gaps': []})
assert len(rows) == 21
result = {'date': '2026-11-05', 'scope': 'AD43:21own-body units19.1–19.6 only.',
          'counts': {'assigned': 21, 'complete': 21}, 'units': rows,
          'checks': 'qa/recovery-full-checks.json:12checks including18,720finite prefix/checkpoint/page-image cases and3invalid algorithm mutants.',
          'sourceInterpretation': 'Section19.6 simplified no-undo restore statement must not be used to replay uncommitted records blindly after a dump; lesson supplies a loser counterexample and requires committed-effect replay or full redo/undo protocol.'}
(O / 'semantic-recovery-basic.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Basic recovery source units', len(rows))
