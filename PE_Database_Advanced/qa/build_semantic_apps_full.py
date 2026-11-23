"""Rebuild only semantic-apps-full.json and its own QA result.

Mappings below are authored semantic decisions after full reads, not a lexical
coverage classifier. This file may not change lessons or the shared inventory.
"""
from pathlib import Path
import hashlib
import json
import re
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'output/database-advanced'
LESSONS = {x: BASE / f'lessons/{x}.md' for x in ['AD11', 'AD12']}
INVENTORY = BASE / 'research/source-section-inventory.json'
LEDGER = BASE / 'research/semantic-apps-full.json'
QA = BASE / 'qa/semantic-apps-full-checks.json'
SELF = Path(__file__).resolve()


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def file_sha(p):
    return sha_bytes(p.read_bytes())


def rel(p):
    return p.relative_to(ROOT).as_posix()


texts = {k: p.read_text(encoding='utf-8') for k, p in LESSONS.items()}
lines = {k: s.splitlines() for k, s in texts.items()}


def paragraph(lesson, prefix, kind):
    ss = lines[lesson]
    hits = [i for i, t in enumerate(ss) if t.startswith(prefix)]
    assert len(hits) == 1, (lesson, prefix, hits)
    a = hits[0]
    b = a
    while b + 1 < len(ss) and ss[b + 1].strip():
        b += 1
    fragment = '\n'.join(ss[a:b + 1])
    heading = next((ss[i] for i in range(a, -1, -1) if ss[i].startswith('#')), None)
    return {'kind': kind, 'path': rel(LESSONS[lesson]), 'sha256': file_sha(LESSONS[lesson]),
            'heading': heading, 'line': a + 1, 'lineRange': [a + 1, b + 1],
            'paragraphAnchor': prefix, 'paragraphExcerpt': fragment,
            'fragmentSha256': sha_bytes(fragment.encode('utf-8')),
            'baselineActuallyRead': False}


def block_containing(lesson, needle):
    blocks = re.findall(r'```sql\n(.*?)```', texts[lesson], re.S)
    chosen = [b for b in blocks if needle in b]
    assert len(chosen) == 1, needle
    return chosen[0]


