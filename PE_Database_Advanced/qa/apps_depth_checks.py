"""Finite reference checks for the bounded applications depth review.

This does not run SQL, XML, RDF or a cluster, and is not a proof of algorithms.
"""
from pathlib import Path
from collections import Counter, deque
from itertools import combinations
from math import log, sqrt, isclose, inf
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
IDS = ['AD01'] + [f'AD{i:02}' for i in range(10, 23)] + [f'AD{i:02}' for i in range(68, 74)]
checks = []

def check(name, actual, expected):
    ok = actual == expected
    if isinstance(expected, float):
        ok = isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-6)
    checks.append(dict(name=name, actual=actual, expected=expected, passed=ok))
    assert ok, (name, actual, expected)

def bfs(edges, start):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
    q = deque([start]); distances = {start: 0}
    while q:
        a = q.popleft()
        for b in adj.get(a, []):
            if b not in distances:
                distances[b] = distances[a] + 1
                q.append(b)
    return distances

e = [('A','B'),('A','C'),('B','D'),('C','D'),('D','B'),('D','E')]
check('AD22 BFS independent queue reference', bfs(e, 'A'), dict(A=0,B=1,C=1,D=2,E=3))
check('AD22 BFS self-loop unchanged', bfs(e + [('E','E')], 'A'), dict(A=0,B=1,C=1,D=2,E=3))
e2 = [('S','T'),('S','U'),('T','V'),('U','V'),('V','T'),('V','W')]
check('AD22 transfer graph', bfs(e2, 'S'), dict(S=0,T=1,U=1,V=2,W=3))

# Enumerate all walks up to k edges independently of the relaxation implementation.
weighted = [('A','B',10),('A','C',1),('C','B',1)]
walks = [('A',0)]
best = {'A':0,'B':inf,'C':inf}
states = []
for k in (1,2):
    walks = [(b,c+w) for a,c in walks for u,b,w in weighted if a == u]
    for b,c in walks:
        best[b] = min(best[b], c)
    states.append(dict(best))
check('AD22 synchronous round 1', states[0], dict(A=0,B=10,C=1))
check('AD22 synchronous round 2', states[1], dict(A=0,B=2,C=1))

def area(box):
    x0,y0,x1,y1 = box
    return (x1-x0)*(y1-y0)
def mbr(a,b):
    return min(a[0],b[0]),min(a[1],b[1]),max(a[2],b[2]),max(a[3],b[3])
boxes = dict(A=(0,0,1,1), B=(9,9,10,10), C=(1,0,2,1), D=(8,9,9,10))
waste = {(a,b):area(mbr(boxes[a],boxes[b]))-area(boxes[a])-area(boxes[b]) for a,b in combinations(boxes,2)}
check('AD15 quadratic split seed pair', list(max(waste,key=waste.get)), ['A','B'])
check('AD15 seed wasted area', waste['A','B'], 98)
check('AD15 C enlargement', [area(mbr(boxes['C'],boxes[x]))-area(boxes[x]) for x in ['A','B']], [1,89])
check('AD15 final page areas', [area(mbr(boxes['A'],boxes['C'])),area(mbr(boxes['B'],boxes['D']))], [2,2])

old_r = ['r1','r2']; old_s = ['s1']; dr = ['r3']; ds = ['s2','s3']
old = {(r,s) for r in old_r for s in old_s}
new = {(r,s) for r in old_r+dr for s in old_s+ds}
check('AD18 simultaneous join insert delta', len(new-old), 7)
check('AD18 projection witness survives first deletion', {a for a,b in [('A',3),('B',4)]}, {'A','B'})
check('AD18 outer first match deletes null row', [(r,s) for r in ['r1'] for s in ['s1']], [('r1','s1')])

corpus = {'d1':'sql sql index','d2':'sql transaction','d3':'index'}
tokens = {d:t.split() for d,t in corpus.items()}
df = Counter(t for ts in tokens.values() for t in set(ts))
scores = {d:sum(log(1+ts.count(t)/len(ts))/df[t] for t in ['sql','index']) for d,ts in tokens.items()}
check('AD69 TF-IDF ranking', sorted(scores,key=lambda d:-scores[d]), ['d1','d3','d2'])
check('AD69 d1 score', scores['d1'], 0.399253848)
check('AD69 cosine', 2/(sqrt(2)*2), 1/sqrt(2))
r = [1/3]*3
for _ in range(2):
    r = [.05+.85*(r[1]+r[2]), .05+.85*r[0], .05]
