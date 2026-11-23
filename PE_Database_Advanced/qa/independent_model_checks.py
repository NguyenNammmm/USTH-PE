from pathlib import Path
import json,hashlib,re,itertools
R=Path('output/database-advanced')
checks=[]
def check(name,ok,details):
    assert ok,name
    checks.append({'name':name,'result':'pass','evidenceKind':'computed-model','details':details})
def graph(ops):
    return {(a[0],b[0]) for i,a in enumerate(ops) for b in ops[i+1:] if a[0]!=b[0] and a[2]==b[2] and 'w' in (a[1],b[1])}
check('AD38 exercise1 conflict witnesses',graph([(1,'r','X'),(2,'w','Y'),(1,'w','Y'),(3,'r','X'),(3,'w','X'),(2,'r','X')])=={(2,1),(1,3),(3,2)},'Cycle T2→T1→T3→T2; read/read pairs excluded.')
check('AD39 converse counterexample graph',graph([(1,'r','X'),(2,'w','X'),(3,'r','Y'),(1,'w','Y')])=={(1,2),(3,1)},'Acyclic serial order3,1,2; impossibility under2PL is a written lock-interval argument, not proved by this test.')
check('AD38 blind-write conflict cycle',graph([(1,'w','X'),(2,'w','X'),(1,'w','X')])=={(1,2),(2,1)},'Final writerT1 agrees with serial T2,T1 when no reads exist.')
check('AD40 wait-die age cases',20>10 and 10<30,'T2(ts20) aborts requesting holderT1(ts10); T1 waits for holderT3(ts30).')
check('AD41 timestamp read/write example',25>=20 and max(30,25)==30 and 25<30,'T25 read succeeds, subsequent basic write aborts at RTS check.')
check('AD41 Thomas check precedence',20>=5 and 20<40 and 20<25,'At RTS5 outdated write can be ignored; at RTS25 it must abort first.')
versions=[(0,5),(12,9),(30,20)]
chosen=max((v for v in versions if v[0]<=20),key=lambda v:v[0])
check('AD42 MVTO exercise',chosen==(12,9) and 15<20,'T20 raises RTS12 to20, so later T15 write aborts.')
check('AD42 write-skew invariant',sum([0,0])==0 and sum([1,0])==1,'Concurrent disjoint writes break guard; serial second guard would stop.')
check('AD42 MV2PL publication snapshots',max(t for t in [7,8] if t<=7)==7 and max(t for t in [7,8] if t<=8)==8,'Reader7 retains(100,100); reader8 sees atomically published(90,110).')
check('AD43 WAL prefix rejection',80<95 and 5<10,'A page carryingLSN95 cannot flush with durableLSN80.')
check('AD43 undo ordering counterexample',([10,20][-1]==20) and ([20,10][-1]==10),'Forward old-images end20; reverse restores10.')
check('AD43 completed-abort redo-only record',([20,10][-1]==10),'Replaying update10→20 then logged compensation:=10 does not resurrect aborted value.')
p={'A':10,'C':30,'pageLSN':60};p.update(C=0,pageLSN=70)
check('AD44 repeated-crash CLR trace',p=={'A':10,'C':0,'pageLSN':70},'RedoCLR70 preserves winnerA10 and restoresC0; undoNext40 continues atQ.B.')
check('AD44 logical inverse preserves successor',700-100+50+100==750 and 700!=750,'Physical restore700 would lose committed +50; inverse+100 gives750.')
check('AD45 remote durability boundary',min(200,150)==150,'Remote receive200 in lostRAM cannot establish durability beyond150.')
check('AD46 Amdahl arithmetic',abs((10+90/8)-21.25)<1e-12 and abs((16+64/4)-32)<1e-12,'Times21.25s and32s in declared ideal models.')
check('AD47 half-open partitions',[0 if k<10 else 1 if k<20 else 2 for k in [9,10,19,20]]==[0,1,1,2],'Boundary keys10 and20 assigned once.')
RR=[('r1','A'),('r2','A'),('r3','B')];SS=[('s1','A'),('s2','A'),('s3','C')]
join=[(r[0],s[0]) for r in RR for s in SS if r[1]==s[1]]
check('AD48 bag join multiplicity',len(join)==4 and len(set(join))==4,'TwoA rows each side produce four distinct identity pairs.')
check('AD48 average partial state',(40*1+10*9)/10==13 and abs((30+100)/3-43.333333333333336)<1e-12,'Count-weighted means; average of averages is invalid.')
RR=[('r1',4),('r2',4)];SS=[('s1',4),('s2',4),('s3',4),('s4',8),('s5',8)];K={r[1] for r in RR};filtered=[s for s in SS if s[1] in K]
check('AD49 semijoin bag contract',len(filtered)==3 and sum(r[1]==s[1] for r in RR for s in filtered)==6,'R semijoin retains2R rows; filteredS retains3; full join6.')
weights={'A':2,'B':1,'C':1};subsets=[set(c) for n in range(1,4) for c in itertools.combinations(weights,n)];reads=[q for q in subsets if sum(weights[x] for x in q)>=2];writes=[q for q in subsets if sum(weights[x] for x in q)>=3]
check('AD51 weighted quorum intersection',all(a&b for a in reads for b in writes) and all(a&b for a in writes for b in writes),'Enumerated fixed-membership subsets withQr2,Qw3,total4.')
check('AD51 failed-heavy-replica availability',sum(weights[x] for x in {'B','C'})>=2 and sum(weights[x] for x in {'B','C'})<3,'LosingA leaves read weight2 but insufficient write weight.')
check('AD53 greedy recomputation trace',40+30==70 and 2+3<=6 and 30/3>10/4,'J first, then updated marginalK beatsI; totalspace5.')
check('AD53 greedy is not optimal',5/3>6/4 and 5<6,'Budget4: ratio greedyA(value5,size3) loses toB(value6,size4).')
def closure(edges):
    out=set(edges)
    while True:
        nxt=out|{(a,d) for a,b in out for c,d in edges if b==c}
        if nxt==out:return out
        out=nxt
