"""Manual judgments after reading all remaining79 source pages and current MD.
The source hashes and literal witnesses are guards, not a semantic classifier.
"""
from pathlib import Path
import hashlib
import json
import unicodedata
from pypdf import PdfReader

O=Path(__file__).resolve().parent;R=O.parent;W=R.parents[1]
load=lambda p:json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest=lambda s:hashlib.sha256(s.encode()).hexdigest()
approved=load(O/'root-reviewed-snapshots.json')['lessons']
text={}
for name in ['USTH08','USTH09','USTH10','USTH11']:
    assert sha(R/'lessons'/f'{name}.md')==approved[name], 'Direct source/current lesson rereview is required'
    text[name]=(R/'lessons'/f'{name}.md').read_text(encoding='utf-8-sig').splitlines()

def witness(name,needle,kind,heading=None):
    lines=text[name];hits=[];current=''
    excluded=['## Luyện tập','## Đáp án và lập luận','## Gợi ý','## Biến thể và cách kiểm','## Học trên web','## Nguồn và đối chiếu']
    for i,line in enumerate(lines):
        if line.startswith('## '):current=line
        if heading:
            if current==heading and line.startswith(needle):hits.append(i)
        elif needle in line and current not in excluded:hits.append(i)
    assert len(hits)==1,(name,needle,hits)
    a=b=hits[0]
    while a>0 and lines[a-1].strip():a-=1
    while b+1<len(lines) and lines[b+1].strip():b+=1
    fragment='\n'.join(lines[a:b+1])
    return {'kind':kind,'path':f'lessons/{name}.md','lessonSha256':approved[name],
      'lineRange':[a+1,b+1],'paragraphExcerpt':fragment,'fragmentSha256':digest(fragment),'baselineActuallyRead':False}

groups={
 'notation':('USTH08','Trong Chen\'s notation','Ví dụ Customer–Places–Order',[1],'Chen entity/weak/normal/key/partial-key/identifying/mandatory symbols and explicit separate role connections; 1:1 requires UNIQUE, 1:N and parent participation distinguished.'),
 'music':('USTH08','Theo brief, mỗi Album','Với Artist A và B',[2,3],'All Music entities/attributes, full nested owner keys, identifying-attribute mapping and play count/MAX with zero plays; one-play-per-second key assumption and surrogate alternative explicit.'),
 'university':('USTH08','Program có program_id','Ví dụ Student S1',[4,5],'Full University fields and weak Course owner key mapped, planned slots retained, attempted term identity/retakes and composite same-Program constraint; source final schema omissions repaired.'),
 'flight':('USTH08','Airplane có registration_number','Bài nguồn gọi book a seat',[6],'Four Flight tables/keys/FKs and all temporal/name/capacity fields, exact source unique-flight-number assumption; booking is not seat allocation, repeated daily number is separate brief.'),
 'northwind8':('USTH08','Hình slide 11','Một mapping theo hình là PO',[7],'Simplified Northwind strong/weak PO owner ordinal and M:N detail attributes fully mapped, list/unit/cost grain separate and repeated-product line policy explicit.'),
 'sdlc':('USTH09','Systems analysis and design','Ví dụ “mỗi giảng viên',[1],'All five SDLC stages with inputs/outputs, feasibility/team/dependencies/plan and feedback loop; concrete requirement/design/test/maintenance example.'),
 'components':('USTH09','Database là phần data','Ví dụ query điểm đúng',[2],'All five information-system components mapped across design and implementation: hardware,software,data,procedures,people; integrated testing/startup and training context preserved.'),
 'requirements':('USTH09','Nguồn gồm phỏng vấn','Một ghi chú phỏng vấn nên',[3],'Interview/forms/reports/queries/programs/websites/usecases/business rules and approved requirements, example notes/provenance, security/audit/mobile/scalability/training needs operationalized rather than slogans.'),
 'amsreq':('USTH09','Với AMS, người dùng muốn','Ví dụ do PE biên soạn:',[3],'All AMS objectives and scope connected to concrete measurable tasks; source illustrative interview not claimed as an actual PE interview, privacy-law names not automatically universal applicability.'),
 'amsmodel':('USTH09','Các đối tượng cần khảo sát','Ví dụ schema nhỏ giữ đúng grain:',[4],'Academic years/building-room/subject-class-session/student-department/internal-adjunct/attendance/results entities preserved; temporal occurrence and enrollment invariant distinguished from two independent FKs.'),
 'actors':('USTH09','Login/logout, profile','| System administrator |',[4],'All four AMS actors and associated usecases including session/enrollment, profile/timetable/results/authentication, explicit permissions and negative tests; source Extends not misread as FK/rights inheritance.'),
 'validate':('USTH09','Với AMS, cho Teacher thử','Mỗi requirement cần đường truy vết:',[9],'Validate full data model against every usecase with user feedback and form/report prototyping; original zero-order/unapproved/history test cases plus traceability and redesign feedback.'),
 'nwreq':('USTH09','Northwind trong slide','Một schema tham khảo dùng',[5],'Fictitious-company context and all eight entity families/fields/roles, sale and purchase price/ordinal scopes, employee/shipper/invoice links; incomplete source proposal not treated as final schema.'),
 'crud':('USTH09','Nghiệp vụ cần CRUD','In chứng từ phải đọc',[7],'Insert/update/delete/report/print workflow, protected referenced objects and transaction/commit/retry semantics, no blanket CASCADE substitution.'),
 'derive':('USTH09','Đầu tiên, chọn danh từ','Ví dụ PO số 1',[6,8],'Three derive/refine steps from nouns/verbs/cardinality to weak identity and report validation, surrogate versus business uniqueness; logical and physical schema constraints explicit.'),
 'sql':('USTH09','SQL cho DBMS thật','Mỗi requirement cần đường truy vết:',[10],'DDL DB/tables/constraints/index/objects and CRUD/query SQL files, component/integration/conversion/maintenance evidence mapped to all-web delivery, not requiring local native installation.'),
 'annual':('USTH11','Biểu đồ nguồn gồm','Ví dụ mới: doanh thu 75',[21],'Annualized-versus-observed periods, dates/status/units/cohorts and linear annualization example, chart height not causal evidence; original source bar numbers not asserted as new fixture data.'),
 'repchart':('USTH11','Biểu đồ nguồn gồm','Employee 3 không có đơn.',[22],'Sales-rep revenue chart backed by employee-grain SQL, zero-activity preservation and status policy; no stale prepared chart represented as learner execution.'),
 'customergeo':('USTH11','Fixture dùng region/country','“Customer theo country” đếm khách',[23],'Customer count by region and country from customer grain, address-time assumption and absent-geography dimension scope; original fixture/results rather than copying screenshot numbers.'),
 'ordergeo':('USTH11','Fixture dùng region/country','“Order theo country” đếm đơn',[24],'Order counts by region/country via correct customer join, COUNT order key and zero-order group; source32/33 repeated chart explicitly noted.'),
 'setup':('USTH10','MySQL Server giữ','SELECT VERSION() AS engine_version',[1,2],'All four Practice1 setup/connect pages read including screenshots. Server/client,host/port/auth,connection label,interactive/batch,prompt,GUI selected SQL and test-connection distinctions taught; installer/service/phpMyAdmin/Workbench operations faithfully mapped to web provisioning under user web-only constraint, actual engine probed instead of XAMPP label.'),
}

