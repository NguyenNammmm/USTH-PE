"""Add visual samples for the newly expanded source-reviewed lessons."""
from pathlib import Path
import json
import pypdfium2 as pdfium

R = Path(__file__).resolve().parents[1]
v = json.loads((R / 'qa/pdf-verification.json').read_text(encoding='utf-8-sig'))
meta = json.loads((R / 'qa/pdf-build.json').read_text(encoding='utf-8-sig'))
chosen = set()
for name in ['AD01', 'AD02', 'AD09', 'AD10', 'AD11', 'AD12', 'AD18', 'AD19',
             'AD39', 'AD40', 'AD41', 'AD42', 'AD43', 'AD44', 'AD45', 'AD63',
             'AD70', 'AD71', 'AD72']:
    chosen.update([meta['bookmarks'][name], meta['bookmarks'][name] + 2])
chosen.update([13, 18, 27, 35, 110, 124, 203, 381, 386, 394, 402, 414, 610, 611])
existing = {x['page']: x for x in v['rendered']}
pdf = pdfium.PdfDocument(str(R / 'Database-Advanced-PE.pdf'))
for n in sorted(chosen - existing.keys()):
    page = pdf[n - 1]
    target = R / 'qa/pdf-render' / f'page-{n:04}.png'
    page.render(scale=1.25).to_pil().save(target)
    page.close()
    existing[n] = {'page': n, 'path': str(target.relative_to(R)).replace('\\', '/')}
pdf.close()
v['rendered'] = [existing[n] for n in sorted(existing)]
v['samplePolicy'] = 'Module/key/appendix pages plus selected openings and dense middle pages of newly expanded SQL/ER/analytics/concurrency/recovery lessons. Visual inspection is sampled, not all pages.'
(R / 'qa/pdf-verification.json').write_text(json.dumps(v, ensure_ascii=False, indent=2), encoding='utf-8')
print('Selected PDF renders', len(v['rendered']))