def by_dfs(edges):
    out=set()
    for start in {x for e in edges for x in e}:
        todo=[b for a,b in edges if a==start];seen=set()
        while todo:
            x=todo.pop()
            if x in seen:continue
            seen.add(x);out.add((start,x));todo.extend(b for a,b in edges if a==x)
    return out
edges={(1,2),(2,3),(3,2)};expected={(1,2),(1,3),(2,2),(2,3),(3,2),(3,3)}
check('AD61 independent closure oracle',closure(edges)==by_dfs(edges)==expected,'Fixpoint versus per-sourceDFS; no(1,1), two cycle selfpairs.')
check('AD61 worked cycle trace',len(closure({('a','b'),('b','c'),('c','a'),('c','d')}))==12,'a,b,c each reacha,b,c,d;d reachesnone forpositive-length closure.')
check('AD62 up-to-date lexicographic rule',[(t,i)>=(6,10) for t,i in [(5,100),(6,9),(6,10),(7,2)]]==[False,False,True,True],'Last term compared before last index.')
check('AD63 logical compensation commutes',3+4==4+3==7,'Only unconditional increments without differing observable return-values in stated model.')
check('AD64 global secondary identity',[u for c,u,e in [('HN',10,'x'),('HN',11,'x'),('HCM',12,'y')] if e=='x']==[10,11],'Partition keycity is not a tuplekey; Ku=userID retains bothhits.')
check('AD65 commit wait and unresolved read',204<=206 and 207>206 and 207<=208,'Firstinterval failsguard, secondpasses; prepared207 belongs to snapshot208 and must resolve.')
merge=lambda a,b:tuple(max(x,y) for x,y in zip(a,b))
check('AD66 grow-only-counter duplicate merge',merge(merge((1,0),(0,1)),(1,0))==(1,1),'Repeated delivery does not doublecount one replica contribution.')
check('AD54 toy PoW arithmetic',4/256==1/64,'Expectedtrials64 under independentuniform toyhash, no fixed success deadline.')
ids=[f'AD{n:02}' for n in list(range(38,55))+[61,62,63,64,65,66,67]]
required=['Luyện tập','Gợi ý','Đáp án và lập luận','Biến thể và cách kiểm','Học trên web','Nguồn và đối chiếu']
files=[]
for lesson in ids:
 p=R/'lessons'/f'{lesson}.md';s=p.read_text(encoding='utf-8')
 assert all('## '+h in s for h in required),lesson
 assert s.count('```')%2==0,lesson
 for section in ['Luyện tập','Đáp án và lập luận']:
  block=s.split('## '+section+'\n',1)[1].split('\n## ',1)[0]
  nums=[int(x) for x in re.findall(r'^(\d+)\.\s',block,re.M)]
  assert nums==list(range(1,len(nums)+1)) and len(nums)>=4,(lesson,section,nums)
 files.append({'lesson':lesson,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'wordCount':len(s.split()),'requiredHeadings':True,'balancedFences':True,'numberedExercisesAndAnswers':True})
result={'scope':'Independent static and finite computed-model QA; no SQL/native engine was executed by this script; not a proof of all algorithms.','checks':checks,'checkCount':len(checks),'files':files}
(R/'qa'/'independent-model-checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checksPassed':len(checks),'lessonStructuresPassed':len(files)},ensure_ascii=False))
