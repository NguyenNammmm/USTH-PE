"""Merge manual semantic evidence, rejecting stale lesson snapshots.

This validates evidence freshness, not the truth of a reviewer judgment.
"""
from pathlib import Path
import collections,hashlib,json
O=Path(__file__).resolve().parent;R=O.parent;W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
inv=load(O/'source-section-inventory.json');ids={s['section'] for s in inv['bookSections']}
def pairs(obj):
 out=[]
 if isinstance(obj,dict):
  path=obj.get('path');digest=obj.get('lessonSha256') or obj.get('sha256')
  if path and digest and str(path).endswith('.md'):out.append((path,digest))
  for key,val in obj.items():
   if isinstance(val,(dict,list)):out.extend(pairs(val))
 elif isinstance(obj,list):
  for val in obj:out.extend(pairs(val))
 return out
def resolve(path):
 p=Path(path)
 if p.is_absolute():return p
 if path.replace('\\','/').startswith('output/'):return W/p
 return R/p
candidates=collections.defaultdict(list);sources=[]
for file in sorted(O.glob('semantic-*.json')):
 if file.name.endswith('-checks.json') or file.name in ['semantic-gate-summary.json','semantic-data-models-integrity.json']:continue
 data=load(file);rows=data.get('units',[])
 if not isinstance(rows,list):continue
 sources.append(str(file.relative_to(R)).replace('\\','/'))
 for row in rows:
  section=row.get('section')
  if section not in ids:continue
  status=row.get('semanticStatus') or row.get('completionStatus') or row.get('status') or 'unreviewed'
  evidence=pairs(row);stale=[]
  for path,digest in evidence:
   p=resolve(path)
   if not p.exists() or sha(p)!=digest:stale.append(path)
  source=row.get('source',{})
  if isinstance(source,dict):
   sp=source.get('path');ss=source.get('sha256')
  else:sp=ss=None
  sp=sp or row.get('sourcePath') or row.get('sourcepath');ss=ss or row.get('sourceSha256') or row.get('sourcehash')
  sourceFresh=bool(sp and ss and (W/Path(sp)).exists() and sha(W/Path(sp))==ss)
  complete=status in ['complete','complete-source-unit-comparison']
  verdict='complete-current-evidence' if complete and evidence and not stale and sourceFresh else ('stale-evidence' if complete and stale else 'unverified-complete-claim' if complete else status)
  candidates[section].append({'ledger':str(file.relative_to(R)).replace('\\','/'),'status':verdict,'reviewerStatus':status,'sourceHashMatches':sourceFresh,'lessonWitnessHashesChecked':len(evidence),'staleLessonPaths':sorted(set(stale))})
rows=[]
for s in inv['bookSections']:
 evidence=candidates[s['section']]
 passed=[e for e in evidence if e['status']=='complete-current-evidence']
 partial=[e for e in evidence if e['status']=='partial']
 state='complete-current-evidence' if passed else 'partial' if partial else 'not-yet-proven'
 rows.append({'section':s['section'],'title':s['title'],'owners':s['plannedAdvancedLessonIds'],'status':state,'evidence':evidence})
counts=dict(collections.Counter(r['status'] for r in rows))
slideFile=O/'semantic-slides-gate-summary.json'
slideGate=load(slideFile).get('allSlidePagesProven',False) if slideFile.exists() else False
result={'scope':'Manual source-body correspondence judgments with current lesson/source hash checks. Not automatically a certification of all book, figures, slides or teaching effectiveness.','counts':counts,'totalSourceUnits':len(rows),'allBookUnitsProven':all(r['status']=='complete-current-evidence' for r in rows),'allSlidePagesProven':slideGate,'sourceLedgers':sources,'units':rows}
(O/'semantic-gate-summary.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
md=['# Tiến độ cổng đối chiếu nội dung đầy đủ','','Báo cáo này gộp các đánh giá đã đọc thân mục nguồn và kiểm hash hiện hành. Không lấy danh sách địa chỉ, số bài hoặc test phần mềm làm tín chỉ kiến thức. Khi Markdown đổi, snapshot của lượt rà cũ cần kiểm lại.','','| Trạng thái | Số mục/tiểu mục |','|---|---|']
md += ['| '+k+' | '+str(v)+' |' for k,v in sorted(counts.items())]
md += ['','Tổng địa chỉ hiện tại: '+str(len(rows))+'. Parent và child được xét theo own-body để không đếm lặp nội dung. Các mục con vẫn cần đánh giá riêng; complete ở parent không suy mọi hậu duệ đã đủ.','','Cổng sách: '+('đã có đối chiếu hiện hành cho mọi own-body.' if result['allBookUnitsProven'] else 'còn mở tới khi mọi mục có bằng chứng đủ và hiện hành.')+' Cổng slide/practice: '+('đã đóng.' if slideGate else 'còn mở; xem báo cáo từng trang.')+' Page map riêng chỉ là địa chỉ; các lượt đọc intro/figure không được thay bằng OCR keyword.','','## Ledger được gộp','']
md += ['- `'+s+'`' for s in sources]
md += ['','Chi tiết từng mục ở `research/semantic-gate-summary.json`. Đây là trạng thái công việc; không phải chứng chỉ độc lập về chất lượng khóa.']
(R/'docs/semantic-coverage-status.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print(json.dumps({'counts':counts,'total':len(rows),'bookGate':result['allBookUnitsProven'],'slideGate':slideGate}))
