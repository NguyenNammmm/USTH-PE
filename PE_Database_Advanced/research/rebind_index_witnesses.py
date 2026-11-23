"""Preserve the48-unit index review after the scoped AD28 concurrency addition.

Exact old witnesses must remain unchanged. No new source credit is granted here.
"""
from pathlib import Path
import hashlib
import json
import re

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
old_md = W / 'tmp/database-source/AD28-before-concurrency-20261105.md'
path = R / 'lessons/AD28.md'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
old_sha = sha(old_md)
new_sha = sha(path)
old = old_md.read_text(encoding='utf-8-sig')
new = path.read_text(encoding='utf-8-sig')
p = O / 'semantic-indexes.json'
ledger = json.loads(p.read_text(encoding='utf-8-sig'))
assert ledger['lessonFinalSha256']['AD28'] == old_sha, 'Expected original frozen snapshot; manual rereview required'
before_count = len(ledger['units'])
paragraphs = list(re.finditer(r'\S.*?(?=\n\s*\n|\Z)', new, re.S))
rebound = 0


def walk(value):
    global rebound
    if isinstance(value, dict):
        if str(value.get('path', '')).replace('\\', '/').endswith('/AD28.md') and 'lessonSha256' in value:
            assert value['lessonSha256'] == old_sha
            text = value.get('exactParagraph', value.get('exactText'))
            assert text and old.count(text) == 1 and new.count(text) == 1, 'Old evidence changed/ambiguous'
            offset = new.index(text)
            value['lessonSha256'] = new_sha
            value['lineRange'] = [new.count('\n', 0, offset) + 1, new.count('\n', 0, offset + len(text)) + 1]
            if 'paragraph' in value:
                found = [i + 1 for i, m in enumerate(paragraphs) if m.group().strip() == text]
                assert len(found) == 1
                value['paragraph'] = found[0]
            rebound += 1
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)


walk(ledger['units'])
assert len(ledger['units']) == before_count == 48
ledger['lessonFinalSha256']['AD28'] = new_sha
ledger['postFreezeScopedChanges'] = [{
    'date': '2026-11-05', 'previousLessonSha256': old_sha, 'currentLessonSha256': new_sha,
    'oldExactWitnessesUnchanged': rebound,
    'change': 'Corrected two bad18.11 citations to18.10.2; added source-reviewed concurrency teaching and exercises11/12 after existing chapter14 material. Existing48 source-unit judgments and exact witness texts unchanged.',
    'sourceCredit': 'None added by rebinding; separate semantic-advanced-concurrency.json holds full18.10 own-body review.'
}]
p.write_text(json.dumps(ledger, ensure_ascii=False, indent=2), encoding='utf-8')
print('Preserved/rebound old AD28 exact witnesses', rebound)
