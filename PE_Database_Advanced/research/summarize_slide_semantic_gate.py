"""Merge reviewed page judgments; source/witness freshness is not semantic proof.

No auto-credit from slide page map, a matching keyword, or the book gate.
"""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import unicodedata
from pypdf import PdfReader

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
digest = lambda s: hashlib.sha256(s.encode()).hexdigest()
sha_cache = {}
reader_cache = {}
def sha(p):
    p = Path(p).resolve()
    if p not in sha_cache:
        sha_cache[p] = hashlib.sha256(p.read_bytes()).hexdigest()
    return sha_cache[p]

def resolve(p):
    p = Path(p)
    if p.is_absolute():
        return p
    if p.parts and p.parts[0] == 'output':
        return W / p
    return R / p

def page_hash(path, number):
    path = str(Path(path).resolve())
    if path not in reader_cache:
        reader_cache[path] = PdfReader(path)
    text = reader_cache[path].pages[number - 1].extract_text()
    return digest(unicodedata.normalize('NFKC', text).replace('\u00ad', '').strip())

inventory = load(O / 'slide-page-map.json')['pages']
key = lambda path, n: (str(Path(path).resolve()).casefold(), int(n))
expected = {key(p['sourcePath'], p['pdfPage']): p for p in inventory}
candidates = defaultdict(list)
reports = []
for file in sorted(O.glob('semantic-slides-*.json')):
    if file.name.endswith('gate-summary.json'):
        continue
    data = load(file)
    rows = data.get('pages')
    if not isinstance(rows, list):
        continue
    reports.append(str(file.relative_to(R)).replace('\\', '/'))
    for row in rows:
        source = row.get('source', {})
        if not isinstance(source, dict):
            continue
        path, number = source.get('path'), source.get('pdfPage')
        if not path or not number or key(path, number) not in expected:
            continue
        issues = []
        sp = Path(path)
        if not sp.exists() or source.get('sha256') != sha(sp):
            issues.append('source PDF hash missing/mismatched')
        elif source.get('pageTextSha256') and source['pageTextSha256'] != page_hash(path, number):
            issues.append('normalized page text hash mismatched')
        witnesses = row.get('evidence', [])
        valid = 0
        for w in witnesses:
            p = resolve(w['path']) if w.get('path') else None
            wanted = w.get('lessonSha256') or w.get('sha256')
            if p is None or not wanted or not p.exists() or sha(p) != wanted:
                issues.append('lesson witness snapshot missing/mismatched:' + str(w.get('path')))
                continue
            content = p.read_text(encoding='utf-8-sig')
            if w.get('lineRange') and w.get('fragmentSha256'):
                a, b = w['lineRange']
                fragment = '\n'.join(content.splitlines()[a - 1:b])
                if digest(fragment) != w['fragmentSha256']:
                    issues.append('literal paragraph fragment mismatched:' + str(w['path']))
                    continue
            valid += 1
        status = row.get('status', 'unreviewed')
        if status in ['complete', 'complete-current-evidence']:
            verdict = 'complete-current-evidence' if valid and not issues and not row.get('pendingGaps') else 'stale-or-unverified-evidence'
        elif status == 'non-instructional':
            verdict = status if not issues and row.get('semanticComparison') else 'stale-or-unverified-evidence'
        else:
            verdict = 'partial' if status == 'partial' else status
        candidates[key(path, number)].append({'ledger': str(file.relative_to(R)).replace('\\', '/'),
          'status': verdict, 'reviewerStatus': status, 'witnessesChecked': valid,
          'issues': issues, 'pendingGaps': row.get('pendingGaps', []),
          'semanticComparison': row.get('semanticComparison', '')})

pages = []
for uid, source in expected.items():
    ev = candidates[uid]
    complete = [x for x in ev if x['status'] == 'complete-current-evidence']
    non = [x for x in ev if x['status'] == 'non-instructional']
    partial = [x for x in ev if x['status'] == 'partial']
    status = 'complete-current-evidence' if complete else 'non-instructional' if non else 'partial' if partial else 'not-yet-proven'
    pages.append({'source': source['source'], 'sourcePath': source['sourcePath'],
                  'pdfPage': source['pdfPage'], 'status': status, 'evidence': ev})
counts = dict(Counter(p['status'] for p in pages))
all_pass = all(p['status'] in ['complete-current-evidence', 'non-instructional'] for p in pages)
out = {'scope': 'Manual page-by-page semantic decisions with current PDF bytes, optional normalized page text and exact MD witness checks; no credit from book completion or page assignment. Non-instructional pages are explicitly reviewed cover/admin/etc, not taught knowledge.',
       'totalPages': len(pages), 'counts': counts, 'allSlidePagesProven': all_pass,
       'sourceLedgers': reports, 'pages': pages}
assert len(pages) == 458
(O / 'semantic-slides-gate-summary.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
md = ['# Đối chiếu từng trang slide và practice USTH', '',
      'Bảng này chỉ gộp những phán đoán đã đọc nội dung trang và kiểm bằng chứng hiện hành. Hoàn tất sách không tự hoàn tất slide. Các trang bìa/quản lý lớp được đánh dấu không có nội dung giảng, không biến thành bài tập giả.', '',
      '| Trạng thái | Số trang |', '|---|---|']
md += [f'| {k} | {v} |' for k, v in sorted(counts.items())]
closed = counts.get('complete-current-evidence', 0) + counts.get('non-instructional', 0)
md += ['', f'Đã chốt {closed}/{len(pages)} trang của 9 lecture và 3 practice; còn {len(pages)-closed} trang cần đối chiếu. Cổng trang đầy đủ: {"đã đóng" if all_pass else "còn mở"}.', '',
       'Các phần bổ sung USTH được ghi riêng trong manifest, có lời giảng, ví dụ và câu hỏi kèm đáp án cho những kỹ năng cần luyện từ slide. Không yêu cầu đọc lại mọi nội dung trước mỗi lượt làm bài.', '',
       'Chi tiết nguồn, phán đoán, literal witnesses và phần thiếu ở `research/semantic-slides-gate-summary.json`. Lịch sử partial được giữ; một ledger sửa mới chỉ thay kết luận khi thực sự có nội dung và bằng chứng đủ.', '', '## Ledger', '']
md += ['- `' + x + '`' for x in reports]
(R / 'docs/slide-semantic-coverage-status.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print(json.dumps({'counts': counts, 'total': len(pages), 'slideGate': all_pass}))
