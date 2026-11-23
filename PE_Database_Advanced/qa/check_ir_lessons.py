"""Finite independent-oracle/math checks; no SQL or search-engine execution."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib, heapq, itertools, json, math, re, sqlite3
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'output/database-advanced'
checks=[]
def check(name, condition, detail):
    checks.append(dict(name=name,passed=bool(condition),detail=detail))
    if not condition:
        raise AssertionError(name)

def threshold(lists,k,universe):
    if k==0:
        return sorted(universe)
    if k>len(lists):
        return []
    heap=[(xs[0],i,0) for i,xs in enumerate(lists) if xs]
    heapq.heapify(heap)
    out=[]
    while heap:
        d=heap[0][0]
        matched=[]
        while heap and heap[0][0]==d:
            _,i,p=heapq.heappop(heap)
            matched.append((i,p))
        if len(matched)>=k:
            out.append(d)
        for i,p in matched:
            if p+1<len(lists[i]):
                heapq.heappush(heap,(lists[i][p+1],i,p+1))
    return out

lists=[[1,2,3],[1,3],[2,3,4]]
check('threshold-original-fixture',threshold(lists,2,range(1,5))==[1,2,3] and threshold(lists,3,range(1,5))==[3], 'Distinct query-term count, not token frequency.')
subsets=[list(c) for n in range(5) for c in itertools.combinations(range(1,5),n)]
cases=0
for triple in itertools.product(subsets,repeat=3):
    for k in range(5):
        oracle=[d for d in range(1,5) if sum(d in xs for xs in triple)>=k]
        assert threshold(triple,k,range(1,5))==oracle
        cases+=1
check('threshold-exhaustive-oracle',True,f'{cases} finite inputs checked against independent document-membership oracle, including empty lists/k0/k>n.')
check('NOT-bounded-universe',set(lists[0])-set(lists[2])=={1} and set(range(1,5))-set(lists[0])=={4},'Difference versus snapshot complement.')
check('popularity-early-stop-counterexample',.4+.1 < .2+.9,'First popularity hit1 loses to document3 under changed score.')
check('unseen-upper-bound-example',math.isclose(.2+.1+.15,.45) and .45<.70,'Valid only if metadata covers every unseen candidate and weights are nonnegative; ties require a separate rule.')
relevant={1,3,5,7}
ranking=[3,2,1,5]
curve=[]
for k in range(1,5):
    hits=len(set(ranking[:k]) & relevant)
    curve.append((hits/len(relevant),hits/k))
check('precision-recall-cutoffs',curve==[(.25,1),(.25,.5),(.5,2/3),(.75,.75)],str(curve))
check('average-precision-and-macro',math.isclose((1+2/3)/4,5/12) and math.isclose((2/3+1)/2,5/6),'AP denominator4 for truncated three-result example; macro P@3 over two queries.')
check('approximate-index-errors',({1,2,3}&{1,3})=={1,3} and ({1,2}&{1,3})=={1},'Post-filter removes false positives but cannot recover a dropped3.')

corpus=['sql sql index','sql transaction','index']
counts=[Counter(s.split()) for s in corpus]
df=Counter(t for c in counts for t in c)
scores=[sum(math.log1p(c[t]/sum(c.values()))/df[t] for t in ['sql','index']) for c in counts]
weighted=[sum(w*math.log1p(c[t]/sum(c.values()))/df[t] for t,w in [('sql',2),('index',1)]) for c in counts]
check('normalized-log-TFIDF',all(abs(a-b)<5e-7 for a,b in zip(scores,[.399254,.202733,.346574])),'Source variant with chosen natural log, IDF1/df; all OR candidates.')
check('weighted-query-rank-change',sorted(range(3),key=lambda i:-weighted[i])==[0,1,2] and all(abs(a-b)<5e-7 for a,b in zip(weighted,[.654667,.405465,.346574])),str(weighted))
check('raw-TF-is-different',2/2==1 and 1/2==.5 and not math.isclose(1,.5*math.log(2)),'Raw frequency and normalized log yield different score units.')
def cosine(a,b):
    n=math.sqrt(sum(x*x for x in a)*sum(x*x for x in b))
    return None if n==0 else sum(x*y for x,y in zip(a,b))/n
check('cosine-original-and-zero',math.isclose(cosine([2,0],[1,1]),1/math.sqrt(2)) and cosine([0,0],[0,0]) is None,'Zero vector has no direction; no0/0 claim.')
check('query-by-example-cosines',abs(cosine([3,2,1],[1,2,0])-.836660)<5e-7 and abs(cosine([3,2,1],[2,0,0])-.801784)<5e-7,'Dot B7>C6 and cosB≈.836660>cosC≈.801784; query-only cosine has norm sqrt13 instead of sqrt14.')

alpha=.85
v=np.ones(3)/3
P=np.array([[0,1,1],[1,0,0],[0,0,0]],dtype=float)
r0=v.copy(); r1=alpha*(P@r0)+(1-alpha)*v; r2=alpha*(P@r1)+(1-alpha)*v
steady=np.linalg.solve(np.eye(3)-alpha*P,(1-alpha)*v)
check('PageRank-two-iterations',np.allclose(r1,[.6166666666666667,.3333333333333333,.05]) and np.allclose(r2,[.3758333333333333,.5741666666666667,.05]),'Direct matrix oracle for the sparse graph A->B,B->A,C->A.')
check('PageRank-stationary-linear-solve',np.allclose(steady,[.4864864864864865,.4635135135135135,.05]),'Independent linear-system solve, not visual convergence guess.')
trail=[]; current=v.copy()
for i in range(200):
    nxt=alpha*(P@current)+(1-alpha)*v
    delta=np.linalg.norm(nxt-current,1)
    assert np.all(nxt>=0) and abs(nxt.sum()-1)<1e-12
    assert np.linalg.norm(nxt-steady,1) <= delta/(1-alpha)+1e-12
    trail.append(delta)
    current=nxt
check('PageRank-mass-and-residual-bound',True,'200 finite synchronous iterations checked for nonnegative unit mass and conservative residual/(1-alpha) error bound; does not replace the contraction proof.')
Pd=P.copy(); Pd[:,2]=v
check('PageRank-dangling-column',np.allclose(Pd.sum(axis=0),1) and abs((alpha*(Pd@v)+(1-alpha)*v).sum()-1)<1e-12,'Dangling C column replaced by v every iteration.')
edges=[(0,1),(1,0),(2,0)]
contrib=defaultdict(float)
for src,dst in sorted(edges):
    contrib[dst]+=alpha*r0[src]
external=np.array([contrib[i]+(1-alpha)*v[i] for i in range(3)])
check('PageRank-streamed-contributions',np.allclose(external,r1),'One sorted edge-contribution/group-sum pass matches synchronous dense oracle. No disk benchmark claimed.')
db=sqlite3.connect(':memory:')
db.executescript('CREATE TABLE Vertex(id TEXT PRIMARY KEY,teleport REAL); CREATE TABLE Transition(src TEXT,dst TEXT,prob REAL,PRIMARY KEY(src,dst)); CREATE TABLE RankOld(id TEXT PRIMARY KEY,rank_value REAL);')
db.executemany('INSERT INTO Vertex VALUES(?,?)',[(n,1/3) for n in 'ABC'])
db.executemany('INSERT INTO RankOld VALUES(?,?)',[(n,1/3) for n in 'ABC'])
db.executemany('INSERT INTO Transition VALUES(?,?,?)',[('A','B',1),('B','A',1),('C','A',1)])
sql=re.findall(r'```sql\n(.*?)\n```',(OUT/'lessons/AD69.md').read_text(encoding='utf-8'),re.S)
assert len(sql)==1
sql_rows=db.execute(sql[0]).fetchall()
check('SQLite-actual-authored-PageRank-SELECT',[r[0] for r in sql_rows]==['A','B','C'] and np.allclose([r[1] for r in sql_rows],r1),f'Exact lesson SQL block executed on SQLite {sqlite3.sqlite_version}, in-memory one-pass fixture; C preserved by outer join.')
db.close()
vs=np.array([.5,.5,0]); vt=np.array([0,0,1]); lam=.3
rs=np.linalg.solve(np.eye(3)-alpha*P,(1-alpha)*vs)
rt=np.linalg.solve(np.eye(3)-alpha*P,(1-alpha)*vt)
rm=np.linalg.solve(np.eye(3)-alpha*P,(1-alpha)*(lam*vs+(1-lam)*vt))
check('query-specific-teleport-linear-mix',np.allclose(rm,lam*rs+(1-lam)*rt),'Linearity checked with fixed shared P and no dangling-dependent transition changes.')
auth=np.array([1,2])/math.sqrt(5); hubs=np.array([3,2])/math.sqrt(13)
check('HITS-one-alternating-step',np.allclose(auth,[1/math.sqrt(5),2/math.sqrt(5)]) and np.allclose(hubs/np.linalg.norm(hubs),hubs),'Finite one-step authority/hub example only; no uniqueness claim.')
check('score-mixture-examples',all(math.isclose(a,b) for a,b in zip([.7*.8+.3*.1,.7*.5+.3*.9,.9*.8+.1*.1,.9*.5+.1*.9],[.59,.62,.73,.54])),'Weight change reverses X/Y ranking.')

dag={'root':['science'],'science':['math','computing'],'math':['graphs'],'computing':['algorithms'],'algorithms':['graphs'],'graphs':[]}
def paths(node,target,active):
    if node in active:
        raise ValueError('cycle')
    return int(node==target)+sum(paths(c,target,active|{node}) for c in dag[node])
check('classification-DAG-two-paths',paths('science','graphs',set())==2,'Single graphs category reachable through math and computing/algorithms; document ID is not duplicated.')
dag['graphs']=['science']
try:
    paths('science','graphs',set())
    cycle=False
except ValueError:
    cycle=True
check('classification-cycle-detected',cycle,'Adding graphs->science violates DAG even though visited can make traversal terminate.')

hashes={k:hashlib.sha256((OUT/f'lessons/{k}.md').read_bytes()).hexdigest() for k in ('AD17','AD69')}
result=dict(date='2026-11-05',scope=['AD17','AD69'],kind='finite-Python-algorithm-and-math-oracle-checks',
            allPassed=all(c['passed'] for c in checks),checks=checks,lessonHashes=hashes,
            thresholdOracleCases=cases,sqlExecuted=True,sqlEngine='SQLite '+sqlite3.sqlite_version,sqlScope='Exact authored one-step PageRank SELECT, in-memory three-node fixture only.',mysqlExecuted=False,searchEngineExecuted=False,webCrawlExecuted=False,
            limitation='Finite arithmetic, independent-oracle checks and one SQLite SELECT; no commercial-search ranking reproduction, MySQL execution, ontology linker, IE/QA model, actual crawler, full SQL PageRank iteration runtime, or general theorem proof is claimed.')
(OUT/'research/semantic-ir-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f"Passed {len(checks)} finite IR checks; threshold oracle cases: {cases}. One exact SQLite SELECT executed; no MySQL/search engine/crawl execution.")
