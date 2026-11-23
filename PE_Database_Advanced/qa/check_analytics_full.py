"""Analytics finite-answer checks plus frozen source/lesson witness integrity.

These are not ML training, SQL runtime, empirical quality or semantic-depth
classifiers. Human full-body comparisons live in semantic-analytics.json.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict
import hashlib,json,math,re

ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'output/database-advanced'

def sha(data):return hashlib.sha256(data).hexdigest()

def subsets(values):
    values=tuple(values)
    return [frozenset(c) for n in range(len(values)+1) for c in combinations(values,n)]

def apriori(transactions,threshold):
    universe=sorted(set().union(*transactions))
    support=lambda c:sum(c<=t for t in transactions)
    previous={frozenset([v]) for v in universe if support({v})>=threshold}
    result=set(previous);k=2
    while previous:
        candidates={a|b for a in previous for b in previous if len(a|b)==k}
        candidates={c for c in candidates if all(frozenset(s) in previous for s in combinations(c,k-1))}
        previous={c for c in candidates if support(c)>=threshold}
        result.update(previous);k+=1
    return result

def cube(rows,d):
    result=Counter()
    for *dimensions,amount in rows:
        for mask in range(1<<d):
            values=tuple(dimensions[i] if mask&(1<<i) else None for i in range(d))
            result[(mask,values)]+=amount
    return result

def join_counts(r,s):
    out=Counter()
    for (rk,rv),rm in r.items():
        for (sk,sv),sm in s.items():
            if rk==sk:out[(rk,rv,sv)]+=rm*sm
    return out

def signed_add(*values):
    out=Counter()
    for value in values:
        for key,count in value.items():out[key]+=count
    return {k:v for k,v in out.items() if v}

def aggregate(values):
    nonnull=[x for x in values if x is not None]
    return None if not values else (len(values),len(nonnull),sum(nonnull),sum(nonnull)/len(nonnull) if nonnull else None)

def merges(points,link):
    clusters=[(x,) for x in sorted(points)];heights=[]
    while len(clusters)>1:
        options=[]
        for i,j in combinations(range(len(clusters)),2):
            distances=[abs(a-b) for a in clusters[i] for b in clusters[j]]
            distance=min(distances) if link=='single' else max(distances)
            options.append((distance,clusters[i],clusters[j],i,j))
        distance,a,b,i,j=min(options)
        heights.append(distance)
        clusters=[c for n,c in enumerate(clusters) if n not in (i,j)]+[tuple(sorted(a+b))]
        clusters.sort()
    return heights

def main():
    checks=[]
    def check(name,value,details=None):checks.append({'name':name,'passed':bool(value),'details':details})
    inventory_raw=(BASE/'research/source-section-inventory.json').read_bytes()
    inventory=json.loads(inventory_raw)
    ledger_path=BASE/'research/semantic-analytics.json'
    ledger=json.loads(ledger_path.read_text(encoding='utf-8'))
    expected={u['section']:u for u in inventory['bookSections'] if u['chapter']=='11' or (u['section'].startswith('16.5.') and 'AD18' in u.get('plannedAdvancedLessonIds',[]))}
    check('exact29 assigned own bodies, no baseline blanket credit',
          len(expected)==len(ledger['units'])==29 and set(expected)=={u['section'] for u in ledger['units']} and
          all(u['status']=='covered-after-fix' and u['source']['readInFull'] and not u['baselineCreditApplied'] for u in ledger['units']))
    check('inventory and five approved lesson hashes fresh',sha(inventory_raw)==ledger['inventorySha256'] and all(
        sha((BASE/f'lessons/{id}.md').read_bytes())==value for id,value in ledger['lessonSha256'].items()))
    source_errors=[];witness_errors=[]
    for row in ledger['units']:
        spec=expected[row['section']];source=row['source']
        data=(ROOT/source['path']).read_bytes();lines=data.splitlines(keepends=True)
        following=[u['sourceLine'] for u in inventory['bookSections'] if u['chapter']==spec['chapter'] and u['sourceLine']>spec['sourceLine']]
        end=min(following)-1 if following else spec['scopeLineEnd']
        own=b''.join(lines[spec['sourceLine']-1:end])
        if not (source['rawSha256']==sha(data) and source.get('sha256',source['rawSha256'])==sha(data) and source['ownLineStart']==spec['sourceLine'] and
                source['ownLineEnd']==end and source['ownBodySha256']==sha(own) and
                source['ownBodyWordCount']==len(own.decode('utf-8-sig').split())):source_errors.append(row['section'])
        for kind in ('explanation','workedExampleOrTrace','activity','answer'):
            witness=row[kind];raw=(ROOT/witness['path']).read_bytes();lesson_lines=raw.decode('utf-8-sig').splitlines()
            exact='\n'.join(lesson_lines[witness['lineStart']-1:witness['lineEnd']])
            if not (exact==witness['exactParagraph'] and sha(exact.encode())==witness['paragraphSha256'] and
                    row['lessonSha256']==sha(raw) and witness.get('lessonSha256',row['lessonSha256'])==sha(raw)):
                witness_errors.append([row['section'],kind])
    check('source raw/own hashes and next-heading boundaries exact',not source_errors,source_errors)
    check('all116 exact explanation/example/activity/answer witnesses fresh',not witness_errors,witness_errors)
    check('all12 source figures remain frozen and inspected',all(f['visuallyInspected'] and sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in ledger['readRangesByReviewer']['renderedContactSheets']))
    activity_counts={}
    for id in ledger['scopeLessonIds']:
        lines=(BASE/f'lessons/{id}.md').read_text(encoding='utf-8-sig').splitlines()
        p=lines.index('## Luyện tập');h=lines.index('## Gợi ý');a=lines.index('## Đáp án và lập luận');b=lines.index('## Biến thể và cách kiểm')
        numbers=lambda part:[int(m.group(1)) for line in part if (m:=re.match(r'^(\d+)\. ',line))]
        questions=numbers(lines[p:h]);answers=numbers(lines[a:b]);activity_counts[id]=len(questions)
        check(f'{id} every independent activity has numbered answer',questions==answers==list(range(1,len(questions)+1)),len(questions))

    check('classification confusion metrics and imbalanced baseline',
          (9+7)/20==.8 and 9/(9+3)==.75 and 9/(9+1)==.9 and 7/(7+3)==.7 and
          math.isclose(2*9/(2*9+3+1),9/11) and 90/100==.9 and 0/10==0)
    gini=lambda counts:1-sum((n/sum(counts))**2 for n in counts if n)
    gain15=gini([2,2])-(1/4*gini([1,0])+3/4*gini([1,2]))
    gain25=gini([2,2])-(2/4*gini([2,0])+2/4*gini([0,2]))
    check('greedy tree split gains and inference',math.isclose(gain15,1/6) and gain25==.5 and (0 if 2.2<=2.5 else 1)==0)
    priors=[3/4,1/4];likelihood=[2/3,1]
    scores=[p*l for p,l in zip(priors,likelihood)];posterior=[x/sum(scores) for x in scores]
    check('Bayes prior normalization, bin boundary and Laplace zero policy',
          math.isclose(posterior[0],2/3) and math.isclose(posterior[1],1/3) and
          5<=5<10 and (0+1)/(3+2)==.2)
    distance=lambda x,w,b:abs(w*x+b)/abs(w)
    check('SVM geometric distance is score-scale invariant',distance(2,2,0)==distance(2,1,0)==2 and
          min(distance(x,1,0) for x in [-2,-1,1,2])==1 and min(abs(x-.5) for x in [-2,-1,1,2])==.5)
    z=.5;p=1/(1+math.exp(-z));gradient=[p-1,2*(p-1),p-1]
    update=[.5-.1*gradient[0],.5-.1*gradient[1],-1-.1*gradient[2]]
    softmax=[math.exp(x)/sum(math.exp(y) for y in [0,math.log(2),0]) for x in [0,math.log(2),0]]
    check('logistic gradient update and multiclass softmax arithmetic',
          math.isclose(p,.6224593312018546) and all(math.isclose(x,y,abs_tol=1e-6) for x,y in zip(update,[.537754,.575508,-.962246])) and
          all(math.isclose(x,y) for x,y in zip(softmax,[.25,.5,.25])),{'update':update,'softmax':softmax})
    x=[1,2,3];y=[3,5,7];xm=sum(x)/3;ym=sum(y)/3
    slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x);intercept=ym-slope*xm
    residual=[intercept+slope*a-b for a,b in zip(x,y)]
    check('least squares coefficient, stationary residual and rank failure',slope==2 and intercept==1 and intercept+slope*4==9 and
          sum(residual)==0 and sum(a*r for a,r in zip(x,residual))==0 and sum((a-2)**2 for a in [2,2,2])==0)
    baskets=[frozenset('AB'),frozenset('ABC'),frozenset('AC'),frozenset('BC')]
    support=lambda items:sum(set(items)<=t for t in baskets)
    check('support confidence lift and changed transaction population',support('AB')/4==.5 and
          math.isclose((support('AB')/support('A'))/(support('B')/4),8/9) and
          support('AB')/(support('A')+1)==.5 and support('AB')/support('B')==2/3)
    universe=frozenset('ABC');possible=subsets(universe);apriori_errors=[];apriori_cases=0
    for transactions in product(possible,repeat=3):
        for threshold in [1,2,3]:
            brute={s for s in possible if s and sum(s<=t for t in transactions)>=threshold}
            if apriori(transactions,threshold)!=brute:apriori_errors.append([transactions,threshold])
            apriori_cases+=1
    check('Apriori candidate/prune result versus exhaustive itemset oracle',not apriori_errors,{'finiteCases':apriori_cases,'failures':len(apriori_errors)})
    points=[0,2,8,10];centers=[0,10]
    assigned=[[x for x in points if min(range(2),key=lambda j:(abs(x-centers[j]),j))==i] for i in range(2)]
    means=[sum(c)/len(c) for c in assigned]
    old_sse=sum((x-centers[i])**2 for i,c in enumerate(assigned) for x in c)
    new_sse=sum((x-means[i])**2 for i,c in enumerate(assigned) for x in c)
    mean_identity=all(math.isclose(sum((x-c)**2 for x in values),sum((x-sum(values)/len(values))**2 for x in values)+len(values)*(sum(values)/len(values)-c)**2)
                      for values in [[0,2],[8,10],[1,1,4]] for c in [-3,0,1,9,12])
    check('Lloyd step and mean minimizer identity',means==[1,9] and old_sse==8 and new_sse==4 and mean_identity)
    check('hierarchical single-link versus complete-link merge heights',merges(points,'single')==[2,2,6] and merges(points,'complete')==[2,2,10])
    ratings={'U4':{'A':5,'C':1},'U5':{'B':5,'D':1},'U6':{'A':5}}
    groups=[set('AB'),set('CD')]
    profile=lambda user:[(sum(v for item,v in ratings[user].items() if item in g)/sum(item in g for item in ratings[user]) if any(item in g for item in ratings[user]) else None,sum(item in g for item in ratings[user])) for g in groups]
    check('item-group collaborative profiles preserve missing and evidence counts',profile('U4')==profile('U5')==[(5,1),(1,1)] and profile('U6')==[(5,1),(None,0)])

    sales=[('North','A',10),('North','B',20),('South','A',5)]
    cubed=cube(sales,2)
    check('cube original totals, grouping masks and real-NULL distinction',
          cubed[(0,(None,None))]==35 and cubed[(1,('North',None))]==30 and cubed[(2,(None,'A'))]==15 and
          cubed[(2,(None,'B'))]==20 and len(cubed)==8 and
          (3,('North',None)) != (1,('North',None)))
    dims=['region','category','day']
    rollup_product={frozenset(a)|frozenset(b) for a in [('region',),()] for b in [('category','day'),('category',),()]}
    check('dense cube cells differ from grouping count and rollup products',
          2*3*2==12 and 3*4*3==36 and len(subsets(dims))==8 and len(rollup_product)==6 and
          set(subsets(dims))-rollup_product=={frozenset(['region','day']),frozenset(['day'])})
    cube_errors=[];cube_cases=0
    # Independent oracle recomputes each grouping directly from all input rows.
    for amounts in product([0,1,2],repeat=4):
        rows=[('N','A',amounts[0]),('N','B',amounts[1]),('S','A',amounts[2]),('S','B',amounts[3])]
        result=cube(rows,2)
        for mask in range(4):
            groups=defaultdict(list)
            for r,c,value in rows:
                groups[(r if mask&1 else None,c if mask&2 else None)].append(value)
            if any(result[(mask,key)]!=sum(values) for key,values in groups.items()):cube_errors.append(amounts)
        cube_cases+=1
    check('cube update algorithm versus independent group-by oracle',not cube_errors,{'finiteFixtures':cube_cases,'failures':len(cube_errors)})
    check('row-column payload and weighted average examples',1_000_000*20*8==160_000_000 and
          1_000_000*2*8==16_000_000 and (20+100)/(2+1)==40 and (10+100)/2==55)

    r=Counter({('K','r1'):1});s=Counter({('K','s1'):1});dr=Counter({('K','r2'):1});ds=Counter({('K','s2'):1})
    new=join_counts(signed_add(r,dr),signed_add(s,ds))
    differential=signed_add(join_counts(dr,s),join_counts(r,ds),join_counts(dr,ds))
    check('simultaneous join delta retains new-new term exactly once',signed_add(join_counts(r,s),differential)==dict(new) and sum(differential.values())==3)
    join_failures=0;join_cases=0
    # All valid insert/delete signed changes for two old multiplicities0..2.
    for mr,ms in product(range(3),repeat=2):
        for nr,ns in product(range(3),repeat=2):
            delta_r=nr-mr;delta_s=ns-ms
            if nr*ns-mr*ms != delta_r*ms+mr*delta_s+delta_r*delta_s:join_failures+=1
            join_cases+=1
    check('signed bag join polynomial across inserts/deletes',join_failures==0,{'finiteCases':join_cases})
    set_failures=0;set_cases=0
    operations=[lambda r,s:r and s,lambda r,s:r or s,lambda r,s:r and not s]
    for old_r,old_s,new_r,new_s in product([0,1],repeat=4):
        for operation in operations:
            old=int(operation(old_r,old_s));new=int(operation(new_r,new_s));delta=new-old
            if old+delta!=new or new not in [0,1]:set_failures+=1
            set_cases+=1
    rr=set('ab');ss=set('bc');ss.add('a');first=(rr&ss,rr|ss,rr-ss);rr.remove('b');second=(rr&ss,rr|ss,rr-ss)
    check('set membership deltas and original answered trace',set_failures==0 and first==(set('ab'),set('abc'),set()) and second==(set('a'),set('abc'),set()),{'finiteTransitions':set_cases})
    values=[10,None];states=[]
    values.append(20);states.append(aggregate(values));values.remove(10);states.append(aggregate(values));values.remove(20);states.append(aggregate(values))
    check('aggregate null/state and group disappearance trace',states==[(3,2,30,15),(2,1,20,20),(1,0,0,None)] and aggregate([]) is None and
          min([10,20])==10 and min([7,23])==7)
    witness_count=2;visible=[]
    for delta in [-1,-1]:witness_count+=delta;visible.append(witness_count>0)
    check('projection derivation count keeps remaining witness',visible==[True,False])
    joined=[('r2','s1',4+3),('r1','s2',2+5),('r2','s2',4+5)]
    check('expression delta selection includes all three changed witness pairs',all(value>6 for _,_,value in joined) and len(joined)==3 and not 2+3>6)
    # A left join has a null row exactly when there are no matches.
    view=lambda matches:{('r',x) for x in matches} if matches else {('r',None)}
    check('outer join first/last match removes/restores null extension',view(set())=={('r',None)} and
          view({'s1'})-view(set())=={('r','s1')} and view(set())-view({'s1'})=={('r',None)} and
          ('r',None) not in view({'s1','s2'}))

    report={'date':'2026-11-05','scopeLessonIds':ledger['scopeLessonIds'],'ledger':'research/semantic-analytics.json',
            'lessonSha256':ledger['lessonSha256'],'allPassed':all(c['passed'] for c in checks),
            'checks':checks,'activityCounts':activity_counts,'sqlRuntimeUsed':False,'heavyTrainingRuntimeUsed':False,
            'semanticClaimLimit':'Finite model and arithmetic checks confirm stated fixtures/answers and exact hashes confirm freshness. Manual full own-body reading and individual content judgments, not this program, support source coverage. No learned-model quality, benchmark or transaction runtime is certified.'}
    (BASE/'qa/analytics-full-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'allPassed':report['allPassed'],'checks':len(checks),'aprioriOracleCases':apriori_cases,'cubeOracleFixtures':cube_cases,'failed':[c['name'] for c in checks if not c['passed']]},ensure_ascii=False))
    if not report['allPassed']:raise SystemExit(1)

if __name__=='__main__':main()
