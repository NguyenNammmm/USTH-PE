"""Finite AD09 answer/model checks and frozen-evidence integrity, not a depth classifier."""
from pathlib import Path
from itertools import combinations
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'output/database-advanced'

def sha(data):
    return hashlib.sha256(data).hexdigest()

def fd_holds(rows, determinant, dependent):
    seen = {}
    for row in rows:
        k = tuple(row[i] for i in determinant)
        v = tuple(row[i] for i in dependent)
        if k in seen and seen[k] != v:
            return False
        seen[k] = v
    return True

def keys(attrs, fds):
    def closure(values):
        result = set(values)
        while True:
            old = result.copy()
            for left,right in fds:
                if set(left) <= result:
                    result.update(right)
            if result == old:
                return result
    result=[]
    for n in range(len(attrs)+1):
        for value in combinations(attrs,n):
            value=frozenset(value)
            if not any(k <= value for k in result) and closure(value)==set(attrs):
                result.append(value)
    return set(result)

def coverage(l,u,intervals):
    reach=l
    trace=[l]
    for s,e in sorted(intervals):
        if e<=reach:
            continue
        if s>reach:
            return False,trace
        reach=max(reach,e)
        trace.append(reach)
        if reach>=u:
            return True,trace
    return False,trace

def overlap(a,b):
    return max(a[0],b[0]) < min(a[1],b[1])