def sql_checks():
    results = []

    def record(name, observed, expected):
        assert observed == expected, (name, observed, expected)
        results.append({'name': name, 'observed': observed, 'expected': expected, 'passed': True})

    def rejected(conn, stmt, args=()):
        try:
            conn.execute(stmt, args)
        except sqlite3.IntegrityError:
            return True
        return False

    db = sqlite3.connect(':memory:', isolation_level=None)
    db.execute('PRAGMA foreign_keys=ON')
    db.executescript(block_containing('AD12', 'CREATE TABLE dept'))
    db.execute("INSERT INTO dept VALUES(1,'Ops',100)")
    record('I1 NOT NULL', rejected(db, 'INSERT INTO dept VALUES(2,NULL,100)'), True)
    record('I1 UNIQUE', rejected(db, "INSERT INTO dept VALUES(2,'Ops',100)"), True)
    record('I1 strict positive CHECK', rejected(db, "INSERT INTO dept VALUES(2,'Dev',0)"), True)
    db.execute('INSERT INTO staff VALUES(1,NULL,1,NULL)')
    db.execute('INSERT INTO staff VALUES(2,NULL,1,20)')
    record('I1 nullable CHECK and repeated NULL UNIQUE', db.execute('SELECT id,salary FROM staff ORDER BY id').fetchall(), [(1, None), (2, 20)])
    record('I1 salary zero rejected', rejected(db, 'INSERT INTO staff VALUES(3,NULL,1,0)'), True)
    record('I2 missing FK parent', rejected(db, 'INSERT INTO staff VALUES(3,NULL,99,20)'), True)
    db.executescript('CREATE TABLE cp(a INT,b INT,PRIMARY KEY(a,b)); CREATE TABLE cc(a INT,b INT,FOREIGN KEY(a,b) REFERENCES cp(a,b));')
    db.execute('INSERT INTO cc VALUES(NULL,7)')
    record('I2 MATCH SIMPLE partial NULL', db.execute('SELECT a,b FROM cc').fetchall(), [(None, 7)])
    db.executescript('CREATE TABLE pair(a TEXT NOT NULL,b INT NOT NULL,UNIQUE(a,b)); INSERT INTO pair VALUES("A",1),("A",2);')
    record('I1 composite UNIQUE pair', rejected(db, 'INSERT INTO pair VALUES("A",1)'), True)
    for action, expected in [('RESTRICT', [(1, 10), (2, 11)]), ('CASCADE', [(2, 11)]), ('SET NULL', [(1, None), (2, 11)])]:
        c = sqlite3.connect(':memory:', isolation_level=None)
        c.execute('PRAGMA foreign_keys=ON')
        c.executescript(f'CREATE TABLE p(id INTEGER PRIMARY KEY); CREATE TABLE c(id INTEGER PRIMARY KEY,pid INT REFERENCES p(id) ON DELETE {action}); INSERT INTO p VALUES(10),(11); INSERT INTO c VALUES(1,10),(2,11);')
        was_rejected = rejected(c, 'DELETE FROM p WHERE id=10')
        record('I2 ' + action + ' rejection', was_rejected, action == 'RESTRICT')
        record('I2 ' + action + ' post-state', c.execute('SELECT id,pid FROM c ORDER BY id').fetchall(), expected)
        c.close()
    c = sqlite3.connect(':memory:', isolation_level=None)
    c.execute('PRAGMA foreign_keys=ON')
    c.execute('CREATE TABLE mentor(name TEXT PRIMARY KEY NOT NULL,mentor TEXT NOT NULL,FOREIGN KEY(mentor) REFERENCES mentor(name) DEFERRABLE INITIALLY DEFERRED)')
    c.execute('BEGIN')
    c.execute("INSERT INTO mentor VALUES('A','B')")
    c.execute("INSERT INTO mentor VALUES('B','A')")
    c.commit()
    record('I2 deferred final valid state', c.execute('SELECT * FROM mentor ORDER BY name').fetchall(), [('A', 'B'), ('B', 'A')])
    c.execute('DELETE FROM mentor')
    c.execute('BEGIN')
    c.execute("INSERT INTO mentor VALUES('A','B')")
    record('I2 deferred commit missing parent fails', rejected(c, 'COMMIT'), True)
    c.rollback()
    record('I2 explicit rollback after failed commit', c.execute('SELECT * FROM mentor').fetchall(), [])
    db.executescript('CREATE TABLE invoice(id INTEGER PRIMARY KEY,total INTEGER NOT NULL); CREATE TABLE line(invoice_id INTEGER NOT NULL,amount INTEGER NOT NULL); INSERT INTO invoice VALUES(1,50),(2,0); INSERT INTO line VALUES(1,30),(1,20);')
    assertion_query = block_containing('AD12', 'SELECT i.id')
    record('I3 exact lesson query initial valid', db.execute(assertion_query).fetchall(), [])
    db.execute('UPDATE line SET amount=25 WHERE amount=20')
    record('I3 changed line counterexample', db.execute(assertion_query).fetchall(), [(1,)])
    db.execute('INSERT INTO invoice VALUES(3,7)')
    record('I3 empty sum counterexample', sorted(db.execute(assertion_query).fetchall()), [(1,), (3,)])
    no_coalesce = assertion_query.replace('COALESCE(\n  (SELECT SUM(l.amount) FROM line AS l WHERE l.invoice_id=i.id), 0\n)', '(SELECT SUM(l.amount) FROM line AS l WHERE l.invoice_id=i.id)')
    record('I3 NULL sum without COALESCE misses invoice3', db.execute(no_coalesce).fetchall(), [(1,)])
    db.executescript('CREATE TABLE credit(id INTEGER PRIMARY KEY,credit INT DEFAULT 0); INSERT INTO credit(id) VALUES(1); INSERT INTO credit VALUES(2,NULL),(3,-5);')
    record('T1 default versus explicit NULL versus negative', db.execute('SELECT * FROM credit ORDER BY id').fetchall(), [(1, 0), (2, None), (3, -5)])
    db.executescript('CREATE TABLE codes(id TEXT); INSERT INTO codes VALUES("11"),("2"),("003");')
    record('T1 text ordering fixture', db.execute('SELECT id FROM codes ORDER BY id COLLATE BINARY').fetchall(), [('003',), ('11',), ('2',)])
    record('T1 numeric ordering fixture', db.execute('SELECT id FROM codes ORDER BY CAST(id AS INTEGER)').fetchall(), [('2',), ('003',), ('11',)])
    db.executescript('CREATE TABLE x(id INT PRIMARY KEY,value INT); INSERT INTO x VALUES(1,10); CREATE TABLE snapshot AS SELECT * FROM x; CREATE VIEW live AS SELECT * FROM x; UPDATE x SET value=20;')
    record('T3 CTAS snapshot', db.execute('SELECT * FROM snapshot').fetchall(), [(1, 10)])
    record('T3 view after update', db.execute('SELECT * FROM live').fetchall(), [(1, 20)])
    db.executescript('CREATE TABLE notes(id INTEGER PRIMARY KEY,body TEXT);')
    for i, value in enumerate(["O'Hoa", "X' OR 'Y'='Y"], 1):
        db.execute('INSERT INTO notes VALUES(?,?)', (i, value))
        record('A1/A3 binding literal ' + str(i), db.execute('SELECT id FROM notes WHERE body=?', (value,)).fetchall(), [(i,)])
    db.executescript('CREATE TABLE account(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL); INSERT INTO account VALUES(1,100),(2,100);')
    db.execute('BEGIN')
    db.execute('UPDATE account SET balance=balance-30 WHERE id=1')
    db.rollback()
    record('AD11 transfer rollback checkpoint', db.execute('SELECT balance FROM account ORDER BY id').fetchall(), [(100,), (100,)])
    db.execute('BEGIN')
    db.execute('UPDATE account SET balance=balance-30 WHERE id=1')
    db.execute('UPDATE account SET balance=balance+30 WHERE id=2')
    db.commit()
    record('AD11 transfer committed post-state', db.execute('SELECT balance FROM account ORDER BY id').fetchall(), [(70,), (130,)])
    db.executescript('CREATE TABLE workflow(id INT PRIMARY KEY,state TEXT,version INT); INSERT INTO workflow VALUES(1,"Submitted",4);')
    counts = [db.execute('UPDATE workflow SET state="Approved",version=version+1 WHERE id=1 AND state="Submitted" AND version=4').rowcount for _ in range(2)]
    record('D1 guarded version sequential attempts', counts, [1, 0])
    db.close()

    def reachable(edges):
        adjacency = {}
        for a, b in edges:
            adjacency.setdefault(a, []).append(b)
        seen = {'R'}
        todo = ['R']
        while todo:
            u = todo.pop()
            for b in adjacency.get(u, []):
                if b not in seen:
                    seen.add(b)
                    todo.append(b)
        return sorted(seen)

    edges = [('R', 'U1'), ('R', 'U2'), ('U1', 'U3'), ('U2', 'U3'), ('U3', 'U4'), ('U4', 'U3')]
    record('P1 model grant multiple paths first cut', reachable([e for e in edges if e != ('R', 'U1')]), ['R', 'U2', 'U3', 'U4'])
    record('P1 model grant unrooted cycle second cut', reachable([e for e in edges if e[0] != 'R']), ['R'])
    latest = 2
    displayed = []
    for version, result in [(2, 'La'), (1, 'L')]:
        if version == latest:
            displayed.append(result)
    record('C1 model stale response suppression', displayed, ['La'])
    return results


