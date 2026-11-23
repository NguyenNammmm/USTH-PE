# Nhánh ERD và object database của Lecture 6–7

Đây là phần bổ sung cho web-runner-spec.md. Nội dung giảng nằm ở USTH06/07; backend của sản phẩm chưa được triển khai trong gói này. Bằng chứng hiện có là qa/usth-lecture67-checks.json: 41 ca kiểm, gồm mô hình hữu hạn, query SQLite chọn lọc và những ca ghi rõ MySQL 8.4.13. Không có lượt chạy SQL Server.

## ERD: chấm facts và constraint

Canvas lưu entity sets, attributes, roles, min/max, identifying relationship, subtype và key dưới dạng dữ liệu; tọa độ chỉ phục vụ hiển thị. Mỗi cardinality phải ghi convention để tránh đảo đầu “one”. Cung cấp bản nhập bằng bảng/form cho người không dùng chuột kéo thả.

Checker thử tuples do người học nhập và các counterexample được tạo theo brief. Permission ba ngôi không được tự đổi thành ba binary tables; nếu đổi, phải chứng minh constraint bổ sung ngăn tuples giả. Maker bắt buộc có featured device khác với Device bắt buộc được một Maker chọn. Parent total participation cần kiểm riêng ngoài FK. Các ca chấm gồm owner thiếu, duplicate partial key trong cùng owner, cùng partial key khác owner, unknown subtype field, joint owners và entity chưa có relationship.

Cho người học thấy một phản ví dụ nhỏ cùng constraint bị vi phạm. Khi schema có nhiều cách đúng, rubric kiểm identity, grain, cardinality, thông tin được giữ và đường cập nhật; không so DDL với một đáp án duy nhất. Phần lập luận tổng quát dùng reviewed-argument, không ghi “đã chứng minh” từ một số input hữu hạn.

## Registry và ranh giới dialect

Nhánh mặc định yêu cầu capability `mysql84.routine-row-trigger.innodb.v1`: engine/version thực tế, InnoDB, sql_mode, charset/collation, quyền CREATE VIEW/ROUTINE/TRIGGER trong database riêng, cùng connection cho CALL và OUT variables. Parser giữ nguyên một CREATE PROCEDURE/CREATE TRIGGER compound body; dấu chấm phẩy trong body không kết thúc request. DELIMITER là chỉ dẫn client, không gửi tới server.

Nhánh so sánh yêu cầu `sqlserver.statement-trigger.v1`, baseline đề xuất SQL Server 2022 với edition/quyền vận hành được dev xác nhận. Registry phải probe engine/version/edition thực tế trước khi available=true. Khi chưa có capability, chỉ cho tính mô hình tập inserted/deleted hoặc nộp lập luận; nhãn kết quả là computed-model/reviewed-argument. Không chuyển T-SQL sang MySQL trong im lặng. GO là batch separator của client, không phải statement T-SQL.

SQL Server fixture dưới là SQL biên soạn cho adapter và chưa được chạy native. Mỗi CREATE TRIGGER/PROCEDURE được gửi ở batch riêng. Không chạy cùng mọi trigger trong một fixture rồi làm chúng tác động chéo tới kết quả bài khác.

```sql
CREATE TABLE dbo.pe_product (
  id int NOT NULL PRIMARY KEY,
  price decimal(10,2) NULL,
  stock int NOT NULL CHECK(stock>=0)
);
CREATE TABLE dbo.pe_line (
  line_id int NOT NULL PRIMARY KEY,
  order_id int NOT NULL,
  product_id int NOT NULL REFERENCES dbo.pe_product(id),
  quantity int NOT NULL CHECK(quantity>0),
  unit_price decimal(10,2) NOT NULL
);
CREATE TABLE dbo.pe_customer (
  id int NOT NULL PRIMARY KEY,
  city nvarchar(255) NOT NULL
);
INSERT INTO dbo.pe_product VALUES(1,10,10),(2,20,20),(3,NULL,7);
INSERT INTO dbo.pe_customer VALUES(1,N'Hue'),(2,N'Hanoi'),(3,N'Hue');
```

