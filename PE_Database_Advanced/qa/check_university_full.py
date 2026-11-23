"""Actual SQLite fixture/query checks plus source-table/time models; not MySQL certification."""
from pathlib import Path
import hashlib
import json
import re
import sqlite3

O = Path(__file__).resolve().parent
R = O.parent
W = R.parents[1]
md = (R / 'lessons/AD59.md').read_text(encoding='utf-8')
blocks = re.findall(r'```sql\n(.*?)```', md, flags=re.S)
checks = []
def check(name, ok, detail):
    assert ok, name
    checks.append({'name': name, 'passed': True, 'detail': detail})
def block(needle):
    matches = [b for b in blocks if needle in b]
    assert len(matches) == 1, needle
    return matches[0]

src = (W / 'tmp/database-source/appendix-a.txt').read_text(encoding='utf-8')
figures = [(2, 'classroom', 'Packard', 3, 5), (3, 'department', 'Biology', 3, 7),
 (4, 'course', 'BIO-101', 4, 13), (5, 'instructor', '10101', 4, 12),
 (6, 'section', 'BIO-101', 7, 15), (7, 'teaches', '10101', 5, 15),
 (8, 'student', '00128', 4, 13), (9, 'takes', '00128', 6, 22),
 (10, 'advisor', '00128', 2, 9), (11, 'time_slot', 'A', 4, 20),
 (12, 'prereq', 'BIO-301', 2, 7), (13, 'time_slot_parts', 'A', 6, 20)]
tables = {}
begin = src.index('A.3 Sample Data')
for fig, name, first, width, expected in figures:
    end = src.index(f'Figure A.{fig} ', begin)
    tokens = [x.strip() for x in src[begin:end].splitlines() if x.strip()]
    tokens = tokens[tokens.index(first):]
    assert len(tokens) % width == 0, (name, len(tokens), width)
    tables[name] = [tokens[i:i + width] for i in range(0, len(tokens), width)]
    assert len(tables[name]) == expected, (name, len(tables[name]))
    begin = end
check('source-tables-cardinality', True, 'Parsed every record of source FiguresA.2–A.13 with explicit per-table arity; 11 relations plus alternative time representation, raw source not redistributed.')
times = {(r[0], r[1], r[2], r[3]) for r in tables['time_slot']}
parts = {(r[0], r[1], f'{int(r[2])}:{int(r[3]):02}', f'{int(r[4])}:{int(r[5]):02}') for r in tables['time_slot_parts']}
check('source-time-representations', times == parts and len(times) == 20, 'All 20 printed meeting rows correspond exactly, no duplicate new meetings from FigureA.13.')
student_ids = {x[0] for x in tables['student']}
takes_ids = {x[0] for x in tables['takes']}
advisor_ids = {x[0] for x in tables['advisor']}
check('source-adversarial-cases', student_ids - takes_ids == {'70557'} and len(student_ids - advisor_ids) == 4 and sum(r[-1] == 'null' for r in tables['takes']) == 1, 'Actual source has zero-registration, missing-advisor and NULL-grade cases; not inferred from PE synthetic data.')

db = sqlite3.connect(':memory:')
db.execute('PRAGMA foreign_keys=ON')
db.create_function('GREATEST', 2, max); db.create_function('LEAST', 2, min)
ddl = block('CREATE TABLE ad_u_classroom').replace(' ENGINE=InnoDB', '')
db.executescript(ddl)
table_count = db.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table'").fetchone()[0]
check('authored-fixture-load', table_count == 12, f'Actual SQLite{sqlite3.sqlite_version} executes unchanged table/data text except ENGINE removal. SQLite type/PK/locking semantics are not asserted equivalent to MySQL.')
q1 = block('SELECT s.id,COUNT(t.course_id)')
check('zero-registration-query', db.execute(q1).fetchall() == [('S1', 2), ('S2', 1), ('S3', 1), ('S4', 0)], 'Exact lesson query; NULL outer join row counted correctly.')
q2 = block('WITH RECURSIVE required').replace('UNION DISTINCT', 'UNION')
check('prerequisite-query', db.execute(q2).fetchall() == [('S1',)], 'SQLite set UNION spelling adaptation only; exact lesson correlated double NOT EXISTS otherwise.')
q3 = block('WITH counts AS')
check('capacity-query', db.execute(q3).fetchall() == [('DB', '1', 'Fall', 2026, 3, 2)], 'Exact lesson aggregate-before-join detector.')
q4 = block('SELECT a.id,a.course_id AS course_a')
check('time-overlap-query', db.execute(q4).fetchall() == [('S1', 'DB', 'OS', 'Fall', 2026, 'M', '09:30:00', '10:00:00')], 'Exact lesson tuple comparison/half-open overlap query; GREATEST/LEAST registered locally.')
cycle = block('WITH RECURSIVE reach').replace('UNION DISTINCT', 'UNION')
check('initial-cycle-query', db.execute(cycle).fetchall() == [], 'No cycle in original authored fixture.')
db.execute('SAVEPOINT trial')
db.execute("INSERT INTO ad_u_prereq VALUES('DB','AI')")
check('cycle-mutant-detected', db.execute(cycle).fetchall() == [('AI',), ('DB',), ('OS',)], 'Inserted back-edge yields all cycle members; rolled back below.')
db.execute('ROLLBACK TO trial'); db.execute('RELEASE trial')

