"""Diagnostic only: candidate headings rejected by the initial capital-letter parser."""
from pathlib import Path
import collections,json,re,unicodedata
R=Path(__file__).resolve().parents[3];O=Path(__file__).resolve().parent
inv=json.loads((O/'source-section-inventory.json').read_text(encoding='utf-8'))
groups=collections.defaultdict(list)
for s in inv['bookSections']:groups[s['sourcePath']].append(s)
found=[]
for source,units in groups.items():
 lines=(R/source).read_text(encoding='utf-8').splitlines();chapter=units[0]['chapter'];known={s['section'] for s in units};stop=max(s['scopeLineEnd'] for s in units)
 for i,line in enumerate(lines[:stop]):
  text=unicodedata.normalize('NFKC',line).replace('\u00ad','').strip()
  m=re.match(r'^('+re.escape(chapter)+r'(?:\.\d+){1,6})\s+([A-Z0-9].{2,180})$',text)
  if not m or m[1] in known:continue
  if re.search(r'\s+\d{1,4}$',m[2]):continue
  found.append({'section':m[1],'title':m[2],'sourcePath':source,'sourceLine':i+1})
(O/'unindexed-heading-candidates.json').write_text(json.dumps(found,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(found,ensure_ascii=False,indent=2))
