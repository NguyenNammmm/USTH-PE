from pathlib import Path
import hashlib
import json

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
texts = {}
for name in ['AD54', 'AD81', 'AD82', 'AD59']:
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
 '26.1': ('AD81', 'Một ledger ngân hàng', 'Hai người cùng đưa', '4. Phản biện ba', '4. Hash công khai', 'Ledger/cryptocurrency/double-spend motivation; conditional trust, public versus permissioned membership and distinct read/submit/validate rights, pseudonymity rather than unconditional anonymity.'),
 '26.2': ('AD81', 'Genesis là block đầu', 'Trong **ca 1**', '5. Luật cũ', '5. Giới hạn8', 'Hash-linked blocks/genesis and need authenticated history; Sybil/fault/consensus families, full/light modes, accidental forks versus soft/hard validation-rule changes, source three historical examples, signatures and conditional claimed properties.'),
 '26.3': ('AD81', 'Một hash mật mã trả', 'Một ví dụ băm', '4. Phản biện ba', '4. Hash công khai', 'Cryptographic hash goals separated from database hashing; hash/signature/transaction state correctness not conflated.'),
 '26.3.1': ('AD81', 'Một hash mật mã trả', 'Một ví dụ băm', '4. Phản biện ba', '4. Hash công khai', 'Preimage/second-preimage/collision resistance, fixed output and unavoidable collisions, ideal work factors, small-domain guessing and canonical encoding; no false mathematical security proof for SHA.'),
 '26.3.2': ('AD81', 'Dùng giao diện `Sign', 'Trong **ca 3**', '4. Phản biện ba', '4. Hash công khai', 'Public/private key and signature verification purpose, all relevant message fields/domain signed, binding key to person and compromise conditions; source generic private-key-encryption description corrected to Sign/Verify API.'),
 '26.3.3': ('AD81', 'Ta dùng UTXO đơn giản', 'Trong **ca 3**', '3. Tình huống mới', '3. X rồi Y:', 'Input outpoint ownership/unspent/unique checks, outputs/change/fee and signature, local creation versus accepted-history ordering, explicit dependencies and implicit ordering control; full Apply pseudocode, conservation induction and complexity, conditional block rejection semantics.'),
 '26.4': ('AD54', '§26.4 phân biệt', 'Ví dụ 3:', '3. Thiết kế ca', '3. Ban đầu u', 'Proposer/fork-choice protocol families, independent full validation, mining incentive subsidy/fee/pool, validity versus consensus and crash versus Byzantine membership assumptions.'),
 '26.4.1': ('AD54', 'Với điều kiện `hash < T`', 'Ví dụ1 dùng toy', '5. Hash8 bit', '5. `<4`', 'Nonce challenge, strict/inclusive target probability and expected trials, puzzle friendliness versus collision resistance, finite nonce-space limit, difficulty/propagation/fork/energy/pool tradeoffs; accumulated-work qualified fork choice.'),
 '26.4.2': ('AD54', '§26.4.2 mô tả', 'Validator có thể ký', '4. Đánh giá ứng dụng', '4. Rubric chấp nhận', 'Stake/holding/locking and hybrid variations, proposal weight not richest-always or mandatory PoW, nothing-at-stake/old keys/checkpoint assumptions; source Ethereum transition forecast explicitly historical.'),
 '26.4.3': ('AD54', 'Byzantine node có thể', 'Ví dụ 2:', '2. N=7', '2. Phần giao', 'Arbitrary malicious/equivocating behavior versus crash, permissioning limitations, signature does not stop owner equivocation, PBFT fault bound and honest-quorum intersection proof, locking/view-change and synchrony/liveness caveats.'),
 '26.5': ('AD82', 'Gọi S0 là', 'Trong **ca 1**', '1. Tự trace', '1. ACCEPT, ACCEPT', 'History versus materialized current state/index and deterministic replay; authenticated state representation and search tradeoff, not merely copying every state to every block.'),
 '26.5.1': ('AD82', '§26.5.1 cần lookup', 'Trong **ca 1**', '5. Transaction g', '5. Cờ theo txid', 'UTXO lookup/index by output not whole transaction, verification fields, Merkle/light-client proof and authenticated-root/pruning/history boundaries, membership does not prove currently unspent.'),
 '26.5.2': ('AD82', 'Gọi S0 là', 'Trace ca 1', '1. Tự trace', '1. ACCEPT, ACCEPT', 'Account state/balance/nonce, persistent path-copy reuse of immutable subtrees and roots, MPT abstraction separated from exact protocol encoding; database-backed state query choices distinguished from commitments.'),
 '26.6': ('AD82', 'Smart contract có thể', 'Ví dụ multisig2-of-3', '4. Một đề xuất', '4. Index chỉ giảm', 'Executable stateful rules, language expressivity/resource/determinism and activation conditions, application correctness distinct from agreement.'),
 '26.6.1': ('AD82', 'Ba đại lượng trong', 'Ví dụ multisig2-of-3', '5. Transaction g', '5. Cờ theo txid', 'Limited script/escrow m-of-n versus Turing-complete language/halting, gas price/transaction/block budgets and abort caveats, toy budget proof, nonce/cross-account ordering and execution sandbox boundaries.'),
 '26.6.2': ('AD82', 'Đặc tả tốt phải', 'Một thiết bị phải', '3. Tình huống mới', '3. Chấp nhận nhiều', 'Oracle trust/identity/freshness/version, corrupt-but-valid signature, periodic recertification and dispute branches; logged external events need deduplication/finality and cannot rollback arbitrary physical effects.'),
 '26.6.3': ('AD82', 'Contract có account', 'Một contract được gọi', '3. Tình huống mới', '3. Chấp nhận nhiều', 'Contract account/balance/storage, user/contract activation and DAO governance, token-on-existing-chain with ERC20/721 distinction, historical other proposals/ICO reference, predesigned upgrades/control versus immutable code and no unsolicited execution.'),
 '26.6.4': ('AD82', 'Cross-chain thêm', 'Trace phản ví dụ:', '4. Một đề xuất', '4. Index chỉ giảm', 'Independent-chain atomicity versus local commits, trusted intermediary/relay versus hash-time-lock and proof/header validation, finality/orphan risk and timing assumptions; no unsupported universal atomic-swap guarantee.'),
 '26.7': ('AD82', 'Sách tách consensus', 'Trong mô hình chi phí', '4. Một đề xuất', '4. Index chỉ giảm', 'Consensus/state-access/execution components; distinct throughput/confirmation/query latency and serial cost example, source historical benchmark rates not current measurements.'),
 '26.7.1': ('AD82', 'Sharding chia dữ liệu', 'Ví dụ workload2PC', '4. Một đề xuất', '4. Index chỉ giảm', 'Shards/cross-shard coordination and smaller-validation-group attack risks; offchain batching/data availability/dispute/trust and periodicity versus settlement/finality tradeoffs.'),
 '26.7.2': ('AD82', 'Tách state-access engine', 'Một index `(asset,height)`', '2. Debug báo cáo', '2. Chọn dòng mới', 'Query optimizer visibility/trie access-path limits, external SQL/read-model indexing versus authenticated/versioned completeness, accepted latest-state query and stale-cache counterexample.'),
 '26.7.3': ('AD82', 'Ví dụ workload2PC', 'Sharding chia dữ liệu', '4. Một đề xuất', '4. Index chỉ giảm', 'Measure latency/throughput/progress under fault/attack, fixed data-participant scope versus replica/validator quorum growth, workload-preserving scaleup rather than nodes-always-faster.'),
 '26.8': ('AD82', '§26.8 là các hướng', '| Bằng cấp, bảng điểm', '3. Tình huống mới', '3. Chấp nhận nhiều', 'All12 source application classes with exact trust/input/privacy/query questions; historical deployment claims not presented as current fact; designs assessed against simpler signed/audited DB alternatives.'),
 'A.1': ('AD59', 'Appendix A.1 có 11', 'Time_slot_id trong mô hình', '1. Viết query phát', '1. Nhóm theo', 'All11 relation grains/keys/attributes/FK structure, weak section identity and no single-key TimeSlot FK, adaptation explicit12 physical tables not source dump.'),
 'A.2': ('AD59', 'Delete actions trong', 'Ví dụ `09:30`', '5. Đổi meeting', '5. `(9,30', 'Full PE DDL mirrors all source relation domains/delete policies, precise type/length/NULL differences and extra checks disclosed; two time representations, component ranges and source wrong-variable erratum, historical portability separated from current runner.'),
 'A.3': ('AD59', 'A.3 cho 5 Classroom', 'Những ca cần giữ', '3. Tự làm:', '3. NET cần', 'All printed source tables read and structurally parsed, cardinalities/zero-child/missing-advisor/repeated-course/NULL grade/time alternatives understood; original synthetic full-domain fixture and independent expected outputs provided, no raw source dataset redistributed.'),
}
inventory = load(O / 'source-section-inventory.json')['bookSections']
rows = []
for chapter, file in [('26', 'chapter-26.txt'), ('A', 'appendix-a.txt')]:
    src = W / 'tmp/database-source' / file
    lines = src.read_text(encoding='utf-8').splitlines()
    units = [u for u in inventory if u['chapter'] == chapter]
    for i, u in enumerate(units):
        name, e, x, q, a, judgment = items[u['section']]
        end = units[i + 1]['sourceLine'] - 1 if i + 1 < len(units) else u['scopeLineEnd']
        rows.append({'section': u['section'], 'title': u['title'], 'owners': [name],
          'source': {'path': f'tmp/database-source/{file}', 'sha256': sha(src),
                     'ownBodyLines': [u['sourceLine'], end],
                     'ownBodySha256': hashlib.sha256('\n'.join(lines[u['sourceLine'] - 1:end]).encode()).hexdigest()},
          'sourceReadEvidence': {'ownBodyRead': True, 'baselineCredit': False,
            'readBatches': [[1, 181], [182, 344], [345, 503], [504, 683], [684, 840], [841, 1010], [1011, 1169]] if chapter == '26' else [[1, 140], [136, 357], [358, 800], [801, 1196]],
            'figurePagesVisuallyInspected': [1284] if chapter == '26' else [1317, 1320, 1326, 1327],
            'scope': 'Direct full own-body/current lesson comparison, source diagrams inspected; AppendixA.3 ends before Index at line1196.'},
          'semanticStatus': 'complete', 'contentComparison': judgment,
          'evidence': [anchor(name, e, 'teaching'), anchor(name, x, 'worked-example-or-proof'),
                       anchor(name, q, 'activity'), anchor(name, a, 'answer')], 'gaps': []})
