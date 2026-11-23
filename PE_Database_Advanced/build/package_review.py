from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
snapshot=load(R/'qa/build-snapshot.json')
changed=[p for p,d in snapshot['files'].items() if sha(R/p)!=d]
assert not changed,('Inputs changed during build; rebuild before packaging',changed)
gate=load(R/'research/semantic-gate-summary.json')
slide=load(R/'research/semantic-slides-gate-summary.json')
assert gate['allBookUnitsProven'] and gate['allSlidePagesProven'] and slide['allSlidePagesProven']
assert load(R/'manifest.json')['allContentComplete']
assert (R/'Database-Advanced-PE.pdf').exists()
pdf=load(R/'qa/pdf-verification.json');ui=load(R/'qa/ui-dom-verification.json')
assert pdf['visualReview']=='sampled-render-review-passed' and pdf['pdfSha256']==sha(R/'Database-Advanced-PE.pdf')
assert len(pdf['checks'])==96 and all(not x['missingLineWitnesses'] for x in pdf['checks'])
assert not load(R/'qa/pdf-layout-checks.json')['outOfBounds']
assert ui['htmlSha256']==sha(R/'course-spec.html') and ui['checksPassed']==17 and not ui['runtimeErrors']
structure=load(R/'qa/package-verification.json');assert structure['passed']==structure['total']==10
editorial=load(R/'qa/usth-editorial-freshness.json')
assert editorial['result']=='pass' and editorial['currentUSTH10Sha256']==sha(R/'lessons/USTH10.md')
allow=[]
historical_helpers={'prepare_pdf_builder.py','rewrite_AD43.ps1','build_inline_flow.py'}
for p in R.rglob('*'):
 if not p.is_file():continue
 rel=p.relative_to(R)
 if '__pycache__' in rel.parts or 'pdf-render' in rel.parts:continue
 if p.name in historical_helpers or p.suffix=='.pyc':continue
 if p.name in ['release-files.json','release-verification.json','final-delivery-audit.json']:continue
 allow.append(p)
record={'status':'source-complete content and developer specification; verified export','sourceGate':gate['counts'],'slideGate':slide['counts'],'excluded':'Raw book/slide files, source figure renders, raw clones, vendor/runtime/server, obsolete authoring helpers and PDF render intermediates are not redistributed.','files':[{'path':str(p.relative_to(R)).replace('\\','/'),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(allow)]}
(R/'release-files.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8');allow.append(R/'release-files.json')
target=R.parent/'Database-Advanced-PE-2026-11-06.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for p in sorted(allow):z.write(p,'database-advanced/'+str(p.relative_to(R)).replace('\\','/'))
with zipfile.ZipFile(target) as z:assert z.testzip() is None;names=z.namelist()
result={'zip':str(target),'sha256':sha(target),'bytes':target.stat().st_size,'files':len(names),'CRC':'pass','status':'source-complete content and developer specification; verified export'}
(R/'qa/release-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
