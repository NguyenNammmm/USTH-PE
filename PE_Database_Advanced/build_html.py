from pathlib import Path
import base64,json
R=Path(__file__).resolve().parent
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
d=load(R/'manifest.json');inv=load(R/'research/source-section-inventory.json');repo=load(R/'research/repo-registry.json')
for l in d['lessons']:
 p=R/l['path']
 assert p.exists(),str(p)
 l['markdown']=p.read_text(encoding='utf-8-sig').replace('](../','](')
 board=R/'assets/state-boards'/(l['id']+'.png')
 if board.exists():l['stateBoard']='data:image/png;base64,'+base64.b64encode(board.read_bytes()).decode('ascii')

for l in d.get('supplementalLessons',[]):
 p=R/l['path']
 assert p.exists(),str(p)
 l['markdown']=p.read_text(encoding='utf-8-sig')
d['repoActivities']=load(R/'activities.json')['activities']
d['sections']=[{'section':s['section'],'title':s['title'],'chapter':s['chapter'],'owners':s['plannedAdvancedLessonIds'],'review':s.get('semanticReviewStatus','Đã gán nơi học; xem báo cáo rà độ sâu')} for s in inv['bookSections']]
gate=load(R/'research/semantic-gate-summary.json')
states={s['section']:s['status'] for s in gate['units']}
labels={'complete-current-evidence':'Đã đối chiếu thân mục; bằng chứng còn đúng hash','partial':'Đã đọc nhưng còn phần cần bổ sung','not-yet-proven':'Chưa đủ bằng chứng đối chiếu toàn thân mục'}
for s in d['sections']:s['review']=labels[states[s['section']]]
d['repos']=repo['repos'];d['docs']={p.stem:p.read_text(encoding='utf-8-sig') for folder in ['docs','research'] for p in (R/folder).glob('*.md')}
text=(R/'build/spec-template.html').read_text(encoding='utf-8')
for label,value in [('CSS',(R/'build/spec.css').read_text(encoding='utf-8')),('DATA','window.ADVANCED_DATA='+json.dumps(d,ensure_ascii=False).replace('</','<\\/')+';'),('MODELS',(R/'build/models.js').read_text(encoding='utf-8')),('UI',(R/'build/spec-ui.js').read_text(encoding='utf-8'))]:text=text.replace('/*__'+label+'__*/',value)
assert not any('/*__'+x+'__*/' in text for x in ['CSS','DATA','MODELS','UI'])
(R/'course-spec.html').write_text(text,encoding='utf-8');print('HTML bytes',len(text.encode('utf-8')))
