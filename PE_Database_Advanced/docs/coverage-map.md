# Bản đồ nguồn, bài nền và bài Advanced

Bản đồ này giữ cả địa chỉ sách và trang lecture/practice. Có 947 mục/tiểu mục sách, trong đó 746 mục lá; parent và child có thể cùng mô tả một nội dung. Việc có địa chỉ không chứng minh nội dung đã đạt độ sâu tự học. Trạng thái rà được lưu riêng; không tự cấp tín chỉ từ một phép tìm từ khóa.

Nguồn raw không được phát hành trong gói. `research/source-section-inventory.json` giữ đường dẫn đầu vào, source line, PDF page và hash. Những địa chỉ đó dùng đối chiếu tại workspace biên soạn; người học không cần các đường dẫn D: để mở khóa.

## Cách đọc quan hệ với 85 bài nền

Các bài mới là phần học sâu hơn. Khi nguồn nhắc lại nhập môn, người học mở đúng bài nền qua prerequisite; không phải làm lại cả85 bài. Snapshot nền giữ nguyên để truy vết. Một mục sách có thể vừa có kiến thức nền ở bài cũ vừa có thuật toán, phản ví dụ hoặc lab ở bài mới.

| Bài nền | Tên bài | Bài Advanced dùng làm điều kiện trước |
|---|---|---|
| F01 | Bắt đầu với dữ liệu và cách học khóa này | Tra cứu theo chủ đề; không bắt học lại |
| F02 | Đọc lệnh, bảng kết quả và chuẩn bị MySQL | Tra cứu theo chủ đề; không bắt học lại |
| M01 | Tập hợp, tuple và tích Descartes | Tra cứu theo chủ đề; không bắt học lại |
| M02 | Logic, lượng từ và UNKNOWN | AD02 |
| M03 | Quan hệ, hàm và ràng buộc dữ liệu | Tra cứu theo chủ đề; không bắt học lại |
| M04 | Chứng minh bằng phản ví dụ và suy diễn | AD03 |
| M05 | Đồ thị cho quan hệ và lịch giao dịch | AD22, AD38 |
| M06 | Đếm, logarit, xác suất và chi phí thuật toán | AD17, AD19, AD23, AD32, AD35, AD69, AD70, AD71, AD76 |
| C01 | Database, DBMS và các góc nhìn dữ liệu | Tra cứu theo chủ đề; không bắt học lại |
| C02 | Schema, instance, domain và keys | AD01, AD67 |
| C03 | Đại số quan hệ: chọn, chiếu và phép tập hợp | AD02 |
| C04 | Join, division và cây biểu thức | AD02 |
| S01 | Chạy MySQL và tái tạo bộ dữ liệu PE | Tra cứu theo chủ đề; không bắt học lại |
| S02 | Kiểu dữ liệu, CREATE và ALTER TABLE | Tra cứu theo chủ đề; không bắt học lại |
| S03 | PRIMARY KEY, FOREIGN KEY và CHECK | Tra cứu theo chủ đề; không bắt học lại |
| S04 | SELECT, WHERE và biểu thức | Tra cứu theo chủ đề; không bắt học lại |
| S05 | NULL, LIKE, chuỗi và ngày | AD01, AD67 |
| S06 | DISTINCT, ORDER BY, LIMIT và phép tập hợp | Tra cứu theo chủ đề; không bắt học lại |
| S07 | COUNT, SUM, GROUP BY và HAVING | AD01, AD67 |
| S08 | INNER JOIN và cardinality của kết quả | Tra cứu theo chủ đề; không bắt học lại |
| S09 | OUTER JOIN, self join và điều kiện ON | AD01, AD67 |
| S10 | Subquery, IN và truy vấn tương quan | Tra cứu theo chủ đề; không bắt học lại |
| S11 | EXISTS, NOT EXISTS và điều kiện mọi | AD01, AD67 |
| S12 | INSERT, UPDATE, DELETE và transaction đầu tiên | Tra cứu theo chủ đề; không bắt học lại |
| S13 | Views, schema và authorization | AD12, AD85 |
| S14 | Functions và stored procedures | AD12, AD85 |
| S15 | Triggers và tính nhất quán | AD12, AD85 |
| S16 | CTE đệ quy và truy vấn cây | AD10 |
| S17 | Window functions, ranking và ROLLUP | AD10 |
| S18 | Gọi SQL từ chương trình và parameter binding | AD11 |
| D01 | Từ yêu cầu nghiệp vụ đến ERD | Tra cứu theo chủ đề; không bắt học lại |
| D02 | Attributes, cardinality, keys và weak entity | Tra cứu theo chủ đề; không bắt học lại |
| D03 | Ánh xạ ERD, ternary và specialization | AD09 |
| D04 | Functional dependencies, closure và candidate keys | AD03 |
| D05 | 1NF, 2NF, 3NF và anomalies | Tra cứu theo chủ đề; không bắt học lại |
| D06 | BCNF, lossless join và dependency preservation | AD05 |
| D07 | Multivalued dependency, 4NF và 5NF | Tra cứu theo chủ đề; không bắt học lại |
| D08 | Quy trình thiết kế và dữ liệu thời gian | AD09 |
| D09 | SDLC, phỏng vấn, reports và kiểm thử thiết kế | AD09 |
| A01 | JSON, RDF và dữ liệu bán cấu trúc | AD13 |
| A02 | Object orientation và dữ liệu văn bản | AD14 |
| A03 | Spatial data và truy vấn không gian | AD15 |
| A04 | Web, dịch vụ và kiến trúc ứng dụng database | AD11 |
| A05 | SQL injection, quyền và mã hóa | AD12, AD85 |
| B01 | Big Data, storage và MapReduce | AD20, AD73 |
| B02 | Streaming data và graph databases | AD21, AD22 |
| B03 | Data warehouse, star schema và OLAP | AD18, AD72 |
| B04 | Data mining, đánh giá và diễn giải | AD19, AD70, AD71 |
| I01 | Thiết bị lưu trữ, RAID và truy cập block | AD23 |
| I02 | Files, records, catalog và buffer pool | AD24, AD25 |
| I03 | Column store và main-memory storage | AD26 |
| I04 | Index có thứ tự và B+ tree | AD27, AD74 |
| I05 | Hash, composite, bitmap và spatial indexes | AD15, AD29, AD30 |
| I06 | Bloom filter, LSM, extendible và linear hashing | AD31, AD75 |
| Q01 | Query processing, selection và mô hình chi phí | AD32, AD76 |
| Q02 | Sort, join, pipeline và xử lý trong RAM | AD33, AD34, AD77 |
| Q03 | Biến đổi biểu thức và ước lượng cardinality | AD35 |
| Q04 | Chọn plan, materialized view và EXPLAIN | AD37, AD78 |
| T01 | Transaction, ACID và mô hình lịch chạy | AD38 |
| T02 | Serializability và conflict graph | AD38 |
| T03 | Isolation levels và locking | AD39 |
| T04 | Deadlock, granularity, timestamp và validation | AD40, AD41, AD63 |
| T05 | MVCC, snapshot isolation và giới hạn nhất quán | AD42 |
| T06 | WAL, checkpoint và khôi phục sau lỗi | AD43 |
| T07 | Remote backup, ARIES và recovery trong RAM | AD44, AD45 |
| P01 | Centralized, parallel, distributed và cloud | AD20, AD46, AD73, AD79 |
| P02 | Partitioning, skew và replication | AD47, AD64 |
| P03 | Distributed files, indexes và key-value stores | Tra cứu theo chủ đề; không bắt học lại |
| P04 | Parallel sort, join và thực thi plan | AD48, AD80 |
| P05 | Parallel streaming và distributed queries | AD49 |
| P06 | Distributed transactions và two-phase commit | AD50 |
| P07 | Replication, consistency, leader và consensus | AD51, AD52, AD62, AD65, AD66 |
| P08 | Tuning, benchmarks, standards và directories | AD53 |
| P09 | Blockchain databases và smart contracts | AD54, AD81, AD82 |
| O01 | Tuple relational calculus và safety | Tra cứu theo chủ đề; không bắt học lại |
| O02 | Domain calculus và diễn đạt truy vấn logic | Tra cứu theo chủ đề; không bắt học lại |
| O03 | Thiết kế nâng cao: join dependency và DKNF | Tra cứu theo chủ đề; không bắt học lại |
| O04 | Object-based databases và persistence | AD14 |
| O05 | XML, XPath, XQuery và schema | AD16, AD68 |
| O06 | Information retrieval, ranking và inverted index | AD17, AD69 |
| O07 | PostgreSQL: đối chiếu một hệ quản trị khác | AD55 |
| Z01 | Project Company: dựng schema và bảo vệ ràng buộc | AD60 |
| Z02 | Lab Northwind PE: từ truy vấn cơ bản đến reports | AD60 |
| Z03 | Project PE: ứng dụng, phân tích và University schema | AD59 |
| Z04 | Capstone hệ thống: hiệu năng, lỗi và phân tán | Tra cứu theo chủ đề; không bắt học lại |

## Lecture và practice USTH

Địa chỉ dưới đây là ánh xạ chủ đề. Phần rà từng trang vẫn cần bằng chứng ngữ nghĩa và hoạt động tương ứng; không gán nhãn đủ chỉ vì lecture có trong bảng.

| Nguồn | Trang PDF | Chủ đề nền được khai báo | Phần Advanced đối chiếu |
|---|---|---|---|
| Lecture 1 DB Overview.pdf | 1–37 | C01, F01, F02, Z01 | AD67 |
| Lecture 2 Relational model.pdf | 1–71 | C02, C03, C04, M01, M02, M03, M04, Z01 | AD01, AD02, AD03 |
| Lecture 3 Simple SQL.pdf | 1–72 | F02, M02, S01, S02, S03, S04, S05, S06, S12, Z01, Z02 | AD01, AD10 |
| Lecture 4 More SQL.pdf | 1–47 | S06, S07, S08, S09, S10, S11, S17, Z02 | AD01, AD10 |
| Lecture 5 FD  NFs.pdf | 1–45 | D04, D05, D06, D07, M03, M04, Z01 | AD03, AD04, AD05, AD06, AD07, AD08 |
| Lecture 6 ERD.pdf | 1–64 | D01, D02, D03, M05, Z01 | AD09, AD59 |
| Lecture 7 View-SP-Ix.pdf | 1–43 | I04, S13, S14, S15, S16, S17, T01, Z02 | AD01, AD12, AD30, AD85 |
| Lecture 8 - ERD some use cases.pdf | 1–21 | D03, D09, Z03 | AD09, AD59, AD60 |
| Lecture 9 - Database Development Process.pdf | 1–48 | A04, A05, D01, D08, D09, S18, Z03 | AD09, AD11, AD12, AD18, AD19, AD59 |
| Practice 1.pdf | 1–5 | Z01 | AD59, AD60 |
| Practice 2.pdf | 1–1 | Z02 | AD60, AD85 |
| Practice 3.pdf | 1–4 | Z02 | AD60, AD85 |

Practice1 có trường EMPLOYEE.Minit. Fixture mới bổ sung nó bằng overlay, giữ sáu primary key và tám foreign key gốc, rồi có một FK mở rộng riêng của PE. Ví dụ Company/Northwind là dữ liệu PE dựng lại; không gọi là đáp án hoặc dump gốc USTH. Các kiểm engine tương ứng nằm trong `qa/apps-mysql-verification.json`.

## Địa chỉ từng mục sách

Trong HTML có thể lọc toàn bộ947 địa chỉ và mở bài liên quan. Bảng dưới dùng `sectionIds` chính xác thay cho chỉ đánh dấu một chương lớn. “Đã gán” vẫn là trạng thái cần rà; các lượt source-aware độc lập trong `qa/` chỉ chứng minh phạm vi excerpt được nêu trong từng báo cáo.