# group, teaching-prefix, worked-prefix; every entry below is selected manually.
G = {
 'A1': ('AD11','SQL xử lý tập hàng;','Ví dụ đọc hai hàng'),
 'A2': ('AD11','Metadata nghĩa là','Ví dụ result có'),
 'A3': ('AD11','Ví dụ sau là pseudocode','Kết quả mong đợi là'),
 'W1': ('AD11','Ứng dụng đăng ký học','Trong URL minh họa'),
 'W2': ('AD11','Servlet API là','Container nạp class'),
 'W3': ('AD11','Server-side scripting','Ví dụ khung'),
 'C1': ('AD11','DOM là cây','Ajax là cách'),
 'C2': ('AD11','Web service nhận','Ví dụ service tính phí'),
 'C3': ('AD11','Mobile native có','Client offline cần'),
 'D1': ('AD11','Theo luồng hình9.14','Workflow nhiều người'),
 'D2': ('AD11','Pool cache connection','Cache-aside ví dụ'),
 'I1': ('AD12','Authorization trả lời','CHECK bác khi'),
 'I2': ('AD12','FK yêu cầu','Ví dụ dự án12'),
 'I3': ('AD12','Ràng buộc “tổng invoice','Giả sử total và'),
 'T1': ('AD12','DATE biểu diễn','Ví dụ có lịch giao'),
 'T2': ('AD12','Domain gom underlying','Distinct type tạo'),
 'T3': ('AD12','Khóa nhân tạo','`CREATE TABLE ... LIKE'),
 'P1': ('AD12','SQL privilege SELECT','Role gói tập quyền'),
 'S1': ('AD12','Password DB hardcode','Directory authentication tập trung'),
 'S2': ('AD12','Thay chữ cái theo','Ví dụ attacker A'),
 'S3': ('AD12','Challenge–response minh họa','Certificate gắn tên'),
 'S4': ('AD12','Audit DB mức row','Privacy gồm mục đích'),
}

# More specific worked examples replace the topic-level example where the own
# body concerns a concrete mechanism rather than the whole topic introduction.
EXAMPLES = {
 '4.4.2': 'NOT NULL loại', '4.4.3': 'NOT NULL loại',
 '4.4.6': 'Tên `budget_positive`', '4.4.7': 'Nếu hai người A,B',
 '4.5.2': 'Ví dụ có lịch giao', '4.5.3': 'DEFAULT áp dụng',
 '4.5.4': 'BLOB chứa bytes', '4.5.5': 'Distinct type tạo',
 '4.5.6': 'Ví dụ hai inserts', '4.5.8': 'Catalog→schema→object',
 '4.7.3': 'View public_order', '4.7.4': 'REFERENCES cho phép',
 '4.7.5': 'Sách §4.7.5', '4.7.6': 'Sách §4.7.5',
 '4.7.7': 'Mô hình trên là nghĩa',
 '5.1.1.1': 'JDBC chuẩn hóa', '5.1.1.2': 'Chuỗi thao tác là',
 '5.1.1.3': 'Chuỗi thao tác là', '5.1.1.6': '`CallableStatement` chuẩn bị',
 '5.1.1.8': 'Updatable result set', '5.1.3': 'ODBC là API',
 '5.1.4': 'Embedded SQL dùng', '9.2.2': 'Submit mặc định',
 '9.2.3': 'HTTP request không', '9.3.1': 'Servlet API là',
 '9.3.2': 'Servlet API là', '9.4.3': 'Framework tích hợp',
 '9.5.1.1': 'DOM là cây', '9.5.4': 'Mobile native có',
 '9.6.2': 'ORM tự ánh xạ', '9.6.2.1': 'Hibernate minh họa',
 '9.6.2.2': 'Django ORM dùng', '9.7.2': 'Nhiều application servers',
 '9.8.3': 'Password DB hardcode', '9.8.4': 'Directory authentication tập trung',
 '9.8.5': 'Mô hình trên là nghĩa', '9.8.6': 'Audit DB mức row',
 '9.9.1': 'Với miền nhỏ như', '9.9.3': 'Challenge–response minh họa',
 '9.9.3.1': 'Digital signature dùng',
}

