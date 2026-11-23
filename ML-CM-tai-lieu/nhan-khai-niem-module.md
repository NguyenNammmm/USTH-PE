# Bảng gắn nhãn khái niệm và module — Python Advanced & SQL

> Nhiệm vụ N36 · Cập nhật ngày 22/11/2026
> 
> Nguồn: `scripts/pe-v4/out-advanced/lessons/*.json` (Python), `frontend/public/static/js/lesson_content.js` & `frontend/src/lib/curricula.json` (SQL)

---

## Python Advanced (48 bài, 8 module)

| Bài | Module | Tên bài | Khái niệm chính (thuật ngữ 2–5 từ) | Tiên quyết thực sự |
|:---|:---|:---|:---|:---|
| P01 | M1 | Program, process và tài nguyên | tiến trình hệ điều hành; mã định danh PID; tiến trình cha PPID; vùng nhớ tiến trình; file descriptor chuẩn | — |
| P02 | M1 | Vòng đời, fork, exec và wait | trạng thái tiến trình; lời gọi fork; thay thế tiến trình exec; chờ tiến trình con wait; tiến trình mồ côi orphan | P01 |
| P03 | M1 | Scheduling và context switch | bộ điều phối scheduler; chuyển ngữ cảnh context switch; hàng đợi điều phối; lát cắt thời gian timeslice | P02 |
| P04 | M1 | stdin, stdout, stderr và pipe | luồng nhập xuất chuẩn; đường ống dẫn pipe; chuyển hướng luồng dữ liệu; bộ đệm dòng tiêu chuẩn | P01 |
| P05 | M1 | subprocess.run và kết quả | tiến trình con subprocess; mã thoát returncode; đối số danh sách; thu thập đầu ra | P04 |
| P06 | M1 | Popen, communicate và timeout | đối tượng Popen; giao tiếp đường ống communicate; thời gian chờ timeout; hủy tiến trình con terminate | P05 |
| P07 | M1 | multiprocessing: Process và Queue | đa tiến trình multiprocessing; hàng đợi liên tiến trình; giao tiếp liên tiến trình; cách ly vùng nhớ | P01, P04 |
| T01 | M2 | Thread, tài nguyên và concurrency | luồng thực thi thread; bộ nhớ heap chung; ngăn xếp stack riêng; thanh ghi luồng riêng; tính toán đồng thời concurrency | P01 |
| T02 | M2 | Thread target, start và join | hàm mục tiêu target; kích hoạt luồng start; chờ hoàn thành join; luồng chính main thread | T01 |
| T03 | M2 | Subclass Thread | kế thừa lớp Thread; ghi đè phương thức run; khởi tạo lớp cha; thuộc tính lưu trạng thái | T02 |
| T04 | M2 | GIL, CPU-bound và I/O-bound | khóa thông dịch viên GIL; tác vụ nghẽn tính toán; tác vụ nghẽn nhập xuất; chia sẻ thời gian luồng | T01 |
| T05 | M2 | Lock, race condition và deadlock | xung đột race condition; khóa đồng bộ hóa Lock; bế tắc luồng deadlock; khối khóa an toàn context | T01 |
| T06 | M2 | Queue và tác vụ lưu nền | hàng đợi an toàn luồng; mô hình sản xuất; giải phóng luồng nghẽn; xử lý tác vụ nền | T05 |
| G01 | M3 | GUI, CLI và cửa sổ | giao diện đồ họa Tkinter; cửa sổ chính root; vòng lặp sự kiện mainloop; kích thước hình học geometry | — |
| G02 | M3 | Widget và callback | thành phần giao diện widget; hàm phản hồi callback; ràng buộc sự kiện bind; hộp thông báo messagebox | G01 |
| G03 | M3 | Dữ liệu nhập và lựa chọn | biến lưu trữ giao diện; ô nhập văn bản Entry; nút bấm lựa chọn Radiobutton; hộp chọn nhiều Checkbutton | G02 |
| G04 | M3 | Layout: pack, place, grid | bố cục đóng gói pack; bố cục lưới grid; neo vị trí sticky; khoảng đệm khoảng cách | G01 |
| G05 | M3 | OOP và tách logic khỏi giao diện | đóng gói hướng đối tượng; tách biệt tầng giao diện; quản lý trạng thái; kế thừa khung giao diện | G02 |
| G06 | M3 | Event loop và worker nền | vòng lặp sự kiện; hẹn giờ phản hồi after; luồng công nhân chạy nền; đồng bộ giao diện | G02, T01 |
| R02 | M3 | Dự án PW5–PW9: lưu, shell, thread và GUI | tích hợp ứng dụng; kết hợp đa tiến trình; kết hợp đa luồng; xử lý dữ liệu | P05, T06 |
| X01 | M4 | Nhập dữ liệu bằng NumPy và pandas | đọc tệp phân tách CSV; ký tự ngăn cách delimiter; chỉ định kiểu dữ liệu; dòng tiêu đề header | — |
| X02 | M4 | Excel, Stata, SAS, HDF5 và MATLAB | tệp dữ liệu Stata; định dạng bảng tính Excel; bảo toàn kiểu gốc; chuyển đổi tệp ngoại vi | X01 |
| X03 | M4 | SQL với sqlite3 và pandas | cơ sở dữ liệu SQLite3; kết nối bộ nhớ tạm; tham số hóa truy vấn; chuyển đổi sang DataFrame | X01 |
| X04 | M4 | Matplotlib: dữ liệu và loại biểu đồ | vùng vẽ đồ họa Figure; hệ trục tọa độ Axes; biểu đồ đường line chart; biểu đồ cột bar chart | X01 |
| X05 | M4 | Matplotlib: tùy chỉnh và xuất | tùy chỉnh nhãn trục; đường mốc tham chiếu ngang; xuất định dạng hình ảnh; độ phân giải DPI | X04 |
| N01 | M5 | Array, dtype, shape và axis | mảng đa chiều ndarray; kiểu dữ liệu đồng nhất; kích thước các chiều shape; trục tổng hợp axis | — |
| N02 | M5 | Indexing, mask và vectorization | chỉ mục mảng đa chiều; mặt nạ lọc logic mask; phép toán vectơ hóa vectorization; lựa chọn mảng con slice | N01 |
| N03 | M5 | Broadcasting và chuẩn hoá dữ liệu | cơ chế lan truyền broadcasting; chuẩn hóa điểm số zscore; giữ nguyên số chiều keepdims; căn chỉnh trục tương thích | N01 |
| N04 | M5 | Thống kê, NaN và trọng số | thống kê bỏ qua khuyết; giá trị khuyết NaN; trung bình có trọng số; độ lệch chuẩn dữ liệu | N01 |
| N05 | M5 | View, copy và sai số số thực | bản nhìn dữ liệu view; bản sao dữ liệu copy; bước nhảy bộ nhớ strides; sai số số thực | N01 |
| N06 | M5 | Đọc dữ liệu và mô phỏng tái lập | đọc mảng số nguyên thủy; tạo số ngẫu nhiên seed; dữ liệu tái lập; kiểm tra tính hợp lệ | N01 |
| PD01 | M6 | Series, DataFrame và index | cột dữ liệu Series; bảng dữ liệu DataFrame; chỉ mục dòng index; truy cập theo nhãn loc; truy cập vị trí iloc | N01 |
| PD02 | M6 | CSV, Excel và schema | lược đồ dữ liệu schema; suy luận kiểu tự động; đặc tả cột kiểu chuỗi; kiểm tra tính toàn vẹn | PD01 |
| PD03 | M6 | Làm sạch thiếu, trùng và sai kiểu | xử lý giá trị khuyết; phát hiện dòng trùng lặp; chuyển đổi kiểu dữ liệu; lọc dữ liệu ngoại lai | PD01 |
| PD04 | M6 | Lọc, tính cột và cập nhật an toàn | lọc dòng theo điều kiện; cập nhật cột an toàn; gán dữ liệu qua nhãn; cảnh báo sao chép ngầm | PD01 |
| PD05 | M6 | GroupBy và KPI có mẫu số rõ ràng | phân nhóm dữ liệu groupby; tính toán chỉ số KPI; hàm tổng hợp nhóm agg; biến đổi theo nhóm transform | PD04 |
| PD06 | M6 | Merge, concat và kiểm tra cardinality | kết nối bảng merge; nối tầng dữ liệu concat; quan hệ lực lượng cardinality; phương thức kết nối join | PD01 |
| PD07 | M6 | Long, wide, pivot và melt | xoay bảng dữ liệu pivot; làm phẳng bảng melt; dữ liệu dạng rộng wide; dữ liệu dạng dài long | PD01 |
| PD08 | M6 | Ngày giờ, resample và rolling | chỉ mục thời gian DatetimeIndex; lấy mẫu lại chuỗi resample; cửa sổ trượt rolling; khoảng thời gian tần suất | PD01 |
| PD09 | M6 | EDA, chất lượng dữ liệu và export | khám phá dữ liệu EDA; chất lượng dữ liệu; chuẩn hóa phân phối; xuất báo cáo tổng kết | PD03, PD05 |
| M01 | M7 | Figure, Axes và chọn biểu đồ | khung chứa đồ họa Figure; vùng biểu đồ Axes; lưới biểu đồ con subplots; chuỗi thời gian | — |
| M02 | M7 | Phân bố, scatter và outlier | biểu đồ phân tán scatter; biểu đồ hộp boxplot; điểm dị biệt ngoại lai; phân bố tần suất histogram | M01 |
| M03 | M7 | Subplot và heatmap đọc được | ma trận nhiệt heatmap; chia vùng hiển thị subplots; thanh đo mức độ colormap; tỷ lệ khung hình | M01 |
| M04 | M7 | Màu, annotation và kể chuyện dữ liệu | chú thích dữ liệu annotate; bảng màu trực quan; đường nét đồ họa linestyle; tiêu đề nhãn đơn vị | M01 |
| M05 | M7 | Ticks, scale và ngày trên trục | định dạng vạch chia formatter; thang đo trục logarit; giới hạn vùng nhìn trục; định dạng nhãn ngày tháng | M01 |
| M06 | M7 | Layout, xuất hình và kiểm tra chất lượng | tự động bố cục tight_layout; độ phân giải DPI; đóng vùng vẽ giải phóng; xuất tập tin ảnh | M01 |
| DA01 | M8 | Mini-project: doanh thu từ raw tới chart | mức độ hạt grain; đối soát số lượng dòng; đường ống dữ liệu pipeline; tỷ số tổng KPI | PD05, M01 |
| DA02 | M8 | Mini-project: điểm số và GPA | phân loại dữ liệu thiếu; xử lý lỗi ngoài khoảng; trung bình tích lũy GPA; bảng báo cáo tổng hợp | DA01 |

