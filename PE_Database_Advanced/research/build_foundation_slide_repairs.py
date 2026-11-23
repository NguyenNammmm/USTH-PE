"""Manual per-page gap closure for the 66 explicitly reviewed foundation pages.

The lookup table records a human comparison. Hash checks preserve that reviewed
snapshot, and must not be auto-refreshed after arbitrary content changes.
"""
from pathlib import Path
import copy
import hashlib
import json
import re

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
load = lambda p: json.loads(Path(p).read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
approved = load(O / 'root-reviewed-snapshots.json')['lessons']
lines = {}
for name in ['USTH01', 'USTH02', 'USTH03']:
    p = R / 'lessons' / f'{name}.md'
    assert sha(p) == approved[name], 'Direct page/content rereview required'
    lines[name] = p.read_text(encoding='utf-8').splitlines()


def witness(name, prefix, kind, heading=None):
    source = lines[name]
    candidates = []
    h = None
    for i, s in enumerate(source):
        if s.startswith('## '):
            h = s
        if s.startswith(prefix) and (heading is None or h == heading):
            candidates.append(i)
    assert len(candidates) == 1, (name, prefix, heading, candidates)
    a = b = candidates[0]
    while b + 1 < len(source) and source[b + 1].strip():
        b += 1
    fragment = '\n'.join(source[a:b + 1])
    return {'kind': kind, 'path': f'lessons/{name}.md', 'lessonSha256': approved[name],
            'lineRange': [a + 1, b + 1], 'paragraphAnchor': prefix,
            'paragraphExcerpt': fragment,
            'fragmentSha256': hashlib.sha256(fragment.encode()).hexdigest(), 'baselineActuallyRead': False}


# page:(teaching paragraph,example paragraph,practice number,actual judgment)
mapping = {
1: {
 15: ('Các hệ file buộc', '| Bachman/network', 1, 'Named early-system milestones reconciled; dates serve model/access changes rather than fabricated exact invention chronology.'),
 16: ('| Codd và', '| IBM, SQL', 1, 'SystemR project versus1981 retrospective and initialANSI1986 versusSQL92 revision corrected; later model/format/product classes distinguished.'),
 18: ('DBMS có thể nằm', 'Ví dụ máy ghi ảnh', 2, 'Embedded/device resource/offline/recovery versus large parallel cluster and coordination-overhead countercase, with transfer design task.'),
 19: ('Integration nối nguồn', 'Ở phía phân tích', 3, 'Two-tier/three-tier already current inAD67; multimedia/time-series storage and integration/warehouse/mining distinctions now have actual worked situations and answer-backed transfer.'),
 23: ('Ở phía phân tích', 'Integration nối nguồn', 3, 'Image/audio/video/sampled-time-series/derived-feature preservation and provenance requirements, not just generic BLOB word.'),
 28: ('Application developer viết', 'Ví dụ query đăng ký', 4, 'DBMS implementer/tool-developer/operator/DBA responsibilities with concrete diagnosis/assignment and multi-team answer.'),
 31: ('Với `SELECT name', 'Với một UPDATE trong transaction', 5, 'Actual source image read: query/update path, single/double boxes, buffers/lock table memory state, control+data versus data-only arrows; tree task and rubric.'),
 33: ('Tên DB2,', 'Integration nối nguồn', 3, 'Product versions explicitly historical rather than currentranking; exact retrieval/warehouse versus inferred prediction distinguished in original example/task.'),
 34: ('Integrity constraint loại', 'Rule có thể suy', 6, 'Constraint enforcement, rule-derivedeligibility and outside email effects separated; retry/outbox task and actual answer.'),
 35: ('Một script đọc file', 'Một vòng điều khiển', 7, 'Cost/overhead versus atomicrecovery even withoneuser; concretefile/embedded/harddeadline choices with requirements and answer.'),
 36: ('Capability mismatch khác', 'Nếu yêu cầu query', 8, 'Unsupported data/operations versus merelyunnecessary overhead, explicit point-lookup-only versus required enginejoin counterexample and decision task.'),
},
2: {
 11: ('Với `Member', 'Nếu `phone`', 1, 'Domain as allowedvalues/type and modeling-relative atomicity; string-name versus embedded phone set, redesigned relation and applied answer.'),
 21: ('Left semijoin', 'Với set semantics', 2, 'Left-result schema and existence semantics; setprojection equivalence versusSQLbag leftduplicates/right-witness amplification and DISTINCTloss.'),
 22: ('Chọn sáu phép', 'Theta join được', 3, 'Sixchosen setalgebra primitives and join/intersection derivation with independent parse/result tasks.'),
 28: ('Cho `Sale', 'Kết quả schema', 4, 'Computed/repeated attributes with separatealiases/types and setcollapse versusSQLbag, fullindependent result answer.'),
 47: ('Nested expression là', 'Đọc từ lá', 5, 'Same OR query inassignments,nestedexpression and annotatedlogicaltree, intermediate schemas/results and logical/physical distinction.'),
 49: ('Quy ước ưu tiên', 'Chẳng hạn', 3, 'Stated unary/product-join/intersection/union-difference precedence, recommendation toparenthesize, actualdifferent result counterexample.'),
 50: ('Đọc từ lá', 'Không giả định FK', 5, 'Leavesrelations/operatorsinternal, schema/result at every branch, independentlybuilt tree required and answer rubric.'),
 51: ('Không giả định FK', 'Nested expression là', 5, 'Original compatible one-columnOR branches,assignments/nested/tree and missing-side rows explicitlypreserved.'),
 52: ('Đọc từ lá', 'Nested expression là', 5, 'Rootunion after branch selection/projection/rename compatibility; exact intermediate values and new E transfer test.'),
 54: ('Muốn tìm room', 'Phải đổi tên cả', 6, 'Two-distinct-witness selfjoin with all namesdisambiguated, noidenticalrowwitness, source naturaljoin cost-equality ambiguity explained and alteredpredicate task.'),
 55: ('Anti-semijoin tìm', 'Muốn tìm room', 15, 'Newdevice-bank threshold/type/conjunction/join/compatibleunion/anti/memoryduplicate/two-model/two-rate skills have complete originalexpressions and witness answers inq7/q15.'),
 60: ('Dùng OR vì', 'Cho `Order', 8, 'SourceANDofnonkeydifferences correctedtoOR; samekey/onedifferingfieldcounterexample, uniqueness versusminimality and explicitsetnoNULL assumptions.'),
 61: ('Với `Booking', 'Dùng OR vì', 9, 'CompositeFD-as-emptyselfjoin, twoattribute equality plusdifferingowner, counterexample and candidatekeyminimality notinferredfromsample.'),
 63: ('Foreign key trong', 'Child có P1', 10, 'Rename-compatible projectiondifference inclusion withmissingparent/emptychild, NULL/targetkeyanddomainqualifications.'),
 64: ('Child có P1', 'Foreign key trong', 10, 'Original childparent trace withviolationP9 andemptychild case; inclusiondirection andresult schema explicit.'),
 65: ('Cho `Instrument', 'SQL CHECK nhận', 11, 'Allowedmode relation violation, noNULLtwo-valuedversusSQLUNKNOWN difference and independent classification answer.'),
 66: ('Cho `Instrument', 'Giá đúng700', 11, 'Newthreshold implication violation rate<50 ANDprice>700 withstrict/equalityboundaries and independentanswer.'),
 67: ('“Nếu memory<16', 'Một thiết bị memory8', 11, 'Conditionaldisjunction negatedwholeconsequentviaDeMorgan, equalityboundaries, implicationnotconverse and truth-table checks.'),
 68: ('Cho Portable', 'L16/800', 12, 'Two-table pairviolation larger-memoryANDnot-larger-price; emptyproduct/vacuity andpriceequalitycountercase, independentresult.'),
 69: ('“Không maker', 'Nếu mỗi relation', 13, 'Directprojecteddomain disjointness andemptyintersection criterion; newmaker task relates direct andindirectrepresentations.'),
 70: ('Nếu Catalog', 'Lấy maker bất kỳ', 13, 'Categorymembership throughCatalogmodeljoin beforemakerprojection; missingjoinfalsepositivecounterexampleandanswer.'),
 71: ('Constraint “model số', 'Domain model ở đây', 14, 'Orderednumericmodel monotonicpair andsame-modelstrictresourcepolicy; uniquemodelvacuity versusConfiggrain, explicitall-versusanyresourcecondition.'),
},
3: {
 5: ('SQL là Structured', 'MySQL,PostgreSQL', 1, 'Correctname/origin, languageversusDBMS/client/OS and noformalunder100wordsclaim.'),
 6: ('MySQL,PostgreSQL', 'Browser của khóa', 1, 'Actualimage-onlylogos classified asDBMS versusOS; browserclient/backend path statedwithappliedclassificationanswer.'),
 8: ('Chuẩn ANSI SQL1986', 'Một feature được', 2, 'Standards evolution1986/87,1992,1999,2003,2006,2008 distinguished fromengineversion/capability andnotcalledlateststandard.'),
 12: ('Cả đoạn tới', 'SELECT,AS,WHERE,DESC', 1, 'Statement/clause/keyword/identifier/literal parsedonoriginalSQL; reservedkeyword contextclarified.'),
 13: ('Keyword SELECT', 'Bài dùng lowercase', 1, 'KeywordcaseversusidentifierOS/configdependence, explicitconsistentnamingconventionandcountertask.'),
 14: ('Thụt dòng làm', 'Với query lồng', 2, 'Format nestedquerypreservingliteral/token/meaning, independentreformattingtaskandsemanticrubric.'),
 15: ('MySQL cần whitespace', 'Chuỗi', 2, 'Line/blockcomments,MySQLdouble-dashwhitespace,stringboundaryandspecialcommentcaveat;repairtaskanswered.'),
 17: ('Backend cấp schema', 'Sau ALTER,', 9, 'DDL commands alreadycurrentinAD01; actualrename/dropcolumn/createtableactivity andmanagedschema/connection semanticsnowconcrete.'),
 18: ('Sơ đồ Company', 'Có tám cạnh FK', 5, 'Actualsixrelationdiagramread,allattributesincludingMinit,allprimary/compositekeysandeightFKedgesexplicit;notgenericUniversitycredit.'),
 19: ('Có tám cạnh FK', 'Một Department có', 5, 'AllsourceFKs,selfreference,manager-departmentcycle andwhatFKdoesnotprove; appliedcompleteedge/keyanswer.'),
 20: ('Backend cấp schema', 'USE chọn default', 9, 'CREATEschema/backendallocationversusconnectionUSE andvisiblecurrentcontext, web-onlytaskandanswer.'),
 22: ('Bit string biểu', 'ID như000001', 3, 'Bitpositionsversusinteger,domain/typeportability andoriginaltypechoicetask;nativeMySQLCHECKadaptationexplicit.'),
 23: ('Trong MySQL, BOOL', 'Bit string biểu', 3, 'Date/time,Booleanaliasnot0/1constraint,DECIMALexactscaleversusFLOAT(p)dialectprecision;appliedanswer.'),
 24: ('Ví dụ DDL sau', 'Tất cả bảng', 6, 'FullEmployee/DepartmentcircularDDLstrategy,DATEandNULL/defaultpolicyexplained,validloadsequenceandALTERanswer.'),
 25: ('Tất cả bảng', 'Nạp Department', 6, 'NoFKdisable;createwithoutoneedge,addconstraintwhenvalid,loadnullablemanagerthenupdate,notassumeddeferredchecks.'),
 26: ('Với cross-column', 'Ngày bằng nhau', 6, 'Cross-column dateCHECKwithNULLpolicyandbefore/equal/NULLboundaryanswers,originalCREATEnotsourcemisspelling.'),
 28: ('Hours1 và56', 'PK composite ngăn', 7, 'Fulltwo-parentWorks_OnDDL,PK/FKs,NOTNULLand1..56CHECK,accepted/rejectedboundaryindependenttask.'),
 30: ('Sau ALTER,', 'Khi thu hồi fixture', 9, 'OriginalDROP COLUMNbefore/afterschema/rowandprecisepreconditions;notclaimallmigrationmeansbaddesign.'),
 31: ('Đổi Department.dnumber', 'Cascade delete manager', 8, 'ParentkeyupdatecascadeversusdeleteSETNULL/RESTRICT,nullablepreconditionandunsupportedInnoDBSETDEFAULTqualified.'),
 32: ('Cascade delete manager', 'Nếu manager field', 8, 'Managerpolicychoicetraced,departmentdeletionversusretentiondistinguishedandactualresult/rubric.'),
 33: ('Đổi Ssn101', 'Không hứa self-referential', 8, 'SourceSSN/ESSNidentifierandREFERENCES corrected;selfreferenceupdateRESTRICTchosen,deleteSETNULLtraceanddifferenttableupdateCASCADEseparated.'),
 34: ('Backend cấp schema', 'Khi thu hồi fixture', 9, 'SHOW/USE/DESCRIBEscopeandDROPdefinitionsversusrows,correctspellinganddedicatedwebcleanup;notuserterminal.'),
 38: ('TOP PERCENT', 'Với7 hàng', 10, 'SQLServerdialectmarked;newceilpercentafterfilter/tiepolicywithfullMySQLwindowrewriteandexactresult.'),
 45: ('Alias annual_salary', 'Alias có dấu cách', 10, 'Space-containingheadingwithbackticksandANSI_QUOTESversusliteral,computedaliasandindependentorderinganswer.'),
 48: ('MySQL8.4 có thể', 'Ví dụ eligible', 10, 'Toppercentfilterdenominator,roundingandtiesdefined;notgenericLIMITequatedwithPERCENT.'),
 52: ('CHAR có độ dài', 'Với VARCHAR dùng', 4, 'DeclaredPADSPACE/NOPAD/VARCHARcomparisonandCHARretrievaldistinguished,actualpredictiontaskandmetadataanswer.'),
 58: ('`ORDER BY 2', 'ORDER BY chưa', 10, 'Computedalias/expressionandpositiveordinal,zeroinvalid,stabletiebreak andLIMITfollowingORDERBYqualified.'),
 59: ('Alias annual_salary', '`ORDER BY 2', 10, 'Originalannualcomputedcolumnalias/ordinalsorttaskandanswer,notonlygenericORDERBYmention.'),
 60: ('Ví dụ riêng trong', 'Khi thu hồi fixture', 9, 'ThreeoriginalsmalltablesfullDDL/dropdependencyorder/schemaandrowstateanswer,isolatedfixture.'),
 62: ('Sau ALTER,', 'Khi thu hồi fixture', 9, 'ThreenewcolumnsremovedwithcompleteALTERcommandsandbefore/afteranswer,notfrozensnapshotedited.'),
 67: ('Target nhận', 'Từ cùng trạng thái', 11, 'ActualfilteredINSERTSELECTsource/targetschema,data,expectedIDs,duplicateconflictandnewfixturetaskanswered.'),
 70: ('Từ cùng trạng thái', 'Predicate', 12, 'OriginalDELETEallversusnullable-reference-subset,retainedIDsandfullSQLansweronfreshbranchfixtures.'),
 71: ('Từ cùng trạng thái', 'Mỗi nhánh hoạt động', 12, 'UPDATEconstantwith/withoutISNULL,changed/unchangedrowsandfullanswer,branchresetexplicit.'),
}}


def find_literal(name, phrase):
    # Mapping uses semantic phrases; record the exact containing paragraph,
    # never a regex token match as proof of completeness.
    teaching = '\n'.join(lines[name]).split('## Luyện tập\n', 1)[0]
    paras = [x for x in teaching.split('\n\n') if x.strip()]
    found = [p for p in paras if phrase in p]
    assert len(found) == 1, (name, phrase, len(found))
    return found[0].splitlines()[0]


base = load(O / 'semantic-slides-foundations.json')
pages = []
for prior in base['pages']:
    if prior['status'] != 'partial':
        continue
    lecture = int(re.search(r'Lecture (\d)', prior['source']['path']).group(1))
    page = prior['source']['pdfPage']
    name = f'USTH0{lecture}'
    e, x, n, judgment = mapping[lecture][page]
    row = copy.deepcopy(prior)
    row['previousGaps'] = row.pop('pendingGaps')
    row['pendingGaps'] = []
    row['status'] = 'complete-current-evidence'
    row['semanticComparison'] = judgment
    row['evidence'] = [witness(name, find_literal(name, e), 'teaching'),
                       witness(name, find_literal(name, x), 'worked-example'),
                       witness(name, f'{n}.', 'activity', '## Luyện tập'),
                       witness(name, f'{n}.', 'answer-rubric', '## Đáp án và lập luận')]
    row['sourceReadStatus'] = 'full-page-text-reread-and-original-figures-reviewed-where-needed;prior-fullpage-audit-retained'
    row['practiceCoverage'] = 'Original equivalent-skill practice with explicit answer/rubric in new supplement; existing source core evidence retained in prior ledger.'
    row['baselineCreditApplied'] = False
    row['engineEvidence'] = 'qa/usth-foundations-supplement-checks.json;selectedSQLite/finiteRAonly,notMySQLDDL/collation/nativewebexecution'
    pages.append(row)
assert len(pages) == 66
out = {'date': '2026-11-05', 'scope': 'Manual closure of66specificpartialpages from lectures1–3 only, afterdirectsourcepage/contentreading and35originalansweredactivities. Does not certify untouched lecture4–9/practicepages.',
       'previousLedger': 'research/semantic-slides-foundations.json',
       'pages': pages, 'counts': {'complete-current-evidence': len(pages)},
       'checks': 'qa/usth-foundations-supplement-checks.json',
       'figureRereview': ['Lecture1p31','Lecture2p21,p60','Lecture3p6,p18'],
       'note': 'Source discrepancies corrected explicitly. No source dates, raw practice bank, obsolete product lists or dialect-specificsyntax blindly copied as current behavior.'}
(O / 'semantic-slides-foundation-repairs.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print('Foundation slide repairs', len(pages))