```sql
CREATE OR ALTER PROCEDURE dbo.pe_find
  @city nvarchar(255)=N'Hue', @min_id int=0
AS
BEGIN
  SET NOCOUNT ON;
  SELECT id,city FROM dbo.pe_customer
  WHERE city=@city AND id>=@min_id ORDER BY id;
END;
```

Ba lời gọi pe_find trong USTH07 đều trả `(3,Hue)` trên fixture này. Procedure này trả result set; không gán kết quả SELECT thành một output parameter ngầm định.

## Ca nghiệm thu engine

| Ca | Thao tác và điều phải kiểm |
|---|---|
| Index | Tạo u7_price_ix, xác nhận metadata, ghi EXPLAIN và actual rows. Không bắt engine dùng index trên fixture ba row. Nhánh benchmark dùng dataset lớn được pin và so cả chi phí ghi. |
| View | u7_sales trả 501/70 và 502/10; view lồng trả 501/70; above-average trả 2/20. Thêm line vào base rồi đọc view trong transaction đã khai báo; kiểm thứ tự ở query ngoài. |
| CHECK OPTION | Insert Hue thành công; insert/update thành Danang qua view lỗi; ghi Danang trực tiếp vào bảng nền thành công nếu role được quyền. Kiểm base rows sau từng ca lỗi. |
| Routine | CREATE body như một statement; CALL Hue→2, Danang→0; đọc OUT trên cùng session. Reconnect không được âm thầm dùng lại @n từ connection khác. Kiểm result sets và output params riêng. |
| MySQL stock | Hai line cùng product 1, qty 3 và 4, stock 10→3; batch tổng 11 trên fixture mới lỗi, không để lại bất kỳ line hay thay đổi stock nào của batch. Kiểm cả BEFORE state và AFTER state. |
| SQL Server stock | Chạy grouped trigger của USTH07 trên pe_product/pe_line. Qty 3 và 4 phải trừ 7. Mutant bỏ SUM phải bị ca này bắt; ghi lỗi và rollback thực tế của phiên bản đã pin. |
| Audit | 10→12, NULL→12, 12→NULL tạo audit; 10→10 và NULL→NULL không tạo. Nhiều row phải ghi đủ; không ghép sai old/new khi key đổi. Fixture giữ ID ổn định. |
| Statement limit | SQL Server UPDATE tác động 0/1/2 row qua, 3 row bị chặn. UPDATE cùng giá trị vẫn tính affected row. Với mẫu ROLLBACK trong USTH07, cả transaction hiện tại bị rollback; thêm ca có một lệnh trước đó để thấy phạm vi này. |
| Referential integrity | FK chặn xóa parent còn con, cho parent không có con; batch nhiều parent lỗi không được xóa dở. Biến thể trigger chỉ phân tích EXISTS theo tập; không chứng nhận thay FK nếu chưa kiểm concurrency. |

Mỗi engine result lưu capability ID, exact engine version, fixture/code/checker hash, seed, isolation/autocommit, statement/batch boundaries, session ID và lỗi gốc có dữ liệu nhạy cảm được che. Lỗi quyền hay environment chưa sẵn sàng là lỗi hạ tầng, không chấm người học sai. Checker dùng snapshot độc lập, không tin chuỗi PASS do code người học tự in.

## Dạng bài và phản hồi

Cho xem một lần tìm key hoặc một batch cập nhật trước, rồi yêu cầu dự đoán. Với ERD, luân phiên min/max, gán roles, dựng tuple phản ví dụ và tự mapping. Với objects, dùng đọc plan, sửa dialect, điền predicate NULL, sửa lỗi multirow rồi viết body không có scaffold. Sau lỗi, hiện fixture và trạng thái liên quan cùng một câu giải thích cụ thể; lần thử sau đổi dữ liệu hoặc multiplicity nhưng giữ đúng kỹ năng đang kiểm.

Không cố dùng drag/drop cho mọi bài. Người học cần tự viết được query/body và giải thích ca lỗi sau giai đoạn nhận biết. Bài ôn có thể mở reminder đúng khái niệm; bài kiểm chuyển giao dùng brief/dữ liệu mới, không để đáp án mẫu xuất hiện trong editor.
