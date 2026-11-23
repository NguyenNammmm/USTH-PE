"""Freeze manual full-body comparisons for analytics; text anchors only locate evidence."""
from pathlib import Path
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'output/database-advanced'
LESSONS=['AD18','AD19','AD70','AD71','AD72']

def sha(data):
    return hashlib.sha256(data).hexdigest()

# section, primary lesson reviewed, explanation locator, worked locator,
# answered activity, judgment. All own bodies were read directly, not inferred
# from source lexical hits, old lessons, parent headings or prior-agent intent.
REVIEWS=[
('11.1','AD72','Trong phạm vi sách, analytics/BI','Một truy vấn OLTP thường',5,'Analytics/BI, decision support, statistical analysis, interactive OLAP and predictive mining are distinguished; multi-source integration/history and workload separation are explained without claiming every future prediction is valid.'),
('11.2','AD72','Một truy vấn OLTP thường','Warehouse gom nhiều nguồn',5,'A consolidated historical repository gives a uniform analytical interface over differing sources and relieves source reporting load. Extraction still has a cost; warehouse data are not presumed identical copies or free of writes.'),
('11.2.1','AD72','Luồng cơ bản là sources','Data cleansing có những việc khác nhau:',5,'All components/issues are taught: source/destination driven capture, freshness/replication, schema integration, cleansing/fuzzy lookup, merge-purge versus householding, units/joins/routing, update propagation, summary information loss, ETL and ELT. Original unit/identity/frontier cases have an answered design activity.'),
('11.2.2','AD72','Một schema gốc cho bài','Fact bán hàng có một row',4,'Fact grain, dimensions/measures, short dimension keys, calendar dimension and star versus snowflake/multiple facts are explicit. History/version and bridge assumptions are added without treating a star schema as a grain proof.'),
('11.2.3','AD72','Row-oriented storage để','Minh họa lý tưởng 1 triệu',7,'Row/column layout, fixed-width offset intuition, selective-column I/O/cache/compression benefits and single-row tradeoff are explained, along with SQL/file-system architecture. The source overgeneralization that warehouses need no concurrency control is explicitly qualified for corrections, loaders, readers and publication.'),
('11.2.4','AD72','Data lake lưu raw CSV/JSON/logs','Một log thiếu field revenue',7,'A lake postpones schema integration across structured/unstructured formats, shifting parser/schema/quality work to query time; raw lineage and missing versus zero are tested. No current vendor recommendation is inferred from historical source examples.'),
('11.3','AD72','Cube trên d dimensions','Một report cố định day1',6,'The own OLAP introduction is matched to grouping dimensions and interactive analysis; source descendants are independently reviewed, not credited by this parent.'),
('11.3.1','AD72','Đừng lẫn số **groupings**','Hierarchy cần mappings có identity rõ:',6,'Cross-tab/cube cells, measures versus dimensions, ALL summaries, 2^d groupings versus product dense cell counts, pivot/slice/dice/rollup/drilldown and hierarchies are taught. An explicit counterexample proves coarse totals cannot reconstruct detail, and cube construction has an induction invariant and cost limits.'),
('11.3.2','AD72','Cross-tab hợp với display','Chẳng hạn (North,NULL,30,0,1)',2,'Fixed relational schema represents dynamic cross-tabs, flags distinguish subtotal NULL from real NULL, and dimension hierarchy mappings use identity keys rather than ambiguous names. Original detail/subtotal and missing-cell examples are used.'),
('11.3.3','AD72','ROLLUP(region,category) tạo hierarchy prefixes','Với ba dimensions (region,category,day)',6,'The whole source own body including OLAP implementation note is covered: pivot input/output and no implicit subtotal, cube powerset, ordered rollup prefixes, products of independent rollups, arbitrary grouping sets, grouping flags, MOLAP/ROLAP/HOLAP and selective/shared precomputation. SQL-standard syntax is separated from MySQL rewrites; no unexecuted SQL is reported as runtime evidence.'),
('11.3.4','AD72','Một report definition gồm query','Visualization giúp tìm patterns/anomalies',7,'Parameterized reusable report definitions, formatting/groups/page subtotals, query reexecution/chart refresh, maps/association heatmaps and interactive drill/filter are explained with original cases. Visual hypotheses require quantitative checking and valid denominators; source tool brands are not treated as current recommendations.'),
('11.4','AD19','Data mining là một phần','Một nhiệm vụ mining cần target',4,'Mining is semiautomatic KDD combining data representation, scalable execution and useful pattern/model selection; rules/equations/models and descriptive versus predictive goals are distinguished. Human preprocessing/postprocessing remains explicit.'),
('11.4.1','AD19','Một nhiệm vụ mining cần target','Một kho muốn dự đoán kiện',4,'Prediction/classification/regression, descriptive associations/clusters and textual tasks are connected to original business questions. Association may inspire a hypothesis but does not by itself establish causation; split/feature-time protocol is an original practical supplement.'),
('11.4.2','AD70','Kho muốn dự đoán một kiện','Model fitting không chỉ lưu training',1,'Classification learns from labeled training instances to predict a new instance class using available features. Continuous regression and unavailable future labels/features are separated; introductory completion does not credit classifier descendants.'),
('11.4.2.1','AD70','Algorithm greedy tree cho fixture hữu hạn:','Training một chiều x với nhãn y:',1,'Internal predicates/leaf classes and traversal are fully demonstrated; an original greedy construction adds stopping rules, node invariant, termination, complexity and generalization limits. The book omits construction details, so the extension is identified rather than attributed as a source solver proof.'),
('11.4.2.2','AD70','Bayes theorem:','Có class A 3 mẫu',2,'Bayes prior/likelihood/denominator argument, training distributions/histograms and conditional-independence product are taught with posterior arithmetic and joint-state sparsity explanation. Smoothing, log computation, fit-only-on-train and calibration limits are original explicit implementation policies.'),
('11.4.2.3','AD70','Một bài SVM một chiều','Với w≠0, khoảng cách',5,'Maximum geometric margin, support points, score-scale invariance, higher-dimensional hyperplanes, soft-margin/noise, kernel inner products and one-vs-rest multiclass are explained. No optimized SVM training or guaranteed accuracy is claimed by a hand-computed separator.'),
('11.4.2.4','AD70','Neural classifier ghép layers:','Ở multiclass output, có thể có',3,'Layer connections/weighted activations, output per class/argmax, learned weights and chain-rule backpropagation are explained with logistic/softmax and one gradient step. Deep/data dependence and train/validation separation are explicit; neither a toy calculation nor a sum-to-one output proves quality/convergence/calibration.'),
('11.4.3','AD70','Trong simple linear regression','Với points(1,2)',4,'Numeric target versus class and multivariable linear/curve-fitting principle are matched. Original simple least-squares equations, stationary/convexity reasoning, rank failure, residual and extrapolation limits make the source outline self-contained for the finite exercise.'),
('11.4.4','AD71','Rule A→B có support','Bốn baskets:',1,'Population/grain, support and asymmetric confidence, low-evidence patterns and uses of associations are explained with exact counts and lift baseline. Original Apriori construction adds soundness/completeness and finite-universe complexity, without claiming toy patterns are causal or validated useful recommendations.'),
('11.4.5','AD71','“Clustering” không có một objective','Collaborative filtering suy sở thích',6,'The source full body is matched: distance/centroid versus pairwise objectives, flat versus hierarchical groups, and collaborative filtering with alternating user/item grouping. Original Lloyd and agglomerative algorithms include traces/proofs/termination/cost policies; item-group profiles show how users without co-rated items can be related. No holdout quality or global-optimum guarantee is inferred.'),
('11.4.6','AD19','Entity recognition tìm một','Sentiment còn có thể theo **aspect**:',5,'Sentiment, entity mentions and identity disambiguation, structured extraction/relations, aspect-specific sentiment/location and knowledge-graph representation all have original examples with provenance. Graph structure does not validate extracted facts and ambiguous identity may remain unresolved.'),
('16.5.1','AD18','Có nhiều cách giữ view:','Để reload batch B không cộng lại',5,'Manual writer changes, triggers/full refresh, native maintenance when supported, incremental versus immediate/deferred refresh and consistency/freshness tradeoffs are explicit. Original replay/atomic batch protocol extends rather than assumes DBMS support.'),
('16.5.2','AD18','Sign +1 là insert một occurrence','Insert (4,A,20)',1,'Insert/delete differentials and update-as-delete-old/insert-new are explicit with signed multiplicity, before images and version assumptions. The source parent introduction is reviewed separately from all operator descendants.'),
('16.5.2.1','AD18','Proof cho một tuple pair khớp predicate:','Old R có r1, old S có s1',3,'Single-input source join insert/delete laws are covered by a more general signed bag identity, with explicit old/new snapshots and simultaneous cross term. Multiplicity polynomial supplies correctness; set union is not substituted for bag union.'),
('16.5.2.2','AD18','Selection và projection ở §16.5.2.2','base R={(A,2),(A,3),(B,4)}',5,'Selection forwards only matching changes, including predicate-crossing updates; projection DISTINCT needs derivation counts until the last witness disappears. Bag projection is distinguished and witness-count reasoning justifies the laws.'),
('16.5.2.3','AD18','Fact f=(event_id,group,amount)','MIN5,count3,sum35 lại không đủ',2,'COUNT/SUM/AVG state, all-NULL versus zero versus absent group and deletes are traced with an induction invariant. MIN/MAX deletion needs more information/recompute or ordered index; the original counterexample proves insufficiency of min/count/sum alone.'),
('16.5.2.4','AD18','Với **set** intersection/union/difference','Outer-join maintenance có điểm chuyển',5,'Set intersection/union/difference use both-side membership and transition laws; bags/DISTINCT need counts. Outer joins remove/add null-extended rows on first/last match transitions. Source intentionally leaves details open; original examples/answered exercises fill them.'),
('16.5.2.5','AD18','Để xử lý một expression','V=σ(a+b>6)(R⋈S)',5,'Bottom-up expression differentials propagate each child change with consistent versions; original simultaneous join/selection trace includes cross term. Structural induction, repeated base occurrences and DAG dependency handling are explained, without claiming a race-proof implementation from algebra alone.')
]

