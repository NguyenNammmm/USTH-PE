"""Capture current authoring inputs before rebuilding review artifacts.

This is a freshness snapshot, not source-coverage approval. Run before builds,
then package_review must find every input unchanged after PDF/HTML verification.
"""
from pathlib import Path
import hashlib
import json

R = Path(__file__).resolve().parents[1]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
files = []
for folder in ['lessons', 'docs', 'research', 'build', 'fixtures']:
    files.extend(p for p in (R / folder).rglob('*') if p.is_file()
                 and '__pycache__' not in p.parts and p.suffix not in ['.pyc', '.png'])
files.extend(R / p for p in ['README.md', 'manifest.json', 'activities.json', 'build_pdf.py', 'build_html.py'])
snapshot = {'status': 'source-complete build candidate; export verification required',
            'policy': 'Input hashes frozen before HTML/PDF regeneration. This records versions, not completeness.',
            'files': {str(p.relative_to(R)).replace('\\', '/'): sha(p) for p in sorted(set(files))}}
(R / 'qa/build-snapshot.json').write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding='utf-8')
print('Frozen authoring input files', len(snapshot['files']))