---

## SQL / Database Design (20 bài, 3 module theo curricula.json)

| Bài | Module (Mã & Tên theo curricula.json) | Tên bài | Khái niệm chính (thuật ngữ 2–5 từ) | Tiên quyết thực sự |
|:---|:---|:---|:---|:---|
| db_01 | Module 1: ER Model & Mapping | Entity Set & Primary Key | tập thực thể Entity Set; khóa chính Primary Key; định danh duy nhất; toàn vẹn thực thể | — |
| db_02 | Module 1: ER Model & Mapping | Composite, Multivalued & Derived Attributes | thuộc tính phức hợp composite; thuộc tính đa trị multivalued; thuộc tính dẫn xuất derived; nguyên tử hóa thuộc tính | db_01 |
| db_03 | Module 1: ER Model & Mapping | Foreign Key & JOIN | khóa ngoại Foreign Key; phép nối hai bảng JOIN; toàn vẹn tham chiếu bảng; điều kiện nối bằng nhau | db_01 |
| db_04 | Module 1: ER Model & Mapping | Foreign Key & Mối quan hệ 1:N | quan hệ một nhiều 1:N; khóa ngoại phía nhiều; ràng buộc NOT NULL; quan hệ cha con | db_03 |
| db_19 | Module 1: ER Model & Mapping | Mối quan hệ M:N & Bảng trung gian | quan hệ nhiều nhiều M:N; bảng trung gian liên kết; khóa chính tổng hợp composite; phân rã quan hệ | db_03 |
| db_05 | Module 1: ER Model & Mapping | Weak Entity & Khóa chính tổng hợp | thực thể yếu Weak Entity; mối quan hệ xác định; khóa riêng phần partial key; khóa chính phụ thuộc | db_01 |
| db_06 | Module 1: ER Model & Mapping | Mapping ER → Bảng quan hệ | ánh xạ lược đồ; thực thể thành bảng; quan hệ thành khóa; thiết kế bảng cơ sở | db_01, db_03 |
| db_07 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | Redundancy & Phụ thuộc hàm (FD) | dư thừa dữ liệu redundancy; phụ thuộc hàm functional dependency; dị thường thêm sửa xóa; xác định hàm duy nhất | db_01 |
| db_08 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | Dạng chuẩn 1 (1NF) — Atomic Domains | dạng chuẩn một 1NF; miền giá trị nguyên tử; loại bỏ mảng lồng nhau; cấu trúc bảng phẳng | db_07 |
| db_09 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | Dạng chuẩn 2 (2NF) — Phụ thuộc đầy đủ | dạng chuẩn hai 2NF; phụ thuộc hàm đầy đủ; khử phụ thuộc bộ phận; tách bảng theo khóa phụ | db_08 |
| db_11 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | Dạng chuẩn 3 (3NF) & Sự thỏa hiệp | dạng chuẩn ba 3NF; phụ thuộc hàm bắc cầu; thuộc tính không khóa; dư thừa bắc cầu | db_09 |
| db_10 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | BCNF & Phân rã Phi tổn thất | dạng chuẩn Boyce Codd BCNF; điều kiện siêu khóa superkey; phân rã phi tổn thất; chuẩn hóa nghiêm ngặt | db_11 |
| db_12 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | 4NF — Phụ thuộc đa trị | dạng chuẩn bốn 4NF; phụ thuộc đa trị MVD; tách dữ liệu độc lập; khử dư thừa tổ hợp | db_10 |
| db_13 | Module 2: Phụ thuộc hàm & Chuẩn hóa (FD & Normal Forms) | Boss Battle — Siêu hệ thống chuẩn hóa | quy trình chuẩn hóa; phân rã bảng phức tạp; bảo toàn thông tin; thiết kế cơ sở | db_10 |
| db_14 | Module 3: Application Design | JSON trong Database — Path Expressions | kiểu dữ liệu JSONB; toán tử trích xuất; toán tử đối tượng; chỉ mục linh hoạt | db_01 |
| db_15 | Module 3: Application Design | Spatial Data — Dữ liệu Không gian | dữ liệu không gian spatial; tọa độ địa lý POINT; tính toán khoảng cách ST_Distance; truy vấn không gian | db_01 |
| db_16 | Module 3: Application Design | ORM (Django) — Ánh xạ Class ↔ Table | ánh xạ đối tượng ORM; lớp mô hình Model; tối ưu truy vấn; truy vấn hướng đối tượng | db_03 |
| db_20 | Module 3: Application Design | Web Services — REST/AJAX | dịch vụ mạng RESTful API; phương thức yêu cầu HTTP; định dạng truyền tải JSON; tầng ứng dụng trung gian | db_01 |
| db_17 | Module 3: Application Design | SQL Injection — Lỗ hổng chết người | tiêm mã SQL Injection; truy vấn tham số hóa; phân tách dữ liệu; bảo mật tầng dữ liệu | db_01 |
| db_18 | Module 3: Application Design | Password Security — Salt & Hashing | mã băm mật khẩu hashing; muối ngẫu nhiên cryptographic salt; thuật toán băm chậm; chống tấn công dò bảng | db_17 |