assert len(rows) == 26
result = {'date': '2026-11-05', 'scope': 'All23 chapter26 own-bodies and three AppendixA own-bodies only.',
          'counts': {'assigned': 26, 'complete': 26}, 'units': rows,
          'checks': ['qa/blockchain-full-checks.json:16named checks,648UTXO fixtures,14858BFT quorum pairs,actualSHA256/Ed25519 and selectedSQLite queries;nochain/VM execution.',
                     'qa/university-full-checks.json:17named checks,allsourceA.3tablesparsed,20time-rowequivalence,selectedactualSQLite DDL/FK/query cases;noMySQLtwo-session certification.'],
          'sourceInterpretation': ['Hash links do not independently choose common history; trust/majority claims qualified by fault model.',
            'Soft/hard fork defined by validation-rule compatibility, not merely historical block readability.',
            'Digital signatures are not universally private-key encryption; identity/private-key compromise and signed-field coverage explicit.',
            'Source generic PoS/work, Ethereum miner rates, portability and self-destruct descriptions are historical; no current protocol parameter claims borrowed from2019.',
            'Source time component CHECK contains start_hr/end_hr error, repaired explicitly.',
            'AppendixA.3 inventory scope corrected to exclude trailing book Index; source raw file unchanged.']}
(O / 'semantic-blockchain-university.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print('Blockchain/university source units', len(rows))
