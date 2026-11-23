"""Verify the explicitly named, packaged PE Chinook adaptation on task MySQL."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parents[1]/'tmp/database-advanced-vendor'))
import pymysql
from pymysql.constants import CLIENT

fixture=ROOT/'fixtures/chinook_advanced.sql'
text=fixture.read_text(encoding='utf-8-sig')
directives_view=re.sub(r'/\*.*?\*/','',text,flags=re.S)
directives_view=re.sub(r'^\s*--.*$','',directives_view,flags=re.M)
assert not re.search(r'^\s*(?:DROP\s+DATABASE|CREATE\s+DATABASE|USE\s)',directives_view,re.M|re.I)
checks=[]
with pymysql.connect(host='127.0.0.1',port=33374,user='root',autocommit=True,
                     charset='utf8mb4',read_timeout=20,client_flag=CLIENT.MULTI_STATEMENTS) as c:
    with c.cursor() as cur:
        cur.execute('SELECT CONNECTION_ID()')
        schema='pe_advanced_chinook_payload_20261105_'+str(cur.fetchone()[0])
        assert re.fullmatch(r'pe_advanced_chinook_payload_20261105_[0-9]+',schema)
        cur.execute('SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME=%s',(schema,))
        existing=cur.fetchall()
        if existing:
            raise RuntimeError('Refusing to modify pre-existing sandbox database: '+schema)
        cur.execute('CREATE DATABASE `'+schema+'`')
        c.select_db(schema)
        cur.execute(text)
        while cur.nextset():pass
        cur.execute('SELECT VERSION(),DATABASE()')
        engine=list(cur.fetchone())
        for table,expected in [('Invoice',412),('InvoiceLine',2240)]:
            cur.execute('SELECT COUNT(*) FROM `'+schema+'`.`'+table+'`')
            actual=cur.fetchone()[0]
            checks.append({'name':table+' row count','actual':actual,'expected':expected,'passed':actual==expected})
        cur.execute("""SELECT TABLE_NAME,COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME
          FROM information_schema.KEY_COLUMN_USAGE
          WHERE TABLE_SCHEMA=%s AND REFERENCED_TABLE_NAME IS NOT NULL
          ORDER BY TABLE_NAME,CONSTRAINT_NAME,ORDINAL_POSITION""",(schema,))
        foreign_keys=list(cur.fetchall())
        for table,column,parent,parent_column in foreign_keys:
            quote=lambda s:'`'+s.replace('`','``')+'`'
            query=('SELECT COUNT(*) FROM '+quote(table)+' AS c LEFT JOIN '+quote(parent)+' AS p '
                   'ON c.'+quote(column)+'=p.'+quote(parent_column)+' WHERE c.'+quote(column)+
                   ' IS NOT NULL AND p.'+quote(parent_column)+' IS NULL')
            cur.execute(query)
            actual=cur.fetchone()[0]
            checks.append({'name':table+'.'+column+' orphan count','actual':actual,'expected':0,'passed':actual==0})

result={'scope':'Actual packaged fixtures/chinook_advanced.sql only. Payload has no DROP/CREATE/USE database directives. Loader allocates a new validated task-prefix schema after proving absence, refuses an existing schema, selects it on the connection, then executes the packaged table/data payload unchanged. Only read-only checks run after load; schema retained. Not old pa_repo_chinook evidence or semantic certification of all lessons.',
        'engine':engine,'fixtureSha256':hashlib.sha256(fixture.read_bytes()).hexdigest(),
        'checks':checks,'passed':all(x['passed'] for x in checks)}
(ROOT/'qa/packaged-chinook-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
if not result['passed']:raise AssertionError(result)
print(json.dumps({'passed':True,'checks':len(checks),'engine':engine}))
