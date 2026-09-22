# Ma trận kiểm tra sau bổ sung

Đã biên soạn bài học và tiêu chí đánh giá cho **237/237 mục đã kiểm kê (100% về ánh xạ nội dung)**. Có 92 bài: 24 bài P giữ lại, 68 bài mới; 59 core và 33 advanced. Danh sách thiếu ban đầu gồm 189 mục chưa đủ trong P01-P24. Các ticket E được triển khai thành bài cụ thể, không còn dùng outline làm bằng chứng hoàn thành.

**Giới hạn kết luận:** đây không phải khẳng định học viên nắm 100% sách, cũng không phải 100% mã đã chạy trên mọi môi trường. Đơn vị là cụm chủ đề/recipe đã định nghĩa trong kiểm toán trước; mọi API, biến thể và ví dụ nhỏ ngoài danh sách này chưa được kiểm kê riêng. Một bài có thể phục vụ nhiều mục trùng nhau.

| Nguồn | Mục | P01-P24: đủ hoàn toàn | Điểm quy đổi P | P+E outline | Sau: có bài + tiêu chí |
|---|---:|---:|---:|---:|---:|
| SL | 112 | 21 | 33.0% | 38.8% | 112/112 |
| HF | 36 | 16 | 65.3% | 65.3% | 36/36 |
| GUI | 89 | 11 | 20.8% | 35.4% | 89/89 |

Điểm quy đổi trước = (đủ + 0.5 × một phần)/số mục. Cột sau dùng tiêu chí có hoạt động và đánh giá được biên soạn, không dùng kết quả runtime để suy ra độ phủ. Không lấy trung bình ba phần trăm do độ hạt và nội dung trùng nhau.

## Các chuyển đổi cần đọc trước khi duyệt

- R064: Giữ so sánh CreateProcess/WinExec ở mức cơ chế; bài Python dùng subprocess. Không tuyên bố có lab lập trình trực tiếp Win32 API.
- R076: Phân tích kiến trúc lịch sử trong slide; không xem đó là mô tả Apache/Chromium hiện tại.
- R077: Giới hạn phát biểu GIL theo CPython build có GIL; không khái quát mọi Python.
- R183: Dùng pip và đọc wheel phù hợp interpreter hiện tại; không cài wheel Python cũ của sách.
- R215: Giữ workflow khám phá/chạy/debug unittest trong IDE; cho phép VS Code thay Eclipse PyDev.
- R219: Phân tích thử nghiệm nhúng wx vào Tk và nguyên nhân loop bị chặn trong sách. Giải pháp chạy kèm là hai process, không phải embedding widget.
- R220: Phân tích thử nghiệm nhúng Tk vào wx và giới hạn vòng đời/main thread. Không tuyên bố đã tạo embedding native di động.
- R221: Điều phối hai GUI bằng process riêng và JSON line; khác thiết kế chung process trong thử nghiệm cũ.
- R222: Giao tiếp hai chiều qua IPC có protocol nghiệm thu; chưa nghiệm thu toàn bộ hai GUI native.
- R223: PyOpenGL compatibility context; không dùng fixed-function API trong core profile.
- R224: Cube 3D và tương tác wx cần compatibility context thực và kiểm tra thủ công.
- R226: Chuyển ví dụ pyglet cũ sang ShaderProgram; giữ mục tiêu tạo cửa sổ/render bằng OpenGL.
- R227: Màu theo vertex và shader; không sao chép API pyglet 2017.
- R228: Tách kiểm thử hàm chuyển động khỏi nghiệm thu hoạt ảnh native theo dt.

## Truy vết từng mục

Mỗi hàng dẫn tới bài, trang PDF và ca đánh giá. Nội dung challenge, guided, rubric, trạng thái runtime chi tiết có trong coverage_after.json. Bài P dùng test gốc cùng protocol manual; PASS tự động không thay thế các protocol ấy.