FIGURE_LINKS = {
 177: ('AD12', 'CHECK bác khi', 'I1', '4.9 composes PK/FK and separate row checks; CHECK alone leaves nullable fields possible.'),
 182: ('AD12', 'Giả sử total và', 'I3', '4.10 expresses a universal invariant as no violating row and uses COALESCE for an empty aggregate.'),
 200: ('AD12', 'Sách §4.7.5', 'P1', '4.11 gives U5 two root-backed paths and U4 only one; revoking one grant path need not revoke all recipients.'),
 214: ('AD11', 'Chuỗi thao tác là', 'A1', '5.1 opens connection/statement with resources, executes update, then iterates a query; abbreviated handlers are not full production logic.'),
 218: ('AD11', 'Ví dụ đọc hai hàng', 'A1', '5.2 changes only the first prepared parameter for the second execute; all other parameter assignments persist.'),
 221: ('AD11', 'Metadata nghĩa là', 'A2', '5.3 returns one metadata row per schema column, not the user table rows themselves.'),
 223: ('AD11', 'Kết quả mong đợi là', 'A3', '5.4 passes Python SQL and parameter tuple separately, commits success and rolls back an insert failure.'),
 224: ('AD11', 'ODBC là API', 'A3', '5.5 binds result columns to C buffers and fills them on SQLFetch, then frees handles in reverse lifetime order.'),
 435: ('AD11', 'Trong URL minh họa', 'W1', '9.1/9.2 link table/tr/th/td source to a three-column rendered table; markup display does not execute a query.'),
 436: ('AD11', 'Submit mặc định', 'W1', '9.3/9.4 link named form controls and action/method to the selected type/name sent to handler.'),
 437: ('AD11', 'Submit mặc định', 'W1', 'Continuation explains URL query encoding versus POST body and HTML input controls; neither validates server-side authorization.'),
 438: ('AD11', 'Container nạp class', 'W2', '9.5 has separate web, application and database server roles after the browser; these deployment roles differ from MVC responsibilities.'),
 439: ('AD11', 'Container nạp class', 'W2', '9.6 merges web/application deployment while retaining a distinct database server; session state survives individual HTTP requests.'),
 441: ('AD11', 'Servlet API là', 'W2', '9.7 maps URL to handler, extracts request fields and writes response; omitted JDBC/authentication details must still be implemented.'),
 443: ('AD11', 'Ví dụ result có', 'A2', '9.8 uses result metadata to print headers/cells; zero-based ResultSet getter and raw HTML concatenation in the abbreviated source are corrected.'),
 446: ('AD11', 'Server-side scripting', 'W3', '9.9 mixes static HTML with a JSP server-side dynamic region; browser receives generated output rather than Java source.'),
 449: ('AD11', 'Framework tích hợp', 'W3', '9.10 routes through Django view/session/query cursor and returns HTML; raw unescaped string rendering is replaced by a template contract.'),
 451: ('AD11', 'DOM là cây', 'C1', '9.11 attaches validation to submit and compares dates; lesson additionally checks missing/invalid values and repeats checks on server.'),
 454: ('AD11', 'Ajax là cách', 'C1', '9.12 associates autocomplete with a text input and asynchronous JSON data with table columns; two services have different response shapes.'),
 455: ('AD11', 'Ajax là cách', 'C1', '9.13 visibly shows a suggestion menu and three matching result rows; client-side display is distinct from server query execution.'),
 459: ('AD11', 'Theo luồng hình9.14', 'D1', '9.14 eight arrows connect controller/model/data access/database/view and response; these are ordered responsibilities rather than eight servers.'),
 463: ('AD11', 'Django ORM dùng', 'D1', '9.15 maps many-to-many advisees to an automatic reverse advisors relationship, requiring a relational join mapping.'),
 464: ('AD11', 'Django ORM dùng', 'D1', '9.16 iterates filtered objects and each object relationship; source plural students.advisors is a typo and lazy per-object access can cause N+1 queries.'),
}

