from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
src = W / 'tmp/database-source/chapter-23.txt'
lines = src.read_text(encoding='utf-8').splitlines()
texts = {}
for name in ['AD52', 'AD62']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct source/current lesson rereview required'
    texts[name] = [x.strip() for x in p.read_text(encoding='utf-8-sig').split('\n\n') if x.strip()]


def anchor(name, needle, kind):
    found = [(i + 1, p) for i, p in enumerate(texts[name]) if needle in p]
    assert len(found) == 1, (name, needle, len(found))
    i, p = found[0]
    return {'path': f'lessons/{name}.md', 'lessonSha256': approved[name],
            'kind': kind, 'paragraph': i, 'exactOpening': p[:350]}


items = {
 '23.7': ('AD52', 'Backup trong §23.7.1', 'Hai node cùng nghi', '6. Backup nhận', '6. Chưa đủ:', 'Backup versus election; authority and reconstructible durable state both needed after coordinator failure.'),
 '23.7.1': ('AD52', 'Backup trong §23.7.1', 'Mô tả “nhận cùng message”', '6. Backup nhận', '6. Chưa đủ:', 'Receive same ordered input, duplicate computation/state but no duplicate external grants; synchronization overhead versus fast takeover and otherwise recovering/aborting active transactions. Source architectural sketch qualified for ordering/durability/fencing.'),
 '23.7.2': ('AD52', '§23.7.2 mô tả', 'Ví dụ election thứ nhất', '4. Ba candidates', '4. Nếu vòng kế', 'Lease-service circularity, failure suspicion, numbered rounds, withdrawal/rejoin after failed high-ID candidate, randomized retry, majority membership, term stale-message handling and lease assumptions; stateful coordinator recovery not provided by election alone.'),
 '23.7.2.1': ('AD52', '§23.7.2.1 giới thiệu', 'Ví dụ một tablet', '6. Backup nhận', '6. Chưa đủ:', 'Coordination-service hierarchical small metadata/create-delete locking/watch interfaces and use cases; atomic operation/session/lease/reread contracts rather than equating a watch with authority.'),
 '23.8': ('AD52', 'State machine replication cần', 'Trong ví dụ Spanner', '7. Hai partition', '7. Không: còn thiếu', 'Consensus foundation for replicated fault-tolerant log, state machines and coordinator decisions, separated from atomic commit across participant groups.'),
 '23.8.1': ('AD52', 'Pha1: proposer gửi', 'Ví dụ 1: proposerP', '1. Năm acceptors', '1. Chọn X', 'One-decision versus committed-prefix log; majority agreement, lag/uncommitted suffixes and chosen versus learned; safety under crash/message loss, progress needs eventual communication/stability rather than unconditional asynchronous termination.'),
 '23.8.2': ('AD52', 'Xét ba acceptors', 'Giả sử proposal m,value X', '1. Năm acceptors', '1. Chọn X', 'Full two-phase Paxos promise/highest-accepted inheritance, unique ballot and stable metadata, lost learning/competing proposers, three concrete traces, induction safety argument and Multi-Paxos/reconfiguration boundary.'),
 '23.8.3': ('AD62', 'Mỗi node giữ currentTerm', 'Năm node S1..S5', '5. Follower có log', '5. Tới5:', 'Term/vote persistence and random election with log freshness; all AppendEntries fields, prefix match, conflict-only suffix replacement, follower matched-prefix apply bound, leader current-term majority commit rule, old-term counterexample and safety induction; membership/snapshot/read boundaries.'),
 '23.8.4': ('AD52', 'Lock manager cũng là', 'Ví dụ một log đã commit', '5. Thiết kế replicated', '5. Áp command', 'Deterministic state transition, same ordered committed input, matching applied-prefix equality, lock-table and key-value applications, return semantics, retry identity/external effects, partition groups and safe read requirements; source Figure23.10 state-label discrepancy corrected.'),
 '23.8.5': ('AD52', 'Đường phục hồi cần', 'Trong ví dụ Spanner', '7. Hai partition', '7. Không: còn thiếu', 'Replicate coordinator outcome plus participants prepared/lock state in per-partition consensus groups, new leader recovery before deciding, preserve existing decision and all-participant YES; nonblocking qualified by necessary quorums and eventual progress.'),
}
units = [u for u in load(O / 'source-section-inventory.json')['bookSections'] if u['chapter'] == '23']
rows = []
for i, u in enumerate(units):
    if u['section'] not in items:
        continue
    name, e, x, q, a, judgment = items[u['section']]
    end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
    rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
      'source': {'path': 'tmp/database-source/chapter-23.txt', 'sha256': sha(src),
                 'ownBodyLines': [u['sourceLine'], end],
                 'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
      'sourceReadEvidence': {'ownBodyRead': True,
        'readBatches': [[2000, 2132], [2133, 2271], [2272, 2371], [2372, 2475], [2476, 2591], [2592, 2711]],
        'figurePagesVisuallyInspected': [1185, 1188], 'baselineCredit': False,
        'scope': 'Direct complete remaining chapter23 own-bodies and current AD52/AD62 read; source figure pages viewed at full page scale.'},
      'semanticStatus': 'complete', 'contentComparison': judgment,
      'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-proof'),
                   anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 10
result = {'date': '2026-11-05', 'scope': 'Coordinator/election/consensus final ten own-bodies of chapter23 only.',
          'counts': {'assigned': 10, 'complete': 10}, 'units': rows,
          'checks': 'qa/consensus-full-checks.json:17 checks;8953 Paxos states/29878 transitions, bounded two-ballot model, selected Raft counterexamples and deterministic replay. No native/network consensus service execution.',
          'primaryDocsChecked': ['https://lamport.azurewebsites.net/pubs/paxos-simple.pdf', 'https://raft.github.io/raft.pdf'],
          'sourceInterpretation': [
            'Majority intersection alone is not Paxos safety: highest accepted value inheritance and durable promises are required; full induction written.',
            'Textbook nonblocking phrasing assumes necessary replica-group quorums and progress; a lost participant YES cannot be invented by coordinator consensus.',
            'Raft follower commit cap uses the newly matched prefix, not an unrelated conflicting local suffix; source condensed last-entry wording clarified with Figure2 of original Raft paper.',
            'Figure23.10 draws z=3 while command history writes z=2; authored replay computes z=2.',
            'Coordination-service API descriptions are conceptual teaching examples, not claims that a specific current product exposes precisely these session semantics.'
          ]}
(O / 'semantic-consensus.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Consensus source units', len(rows))
