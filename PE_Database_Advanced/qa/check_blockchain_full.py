"""Authored finite models and real local crypto/SQL operations, no blockchain node."""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import sqlite3
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

O = Path(__file__).resolve().parent
R = O.parent
checks = []
def check(name, ok, detail):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'detail': detail})
encode = lambda o: json.dumps(o, sort_keys=True, separators=(',', ':')).encode()
H = lambda x: hashlib.sha256(x).digest()

chain = []
for i in range(3):
    chain.append({'height': i, 'prev': H(encode(chain[-1])).hex() if chain else 'genesis', 'tx': [f't{i}']})
old_tip = H(encode(chain[-1]))
chain[1]['tx'] = ['changed']
check('hash-link-tamper', chain[2]['prev'] != H(encode(chain[1])).hex(), 'Real SHA256 detects middle block edit against unchanged successor.')
chain[2]['prev'] = H(encode(chain[1])).hex()
check('recomputed-chain-needs-anchor', old_tip != H(encode(chain[2])), 'Recomputed internally consistent history changes the authenticated tip; hashes alone do not select authority.')

leaves = [H(b'\x00' + encode(f't{i}')) for i in range(8)]
tree = [leaves]
while len(tree[-1]) > 1:
    x = tree[-1]
    tree.append([H(b'\x01' + x[i] + x[i + 1]) for i in range(0, len(x), 2)])
def verify(t, index, n, siblings, root):
    if n < 1 or n & (n - 1) or not 0 <= index < n or len(siblings) != n.bit_length() - 1:
        return False
    x = H(b'\x00' + encode(t))
    for s in siblings:
        x = H(b'\x01' + (x + s if index % 2 == 0 else s + x))
        index //= 2
    return x == root
for i in range(8):
    j = i; proof = []
    for level in tree[:-1]:
        proof.append(level[j ^ 1]); j //= 2
    assert verify(f't{i}', i, 8, proof, tree[-1][0])
    assert not verify('altered', i, 8, proof, tree[-1][0])
    assert not verify(f't{i}', i, 8, proof[:-1], tree[-1][0])
check('merkle-membership', True, '24 actual SHA256 positive/altered-message/short-proof checks for authored eight-leaf tree; not Bitcoin wire format.')

key = Ed25519PrivateKey.from_private_bytes(bytes(range(32)))  # disposable test key
pub = key.public_key()
tx = {'domain': 'PE-TOY-v1', 'inputs': ['g:0'], 'outputs': [['B', 6]], 'fee': 1}
sig = key.sign(encode(tx))
pub.verify(sig, encode(tx))
altered = dict(tx, outputs=[['C', 6]])
try:
    pub.verify(sig, encode(altered)); rejected = False
except InvalidSignature:
    rejected = True
check('signature-covers-recipient', rejected, 'Actual Ed25519 sign/verify for canonical entire toy message; changed recipient rejected. Not a blockchain signature implementation or a proof of real-world identity.')

def apply_utxo(u, txid, ins, outs, fee):
    if not ins or len(set(ins)) != len(ins) or any(i not in u for i in ins):
        return False, dict(u)
    if any(v < 0 for _, v in outs) or fee < 0 or sum(u[i][1] for i in ins) != sum(v for _, v in outs) + fee:
        return False, dict(u)
    result = {k: v for k, v in u.items() if k not in ins}
    for j, out in enumerate(outs):
        if (txid, j) in result:
            return False, dict(u)
        result[(txid, j)] = out
    return True, result
u = {('g', 0): ('A', 7), ('g', 1): ('A', 5)}
ok, u1 = apply_utxo(u, 'T1', [('g', 0), ('g', 1)], [('B', 10), ('A', 1)], 1)
ok2, u2 = apply_utxo(u1, 'T2', [('g', 0)], [('C', 6)], 1)
check('utxo-sequential-double-spend', ok and not ok2 and u2 == u1 and sum(v for _, v in u1.values()) == 11, '12 input, 11 remaining value plus fee1; second valid-signature transaction cannot spend deleted input.')
check('duplicate-input-mutant-killed', not apply_utxo({('g', 0): ('A', 7)}, 'B', [('g', 0), ('g', 0)], [('B', 14)], 0)[0], 'Duplicate outpoint must be rejected before summing; otherwise one value can be counted twice.')
check('partial-output-spend', apply_utxo(u, 'T3', [('g', 0)], [('B', 7)], 0)[1].get(('g', 1)) == ('A', 5), 'Index by outpoint preserves unspent second output of same transaction.')

fixtures = 0
for amount, out, fee in product(range(1, 9), range(9), range(9)):
    original = {('g', 0): ('A', amount)}
    ok, nxt = apply_utxo(original, 'N', [('g', 0)], [('B', out)], fee)
    assert ok == (amount == out + fee)
    assert sum(v for _, v in nxt.values()) == amount - (fee if ok else 0)
    fixtures += 1