# section|group|specific teaching paragraph|semantic comparison of this own body
DECISIONS = r'''4.4|I1|Authorization trả lời|Separates accidental inconsistency under authorized writes from access control; predicates, cost, schema declarations and validation of old data are explained.
4.4.1|I1|NOT NULL loại|Identifies relation-level NOT NULL, UNIQUE and CHECK alongside primary keys, with non-equivalent roles and composite-key counterexamples.
4.4.2|I1|NOT NULL loại|NULL absence and explicit NOT NULL are taught with insert rejection, and primary-key behavior is qualified for the actual SQLite fixture.
4.4.3|I1|NOT NULL loại|Composite UNIQUE and nullable uniqueness are distinguished; the exercise includes duplicate/nonduplicate pairs and repeated NULL with an engine caveat.
4.4.4|I1|CHECK bác khi|CHECK rejects false but permits unknown; strict positive differs from nonnegative and NOT NULL must be separate. Constraint placement is explained.
4.4.5|I2|FK yêu cầu|Covers compatible referenced keys, NULL including partial-null composite MATCH SIMPLE, delete/update cascade and alternatives with full-chain failure reasoning.
4.4.6|I1|Tên `budget_positive`|Names support diagnostics and migrations; standard DROP CONSTRAINT is separated from engine-specific ALTER and old-row validation.
4.4.7|I2|Nếu hai người A,B|Immediate versus deferred checking is traced on mutual references, final failed commit and nullable workaround; no MySQL deferrability claim.
4.4.8|I3|Ràng buộc “tổng invoice|Cross-table invariants, invalid FK workaround, unsupported assertion/subquery-CHECK syntax, all mutation directions, cost, and forall/not-exists reasoning are taught.
4.5|T1|DATE biểu diễn|Introduces additional temporal types and links to basic user-defined distinctions; parent introduction does not receive automatic child credit.
4.5.1|T1|DATE biểu diễn|Covers date/time/timestamp precision and zones, extraction/current values/intervals; source temporal-validity sidebar is explained with interval and key implications.
4.5.2|T1|Formatting thay|Separates CAST, text/numeric sort and display formatting; compatible-type COALESCE/CASE and product-specific DECODE are qualified.
4.5.3|T1|DEFAULT áp dụng|Omitted attribute gets default, explicit NULL remains NULL, and default does not enforce a range; three-row output checks each case.
4.5.4|T2|BLOB chứa bytes|BLOB versus CLOB, locator/stream and bounded memory/partial reads are explained. Temporal sidebar in this own body is covered separately in T1.
4.5.5|T2|Distinct type tạo|Strong distinct types versus constrained domains are contrasted, including defaults, compatible assignment, currency and explicit cast limitations; structured types are bounded.
4.5.6|T3|Khóa nhân tạo|Identity ALWAYS/BY DEFAULT, separate sequences, MAX+1 race and generated-key API are taught with gap/commit-order caveats.
4.5.7|T3|`CREATE TABLE ... LIKE|LIKE schema copy and CTAS materialization/data defaults are distinguished from live views and copying constraints; snapshot example and exercise verify result.
4.5.8|T3|Catalog→schema→object|Catalog/schema/object naming, omitted qualifiers and per-connection environment/defaults are explained with test/prod isolation and permission limits.
4.7|P1|SQL privilege SELECT|Privilege types, object/schema authority and rejection of unauthorized actions are connected to a working least-privilege policy, not only deny-all tests.
4.7.1|P1|SQL privilege SELECT|GRANT/REVOKE, column update, direct versus inherited paths, PUBLIC breadth and grant option are taught; revoke-one-path is not assumed effective denial.
4.7.2|P1|Role gói tập quyền|Role inheritance and user-specific audit identities are explained with reader/support/Mai and direct-grant residual access; activation is engine-qualified.
4.7.3|P1|View public_order|View authorization before expansion, creator privilege limits, updatability, EXECUTE and definer/invoker are distinguished; base-table bypass must deny.
4.7.4|P1|REFERENCES cho phép|Schema authority and REFERENCES are motivated by a child FK that constrains another owner's deletes, including dependency limitations of subquery constraints.
4.7.5|P1|Với grant option|Grant option versus ordinary privilege and rooted grant-path semantics are taught with a concrete graph and current-role grantor explanation.
4.7.6|P1|Sách §4.7.5|Multiple grant paths, unsupported cycles, CASCADE/RESTRICT, grant-option-only revocation and role grantor lifetimes have trace, algorithm and reachability proof.
4.7.7|P1|Với grant option|Row predicates use trusted application principal, pool context reset and population-correct aggregates; mechanism is not falsely attributed to MySQL.
5.1|A1|SQL xử lý tập hàng;|Explains SQL relation versus host variables, non-query application work and dynamic versus embedded SQL preprocessing; broad SQL expressiveness claims are qualified.
5.1.1|A1|JDBC chuẩn hóa|JDBC is a Java API implemented by product driver rather than a universal wire protocol; configuration and web-only learner separation are explicit.
5.1.1.1|A1|JDBC chuẩn hóa|Connection profile components, driver availability, product protocol and secret location are taught using a non-routable example URL.
5.1.1.2|A1|Chuỗi thao tác là|Statement object and executeQuery/executeUpdate returns are explained, with zero update count versus exception and DDL qualification.
5.1.1.3|A1|Chuỗi thao tác là|SQLException versus programming failures, try-with-resources, rollback decision and reverse-order cleanup are taught without retrying all exceptions.
5.1.1.4|A1|Ví dụ đọc hai hàng|Cursor before first/next true true false, empty result, getters by label/one-based position, decimal and SQL NULL checks have exact trace and answers.
5.1.1.5|A1|Ví dụ đọc hai hàng|Prepared value binding, persisted parameter assignments and driver prepare timing are covered; injection and identifier allowlist are handled by original example and practice.
5.1.1.6|A2|`CallableStatement` chuẩn bị|Routine call order registers OUT, binds IN, executes then reads output, with distinct EXECUTE/transaction contracts.
5.1.1.7|A2|Metadata nghĩa là|Result metadata versus database metadata, column patterns, table types, PK/FK/capabilities and generic rendering are taught with secret projection counterexample.
5.1.1.8|A2|Updatable result set|Autocommit boundary plus updatable result sets, RowSet snapshots, Blob/Clob locators and stream writes/reads have assumptions and exercises.
5.1.2|A3|Ví dụ sau là pseudocode|Python DB-API connection/cursor, parameter sequence and driver marker, commit/rollback/cleanup, quoted-name output and driver-specific defaults are explained.
5.1.3|A3|ODBC là API|Environment/connection/statement lifecycle, input/output binding, buffers/NULL/diagnostics, cleanup, transaction and conformance/CLI are covered by trace and self-check.
5.1.4|A3|Embedded SQL dùng|EXEC SQL, colon host variables, cursor fetch/indicators, preprocessor compile/runtime tradeoff and embedded-database distinction are explained and exercised.
9.1|W1|Ứng dụng đăng ký học|Front end/business/data access, forms and shared backend for browser/mobile are motivated against direct DB access and coordinated desktop updates.
9.2|W1|Trong URL minh họa|Web transport/route/form basics introduce the next children with an actual request/output, without assuming a route is a physical file.
9.2.1|W1|Trong URL minh họa|Scheme/host/path/query and URL-encoded arguments are decomposed; HTTPS versus HTTP and dynamic handler mapping are explained.
9.2.2|W1|Submit mặc định|HTML table/form controls, action/method/name, GET/POST, CSS and date/time/file/range controls have source markup and outcome; client constraints are untrusted.
9.2.3|W1|HTTP request không|Web/application/DB layers, CGI overhead, cookies and server-side session identity/lifetime are taught; persistent transport is separated from stateless semantics.
9.3|W2|Servlet API là|Servlet is a container-handler API for dynamic responses, with routing/request/response and lifecycle rather than a new process per request.
9.3.1|W2|Servlet API là|Request→session→parameter validation→business→JDBC→escaped response is traced; output metadata does not expose arbitrary columns or raw HTML values.
9.3.2|W2|Servlet API là|getSession false/true, login-set attributes, missing/expired state and per-request principal are distinguished from untrusted parameters/cookies.
9.3.3|W2|Container nạp class|init/service/doGet/doPost/destroy and parallel requests on a shared instance are explained with a mutable-field interleaving counterexample and repair.
9.3.4|W2|Container nạp class|Application server deploy/stop/monitor/resource responsibilities are taught with a concrete operational self-check, without recommending historical product versions.
9.4|W3|Server-side scripting|Alternative server-side rendering/framework roles are explained through where code executes and what reaches the browser.
9.4.1|W3|Server-side scripting|Static markup plus server-executed dynamic regions, generated output and source leakage caveat have an original greeting output example.
9.4.1.1|W3|Server-side scripting|JSP scriptlets translate into servlet/compile and tags/templates reduce Java string markup; example output is escaped rather than copied unsafely.
9.4.1.2|W3|Server-side scripting|PHP delimiters, request arrays and echo output are explained as server execution; browser-only outcome is contrasted with secret/source configuration risk.
9.4.2|W3|Framework tích hợp|Routing/controllers, form validation, sessions/authentication, templates, ORM and scaffold CRUD are taught with independent allow/deny responsibilities.
9.4.3|W3|Framework tích hợp|Django URL mapping/view function, request.GET, trusted session, fixed query branches, cursor context, config/template roles and invalid enum rejection are traced.
9.5|C2|Web service nhận|Client-side UI code talks to backend services rather than direct DB; response schema, transport and multiple client kinds are explained.
9.5.1|C1|DOM là cây|JavaScript's three roles validation/DOM/service interaction are tied to a concrete asynchronous search UI and server checks.
9.5.1.1|C1|DOM là cây|HTML input and JS validation cover ranges/date ordering plus missing/invalid input; server validates again despite bypassable client checks.
9.5.1.2|C1|DOM là cây|DOM mutation, item rows/widgets and server events are distinguished from database transactions; responsive behavior and event assumptions are explicit.
9.5.1.3|C1|Ajax là cách|JSON array versus data-row object contracts, autocomplete/table fetch, URL encoding and out-of-order responses have concrete version trace and answer.
9.5.2|C2|Web service nhận|HTTP services, REST caveat, JSON/XML, formal SOAP/WSDL family and backend-to-backend services are covered with remote side-effect/timeout boundaries.
9.5.3|C3|Client offline cần|Web Storage correct methods, IndexedDB indices/version migration and quota caveats are covered by outbox requestId/baseVersion conflict example.
9.5.4|C3|Mobile native có|Native/cross-platform/PWA tradeoffs, local storage, permissions, service workers and compilation role are explained without requiring native installation.
9.6|D1|Theo luồng hình9.14|All numbered MVC/data-access flow responsibilities are traced and separated from deployment tier counts; multiple device views share business action.
9.6.1|D1|Workflow nhiều người|Business guards and multi-participant workflows include deadlines/escalation; finite state/version transition has induction reasoning and race-oriented exercise.
9.6.2|D1|ORM tự ánh xạ|Demand-loaded object/relational mappings, manual conversion motivation, PK identity and many-to-many join tables have original three-pair output.
9.6.2.1|D1|Hibernate minh họa|JPA annotations/files, configuration, session/unit-of-work/transaction, managed changes, key load, HQL versus SQL and bypass implications are covered.
9.6.2.2|D1|Django ORM dùng|Django fields/filter/relationship directions, SQL-backed output, N+1 query count and migrations/backfill are explained; adjacent Figure9.16 was read too.
9.7|D2|Nhiều application servers|Performance distinguishes per-request work from parallel scale and gives capacity assumptions; adjacent prior-section Figure9.16 is credited to ORM, not invented as performance proof.
9.7.1|D2|Pool cache connection|Connection pooling/DataSource, result/page/fragment caching, materialized result maintenance, KV partitioning, eviction versus freshness and invalidation race are taught.
9.7.2|D2|Nhiều application servers|Load distribution, session affinity/shared state, shared DB bottleneck and query reduction have a numeric bound; source IP/session rule is qualified.
9.8|S1|Authentication kiểm|Application security beyond DB authorization is explained as distinct identity/action/secret boundaries; finite policy tests are bounded evidence.
9.8.1|P1|Ghép `WHERE name|Literal value binding and dynamic identifier allowlist address both injection classes with fixture-only request tests and quoted-name cases.
9.8.2|P1|XSS xuất hiện|XSS output context versus CSRF ambient credential risk are distinguished, with framework token/origin policy, safe GET and fixture outcomes.
9.8.3|S1|Password DB hardcode|Plain source/config secret exposure, key separation, rotation/least privilege and network restrictions are taught with compromised-app boundary caveat.
9.8.4|S1|Authentication kiểm|Independent factors, OTP/phishing limits, directory centralization versus SSO, trusted assertions and OAuth authorization distinction have concrete rejection cases.
9.8.5|P1|Với grant option|Shared DB account/end-user context, per-user view scaling, declarative row policy and application surface/bypass risks are tied to trusted principal and pool cleanup.
9.8.6|S4|Audit DB mức row|DB versus app actor/action granularity, change reconstruction/correction, separate log protection and tamper-evidence limits have grade/version example and answer.
9.8.7|S4|Privacy gồm mục đích|Purpose/retention/sharing/minimization and reidentification through DOB/postcode plus small aggregates are taught without claiming a legal determination.
9.9|S2|Thay chữ cái theo|Confidentiality/identity-theft motivation and threat-specific protection are explained; no universal law or 2019 algorithm security claim is promoted.
9.9.1|S2|Nguồn dùng tích hai|Key secrecy, symmetric/public-key, AES block/key size, weak substitution, hybrid scheme and frequency/dictionary attacks are covered with corrected RSA/IV simplifications.
9.9.2|S2|Disk/block encryption|Block/column/application encryption, master/wallet key boundary, backup/restore and encrypted querying/index leakage are explained by attacker A/B/C cases.
9.9.3|S3|Challenge–response minh họa|Fresh challenge/response and private-key possession are separated from identity binding; replay and hardware storage assumptions are explicit.
9.9.3.1|S3|Digital signature dùng|Signature authenticity/integrity, wrong message/key checks and nonrepudiation assumptions are taught without equating every signature with private-key encryption.
9.9.3.2|S3|Certificate gắn tên|Root/intermediate/leaf chain, trust anchor, signature/constraints/name/time checks, recursion termination and TLS key possession are taught with wrong-host rejection.''' 