def add_group(row,key):
    name,teaching,example,questions,judgment=groups[key]
    row['semanticComparisons'].append(judgment)
    row['evidence'] += [witness(name,teaching,'teaching'),witness(name,example,'worked-example-or-counterexample')]
    for n in questions:
        row['evidence'] += [witness(name,f'{n}.','activity','## Luyện tập'),witness(name,f'{n}.','answer-rubric','## Đáp án và lập luận')]

def add_tasks(row,name,questions,tags=None):
    for n in questions:
        row['evidence'] += [witness(name,f'{n}.','activity','## Luyện tập'),witness(name,f'{n}.','answer-rubric','## Đáp án và lập luận')]
    if tags:
        lines=text[name]
        for tag in tags:
            # Code is in the answer section, so scope explicitly to it.
            row['evidence'].append(witness(name,'-- '+tag,'exact-answer-SQL','## Đáp án và lập luận'))
    row['semanticComparisons'].append('Every listed source task on this page has an explicit corresponding prompt, written answer and SQL reference where applicable; current exact SQL was executed in the named MySQL QA scope. Source dump/screenshot rows are not claimed as fixture data.')

L8={4:['notation'],5:['notation'],6:['notation'],7:['notation'],8:['music'],9:['university'],10:['flight'],11:['northwind8'],13:['music'],14:['music'],15:['music'],16:['university'],17:['notation'],18:['university'],19:['university'],20:['university'],21:['flight']}
L9={3:['sdlc'],4:['sdlc'],5:['sdlc'],6:['amsreq'],7:['amsreq'],8:['requirements'],9:['components'],10:['sql'],11:['components'],12:['sdlc'],14:['derive'],15:['requirements'],16:['amsmodel'],17:['requirements'],18:['requirements'],19:['actors'],20:['actors'],21:['validate'],23:['nwreq'],25:['nwreq'],26:['nwreq'],27:['crud'],28:['annual'],29:['repchart'],30:['customergeo'],31:['customergeo'],32:['ordergeo'],33:['ordergeo'],34:['ordergeo'],35:[],36:[],38:['derive'],39:['derive'],40:['derive'],41:['nwreq','derive'],42:['nwreq','derive'],44:['derive'],45:['derive'],46:['derive'],48:['sql']}
sources=[('L8','Lecture 8 - ERD some use cases.pdf',L8),('L9','Lecture 9 - Database Development Process.pdf',L9),('P1','Practice 1.pdf',{1:['setup'],2:['setup'],3:['setup'],4:['setup'],5:[]}),('P2','Practice 2.pdf',{1:[]}),('P3','Practice 3.pdf',{1:[],2:[],3:[],4:[]})]
inventory=load(O/'slide-page-map.json')['pages'];pages=[]
for label,basename,mapping in sources:
    assigned=[r for r in inventory if r['source']==basename]
    path=Path(assigned[0]['sourcePath']);reader=PdfReader(path);sourcehash=sha(path)
    for src in assigned:
        n=src['pdfPage'];raw=reader.pages[n-1].extract_text()
        suffix=f'{n:02}' if label.startswith('L') else str(n)
        rendered=f'tmp/database-source/slides-lecture89-practice/{label}-{suffix}.png'
        row={'source':{'path':str(path),'sha256':sourcehash,'pdfPage':n,
              'pageTextSha256':digest(unicodedata.normalize('NFKC',raw).replace('\u00ad','').strip()),
              'normalization':'pypdfextract_text,NFKC,removeU+00AD,strip,UTF8SHA256'},
             'sourceReadStatus':'All page text read in full; all4 L8/8 L9/3 practice contact sheets visually inspected; selected Music/University/SDLC/AMS/Company diagrams also inspected full size.',
             'observedContent':raw[:1000],'pendingGaps':[],'baselineCreditApplied':False,
             'sourceFiguresRead':[{'renderedPath':rendered,'renderedSha256':sha(W/rendered),
                'visuallyInspected':True,'inspectionMode':'Six-page contact sheet, with body text read separately and selected diagrams full size.'}],
             'engineEvidence':'qa/usth-final-sources-checks.json: 106 named checks including78 native MySQL8.4.13 checks; new random schemas only, Company table deletion only inside its own newly created schema; finite SQLite key examples separate.',
             'semanticComparisons':[],'evidence':[]}
        if n not in mapping:
            row.update(status='non-instructional',semanticComparison='Cover/objectives/section-title or suggested drawing tools only; substantive concepts judged on following pages.',practiceCoverage='not-applicable-non-instructional')
        else:
            row['status']='complete-current-evidence'
            for key in mapping[n]:add_group(row,key)
            if label=='L9' and n in [35,36]:
                qs=range(1,11) if n==35 else range(11,21)
                add_tasks(row,'USTH11',qs,[f'L9.R{i:02}' for i in qs])
            if label=='P1' and n==5:
                add_tasks(row,'USTH10',range(1,7),['P1.03','P1.04','P1.05','P1.06'])
                row['evidence'] += [witness('USTH10','Hình Practice 1 trang 5','teaching'),witness('USTH10','Employee trỏ Department','worked-example-or-counterexample')]
            if label=='P2':
                add_tasks(row,'USTH10',range(7,22),[f'P2.{i:02}' for i in range(1,16)])
                row['evidence'].append(witness('USTH10','Top 4 lấy đúng bốn rows','teaching'))
            if label=='P3':
                qs={1:range(22,26),2:range(26,33),3:range(33,36),4:range(36,37)}[n]
                add_tasks(row,'USTH10',qs,[f'P3.{i-21:02}' for i in qs])
                row['evidence'].append(witness('USTH10','Ví dụ đơn 31 có hai line','teaching-and-worked-example'))
            row['semanticComparison']=' '.join(row['semanticComparisons'])
            row['practiceCoverage']='Every substantive page skill linked to original/equivalent answered task; complete multi-task source pages linked to all listed tasks/SQL, not a generic keyword exercise.'
        pages.append(row)
assert len(pages)==79
assert sum(r['status']=='complete-current-evidence' for r in pages)==67
out={'date':'2026-11-06','scope':'Direct full-body/figure/current MD review of all remaining79 pages: Lecture8, Lecture9 and Practice1/2/3; all36 practice tasks and24 report/chart tasks retained with explicit answers/SQL and source-specific assumptions.',
     'counts':{'complete-current-evidence':67,'non-instructional':12},'pages':pages,
     'sourceErrata':['University final mapping omits planned slots and retake term key; preserve both.',
       'Album/Track local IDs require full owner keys; play timestamp key needs collision assumption.',
       '1:1 FK needs UNIQUE; seat booking lacks seat identity/capacity invariant.',
       'Practice1 Company source includes Minit, and local setup must be mapped to web per user constraint.',
       'Reports require explicit grain/ties/status/date/NULL/population/geography assumptions; source screenshots are not the provided PE fixture.'],
     'qa':'qa/usth-final-sources-checks.json: selected finite SQLite and exact MySQL8.4.13 cases, no production learner runner/pilot certification.'}
(O/'semantic-slides-final-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'pages':len(pages),'complete':67,'nonInstructional':12}))