check('AD69 PageRank mass', sum(r), 1.)
check('AD69 PageRank second round A', r[0], .3758333333333333)
check('AD69 HITS hub ratio', (3/sqrt(5))/(2/sqrt(5)), 1.5)
check('AD17 AP denominator four', (1+2/3)/4, 5/12)

events = [(2,5),(7,3),(4,2),(12,1),(14,4)]
totals = [sum(v for t,v in events if s <= t < s+10) for s in [0,5,10]]
check('AD21 hopping totals', totals, [10,8,5])
check('AD21 sliding at12 with open left endpoint', sum(v for t,v in events if 2 < t <= 12), 6)
check('AD21 watermark trace', [max(t for t,v in events[:i])-3 for i in range(1,6)], [-1,4,4,9,11])
check('AD21 CEP two fails inside60 seconds at success40', sum(40-t <= 60 for t in [1,20]) >= 2, True)
check('AD21 CEP expired prefix at success80', sum(80-t <= 60 for t in [1,20]) >= 2, False)

check('AD19 F1 from counts', 2*9/(2*9+3+1), 9/11)
check('AD70 split1.5 Gini gain', .5-(3/4)*(1-(1/3)**2-(2/3)**2), 1/6)
baskets = [set('AB'),set('ABC'),set('AC'),set('BC')]
support = sum(set('AB') <= t for t in baskets)/len(baskets)
check('AD71 association lift', (support/(3/4))/(3/4), 8/9)
check('AD71 kmeans SSE', sum((x-c)**2 for xs,c in [([0,2],1),([8,10],9)] for x in xs), 4)
check('AD71 single-link final distance', min(abs(x-y) for x in [0,2] for y in [8,10]), 6)
check('AD71 complete-link final distance', max(abs(x-y) for x in [0,2] for y in [8,10]), 10)
check('AD72 missing cube grouping', [10+5,20], [15,20])
check('AD16 DFS descendant test', [2<p and q<7 for p,q in [(3,4),(5,6),(8,11)]], [True,True,False])

required = ['Luyện tập','Gợi ý','Đáp án và lập luận','Biến thể và cách kiểm','Học trên web','Nguồn và đối chiếu']
lessons = []
for id in IDS:
    p = ROOT/'lessons'/f'{id}.md'; b = p.read_bytes(); t = b.decode('utf8').replace('\r\n','\n')
    sections = {name: f'## {name}' in t for name in required}
    assert all(sections.values()) and t.count('```')%2 == 0
    q = t.split('## Luyện tập\n',1)[1].split('\n## ',1)[0]
    a = t.split('## Đáp án và lập luận\n',1)[1].split('\n## ',1)[0]
    qs = re.findall(r'^(\d+)\. ',q,re.M); ans = re.findall(r'^(\d+)\. ',a,re.M)
    assert qs == ans and len(qs) >= 4, (id,qs,ans)
    lessons.append(dict(id=id,sha256=hashlib.sha256(b).hexdigest(),questionCount=len(qs),sections=sections,balancedFences=True))

report = dict(date='2026-11-05',scope=IDS,kind='bounded-source-and-model-review',
              finiteChecks=checks,passed=sum(c['passed'] for c in checks),total=len(checks),lessons=lessons,
              limits=['No native SQL/XML/RDF/graph/cluster execution in this pass.',
                      'Finite calculations are not general correctness proofs.',
                      'Not a semantic certification of all 945 source inventory entries.',
                      'HTML/PDF rendering is owned by the root packaging task.'])
# Sets only appear in model actual/expected values; normalize deterministically.
def encode(x):
    if isinstance(x,set): return sorted(x)
    raise TypeError(type(x).__name__)
(ROOT/'qa/apps-depth-model-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,default=encode),encoding='utf8')
print(json.dumps(dict(passed=report['passed'],total=report['total'],lessons=len(lessons))))