| Mục | Nguồn/trang PDF nguồn | Chủ đề | Trước P / P+E | Bài mới hoặc giữ lại (trang PDF v2) | Ca đánh giá |
|---|---|---|---|---|---|
| R001 | SL 4-19 | Đặc trưng, ứng dụng và giới hạn Python | 0 / 0 | C01 (tr.6) | C01: C01-K01, C01-K02, C01-K03 |
| R002 | SL 19-21 | Phiên bản, môi trường ảo và cài package | 0 / 0 | C01 (tr.6) | C01: C01-K01, C01-K02, C01-K03 |
| R003 | SL 22-25 | IDE, Jupyter và thao tác notebook | 0 / 0 | C02 (tr.7) | C02: C02-K01, C02-K02 |
| R004 | SL 28 | Chạy tương tác so với script | 0.5 / 0.5 | C02 (tr.7); P01 (tr.9) | C02: C02-K01, C02-K02; P01: P01-a, P01-b, P01-c |
| R005 | SL 96 | Git và GitHub workflow | 0 / 0.5 | C03 (tr.8) | C03: C03-K01, C03-K02 |
| R006 | SL 29-31 | Literal, biến và phép gán | 1 / 1 | X01 (tr.64); P01 (tr.9); P02 (tr.10) | X01: X01-K01, X01-K02; P01: P01-a, P01-b, P01-c; P02: P02-a, P02-b, P02-c |
| R007 | SL 32-33 | Tên biến hợp lệ và từ khóa dành riêng | 0 / 0 | C04 (tr.11) | C04: C04-K01, C04-K02 |
| R008 | SL 34-36 | Toán tử số và thứ tự tính | 0.5 / 0.5 | C05 (tr.12); P02 (tr.10); P23 (tr.47) | C05: C05-K01, C05-K02; P02: P02-a, P02-b, P02-c; P23: P23-a, P23-b, P23-c, P23-d |
| R009 | SL 38-45 | Kiểu int/float/bool/str và dynamic typing | 0.5 / 0.5 | C04 (tr.11); P02 (tr.10); P04 (tr.15); P13 (tr.34) | C04: C04-K01, C04-K02; P02: P02-a, P02-b, P02-c; P04: P04-a, P04-b, P04-c, P04-d; P13: P13-a, P13-b, P13-c, P13-d, P13-e, P13-f |
| R010 | SL 44-45 | Chuyển đổi giữa chuỗi và số | 1 / 1 | X01 (tr.64); P02 (tr.10); P13 (tr.34) | X01: X01-K01, X01-K02; P02: P02-a, P02-b, P02-c; P13: P13-a, P13-b, P13-c, P13-d, P13-e, P13-f |
| R011 | SL 46 | Nối và lặp chuỗi | 1 / 1 | P01 (tr.9); P02 (tr.10) | P01: P01-a, P01-b, P01-c; P02: P02-a, P02-b, P02-c |
| R012 | SL 47-48 | Indexing và slicing chuỗi | 0 / 0 | C07 (tr.17); P03 (tr.13) | C07: C07-K01, C07-K02; P03: P03-a, P03-b, P03-c |
| R013 | SL 49 | Định dạng chuỗi | 0.5 / 0.5 | C06 (tr.14); P23 (tr.47) | C06: C06-K01, C06-K02; P23: P23-a, P23-b, P23-c, P23-d |
| R014 | SL 50-51,61 | Comment và docstring | 0 / 0 | C04 (tr.11) | C04: C04-K01, C04-K02 |
| R015 | SL 53-54 | Thụt lề và khối lệnh | 1 / 1 | P04 (tr.15); P08 (tr.24) | P04: P04-a, P04-b, P04-c, P04-d; P08: P08-a, P08-b, P08-c, P08-d |
| R016 | SL 55 | if/else | 1 / 1 | P04 (tr.15) | P04: P04-a, P04-b, P04-c, P04-d |
| R017 | SL 56-57 | Nhánh lồng nhau và elif | 0.5 / 0.5 | C12 (tr.35); P24 (tr.49) | C12: C12-K01, C12-K02; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R018 | SL 58-61 | Định nghĩa/gọi hàm, tham số, return | 1 / 1 | X01 (tr.64); P10 (tr.28) | X01: X01-K01, X01-K02; P10: P10-a, P10-b, P10-c, P10-d |
| R019 | SL 62 | Hàm dựng sẵn len/print và input | 0.5 / 0.5 | C12 (tr.35); P01 (tr.9); P07 (tr.21); P10 (tr.28) | C12: C12-K01, C12-K02; P01: P01-a, P01-b, P01-c; P07: P07-a, P07-b, P07-c; P10: P10-a, P10-b, P10-c, P10-d |
| R020 | SL 64-67,81 | Chọn collection, tính có thứ tự và thay đổi được | 0.5 / 0.5 | C10 (tr.22); P05 (tr.16); P07 (tr.21) | C10: C10-K01, C10-K02; P05: P05-a, P05-b, P05-c; P07: P07-a, P07-b, P07-c |
| R021 | SL 65 | Set và loại phần tử trùng | 1 / 1 | P07 (tr.21) | P07: P07-a, P07-b, P07-c |
| R022 | SL 68-70 | List append và nối/extend | 0.5 / 0.5 | C08 (tr.18); P05 (tr.16) | C08: C08-K01, C08-K02; P05: P05-a, P05-b, P05-c |
| R023 | SL 71-76 | List indexing/slicing và cập nhật đoạn | 0 / 0 | C07 (tr.17) | C07: C07-K01, C07-K02 |
| R024 | SL 77-78 | List xóa phần tử | 0 / 0 | C08 (tr.18) | C08: C08-K01, C08-K02 |
| R025 | SL 79-80,93 | range và quy tắc start/stop/step | 0 / 0 | C11 (tr.27); P08 (tr.24) | C11: C11-K01, C11-K02; P08: P08-a, P08-b, P08-c, P08-d |
| R026 | SL 81-82 | Tuple tạo và unpack | 1 / 1 | C10 (tr.22); P07 (tr.21); P23 (tr.47) | C10: C10-K01, C10-K02; P07: P07-a, P07-b, P07-c; P23: P23-a, P23-b, P23-c, P23-d |
| R027 | SL 83-86 | Dict tạo/tra cứu/gán theo khóa | 1 / 1 | X01 (tr.64); P06 (tr.19); P24 (tr.49) | X01: X01-K01, X01-K02; P06: P06-a, P06-b, P06-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R028 | SL 85-87 | Dict pop/keys/values/items | 0 / 0 | C09 (tr.20) | C09: C09-K01, C09-K02 |
| R029 | SL 88-89,94 | for và biến tích lũy | 1 / 1 | X01 (tr.64); P08 (tr.24) | X01: X01-K01, X01-K02; P08: P08-a, P08-b, P08-c, P08-d |
| R030 | SL 90 | while và điều kiện dừng | 1 / 1 | X01 (tr.64); P09 (tr.26) | X01: X01-K01, X01-K02; P09: P09-a, P09-b, P09-c, P09-d |
| R031 | SL 91-92 | break/continue | 0 / 0 | C11 (tr.27); P09 (tr.26) | C11: C11-K01, C11-K02; P09: P09-a, P09-b, P09-c, P09-d |
| R032 | SL 107-113 | Class/instance, khởi tạo và self | 1 / 1 | X02 (tr.93); P15 (tr.40) | X02: X02-K01, X02-K02; P15: P15-a, P15-b, P15-c |
| R033 | SL 114 | Phương thức so sánh __lt__ | 0 / 0 | C20 (tr.42) | C20: C20-K01, C20-K02 |
| R034 | SL 115-117 | Biểu diễn __str__ | 0 / 0 | C20 (tr.42) | C20: C20-K01, C20-K02 |
| R035 | SL 118-120 | Kế thừa đơn | 1 / 1 | X02 (tr.93); P16 (tr.41) | X02: X02-K01, X02-K02; P16: P16-a, P16-b, P16-c |
| R036 | SL 121-122 | isinstance và issubclass | 0.5 / 0.5 | C20 (tr.42); P16 (tr.41); P24 (tr.49) | C20: C20-K01, C20-K02; P16: P16-a, P16-b, P16-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R037 | SL 123-124 | Đa kế thừa | 0 / 0 | A01 (tr.65) | A01: A01-K01, A01-K02 |
| R038 | SL 125-127 | Override và đa hình | 1 / 1 | X02 (tr.93); P16 (tr.41) | X02: X02-K01, X02-K02; P16: P16-a, P16-b, P16-c |
| R039 | SL 128-131 | Encapsulation, underscore và accessor | 0 / 0 | C20 (tr.42) | C20: C20-K01, C20-K02 |
| R040 | SL 101-106 | OOP review: abstract class và type conformance | 0 / 0 | A01 (tr.65) | A01: A01-K01, A01-K02 |
| R041 | SL 136-139,151 | Tạo module và tái cấu trúc nhiều file | 0.5 / 1 | C19 (tr.32); X02 (tr.93); P11 (tr.31) | C19: C19-K01, C19-K02; X02: X02-K01, X02-K02; P11: P11-a, P11-b, P11-c |
| R042 | SL 140-141 | import và from-import | 1 / 1 | P11 (tr.31) | P11: P11-a, P11-b, P11-c |
| R043 | SL 142 | Import alias | 0.5 / 0.5 | C19 (tr.32); P17 (tr.43) | C19: C19-K01, C19-K02; P17: rubric/manual |
| R044 | SL 143-148 | Package và package lồng nhau | 0 / 0.5 | C19 (tr.32); X02 (tr.93) | C19: C19-K01, C19-K02; X02: X02-K01, X02-K02 |
| R045 | SL 150 | math.floor và làm tròn xuống 1 chữ số | 0 / 0 | C05 (tr.12); X02 (tr.93); P23 (tr.47) | C05: C05-K01, C05-K02; X02: X02-K01, X02-K02; P23: P23-a, P23-b, P23-c, P23-d |
| R046 | SL 150 | NumPy array và GPA có trọng số | 0.5 / 1 | A02 (tr.66); X02 (tr.93); P11 (tr.31) | A02: A02-K01, A02-K02; X02: X02-K01, X02-K02; P11: P11-a, P11-b, P11-c |
| R047 | SL 150 | Sắp sinh viên theo GPA giảm dần | 0 / 0 | A02 (tr.66); X02 (tr.93); P24 (tr.49) | A02: A02-K01, A02-K02; X02: X02-K01, X02-K02; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R048 | SL 150-151 | Curses UI | 0 / 1 | A03 (tr.67); X02 (tr.93) | A03: A03-K01, A03-K02; X02: X02-K01, X02-K02 |
| R049 | SL 155-157 | File tồn tại qua lần chạy so với RAM | 1 / 1 | X03 (tr.94); X06 (tr.97); P14 (tr.37); P24 (tr.49) | X03: X03-K01, X03-K02; X06: X06-K01, X06-K02, X06-K03; P14: P14-a, P14-b, P14-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R050 | SL 158-160 | open và các chế độ r/w/a/b/+ | 0.5 / 0.5 | C21 (tr.38); P12 (tr.33); P14 (tr.37) | C21: C21-K01, C21-K02; P12: P12-a, P12-b, P12-c; P14: P14-a, P14-b, P14-c |
| R051 | SL 161-163 | Đọc/ghi, read/readline/readlines | 0.5 / 0.5 | C21 (tr.38); P12 (tr.33); P14 (tr.37) | C21: C21-K01, C21-K02; P12: P12-a, P12-b, P12-c; P14: P14-a, P14-b, P14-c |
| R052 | SL 164-165 | Buffering | 0 / 0 | C21 (tr.38) | C21: C21-K01, C21-K02 |
| R053 | SL 166-167 | Đóng file và with | 1 / 1 | P12 (tr.33); P14 (tr.37) | P12: P12-a, P12-b, P12-c; P14: P14-a, P14-b, P14-c |
| R054 | SL 169-170 | Xử lý ngoại lệ I/O | 0.5 / 0.5 | C21 (tr.38); P14 (tr.37) | C21: C21-K01, C21-K02; P14: P14-a, P14-b, P14-c |
| R055 | SL 171-172 | File tạm | 0 / 0 | C21 (tr.38) | C21: C21-K01, C21-K02 |
| R056 | SL 173-178,191 | Nén dữ liệu | 0 / 1 | A04 (tr.68); X03 (tr.94) | A04: A04-K01, A04-K02; X03: X03-K01, X03-K02 |
| R057 | SL 179-181,192 | Pickle serialization và giới hạn kiểu | 0 / 1 | A05 (tr.69); X03 (tr.94) | A05: A05-K01, A05-K02; X03: X03-K01, X03-K02 |
| R058 | SL 182 | So sánh pickle/JSON | 0.5 / 1 | A05 (tr.69); X03 (tr.94); P14 (tr.37) | A05: A05-K01, A05-K02; X03: X03-K01, X03-K02; P14: P14-a, P14-b, P14-c |
| R059 | SL 183-188 | Cấu trúc thư mục và duyệt file | 0 / 0.5 | C22 (tr.39) | C22: C22-K01, C22-K02 |
| R060 | SL 187-188 | Tạo/xóa thư mục và thao tác filesystem | 0 / 0 | C22 (tr.39) | C22: C22-K01, C22-K02 |
| R061 | SL 196-206 | Program/process và không gian chạy riêng | 0.5 / 0.5 | A06 (tr.84); P22 (tr.83) | A06: A06-K01, A06-K02; P22: P22-a, P22-b |
| R062 | SL 207-208 | Trạng thái tiến trình | 0 / 0 | A06 (tr.84) | A06: A06-K01, A06-K02 |
| R063 | SL 209-210 | Cây tiến trình và tạo tiến trình con | 0.5 / 0.5 | A06 (tr.84); P22 (tr.83) | A06: A06-K01, A06-K02; P22: P22-a, P22-b |
| R064 | SL 211-213 | Tạo tiến trình Windows | 0 / 0 | A08 (tr.86) | A08: A08-K01, A08-K02 |
| R065 | SL 214-221 | fork/exec trên UNIX | 0 / 0 | A08 (tr.86); P22 (tr.83) | A08: A08-K01, A08-K02; P22: P22-a, P22-b |
| R066 | SL 222-225 | Mục tiêu lập lịch, preemption | 0 / 0 | A07 (tr.85) | A07: A07-K01, A07-K02 |
| R067 | SL 226-228 | Context switch và PCB | 0 / 0 | A06 (tr.84) | A06: A06-K01, A06-K02 |
| R068 | SL 229-235 | Scheduler, hàng đợi và thuật toán | 0 / 0 | A07 (tr.85) | A07: A07-K01, A07-K02 |
| R069 | SL 236-240 | stdin/stdout/stderr và redirection | 0.5 / 0.5 | A09 (tr.87); X04 (tr.95); P22 (tr.83) | A09: A09-K01, A09-K02; X04: X04-K01, X04-K02; P22: P22-a, P22-b |
| R070 | SL 241-245 | subprocess run/wait và returncode | 1 / 1 | X04 (tr.95); P22 (tr.83) | X04: X04-K01, X04-K02; P22: P22-a, P22-b |
| R071 | SL 245 | Background/Popen, pipe, timeout/terminate | 0.5 / 0.5 | A09 (tr.87); X04 (tr.95); P22 (tr.83) | A09: A09-K01, A09-K02; X04: X04-K01, X04-K02; P22: P22-a, P22-b |
| R072 | SL 247-248 | Shell tương tác | 0 / 0 | X04 (tr.95); P22 (tr.83) | X04: X04-K01, X04-K02; P22: P22-a, P22-b |
| R073 | SL 251-264 | Thread/process, bộ nhớ chia sẻ và stack riêng | 0.5 / 0.5 | A10 (tr.88); P21 (tr.82); P22 (tr.83) | A10: A10-K01, A10-K02; P21: P21-a, P21-b, P21-c; P22: P22-a, P22-b |
| R074 | SL 265-272 | Responsiveness, hiệu năng và scalability | 0.5 / 0.5 | A10 (tr.88); P21 (tr.82) | A10: A10-K01, A10-K02; P21: P21-a, P21-b, P21-c |
| R075 | SL 273 | Nondeterminism và lỗi tranh chấp | 0 / 0 | A11 (tr.89) | A11: A11-K01 |
| R076 | SL 274-276 | Kiến trúc Apache/Chromium | 0 / 0 | A10 (tr.88) | A10: A10-K01, A10-K02 |
| R077 | SL 278-286 | GIL và concurrency một/nhiều core | 0 / 0 | A10 (tr.88) | A10: A10-K01, A10-K02 |
| R078 | SL 287-291 | Subclass Thread | 0 / 0 | A12 (tr.90); P21 (tr.82) | A12: A12-K01, A12-K02; P21: P21-a, P21-b, P21-c |
| R079 | SL 292-295 | Thread target/start/join | 1 / 1 | P21 (tr.82) | P21: P21-a, P21-b, P21-c |
| R080 | SL 296-297 | Lock/mutex | 0 / 0 | A11 (tr.89) | A11: A11-K01 |
| R081 | SL 299 | Lưu pickle+nén trong background thread | 0 / 0.5 | X05 (tr.96); X06 (tr.97); P21 (tr.82) | X05: X05-K01, X05-K02; X06: X06-K01, X06-K02, X06-K03; P21: P21-a, P21-b, P21-c |
| R082 | SL 302-307 | CLI/GUI và so sánh toolkit | 0.5 / 0.5 | T01 (tr.50); P17 (tr.43) | T01: T01-K01; P17: rubric/manual |
| R083 | SL 309 | Cửa sổ, title và subwindow/size | 0.5 / 0.5 | T01 (tr.50); P17 (tr.43) | T01: T01-K01; P17: rubric/manual |
| R084 | SL 310-311 | Widget container/Frame | 0.5 / 0.5 | T03 (tr.52); P17 (tr.43) | T03: T03-K01; P17: rubric/manual |
| R085 | SL 312-313 | Button và Entry | 1 / 1 | X06 (tr.97); P17 (tr.43); P18 (tr.44) | X06: X06-K01, X06-K02, X06-K03; P17: rubric/manual; P18: rubric/manual |
| R086 | SL 314 | Radiobutton | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R087 | SL 315 | Listbox | 0 / 0 | T02 (tr.51); P24 (tr.49) | T02: T02-K01; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R088 | SL 316 | Combobox | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R089 | SL 318-319 | Layout pack | 0 / 0 | T03 (tr.52) | T03: T03-K01 |
| R090 | SL 320-321 | Layout place | 0 / 0 | T03 (tr.52) | T03: T03-K01 |
| R091 | SL 322-324 | Layout grid | 1 / 1 | X06 (tr.97); P17 (tr.43) | X06: X06-K01, X06-K02, X06-K03; P17: rubric/manual |
| R092 | SL 325 | Event loop | 0.5 / 0.5 | T07 (tr.56); X06 (tr.97); P17 (tr.43); P18 (tr.44) | T07: T07-K01; X06: X06-K01, X06-K02, X06-K03; P17: rubric/manual; P18: rubric/manual |
| R093 | SL 328 | Nhập file bằng NumPy | 0 / 0 | A14 (tr.70) | A14: A14-K01 |
| R094 | SL 328 | Pandas CSV và khám phá DataFrame | 0 / 0 | A15 (tr.71) | A15: A15-K01, A15-K02 |
| R095 | SL 328 | Excel bằng pandas | 0 / 0 | A15 (tr.71) | A15: A15-K01, A15-K02 |
| R096 | SL 328 | SAS/Stata/HDF5/Matlab | 0 / 0 | A16 (tr.72) | A16: A16-K01 |
| R097 | SL 328 | SQLAlchemy/pandas đọc DB | 0 / 0 | A15 (tr.71) | A15: A15-K01, A15-K02 |
| R098 | SL 328 | Thao tác filesystem bổ sung: cwd/rename | 0 / 0 | C22 (tr.39) | C22: C22-K01, C22-K02 |
| R099 | SL 329 | Figure/axes và nhiều subplot | 0.5 / 0.5 | A17 (tr.73); P19 (tr.45) | A17: A17-K01; P19: P19-a, P19-b, P19-c |
| R100 | SL 329 | Nhóm plot line/scatter/bar | 0.5 / 0.5 | A17 (tr.73); P19 (tr.45) | A17: A17-K01; P19: P19-a, P19-b, P19-c |
| R101 | SL 329 | Phân phối: histogram/box/violin | 0 / 0 | A17 (tr.73) | A17: A17-K01 |
| R102 | SL 329 | Image/2D/vector fields | 0 / 0 | A17 (tr.73) | A17: A17-K01 |
| R103 | SL 329 | Nhãn/limits/legend/ticks/styles | 0.5 / 0.5 | A17 (tr.73); P19 (tr.45) | A17: A17-K01; P19: P19-a, P19-b, P19-c |
| R104 | SL 329 | Lưu/hiển thị/đóng biểu đồ | 0.5 / 0.5 | A17 (tr.73); P19 (tr.45); P24 (tr.49) | A17: A17-K01; P19: P19-a, P19-b, P19-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R105 | SL 330 | String lower/title/zfill/splitlines | 0 / 0 | C06 (tr.14); P23 (tr.47) | C06: C06-K01, C06-K02; P23: P23-a, P23-b, P23-c, P23-d |
| R106 | SL 330 | Dict min/max theo giá trị | 0 / 0 | C09 (tr.20) | C09: C09-K01, C09-K02 |
| R107 | SL 330 | Regex search/sub | 0 / 0 | C16 (tr.36) | C16: C16-K01, C16-K02 |
| R108 | SL 330 | List comprehension | 0.5 / 0.5 | C14 (tr.25); P21 (tr.82) | C14: C14-K01, C14-K02, C14-K03; P21: P21-a, P21-b, P21-c |
| R109 | SL 330 | enumerate và zip | 0.5 / 0.5 | C14 (tr.25); P11 (tr.31) | C14: C14-K01, C14-K02, C14-K03; P11: P11-a, P11-b, P11-c |
| R110 | SL 330 | datetime/timedelta/parse/format | 0 / 0 | C16 (tr.36) | C16: C16-K01, C16-K02 |
| R111 | SL 330 | random | 0 / 0 | C15 (tr.30) | C15: C15-K01, C15-K02 |
| R112 | SL 330 | Counter và most_common | 0 / 0 | C14 (tr.25); P07 (tr.21) | C14: C14-K01, C14-K02, C14-K03; P07: P07-a, P07-b, P07-c |
| R113 | HF 5-14 | Cài Python/VS Code/extensions | 0 / 0 | C01 (tr.6) | C01: C01-K01, C01-K02, C01-K03 |
| R114 | HF 28-48,100-101 | REPL/notebook, kernel và quản lý cell | 0 / 0 | C02 (tr.7) | C02: C02-K01, C02-K02 |
| R115 | HF 20-43 | Đọc/dự đoán/chạy chương trình ngắn | 1 / 1 | P01 (tr.9); P04 (tr.15); P08 (tr.24) | P01: P01-a, P01-b, P01-c; P04: P04-a, P04-b, P04-c, P04-d; P08: P08-a, P08-b, P08-c, P08-d |
| R116 | HF 25-26,63,88 | Biến, object reference và dynamic typing | 0.5 / 0.5 | C04 (tr.11); P01 (tr.9); P05 (tr.16) | C04: C04-K01, C04-K02; P01: P01-a, P01-b, P01-c; P05: P05-a, P05-b, P05-c |
| R117 | HF 39-43 | Định nghĩa rồi gọi hàm | 1 / 1 | P10 (tr.28) | P10: P10-a, P10-b, P10-c, P10-d |
| R118 | HF 39-43 | random và ví dụ bộ bài | 0 / 0 | C15 (tr.30) | C15: C15-K01, C15-K02 |
| R119 | HF 51-60 | Thư viện chuẩn, chọn và import module | 0.5 / 0.5 | C13 (tr.29); P11 (tr.31) | C13: C13-K01; P11: P11-a, P11-b, P11-c |
| R120 | HF 61-68 | print và len | 1 / 1 | P01 (tr.9); P07 (tr.21); P10 (tr.28) | P01: P01-a, P01-b, P01-c; P07: P07-a, P07-b, P07-c; P10: P10-a, P10-b, P10-c, P10-d |
| R121 | HF 61-73 | type/dir/help để khám phá API | 0.5 / 0.5 | C13 (tr.29); P02 (tr.10) | C13: C13-K01; P02: P02-a, P02-b, P02-c |
| R122 | HF 74-75 | Kiểu số và boolean | 1 / 1 | P02 (tr.10); P04 (tr.15); P13 (tr.34) | P02: P02-a, P02-b, P02-c; P04: P04-a, P04-b, P04-c, P04-d; P13: P13-a, P13-b, P13-c, P13-d, P13-e, P13-f |
| R123 | HF 76-79 | List và tính mutable | 1 / 1 | P05 (tr.16) | P05: P05-a, P05-b, P05-c |
| R124 | HF 78-80 | Tuple và tính immutable | 0.5 / 0.5 | C10 (tr.22); P07 (tr.21) | C10: C10-K01, C10-K02; P07: P07-a, P07-b, P07-c |
| R125 | HF 81-83 | Dictionary mapping | 1 / 1 | P06 (tr.19) | P06: P06-a, P06-b, P06-c |
| R126 | HF 84-85 | Set và loại trùng | 1 / 1 | P07 (tr.21) | P07: P07-a, P07-b, P07-c |
| R127 | HF 86-87 | Membership in trên các collection | 0.5 / 0.5 | C09 (tr.20); P24 (tr.49) | C09: C09-K01, C09-K02; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R128 | HF 89-90 | PyPI và hệ sinh thái package | 0 / 0 | C01 (tr.6) | C01: C01-K01, C01-K02, C01-K03 |
| R129 | HF 103-118 | Chia bài toán dữ liệu thành nhiệm vụ nhỏ | 0.5 / 0.5 | C17 (tr.23); P23 (tr.47); P24 (tr.49) | C17: C17-K01, C17-K02; P23: P23-a, P23-b, P23-c, P23-d; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R130 | HF 120-132 | Object, method và dot notation | 1 / 1 | P03 (tr.13); P05 (tr.16); P15 (tr.40) | P03: P03-a, P03-b, P03-c; P05: P05-a, P05-b, P05-c; P15: P15-a, P15-b, P15-c |
| R131 | HF 130-136 | upper/lower và chuỗi không thay tại chỗ | 0.5 / 0.5 | C06 (tr.14); P03 (tr.13) | C06: C06-K01, C06-K02; P03: P03-a, P03-b, P03-c |
| R132 | HF 137-150 | split với delimiter và kiểu list trả về | 1 / 1 | P03 (tr.13); P23 (tr.47) | P03: P03-a, P03-b, P03-c; P23: P23-a, P23-b, P23-c, P23-d |
| R133 | HF 151-155 | Đọc traceback và xác định lỗi gọi sai method | 0.5 / 0.5 | C13 (tr.29); P03 (tr.13); P13 (tr.34) | C13: C13-K01; P03: P03-a, P03-b, P03-c; P13: P13-a, P13-b, P13-c, P13-d, P13-e, P13-f |
| R134 | HF 153-173 | Method chaining và tính dễ đọc | 0.5 / 0.5 | C06 (tr.14); P03 (tr.13) | C06: C06-K01, C06-K02; P03: P03-a, P03-b, P03-c |
| R135 | HF 156-163 | rstrip khác removesuffix | 1 / 1 | P03 (tr.13) | P03: P03-a, P03-b, P03-c |
| R136 | HF 166-173 | Indexing list từ 0 | 0.5 / 0.5 | C07 (tr.17); P03 (tr.13); P09 (tr.26) | C07: C07-K01, C07-K02; P03: P03-a, P03-b, P03-c; P09: P09-a, P09-b, P09-c, P09-d |
| R137 | HF 174-182 | Unpacking/multiple assignment | 0.5 / 0.5 | C10 (tr.22); P23 (tr.47) | C10: C10-K01, C10-K02; P23: P23-a, P23-b, P23-c, P23-d |
| R138 | HF 183-186 | Trích metadata đầy đủ từ tên file | 0.5 / 0.5 | C17 (tr.23); P03 (tr.13) | C17: C17-K01, C17-K02; P03: P03-a, P03-b, P03-c |
| R139 | HF 196-203 | open/with và đóng file | 1 / 1 | P12 (tr.33); P14 (tr.37) | P12: P12-a, P12-b, P12-c; P14: P14-a, P14-b, P14-c |
| R140 | HF 199-200 | Hằng số quy ước UPPERCASE | 0 / 0 | C04 (tr.11) | C04: C04-K01, C04-K02 |
| R141 | HF 200-207 | readlines và đọc dòng cần thiết | 0.5 / 0.5 | C18 (tr.48); P12 (tr.33) | C18: C18-K01, C18-K02; P12: P12-a, P12-b, P12-c |
| R142 | HF 208-218 | strip và split dòng dữ liệu | 1 / 1 | P12 (tr.33); P23 (tr.47) | P12: P12-a, P12-b, P12-c; P23: P23-a, P23-b, P23-c, P23-d |
| R143 | HF 219-223 | Chuyển thời gian thành số cùng đơn vị | 1 / 1 | P23 (tr.47) | P23: P23-a, P23-b, P23-c, P23-d |
| R144 | HF 224-230 | for so với while khi duyệt list | 1 / 1 | P08 (tr.24); P09 (tr.26) | P08: P08-a, P08-b, P08-c, P08-d; P09: P09-a, P09-b, P09-c, P09-d |
| R145 | HF 231-244 | Tạo list kết quả bằng append | 1 / 1 | P05 (tr.16); P12 (tr.33); P23 (tr.47) | P05: P05-a, P05-b, P05-c; P12: P12-a, P12-b, P12-c; P23: P23-a, P23-b, P23-c, P23-d |
| R146 | HF 245-246 | Trung bình và tái sử dụng statistics.mean | 0.5 / 0.5 | C18 (tr.48); P10 (tr.28); P23 (tr.47) | C18: C18-K01, C18-K02; P10: P10-a, P10-b, P10-c, P10-d; P23: P23-a, P23-b, P23-c, P23-d |
| R147 | HF 247-254 | Định dạng thời gian trở lại và kiểm tra số | 1 / 1 | P23 (tr.47) | P23: P23-a, P23-b, P23-c, P23-d |
| R148 | HF 256-260 | Ghép metadata + đọc file + thống kê thành pipeline | 0.5 / 0.5 | C18 (tr.48); P03 (tr.13); P12 (tr.33); P23 (tr.47) | C18: C18-K01, C18-K02; P03: P03-a, P03-b, P03-c; P12: P12-a, P12-b, P12-c; P23: P23-a, P23-b, P23-c, P23-d |
| R149 | GUI 55-88 | Creating our first Python GUI | 1 / 1 | P17 (tr.43) | P17: rubric/manual |
| R150 | GUI 55-88 | Preventing the GUI from being resized | 0 / 0 | T01 (tr.50) | T01: T01-K01 |
| R151 | GUI 55-88 | Adding a label to the GUI form | 1 / 1 | P17 (tr.43) | P17: rubric/manual |
| R152 | GUI 55-88 | Creating buttons and changing their text property | 0.5 / 0.5 | T01 (tr.50); P18 (tr.44) | T01: T01-K01; P18: rubric/manual |
| R153 | GUI 55-88 | Text box widgets | 1 / 1 | P17 (tr.43); P18 (tr.44) | P17: rubric/manual; P18: rubric/manual |
| R154 | GUI 55-88 | Setting focus and disabling widgets | 0.5 / 0.5 | T01 (tr.50); P18 (tr.44) | T01: T01-K01; P18: rubric/manual |
| R155 | GUI 55-88 | Combo box widgets | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R156 | GUI 55-88 | Check button initial states | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R157 | GUI 55-88 | Radio button widgets | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R158 | GUI 55-88 | Scrolled text widgets | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R159 | GUI 55-88 | Adding several widgets in a loop | 0 / 0 | T02 (tr.51); P08 (tr.24) | T02: T02-K01; P08: P08-a, P08-b, P08-c, P08-d |
| R160 | GUI 88-125 | Labels within a label frame | 0.5 / 0.5 | T03 (tr.52); P17 (tr.43) | T03: T03-K01; P17: rubric/manual |
| R161 | GUI 88-125 | Padding around widgets | 0 / 0 | T03 (tr.52) | T03: T03-K01 |
| R162 | GUI 88-125 | Widgets dynamically expand GUI | 0 / 0 | T03 (tr.52) | T03: T03-K01 |
| R163 | GUI 88-125 | Frames within frames | 0 / 0 | T03 (tr.52) | T03: T03-K01 |
| R164 | GUI 88-125 | Menu bars | 0 / 0 | T04 (tr.53) | T04: T04-K01 |
| R165 | GUI 88-125 | Tabbed widgets | 0 / 0 | T04 (tr.53) | T04: T04-K01 |
| R166 | GUI 88-125 | Grid layout manager | 1 / 1 | T03 (tr.52); P17 (tr.43) | T03: T03-K01; P17: rubric/manual |
| R167 | GUI 125-156 | Message boxes information/warning/error | 0 / 0 | T05 (tr.54); P18 (tr.44) | T05: T05-K01, T05-K02; P18: rubric/manual |
| R168 | GUI 125-156 | Independent message boxes | 0 / 0 | T05 (tr.54) | T05: T05-K01, T05-K02 |
| R169 | GUI 125-156 | Title of tkinter window | 1 / 1 | T01 (tr.50); P17 (tr.43) | T01: T01-K01; P17: rubric/manual |
| R170 | GUI 125-156 | Main window icon | 0 / 0 | T01 (tr.50) | T01: T01-K01 |
| R171 | GUI 125-156 | Spin box control | 0 / 0 | T02 (tr.51) | T02: T02-K01 |
| R172 | GUI 125-156 | Relief/sunken/raised appearance | 0 / 0 | T06 (tr.55) | T06: T06-K01 |
| R173 | GUI 125-156 | Tooltips using Python | 0 / 0 | T06 (tr.55) | T06: T06-K01 |
| R174 | GUI 125-156 | Progressbar | 0 / 0 | T07 (tr.56) | T07: T07-K01 |
| R175 | GUI 125-156 | Canvas widget | 0 / 0.5 | T06 (tr.55) | T06: T06-K01 |
| R176 | GUI 156-187 | StringVar | 0.5 / 0.5 | T08 (tr.57); P18 (tr.44) | T08: T08-K01; P18: rubric/manual |
| R177 | GUI 156-187 | Getting data from widget | 1 / 1 | X06 (tr.97); P18 (tr.44) | X06: X06-K01, X06-K02, X06-K03; P18: rubric/manual |
| R178 | GUI 156-187 | Module-level global variables | 0 / 0 | T08 (tr.57); P10 (tr.28) | T08: T08-K01; P10: P10-a, P10-b, P10-c, P10-d |
| R179 | GUI 156-187 | Classes improving GUI | 0.5 / 0.5 | T08 (tr.57); P15 (tr.40); P24 (tr.49) | T08: T08-K01; P15: P15-a, P15-b, P15-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R180 | GUI 156-187 | Writing callback functions | 1 / 1 | X06 (tr.97); P18 (tr.44) | X06: X06-K01, X06-K02, X06-K03; P18: rubric/manual |
| R181 | GUI 156-187 | Reusable GUI components | 0.5 / 0.5 | T08 (tr.57); P17 (tr.43); P18 (tr.44) | T08: T08-K01; P17: rubric/manual; P18: rubric/manual |
| R182 | GUI 187-225 | Creating beautiful charts using Matplotlib | 0.5 / 0.5 | T09 (tr.58); P19 (tr.45) | T09: T09-K01; P19: P19-a, P19-b, P19-c |
| R183 | GUI 187-225 | Installing Matplotlib with whl/pip | 0 / 0 | C01 (tr.6) | C01: C01-K01, C01-K02, C01-K03 |
| R184 | GUI 187-225 | Creating our first chart | 1 / 1 | P19 (tr.45) | P19: P19-a, P19-b, P19-c |
| R185 | GUI 187-225 | Placing labels on charts | 1 / 1 | P19 (tr.45) | P19: P19-a, P19-b, P19-c |
| R186 | GUI 187-225 | Legend | 0 / 0 | T09 (tr.58) | T09: T09-K01 |
| R187 | GUI 187-225 | Scaling charts | 0.5 / 0.5 | T09 (tr.58); P19 (tr.45) | T09: T09-K01; P19: P19-a, P19-b, P19-c |
| R188 | GUI 187-225 | Adjusting scale dynamically | 0 / 0 | T09 (tr.58) | T09: T09-K01 |
| R189 | GUI 225-283 | Creating multiple threads | 0.5 / 0.5 | A12 (tr.90); P21 (tr.82) | A12: A12-K01, A12-K02; P21: P21-a, P21-b, P21-c |
| R190 | GUI 225-283 | Starting a thread | 1 / 1 | P21 (tr.82) | P21: P21-a, P21-b, P21-c |
| R191 | GUI 225-283 | Stopping a thread | 0 / 0.5 | A12 (tr.90) | A12: A12-K01, A12-K02 |
| R192 | GUI 225-283 | Queues | 1 / 1 | P21 (tr.82) | P21: P21-a, P21-b, P21-c |
| R193 | GUI 225-283 | Passing queues among modules | 0 / 0.5 | A12 (tr.90) | A12: A12-K01, A12-K02 |
| R194 | GUI 225-283 | Dialog widgets to copy files to network | 0 / 0 | T05 (tr.54) | T05: T05-K01, T05-K02 |
| R195 | GUI 225-283 | TCP/IP communication | 0 / 0.5 | A13 (tr.91) | A13: A13-K01, A13-K02 |
| R196 | GUI 225-283 | urlopen reading websites | 0 / 0.5 | A13 (tr.91) | A13: A13-K01, A13-K02 |
| R197 | GUI 283-339 | Installing and connecting MySQL | 0 / 0.5 | A18 (tr.74) | A18: A18-K01, A18-K02 |
| R198 | GUI 283-339 | Configuring connection | 0 / 0.5 | A18 (tr.74) | A18: A18-K01, A18-K02 |
| R199 | GUI 283-339 | Designing GUI database | 0 / 0.5 | A18 (tr.74) | A18: A18-K01, A18-K02 |
| R200 | GUI 283-339 | SQL INSERT | 0 / 1 | A19 (tr.75) | A19: A19-K01, A19-K02 |
| R201 | GUI 283-339 | SQL UPDATE | 0 / 1 | A19 (tr.75) | A19: A19-K01, A19-K02 |
| R202 | GUI 283-339 | SQL DELETE | 0 / 0 | A19 (tr.75) | A19: A19-K01, A19-K02 |
| R203 | GUI 283-339 | Storing/retrieving MySQL via GUI | 0 / 0.5 | A20 (tr.76); P18 (tr.44) | A20: A20-K01, A20-K02; P18: rubric/manual |
| R204 | GUI 283-339 | MySQL Workbench | 0 / 0 | A18 (tr.74) | A18: A18-K01, A18-K02 |
| R205 | GUI 339-409 | Widget text in different languages | 0 / 1 | T12 (tr.61) | T12: T12-K01, T12-K02 |
| R206 | GUI 339-409 | Entire GUI language at once | 0 / 1 | T12 (tr.61) | T12: T12-K01, T12-K02 |
| R207 | GUI 339-409 | Localizing GUI | 0 / 0 | T12 (tr.61) | T12: T12-K01, T12-K02 |
| R208 | GUI 339-409 | Preparing for internationalization | 0 / 0.5 | T12 (tr.61) | T12: T12-K01, T12-K02 |
| R209 | GUI 339-409 | Agile GUI design | 0 / 0.5 | T14 (tr.63); P24 (tr.49) | T14: T14-K01; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R210 | GUI 339-409 | Why test GUI code | 0.5 / 0.5 | T10 (tr.59); P20 (tr.46) | T10: T10-K01, T10-K02; P20: P20-a, P20-b |
| R211 | GUI 339-409 | Debug watches | 0 / 0 | T11 (tr.60) | T11: T11-K01 |
| R212 | GUI 339-409 | Debug output levels | 0 / 0 | T11 (tr.60) | T11: T11-K01 |
| R213 | GUI 339-409 | Self-testing with __main__ | 0.5 / 0.5 | T10 (tr.59); P17 (tr.43); P18 (tr.44) | T10: T10-K01, T10-K02; P17: rubric/manual; P18: rubric/manual |
| R214 | GUI 339-409 | Robust GUIs using unit tests | 0.5 / 0.5 | T10 (tr.59); P20 (tr.46) | T10: T10-K01, T10-K02; P20: P20-a, P20-b |
| R215 | GUI 339-409 | Unit tests with Eclipse PyDev | 0 / 0 | T10 (tr.59) | T10: T10-K01, T10-K02 |
| R216 | GUI 409-454 | Installing wxPython | 0 / 0 | A21 (tr.77) | A21: A21-K01, A21-K02 |
| R217 | GUI 409-454 | Creating GUI in wxPython | 0 / 0.5 | A21 (tr.77) | A21: A21-K01, A21-K02 |
| R218 | GUI 409-454 | Quickly adding wx controls | 0 / 0.5 | A21 (tr.77) | A21: A21-K01, A21-K02 |
| R219 | GUI 409-454 | Embedding wx main app in Tk | 0 / 0 | A22 (tr.92) | A22: A22-K01, A22-K02 |
| R220 | GUI 409-454 | Embedding Tk GUI into wx | 0 / 0 | A22 (tr.92) | A22: A22-K01, A22-K02 |
| R221 | GUI 409-454 | Controlling two GUI frameworks | 0 / 0 | A22 (tr.92) | A22: A22-K01, A22-K02 |
| R222 | GUI 409-454 | Communication between GUIs | 0 / 0 | A22 (tr.92) | A22: A22-K01, A22-K02 |
| R223 | GUI 455-498 | PyOpenGL transforms GUI | 0 / 0.5 | A24 (tr.79) | A24: A24-K01, A24-K02 |
| R224 | GUI 455-498 | GUI in 3D | 0 / 0.5 | A24 (tr.79) | A24: A24-K01, A24-K02 |
| R225 | GUI 455-498 | Bitmaps in GUI | 0 / 0 | A23 (tr.78) | A23: A23-K01, A23-K02 |
| R226 | GUI 455-498 | PyGLet alternative to PyOpenGL | 0 / 0 | A25 (tr.80) | A25: A25-K01, A25-K02 |
| R227 | GUI 455-498 | GUI in colors | 0 / 0 | A25 (tr.80) | A25: A25-K01, A25-K02 |
| R228 | GUI 455-498 | OpenGL animation | 0 / 0.5 | A26 (tr.81) | A26: A26-K01, A26-K02 |
| R229 | GUI 455-498 | Tkinter slide show | 0 / 0.5 | T13 (tr.62) | T13: T13-K01 |
| R230 | GUI 499-560 | Avoiding spaghetti code | 0.5 / 0.5 | T08 (tr.57); P24 (tr.49) | T08: T08-K01; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R231 | GUI 499-560 | __init__ to connect modules | 0 / 0.5 | C19 (tr.32) | C19: C19-K01, C19-K02 |
| R232 | GUI 499-560 | Mixing procedural and OOP code | 0.5 / 0.5 | T08 (tr.57); P15 (tr.40); P24 (tr.49) | T08: T08-K01; P15: P15-a, P15-b, P15-c; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R233 | GUI 499-560 | Naming convention | 0 / 0 | C04 (tr.11) | C04: C04-K01, C04-K02 |
| R234 | GUI 499-560 | When not to use OOP | 0 / 0 | T08 (tr.57) | T08: T08-K01 |
| R235 | GUI 499-560 | Design patterns successfully | 0 / 0 | T14 (tr.63) | T14: T14-K01 |
| R236 | GUI 499-560 | Avoiding complexity | 0.5 / 0.5 | T08 (tr.57); P24 (tr.49) | T08: T08-K01; P24: P24-a, P24-b, P24-c, P24-d, P24-e |
| R237 | GUI 499-560 | GUI with multiple notebooks | 0 / 0 | T04 (tr.53) | T04: T04-K01 |