def main():
    assert ROOT.name == 'PE USTH', ROOT
    frozen_path = BASE / 'lessons/AD85.md'
    frozen = file_sha(frozen_path)
    inv = json.loads(INVENTORY.read_text(encoding='utf-8'))
    assigned = [u for u in inv['bookSections'] if set(u.get('plannedAdvancedLessonIds', [])) & set(LESSONS)]
    decisions = {}
    for row in DECISIONS.splitlines():
        section, group, prefix, judgment = row.split('|', 3)
        assert section not in decisions
        decisions[section] = group, prefix, judgment
    assert len(assigned) == len(decisions) == 85
    assert set(decisions) == {u['section'] for u in assigned}
    source_paths = {Path(u['sourcePath']) for u in assigned}
    source_data = {p.as_posix(): (ROOT / p).read_text(encoding='utf-8').splitlines() for p in source_paths}
    units = []
    for u in assigned:
        section = u['section']
        group, prefix, judgment = decisions[section]
        lesson, general, example = G[group]
        ss = source_data[Path(u['sourcePath']).as_posix()]
        start = u['sourceLine']
        next_lines = [v['sourceLine'] for v in inv['bookSections'] if v['chapter'] == u['chapter'] and v['sourceLine'] > start]
        end = min(next_lines) - 1 if next_lines else u['scopeLineEnd']
        source_path = ROOT / u['sourcePath']
        source_fragment = '\n'.join(ss[start - 1:end])
        evidence = [paragraph(lesson, prefix, 'teaching'), paragraph(lesson, EXAMPLES.get(section, example), 'worked-example')]
        if group == 'P1' and section in ['9.8.1', '9.8.2']:
            evidence += [paragraph('AD12', 'Trong lab, ba request', 'worked-example'), paragraph('AD12', '3. Phân loại ba lỗi:', 'activity'), paragraph('AD12', '3. XSS→escaping', 'answer-rubric')]
        else:
            evidence += [paragraph(lesson, f'**Tự kiểm {group}.**', 'activity'), paragraph(lesson, f'**Đáp án {group}.**', 'answer-rubric')]
        proof = []
        if section in ['4.7.5', '4.7.6']:
            proof = [paragraph('AD12', 'Thuật toán mô hình:', 'algorithm-and-correctness')]
        if section == '4.4.8':
            proof = [paragraph('AD12', 'Giả sử total và', 'equivalence-and-null-assumptions')]
        if section == '9.6.1':
            proof = [paragraph('AD11', 'Workflow nhiều người', 'guarded-transition-induction')]
        if section == '9.9.3.2':
            proof = [paragraph('AD12', 'Certificate gắn tên', 'trust-chain-reasoning')]
        if section in ['5.1.1.4', '5.1.3', '5.1.4']:
            proof = [paragraph(lesson, prefix, 'api-lifecycle-or-fetch-algorithm')]
        units.append({'section': section, 'title': u['title'], 'owners': u['plannedAdvancedLessonIds'],
            'source': {'path': rel(source_path), 'sha256': file_sha(source_path), 'ownBodyLines': [start, end],
                       'scopeLines': [start, u['scopeLineEnd']], 'ownBodySha256': sha_bytes(source_fragment.encode('utf-8')),
                       'hashNormalization': 'UTF-8 LF-joined splitlines, no terminal LF'},
            'sourceReadStatus': 'full-assigned-own-body-read', 'semanticStatus': 'complete',
            'baselineCreditApplied': False, 'semanticComparison': judgment, 'evidence': evidence,
            'algorithmProofEvidence': proof,
            'sourceAlgorithmProofReview': {'inventoryAlgorithmSignals': u.get('algorithmSignals', []),
                'inventoryProofSignals': u.get('proofSignals', []), 'formalSourceProofPresent': False,
                'conclusion': 'Full own body read. Source gives explanatory/API/query/architecture/cryptography sketches, not a formal theorem proof. Applicable execution steps and correctness assumptions are preserved; original proof/trace additions are explicitly bounded by their models.'},
            'childUnits': [v['section'] for v in inv['bookSections'] if v.get('parentSection') == section],
            'remainingGaps': []})
    results = sql_checks()
    pdf = Path('D:/Downloads/Abraham-Silberschatz-Henry-F.-Korth-S.-Sudarshan-Database-System-Concepts-McGraw-Hill-Education-2019.pdf')
    pages = {177: '4.9 PK/FK/CHECK schema', 182: '4.10 NOT EXISTS assertion', 200: '4.11 rooted grant graph',
        214: '5.1 JDBC', 218: '5.2 persisted prepared parameters', 221: '5.3 metadata rows', 223: '5.4 Python driver API', 224: '5.5 ODBC lifecycle',
        435: '9.1–9.2 table source/render', 436: '9.3–9.4 form source/render', 437: 'form methods and server transition',
        438: '9.5 separate web/application/database layers', 439: '9.6 combined web/application layer',
        441: '9.7 servlet request/response', 443: '9.8 ResultSet renderer', 446: '9.9 JSP execution region',
        449: '9.10 Django handler/cursor', 451: '9.11 validation', 454: '9.12 asynchronous table/autocomplete',
        455: '9.13 rendered autocomplete/table', 459: '9.14 eight-step MVC/data access', 463: '9.15 many-to-many Django model', 464: '9.16 reverse relationship query'}
    figures = []
    for page, observation in pages.items():
        p = ROOT / f'tmp/database-source/apps-full-figures/page-{page}.png'
        assert p.is_file()
        flesson, fprefix, fgroup, fobservation = FIGURE_LINKS[page]
        figures.append({'sourcePdf': str(pdf), 'sourcePdfSha256': file_sha(pdf), 'pdfPageOneBased': page,
                        'renderedPath': rel(p), 'renderedSha256': file_sha(p), 'visuallyInspected': True,
                        'semanticObservation': fobservation, 'sourceLabel': observation,
                        'counterpart': [paragraph(flesson, fprefix, 'teaching'),
                            paragraph(flesson, f'**Tự kiểm {fgroup}.**', 'activity'),
                            paragraph(flesson, f'**Đáp án {fgroup}.**', 'answer-rubric')]})
    ledger = {'date': '2026-11-05', 'scope': 'Exactly 85 assigned book own bodies for AD11/AD12. No certification of other lessons, USTH pages, production runtime or whole-course coverage.',
        'ownedLessonIds': list(LESSONS), 'inventorySha256': file_sha(INVENTORY), 'lessonHashes': {k: file_sha(p) for k, p in LESSONS.items()},
        'sourceHashes': {p: file_sha(ROOT / p) for p in sorted(source_data)},
        'readBatches': [{'id': 'apps-ch4-full', 'sourcePath': 'tmp/database-source/chapter-4.txt', 'readLineRanges': [[1719, 2548], [2624, 2953]], 'baselineCreditApplied': False},
                        {'id': 'apps-ch5-full', 'sourcePath': 'tmp/database-source/chapter-5.txt', 'readLineRanges': [[15, 658]], 'baselineCreditApplied': False},
                        {'id': 'apps-ch9-full', 'sourcePath': 'tmp/database-source/chapter-9.txt', 'readLineRanges': [[22, 2097]], 'baselineCreditApplied': False}],
        'fullLessonReads': [rel(p) for p in LESSONS.values()], 'figureReview': figures,
        'sourceCaveats': ['Source budget>0 described as nonnegative corrected to strictly positive.', 'Web Storage deletion method corrected deleteItem to removeItem.', 'JDBC renderer source uses zero-based getter; lesson uses one-based JDBC columns and escaped output.', 'Django Figure9.16 plural students.advisors corrected conceptually to each student relationship.', 'HTTP statelessness separated from persistent transport; JavaScript browser sandbox is not application security.', 'Historical framework API/product popularity not promoted as current installation recommendation.', 'RSA modulus-only sketch, private-key encryption description of all signatures and arbitrary IV/salt concatenation are explicitly qualified.', 'IP affinity and MFA/HTTPS are not absolute guarantees; engine encryption/index/deferrability/role details remain version-dependent.'],
        'units': units, 'totals': {'assignedOwnBodies': 85, 'fullRead': 85, 'semanticComplete': 85, 'remainingGaps': 0},
        'validation': {'engine': 'Python stdlib sqlite3 ' + sqlite3.sqlite_version, 'finiteChecks': len(results),
            'resultFile': rel(QA), 'scope': 'Single-process in-memory fixture SQL plus finite grant/response models. Includes exact SQL blocks extracted from lesson for constraints/assertion query.',
            'notValidated': ['MySQL or another server DB', 'JDBC/ODBC/Python remote drivers', 'Django/Hibernate runtime', 'real interleaved transactions/network', 'deployed web lab', 'production security/SSO/TLS/cryptography']},
        'status': 'full-owned-source-semantic-review-complete; web-lab implementation contract remains separate',
        'remainingGaps': [], 'baselineCreditApplied': False,
        'frozen': {'AD85': {'path': rel(frozen_path), 'sha256': frozen, 'untouchedByThisScript': True}},
        'regeneration': {'script': rel(SELF), 'scriptSha256': file_sha(SELF), 'algorithm': 'Own end is next numbered heading in same chapter minus one; terminal scope only for final unit. Explicit human-authored mapping selects paragraphs, no keyword-based completeness promotion.'}}
    # Validate every witness against the exact current source, then freeze file bytes.
    witness_groups = [unit['evidence'] + unit['algorithmProofEvidence'] for unit in units]
    witness_groups.extend(figure['counterpart'] for figure in figures)
    for witnesses in witness_groups:
        for w in witnesses:
            p = ROOT / w['path']
            a, b = w['lineRange']
            fragment = '\n'.join(p.read_text(encoding='utf-8').splitlines()[a - 1:b])
            assert file_sha(p) == w['sha256']
            assert fragment == w['paragraphExcerpt']
            assert sha_bytes(fragment.encode('utf-8')) == w['fragmentSha256']
    assert file_sha(frozen_path) == frozen
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    qa = {'date': '2026-11-05', 'scope': ledger['validation'], 'ledgerPath': rel(LEDGER), 'ledgerSha256': file_sha(LEDGER),
          'scriptSha256': file_sha(SELF), 'lessonHashes': ledger['lessonHashes'], 'inventorySha256': file_sha(INVENTORY),
          'assignedOwnBodies': len(units), 'allWitnessLineRangesHashesVerified': True, 'frozenAD85': frozen,
          'checks': results, 'passed': True}
    QA.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'units': len(units), 'checks': len(results), 'ledger': rel(LEDGER), 'lessonHashes': ledger['lessonHashes'], 'frozenAD85': frozen}, ensure_ascii=False))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