| Mục | Tên trong nguồn | Bài Advanced | Trang PDF nguồn | Trạng thái |
|---|---|---|---|
| 1.1 | Database-System Applications | AD67 | 30 | Đã gán; xem phạm vi rà nội dung |
| 1.2 | Purpose of Database Systems | AD67 | 34 | Đã gán; xem phạm vi rà nội dung |
| 1.3 | View of Data | AD67 | 37 | Đã gán; xem phạm vi rà nội dung |
| 1.3.1 | Data Models | AD67 | 37 | Đã gán; xem phạm vi rà nội dung |
| 1.3.2 | Relational Data Model | AD67 | 38 | Đã gán; xem phạm vi rà nội dung |
| 1.3.3 | Data Abstraction | AD67 | 38 | Đã gán; xem phạm vi rà nội dung |
| 1.3.4 | Instances and Schemas | AD67 | 41 | Đã gán; xem phạm vi rà nội dung |
| 1.4 | Database Languages | AD67 | 42 | Đã gán; xem phạm vi rà nội dung |
| 1.4.1 | Data-Definition Language | AD67 | 42 | Đã gán; xem phạm vi rà nội dung |
| 1.4.2 | The SQL Data-Definition Language | AD67 | 43 | Đã gán; xem phạm vi rà nội dung |
| 1.4.3 | Data-Manipulation Language | AD67 | 44 | Đã gán; xem phạm vi rà nội dung |
| 1.4.4 | The SQL Data-Manipulation Language | AD67 | 45 | Đã gán; xem phạm vi rà nội dung |
| 1.4.5 | Database Access from Application Programs | AD67 | 45 | Đã gán; xem phạm vi rà nội dung |
| 1.5 | Database Design | AD67 | 46 | Đã gán; xem phạm vi rà nội dung |
| 1.6 | Database Engine | AD67 | 47 | Đã gán; xem phạm vi rà nội dung |
| 1.6.1 | Storage Manager | AD67 | 48 | Đã gán; xem phạm vi rà nội dung |
| 1.6.2 | The Query Processor | AD67 | 49 | Đã gán; xem phạm vi rà nội dung |
| 1.6.3 | Transaction Management | AD67 | 49 | Đã gán; xem phạm vi rà nội dung |
| 1.7 | Database and Application Architecture | AD67 | 50 | Đã gán; xem phạm vi rà nội dung |
| 1.8 | Database Users and Administrators | AD67 | 53 | Đã gán; xem phạm vi rà nội dung |
| 1.8.1 | Database Users and User Interfaces | AD67 | 53 | Đã gán; xem phạm vi rà nội dung |
| 1.8.2 | Database Administrator | AD67 | 53 | Đã gán; xem phạm vi rà nội dung |
| 1.9 | History of Database Systems | AD67 | 54 | Đã gán; xem phạm vi rà nội dung |
| 2.1 | Structure of Relational Databases | AD01 | 66 | Đã gán; xem phạm vi rà nội dung |
| 2.2 | Database Schema | AD01 | 70 | Đã gán; xem phạm vi rà nội dung |
| 2.3 | Keys | AD01 | 72 | Đã gán; xem phạm vi rà nội dung |
| 2.4 | Schema Diagrams | AD01 | 75 | Đã gán; xem phạm vi rà nội dung |
| 2.5 | Relational Query Languages | AD01 | 76 | Đã gán; xem phạm vi rà nội dung |
| 2.6 | The Relational Algebra | AD01 | 77 | Đã gán; xem phạm vi rà nội dung |
| 2.6.1 | The Select Operation | AD01 | 78 | Đã gán; xem phạm vi rà nội dung |
| 2.6.2 | The Project Operation | AD01 | 78 | Đã gán; xem phạm vi rà nội dung |
| 2.6.3 | Composition of Relational Operations | AD01 | 79 | Đã gán; xem phạm vi rà nội dung |
| 2.6.4 | The Cartesian-Product Operation | AD01 | 79 | Đã gán; xem phạm vi rà nội dung |
| 2.6.5 | The Join Operation | AD01 | 81 | Đã gán; xem phạm vi rà nội dung |
| 2.6.6 | Set Operations | AD01 | 82 | Đã gán; xem phạm vi rà nội dung |
| 2.6.7 | The Assignment Operation | AD01 | 84 | Đã gán; xem phạm vi rà nội dung |
| 2.6.8 | The Rename Operation | AD01 | 85 | Đã gán; xem phạm vi rà nội dung |
| 2.6.9 | Equivalent Queries | AD01 | 87 | Đã gán; xem phạm vi rà nội dung |
| 3.1 | Overview of the SQL Query Language | AD01 | 94 | Đã gán; xem phạm vi rà nội dung |
| 3.2 | SQL Data Definition | AD01 | 95 | Đã gán; xem phạm vi rà nội dung |
| 3.2.1 | Basic Types | AD01 | 96 | Đã gán; xem phạm vi rà nội dung |
| 3.2.2 | Basic Schema Definition | AD01 | 97 | Đã gán; xem phạm vi rà nội dung |
| 3.3 | Basic Structure of SQL Queries | AD01 | 100 | Đã gán; xem phạm vi rà nội dung |
| 3.3.1 | Queries on a Single Relation | AD01 | 100 | Đã gán; xem phạm vi rà nội dung |
| 3.3.2 | Queries on Multiple Relations | AD01 | 103 | Đã gán; xem phạm vi rà nội dung |
| 3.4 | Additional Basic Operations | AD01 | 108 | Đã gán; xem phạm vi rà nội dung |
| 3.4.1 | The Rename Operation | AD01 | 108 | Đã gán; xem phạm vi rà nội dung |
| 3.4.2 | String Operations | AD01 | 111 | Đã gán; xem phạm vi rà nội dung |
| 3.4.3 | Attribute Specification in the Select Clause | AD01 | 112 | Đã gán; xem phạm vi rà nội dung |
| 3.4.4 | Ordering the Display of Tuples | AD01 | 112 | Đã gán; xem phạm vi rà nội dung |
| 3.4.5 | Where-Clause Predicates | AD01 | 113 | Đã gán; xem phạm vi rà nội dung |
| 3.5 | Set Operations | AD01 | 114 | Đã gán; xem phạm vi rà nội dung |
| 3.5.1 | The Union Operation | AD01 | 115 | Đã gán; xem phạm vi rà nội dung |
| 3.5.2 | The Intersect Operation | AD01 | 116 | Đã gán; xem phạm vi rà nội dung |
| 3.5.3 | The Except Operation | AD01 | 117 | Đã gán; xem phạm vi rà nội dung |
| 3.6 | Null Values | AD01 | 118 | Đã gán; xem phạm vi rà nội dung |
| 3.7 | Aggregate Functions | AD10 | 120 | Đã gán; xem phạm vi rà nội dung |
| 3.7.1 | Basic Aggregation | AD10 | 120 | Đã gán; xem phạm vi rà nội dung |
| 3.7.2 | Aggregation with Grouping | AD10 | 121 | Đã gán; xem phạm vi rà nội dung |
| 3.7.3 | The Having Clause | AD10 | 124 | Đã gán; xem phạm vi rà nội dung |
| 3.7.4 | Aggregation with Null and Boolean Values | AD10 | 125 | Đã gán; xem phạm vi rà nội dung |
| 3.8 | Nested Subqueries | AD10 | 127 | Đã gán; xem phạm vi rà nội dung |
| 3.8.1 | Set Membership | AD10 | 127 | Đã gán; xem phạm vi rà nội dung |
| 3.8.2 | Set Comparison | AD10 | 128 | Đã gán; xem phạm vi rà nội dung |
| 3.8.3 | Test for Empty Relations | AD10 | 130 | Đã gán; xem phạm vi rà nội dung |
| 3.8.4 | Test for the Absence of Duplicate Tuples | AD10 | 132 | Đã gán; xem phạm vi rà nội dung |
| 3.8.5 | Subqueries in the From Clause | AD10 | 133 | Đã gán; xem phạm vi rà nội dung |
| 3.8.6 | The With Clause | AD10 | 134 | Đã gán; xem phạm vi rà nội dung |
| 3.8.7 | Scalar Subqueries | AD10 | 135 | Đã gán; xem phạm vi rà nội dung |
| 3.8.8 | Scalar Without a From Clause | AD10 | 136 | Đã gán; xem phạm vi rà nội dung |
| 3.9 | Modification of the Database | AD01 | 137 | Đã gán; xem phạm vi rà nội dung |
| 3.9.1 | Deletion | AD01 | 137 | Đã gán; xem phạm vi rà nội dung |
| 3.9.2 | Insertion | AD01 | 139 | Đã gán; xem phạm vi rà nội dung |
| 3.9.3 | Updates | AD01 | 140 | Đã gán; xem phạm vi rà nội dung |
| 4.1 | Join Expressions | AD01 | 154 | Đã gán; xem phạm vi rà nội dung |
| 4.1.1 | The Natural Join | AD01 | 155 | Đã gán; xem phạm vi rà nội dung |
| 4.1.2 | Join Conditions | AD01 | 159 | Đã gán; xem phạm vi rà nội dung |
| 4.1.3 | Outer Joins | AD01 | 160 | Đã gán; xem phạm vi rà nội dung |
| 4.1.4 | Join Types and Conditions | AD01 | 165 | Đã gán; xem phạm vi rà nội dung |
| 4.2 | Views | AD01 | 166 | Đã gán; xem phạm vi rà nội dung |
| 4.2.1 | View Definition | AD01 | 167 | Đã gán; xem phạm vi rà nội dung |
| 4.2.2 | Using Views in SQL Queries | AD01 | 167 | Đã gán; xem phạm vi rà nội dung |
| 4.2.3 | Materialized Views | AD01 | 169 | Đã gán; xem phạm vi rà nội dung |
| 4.2.4 | Update of a View | AD01 | 169 | Đã gán; xem phạm vi rà nội dung |
| 4.3 | Transactions | AD01 | 172 | Đã gán; xem phạm vi rà nội dung |
| 4.4 | Integrity Constraints | AD12 | 174 | Đã gán; xem phạm vi rà nội dung |
| 4.4.1 | Constraints on a Single Relation | AD12 | 175 | Đã gán; xem phạm vi rà nội dung |
| 4.4.2 | Not Null Constraint | AD12 | 175 | Đã gán; xem phạm vi rà nội dung |
| 4.4.3 | Unique Constraint | AD12 | 176 | Đã gán; xem phạm vi rà nội dung |
| 4.4.4 | The Check Clause | AD12 | 176 | Đã gán; xem phạm vi rà nội dung |
| 4.4.5 | Referential Integrity | AD12 | 178 | Đã gán; xem phạm vi rà nội dung |
| 4.4.6 | Assigning Names to Constraints | AD12 | 180 | Đã gán; xem phạm vi rà nội dung |
| 4.4.7 | Integrity Constraint Violation During a Transaction | AD12 | 180 | Đã gán; xem phạm vi rà nội dung |
| 4.4.8 | Complex Check Conditions and Assertions | AD12 | 181 | Đã gán; xem phạm vi rà nội dung |
| 4.5 | SQL Data Types and Schemas | AD12 | 182 | Đã gán; xem phạm vi rà nội dung |
| 4.5.1 | Date and Time Types in SQL | AD12 | 183 | Đã gán; xem phạm vi rà nội dung |
| 4.5.2 | Type Conversion and Formatting Functions | AD12 | 184 | Đã gán; xem phạm vi rà nội dung |
| 4.5.3 | Default Values | AD12 | 185 | Đã gán; xem phạm vi rà nội dung |
| 4.5.4 | Large-Object Types | AD12 | 185 | Đã gán; xem phạm vi rà nội dung |
| 4.5.5 | User-Defined Types | AD12 | 187 | Đã gán; xem phạm vi rà nội dung |
| 4.5.6 | Generating Unique Key Values | AD12 | 189 | Đã gán; xem phạm vi rà nội dung |
| 4.5.7 | Create Table Extensions | AD12 | 191 | Đã gán; xem phạm vi rà nội dung |
| 4.5.8 | Schemas, Catalogs, and Environments | AD12 | 191 | Đã gán; xem phạm vi rà nội dung |
| 4.6 | Index Definition in SQL | AD01 | 193 | Đã gán; xem phạm vi rà nội dung |
| 4.7 | Authorization | AD12 | 194 | Đã gán; xem phạm vi rà nội dung |
| 4.7.1 | Granting and Revoking of Privileges | AD12 | 195 | Đã gán; xem phạm vi rà nội dung |
| 4.7.2 | Roles | AD12 | 196 | Đã gán; xem phạm vi rà nội dung |
| 4.7.3 | Authorization on Views | AD12 | 198 | Đã gán; xem phạm vi rà nội dung |
| 4.7.4 | Authorizations on Schema | AD12 | 199 | Đã gán; xem phạm vi rà nội dung |
| 4.7.5 | Transfer of Privileges | AD12 | 199 | Đã gán; xem phạm vi rà nội dung |
| 4.7.6 | Revoking of Privileges | AD12 | 200 | Đã gán; xem phạm vi rà nội dung |
| 4.7.7 | Row-Level Authorization | AD12 | 202 | Đã gán; xem phạm vi rà nội dung |
| 5.1 | Accessing SQL from a Programming Language | AD11 | 212 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1 | JDBC | AD11 | 213 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.1 | Connecting to the Database | AD11 | 214 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.2 | Shipping SQL Statements to the Database System | AD11 | 215 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.3 | Exceptions and Resource Management | AD11 | 216 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.4 | Retrieving the Result of a Query | AD11 | 216 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.5 | Prepared Statements | AD11 | 217 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.6 | Callable Statements | AD11 | 219 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.7 | Metadata Features | AD11 | 220 | Đã gán; xem phạm vi rà nội dung |
| 5.1.1.8 | Other Features | AD11 | 222 | Đã gán; xem phạm vi rà nội dung |
| 5.1.2 | Database Access from Python | AD11 | 222 | Đã gán; xem phạm vi rà nội dung |
| 5.1.3 | ODBC | AD11 | 223 | Đã gán; xem phạm vi rà nội dung |
| 5.1.4 | Embedded SQL | AD11 | 226 | Đã gán; xem phạm vi rà nội dung |
| 5.2 | Functions and Procedures | AD85 | 227 | Đã gán; xem phạm vi rà nội dung |
| 5.2.1 | Declaring and Invoking SQL Functions and Procedures | AD85 | 228 | Đã gán; xem phạm vi rà nội dung |
| 5.2.2 | Language Constructs for Procedures and Functions | AD85 | 230 | Đã gán; xem phạm vi rà nội dung |
| 5.2.3 | External Language Routines | AD85 | 232 | Đã gán; xem phạm vi rà nội dung |
| 5.3 | Triggers | AD85 | 235 | Đã gán; xem phạm vi rà nội dung |
| 5.3.1 | Need for Triggers | AD85 | 235 | Đã gán; xem phạm vi rà nội dung |
| 5.3.2 | Triggers in SQL | AD85 | 236 | Đã gán; xem phạm vi rà nội dung |
| 5.3.3 | When Not to Use Triggers | AD85 | 239 | Đã gán; xem phạm vi rà nội dung |
| 5.4 | Recursive Queries | AD10 | 242 | Đã gán; xem phạm vi rà nội dung |
| 5.4.1 | Transitive Closure Using Iteration | AD10 | 243 | Đã gán; xem phạm vi rà nội dung |
| 5.4.2 | Recursion in SQL | AD10 | 245 | Đã gán; xem phạm vi rà nội dung |
| 5.5 | Advanced Aggregation Features | AD10 | 248 | Đã gán; xem phạm vi rà nội dung |
| 5.5.1 | Ranking | AD10 | 248 | Đã gán; xem phạm vi rà nội dung |
| 5.5.2 | Windowing | AD10 | 252 | Đã gán; xem phạm vi rà nội dung |
| 5.5.3 | Pivoting | AD10 | 255 | Đã gán; xem phạm vi rà nội dung |
| 5.5.4 | Rollup and Cube | AD10 | 256 | Đã gán; xem phạm vi rà nội dung |
| 6.1 | Overview of the Design Process | AD09 | 270 | Đã gán; xem phạm vi rà nội dung |
| 6.1.1 | Design Phases | AD09 | 270 | Đã gán; xem phạm vi rà nội dung |
| 6.1.2 | Design Alternatives | AD09 | 272 | Đã gán; xem phạm vi rà nội dung |
| 6.2 | The Entity-Relationship Model | AD09 | 273 | Đã gán; xem phạm vi rà nội dung |
| 6.2.1 | Entity Sets | AD09 | 273 | Đã gán; xem phạm vi rà nội dung |
| 6.2.2 | Relationship Sets | AD09 | 275 | Đã gán; xem phạm vi rà nội dung |
| 6.3 | Complex Attributes | AD09 | 278 | Đã gán; xem phạm vi rà nội dung |
| 6.4 | Mapping Cardinalities | AD09 | 281 | Đã gán; xem phạm vi rà nội dung |
| 6.5 | Primary Key | AD09 | 285 | Đã gán; xem phạm vi rà nội dung |
| 6.5.1 | Entity Sets | AD09 | 286 | Đã gán; xem phạm vi rà nội dung |
| 6.5.2 | Relationship Sets | AD09 | 286 | Đã gán; xem phạm vi rà nội dung |
| 6.5.3 | Weak Entity Sets | AD09 | 288 | Đã gán; xem phạm vi rà nội dung |
| 6.6 | Removing Redundant Attributes in Entity Sets | AD09 | 290 | Đã gán; xem phạm vi rà nội dung |
| 6.7 | Reducing E-R Diagrams to Relational Schemas | AD09 | 293 | Đã gán; xem phạm vi rà nội dung |
| 6.7.1 | Representation of Strong Entity Sets | AD09 | 294 | Đã gán; xem phạm vi rà nội dung |
| 6.7.2 | Representation of Strong Entity Sets with Complex Attributes | AD09 | 294 | Đã gán; xem phạm vi rà nội dung |
| 6.7.3 | Representation of Weak Entity Sets | AD09 | 296 | Đã gán; xem phạm vi rà nội dung |
| 6.7.4 | Representation of Relationship Sets | AD09 | 297 | Đã gán; xem phạm vi rà nội dung |
| 6.7.5 | Redundancy of Schemas | AD09 | 298 | Đã gán; xem phạm vi rà nội dung |
| 6.7.6 | Combination of Schemas | AD09 | 299 | Đã gán; xem phạm vi rà nội dung |
| 6.8 | Extended E-R Features | AD09 | 300 | Đã gán; xem phạm vi rà nội dung |
| 6.8.1 | Specialization | AD09 | 300 | Đã gán; xem phạm vi rà nội dung |
| 6.8.2 | Generalization | AD09 | 302 | Đã gán; xem phạm vi rà nội dung |
| 6.8.3 | Attribute Inheritance | AD09 | 303 | Đã gán; xem phạm vi rà nội dung |
| 6.8.4 | Constraints on Specializations | AD09 | 304 | Đã gán; xem phạm vi rà nội dung |
| 6.8.5 | Aggregation | AD09 | 305 | Đã gán; xem phạm vi rà nội dung |
| 6.8.6 | Reduction to Relation Schemas | AD09 | 306 | Đã gán; xem phạm vi rà nội dung |
| 6.8.6.1 | Representation of Generalization | AD09 | 307 | Đã gán; xem phạm vi rà nội dung |
| 6.8.6.2 | Representation of Aggregation | AD09 | 308 | Đã gán; xem phạm vi rà nội dung |
| 6.9 | Entity-Relationship Design Issues | AD09 | 308 | Đã gán; xem phạm vi rà nội dung |
| 6.9.1 | Common Mistakes in E-R Diagrams | AD09 | 309 | Đã gán; xem phạm vi rà nội dung |
| 6.9.2 | Use of Entity Sets versus Attributes | AD09 | 310 | Đã gán; xem phạm vi rà nội dung |
| 6.9.3 | Use of Entity Sets versus Relationship Sets | AD09 | 311 | Đã gán; xem phạm vi rà nội dung |
| 6.9.4 | Binary versus n-ary Relationship Sets | AD09 | 312 | Đã gán; xem phạm vi rà nội dung |
| 6.10 | Alternative Notations for Modeling Data | AD09 | 314 | Đã gán; xem phạm vi rà nội dung |
| 6.10.1 | Alternative E-R Notations | AD09 | 314 | Đã gán; xem phạm vi rà nội dung |
| 6.10.2 | The Unified Modeling Language UML | AD09 | 317 | Đã gán; xem phạm vi rà nội dung |
| 6.11 | Other Aspects of Database Design | AD09 | 320 | Đã gán; xem phạm vi rà nội dung |
| 6.11.1 | Functional Requirements | AD09 | 320 | Đã gán; xem phạm vi rà nội dung |
| 6.11.2 | Data Flow, Workflow | AD09 | 320 | Đã gán; xem phạm vi rà nội dung |
| 6.11.3 | Schema Evolution | AD09 | 321 | Đã gán; xem phạm vi rà nội dung |
| 7.1 | Features of Good Relational Designs | AD05 | 332 | Đã gán; xem phạm vi rà nội dung |
| 7.1.1 | Decomposition | AD05 | 334 | Đã gán; xem phạm vi rà nội dung |
| 7.1.2 | Lossless Decomposition | AD05 | 336 | Đã gán; xem phạm vi rà nội dung |
| 7.1.3 | Normalization Theory | AD05 | 337 | Đã gán; xem phạm vi rà nội dung |
| 7.2 | Decomposition Using Functional Dependencies | AD05 | 337 | Đã gán; xem phạm vi rà nội dung |
| 7.2.1 | Notational Conventions | AD05 | 338 | Đã gán; xem phạm vi rà nội dung |
| 7.2.2 | Keys and Functional Dependencies | AD05 | 338 | Đã gán; xem phạm vi rà nội dung |
| 7.2.3 | Lossless Decomposition and Functional Dependencies | AD05 | 341 | Đã gán; xem phạm vi rà nội dung |
| 7.3 | Normal Forms | AD05 | 342 | Đã gán; xem phạm vi rà nội dung |
| 7.3.1 | Boyce – Codd Normal Form | AD05 | 342 | Đã gán; xem phạm vi rà nội dung |
| 7.3.1.1 | Definition | AD05 | 342 | Đã gán; xem phạm vi rà nội dung |
| 7.3.1.2 | BCNF and Dependency Preservation | AD05 | 344 | Đã gán; xem phạm vi rà nội dung |
| 7.3.2 | Third Normal Form | AD05 | 346 | Đã gán; xem phạm vi rà nội dung |
| 7.3.3 | Comparison of BCNF and 3NF | AD05 | 347 | Đã gán; xem phạm vi rà nội dung |
| 7.3.4 | Higher Normal Forms | AD05 | 348 | Đã gán; xem phạm vi rà nội dung |
| 7.4 | Functional-Dependency Theory | AD03 | 349 | Đã gán; xem phạm vi rà nội dung |
| 7.4.1 | Closure of a Set of Functional Dependencies | AD03 | 349 | Đã gán; xem phạm vi rà nội dung |
| 7.4.2 | Closure of Attribute Sets | AD03 | 351 | Đã gán; xem phạm vi rà nội dung |
| 7.4.3 | Canonical Cover | AD04 | 353 | Đã gán; xem phạm vi rà nội dung |
| 7.4.4 | Dependency Preservation | AD04 | 357 | Đã gán; xem phạm vi rà nội dung |
| 7.5 | Algorithms for Decomposition Using Functional Dependencies | AD05 | 359 | Đã gán; xem phạm vi rà nội dung |
| 7.5.1 | BCNF Decomposition | AD05 | 359 | Đã gán; xem phạm vi rà nội dung |
| 7.5.1.1 | Testing for BCNF | AD05 | 359 | Đã gán; xem phạm vi rà nội dung |
| 7.5.1.2 | BCNF Decomposition Algorithm | AD05 | 360 | Đã gán; xem phạm vi rà nội dung |
| 7.5.2 | 3NF Decomposition | AD06 | 362 | Đã gán; xem phạm vi rà nội dung |
| 7.5.3 | Correctness of the 3NF Algorithm | AD06 | 363 | Đã gán; xem phạm vi rà nội dung |
| 7.6 | Decomposition Using Multivalued Dependencies | AD07 | 365 | Đã gán; xem phạm vi rà nội dung |
| 7.6.1 | Multivalued Dependencies | AD07 | 366 | Đã gán; xem phạm vi rà nội dung |
| 7.6.2 | Fourth Normal Form | AD07 | 368 | Đã gán; xem phạm vi rà nội dung |
| 7.6.3 | 4NF Decomposition | AD07 | 369 | Đã gán; xem phạm vi rà nội dung |
| 7.7 | More Normal Forms | AD08 | 370 | Đã gán; xem phạm vi rà nội dung |
| 7.8 | Atomic Domains and First Normal Form | AD09 | 371 | Đã gán; xem phạm vi rà nội dung |
| 7.9 | Database-Design Process | AD09 | 372 | Đã gán; xem phạm vi rà nội dung |
| 7.9.1 | E-R Model and Normalization | AD09 | 373 | Đã gán; xem phạm vi rà nội dung |
| 7.9.2 | Naming of Attributes and Relationships | AD09 | 374 | Đã gán; xem phạm vi rà nội dung |
| 7.9.3 | Denormalization for Performance | AD09 | 375 | Đã gán; xem phạm vi rà nội dung |
| 7.9.4 | Other Design Issues | AD09 | 375 | Đã gán; xem phạm vi rà nội dung |
| 7.10 | Modeling Temporal Data | AD09 | 376 | Đã gán; xem phạm vi rà nội dung |
| 8.1 | Semi-structured Data | AD13 | 394 | Đã gán; xem phạm vi rà nội dung |
| 8.1.1 | Overview of Semi-structured Data Models | AD13 | 395 | Đã gán; xem phạm vi rà nội dung |
| 8.1.1.1 | Flexible Schema | AD13 | 395 | Đã gán; xem phạm vi rà nội dung |
| 8.1.1.2 | Multivalued Data Types | AD13 | 395 | Đã gán; xem phạm vi rà nội dung |
| 8.1.1.3 | Nested Data Types | AD13 | 396 | Đã gán; xem phạm vi rà nội dung |
| 8.1.1.4 | Knowledge Representation | AD13 | 397 | Đã gán; xem phạm vi rà nội dung |
| 8.1.2 | JSON | AD13 | 397 | Đã gán; xem phạm vi rà nội dung |
| 8.1.3 | XML | AD13 | 399 | Đã gán; xem phạm vi rà nội dung |
| 8.1.4 | RDF and Knowledge Graphs | AD13 | 401 | Đã gán; xem phạm vi rà nội dung |
| 8.1.4.1 | Triple Representation | AD13 | 401 | Đã gán; xem phạm vi rà nội dung |
| 8.1.4.2 | Graph Representation of RDF | AD13 | 403 | Đã gán; xem phạm vi rà nội dung |
| 8.1.4.3 | SPARQL | AD13 | 404 | Đã gán; xem phạm vi rà nội dung |
| 8.1.4.4 | Representing N-ary Relationships | AD13 | 405 | Đã gán; xem phạm vi rà nội dung |
| 8.2 | Object Orientation | AD14 | 405 | Đã gán; xem phạm vi rà nội dung |
| 8.2.1 | Object-Relational Database Systems | AD14 | 406 | Đã gán; xem phạm vi rà nội dung |
| 8.2.1.1 | User-Defined Types | AD14 | 407 | Đã gán; xem phạm vi rà nội dung |
| 8.2.1.2 | Type Inheritance | AD14 | 407 | Đã gán; xem phạm vi rà nội dung |
| 8.2.1.3 | Table Inheritance | AD14 | 408 | Đã gán; xem phạm vi rà nội dung |
| 8.2.1.4 | Reference Types in SQL | AD14 | 409 | Đã gán; xem phạm vi rà nội dung |
| 8.2.2 | Object-Relational Mapping | AD14 | 410 | Đã gán; xem phạm vi rà nội dung |
| 8.3 | Textual Data | AD17, AD69 | 411 | Đã gán; xem phạm vi rà nội dung |
| 8.3.1 | Keyword Queries | AD17, AD69 | 412 | Đã gán; xem phạm vi rà nội dung |
| 8.3.2 | Relevance Ranking | AD17, AD69 | 412 | Đã gán; xem phạm vi rà nội dung |
| 8.3.2.1 | Ranking Using TF-IDF | AD17, AD69 | 413 | Đã gán; xem phạm vi rà nội dung |
| 8.3.2.2 | Ranking Using Hyperlinks | AD17, AD69 | 414 | Đã gán; xem phạm vi rà nội dung |
| 8.3.3 | Measuring Retrieval Effectiveness | AD17, AD69 | 415 | Đã gán; xem phạm vi rà nội dung |
| 8.3.4 | Keyword Querying on Structured Data and Knowledge Graphs | AD17, AD69 | 415 | Đã gán; xem phạm vi rà nội dung |
| 8.4 | Spatial Data | AD15 | 416 | Đã gán; xem phạm vi rà nội dung |
| 8.4.1 | Representation of Geometric Information | AD15 | 417 | Đã gán; xem phạm vi rà nội dung |
| 8.4.2 | Design Databases | AD15 | 419 | Đã gán; xem phạm vi rà nội dung |
| 8.4.3 | Geographic Data | AD15 | 420 | Đã gán; xem phạm vi rà nội dung |
| 8.4.3.1 | Applications of Geographic Data | AD15 | 420 | Đã gán; xem phạm vi rà nội dung |
| 8.4.3.2 | Representation of Geographic Data | AD15 | 421 | Đã gán; xem phạm vi rà nội dung |
| 8.4.4 | Spatial Queries | AD15 | 422 | Đã gán; xem phạm vi rà nội dung |
| 9.1 | Application Programs and User Interfaces | AD11 | 432 | Đã gán; xem phạm vi rà nội dung |
| 9.2 | Web Fundamentals | AD11 | 434 | Đã gán; xem phạm vi rà nội dung |
| 9.2.1 | Uniform Resource Locators | AD11 | 434 | Đã gán; xem phạm vi rà nội dung |
| 9.2.2 | HyperText Markup Language | AD11 | 435 | Đã gán; xem phạm vi rà nội dung |
| 9.2.3 | Web Servers and Sessions | AD11 | 437 | Đã gán; xem phạm vi rà nội dung |
| 9.3 | Servlets | AD11 | 440 | Đã gán; xem phạm vi rà nội dung |
| 9.3.1 | A Servlet Example | AD11 | 440 | Đã gán; xem phạm vi rà nội dung |
| 9.3.2 | Servlet Sessions | AD11 | 442 | Đã gán; xem phạm vi rà nội dung |
| 9.3.3 | Servlet Life Cycle | AD11 | 444 | Đã gán; xem phạm vi rà nội dung |
| 9.3.4 | Application Servers | AD11 | 445 | Đã gán; xem phạm vi rà nội dung |
| 9.4 | Alternative Server-Side Frameworks | AD11 | 445 | Đã gán; xem phạm vi rà nội dung |
| 9.4.1 | Server-Side Scripting | AD11 | 445 | Đã gán; xem phạm vi rà nội dung |
| 9.4.1.1 | Java Server Pages | AD11 | 446 | Đã gán; xem phạm vi rà nội dung |
| 9.4.1.2 | PHP | AD11 | 447 | Đã gán; xem phạm vi rà nội dung |
| 9.4.2 | Web Application Frameworks | AD11 | 447 | Đã gán; xem phạm vi rà nội dung |
| 9.4.3 | The Django Framework | AD11 | 448 | Đã gán; xem phạm vi rà nội dung |
| 9.5 | Client-Side Code and Web Services | AD11 | 450 | Đã gán; xem phạm vi rà nội dung |
| 9.5.1 | JavaScript | AD11 | 450 | Đã gán; xem phạm vi rà nội dung |
| 9.5.1.1 | Input Validation | AD11 | 451 | Đã gán; xem phạm vi rà nội dung |
| 9.5.1.2 | Responsive User Interfaces | AD11 | 452 | Đã gán; xem phạm vi rà nội dung |
| 9.5.1.3 | Interfacing with Web Services | AD11 | 452 | Đã gán; xem phạm vi rà nội dung |
| 9.5.2 | Web Services | AD11 | 455 | Đã gán; xem phạm vi rà nội dung |
| 9.5.3 | Disconnected Operation | AD11 | 456 | Đã gán; xem phạm vi rà nội dung |
| 9.5.4 | Mobile Application Platforms | AD11 | 457 | Đã gán; xem phạm vi rà nội dung |
| 9.6 | Application Architectures | AD11 | 458 | Đã gán; xem phạm vi rà nội dung |
| 9.6.1 | The Business-Logic Layer | AD11 | 460 | Đã gán; xem phạm vi rà nội dung |
| 9.6.2 | The Data-Access Layer and Object-Relational Mapping | AD11 | 460 | Đã gán; xem phạm vi rà nội dung |
| 9.6.2.1 | Hibernate ORM | AD11 | 460 | Đã gán; xem phạm vi rà nội dung |
| 9.6.2.2 | The Django ORM | AD11 | 462 | Đã gán; xem phạm vi rà nội dung |
| 9.7 | Application Performance | AD11 | 463 | Đã gán; xem phạm vi rà nội dung |
| 9.7.1 | Reducing Overhead by Caching | AD11 | 464 | Đã gán; xem phạm vi rà nội dung |
| 9.7.2 | Parallel Processing | AD11 | 466 | Đã gán; xem phạm vi rà nội dung |
| 9.8 | Application Security | AD12 | 466 | Đã gán; xem phạm vi rà nội dung |
| 9.8.1 | SQL Injection | AD12 | 467 | Đã gán; xem phạm vi rà nội dung |
| 9.8.2 | Cross-Site Scripting and Request Forgery | AD12 | 468 | Đã gán; xem phạm vi rà nội dung |
| 9.8.3 | Password Leakage | AD12 | 469 | Đã gán; xem phạm vi rà nội dung |
| 9.8.4 | Application-Level Authentication | AD12 | 470 | Đã gán; xem phạm vi rà nội dung |
| 9.8.5 | Application-Level Authorization | AD12 | 472 | Đã gán; xem phạm vi rà nội dung |
| 9.8.6 | Audit Trails | AD12 | 474 | Đã gán; xem phạm vi rà nội dung |
| 9.8.7 | Privacy | AD12 | 475 | Đã gán; xem phạm vi rà nội dung |
| 9.9 | Encryption and Its Applications | AD12 | 476 | Đã gán; xem phạm vi rà nội dung |
| 9.9.1 | Encryption Techniques | AD12 | 476 | Đã gán; xem phạm vi rà nội dung |
| 9.9.2 | Encryption Support in Databases | AD12 | 478 | Đã gán; xem phạm vi rà nội dung |
| 9.9.3 | Encryption and Authentication | AD12 | 479 | Đã gán; xem phạm vi rà nội dung |
| 9.9.3.1 | Digital Signatures | AD12 | 480 | Đã gán; xem phạm vi rà nội dung |
| 9.9.3.2 | Digital Certificates | AD12 | 480 | Đã gán; xem phạm vi rà nội dung |
| 10.1 | Motivation | AD73 | 496 | Đã gán; xem phạm vi rà nội dung |
| 10.1.1 | Sources and Uses of Big Data | AD73 | 497 | Đã gán; xem phạm vi rà nội dung |
| 10.1.2 | Querying Big Data | AD73 | 499 | Đã gán; xem phạm vi rà nội dung |
| 10.2 | Big Data Storage Systems | AD73 | 501 | Đã gán; xem phạm vi rà nội dung |
| 10.2.1 | Distributed File Systems | AD73 | 502 | Đã gán; xem phạm vi rà nội dung |
| 10.2.2 | Sharding | AD73 | 504 | Đã gán; xem phạm vi rà nội dung |
| 10.2.3 | Key-Value Storage Systems | AD73 | 505 | Đã gán; xem phạm vi rà nội dung |
| 10.2.4 | Parallel and Distributed Databases | AD73 | 509 | Đã gán; xem phạm vi rà nội dung |
| 10.2.5 | Replication and Consistency | AD73 | 510 | Đã gán; xem phạm vi rà nội dung |
| 10.3 | The MapReduce Paradigm | AD20 | 512 | Đã gán; xem phạm vi rà nội dung |
| 10.3.1 | Why MapReduce? | AD20 | 512 | Đã gán; xem phạm vi rà nội dung |
| 10.3.2 | MapReduce By Example 1: Word Count | AD20 | 513 | Đã gán; xem phạm vi rà nội dung |
| 10.3.3 | MapReduce by Example 2: Log Processing | AD20 | 515 | Đã gán; xem phạm vi rà nội dung |
| 10.3.4 | Parallel Processing of MapReduce Tasks | AD20 | 517 | Đã gán; xem phạm vi rà nội dung |
| 10.3.5 | MapReduce in Hadoop | AD20 | 518 | Đã gán; xem phạm vi rà nội dung |
| 10.3.6 | SQL on MapReduce | AD20 | 522 | Đã gán; xem phạm vi rà nội dung |
| 10.4 | Beyond MapReduce: Algebraic Operations | AD20 | 523 | Đã gán; xem phạm vi rà nội dung |
| 10.4.1 | Motivation for Algebraic Operations | AD20 | 524 | Đã gán; xem phạm vi rà nội dung |
| 10.4.2 | Algebraic Operations in Spark | AD20 | 525 | Đã gán; xem phạm vi rà nội dung |
| 10.5 | Streaming Data | AD21 | 529 | Đã gán; xem phạm vi rà nội dung |
| 10.5.1 | Applications of Streaming Data | AD21 | 529 | Đã gán; xem phạm vi rà nội dung |
| 10.5.2 | Querying Streaming Data | AD21 | 531 | Đã gán; xem phạm vi rà nội dung |
| 10.5.2.1 | Stream Extensions to SQL | AD21 | 533 | Đã gán; xem phạm vi rà nội dung |
| 10.5.3 | Algebraic Operations on Streams | AD21 | 535 | Đã gán; xem phạm vi rà nội dung |
| 10.6 | Graph Databases | AD22 | 537 | Đã gán; xem phạm vi rà nội dung |
| 11.1 | Overview of Analytics | AD72 | 548 | Đã gán; xem phạm vi rà nội dung |
| 11.2 | Data Warehousing | AD72 | 550 | Đã gán; xem phạm vi rà nội dung |
| 11.2.1 | Components of a Data Warehouse | AD72 | 551 | Đã gán; xem phạm vi rà nội dung |
| 11.2.2 | Multidimensional Data and Warehouse Schemas | AD72 | 553 | Đã gán; xem phạm vi rà nội dung |
| 11.2.3 | Database Support for Data Warehouses | AD72 | 554 | Đã gán; xem phạm vi rà nội dung |
| 11.2.4 | Data Lakes | AD72 | 556 | Đã gán; xem phạm vi rà nội dung |
| 11.3 | Online Analytical Processing | AD72 | 556 | Đã gán; xem phạm vi rà nội dung |
| 11.3.1 | Aggregation on Multidimensional Data | AD72 | 556 | Đã gán; xem phạm vi rà nội dung |
| 11.3.2 | Relational Representation of Cross-Tabs | AD72 | 561 | Đã gán; xem phạm vi rà nội dung |
| 11.3.3 | OLAP in SQL | AD72 | 562 | Đã gán; xem phạm vi rà nội dung |
| 11.3.4 | Reporting and Visualization Tools | AD72 | 567 | Đã gán; xem phạm vi rà nội dung |
| 11.4 | Data Mining | AD19 | 569 | Đã gán; xem phạm vi rà nội dung |
| 11.4.1 | Types of Data-Mining Tasks | AD19 | 570 | Đã gán; xem phạm vi rà nội dung |
| 11.4.2 | Classification | AD70 | 570 | Đã gán; xem phạm vi rà nội dung |
| 11.4.2.1 | Decision-Tree Classifiers | AD70 | 571 | Đã gán; xem phạm vi rà nội dung |
| 11.4.2.2 | Bayesian Classifiers | AD70 | 572 | Đã gán; xem phạm vi rà nội dung |
| 11.4.2.3 | Support Vector Machine Classifiers | AD70 | 573 | Đã gán; xem phạm vi rà nội dung |
| 11.4.2.4 | Neural Network Classifiers | AD70 | 574 | Đã gán; xem phạm vi rà nội dung |
| 11.4.3 | Regression | AD70 | 575 | Đã gán; xem phạm vi rà nội dung |
| 11.4.4 | Association Rules | AD71 | 575 | Đã gán; xem phạm vi rà nội dung |
| 11.4.5 | Clustering | AD71 | 577 | Đã gán; xem phạm vi rà nội dung |
| 11.4.6 | Text Mining | AD19 | 578 | Đã gán; xem phạm vi rà nội dung |
| 12.1 | Overview of Physical Storage Media | AD23 | 588 | Đã gán; xem phạm vi rà nội dung |
| 12.2 | Storage Interfaces | AD23 | 591 | Đã gán; xem phạm vi rà nội dung |
| 12.3 | Magnetic Disks | AD23 | 592 | Đã gán; xem phạm vi rà nội dung |
| 12.3.1 | Physical Characteristics of Disks | AD23 | 592 | Đã gán; xem phạm vi rà nội dung |
| 12.3.2 | Performance Measures of Disks | AD23 | 594 | Đã gán; xem phạm vi rà nội dung |
| 12.4 | Flash Memory | AD23 | 596 | Đã gán; xem phạm vi rà nội dung |
| 12.5 | RAID | AD23 | 599 | Đã gán; xem phạm vi rà nội dung |
| 12.5.1 | Improvement of Reliability via Redundancy | AD23 | 599 | Đã gán; xem phạm vi rà nội dung |
| 12.5.2 | Improvement in Performance via Parallelism | AD23 | 600 | Đã gán; xem phạm vi rà nội dung |
| 12.5.3 | RAID Levels | AD23 | 601 | Đã gán; xem phạm vi rà nội dung |
| 12.5.4 | Hardware Issues | AD23 | 603 | Đã gán; xem phạm vi rà nội dung |
| 12.5.5 | Choice of RAID Level | AD23 | 605 | Đã gán; xem phạm vi rà nội dung |
| 12.5.6 | Other RAID Applications | AD23 | 606 | Đã gán; xem phạm vi rà nội dung |
| 12.6 | Disk-Block Access | AD23 | 606 | Đã gán; xem phạm vi rà nội dung |
| 13.1 | Database Storage Architecture | AD24 | 616 | Đã gán; xem phạm vi rà nội dung |
| 13.2 | File Organization | AD24 | 617 | Đã gán; xem phạm vi rà nội dung |
| 13.2.1 | Fixed-Length Records | AD24 | 618 | Đã gán; xem phạm vi rà nội dung |
| 13.2.2 | Variable-Length Records | AD24 | 621 | Đã gán; xem phạm vi rà nội dung |
| 13.2.3 | Storing Large Objects | AD24 | 623 | Đã gán; xem phạm vi rà nội dung |
| 13.3 | Organization of Records in Files | AD24 | 624 | Đã gán; xem phạm vi rà nội dung |
| 13.3.1 | Heap File Organization | AD24 | 625 | Đã gán; xem phạm vi rà nội dung |
| 13.3.2 | Sequential File Organization | AD24 | 626 | Đã gán; xem phạm vi rà nội dung |
| 13.3.3 | Multitable Clustering File Organization | AD24 | 627 | Đã gán; xem phạm vi rà nội dung |
| 13.3.4 | Partitioning | AD24 | 630 | Đã gán; xem phạm vi rà nội dung |
| 13.4 | Data-Dictionary Storage | AD24 | 631 | Đã gán; xem phạm vi rà nội dung |
| 13.5 | Database Buffer | AD25 | 633 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1 | Buffer Manager | AD25 | 633 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1.1 | Buffer replacement strategy | AD25 | 634 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1.2 | Pinned blocks | AD25 | 634 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1.3 | Shared and Exclusive Locks on Buffer | AD25 | 634 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1.4 | Output of blocks | AD25 | 635 | Đã gán; xem phạm vi rà nội dung |
| 13.5.1.5 | Forced output of blocks | AD25 | 636 | Đã gán; xem phạm vi rà nội dung |
| 13.5.2 | Buffer-Replacement Strategies | AD25 | 636 | Đã gán; xem phạm vi rà nội dung |
| 13.5.3 | Reordering of Writes and Recovery | AD25 | 638 | Đã gán; xem phạm vi rà nội dung |
| 13.6 | Column-Oriented Storage | AD26 | 640 | Đã gán; xem phạm vi rà nội dung |
| 13.7 | Storage Organization in Main-Memory Databases | AD26 | 644 | Đã gán; xem phạm vi rà nội dung |
| 14.1 | Basic Concepts | AD74 | 652 | Đã gán; xem phạm vi rà nội dung |
| 14.2 | Ordered Indices | AD74 | 654 | Đã gán; xem phạm vi rà nội dung |
| 14.2.1 | Dense and Sparse Indices | AD74 | 655 | Đã gán; xem phạm vi rà nội dung |
| 14.2.2 | Multilevel Indices | AD74 | 657 | Đã gán; xem phạm vi rà nội dung |
| 14.2.3 | Index Update | AD74 | 659 | Đã gán; xem phạm vi rà nội dung |
| 14.2.3.1 | Insertion | AD74 | 659 | Đã gán; xem phạm vi rà nội dung |
| 14.2.3.2 | Deletion | AD74 | 660 | Đã gán; xem phạm vi rà nội dung |
| 14.2.4 | Secondary Indices | AD74 | 661 | Đã gán; xem phạm vi rà nội dung |
| 14.2.5 | Indices on Multiple Keys | AD74 | 662 | Đã gán; xem phạm vi rà nội dung |
| 14.3 | B+-Tree Index Files | AD28 | 663 | Đã gán; xem phạm vi rà nội dung |
| 14.3.1 | Structure of a B +-Tree | AD28 | 663 | Đã gán; xem phạm vi rà nội dung |
| 14.3.2 | Queries on B +-Trees | AD28 | 666 | Đã gán; xem phạm vi rà nội dung |
| 14.3.3 | Updates on B +-Trees | AD28 | 670 | Đã gán; xem phạm vi rà nội dung |
| 14.3.3.1 | Insertion | AD28 | 670 | Đã gán; xem phạm vi rà nội dung |
| 14.3.3.2 | Deletion | AD28 | 674 | Đã gán; xem phạm vi rà nội dung |
| 14.3.4 | Complexity of B +-Tree Updates | AD28 | 676 | Đã gán; xem phạm vi rà nội dung |
| 14.3.5 | Nonunique Search Keys | AD28 | 678 | Đã gán; xem phạm vi rà nội dung |
| 14.4 | B+-Tree Extensions | AD28 | 679 | Đã gán; xem phạm vi rà nội dung |
| 14.4.1 | B +- T r e eF i l eO r g a n i z a t i o n | AD27 | 679 | Đã gán; xem phạm vi rà nội dung |
| 14.4.2 | Secondary Indices and Record Relocation | AD27 | 681 | Đã gán; xem phạm vi rà nội dung |
| 14.4.3 | Indexing Strings | AD28 | 682 | Đã gán; xem phạm vi rà nội dung |
| 14.4.4 | Bulk Loading of B +-Tree Indices | AD28 | 682 | Đã gán; xem phạm vi rà nội dung |
| 14.4.5 | B-Tree Index Files | AD28 | 684 | Đã gán; xem phạm vi rà nội dung |
| 14.4.6 | Indexing on Flash Storage | AD28 | 685 | Đã gán; xem phạm vi rà nội dung |
| 14.4.7 | Indexing in Main Memory | AD28 | 686 | Đã gán; xem phạm vi rà nội dung |
| 14.5 | Hash Indices | AD29 | 687 | Đã gán; xem phạm vi rà nội dung |
| 14.6 | Multiple-Key Access | AD30 | 690 | Đã gán; xem phạm vi rà nội dung |
| 14.6.1 | Using Multiple Single-Key Indices | AD30 | 690 | Đã gán; xem phạm vi rà nội dung |
| 14.6.2 | Indices on Multiple Keys | AD30 | 691 | Đã gán; xem phạm vi rà nội dung |
| 14.6.3 | Covering Indices | AD30 | 692 | Đã gán; xem phạm vi rà nội dung |
| 14.7 | Creation of Indices | AD30 | 693 | Đã gán; xem phạm vi rà nội dung |
| 14.8 | Write-Optimized Index Structures | AD31 | 694 | Đã gán; xem phạm vi rà nội dung |
| 14.8.1 | LSM Trees | AD31 | 695 | Đã gán; xem phạm vi rà nội dung |
| 14.8.2 | Buffer Tree | AD31 | 697 | Đã gán; xem phạm vi rà nội dung |
| 14.9 | Bitmap Indices | AD30 | 699 | Đã gán; xem phạm vi rà nội dung |
| 14.10 | Indexing of Spatial and Temporal Data | AD30 | 701 | Đã gán; xem phạm vi rà nội dung |
| 14.10.1 | Indexing of Spatial Data | AD30 | 701 | Đã gán; xem phạm vi rà nội dung |
| 14.10.2 | Indexing Temporal Data | AD30 | 704 | Đã gán; xem phạm vi rà nội dung |
| 15.1 | Overview | AD76 | 718 | Đã gán; xem phạm vi rà nội dung |
| 15.2 | Measures of Query Cost | AD76 | 721 | Đã gán; xem phạm vi rà nội dung |
| 15.3 | Selection Operation | AD76 | 724 | Đã gán; xem phạm vi rà nội dung |
| 15.3.1 | Selections Using File Scans and Indices | AD76 | 724 | Đã gán; xem phạm vi rà nội dung |
| 15.3.2 | Selections Involving Comparisons | AD76 | 727 | Đã gán; xem phạm vi rà nội dung |
| 15.3.3 | Implementation of Complex Selections | AD76 | 728 | Đã gán; xem phạm vi rà nội dung |
| 15.4 | Sorting | AD32 | 730 | Đã gán; xem phạm vi rà nội dung |
| 15.4.1 | External Sort-Merge Algorithm | AD32 | 730 | Đã gán; xem phạm vi rà nội dung |
| 15.4.2 | Cost Analysis of External Sort-Merge | AD32 | 731 | Đã gán; xem phạm vi rà nội dung |
| 15.5 | Join Operation | AD33 | 733 | Đã gán; xem phạm vi rà nội dung |
| 15.5.1 | Nested-Loop Join | AD77 | 733 | Đã gán; xem phạm vi rà nội dung |
| 15.5.2 | Block Nested-Loop Join | AD77 | 734 | Đã gán; xem phạm vi rà nội dung |
| 15.5.3 | Indexed Nested-Loop Join | AD77 | 736 | Đã gán; xem phạm vi rà nội dung |
| 15.5.4 | Merge Join | AD33 | 737 | Đã gán; xem phạm vi rà nội dung |
| 15.5.4.1 | Merge-Join Algorithm | AD33 | 737 | Đã gán; xem phạm vi rà nội dung |
| 15.5.4.2 | Cost Analysis | AD33 | 739 | Đã gán; xem phạm vi rà nội dung |
| 15.5.4.3 | Hybrid Merge Join | AD33 | 741 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5 | Hash Join | AD33 | 741 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5.1 | Basics | AD33 | 741 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5.2 | Recursive Partitioning | AD33 | 743 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5.3 | Handling of Overflows | AD33 | 744 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5.4 | Cost of Hash Join | AD33 | 744 | Đã gán; xem phạm vi rà nội dung |
| 15.5.5.5 | Hybrid Hash Join | AD33 | 746 | Đã gán; xem phạm vi rà nội dung |
| 15.5.6 | Complex Joins | AD33 | 747 | Đã gán; xem phạm vi rà nội dung |
| 15.5.7 | Joins over Spatial Data | AD33 | 748 | Đã gán; xem phạm vi rà nội dung |
| 15.6 | Other Operations | AD34 | 748 | Đã gán; xem phạm vi rà nội dung |
| 15.6.1 | Duplicate Elimination | AD34 | 748 | Đã gán; xem phạm vi rà nội dung |
| 15.6.2 | Projection | AD34 | 749 | Đã gán; xem phạm vi rà nội dung |
| 15.6.3 | Set Operations | AD34 | 749 | Đã gán; xem phạm vi rà nội dung |
| 15.6.4 | Outer Join | AD34 | 751 | Đã gán; xem phạm vi rà nội dung |
| 15.6.5 | Aggregation | AD34 | 752 | Đã gán; xem phạm vi rà nội dung |
| 15.7 | Evaluation of Expressions | AD34 | 753 | Đã gán; xem phạm vi rà nội dung |
| 15.7.1 | Materialization | AD34 | 753 | Đã gán; xem phạm vi rà nội dung |
| 15.7.2 | Pipelining | AD34 | 754 | Đã gán; xem phạm vi rà nội dung |
| 15.7.2.1 | Implementation of Pipelining | AD34 | 755 | Đã gán; xem phạm vi rà nội dung |
| 15.7.2.2 | Evaluation Algorithms for Pipelining | AD34 | 757 | Đã gán; xem phạm vi rà nội dung |
| 15.7.3 | Pipelines for Continuous-Stream Data | AD34 | 760 | Đã gán; xem phạm vi rà nội dung |
| 15.8 | Query Processing in Memory | AD34 | 760 | Đã gán; xem phạm vi rà nội dung |
| 15.8.1 | Cache-Conscious Algorithms | AD34 | 761 | Đã gán; xem phạm vi rà nội dung |
| 15.8.2 | Query Compilation | AD34 | 762 | Đã gán; xem phạm vi rà nội dung |
| 15.8.3 | Column-Oriented Storage | AD34 | 763 | Đã gán; xem phạm vi rà nội dung |
| 16.1 | Overview | AD35 | 772 | Đã gán; xem phạm vi rà nội dung |
| 16.2 | Transformation of Relational Expressions | AD35 | 776 | Đã gán; xem phạm vi rà nội dung |
| 16.2.1 | Equivalence Rules | AD35 | 776 | Đã gán; xem phạm vi rà nội dung |
| 16.2.2 | Examples of Transformations | AD35 | 781 | Đã gán; xem phạm vi rà nội dung |
| 16.2.3 | Join Ordering | AD35 | 783 | Đã gán; xem phạm vi rà nội dung |
| 16.2.4 | Enumeration of Equivalent Expressions | AD35 | 784 | Đã gán; xem phạm vi rà nội dung |
| 16.3 | Estimating Statistics of Expression Results | AD35 | 786 | Đã gán; xem phạm vi rà nội dung |
| 16.3.1 | Catalog Information | AD35 | 787 | Đã gán; xem phạm vi rà nội dung |
| 16.3.2 | Selection Size Estimation | AD35 | 789 | Đã gán; xem phạm vi rà nội dung |
| 16.3.3 | Join Size Estimation | AD35 | 791 | Đã gán; xem phạm vi rà nội dung |
| 16.3.4 | Size Estimation for Other Operations | AD35 | 793 | Đã gán; xem phạm vi rà nội dung |
| 16.3.5 | Estimation of Number of Distinct Values | AD35 | 794 | Đã gán; xem phạm vi rà nội dung |
| 16.4 | Choice of Evaluation Plans | AD36 | 795 | Đã gán; xem phạm vi rà nội dung |
| 16.4.1 | Cost-Based Join-Order Selection | AD36 | 796 | Đã gán; xem phạm vi rà nội dung |
| 16.4.2 | Cost-Based Optimization with Equivalence Rules | AD36 | 800 | Đã gán; xem phạm vi rà nội dung |
| 16.4.3 | Heuristics in Optimization | AD36 | 800 | Đã gán; xem phạm vi rà nội dung |
| 16.4.4 | Optimizing Nested Subqueries | AD78 | 803 | Đã gán; xem phạm vi rà nội dung |
| 16.5 | Materialized Views | AD37 | 807 | Đã gán; xem phạm vi rà nội dung |
| 16.5.1 | View Maintenance | AD18, AD37 | 808 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2 | Incremental View Maintenance | AD18, AD37 | 808 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2.1 | Join Operation | AD18, AD37 | 809 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2.2 | Selection and Projection Operations | AD18, AD37 | 809 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2.3 | Aggregation Operations | AD18, AD37 | 810 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2.4 | Other Operations | AD18, AD37 | 811 | Đã gán; xem phạm vi rà nội dung |
| 16.5.2.5 | Handling Expressions | AD18, AD37 | 811 | Đã gán; xem phạm vi rà nội dung |
| 16.5.3 | Query Optimization and Materialized Views | AD37 | 811 | Đã gán; xem phạm vi rà nội dung |
| 16.5.4 | Materialized View and Index Selection | AD37 | 812 | Đã gán; xem phạm vi rà nội dung |
| 16.6 | Advanced Topics in Query Optimization | AD37 | 812 | Đã gán; xem phạm vi rà nội dung |
| 16.6.1 | Top- K Optimization | AD37 | 813 | Đã gán; xem phạm vi rà nội dung |
| 16.6.2 | Join Minimization | AD37 | 813 | Đã gán; xem phạm vi rà nội dung |
| 16.6.3 | Optimization of Updates | AD37 | 813 | Đã gán; xem phạm vi rà nội dung |
| 16.6.4 | Multiquery Optimization and Shared Scans | AD37 | 814 | Đã gán; xem phạm vi rà nội dung |
| 16.6.5 | Parametric Query Optimization | AD37 | 815 | Đã gán; xem phạm vi rà nội dung |
| 16.6.6 | Adaptive Query Processing | AD37 | 815 | Đã gán; xem phạm vi rà nội dung |
| 17.1 | Transaction Concept | AD38 | 828 | Đã gán; xem phạm vi rà nội dung |
| 17.2 | A Simple TransactionModel | AD38 | 830 | Đã gán; xem phạm vi rà nội dung |
| 17.3 | Storage Structure | AD23 | 833 | Đã gán; xem phạm vi rà nội dung |
| 17.4 | Transaction Atomicity and Durability | AD38 | 834 | Đã gán; xem phạm vi rà nội dung |
| 17.5 | Transaction Isolation | AD38 | 836 | Đã gán; xem phạm vi rà nội dung |
| 17.6 | Serializability | AD38 | 841 | Đã gán; xem phạm vi rà nội dung |
| 17.7 | Transaction Isolation and Atomicity | AD38 | 848 | Đã gán; xem phạm vi rà nội dung |
| 17.7.1 | Recoverable Schedules | AD38 | 848 | Đã gán; xem phạm vi rà nội dung |
| 17.7.2 | Cascadeless Schedules | AD38 | 849 | Đã gán; xem phạm vi rà nội dung |
| 17.8 | Transaction Isolation Levels | AD38 | 850 | Đã gán; xem phạm vi rà nội dung |
| 17.9 | Implementation of Isolation Levels | AD38 | 852 | Đã gán; xem phạm vi rà nội dung |
| 17.9.1 | Locking | AD38 | 852 | Đã gán; xem phạm vi rà nội dung |
| 17.9.2 | Timestamps | AD38 | 854 | Đã gán; xem phạm vi rà nội dung |
| 17.9.3 | Multiple Versions and Snapshot Isolation | AD38 | 854 | Đã gán; xem phạm vi rà nội dung |
| 17.10 | Transactions as SQL Statements | AD38 | 855 | Đã gán; xem phạm vi rà nội dung |
| 18.1 | Lock-Based Protocols | AD39 | 864 | Đã gán; xem phạm vi rà nội dung |
| 18.1.1 | Locks | AD39 | 864 | Đã gán; xem phạm vi rà nội dung |
| 18.1.2 | Granting of Locks | AD39 | 869 | Đã gán; xem phạm vi rà nội dung |
| 18.1.3 | The Two-Phase Locking Protocol | AD39 | 870 | Đã gán; xem phạm vi rà nội dung |
| 18.1.4 | Implementation of Locking | AD39 | 873 | Đã gán; xem phạm vi rà nội dung |
| 18.1.5 | Graph-Based Protocols | AD39 | 875 | Đã gán; xem phạm vi rà nội dung |
| 18.2 | Deadlock Handling | AD40 | 878 | Đã gán; xem phạm vi rà nội dung |
| 18.2.1 | Deadlock Prevention | AD40 | 878 | Đã gán; xem phạm vi rà nội dung |
| 18.2.2 | Deadlock Detection and Recovery | AD40 | 880 | Đã gán; xem phạm vi rà nội dung |
| 18.2.2.1 | Deadlock Detection | AD40 | 880 | Đã gán; xem phạm vi rà nội dung |
| 18.2.2.2 | Recovery from Deadlock | AD40 | 882 | Đã gán; xem phạm vi rà nội dung |
| 18.3 | Multiple Granularity | AD39 | 882 | Đã gán; xem phạm vi rà nội dung |
| 18.4 | Insert Operations, Delete Operations, and Predicate Reads | AD40 | 886 | Đã gán; xem phạm vi rà nội dung |
| 18.4.1 | Deletion | AD40 | 886 | Đã gán; xem phạm vi rà nội dung |
| 18.4.2 | Insertion | AD40 | 887 | Đã gán; xem phạm vi rà nội dung |
| 18.4.3 | Predicate Reads and The Phantom Phenomenon | AD40 | 887 | Đã gán; xem phạm vi rà nội dung |
| 18.5 | Timestamp-Based Protocols | AD41 | 890 | Đã gán; xem phạm vi rà nội dung |
| 18.5.1 | Timestamps | AD41 | 890 | Đã gán; xem phạm vi rà nội dung |
| 18.5.2 | The Timestamp-Ordering Protocol | AD41 | 891 | Đã gán; xem phạm vi rà nội dung |
| 18.5.3 | Thomas’ Write Rule | AD41 | 893 | Đã gán; xem phạm vi rà nội dung |
| 18.6 | Validation-Based Protocols | AD41 | 895 | Đã gán; xem phạm vi rà nội dung |
| 18.7 | Multiversion Schemes | AD42 | 898 | Đã gán; xem phạm vi rà nội dung |
| 18.7.1 | Multiversion Timestamp Ordering | AD42 | 899 | Đã gán; xem phạm vi rà nội dung |
| 18.7.2 | Multiversion Two-Phase Locking | AD42 | 900 | Đã gán; xem phạm vi rà nội dung |
| 18.8 | Snapshot Isolation | AD42 | 901 | Đã gán; xem phạm vi rà nội dung |
| 18.8.1 | Multiversioning in Snapshot Isolation | AD42 | 902 | Đã gán; xem phạm vi rà nội dung |
| 18.8.2 | Validation Steps for Update Transactions | AD42 | 903 | Đã gán; xem phạm vi rà nội dung |
| 18.8.3 | Serializability Issues and Solutions | AD42 | 904 | Đã gán; xem phạm vi rà nội dung |
| 18.9 | Weak Levels of Consistency in Practice | AD42 | 909 | Đã gán; xem phạm vi rà nội dung |
| 18.9.1 | Degree-Two Consistency | AD42 | 909 | Đã gán; xem phạm vi rà nội dung |
| 18.9.2 | Cursor Stability | AD42 | 910 | Đã gán; xem phạm vi rà nội dung |
| 18.9.3 | Concurrency Control Across User Interactions | AD42 | 910 | Đã gán; xem phạm vi rà nội dung |
| 18.10 | Advanced Topics in Concurrency Control | AD63 | 912 | Đã gán; xem phạm vi rà nội dung |
| 18.10.1 | Online Index Creation | AD63 | 913 | Đã gán; xem phạm vi rà nội dung |
| 18.10.2 | Concurrency in Index Structures | AD63 | 914 | Đã gán; xem phạm vi rà nội dung |
| 18.10.3 | Concurrency Control in Main-Memory Databases | AD63 | 916 | Đã gán; xem phạm vi rà nội dung |
| 18.10.4 | Long-Duration Transactions | AD63 | 919 | Đã gán; xem phạm vi rà nội dung |
| 18.10.5 | Concurrency Control with Operations | AD63 | 920 | Đã gán; xem phạm vi rà nội dung |
| 18.10.6 | Real-Time Transaction Systems | AD63 | 923 | Đã gán; xem phạm vi rà nội dung |
| 19.1 | Failure Classification | AD43 | 936 | Đã gán; xem phạm vi rà nội dung |
| 19.2 | Storage | AD43 | 937 | Đã gán; xem phạm vi rà nội dung |
| 19.2.1 | Stable-Storage Implementation | AD43 | 938 | Đã gán; xem phạm vi rà nội dung |
| 19.2.2 | Data Access | AD43 | 939 | Đã gán; xem phạm vi rà nội dung |
| 19.3 | Recovery and Atomicity | AD43 | 941 | Đã gán; xem phạm vi rà nội dung |
| 19.3.1 | Log Records | AD43 | 942 | Đã gán; xem phạm vi rà nội dung |
| 19.3.2 | Database Modification | AD43 | 944 | Đã gán; xem phạm vi rà nội dung |
| 19.3.3 | Concurrency Control and Recovery | AD43 | 945 | Đã gán; xem phạm vi rà nội dung |
| 19.3.4 | Transaction Commit | AD43 | 946 | Đã gán; xem phạm vi rà nội dung |
| 19.3.5 | Using the Log to Redo and Undo Transactions | AD43 | 946 | Đã gán; xem phạm vi rà nội dung |
| 19.3.6 | Checkpoints | AD43 | 949 | Đã gán; xem phạm vi rà nội dung |
| 19.4 | Recovery Algorithm | AD43 | 951 | Đã gán; xem phạm vi rà nội dung |
| 19.4.1 | Transaction Rollback | AD43 | 951 | Đã gán; xem phạm vi rà nội dung |
| 19.4.2 | Recovery After a System Crash | AD43 | 952 | Đã gán; xem phạm vi rà nội dung |
| 19.4.3 | Optimizing Commit Processing | AD43 | 954 | Đã gán; xem phạm vi rà nội dung |
| 19.5 | Buffer Management | AD43 | 955 | Đã gán; xem phạm vi rà nội dung |
| 19.5.1 | Log-Record Buffering | AD43 | 955 | Đã gán; xem phạm vi rà nội dung |
| 19.5.2 | Database Buffering | AD43 | 956 | Đã gán; xem phạm vi rà nội dung |
| 19.5.3 | Operating System Role in Buffer Management | AD43 | 958 | Đã gán; xem phạm vi rà nội dung |
| 19.5.4 | Fuzzy Checkpointing | AD43 | 959 | Đã gán; xem phạm vi rà nội dung |
| 19.6 | Failure with Loss of Non-Volatile Storage | AD43 | 959 | Đã gán; xem phạm vi rà nội dung |
| 19.7 | High Availability Using Remote Backup Systems | AD45 | 960 | Đã gán; xem phạm vi rà nội dung |
| 19.8 | Early Lock Release and Logical Undo Operations | AD44 | 964 | Đã gán; xem phạm vi rà nội dung |
| 19.8.1 | Logical Operations | AD44 | 964 | Đã gán; xem phạm vi rà nội dung |
| 19.8.2 | Logical Undo Log Records | AD44 | 965 | Đã gán; xem phạm vi rà nội dung |
| 19.8.3 | Transaction Rollback with Logical Undo | AD44 | 966 | Đã gán; xem phạm vi rà nội dung |
| 19.8.4 | Concurrency Issues in Logical Undo | AD44 | 969 | Đã gán; xem phạm vi rà nội dung |
| 19.9 | ARIES | AD44 | 970 | Đã gán; xem phạm vi rà nội dung |
| 19.9.1 | Data Structures | AD44 | 971 | Đã gán; xem phạm vi rà nội dung |
| 19.9.2 | Recovery Algorithm | AD44 | 973 | Đã gán; xem phạm vi rà nội dung |
| 19.9.2.1 | Analysis Pass | AD44 | 973 | Đã gán; xem phạm vi rà nội dung |
| 19.9.2.2 | Redo Pass | AD44 | 973 | Đã gán; xem phạm vi rà nội dung |
| 19.9.2.3 | Undo Pass and Transaction Rollback | AD44 | 974 | Đã gán; xem phạm vi rà nội dung |
| 19.9.3 | Other Features | AD44 | 975 | Đã gán; xem phạm vi rà nội dung |
| 19.10 | Recovery in Main-Memory Databases | AD45 | 976 | Đã gán; xem phạm vi rà nội dung |
| 20.1 | Overview | AD46 | 990 | Đã gán; xem phạm vi rà nội dung |
| 20.2 | Centralized Database Systems | AD46 | 991 | Đã gán; xem phạm vi rà nội dung |
| 20.3 | Server System Architectures | AD46 | 992 | Đã gán; xem phạm vi rà nội dung |
| 20.3.1 | Transaction-Server Architecture | AD46 | 993 | Đã gán; xem phạm vi rà nội dung |
| 20.3.2 | Data Servers and Data Storage Systems | AD46 | 997 | Đã gán; xem phạm vi rà nội dung |
| 20.3.3 | Caching at Clients | AD46 | 997 | Đã gán; xem phạm vi rà nội dung |
| 20.4 | Parallel Systems | AD46 | 999 | Đã gán; xem phạm vi rà nội dung |
| 20.4.1 | Motivation for Parallel Databases | AD46 | 999 | Đã gán; xem phạm vi rà nội dung |
| 20.4.2 | Measures of Performance for Parallel Systems | AD46 | 1000 | Đã gán; xem phạm vi rà nội dung |
| 20.4.3 | Interconnection Networks | AD46 | 1004 | Đã gán; xem phạm vi rà nội dung |
| 20.4.4 | Parallel Database Architectures | AD46 | 1008 | Đã gán; xem phạm vi rà nội dung |
| 20.4.5 | Shared Memory | AD46 | 1009 | Đã gán; xem phạm vi rà nội dung |
| 20.4.5.1 | Shared-Memory Architectures | AD46 | 1010 | Đã gán; xem phạm vi rà nội dung |
| 20.4.5.2 | Cache Coherency | AD46 | 1012 | Đã gán; xem phạm vi rà nội dung |
| 20.4.6 | Shared Disk | AD46 | 1013 | Đã gán; xem phạm vi rà nội dung |
| 20.4.7 | Shared Nothing | AD46 | 1014 | Đã gán; xem phạm vi rà nội dung |
| 20.4.8 | Hierarchical | AD46 | 1015 | Đã gán; xem phạm vi rà nội dung |
| 20.5 | Distributed Systems | AD79 | 1015 | Đã gán; xem phạm vi rà nội dung |
| 20.6 | Transaction Processing in Parallel and Distributed Systems | AD79 | 1018 | Đã gán; xem phạm vi rà nội dung |
| 20.7 | Cloud-Based Services | AD79 | 1019 | Đã gán; xem phạm vi rà nội dung |
| 20.7.1 | Cloud Service Models | AD79 | 1020 | Đã gán; xem phạm vi rà nội dung |
| 20.7.2 | Benefits and Limitations of Cloud Services | AD79 | 1024 | Đã gán; xem phạm vi rà nội dung |
| 21.1 | Overview | AD47 | 1032 | Đã gán; xem phạm vi rà nội dung |
| 21.2 | Data Partitioning | AD47 | 1033 | Đã gán; xem phạm vi rà nội dung |
| 21.2.1 | Partitioning Strategies | AD47 | 1033 | Đã gán; xem phạm vi rà nội dung |
| 21.2.2 | Comparison of Partitioning Techniques | AD47 | 1035 | Đã gán; xem phạm vi rà nội dung |
| 21.3 | Dealing with Skew in Partitioning | AD47 | 1036 | Đã gán; xem phạm vi rà nội dung |
| 21.3.1 | Balanced Range-Partitioning Vectors | AD47 | 1037 | Đã gán; xem phạm vi rà nội dung |
| 21.3.2 | Virtual Node Partitioning | AD47 | 1038 | Đã gán; xem phạm vi rà nội dung |
| 21.3.3 | Dynamic Repartitioning | AD47 | 1039 | Đã gán; xem phạm vi rà nội dung |
| 21.4 | Replication | AD47 | 1042 | Đã gán; xem phạm vi rà nội dung |
| 21.4.1 | Location of Replicas | AD47 | 1043 | Đã gán; xem phạm vi rà nội dung |
| 21.4.2 | Updates and Consistency of Replicas | AD47 | 1044 | Đã gán; xem phạm vi rà nội dung |
| 21.5 | Parallel Indexing | AD64 | 1046 | Đã gán; xem phạm vi rà nội dung |
| 21.6 | Distributed File Systems | AD64 | 1048 | Đã gán; xem phạm vi rà nội dung |
| 21.7 | Parallel Key-Value Stores | AD64 | 1052 | Đã gán; xem phạm vi rà nội dung |
| 21.7.1 | Data Representation | AD64 | 1053 | Đã gán; xem phạm vi rà nội dung |
| 21.7.2 | Storing and Retrieving Data | AD64 | 1054 | Đã gán; xem phạm vi rà nội dung |
| 21.7.2.1 | Geographically Distributed Storage | AD64 | 1055 | Đã gán; xem phạm vi rà nội dung |
| 21.7.2.2 | Index Structure | AD64 | 1057 | Đã gán; xem phạm vi rà nội dung |
| 21.7.3 | Support for Transactions | AD64 | 1057 | Đã gán; xem phạm vi rà nội dung |
| 21.7.3.1 | Concurrency Control | AD64 | 1057 | Đã gán; xem phạm vi rà nội dung |
| 21.7.3.2 | Atomic Commit | AD64 | 1058 | Đã gán; xem phạm vi rà nội dung |
| 21.7.3.3 | Dealing with Failures | AD64 | 1058 | Đã gán; xem phạm vi rà nội dung |
| 21.7.4 | Managing Without Declarative Queries | AD64 | 1059 | Đã gán; xem phạm vi rà nội dung |
| 21.7.5 | Performance Optimizations | AD64 | 1060 | Đã gán; xem phạm vi rà nội dung |
| 22.1 | Overview | AD48 | 1068 | Đã gán; xem phạm vi rà nội dung |
| 22.2 | Parallel Sort | AD48 | 1070 | Đã gán; xem phạm vi rà nội dung |
| 22.2.1 | Range-Partitioning Sort | AD48 | 1070 | Đã gán; xem phạm vi rà nội dung |
| 22.2.2 | Parallel External Sort-Merge | AD48 | 1071 | Đã gán; xem phạm vi rà nội dung |
| 22.3 | Parallel Join | AD48 | 1072 | Đã gán; xem phạm vi rà nội dung |
| 22.3.1 | Partitioned Join | AD48 | 1072 | Đã gán; xem phạm vi rà nội dung |
| 22.3.2 | Fragment-and-Replicate Join | AD48 | 1075 | Đã gán; xem phạm vi rà nội dung |
| 22.3.3 | Handling Skew in Parallel Joins | AD48 | 1076 | Đã gán; xem phạm vi rà nội dung |
| 22.4 | Other Operations | AD48 | 1077 | Đã gán; xem phạm vi rà nội dung |
| 22.4.1 | Other Relational Operations | AD48 | 1078 | Đã gán; xem phạm vi rà nội dung |
| 22.4.2 | Map and Reduce Operations | AD48 | 1079 | Đã gán; xem phạm vi rà nội dung |
| 22.5 | Parallel Evaluation of Query Plans | AD80 | 1081 | Đã gán; xem phạm vi rà nội dung |
| 22.5.1 | Interoperation Parallelism | AD80 | 1081 | Đã gán; xem phạm vi rà nội dung |
| 22.5.1.1 | Pipelined Parallelism | AD80 | 1082 | Đã gán; xem phạm vi rà nội dung |
| 22.5.1.2 | Independent Parallelism | AD80 | 1083 | Đã gán; xem phạm vi rà nội dung |
| 22.5.2 | The Exchange Operator Model | AD80 | 1084 | Đã gán; xem phạm vi rà nội dung |
| 22.5.3 | Putting It All Together | AD80 | 1086 | Đã gán; xem phạm vi rà nội dung |
| 22.5.4 | Fault Tolerance in Query Plans | AD80 | 1088 | Đã gán; xem phạm vi rà nội dung |
| 22.6 | Query Processing on Shared-Memory Architectures | AD80 | 1090 | Đã gán; xem phạm vi rà nội dung |
| 22.7 | Query Optimization for Parallel Execution | AD80 | 1093 | Đã gán; xem phạm vi rà nội dung |
| 22.7.1 | Parallel Query Plan Space | AD80 | 1093 | Đã gán; xem phạm vi rà nội dung |
| 22.7.2 | Cost of Parallel Query Evaluation | AD80 | 1094 | Đã gán; xem phạm vi rà nội dung |
| 22.7.3 | Choosing a Parallel Query Plan | AD80 | 1095 | Đã gán; xem phạm vi rà nội dung |
| 22.7.4 | Colocation of Data | AD80 | 1097 | Đã gán; xem phạm vi rà nội dung |
| 22.7.5 | Parallel Maintenance of Materialized Views | AD80 | 1098 | Đã gán; xem phạm vi rà nội dung |
| 22.8 | Parallel Processing of Streaming Data | AD49 | 1099 | Đã gán; xem phạm vi rà nội dung |
| 22.8.1 | Routing of Tuples | AD49 | 1100 | Đã gán; xem phạm vi rà nội dung |
| 22.8.2 | Parallel Processing of Stream Operations | AD49 | 1102 | Đã gán; xem phạm vi rà nội dung |
| 22.8.3 | Fault Tolerance with Streaming Data | AD49 | 1103 | Đã gán; xem phạm vi rà nội dung |
| 22.9 | Distributed Query Processing | AD49 | 1105 | Đã gán; xem phạm vi rà nội dung |
| 22.9.1 | Data Integration from Multiple Data Sources | AD49 | 1105 | Đã gán; xem phạm vi rà nội dung |
| 22.9.2 | Schema and Data Integration | AD49 | 1107 | Đã gán; xem phạm vi rà nội dung |
| 22.9.3 | Query Processing Across Multiple Data Sources | AD49 | 1109 | Đã gán; xem phạm vi rà nội dung |
| 22.9.3.1 | Join Locations and Join Ordering | AD49 | 1110 | Đã gán; xem phạm vi rà nội dung |
| 22.9.3.2 | Semijoin Strategy | AD49 | 1111 | Đã gán; xem phạm vi rà nội dung |
| 22.9.3.3 | Distributed Query Optimization | AD49 | 1113 | Đã gán; xem phạm vi rà nội dung |
| 22.9.4 | Distributed Directory Systems | AD49 | 1113 | Đã gán; xem phạm vi rà nội dung |
| 23.1 | Distributed Transactions | AD50 | 1127 | Đã gán; xem phạm vi rà nội dung |
| 23.1.1 | System Structure | AD50 | 1127 | Đã gán; xem phạm vi rà nội dung |
| 23.1.2 | System Failure Modes | AD50 | 1129 | Đã gán; xem phạm vi rà nội dung |
| 23.2 | Commit Protocols | AD50 | 1129 | Đã gán; xem phạm vi rà nội dung |
| 23.2.1 | Two-Phase Commit | AD50 | 1130 | Đã gán; xem phạm vi rà nội dung |
| 23.2.1.1 | The Commit Protocol | AD50 | 1130 | Đã gán; xem phạm vi rà nội dung |
| 23.2.1.2 | Handling of Failures | AD50 | 1132 | Đã gán; xem phạm vi rà nội dung |
| 23.2.1.3 | Recovery and Concurrency Control | AD50 | 1134 | Đã gán; xem phạm vi rà nội dung |
| 23.2.2 | A voiding Blocking During Commit | AD50 | 1135 | Đã gán; xem phạm vi rà nội dung |
| 23.2.3 | Alternative Models of Transaction Processing | AD50 | 1137 | Đã gán; xem phạm vi rà nội dung |
| 23.3 | Concurrency Control in Distributed Databases | AD65 | 1140 | Đã gán; xem phạm vi rà nội dung |
| 23.3.1 | Locking Protocols | AD65 | 1140 | Đã gán; xem phạm vi rà nội dung |
| 23.3.1.1 | Single Lock-Manager Approach | AD65 | 1140 | Đã gán; xem phạm vi rà nội dung |
| 23.3.1.2 | Distributed Lock Manager | AD65 | 1141 | Đã gán; xem phạm vi rà nội dung |
| 23.3.2 | Deadlock Handling | AD65 | 1141 | Đã gán; xem phạm vi rà nội dung |
| 23.3.3 | Leases | AD65 | 1144 | Đã gán; xem phạm vi rà nội dung |
| 23.3.4 | Distributed Timestamp-Based Protocols | AD65 | 1145 | Đã gán; xem phạm vi rà nội dung |
| 23.3.5 | Generation of Timestamps | AD65 | 1146 | Đã gán; xem phạm vi rà nội dung |
| 23.3.6 | Distributed Timestamp Ordering | AD65 | 1147 | Đã gán; xem phạm vi rà nội dung |
| 23.3.7 | Distributed Validation | AD65 | 1148 | Đã gán; xem phạm vi rà nội dung |
| 23.4 | Replication | AD51 | 1150 | Đã gán; xem phạm vi rà nội dung |
| 23.4.1 | Consistency of Replicas | AD51 | 1150 | Đã gán; xem phạm vi rà nội dung |
| 23.4.2 | Concurrency Control with Replicas | AD51 | 1152 | Đã gán; xem phạm vi rà nội dung |
| 23.4.2.1 | Primary Copy | AD51 | 1152 | Đã gán; xem phạm vi rà nội dung |
| 23.4.2.2 | Majority Protocol | AD51 | 1152 | Đã gán; xem phạm vi rà nội dung |
| 23.4.2.3 | Biased Protocol | AD51 | 1153 | Đã gán; xem phạm vi rà nội dung |
| 23.4.2.4 | Quorum Consensus Protocol | AD51 | 1153 | Đã gán; xem phạm vi rà nội dung |
| 23.4.3 | Dealing with Failures | AD51 | 1154 | Đã gán; xem phạm vi rà nội dung |
| 23.4.3.1 | Robustness Using the Majority-Based Protocol | AD51 | 1154 | Đã gán; xem phạm vi rà nội dung |
| 23.4.3.2 | Reducing Read Cost | AD51 | 1156 | Đã gán; xem phạm vi rà nội dung |
| 23.4.4 | Reconfiguration and Reintegration | AD51 | 1157 | Đã gán; xem phạm vi rà nội dung |
| 23.5 | Extended Concurrency Control Protocols | AD65 | 1158 | Đã gán; xem phạm vi rà nội dung |
| 23.5.1 | Multiversion 2PL and Globally Consistent Timestamps | AD65 | 1158 | Đã gán; xem phạm vi rà nội dung |
| 23.5.2 | Distributed Snapshot Isolation | AD65 | 1160 | Đã gán; xem phạm vi rà nội dung |
| 23.5.3 | Concurrency Control in Federated Database Systems | AD65 | 1161 | Đã gán; xem phạm vi rà nội dung |
| 23.6 | Replication with Weak Degrees of Consistency | AD66 | 1162 | Đã gán; xem phạm vi rà nội dung |
| 23.6.1 | Trading Off Consistency for A vailability | AD66 | 1163 | Đã gán; xem phạm vi rà nội dung |
| 23.6.2 | Asynchronous Replication | AD66 | 1164 | Đã gán; xem phạm vi rà nội dung |
| 23.6.3 | Asynchronous View Maintenance | AD66 | 1167 | Đã gán; xem phạm vi rà nội dung |
| 23.6.4 | Detecting Inconsistent Updates | AD66 | 1169 | Đã gán; xem phạm vi rà nội dung |
| 23.6.5 | Resolving Conflicting Updates | AD66 | 1171 | Đã gán; xem phạm vi rà nội dung |
| 23.6.6 | Detecting Differences Between Collections Using Merkle Tree | AD66 | 1172 | Đã gán; xem phạm vi rà nội dung |
| 23.7 | Coordinator Selection | AD52 | 1175 | Đã gán; xem phạm vi rà nội dung |
| 23.7.1 | Backup Coordinator | AD52 | 1175 | Đã gán; xem phạm vi rà nội dung |
| 23.7.2 | Election of Coordinator | AD52 | 1176 | Đã gán; xem phạm vi rà nội dung |
| 23.7.2.1 | Distributed Coordination Services | AD52 | 1179 | Đã gán; xem phạm vi rà nội dung |
| 23.8 | Consensus in Distributed Systems | AD52 | 1179 | Đã gán; xem phạm vi rà nội dung |
| 23.8.1 | Problem Overview | AD52 | 1180 | Đã gán; xem phạm vi rà nội dung |
| 23.8.2 | The Paxos Consensus Protocol | AD52 | 1181 | Đã gán; xem phạm vi rà nội dung |
| 23.8.3 | The Raft Consensus Protocol | AD62 | 1184 | Đã gán; xem phạm vi rà nội dung |
| 23.8.4 | Fault-Tolerant Services Using Replicated State Machines | AD52 | 1187 | Đã gán; xem phạm vi rà nội dung |
| 23.8.5 | Two-Phase Commit Using Consensus | AD52 | 1190 | Đã gán; xem phạm vi rà nội dung |
| 24.1 | Bloom Filter | AD75 | 1204 | Đã gán; xem phạm vi rà nội dung |
| 24.2 | Log-Structured Merge Tree and Variants | AD31 | 1205 | Đã gán; xem phạm vi rà nội dung |
| 24.2.1 | Insertion into LSM Trees | AD31 | 1206 | Đã gán; xem phạm vi rà nội dung |
| 24.2.2 | Rolling Merges | AD31 | 1207 | Đã gán; xem phạm vi rà nội dung |
| 24.2.3 | Handling Deletes and Updates | AD31 | 1207 | Đã gán; xem phạm vi rà nội dung |
| 24.2.4 | The Stepped-Merge Index | AD31 | 1208 | Đã gán; xem phạm vi rà nội dung |
| 24.2.4.1 | Insertion Algorithm | AD31 | 1209 | Đã gán; xem phạm vi rà nội dung |
| 24.2.4.2 | Lookup Operations Using Bloom Filters | AD31 | 1210 | Đã gán; xem phạm vi rà nội dung |
| 24.2.5 | LSM Trees For Flash Storage | AD31 | 1211 | Đã gán; xem phạm vi rà nội dung |
| 24.3 | Bitmap Indices | AD30 | 1211 | Đã gán; xem phạm vi rà nội dung |
| 24.3.1 | Bitmap Index Structure | AD30 | 1211 | Đã gán; xem phạm vi rà nội dung |
| 24.3.2 | Efficient Implementation of Bitmap Operations | AD30 | 1213 | Đã gán; xem phạm vi rà nội dung |
| 24.3.3 | Bitmaps and B +-Trees | AD30 | 1214 | Đã gán; xem phạm vi rà nội dung |
| 24.4 | Indexing of Spatial Data | AD15 | 1215 | Đã gán; xem phạm vi rà nội dung |
| 24.4.1 | Quadtrees | AD15 | 1215 | Đã gán; xem phạm vi rà nội dung |
| 24.4.2 | R-Trees | AD15 | 1216 | Đã gán; xem phạm vi rà nội dung |
| 24.5 | Hash Indices | AD29 | 1219 | Đã gán; xem phạm vi rà nội dung |
| 24.5.1 | Static Hashing | AD29 | 1219 | Đã gán; xem phạm vi rà nội dung |
| 24.5.1.1 | Hash Functions | AD29 | 1221 | Đã gán; xem phạm vi rà nội dung |
| 24.5.1.2 | Handling of Bucket Overflows | AD29 | 1223 | Đã gán; xem phạm vi rà nội dung |
| 24.5.2 | Dynamic Hashing | AD29 | 1224 | Đã gán; xem phạm vi rà nội dung |
| 24.5.2.1 | Data Structure | AD29 | 1224 | Đã gán; xem phạm vi rà nội dung |
| 24.5.2.2 | Queries and Updates | AD29 | 1226 | Đã gán; xem phạm vi rà nội dung |
| 24.5.2.3 | Static Hashing versus Dynamic Hashing | AD29 | 1231 | Đã gán; xem phạm vi rà nội dung |
| 24.5.3 | Comparison of Ordered Indexing and Hashing | AD29 | 1232 | Đã gán; xem phạm vi rà nội dung |
| 25.1 | Performance Tuning | AD53 | 1239 | Đã gán; xem phạm vi rà nội dung |
| 25.1.1 | Motivation for Tuning | AD53 | 1239 | Đã gán; xem phạm vi rà nội dung |
| 25.1.2 | Location of Bottlenecks | AD53 | 1240 | Đã gán; xem phạm vi rà nội dung |
| 25.1.3 | Tuning Levels | AD53 | 1242 | Đã gán; xem phạm vi rà nội dung |
| 25.1.4 | Tuning of Physical Schema | AD53 | 1243 | Đã gán; xem phạm vi rà nội dung |
| 25.1.4.1 | Tuning of Indices | AD53 | 1244 | Đã gán; xem phạm vi rà nội dung |
| 25.1.4.2 | Using Materialized Views | AD53 | 1244 | Đã gán; xem phạm vi rà nội dung |
| 25.1.4.3 | Horizontal Partitioning of Relation Schema | AD53 | 1245 | Đã gán; xem phạm vi rà nội dung |
| 25.1.4.4 | Automated Tuning of Physical Design | AD53 | 1246 | Đã gán; xem phạm vi rà nội dung |
| 25.1.5 | Tuning of Queries | AD53 | 1248 | Đã gán; xem phạm vi rà nội dung |
| 25.1.5.1 | Tuning of Query Plans | AD53 | 1248 | Đã gán; xem phạm vi rà nội dung |
| 25.1.5.2 | Improving Set Orientation | AD53 | 1249 | Đã gán; xem phạm vi rà nội dung |
| 25.1.5.3 | Tuning of Bulk Loads and Updates | AD53 | 1250 | Đã gán; xem phạm vi rà nội dung |
| 25.1.6 | Tuning of the Logical Schema | AD53 | 1252 | Đã gán; xem phạm vi rà nội dung |
| 25.1.7 | Tuning of Concurrent Transactions | AD53 | 1253 | Đã gán; xem phạm vi rà nội dung |
| 25.1.8 | Tuning of Hardware | AD53 | 1256 | Đã gán; xem phạm vi rà nội dung |
| 25.1.9 | Performance Simulation | AD53 | 1259 | Đã gán; xem phạm vi rà nội dung |
| 25.2 | Performance Benchmarks | AD53 | 1259 | Đã gán; xem phạm vi rà nội dung |
| 25.2.1 | Suites of Tasks | AD53 | 1260 | Đã gán; xem phạm vi rà nội dung |
| 25.2.2 | Database-Application Classes | AD53 | 1260 | Đã gán; xem phạm vi rà nội dung |
| 25.2.3 | The TPC Benchmarks | AD53 | 1261 | Đã gán; xem phạm vi rà nội dung |
| 25.3 | Other Issues in Application Development | AD53 | 1263 | Đã gán; xem phạm vi rà nội dung |
| 25.3.1 | Testing Applications | AD53 | 1263 | Đã gán; xem phạm vi rà nội dung |
| 25.3.2 | Application Migration | AD53 | 1264 | Đã gán; xem phạm vi rà nội dung |
| 25.4 | Standardization | AD53 | 1266 | Đã gán; xem phạm vi rà nội dung |
| 25.4.1 | SQL Standards | AD53 | 1266 | Đã gán; xem phạm vi rà nội dung |
| 25.4.2 | Database Connectivity Standards | AD53 | 1267 | Đã gán; xem phạm vi rà nội dung |
| 25.4.3 | Object Database Standards | AD53 | 1268 | Đã gán; xem phạm vi rà nội dung |
| 25.5 | Distributed Directory Systems | AD53 | 1269 | Đã gán; xem phạm vi rà nội dung |
| 25.5.1 | Directory Access Protocols | AD53 | 1269 | Đã gán; xem phạm vi rà nội dung |
| 25.5.2 | LDAP: Lightweight Directory Access Protocol | AD53 | 1270 | Đã gán; xem phạm vi rà nội dung |
| 25.5.2.1 | LDAP Data Model | AD53 | 1270 | Đã gán; xem phạm vi rà nội dung |
| 25.5.2.2 | Data Manipulation | AD53 | 1271 | Đã gán; xem phạm vi rà nội dung |
| 25.5.2.3 | Distributed Directory Trees | AD53 | 1272 | Đã gán; xem phạm vi rà nội dung |
| 26.1 | Overview | AD81 | 1281 | Đã gán; xem phạm vi rà nội dung |
| 26.2 | Blockchain Properties | AD81 | 1283 | Đã gán; xem phạm vi rà nội dung |
| 26.3 | Achieving Blockchain Properties via Cryptographic Hash Functions | AD81 | 1288 | Đã gán; xem phạm vi rà nội dung |
| 26.3.1 | Properties of Cryptographic Hash Functions | AD81 | 1288 | Đã gán; xem phạm vi rà nội dung |
| 26.3.2 | Public-Key Encryption, Digital Signatures, and Irrefutability | AD81 | 1289 | Đã gán; xem phạm vi rà nội dung |
| 26.3.3 | Simple Blockchain Transactions | AD81 | 1290 | Đã gán; xem phạm vi rà nội dung |
| 26.4 | Consensus | AD54 | 1292 | Đã gán; xem phạm vi rà nội dung |
| 26.4.1 | Proof of Work | AD54 | 1293 | Đã gán; xem phạm vi rà nội dung |
| 26.4.2 | Proof of Stake | AD54 | 1295 | Đã gán; xem phạm vi rà nội dung |
| 26.4.3 | Byzantine Consensus | AD54 | 1295 | Đã gán; xem phạm vi rà nội dung |
| 26.5 | Data Management in a Blockchain | AD82 | 1296 | Đã gán; xem phạm vi rà nội dung |
| 26.5.1 | Efficient Lookup in a Blockchain | AD82 | 1297 | Đã gán; xem phạm vi rà nội dung |
| 26.5.2 | Maintaining Blockchain State | AD82 | 1298 | Đã gán; xem phạm vi rà nội dung |
| 26.6 | Smart Contracts | AD82 | 1298 | Đã gán; xem phạm vi rà nội dung |
| 26.6.1 | Languages and Transactions | AD82 | 1298 | Đã gán; xem phạm vi rà nội dung |
| 26.6.2 | External Input | AD82 | 1300 | Đã gán; xem phạm vi rà nội dung |
| 26.6.3 | Autonomous Smart Contracts | AD82 | 1301 | Đã gán; xem phạm vi rà nội dung |
| 26.6.4 | Cross-Chain Transactions | AD82 | 1302 | Đã gán; xem phạm vi rà nội dung |
| 26.7 | Performance Enhancement | AD82 | 1303 | Đã gán; xem phạm vi rà nội dung |
| 26.7.1 | Enhancing Consensus Performance | AD82 | 1304 | Đã gán; xem phạm vi rà nội dung |
| 26.7.2 | Enhancing Query Performance | AD82 | 1304 | Đã gán; xem phạm vi rà nội dung |
| 26.7.3 | Fault-Tolerance and Scalability | AD82 | 1305 | Đã gán; xem phạm vi rà nội dung |
| 26.8 | Emerging Applications | AD82 | 1305 | Đã gán; xem phạm vi rà nội dung |
| 27.1 | The Tuple Relational Calculus | AD02 | 1 | Đã gán; xem phạm vi rà nội dung |
| 27.1.1 | Example Queries | AD02 | 2 | Đã gán; xem phạm vi rà nội dung |
| 27.1.2 | Formal Definition | AD02 | 5 | Đã gán; xem phạm vi rà nội dung |
| 27.1.3 | Safety of Expressions | AD02 | 6 | Đã gán; xem phạm vi rà nội dung |
| 27.2 | The Domain Relational Calculus | AD02 | 7 | Đã gán; xem phạm vi rà nội dung |
| 27.2.1 | Formal Definition | AD02 | 7 | Đã gán; xem phạm vi rà nội dung |
| 27.2.2 | Example Queries | AD02 | 8 | Đã gán; xem phạm vi rà nội dung |
| 27.2.3 | Safety of Expressions | AD02 | 9 | Đã gán; xem phạm vi rà nội dung |
| 27.3 | Expressive Power of Pure Relational Query Languages | AD02 | 10 | Đã gán; xem phạm vi rà nội dung |
| 27.4 | Datalog | AD61 | 11 | Đã gán; xem phạm vi rà nội dung |
| 27.4.1 | Basic Structure | AD61 | 11 | Đã gán; xem phạm vi rà nội dung |
| 27.4.2 | Syntax of Datalog Rules | AD61 | 13 | Đã gán; xem phạm vi rà nội dung |
| 27.4.3 | Semantics of Nonrecursive Datalog | AD61 | 15 | Đã gán; xem phạm vi rà nội dung |
| 27.4.3.1 | Semantics of a Rule | AD61 | 15 | Đã gán; xem phạm vi rà nội dung |
| 27.4.3.2 | Semantics of a Program | AD61 | 16 | Đã gán; xem phạm vi rà nội dung |
| 27.4.4 | Safety | AD61 | 18 | Đã gán; xem phạm vi rà nội dung |
| 27.4.5 | Relational Operations in Datalog | AD61 | 19 | Đã gán; xem phạm vi rà nội dung |
| 27.4.6 | Recursion in Datalog | AD61 | 20 | Đã gán; xem phạm vi rà nội dung |
| 27.4.7 | The Power of Recursion | AD61 | 23 | Đã gán; xem phạm vi rà nội dung |
| 28.1 | Multivalued Dependencies | AD07 | 1 | Đã gán; xem phạm vi rà nội dung |
| 28.1.1 | Theory of Multivalued Dependencies | AD07 | 1 | Đã gán; xem phạm vi rà nội dung |
| 28.1.2 | Dependency Preservation | AD07 | 3 | Đã gán; xem phạm vi rà nội dung |
| 28.2 | Join Dependencies | AD08 | 6 | Đã gán; xem phạm vi rà nội dung |
| 28.2.1 | Definition of Join Dependencies | AD08 | 6 | Đã gán; xem phạm vi rà nội dung |
| 28.2.2 | Project-Join Normal Form | AD08 | 9 | Đã gán; xem phạm vi rà nội dung |
| 28.3 | Domain-Key Normal Form | AD08 | 9 | Đã gán; xem phạm vi rà nội dung |
| 29.1 | Complex Data Types | AD14 | 1 | Đã gán; xem phạm vi rà nội dung |
| 29.2 | SQL Extensions to Deal with Complex Data Types | AD14 | 4 | Đã gán; xem phạm vi rà nội dung |
| 29.3 | Type and Table Inheritance | AD14 | 7 | Đã gán; xem phạm vi rà nội dung |
| 29.3.1 | Type Inheritance | AD14 | 7 | Đã gán; xem phạm vi rà nội dung |
| 29.3.2 | Table Inheritance | AD14 | 9 | Đã gán; xem phạm vi rà nội dung |
| 29.4 | Array and Multiset Types in SQL | AD14 | 11 | Đã gán; xem phạm vi rà nội dung |
| 29.4.1 | Creating and Accessing Collection Values | AD14 | 12 | Đã gán; xem phạm vi rà nội dung |
| 29.4.2 | Querying Collection-Valued Attributes | AD14 | 12 | Đã gán; xem phạm vi rà nội dung |
| 29.4.3 | Nesting and Unnesting | AD14 | 13 | Đã gán; xem phạm vi rà nội dung |
| 30.1 | Motivation | AD68 | 1 | Đã gán; xem phạm vi rà nội dung |
| 30.2 | Structure of XML Data | AD68 | 6 | Đã gán; xem phạm vi rà nội dung |
| 30.3 | XML Document Schema | AD68 | 10 | Đã gán; xem phạm vi rà nội dung |
| 30.3.1 | Document Type Definition | AD68 | 11 | Đã gán; xem phạm vi rà nội dung |
| 30.3.2 | XML Schema | AD68 | 15 | Đã gán; xem phạm vi rà nội dung |
| 30.4 | Querying and Transformation | AD16 | 18 | Đã gán; xem phạm vi rà nội dung |
| 30.4.1 | Tree Model of XML | AD68 | 19 | Đã gán; xem phạm vi rà nội dung |
| 30.4.2 | XPath | AD68 | 19 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3 | XQuery | AD16 | 23 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.1 | FLWOR Expressions | AD16 | 23 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.2 | Joins | AD16 | 24 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.3 | Nested Queries | AD16 | 25 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.4 | Sorting of Results | AD16 | 27 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.5 | Functions and Types | AD16 | 27 | Đã gán; xem phạm vi rà nội dung |
| 30.4.3.6 | Other Features | AD16 | 28 | Đã gán; xem phạm vi rà nội dung |
| 30.5 | Application Program Interfaces to XML | AD16 | 29 | Đã gán; xem phạm vi rà nội dung |
| 30.6 | Storage of XML Data | AD16 | 30 | Đã gán; xem phạm vi rà nội dung |
| 30.6.1 | Non-relational Data Stores | AD16 | 31 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2 | Relational Databases | AD16 | 31 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2.1 | Store as String | AD16 | 32 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2.2 | Tree Representation | AD16 | 32 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2.3 | Map to Relations | AD16 | 33 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2.4 | Publishing and Shredding XML Data | AD16 | 34 | Đã gán; xem phạm vi rà nội dung |
| 30.6.2.5 | Native Storage within a Relational Database | AD16 | 34 | Đã gán; xem phạm vi rà nội dung |
| 30.6.3 | SQL/XML | AD16 | 35 | Đã gán; xem phạm vi rà nội dung |
| 30.7 | XML Applications | AD16 | 37 | Đã gán; xem phạm vi rà nội dung |
| 30.7.1 | Storing Data with Complex Structure | AD16 | 37 | Đã gán; xem phạm vi rà nội dung |
| 30.7.2 | Standardized Data Exchange Formats | AD16 | 38 | Đã gán; xem phạm vi rà nội dung |
| 30.7.3 | Web Services | AD16 | 38 | Đã gán; xem phạm vi rà nội dung |
| 30.7.4 | Data Mediation | AD16 | 40 | Đã gán; xem phạm vi rà nội dung |
| 31.1 | Overview | AD69 | 1 | Đã gán; xem phạm vi rà nội dung |
| 31.2 | Relevance Ranking Using Terms | AD69 | 3 | Đã gán; xem phạm vi rà nội dung |
| 31.2.1 | Ranking Using TF-IDF | AD69 | 3 | Đã gán; xem phạm vi rà nội dung |
| 31.2.2 | Similarity-Based Retrieval | AD69 | 5 | Đã gán; xem phạm vi rà nội dung |
| 31.3 | Relevance Using Hyperlinks | AD69 | 6 | Đã gán; xem phạm vi rà nội dung |
| 31.3.1 | Popularity Ranking | AD69 | 6 | Đã gán; xem phạm vi rà nội dung |
| 31.3.2 | PageRank | AD69 | 8 | Đã gán; xem phạm vi rà nội dung |
| 31.3.3 | Other Measures of Popularity | AD69 | 9 | Đã gán; xem phạm vi rà nội dung |
| 31.3.4 | Search Engine Spamming | AD69 | 10 | Đã gán; xem phạm vi rà nội dung |
| 31.3.5 | Combining TF-IDF and Popularity Ranking Measures | AD69 | 11 | Đã gán; xem phạm vi rà nội dung |
| 31.4 | Synonyms, Homonyms, and Ontologies | AD69 | 11 | Đã gán; xem phạm vi rà nội dung |
| 31.5 | Indexing of Documents | AD17 | 13 | Đã gán; xem phạm vi rà nội dung |
| 31.6 | Measuring Retrieval Effectiveness | AD17 | 15 | Đã gán; xem phạm vi rà nội dung |
| 31.7 | Crawling and Indexing the web | AD17 | 16 | Đã gán; xem phạm vi rà nội dung |
| 31.8 | Information Retrieval: Beyond Ranking of Pages | AD17 | 17 | Đã gán; xem phạm vi rà nội dung |
| 31.8.1 | Diversity of Query Results | AD17 | 18 | Đã gán; xem phạm vi rà nội dung |
| 31.8.2 | Information Extraction | AD17 | 18 | Đã gán; xem phạm vi rà nội dung |
| 31.8.3 | Question Answering | AD17 | 19 | Đã gán; xem phạm vi rà nội dung |
| 31.8.4 | Querying Structured Data | AD17 | 20 | Đã gán; xem phạm vi rà nội dung |
| 31.9 | Directories and Categories | AD17 | 21 | Đã gán; xem phạm vi rà nội dung |
| 32.1 | Interacting with PostgreSQL | AD55 | 2 | Đã gán; xem phạm vi rà nội dung |
| 32.1.1 | Interactive Terminal Interfaces | AD55 | 2 | Đã gán; xem phạm vi rà nội dung |
| 32.1.2 | Graphical Interfaces | AD55 | 2 | Đã gán; xem phạm vi rà nội dung |
| 32.1.3 | Programming Language Interfaces | AD55 | 2 | Đã gán; xem phạm vi rà nội dung |
| 32.2 | System Architecture | AD55 | 3 | Đã gán; xem phạm vi rà nội dung |
| 32.3 | Storage and Indexing | AD55 | 5 | Đã gán; xem phạm vi rà nội dung |
| 32.3.1 | Tables | AD55 | 5 | Đã gán; xem phạm vi rà nội dung |
| 32.3.2 | Indices | AD55 | 7 | Đã gán; xem phạm vi rà nội dung |
| 32.3.2.1 | Index Types | AD55 | 7 | Đã gán; xem phạm vi rà nội dung |
| 32.3.2.2 | Other Index Variations | AD55 | 10 | Đã gán; xem phạm vi rà nội dung |
| 32.3.2.3 | Index Construction | AD55 | 11 | Đã gán; xem phạm vi rà nội dung |
| 32.3.2.4 | Index-Only Scans | AD55 | 12 | Đã gán; xem phạm vi rà nội dung |
| 32.3.3 | Partitioning | AD55 | 13 | Đã gán; xem phạm vi rà nội dung |
| 32.4 | Query Processing and Optimization | AD55 | 14 | Đã gán; xem phạm vi rà nội dung |
| 32.4.1 | Query Rewrite | AD55 | 14 | Đã gán; xem phạm vi rà nội dung |
| 32.4.2 | Query Planning and Optimization | AD55 | 15 | Đã gán; xem phạm vi rà nội dung |
| 32.4.3 | Query Executor | AD55 | 16 | Đã gán; xem phạm vi rà nội dung |
| 32.4.4 | Parallel Query Support | AD55 | 17 | Đã gán; xem phạm vi rà nội dung |
| 32.4.5 | Triggers and Constraints | AD55 | 18 | Đã gán; xem phạm vi rà nội dung |
| 32.4.6 | Just-in-Time (JIT) Compilation | AD55 | 18 | Đã gán; xem phạm vi rà nội dung |
| 32.5 | Transaction Management in PostgreSQL | AD56 | 19 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1 | Concurrency Control | AD56 | 20 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.1 | Isolation Levels | AD56 | 20 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.2 | Concurrency Control for DML Commands | AD56 | 21 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.3 | Implementation of MVCC | AD56 | 21 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.4 | Implications of Using MVCC | AD56 | 26 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.5 | DDL Concurrency Control | AD56 | 27 | Đã gán; xem phạm vi rà nội dung |
| 32.5.1.6 | Locking and Indices | AD56 | 29 | Đã gán; xem phạm vi rà nội dung |
| 32.5.2 | Recovery | AD56 | 29 | Đã gán; xem phạm vi rà nội dung |
| 32.5.3 | High A vailability and Replication | AD56 | 30 | Đã gán; xem phạm vi rà nội dung |
| 32.6 | SQL Variations and Extensions | AD57 | 31 | Đã gán; xem phạm vi rà nội dung |
| 32.6.1 | PostgreSQL Types | AD57 | 31 | Đã gán; xem phạm vi rà nội dung |
| 32.6.1.1 | The PostgreSQL Type System | AD57 | 32 | Đã gán; xem phạm vi rà nội dung |
| 32.6.1.2 | Nonstandard Types | AD57 | 33 | Đã gán; xem phạm vi rà nội dung |
| 32.6.2 | Extensibility | AD57 | 34 | Đã gán; xem phạm vi rà nội dung |
| 32.6.2.1 | Types | AD57 | 34 | Đã gán; xem phạm vi rà nội dung |
| 32.6.2.2 | Functions | AD57 | 35 | Đã gán; xem phạm vi rà nội dung |
| 32.6.2.3 | Index Extensions | AD57 | 37 | Đã gán; xem phạm vi rà nội dung |
| 32.6.2.4 | Procedural Languages | AD57 | 38 | Đã gán; xem phạm vi rà nội dung |
| 32.7 | Foreign Data Wrappers | AD57 | 38 | Đã gán; xem phạm vi rà nội dung |
| 32.8 | PostgreSQL Internals for Developers | AD58 | 39 | Đã gán; xem phạm vi rà nội dung |
| 32.8.1 | Installation From Source Code | AD58 | 40 | Đã gán; xem phạm vi rà nội dung |
| 32.8.1.1 | Requirements | AD58 | 40 | Đã gán; xem phạm vi rà nội dung |
| 32.8.1.2 | Installation Steps | AD58 | 40 | Đã gán; xem phạm vi rà nội dung |
| 32.8.1.3 | Creating a Database | AD58 | 42 | Đã gán; xem phạm vi rà nội dung |
| 32.8.2 | Code Organization | AD58 | 44 | Đã gán; xem phạm vi rà nội dung |
| 32.8.3 | System Catalogs | AD58 | 46 | Đã gán; xem phạm vi rà nội dung |
| 32.8.4 | The Region-Based Memory Manager | AD83 | 47 | Đã gán; xem phạm vi rà nội dung |
| 32.8.5 | Node Structure and Node Functions | AD84 | 48 | Đã gán; xem phạm vi rà nội dung |
| 32.8.5.1 | Steps For Adding a New Node Type | AD84 | 49 | Đã gán; xem phạm vi rà nội dung |
| 32.8.5.2 | Casting Pointers to Subtypes and Supertypes | AD84 | 50 | Đã gán; xem phạm vi rà nội dung |
| 32.8.6 | Datum | AD84 | 51 | Đã gán; xem phạm vi rà nội dung |
| 32.8.7 | Tuple | AD84 | 51 | Đã gán; xem phạm vi rà nội dung |
| 32.8.8 | Query Execution Stack | AD58 | 53 | Đã gán; xem phạm vi rà nội dung |
| 32.8.8.1 | Memory Management and Contexts Switches | AD83 | 54 | Đã gán; xem phạm vi rà nội dung |
| 32.8.9 | Error Handling | AD58 | 56 | Đã gán; xem phạm vi rà nội dung |
| 32.8.10 | Tips For Adding New Functionality | AD58 | 56 | Đã gán; xem phạm vi rà nội dung |
| A.1 | Full Schema | AD59 | online | Đã gán; xem phạm vi rà nội dung |
| A.2 | DDL | AD59 | online | Đã gán; xem phạm vi rà nội dung |
| A.3 | Sample Data | AD59 | online | Đã gán; xem phạm vi rà nội dung |

## Cổng xác nhận đủ kiến thức

Để xác nhận một mục đạt: người rà phải mở nội dung nguồn, chỉ đúng đoạn giảng ở bài, kiểm ví dụ và điều kiện thuật toán/chứng minh khi nguồn có, rồi kiểm bài tập/đáp án. Một source hash, parser hoặc số file không thay được bước này. Hai cổng hiện đã đóng cho 947 thân mục sách và 458 trang USTH; `manifest.allContentComplete` là true. Nhãn “Đã gán” trong bảng trên mô tả mapping; bằng chứng đối chiếu và hash hiện hành nằm riêng ở [cổng sách](semantic-coverage-status.md) và [cổng slide](slide-semantic-coverage-status.md).

Các báo cáo engine, model và render chỉ mang phạm vi riêng của chúng. Việc chưa có PostgreSQL native, crash/cluster runner hoặc pilot không được che bằng output mẫu.
