"""Find rendered page changes after correcting two handoff status documents.

The prior archive is the visually reviewed export, not the final delivery.
This comparison does not grant a visual signoff to any changed page.
"""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
import pypdfium2 as pdfium

R = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--previous-zip', required=True, type=Path)
parser.add_argument('--expected-previous-pdf-sha256', required=True)
args = parser.parse_args()
archive = args.previous_zip
with zipfile.ZipFile(archive) as z:
    previous = z.read('database-advanced/Database-Advanced-PE.pdf')
assert hashlib.sha256(previous).hexdigest() == args.expected_previous_pdf_sha256
current = (R / 'Database-Advanced-PE.pdf').read_bytes()
old = pdfium.PdfDocument(previous)
new = pdfium.PdfDocument(current)
assert len(old) == len(new) == 785
changed = []
for i in range(len(new)):
    before, after = old[i], new[i]
    a = before.render(scale=0.5).to_pil()
    b = after.render(scale=0.5).to_pil()
    if a.size != b.size or a.tobytes() != b.tobytes():
        target = R / 'qa/pdf-render' / f'revision-{i+1:04d}.png'
        after.render(scale=1.25).to_pil().save(target)
        changed.append({'page': i+1, 'render': str(target.relative_to(R)).replace('\\', '/')})
    before.close()
    after.close()
old.close()
new.close()
result = {'scope': 'Every page raster compared at scale 0.5 to the prior visually reviewed export. Each changed page rendered separately at scale 1.25 for visual review.',
          'pages': 785, 'unchangedPages': 785-len(changed), 'changedPages': changed,
          'previousPdfSha256': hashlib.sha256(previous).hexdigest(),
          'currentPdfSha256': hashlib.sha256(current).hexdigest()}
(R / 'qa/pdf-revision-comparison.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result))