def main():
    checks=[]
    def check(name, condition, details=None):
        checks.append({'name':name,'passed':bool(condition),'details':details})

    inventory_raw=(BASE/'research/source-section-inventory.json').read_bytes()
    inventory=json.loads(inventory_raw)
    ledger=json.loads((BASE/'research/semantic-er.json').read_text(encoding='utf-8'))
    lesson_raw=(BASE/'lessons/AD09.md').read_bytes()
    lines=lesson_raw.decode('utf-8-sig').splitlines()
    check('frozen inventory and lesson hashes',
          sha(inventory_raw)==ledger['inventorySha256'] and sha(lesson_raw)==ledger['lessonSha256'])
    assigned={u['section']:u for u in inventory['bookSections'] if 'AD09' in u.get('plannedAdvancedLessonIds',[])}
    check('exactly 48 assigned own bodies, no baseline or pending credit',
          len(assigned)==len(ledger['units'])==48 and
          set(assigned)=={u['section'] for u in ledger['units']} and
          all(u['status']=='covered-after-fix' and not u['baselineCreditApplied'] for u in ledger['units']))
    source_errors=[]
    witness_errors=[]
    for u in ledger['units']:
        spec=assigned[u['section']]
        source=u['source']
        data=(ROOT/source['path']).read_bytes()
        source_lines=data.splitlines(keepends=True)
        following=[x['sourceLine'] for x in inventory['bookSections'] if x['chapter']==spec['chapter'] and x['sourceLine']>spec['sourceLine']]
        end=min(following)-1 if following else spec['scopeLineEnd']
        own=b''.join(source_lines[spec['sourceLine']-1:end])
        if not (source['rawSha256']==sha(data) and source.get('sha256',source['rawSha256'])==sha(data) and source['ownLineStart']==spec['sourceLine'] and
                source['ownLineEnd']==end and source['ownBodySha256']==sha(own) and source['readInFull']):
            source_errors.append(u['section'])
        for kind in ('explanation','workedExampleOrTrace','activity','answer'):
            w=u[kind]
            exact='\n'.join(lines[w['lineStart']-1:w['lineEnd']])
            if not (exact==w['exactParagraph'] and sha(exact.encode('utf-8'))==w['paragraphSha256'] and
                    u['lessonSha256']==sha(lesson_raw) and w.get('lessonSha256',u['lessonSha256'])==sha(lesson_raw)):
                witness_errors.append([u['section'],kind])
    check('source raw hashes and nonoverlapping own-body boundaries',not source_errors,source_errors)
    check('all exact paragraph/line witnesses fresh',not witness_errors,witness_errors)
    figures=ledger['readRangesByReviewer']['renderedContactSheets']
    check('inspected figure render artifacts unchanged',all(sha((ROOT/f['path']).read_bytes())==f['sha256'] for f in figures),{'sheets':len(figures),'figures':29})
    p=lines.index('## Luyện tập')
    h=lines.index('## Gợi ý')
    a=lines.index('## Đáp án và lập luận')
    practice=[int(m.group(1)) for line in lines[p:h] if (m:=re.match(r'^(\d+)\. ',line))]
    answers=[int(m.group(1)) for line in lines[a:] if (m:=re.match(r'^(\d+)\. ',line))]
    check('17 original activities have corresponding numbered answers',practice==answers==list(range(1,18)))

    supply={('S1','P1','J1'),('S1','P2','J2'),('S2','P1','J2')}
    sp={(s,p) for s,p,j in supply}
    sj={(s,j) for s,p,j in supply}
    pj={(p,j) for s,p,j in supply}
    joined={(s,p,j) for s,p in sp for s2,j in sj if s==s2 and (p,j) in pj}
    check('ternary pairwise projection counterexample',joined-supply=={('S1','P1','J2')},sorted(joined-supply))
    cases={f'K{i}':row for i,row in enumerate(sorted(supply),1)}
    check('intermediary entity encode/decode preserves triples',set(cases.values())==supply and len(cases)==len(supply))
    extra=supply|{('S1','P1','J2')}
    check('three endpoint FKs and triple uniqueness do not enforce PP-to-S',
          len(extra)==4 and not fd_holds(extra,[1,2],[0]))
    arrow_rows={('a','b','c1','d1'),('a','b','c2','d2')}
    check('multiple-arrow interpretations differ',
          fd_holds(arrow_rows,[0,1,2],[3]) and fd_holds(arrow_rows,[0,1,3],[2]) and not fd_holds(arrow_rows,[0,1],[2,3]))
    check('candidate keys for both arrow interpretations',
          keys('ABCD',[('AB','CD')])=={frozenset('AB')} and
          keys('ABCD',[('ABC','D'),('ABD','C')])=={frozenset('ABC'),frozenset('ABD')})
    offerings={('DB','2026A',1),('DB','2026B',1)}
    check('weak discriminator reuse and natural-key identity',
          len(offerings)==2 and len({r[2] for r in offerings})==1 and ('DB','2026A',2) not in offerings)
    slots={'S1','S2'}
    meetings={('S1','Mon',9,10),('S1','Wed',9,10.5)}
    reconstructed={slot:{row[1:] for row in meetings if row[0]==slot} for slot in slots}
    check('multivalue zero-owner and FK target tradeoff',
          reconstructed['S2']==set() and 'S2' not in {r[0] for r in meetings} and
          len({r[0] for r in meetings})<len(meetings))
    assignments={('E1','J1'),('E2','J2')}
    review=('E1','J2')
    check('aggregation requires a composite relationship reference',
          review[0] in {r[0] for r in assignments} and review[1] in {r[1] for r in assignments} and review not in assignments)
    memberships=[(False,False),(True,False),(False,True),(True,True)]
    counts={
        'partial-overlap':sum(1 for s,e in memberships),
        'partial-disjoint':sum(not(s and e) for s,e in memberships),
        'total-overlap':sum(s or e for s,e in memberships),
        'total-disjoint':sum((s or e) and not(s and e) for s,e in memberships)}
    check('specialization constraints are independent',counts=={'partial-overlap':4,'partial-disjoint':3,'total-overlap':3,'total-disjoint':2},counts)
    teachers={'T1','T2','T3'}
    students={'S1','S2','S3'}
    advisor={('T1','S1'),('T1','S2'),('T2','S3')}
    valid=lambda ss,rr: all(sum(s==student for t,s in rr)==1 for student in ss) and all(t in teachers and s in ss for t,s in rr)
    check('Advisor meaning is constant across four notations',
          valid(students,advisor) and not valid(students|{'S4'},advisor) and not valid(students,advisor|{('T2','S1')}))

    inf=float('inf')
    salary=[{'id':1,'valid':(0,31),'system':(0,inf),'amount':3000},
            {'id':2,'valid':(31,inf),'system':(31,40),'amount':3500},
            {'id':3,'valid':(31,inf),'system':(40,inf),'amount':3600}]
    query=lambda rows,v,k:[r['amount'] for r in rows if r['valid'][0]<=v<r['valid'][1] and r['system'][0]<=k<r['system'][1]]
    conflicts=lambda rows:[(x['id'],y['id']) for x,y in combinations(rows,2) if overlap(x['valid'],y['valid']) and overlap(x['system'],y['system'])]
    check('bitemporal salary snapshots and boundary detector',
          query(salary,35,36)==[3500] and query(salary,35,42)==[3600] and conflicts(salary)==[])
    pending=salary+[{'id':4,'valid':(31,inf),'system':(45,inf),'amount':3700}]
    observed=conflicts(pending)
    fixed=[dict(r,system=(40,45)) if r['id']==3 else r for r in pending]
    check('closing old system interval repairs the intended conflict',observed==[(3,4)] and conflicts(fixed)==[] and query(fixed,35,45)==[3700],observed)
    check('temporal join discards touching intervals',
          not overlap((0,31),(31,60)) and (max(0,31),min(60,90))==(31,60))
    good,trace=coverage(15,60,[(0,31),(31,90)])
    gap,gap_trace=coverage(15,60,[(0,31),(32,90)])
    endpoints_false_positive=(min(0,31)<=15 and max(20,90)>=60 and not coverage(15,60,[(0,20),(31,90)])[0])
    check('temporal FK union coverage, gap and endpoint false positive',good and trace==[15,31,90] and not gap and gap_trace==[15,31] and endpoints_false_positive,{'coveredTrace':trace,'gapTrace':gap_trace})
    intervals=list(combinations(range(5),2))
    cases_checked=0
    mismatches=[]
    for mask in range(1<<len(intervals)):
        selected=[iv for i,iv in enumerate(intervals) if mask&(1<<i)]
        for l,u in intervals:
            # Independent point-cell oracle: all breakpoints are integral, so
            # every open unit cell in the target must lie in some source interval.
            expected=all(any(s<=cell and cell+1<=e for s,e in selected) for cell in range(l,u))
            if coverage(l,u,selected)[0] != expected:
                mismatches.append([l,u,selected])
            cases_checked+=1
    check('coverage scan versus independent point-cell oracle',not mismatches,{'finiteCases':cases_checked,'failures':len(mismatches),'scope':'All interval subsets/targets on endpoints 0..4; the lesson invariant supplies the general proof.'})
    report={'date':'2026-11-05','lesson':'AD09','ledger':'research/semantic-er.json',
            'lessonSha256':sha(lesson_raw),'checks':checks,'allPassed':all(c['passed'] for c in checks),
            'sqlRuntimeUsed':False,
            'semanticClaimLimit':'Hashes confirm freshness and finite model checks confirm stated examples/answers. Full reading and manual content judgments in semantic-er.json, not these checks, support source coverage.'}
    (BASE/'qa/er-full-checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'allPassed':report['allPassed'],'checks':len(checks),'coverageOracleCases':cases_checked,'failed':[c['name'] for c in checks if not c['passed']]},ensure_ascii=False))
    if not report['allPassed']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
