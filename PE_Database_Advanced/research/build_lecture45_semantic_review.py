"""Manual semantic decisions for all92pages; exact hashes guard reviewed text."""
from pathlib import Path
import hashlib
import json
import unicodedata
from pypdf import PdfReader

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
digest = lambda s: hashlib.sha256(s.encode()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
text = {}
for name in ['USTH04', 'USTH05']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct source/current MD rereview required'
    text[name] = p.read_text(encoding='utf-8-sig').splitlines()

def witness(name, needle, kind, heading=None):
    lines = text[name]
    found = []
    current = None
    for i, line in enumerate(lines):
        if line.startswith('## '):
            current = line
        if heading is not None:
            if current == heading and line.startswith(needle):
                found.append(i)
        elif needle in line and current not in ['## Luyện tập','## Đáp án và lập luận','## Gợi ý','## Biến thể và cách kiểm','## Học trên web','## Nguồn và đối chiếu']:
            found.append(i)
    assert len(found) == 1, (name, needle, found)
    a = found[0]
    # Capture a complete paragraph including a table/code group as appropriate.
    while a > 0 and lines[a - 1].strip():
        a -= 1
    b = found[0]
    while b + 1 < len(lines) and lines[b + 1].strip():
        b += 1
    fragment = '\n'.join(lines[a:b + 1])
    return {'kind': kind, 'path': f'lessons/{name}.md', 'lessonSha256': approved[name],
            'lineRange': [a + 1,b + 1], 'paragraphExcerpt': fragment,
            'fragmentSha256': digest(fragment), 'baselineActuallyRead': False}

groups = {
 'query': ('USTH04','Không khai báo FK','Qualification r.id/m.id',1,'Projection/selection/join qualified aliases, product cardinality and result-schema contract, set selection notation corrected;originalfixture and answered missing-parent transfer.'),
 'range': ('USTH04','INNER JOIN bao gồm','Ví dụ xếp hạng',3,'Non-equijoin still inner, half-open bands and overlap/gap boundary semantics, full independent predicate/task/result; source non-INNER/selection/mark typos corrected.'),
 'outer': ('USTH04','Room LEFT JOIN Member','Kết quả có5 hàng',2,'Left/right/full bag preservation including unmatched NULL keys, full emulation with nonNULL marker and unionall, ONversusWHERE and projected schema caveat; source displayed SELECT* not equated to one-column query.'),
 'domain': ('USTH04','domain là các giá trị','Room LEFT JOIN Member',2,'Allowed domain versus values appearing in instance; inner matchedpairs versus preserving left/right/all; not a Venn multiplicity argument.'),
 'self': ('USTH04','Với Employee(id,manager_id)','Thêm row tự tham chiếu',4,'Two aliased roles, selfjoin nullable-root preservation, qualification/outputalias and MySQLCONCAT rather than numericplus; businesscycle constraints separate.'),
 'sets': ('USTH04','Cho hai bag một cột','Với A={x,y}',5,'Six set/bag operator multiplicities,compatiblearity/types/whole-rowdistinct,NULL nondistinct and source Venn intersection corrected, dialect/capability marked.'),
 'agg': ('USTH04','COUNT(*) đếm hàng','GroupA có',6,'Actualgroup memberships/output schemas,COUNTrowversusnonnull/distinct,SUM/AVG/MIN/MAX,empty implicitgroup versusnogroup,groupNULLs and two-column grouping;sourceCOUNTexception corrected.'),
 'variance': ('USTH04','Độ phân tán cần','Với giá trị[2,4,6]',8,'Population/sample variance and standarddeviation defined with exact arithmetic,one-samplecase andMySQLalias qualifications;source genericfunctionsnotblindlytransferred.'),
 'having': ('USTH04','Sau WHERE còn','Đổi WHERE thành',7,'Logical rowfilter/group/HAVING/order stages,exactnewoutputs and independentMAX/SUM variation;notphysicalexecutionorder orOraclegrammartreatedasMySQL.'),
 'nested': ('USTH04','Muốn “giá trị lớn nhất','Kết quả15.',8,'Derived-tabletwo-query-blockrewrite formaxofgroupmeans,explicitresult15andidentity/tie distinction;notuniversaldepth-two nestedaggregateclaim.'),
 'fd': ('USTH05','X → Y nghĩa','Ví dụ Teach',1,'Two-tuple FD semantics,determinant/dependentsets,triviality,businessconstraintversussample,onecourse/manyteachers counterexample and grain/key distinctions.'),
 'rules': ('USTH05','Ba tiên đề Armstrong','| Union:',2,'Allthreeaxiomswithtwo-tuple soundness and five derived rules including accumulation/extension;RHSsplitnotLHS and explicit answered proof task.'),
 'keys': ('USTH05','X là superkey nếu X+ = R.','Dưới duy nhất FD',4,'Superkeyversuscandidatekey,minimalnotminimum,primarychoice and supersets;distinctteachergrain and allfourFD-system enumeration answers,sourceDDtypo corrected.'),
 'closure': ('USTH05','Cho R(A,B,C,D,E,F), G','Tách RHS thành',3,'Completefixpointalgorithm,trace,termination/soundness/completenesscountermodel/complexity and exactAB/CF exercise answers;safeRHSpruninglimits explicit.'),
 'anomaly': ('USTH05','Cho Session(course','Sau decomposition',6,'Originalmultiteachergrain redundancy/update/delete/insertionproblems,projectionsandretainedfact versusinnerjoinview,losslessFDargument.'),
 'decomp': ('USTH05','Chiếu thành SessionInfo','Ví dụ lossy:',6,'Projection schema union and binaryreconstruction,losslessproof and exact spuriousrows,sourceproduct/dimensioncomparison errorscorrected;notall tách eliminatesallconstraints.'),
 'preserve': ('USTH05','Dependency preservation','AC = {(a,c1)',10,'Losslessness distinct from localconstraintpreservation,concreteAC/BC stateswithlocalC->BandglobalAB->Cviolation,independenttransferanswer.'),
 'first': ('USTH05','Trong mô hình quan hệ phẳng','Name có dấu cách',7,'Atomicityrelative todomain/operations,originalproductcolormapping andidentity,fullnamedoesnotforcefirst/lastsplit,repeatingcolumns/punctuationdiagnosticsnotautomaticproof.'),
 'second': ('USTH05','Prime attribute nằm','Một PK một cột',8,'2NF allcandidatekeys/nonprime/fullversuspartialdependencies,explicitcounterexamplesinglechosenPKandcompositealternatekey;sourceitem->pricepartialversustaxtransitive explained.'),
 'third': ('USTH05','3NF có điều kiện','keys là AB và AC',5,'FormalallimpliedFDsuperkey-or-primeconditionversusBCNF;multiplekeyexceptionandsystemclassificationsafterfullkeyenumeration,notnonkey-slogan.'),
 'authorship': ('USTH05','Ví dụ Authorship','Nếu một publisher',9,'OriginalAuthorship/Book/Author2NFdecompositionplusBook/Publisher3NFunderexplicitFDassumption,keys/FKs/retainedindependentfactsandmultiplecitycounterpolicy.'),
}
L4 = {2:'query',4:'query',5:'query',6:'query',7:'range',8:'range',9:'outer',10:'outer',11:'outer',12:'outer',13:'outer',14:'outer',15:'outer',16:'domain',17:'self',18:'query',19:'query',20:'query',21:'sets',22:'sets',23:'sets',24:'sets',26:'sets',27:'sets',28:'sets',29:'sets',30:'agg',31:'variance',32:'agg',33:'agg',34:'agg',35:'agg',36:'agg',37:'agg',38:'agg',39:'agg',40:'agg',41:'having',42:'having',43:'having',44:'having',45:'having',46:'having',47:'nested'}
L5 = {4:'fd',5:'fd',6:'rules',7:'fd',8:'fd',9:'rules',10:'keys',11:'keys',12:'keys',13:'keys',14:'closure',15:'closure',16:'closure',17:'closure',18:'closure',19:'keys',20:'keys',21:'keys',22:'keys',24:'anomaly',25:'anomaly',26:'decomp',27:'decomp',28:'anomaly',29:'preserve',30:'decomp',31:'first',32:'first',33:'first',34:'first',35:'second',36:'second',37:'third',38:'authorship',39:'authorship',40:'authorship',41:'third',42:'third',43:'third',44:'third',45:'third'}
inventory = load(O / 'slide-page-map.json')['pages']
pages = []
for lecture, mapping, basename in [(4,L4,'Lecture 4 More SQL.pdf'),(5,L5,'Lecture 5 FD  NFs.pdf')]:
    assigned = [x for x in inventory if x['source'] == basename]
    path = Path(assigned[0]['sourcePath'])
    reader = PdfReader(path)
    sourcehash = sha(path)
    for source in assigned:
        n = source['pdfPage']
        raw = reader.pages[n-1].extract_text()
        row = {'source': {'path': str(path),'sha256':sourcehash,'pdfPage':n,
                         'pageTextSha256':digest(unicodedata.normalize('NFKC',raw).replace('\u00ad','').strip()),
                         'normalization':'pypdfextract_text,NFKC,removeU+00AD,strip,UTF8SHA256'},
               'sourceReadStatus':'Fullpage text read; all23contact sheets00..22 visually inspected including all source screenshots and diagrams.',
               'observedContent':raw[:1000], 'pendingGaps':[], 'baselineCreditApplied':False,
               'sourceFiguresRead':[{'renderedPath':f'tmp/database-source/slides-lecture45/L{lecture}-page-{n:02}.png',
                   'renderedSha256':sha(W/f'tmp/database-source/slides-lecture45/L{lecture}-page-{n:02}.png'),
                   'visuallyInspected':True,'inspectionMode':'Four-pagecontactsheetoriginalresolution;rawtextreadseparately'}],
               'engineEvidence':'qa/usth-lecture45-checks.json:selectedactualSQLiteandfiniteFD/bagmodels,noMySQL/nativewebclaim'}
        if n not in mapping:
            row.update(status='non-instructional',semanticComparison='Cover/section/reference/objectives page; no additional substantive concept;topicgoalsimplementedinthefollowingreviewedteachingpages.',evidence=[],practiceCoverage='not-applicable-non-instructional')
        else:
            name,e,x,q,judgment = groups[mapping[n]]
            row.update(status='complete-current-evidence',semanticComparison=judgment,
              evidence=[witness(name,e,'teaching'),witness(name,x,'worked-example-or-proof'),
                        witness(name,f'{q}.','activity','## Luyện tập'),witness(name,f'{q}.','answer-rubric','## Đáp án và lập luận')],
              practiceCoverage='Answeredoriginal/equivalentskilltaskpluscomputedexample;sourceFDsystemexercisesalsofullyanswered,notgenerickeywordcredit.')
        pages.append(row)
assert len(pages)==92 and sum(p['status']=='complete-current-evidence' for p in pages)==85
out={'date':'2026-11-05','scope':'All47Lecture4+45Lecture5pages,personallyreadbodies/23original-resolutioncontactsheets and current USTH04/05 teaching/examples/18activities/answers. Does not certify Lecture6–9/practice.',
     'pages':pages,'counts':{'complete-current-evidence':85,'non-instructional':7},
     'checks':'qa/usth-lecture45-checks.json:19namedchecks,128independentFDclosureoracles,all5FDsystemskeys/normalforms,selectedactualSQLite queries.',
     'sourceErrata':['Non-INNERlabelmeansnon-equijoinwhichcanstillbeinner.','Selectionusesσnotδ.','Vennintersectionregionsmustbeoverlap.','ActualSELECTprojectiondistinctfromsourceSELECT*screenshots.','MySQLFULL/nestedaggregate/concat dialectcorrected.','FDkeyDDtypoandsinglePK2NF/RHSpruning/fullName1NFshortcutsrepaired.','NaturaljoinreconstructioncomparedwithoriginalR,notprojectedR1;spurioustuplesexplaininformationloss.']}
(O/'semantic-slides-lecture45-review.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print('Lecture4/5 reviewedpages',len(pages))
