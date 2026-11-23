"""Prove the post-native USTH10 edit changed only three prose passages.
Reconstruct and hash the exact MD at native execution, then compare all SQL.
This does not relabel a new SQL run as if one occurred.
"""
from pathlib import Path
import hashlib
import json
import re

R=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
native=json.loads((R/'qa/usth-final-sources-checks.json').read_text(encoding='utf-8'))
assert native['engine']=='8.4.13' and native['passed']==native['total']==106
p=R/'lessons/USTH10.md';current=p.read_text(encoding='utf-8-sig')
replacements=[
('Đây là probe bạn có thể chạy trong editor của đúng lượt. `SHOW DATABASES` trong nguồn liệt kê database theo quyền tài khoản; ở khóa này không yêu cầu tài khoản quản trị. Client CLI có chế độ interactive nhận từng lệnh và chế độ batch đọc SQL đã chuẩn bị; cả hai vẫn gửi công việc tới server. Prompt `mysql>` là của client CLI, không phải phần phải chép vào SQL. Các lệnh shell cài/chạy service chỉ được giảng để hiểu kiến trúc, không là bước nộp bài của học viên.',
 'Đây là probe bạn có thể chạy trong editor của đúng lượt. `SHOW DATABASES` trong nguồn liệt kê database theo quyền tài khoản; ở khóa này không yêu cầu tài khoản quản trị. Prompt `mysql>` là của client CLI, không phải phần phải chép vào SQL. Các lệnh shell cài/chạy service chỉ được giảng để hiểu kiến trúc, không là bước nộp bài của học viên.'),
('2. **P1.02:** Chọn Company làm default working database, rồi probe để biết connection đang ở database nào. Phân biệt nhãn connection, database, client/server và kết nối thành công với query đúng.',
 '2. **P1.02:** Chọn Company làm default working database, rồi probe để biết connection đang ở database nào.'),
('2. Dùng `USE Company; SELECT DATABASE();` trên namespace đã được cấp. Nhãn connection chỉ đặt tên cấu hình client; database là nơi chứa objects được chọn trong session; client gửi lệnh, server thực thi. Kết nối thành công chưa chứng minh mọi query đúng. Backend giữ cùng connection/session; pool không được tráo connection giữa hai bước rồi báo người học chọn sai database. Trong fixture nạp sẵn của bài query, backend đã chọn đúng database và chỉ cần probe.',
 '2. Dùng `USE Company; SELECT DATABASE();` trên namespace đã được cấp. Backend giữ cùng connection/session; pool không được tráo connection giữa hai bước rồi báo người học chọn sai database và chỉ cần probe.')]
# The answer at execution had the same closing sentences as the current answer;
# keep their exact original wording in the reconstructed byte candidate.
replacements[2]=(replacements[2][0],
 '2. Dùng `USE Company; SELECT DATABASE();` trên namespace đã được cấp. Backend giữ cùng connection/session; pool không được tráo connection giữa hai bước rồi báo người học chọn sai database. Trong fixture nạp sẵn của bài query, backend đã chọn đúng database và chỉ cần probe.')
old=current
for new,previous in replacements:
    assert old.count(new)==1,new[:60]
    old=old.replace(new,previous)
candidates=[old.encode('utf-8'),old.replace('\n','\r\n').encode('utf-8')]
matched=[b for b in candidates if sha(b)==native['lessons']['USTH10']]
assert len(matched)==1,'Reconstruction must match exact recorded MD hash, not just similar prose'
sql=lambda s:re.findall(r'```sql\n(.*?)```',s,re.S)
assert sql(current)==sql(old)
for name in ['USTH08','USTH09','USTH11']:
    assert sha((R/'lessons'/f'{name}.md').read_bytes())==native['lessons'][name]
out={'scope':'Native run remains qa/usth-final-sources-checks.json; no new native execution. Exact previous USTH10 bytes reconstructed from three prose-only changes and matched to its execution hash. Every SQL block unchanged; three other lesson hashes unchanged.',
 'nativeReportSha256':sha((R/'qa/usth-final-sources-checks.json').read_bytes()),
 'previousUSTH10Sha256':native['lessons']['USTH10'],'currentUSTH10Sha256':sha(p.read_bytes()),
 'unchangedSQLBlocks':len(sql(current)),'sqlPayloadSha256':sha('\n\n'.join(sql(current)).encode()),
 'currentLessonHashes':{name:sha((R/'lessons'/f'{name}.md').read_bytes()) for name in native['lessons']},
 'result':'pass'}
(R/'qa/usth-editorial-freshness.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'result':'pass','unchangedSQLBlocks':out['unchangedSQLBlocks']}))