check('utxo-conservation-grid', fixtures == 648, '648 finite value/output/fee comparisons; format, identity and signature preconditions assumed separately, not a crypto proof.')

quorum_pairs = 0
for f in range(4):
    n = 3 * f + 1; q = 2 * f + 1
    qs = [set(c) for c in combinations(range(n), q)]
    for a, b in product(qs, repeat=2):
        assert len(a & b) >= f + 1
        quorum_pairs += 1
check('byzantine-quorum-bound', quorum_pairs > 0, f'{quorum_pairs} quorum pairs for f0..3. Guarantees an honest intersection only with <=f Byzantine and correct locking rules; not a complete BFT protocol.')
check('pow-threshold-count', sum(h < 4 for h in range(256)) == 4 and sum(h <= 4 for h in range(256)) == 5, 'Actual enumeration of toy eight-bit outputs; expected trials64 versus51.2 under independent uniform trials.')
old_valid = set(range(11)); new_small = set(range(9)); new_large = set(range(13))
check('fork-validity-set', new_small < old_valid and not new_large <= old_valid, 'Toy max-transactions rules illustrate narrowing versus expanding validation set; activation/convergence not modeled.')
check('escrow-multisig', [len(set(x)) >= 2 for x in [('B', 'S'), ('B', 'A'), ('A',), ('A', 'A')]] == [True, True, False, False], 'Two distinct authorized signer identities, not number of signature strings; no delivery truth inferred.')

def account_step(bal, nonce, sender, recipient, amount, seq):
    if sender == recipient or amount <= 0 or nonce[sender] != seq or bal[sender] < amount:
        return False, dict(bal), dict(nonce)
    b, n = dict(bal), dict(nonce)
    b[sender] -= amount; b[recipient] += amount; n[sender] += 1
    return True, b, n
b = {'A': 8, 'B': 2, 'C': 0}; n = dict.fromkeys(b, 0); statuses = []
for t in [('A', 'B', 5, 0), ('B', 'C', 6, 0), ('A', 'C', 4, 1), ('A', 'B', 5, 0)]:
    ok, b, n = account_step(b, n, *t); statuses.append(ok)
check('account-nonce-and-replay', statuses == [True, True, False, False] and b == {'A': 3, 'B': 1, 'C': 6} and sum(b.values()) == 10, 'Actual authored state-transition trace, not Ethereum failure/fee semantics.')

db = sqlite3.connect(':memory:')
db.execute('CREATE TABLE events(height INTEGER,tx TEXT,asset TEXT,owner TEXT,status TEXT)')
db.executemany('INSERT INTO events VALUES(?,?,?,?,?)', [(1, 'a', 'Q1', 'A', 'accepted'), (2, 'b', 'Q2', 'A', 'accepted'), (3, 'c', 'Q1', 'B', 'accepted'), (4, 'd', 'Q2', 'C', 'rejected')])
rows = db.execute("WITH ranked AS (SELECT asset,owner,ROW_NUMBER() OVER(PARTITION BY asset ORDER BY height DESC,tx DESC) AS rn FROM events WHERE status='accepted') SELECT asset,owner FROM ranked WHERE rn=1 ORDER BY asset").fetchall()
check('actual-sql-read-model', rows == [('Q1', 'B'), ('Q2', 'A')], f'Executed SQLite{sqlite3.sqlite_version} window query on authored data. No SQL-to-blockchain or native-chain integration.')
wrong = db.execute('WITH ranked AS (SELECT asset,owner,ROW_NUMBER() OVER(PARTITION BY asset ORDER BY height DESC) AS rn FROM events) SELECT asset,owner FROM ranked WHERE rn=1 ORDER BY asset').fetchall()
check('rejected-event-query-mutant-killed', wrong != rows and wrong[-1] == ('Q2', 'C'), 'Dropping acceptance filter changes actual query result.')
db.close()

# Budget model: stage writes, publish only on success. Toy instruction costs.
def gas_run(budget):
    costs = [1, 2, 3] * 3; staged = 0
    for c in costs:
        if budget < c:
            return False, 0
        budget -= c; staged += 1
    return True, staged
check('gas-budget-atomicity', gas_run(17) == (False, 0) and gas_run(18) == (True, 9), 'Finite toy VM budget and rollback of staged business writes, not EVM fee schedule.')

out = {'date': '2026-11-05', 'passed': len(checks), 'checks': checks,
       'scope': 'Authored finite models, actual SHA256/Ed25519 computations and two SQLite query executions. No public/devnet blockchain, EVM, token, wallet, Byzantine network or oracle service was executed. No collision-resistance proof from these samples.',
       'lessons': {n: hashlib.sha256((R / 'lessons' / f'{n}.md').read_bytes()).hexdigest() for n in ['AD54', 'AD81', 'AD82']}}
(O / 'blockchain-full-checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'passed': len(checks), 'utxoFixtures': fixtures, 'bftQuorumPairs': quorum_pairs, 'sqlite': sqlite3.sqlite_version}))