---

### Lý do sư phạm chọn bài tiên quyết cho Boss Battle & Module 3

1. **`db_13` (Boss Battle — Siêu hệ thống chuẩn hóa, Bài 14)** $ightarrow$ **Tiên quyết: `db_10` (BCNF)**
   - *Lý do:* Boss Battle yêu cầu phân rã thực chiến một bảng phức tạp qua toàn bộ các cấp độ chuẩn hóa đến BCNF, nên người học bắt buộc phải nắm vững dạng chuẩn BCNF (ở bài db_10) trước khi làm bài tổng hợp này.
2. **`db_14` (JSON trong Database — Path Expressions, Bài 15)** $ightarrow$ **Tiên quyết: `db_01` (Entity Set & Primary Key)**
   - *Lý do:* Truy vấn cột JSONB thực hiện trên bảng người dùng đơn lẻ; người học chỉ cần nắm vững cấu trúc bảng có khóa chính và câu lệnh SELECT cơ bản từ db_01 để áp dụng toán tử trích xuất `->>`.
3. **`db_15` (Spatial Data — Dữ liệu Không gian, Bài 16)** $ightarrow$ **Tiên quyết: `db_01` (Entity Set & Primary Key)**
   - *Lý do:* Bài toán tìm chi nhánh trong bán kính 10km thực chất là lọc điều kiện không gian trên bảng cửa hàng đơn lẻ của db_01, không cần quan hệ bảng phức tạp.
