"""One-time insertion of already reviewed PE reference SQL into USTH10.
Does not infer semantic coverage or execute any SQL.
"""
from pathlib import Path
import re

R = Path(__file__).resolve().parents[1]
p = R/'lessons/USTH10.md'
text = p.read_text(encoding='utf-8')
assert text.count('<!--__NORTHWIND_ANSWERS__-->') == 1
sql = (R/'baseline/fixtures/northwind_answers.sql').read_text(encoding='utf-8-sig')
pattern = re.compile(r'^-- (P[23]\.\d\d(?:-15)?)[^\n]*\n',re.M)
marks = list(pattern.finditer(sql))
chunks = {m.group(1):sql[m.end():marks[i+1].start() if i+1<len(marks) else len(sql)].strip() for i,m in enumerate(marks)}
assert len(chunks) == 27
explanations = {
 'P2.01':'Product 3 (Old Notebook). Filter discontinued=1; không coi mọi product có giá thấp là ngừng bán.',
 'P2.02':'ID theo thứ tự là 5,7,3,4. Cùng giá được phá hòa bằng ID; policy này lấy đúng bốn rows.',
 'P2.03':'IDs 1,2,3,4; BETWEEN gồm cả 15 và 25.',
 'P2.04':'Ghép first_name, khoảng trắng và last_name; tên là hiển thị, ID là identity. Các phần tên NOT NULL trong fixture này.',
 'P2.05':'IDs 1 và 3 theo collation đã chọn; lời giải tìm first_name. Muốn full name hay case-sensitive phải chốt yêu cầu khác.',
 'P2.06':'Có 2 city đã biết khác nhau; COUNT DISTINCT bỏ NULL.',
 'P2.07':'Hanoi Lab, Hue Studio, PE School. DISTINCT bỏ bản lặp; ORDER BY mới hứa thứ tự.',
 'P2.08':'MIN=5, MAX=200.',
 'P2.09':'Có 6 product hiện hành.',
 'P2.10':'AVG=285/7, STDDEV_POP khoảng 65.379582. Dùng VAR_POP rồi căn hoặc công thức population để đối chiếu; số 200 làm mức phân tán tăng.',
 'P2.11':'Machine/200. AVG toàn Products khác AVG trong từng category.',
 'P2.12':'Bắt đầu transaction và giữ LAST_INSERT_ID trên cùng connection; không hard-code ID mà auto increment vừa cấp.',
 'P2.13':'Sản phẩm dùng @habeco_id, giá 22, category Beverages và discontinued=0; product_name được thêm làm tên hiển thị nhất quán.',
 'P2.14':'UPDATE theo product_code unique; không sửa mọi sản phẩm vì thiếu WHERE.',
 'P2.15':'DELETE supplier bị FK từ Products chặn (MySQL error 1451). Sau khi xem trạng thái, ROLLBACK toàn chuỗi thêm/sửa để các câu khác trở lại fixture ban đầu.',
 'P3.01':'IDs 31,32,34. Dấu > giữ đúng sau mốc, không gồm chính ngày 24.',
 'P3.02':'Hai line TEA và COF có value 540 và 500. Giá lịch sử/discount của line quyết định kết quả.',
 'P3.03':'Ba rows ở grain line của orders 31,32; order 34 chưa có line nên không xuất hiện trong report từng line.',
 'P3.04':'31→1040,32→1200,34→0. LEFT JOIN giữ order trống; COALESCE là policy hiển thị, SUM tập rỗng tự nó là NULL.',
 'P3.05':'Orders 31 và 32 qua biên subtotal>=800. WHERE lọc ngày; HAVING lọc group subtotal.',
 'P3.06':'Minh Tran/1200 rồi Anh Nguyen/1055. Đây là mọi đơn, không thêm filter ngày của câu trước. Group theo ID để không gộp hai người trùng tên.',
 'P3.07':'Beverages, Equipment, Stationery theo collation của sandbox.',
 'P3.08':'MIN=2, MAX=140, AVG=192.5/7=27.5; STD/VAR dùng population trên standard_cost. Kiểm numeric tolerance thay vì chuỗi số thực.',
 'P3.09':'Beverages=20, Equipment=200, Stationery=25/3. Không join lines làm product bán nhiều lần có trọng số lớn hơn.',
 'P3.10':'Hanoi MAX/AVG=10/10, Hue=20/20; các fee NULL không góp vào mẫu số.',
 'P3.11':'n=2 cho Equipment/200 và Beverages/20. Body là một statement, CALL ở statement riêng; n=NULL/0/âm bị SIGNAL. n lớn hơn số nhóm trả tất cả nhóm sẵn có.',
 'P3.12':'Giá trị nhỏ nhất trong AVG categories là 25/3. Derived table tạo query block đầu, MIN đọc các AVG ở block sau.',
 'P3.13':'PO80 có creator Anh Nguyen, approver Minh Tran; PO81 creator An Le, approver NULL. INNER JOIN approver sẽ làm mất PO81.',
 'P3.14':'Có 6 records của hai vai C/S. UNION ALL giữ record; full_name không là khóa để khử người trùng tên.',
 'P3.15':'Products 3 (Old Notebook) và 7 (Ruler). EXISTS/NOT EXISTS giữ đúng grain Product, không nhân khi có nhiều dòng mua.',
}
chunks['P2.12']="START TRANSACTION;\nINSERT INTO suppliers(company,last_name,first_name,city,country_region) VALUES('Habeco','Nguyễn','Hồng Linh','Hanoi','Vietnam');\nSET @habeco_id=LAST_INSERT_ID();"
chunks['P2.13']="INSERT INTO products(product_code,product_name,supplier_id,list_price,discontinued,category) VALUES('TBTruc Bach','Truc Bach',@habeco_id,22,0,'Beverages');"
chunks['P2.14']="UPDATE products SET standard_cost=18 WHERE product_code='TBTruc Bach';"
chunks['P2.15']="-- Run separately and observe expected FK error; do not stop before cleanup.\nDELETE FROM suppliers WHERE id=@habeco_id;\n-- Send ROLLBACK as the following statement even after the expected DELETE error.\nROLLBACK;"
proc = chunks['P3.11']
proc = proc[proc.index('CREATE PROCEDURE'):proc.index('END$$')+3]+';'
chunks['P3.11']=proc
parts=[]
for section in [2,3]:
    for n in range(1,16):
        source_id=f'P{section}.{n:02}'
        number=6+n if section==2 else 21+n
        body=chunks[source_id]
        parts += [f'{number}. **{source_id}:** {explanations[source_id]}','',f'```sql\n-- {source_id}\n{body}\n```','']
        if source_id=='P3.11':
            parts += ['```sql\nCALL top_categories(2);\n```','']
text=text.replace('<!--__NORTHWIND_ANSWERS__-->','\n'.join(parts))
fixture=(R/'baseline/fixtures/northwind_pe.sql').read_text(encoding='utf-8-sig')
fixture=fixture[fixture.index('CREATE TABLE employees'):]
text=text.replace('<!--__NORTHWIND_FIXTURE__-->','```sql\n'+fixture.strip()+'\n```')
p.write_text(text,encoding='utf-8')
print('Inserted 30 numbered answers, full Company solution and Northwind fixture remain in one standalone lesson')