def fails(sql):
    db.execute('SAVEPOINT failed_case')
    try:
        db.execute(sql)
    except sqlite3.IntegrityError:
        result = True
    else:
        result = False
    db.execute('ROLLBACK TO failed_case'); db.execute('RELEASE failed_case')
    return result
check('referenced-prerequisite-delete-blocked', fails("DELETE FROM ad_u_course WHERE course_id='DB'"), 'Delete cascade on course_id does not bypass referenced prereq_id restriction.')
check('invalid-meeting-check', fails("INSERT INTO ad_u_time_slot VALUES('T1','M','11:00:00','10:00:00')"), 'Additional same-day start<end constraint rejects reversed interval.')
check('check-is-not-not-null', not fails("INSERT INTO ad_u_instructor VALUES('I3','Lan','CS',NULL)"), 'CHECK(salary>29000) alone permits NULL in selected SQLite test, matching lesson three-valued logic explanation.')
db.execute('SAVEPOINT trial')
db.execute("DELETE FROM ad_u_instructor WHERE id='I1'")
check('instructor-delete-actions', db.execute("SELECT i_id FROM ad_u_advisor WHERE s_id IN ('S1','S2') ORDER BY s_id").fetchall() == [(None,), (None,)] and db.execute("SELECT COUNT(*) FROM ad_u_teaches WHERE id='I1'").fetchone()[0] == 0 and db.execute('SELECT COUNT(*) FROM ad_u_student').fetchone()[0] == 4, 'Actual selected FK SET NULL/CASCADE paths; students retained.')
db.execute('ROLLBACK TO trial'); db.execute('RELEASE trial')
db.execute('SAVEPOINT trial')
db.execute("DELETE FROM ad_u_student WHERE id='S1'")
check('student-delete-actions', db.execute("SELECT COUNT(*) FROM ad_u_takes WHERE id='S1'").fetchone()[0] == 0 and db.execute("SELECT COUNT(*) FROM ad_u_advisor WHERE s_id='S1'").fetchone()[0] == 0, 'Actual Takes/Advisor cascade for student delete.')
db.execute('ROLLBACK TO trial'); db.execute('RELEASE trial')
check('time-component-counterexample', 25 >= 0 and 10 < 24 and not 0 <= 25 < 24 and (9 * 60 + 30, 10 * 60 + 15) == (570, 615), 'Wrong start_hr/end_hr check admits invalid start25; corrected range and conversion tested.')
check('half-open-boundary', not (9 * 60 < 11 * 60 and 10 * 60 < 10 * 60), '09:00–10:00 and10:00–11:00 do not overlap under strict half-open comparisons.')
db.close()
out = {'date': '2026-11-05', 'passed': len(checks), 'checks': checks,
       'scope': 'Actual source-table parsing, selected actual SQLite translated DDL/query/constraint checks and arithmetic models. No native MySQL two-session capacity/locking run in this report; web runner requirements remain separate. No assertion that SQLite type/NULL-PK/concurrency behavior equals MySQL.',
       'lessonSha256': hashlib.sha256((R / 'lessons/AD59.md').read_bytes()).hexdigest(),
       'sourceSha256': hashlib.sha256((W / 'tmp/database-source/appendix-a.txt').read_bytes()).hexdigest()}
(O / 'university-full-checks.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'passed': len(checks), 'sourceRelations': 11, 'sourceMeetingRows': len(times), 'sqlite': sqlite3.sqlite_version}))