4. **`db_16` (ORM Django — Ánh xạ Class ↔ Table, Bài 17)** $ightarrow$ **Tiên quyết: `db_03` (Foreign Key & JOIN)**
   - *Lý do:* ORM ánh xạ khóa ngoại thành liên kết đối tượng và method `select_related` ánh xạ trực tiếp thành câu lệnh SQL JOIN; bắt buộc phải hiểu bản chất JOIN ở db_03 mới hiểu được cơ chế hoạt động của ORM.
5. **`db_20` (Web Services — REST/AJAX, Bài 18)** $ightarrow$ **Tiên quyết: `db_01` (Entity Set & Primary Key)**
   - *Lý do:* Endpoint REST API đóng gói câu lệnh truy vấn lọc danh mục game theo điều kiện WHERE từ bảng catalog của db_01 để trả dữ liệu JSON cho frontend.
6. **`db_17` (SQL Injection — Lỗ hổng chết người, Bài 19)** $ightarrow$ **Tiên quyết: `db_01` (Entity Set & Primary Key)**
   - *Lý do:* SQL Injection khai thác cơ chế xác thực tài khoản qua mệnh đề WHERE `username = '...'` trên bảng user đơn lẻ của db_01, cần hiểu cách truy vấn tài khoản trước khi tìm hiểu cách bẻ gãy nó.
7. **`db_18` (Password Security — Salt & Hashing, Bài 20)** $ightarrow$ **Tiên quyết: `db_17` (SQL Injection)**
   - *Lý do:* Sau khi thấy rõ nguy cơ bảng mật khẩu bị trích xuất qua lỗ hổng tiêm mã ở bài db_17, người học được dẫn dắt tự nhiên sang bài db_18 để hiểu tại sao bắt buộc phải dùng thuật toán băm có muối (salt) bảo vệ tầng sâu.