def witness(lesson,lines,locator,low=0,high=None):
    high=len(lines) if high is None else high
    found=[i for i in range(low,high) if locator in lines[i]]
    if not found:
        raise ValueError((lesson,locator))
    i=found[0];a=i;b=i+1
    if not re.match(r'^\d+\. ',lines[i]) and not lines[i].startswith('|'):
        while a>low and lines[a-1].strip(): a-=1
        while b<high and lines[b].strip(): b+=1
    text='\n'.join(lines[a:b])
    return {'path':f'output/database-advanced/lessons/{lesson}.md','lineStart':a+1,'lineEnd':b,
            'exactParagraph':text,'paragraphSha256':sha(text.encode('utf-8')),'locator':locator}

def main():
    inventory_raw=(BASE/'research/source-section-inventory.json').read_bytes()
    inventory=json.loads(inventory_raw)
    all_units=inventory['bookSections']
    assigned=[u for u in all_units if u['chapter']=='11' or (u['section'].startswith('16.5.') and 'AD18' in u.get('plannedAdvancedLessonIds',[]))]
    assert len(assigned)==len(REVIEWS)==29
    assert {u['section'] for u in assigned}=={r[0] for r in REVIEWS}
    lesson_data={id:(BASE/f'lessons/{id}.md').read_bytes() for id in LESSONS}
    validation_path=BASE/'qa/analytics-full-checks.json'
    validation=json.loads(validation_path.read_text(encoding='utf-8'))
    if not validation['allPassed'] or validation['lessonSha256']!={id:sha(data) for id,data in lesson_data.items()}:
        raise ValueError('Complete semantic freeze requires the current approved finite/integrity QA report.')
    units=[]
    for section,lesson,explanation,worked,activity,judgment in REVIEWS:
        spec=next(u for u in assigned if u['section']==section)
        source_path=spec['sourcePath'].replace('\\','/')
        data=(ROOT/source_path).read_bytes()
        raw_lines=data.splitlines(keepends=True)
        following=[u['sourceLine'] for u in all_units if u['chapter']==spec['chapter'] and u['sourceLine']>spec['sourceLine']]
        end=min(following)-1 if following else spec['scopeLineEnd']
        own=b''.join(raw_lines[spec['sourceLine']-1:end])
        lines=lesson_data[lesson].decode('utf-8-sig').splitlines()
        p_start=lines.index('## Luyện tập')+1;p_end=lines.index('## Gợi ý')
        a_start=lines.index('## Đáp án và lập luận')+1;a_end=lines.index('## Biến thể và cách kiểm')
        units.append({
            'section':section,'title':spec['title'],'primaryLesson':lesson,
            'inventoryOwners':spec.get('plannedAdvancedLessonIds',[]),
            'status':'covered-after-fix','semanticStatus':'complete','baselineCreditApplied':False,
            'source':{'path':source_path,'sha256':sha(data),'rawSha256':sha(data),'ownLineStart':spec['sourceLine'],
                      'ownLineEnd':end,'ownBodySha256':sha(own),'ownBodyWordCount':len(own.decode('utf-8-sig').split()),
                      'sourcePdfPage':spec['sourcePdfPage'],'readInFull':True,
                      'rangePolicy':'Own body ends immediately before the next numbered heading in the same chapter; final chapter own body ends at the reviewed pre-Summary boundary.'},
            'lessonSha256':sha(lesson_data[lesson]),
            'explanation':witness(lesson,lines,explanation),
            'workedExampleOrTrace':witness(lesson,lines,worked),
            'activity':witness(lesson,lines,f'{activity}. ',p_start,p_end),
            'answer':witness(lesson,lines,f'{activity}. ',a_start,a_end),
            'semanticJudgment':judgment,
            'algorithmProofAssessment':(
                'Original finite algorithms/proofs extend the source outline; their arithmetic/invariants are checked, not claimed as empirical model quality or global optimizer guarantees.' if lesson in ['AD70','AD71'] else
                'Differential laws include state/version assumptions and multiplicity or membership reasoning; operator composition is by induction. Finite checks supplement universal arguments, not transaction-runtime evidence.' if lesson=='AD18' else
                'Cube construction has an induction invariant and explicit exponential grouping cost; reports/storage/ETL examples are design/model evidence, not measured runtime.' if lesson=='AD72' else
                'The source introduces task families and text mining; the lesson adds an explicit evaluation protocol/provenance contract, not a trained or quality-validated ML artifact.')
        })
        for kind in ('explanation','workedExampleOrTrace','activity','answer'):
            units[-1][kind]['lessonSha256']=sha(lesson_data[lesson])
            units[-1][kind]['lessonHashPath']=f'output/database-advanced/lessons/{lesson}.md'
    sheets=[f'tmp/pdfs/analytics-source/contact-{i}.png' for i in range(1,7)]
    ledger={
        'auditType':'Full source semantic continuation: warehouse, OLAP, mining and materialized-view maintenance',
        'date':'2026-11-05','status':'complete','semanticStatus':'complete','scopeLessonIds':LESSONS,
        'scopeNote':'All22 chapter11 own bodies plus seven AD18-mapped section16.5 bodies were directly read and compared to full current lessons. AD37 is a secondary inventory owner and was not edited or credited by this batch. Unassigned16.5 parent was read for context;16.5.3/16.5.4 remain outside this batch. No baseline lesson or prior-agent intent receives credit. USTH page review is coordinated separately by root.',
        'inventorySha256':sha(inventory_raw),'sourceBookSha256FromInventory':inventory['sourceBook']['sha256'],
        'lessonSha256':{id:sha(data) for id,data in lesson_data.items()},
        'counts':{'assignedUnits':29,'coveredAfterFix':29,'partial':0,'pending':0,
                  'chapter11Units':22,'ad18Units':7,'sourceOwnBodyWords':sum(u['source']['ownBodyWordCount'] for u in units)},
        'readRangesByReviewer':{'reviewer':'er_full_gate_complete',
            'sourceFullContiguousRanges':{'tmp/database-source/chapter-11.txt':[[1,1645]],'tmp/database-source/chapter-16.txt':[[1478,1654]]},
            'lessonsFullyRead':[f'output/database-advanced/lessons/{id}.md' for id in LESSONS],
            'figuresInspected':[f'11.{i}' for i in range(1,13)],
            'sourcePdfPagesInspected':[551,554,557,558,559,560,561,562,563,568,571,573],
            'renderedContactSheets':[{'path':p,'sha256':sha((ROOT/p).read_bytes()),'visuallyInspected':True} for p in sheets]},
        'changesThisContinuation':[
            'AD18 adds manual/trigger/native and immediate/deferred maintenance, set membership differential laws and bottom-up expression/DAG trace with independent answered activity.',
            'AD19 adds semiautomatic KDD boundaries, entity mention/linking ambiguity, aspect sentiment, structured facts/knowledge-graph provenance and a complete answered activity.',
            'AD70 adds joint-configuration sparsity, histogram boundary, geometric SVM/support vectors, multiclass softmax and a numerical gradient update with an answered activity; no training-quality claim.',
            'AD71 adds objective distinctions and explicit item-group collaborative filtering/co-clustering protocol, missing/holdout/termination limits and an answered activity.',
            'AD72 adds analytics/decision-support roles, complete warehouse components/cleansing/schema integration/ETL/ELT/freshness, concrete star/snowflake dimensions, cube cells/grouping sets/hierarchy limits, relational cross-tab/pivot, MOLAP/ROLAP/HOLAP/partial aggregates, row-column tradeoffs, lake query contracts and reporting/visualization with three answered activities.'
        ],
        'sourceCaveats':[
            'Chapter11.2.3 says warehouse records are never updated and therefore no concurrency-control overhead is needed. The lesson explicitly limits that simplifying model and retains snapshot/refresh/correction coordination.',
            'Figure11.7 displays repeated dark/pastel values inconsistent with the source fact rows/earlier cross-tab. Lesson fixtures and totals are original and computed independently.',
            'Section16.5.2.3 count(B) prose omits SQL NULL detail; lesson distinguishes row_count and nonnull_count and preserves SQL SUM/AVG all-NULL/group-disappearance behavior.',
            'Book omits many ML solver and tree-building details. Original toy algorithms/proofs/calculations teach mechanics; neither model quality, convergence for every solver nor large-data benchmark is inferred.',
            'Historical vendor/tool support statements are not repeated as current recommendations. MySQL examples are explicitly expected outputs, not SQL execution evidence.'
        ],
        'validation':{'path':'output/database-advanced/qa/analytics-full-checks.json','sqlRuntimeUsed':False,'heavyTrainingRuntimeUsed':False,
                      'allPassed':True,'checkCount':len(validation['checks']),'reportSha256':sha(validation_path.read_bytes()),
                      'claimLimit':'Finite answer/model checks and cryptographic freshness supplement the manual full-source content judgments. They do not automatically establish source completeness, model quality or runtime/transaction performance.'},
        'units':units
    }
    (BASE/'research/semantic-analytics.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'counts':ledger['counts'],'lessonSha256':ledger['lessonSha256']},ensure_ascii=False))

if __name__=='__main__':main()