## PW và ticket mở rộng

| Yêu cầu | Bài / minh chứng thiết kế |
|---|---|
| PW0 | C01-C03: môi trường, fork/clone/commit/push |
| PW1 | X01: CLI, hồ sơ DoB, môn, điểm, danh sách |
| PW2-PW4 | C19-C20, A01-A03, X02; package_pw4: OOP, floor, NumPy GPA/ranking, curses, package |
| PW5-PW6 | A04-A05, X03: ba file, ZIP, gzip/pickle, nạp qua lần chạy |
| PW7 | A06-A09, X04: shell, redirect, pipeline; POSIX lab còn cần chạy |
| PW8 | A10-A12, X05: snapshot, worker, atomic replace, lỗi và queue |
| PW9 | X06 và capstone_pw9: Tkinter, domain, điểm, GPA, lưu nền, mở lại |
| E01 | C03,C05,C19,C20,A01-A03,X01-X02 |
| E02 | C21-C22,A04-A05,X03,X05 |
| E03 | T07,A06-A13,X04-X06 |
| E04 | A18-A20: MySQL, transaction, GUI |
| E05 | A21-A23: wx, hai toolkit, bitmap |
| E06 | T06,A24-A26: Canvas/OpenGL/chuyển động |

## Đủ chưa?

Đủ để bàn giao **thiết kế bài học cho phạm vi 237 mục đã kiểm kê**. Chưa đủ để tuyên bố toàn bộ khóa học đã chạy production hoặc đạt hiệu quả học tập. Dev phải đóng các gate trong QA_Ban_giao.md: MySQL thật, POSIX/curses, wx/GL compatibility, hai GUI, network share, IDE/Git và đánh giá giải thích của người học. Không có gate nào được tự chuyển từ NOT_RUN sang PASS chỉ vì đã có đáp án.
