"""Independent finite models for the authored AD15/20/21/22/35/36/37/61/73 examples.

Run with the bundled Python. These checks do not run MySQL, Hadoop, Spark,
MongoDB, Neo4j or a distributed service, and do not establish general proofs.
"""
from pathlib import Path
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
import hashlib
import json
import math
import random
import sqlite3

OUT = Path(__file__).resolve().parent
COURSE = OUT.parent
RNG = random.Random(20261105)
results = []


def check(name, actual, expected, comparisons=1, scope='finite Python model'):
    assert actual == expected, (name, actual, expected)
    results.append(dict(name=name, status='pass', comparisons=comparisons,
                        scope=scope))


def closure_naive(edges):
    r = set()
    while True:
        nxt = r | set(edges) | {(a, d) for a, b in r for c, d in edges if b == c}
        if nxt == r:
            return r
        r = nxt


def closure_delta(edges):
    r = set(edges)
    delta = r.copy()
    while delta:
        new = {(a, d) for a, b in delta for c, d in edges if b == c} - r
        r |= new
        delta = new
    return r


def warshall(edges, n):
    a = [[(i, j) in edges for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                a[i][j] = a[i][j] or (a[i][k] and a[k][j])
    return {(i, j) for i in range(n) for j in range(n) if a[i][j]}


def bfs(edges, start):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
    d, queue = {start: 0}, deque([start])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                queue.append(v)
    return d


edges3 = list(product(range(3), repeat=2))
for mask in range(1 << len(edges3)):
    e = {p for i, p in enumerate(edges3) if mask & (1 << i)}
    oracle = warshall(e, 3)
    assert closure_naive(e) == oracle == closure_delta(e)
    for start in range(3):
        # Floyd-style independent all-pairs distances include the empty path.
        d = [[0 if i == j else (1 if (i, j) in e else 99)
              for j in range(3)] for i in range(3)]
        for k, i, j in product(range(3), repeat=3):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        assert bfs(e, start) == {v: d[start][v] for v in range(3) if d[start][v] < 99}
check('Datalog naive and semi-naive versus Warshall on every 3-node directed graph', True, True, 512)
check('BFS versus all-pairs distances, all starts including cycles and disconnected nodes', True, True, 1536)
check('Datalog authored cycle closure', closure_naive({('a','b'),('b','c'),('c','a'),('c','d')}),
      {(a,b) for a in 'abc' for b in 'abcd'})
check('Datalog exercise Delta closure', closure_delta({(1,2),(2,3),(3,2)}),
      {(1,2),(1,3),(2,2),(2,3),(3,2),(3,3)})
check('Nonlinear rule needs new-old term', {(x,z) for x,y in {('a','b')} for u,z in {('b','c')} if y == u}, {('a','c')})
check('Unsafe arithmetic recursion keeps extending beyond finite input domain', len({0} | set(range(1,21))), 21)
check('Ground rule and nonrecursive arithmetic examples',
      ([(i,b) for i,branch,b in [('a1','west',900),('a2','west',650),('a3','east',950)] if branch == 'west' and b > 800],
       {b+1 for b in [1,4]}), ([('a1',900)], {2,5}))
check('Difference counterexample to monotonicity', ({'a','b'}-{'a'}, {'a','b'}-{'a','b'}), ({'b'}, set()))


def bbox(boxes):
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


def area(b):
    return (b[2]-b[0])*(b[3]-b[1])


def intersect(a,b):
    return a[0] <= b[2] and b[0] <= a[2] and a[1] <= b[3] and b[1] <= a[3]


def split_quad(boxes, minimum=2):
    seeds = max(combinations(range(len(boxes)),2), key=lambda ij:
                area(bbox([boxes[ij[0]],boxes[ij[1]]]))-area(boxes[ij[0]])-area(boxes[ij[1]]))
    groups = [[seeds[0]], [seeds[1]]]
    remaining = set(range(len(boxes))) - set(seeds)
    while remaining:
        for gi in range(2):
            if len(groups[gi])+len(remaining) == minimum:
                groups[gi].extend(sorted(remaining)); remaining.clear(); break
        if not remaining:
            break
        bounds = [bbox([boxes[i] for i in g]) for g in groups]
        def increases(i):
            return [area(bbox([b,boxes[i]]))-area(b) for b in bounds]
        i = max(sorted(remaining), key=lambda i: abs(increases(i)[0]-increases(i)[1]))
        inc = increases(i)
        gi = 0 if inc[0] < inc[1] else 1
        groups[gi].append(i); remaining.remove(i)
    return groups


boxes = [(0,0,1,1),(9,9,10,10),(1,0,2,1),(8,9,9,10)]
check('R-tree quadratic split trace', {frozenset(g) for g in split_quad(boxes)},
      {frozenset([0,2]),frozenset([1,3])})
for trial in range(200):
    boxes = [(x,y,x+RNG.randint(1,4),y+RNG.randint(1,4))
             for x,y in [(RNG.randint(0,20),RNG.randint(0,20)) for _ in range(4)]]
    groups = split_quad(boxes)
    assert sorted(i for g in groups for i in g) == list(range(4))
    assert all(len(g) >= 2 for g in groups)
    query = tuple(RNG.randint(0,20) for _ in range(4))
    query = (min(query[0],query[2]),min(query[1],query[3]),max(query[0],query[2]),max(query[1],query[3]))
    candidate_hits = {i for g in groups if intersect(bbox([boxes[j] for j in g]),query)
                      for i in g if intersect(boxes[i],query)}
    assert candidate_hits == {i for i,b in enumerate(boxes) if intersect(b,query)}
check('R-tree split invariants and range-search completeness versus full scan', True, True, 200)
check('Spatial triangle filter/exact/boundary cases',
      [(0 <= x <= 10 and 0 <= y <= 10, x > 0 and y > 0 and x+y < 10, x >= 0 and y >= 0 and x+y <= 10)
       for x,y in [(9,9),(5,5)]], [(True,False,False),(True,False,True)])
check('Nearest-distance tie contract', [i for i,p in enumerate([(3,4),(-3,4),(9,0)]) if math.hypot(*p) == 5], [0,1])
check('TIN and triangulated rectangle area', (1+2*0.5, 4+4), (2.0,8))
check('Region quadtree lossless leaf condition', (len(set([1,1,1,0]))==1,len(set([1,1,1,1]))==1), (False,True))


def mr_count(parts, combine):
    emitted = []
    for part in parts:
        local = [(w,1) for line in part for w in line.lower().split()]
        if combine:
            local = list(Counter(w for w,v in local).items())
        emitted.extend(local)
    groups = defaultdict(list)
    for w,v in emitted:
        groups[w].append(v)
    return {w:sum(vs) for w,vs in groups.items()}


for trial in range(200):
    docs = [' '.join(RNG.choice(['db','sql','log']) for _ in range(RNG.randrange(8))) for _ in range(12)]
    parts = [[] for _ in range(4)]
    for line in docs:
        parts[RNG.randrange(4)].append(line)
    oracle = dict(Counter(w for line in docs for w in line.split()))
    assert mr_count(parts,False) == oracle == mr_count(parts,True)
check('MapReduce combiner and partition invariance versus occurrence Counter', True, True, 200)
check('Weighted-average sufficient state and wrong scalar combine', ((0+9)/2, (0+9)/(2+1)), (4.5,3))
check('Authored word-count fixture', mr_count([['sql index sql','index log'],['sql log']],True), {'sql':3,'index':2,'log':2})
check('Authored map versus flatMap fixture', ([s.split() for s in ['db db','sql']], [w for s in ['db db','sql'] for w in s.split()]),
      ([['db','db'],['sql']],['db','db','sql']))
logs = [('2026-01-03','/slides/a',100),('2026-01-05','/notes/b',60),('2026-02-01','/slides/a',40),('2026-01-03','/slides/a',20)]
chosen = [r for r in logs if '2026-01-01' <= r[0] < '2026-02-01' and r[1].startswith('/slides/')]
check('Log interval right boundary and aggregate grain', (sum(r[2] for r in chosen),len(chosen)), (120,2))


# Enumerate every ordered labelled tree independently from the DP subset recurrence.
def trees(labels):
    if len(labels) == 1:
        yield labels[0]
        return
    for size in range(1,len(labels)):
        for left in combinations(labels,size):
            right = tuple(x for x in labels if x not in left)
            for a in trees(tuple(left)):
                for b in trees(right):
                    yield (a,b)


def leafset(t):
    return frozenset([t]) if isinstance(t,int) else leafset(t[0])|leafset(t[1])


alltrees = list(trees((0,1,2,3)))
check('Catalan-labelled tree counts', (len(list(trees((0,1,2)))),len(alltrees),math.factorial(4)), (12,120,24))
for trial in range(12):
    scans = {i:(RNG.randrange(1,8),RNG.randrange(5,15)) for i in range(4)}
    sizes = [frozenset(c) for k in range(1,5) for c in combinations(range(4),k)]
    sorts = {s:RNG.randrange(1,20) for s in sizes}
    extra = {(a,b,m):RNG.randrange(1,30) for a in sizes for b in sizes if a.isdisjoint(b) for m in ['hash','merge']}
    def physical_costs(t):
        if isinstance(t,int):
            s=frozenset([t]); u,o=scans[t]
            return [(u,'u'),(o,'o'),(u+sorts[s],'o')]
        a,b=t; sa,sb=leafset(a),leafset(b); s=sa|sb; out=[]
        for (ca,pa),(cb,pb) in product(physical_costs(a),physical_costs(b)):
            h=ca+cb+extra[sa,sb,'hash']
            out.extend([(h,'u'),(h+sorts[s],'o')])
            merge=ca+cb+extra[sa,sb,'merge']+(0 if pa=='o' else sorts[sa])+(0 if pb=='o' else sorts[sb])
            out.append((merge,'o'))
        return out
    memo={}
    for s in sizes:
        if len(s)==1:
            i=next(iter(s));u,o=scans[i];memo[s]={'u':u,'o':min(o,u+sorts[s])};continue
        best={'u':math.inf,'o':math.inf}
        for size in range(1,len(s)):
            for aa in combinations(sorted(s),size):
                a=frozenset(aa); b=s-a
                for (pa,ca),(pb,cb) in product(memo[a].items(),memo[b].items()):
                    h=ca+cb+extra[a,b,'hash']
                    best['u']=min(best['u'],h)
                    m=ca+cb+extra[a,b,'merge']+(0 if pa=='o' else sorts[a])+(0 if pb=='o' else sorts[b])
                    best['o']=min(best['o'],m,h+sorts[s])
        memo[s]=best
    candidates=[v for t in alltrees for v in physical_costs(t)]
    assert memo[frozenset(range(4))]['o'] == min(c for c,p in candidates if p=='o')
check('DP interesting-order state versus exhaustive physical trees under 12 seeded cost models', True, True, 12)
check('Authored greedy, interesting-order and lookup conventions',
      (5+5+10+5+5, 5+(5+5+2)+50, min(20+20+5+3,25+5+3), min(18+12+4+2,26+4+2), 30 < 100000+20),
      (30,67,33,32,True))


def bagjoin(r,s):
    return Counter((a,b) for a in r for b in s if a[0] is not None and a[0]==b[0])


for trial in range(200):
    r=[(RNG.choice(['K','L',None]),i) for i in range(RNG.randrange(8))]
    s=[(RNG.choice(['K','L',None]),i+100) for i in range(RNG.randrange(8))]
    dr=RNG.sample(r,RNG.randrange(len(r)+1)); ds=RNG.sample(s,RNG.randrange(len(s)+1))
    ir=[(RNG.choice(['K','L',None]),i+200) for i in range(RNG.randrange(4))]
    ins=[(RNG.choice(['K','L',None]),i+300) for i in range(RNG.randrange(4))]
    v=bagjoin(r,s)
    v.subtract(bagjoin(dr,s));v.update(bagjoin(ir,s))
    rnew=[a for a in r if a not in dr]+ir
    v.subtract(bagjoin(rnew,ds));v.update(bagjoin(rnew,ins))
    snew=[b for b in s if b not in ds]+ins
    assert +v==bagjoin(rnew,snew)
    assert all(n>=0 for n in v.values())
check('Sequential two-input join deltas with inserts/deletes versus full bag recompute', True, True, 200)
check('Authored join cross term', (2*2,3*3,1*2+2*1+1*1), (4,9,5))
state={}; rows={}
for step in range(300):
    if rows and RNG.random()<0.45:
        i=RNG.choice(list(rows));g,x=rows.pop(i);sign=-1
    else:
        i=step;g=RNG.choice(['A','B','C']);x=RNG.choice([None,-5,0,5,10]);rows[i]=(g,x);sign=1
    rc,nc,total=state.get(g,(0,0,0));rc+=sign
    if x is not None:nc+=sign;total+=sign*x
    if rc:state[g]=(rc,nc,total)
    else:state.pop(g,None)
    oracle={}
    for gg in {v[0] for v in rows.values()}:
        vals=[v for group,v in rows.values() if group==gg]
        oracle[gg]=(len(vals),sum(v is not None for v in vals),sum(v for v in vals if v is not None))
    assert state==oracle
check('SUM/COUNT/AVG sufficient state, empty/all-NULL/zero-sum groups versus recompute', True, True, 300)
counts=Counter({'K':2}); trace=[]
for delta in [-1,1,-1,-1]:
    counts['K']+=delta; trace.append((counts['K'],{k for k,n in counts.items() if n>0}))
check('DISTINCT support-count exercise trace', trace, [(1,{'K'}),(2,{'K'}),(1,{'K'}),(0,set())])
check('Outer-join match transitions', [(n, n==0) for n in [0,1,2,1,0]], [(0,True),(1,False),(2,False),(1,False),(0,True)])
check('Top-K tie-break and WITH TIES',
      ([i+1 for i,v in sorted(enumerate([4,9,2,10,9]),key=lambda p:(-p[1],p[0]))[:2]],
       [v for v in [4,9,2,10,9] if v>=9]), ([4,2],[9,10,9]))
check('Parametric plan threshold and workload benefit', (min(10+2*20,100),min(10+2*80,100),200*20-600*4), (50,100,1600))
check('Shared-plan, restart sunk work and MV expansion arithmetic', (12+2+2,30+200,30+50,3+3), (16,230,80,6))


events=[(1,2,5),(2,7,3),(3,4,2),(4,12,1),(5,14,4)]
tumbling=defaultdict(int);hopping=defaultdict(int)
watermarks=[];maximum=-math.inf
for _,t,v in events:
    tumbling[(t//10)*10]+=v
    for start in [0,5,10]:
        if start<=t<start+10:hopping[start]+=v
    maximum=max(maximum,t);watermarks.append(maximum-3)
check('Stream authored tumbling/hopping/sliding populations',
      (dict(tumbling),dict(hopping),sum(v for _,t,v in events if 2<t<=12)), ({0:10,10:5},{0:10,5:8,10:5},6))
check('Watermarks and late revision/drop', (watermarks, tumbling[0],tumbling[0]+8), ([-1,4,4,9,11],10,18))
check('Hopping/tumbling boundary at exactly time10', (10//10*10,[s for s in [0,5,10] if s<=10<s+10]), (10,[5,10]))
topics={'raw':['parse'],'parsed':['aggregate','archive'],'summary':['dashboard']}
check('Pubsub fanout and retention distinction', (topics['parsed'],10+20>25,10+20>35), (['aggregate','archive'],True,False))
check('Temporal dimension join before and after category change', ('Book' if 12<15 else 'Gift','Book' if 20<15 else 'Gift'), ('Book','Gift'))


def bellman(edges,n,start):
    d=[math.inf]*n;d[start]=0
    for _ in range(n-1):
        nxt=d.copy()
        for a,b,w in edges:nxt[b]=min(nxt[b],d[a]+w)
        if nxt==d:return d,False
        d=nxt
    return d,any(d[a]+w<d[b] for a,b,w in edges if math.isfinite(d[a]))


def simple_path_cost(edges,n,start):
    # Independent path enumeration; only tested on acyclic weighted graphs.
    weights={(a,b):w for a,b,w in edges};d=[math.inf]*n;d[start]=0
    for size in range(1,n):
        for tail in permutations([i for i in range(n) if i!=start],size):
            p=(start,)+tail
            if all((a,b) in weights for a,b in zip(p,p[1:])):
                d[p[-1]]=min(d[p[-1]],sum(weights[a,b] for a,b in zip(p,p[1:])))
    return d


for trial in range(100):
    e=[(a,b,RNG.randrange(-5,10)) for a in range(4) for b in range(a+1,4) if RNG.random()<0.7]
    for start in range(4):
        d,negative=bellman(e,4,start)
        assert not negative and d==simple_path_cost(e,4,start)
check('Synchronous weighted relaxation versus independent simple-path enumeration on acyclic graphs', True, True, 400)
check('BFS minimum-hop counterexample', bellman([(0,1,10),(0,2,1),(2,1,1)],3,0), ([0,2,1],False))
check('Reachable negative-cycle flag and unaffected branch', bellman([(0,1,0),(1,2,-2),(2,1,1),(0,3,7)],4,0)[1], True)


con=sqlite3.connect(':memory:')
con.executescript('CREATE TABLE R(id,keep); CREATE TABLE S(rid,sid); INSERT INTO R VALUES(1,1),(2,0); INSERT INTO S VALUES(1,10),(1,11),(2,20);')
q1=con.execute('SELECT R.id,S.sid FROM R JOIN S ON R.id=S.rid WHERE R.keep=1').fetchall()
q2=con.execute('SELECT R.id,S.sid FROM (SELECT * FROM R WHERE keep=1) R JOIN S ON R.id=S.rid').fetchall()
check('Actual SQLite inner-selection pushdown with bag rows', Counter(q1),Counter(q2),scope='executed SQLite '+sqlite3.sqlite_version)
con.executescript('CREATE TABLE A(id); CREATE TABLE B(rid,amount); INSERT INTO A VALUES(1);')
left=con.execute('SELECT A.id,B.amount FROM A LEFT JOIN B ON A.id=B.rid WHERE B.amount>0').fetchall()
right=con.execute('SELECT A.id,B.amount FROM A LEFT JOIN (SELECT * FROM B WHERE amount>0) B ON A.id=B.rid').fetchall()
check('Actual SQLite invalid outer-predicate pushdown counterexample', (left,right), ([],[(1,None)]),scope='executed SQLite '+sqlite3.sqlite_version)
con.executescript('CREATE TABLE RK(k); CREATE TABLE SK(k); INSERT INTO RK VALUES(1),(1),(2),(NULL); INSERT INTO SK VALUES(1),(1),(1),(3),(NULL);')
check('Actual SQLite NULL-aware equality-join count', con.execute('SELECT COUNT(*) FROM RK JOIN SK USING(k)').fetchone()[0],6,scope='executed SQLite '+sqlite3.sqlite_version)
con.close()
check('Cardinality arithmetic and FALSE/UNKNOWN distinction', (8000//250,math.ceil(1025/32),1025-200-50,90-10-5), (32,33,775,75))
check('Same-base independent predicate union/intersection/difference estimates', (1000*(.2+.3-.2*.3),1000*.2*.3,1000*.2*(1-.3)), (440.0,60.0,140.0))


# Finite storage scenarios, not service execution or a CAP model checker.
placements={'c1':{'A','B','C'},'c2':{'B','C','D'}}
check('File copies after sequential failures',
      (all(locs-{'A'} for locs in placements.values()),all(locs-{'A','B','C'} for locs in placements.values())), (True,False))
version=5;cart=[]
old_version=version
if version==old_version:cart.append('item1');version+=1
second_success=version==old_version
check('CAS rejects stale second writer', (version,cart,second_success), (6,['item1'],False))
cells=[('u7','dept',5,'DB'),('u7','dept',7,'AI')]
check('Wide-column latest and bounded version lookup',
      (max(cells,key=lambda c:c[2])[3],max((c for c in cells if c[2]<=6),key=lambda c:c[2])[3]), ('AI','DB'))
keys=['edu.example.cs.www/a','edu.example.csx.www/b','edu.example.cs.mail/c']
check('Hierarchical row-key prefix delimiter', [k for k in keys if k.startswith('edu.example.cs.')], [keys[0],keys[2]])
check('File assembly follows metadata rather than completion order', ''.join({'b7':'first','b8':'second'}[b] for b in ['b7','b8']), 'firstsecond')

payload={'date':'2026-11-05','seed':20261105,'status':'pass','scope':__doc__.strip(),
         'counts':{'namedChecks':len(results),'finiteComparisons':sum(r['comparisons'] for r in results),
                   'actualSQLiteChecks':sum(r['scope'].startswith('executed SQLite') for r in results)},
         'checks':results,'notExecuted':['MySQL','Hadoop','Spark','MongoDB','Neo4j','distributed services'],
         'limitations':['Finite examples corroborate worked calculations; general correctness is supplied by conditional arguments in the lessons.',
                        'No frontend, browser interaction, runtime latency or live distributed failure experiment was run.'],
         'lessonSha256':{p.stem:hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in sorted((COURSE/'lessons').glob('AD*.md'))
                         if p.stem in {'AD15','AD20','AD21','AD22','AD35','AD36','AD37','AD61','AD73'}}}
(OUT/'optimizer-bigdata-checks.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(payload['counts']))
