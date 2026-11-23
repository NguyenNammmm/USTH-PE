from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
source = W / 'tmp/database-source/chapter-19.txt'
lines = source.read_text(encoding='utf-8').splitlines()
texts = {}
for name in ['AD44', 'AD45']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct source/current lesson rereview required'
    texts[name] = [x.strip() for x in p.read_text(encoding='utf-8-sig').split('\n\n') if x.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(texts[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    i, p = found[0]
    return {'path': f'lessons/{name}.md', 'lessonSha256': approved[name], 'kind': kind,
            'paragraph': i, 'exactOpening': p[:350]}


items = {
 '19.7': ('AD45', 'Primary nhận transaction', 'Ví dụ 1: log primary', '5. Remote hỏng', '5. Chỉ có một bản', 'Remote separation/failure detection, safe transfer and reconnect/proxy/old-primarycatchup, hot-spare redo/undo, all3durability modes with degraded failure caveat, read-only replicas, NAS/SAN WAL ordering and application-tier availability.'),
 '19.8': ('AD44', 'Một index có thể split', 'Trace: O1 trừ100', '4. Trace O1 trừ100', '4. Trước rollback C=650', 'Early lower-level release invalidates restoring old page images after another operation changes it; logical compensation preserves other committed effects.'),
 '19.8.1': ('AD44', 'Ví dụ lower-level latch', 'Trace: O1 trừ100', '5. Một nhóm nói', '5. Khóa phải nhận diện', 'Operation-level conflicts/higher-key2PL versus short page locks, free-space/block structures and correct logical compensation conditions.'),
 '19.8.2': ('AD44', 'Cần phân biệt sơ đồ', 'Trong sơ đồ §19.8, **redo', '4. Trace O1 trừ100', '4. Trước rollback C=650', 'Operation uniqueID/begin, physical intermediate old/new, operation-end logical inverse; operation consistency and physical-only redo; nonidempotent logical operation distinction.'),
 '19.8.3': ('AD44', 'rollback scan ngược theo transaction:', 'Các update phát sinh trong', '4. Trace O1 trừ100', '4. Trước rollback C=650', 'Allnormal/incomplete/completed/operation-abort/start paths; per-transaction skip not othertransactions; partial inverse physical undo before retry, full logical inverse skip and termination.'),
 '19.8.4': ('AD44', 'Điều kiện concurrency của', 'Nếu O1 hoàn tất nhưng O2', '5. Một nhóm nói', '5. Khóa phải nhận diện', 'Original lower-level lock coverage must include later inverse conflicts; incompleteO2 physicalundo can overwrite logicalinverseO1; single-page physiological case versus multi-page analysis.'),
 '19.9': ('AD44', 'ARIES có thể log', 'Undo T2 bắt đầu60', '6. Một physiological record', '6. Xóa slot hai lần', 'Four ARIES differences:LSN/PageLSN,physiologicalredo,conservativeDPT and no-force fuzzy checkpoint; explicit complexity and separate simplified textbook record schemes.'),
 '19.9.1': ('AD44', 'LSN có thể được', 'Trong vận hành bình thường', '1. DPT[P]=40', '1. Bỏ30', 'File-offset LSN,PageLSN,PrevLSN,CLR/UndoNext,LastLSN,dirty/flush/redirtyRecLSN and complete checkpoint pointer; page latch and physiological idempotence. Exercise first uses no-fetch filter without inventing an inconsistent low storagePageLSN.'),
 '19.9.2': ('AD44', 'Khởi tạo từ checkpoint', 'Storage lúc crash có', '3. Tạo log hai losers', '3. Chấp nhận nhiều log', 'Analysis/redo/undo roles and their input/output tables; worked complete crash/restart trace.'),
 '19.9.2.1': ('AD44', 'Nếu DPT ở checkpoint rỗng', 'Storage lúc crash có', '8. DPT trong checkpoint', '8. Analysis scan phần', 'Load completed checkpoint; track outcomes/lastLSNs conservatively,add later dirtypages; initiallyemptyDPT not a stoppingrule; committednot-end distinct from loser.'),
 '19.9.2.2': ('AD44', 'Redo bắt đầu từ', 'for record theo thứ tự', '1. DPT[P]=40', '1. Bỏ30', 'Exact3redo filters including no-read DPT/recLSN filters and on-pageLSN; redohistoryincludingCLR and conditionalidempotence.'),
 '19.9.2.3': ('AD44', 'Đưa lastLSN của các losers', 'Undo T2 bắt đầu60', '3. Tạo log hai losers', '3. Chấp nhận nhiều log', 'MaxpendingLSN acrosslosers;normal inverse CLR/prev,existingCLRundoNext,control/endpaths,WALforcompensation and repeated-crash safety/conditionaltermination proof.'),
 '19.9.3': ('AD44', 'Các khả năng khác ở', 'Một dummy CLR có thể', '7. Trace user update60', '7. Undo60 ghi CLR', 'Nestedtopaction dummyCLRskip, recoveryindependence,savepoints,fineindexlocking,prefetch/outoforderwithpage/dependencyorderretained.'),
 '19.10': ('AD45', 'Nếu index hoàn toàn dựng lại', 'Một thiết kế redo-only', '7. Main-memory snapshot', '7. Chỉ redo V', 'RAMpersistentbaseline/logreload,indexredo omission withliveundo,redo-only committed/version snapshotconditions,parallelpartition dependencies;Note19.2NVRAMpersistenceversusatomicityandconditionalundo/redoavoidance.')
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '19']
rows = []
for i, u in enumerate(units):
    if u['section'] not in items:
        continue
    name, e, x, q, a, judgment = items[u['section']]
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
        'source': {'path': 'tmp/database-source/chapter-19.txt', 'sha256': sha(source),
                   'ownBodyLines': [u['sourceLine'], end],
                   'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
        'sourceReadEvidence': {'ownBodyRead': True, 'readBatches': [[983, 1124], [1125, 1300], [1301, 1436], [1437, 1557], [1558, 1721]],
                               'figurePagesVisuallyInspected': [961] if name == 'AD45' else [967, 969, 972, 975],
                               'baselineCredit': False, 'scope': 'Actual full source bodies and full current AD44/45; exact witnesses locate manually reviewed content.'},
        'semanticStatus': 'complete', 'contentComparison': judgment,
        'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-algorithm'),
                     anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 14
result = {'date': '2026-11-05', 'scope': 'Fourteen own-body units19.7–19.10; twelveAD44 and twoAD45.',
          'counts': {'assigned': 14, 'complete': 14}, 'units': rows,
          'checks': 'qa/aries-backup-full-checks.json:16finitechecks including12CLRcrashvariants; no nativeengine/failover/restore/SCMexecution.',
          'sourceInterpretation': [
              '19.7two-safe single-site fallback doesnotpromise survival of anotherstoragefailure before resync.',
              '19.8figure/prose has inconsistent sign forT1delta; authored arithmetic uses700-100+50+100=750 preserving othertransactiondelta.',
              'Source analysis description abbreviates end/outcome handling; current model explicitly retains durable committed winners, no blanketundo of committed-not-end.'
          ]}
(O / 'semantic-aries-backup.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('ARIES/backup source units', len(rows))
