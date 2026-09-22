# Danh sách thiếu trước bổ sung

Baseline: P01-P24 và phạm vi E01-E06 của bản v1. Đủ=1, một phần=0.5, chưa có=0. Ticket E là outline, không phải bài hoàn chỉnh. Giữ nguyên 237 đơn vị để so sánh trước/sau.

| ID | Nguồn/trang PDF | Chủ đề | P | P+E outline | Phần thiếu |
|---|---|---|---:|---:|---|
| R001 | SL 4-19 | Đặc trưng, ứng dụng và giới hạn Python | 0 | 0 | Chưa có câu hỏi hay bài lựa chọn công cụ |
| R002 | SL 19-21 | Phiên bản, môi trường ảo và cài package | 0 | 0 | Thiếu lab cài đặt, môi trường và pip |
| R003 | SL 22-25 | IDE, Jupyter và thao tác notebook | 0 | 0 | Thiếu kernel/cell/lưu notebook |
| R004 | SL 28 | Chạy tương tác so với script | 0.5 | 0.5 | Chưa đối chiếu REPL với script |
| R005 | SL 96 | Git và GitHub workflow | 0 | 0.5 | Chưa có fork/push remote như PW0 |
| R007 | SL 32-33 | Tên biến hợp lệ và từ khóa dành riêng | 0 | 0 | Cần sửa lỗi tên biến |
| R008 | SL 34-36 | Toán tử số và thứ tự tính | 0.5 | 0.5 | Chưa luyện toàn bộ toán tử và precedence |
| R009 | SL 38-45 | Kiểu int/float/bool/str và dynamic typing | 0.5 | 0.5 | Có đổi kiểu, chưa luyện gán lại tên sang kiểu khác |
| R012 | SL 47-48 | Indexing và slicing chuỗi | 0 | 0 | Chấp nhận slicing như lời giải không đồng nghĩa dạy slicing |
| R013 | SL 49 | Định dạng chuỗi | 0.5 | 0.5 | Chỉ một mẫu, chưa so format và f-string |
| R014 | SL 50-51,61 | Comment và docstring | 0 | 0 | Chưa yêu cầu đọc/viết comment hay docstring |
| R017 | SL 56-57 | Nhánh lồng nhau và elif | 0.5 | 0.5 | Chưa có bài riêng dự đoán chuỗi nhánh |
| R019 | SL 62 | Hàm dựng sẵn len/print và input | 0.5 | 0.5 | input CLI chưa được luyện; đầu vào đều được cấp |
| R020 | SL 64-67,81 | Chọn collection, tính có thứ tự và thay đổi được | 0.5 | 0.5 | Tuple bất biến chưa có câu sửa lỗi thay phần tử |
| R022 | SL 68-70 | List append và nối/extend | 0.5 | 0.5 | Chưa luyện khác nhau append/extend |
| R023 | SL 71-76 | List indexing/slicing và cập nhật đoạn | 0 | 0 | Thiếu chỉ số âm, bước nhảy và slice assignment |
| R024 | SL 77-78 | List xóa phần tử | 0 | 0 | Thiếu del/remove/pop |
| R025 | SL 79-80,93 | range và quy tắc start/stop/step | 0 | 0 | Chưa có bài range hoặc lỗi off-by-one của range |
| R028 | SL 85-87 | Dict pop/keys/values/items | 0 | 0 | Thiếu duyệt và xóa cặp khóa/giá trị |
| R031 | SL 91-92 | break/continue | 0 | 0 | Lời giải thay thế dùng break chưa phải bài dạy break/continue |
| R033 | SL 114 | Phương thức so sánh __lt__ | 0 | 0 | Thiếu so sánh/sắp xếp object |
| R034 | SL 115-117 | Biểu diễn __str__ | 0 | 0 | Thiếu custom text representation |
| R036 | SL 121-122 | isinstance và issubclass | 0.5 | 0.5 | Chưa có nhiệm vụ trực tiếp phân biệt hai hàm |
| R037 | SL 123-124 | Đa kế thừa | 0 | 0 | Chưa có bài |
| R039 | SL 128-131 | Encapsulation, underscore và accessor | 0 | 0 | Chưa có bài getter/setter hay name mangling |
| R040 | SL 101-106 | OOP review: abstract class và type conformance | 0 | 0 | Chỉ xuất hiện như câu hỏi ôn trong slide |
| R041 | SL 136-139,151 | Tạo module và tái cấu trúc nhiều file | 0.5 | 1 | P hiện tại chưa buộc tự tạo kiến trúc module |
| R043 | SL 142 | Import alias | 0.5 | 0.5 | Chưa tự sửa lỗi namespace/alias |
| R044 | SL 143-148 | Package và package lồng nhau | 0 | 0.5 | Chưa có nhiệm vụ import package lồng nhau |
| R045 | SL 150 | math.floor và làm tròn xuống 1 chữ số | 0 | 0 | Chưa có bài đúng quy tắc PW3 |
| R046 | SL 150 | NumPy array và GPA có trọng số | 0.5 | 1 | Trong P chỉ gọi hàm, chưa tự dùng NumPy |
| R047 | SL 150 | Sắp sinh viên theo GPA giảm dần | 0 | 0 | Thiếu xếp hạng theo GPA |
| R048 | SL 150-151 | Curses UI | 0 | 1 | Mới là ticket, chưa bài P hoàn chỉnh |
| R050 | SL 158-160 | open và các chế độ r/w/a/b/+ | 0.5 | 0.5 | Chưa luyện append/binary/update mode |
| R051 | SL 161-163 | Đọc/ghi, read/readline/readlines | 0.5 | 0.5 | Chưa so các API và đọc size |
| R052 | SL 164-165 | Buffering | 0 | 0 | Chưa luyện/giải thích buffering |
| R054 | SL 169-170 | Xử lý ngoại lệ I/O | 0.5 | 0.5 | Chưa có hoạt động phân biệt lỗi quyền đọc/ghi |
| R055 | SL 171-172 | File tạm | 0 | 0 | Chưa có bài tempfile |
| R056 | SL 173-178,191 | Nén dữ liệu | 0 | 1 | Chỉ bao phủ cơ chế nén một lựa chọn, chưa mọi thư viện |
| R057 | SL 179-181,192 | Pickle serialization và giới hạn kiểu | 0 | 1 | P14 JSON không thay thế kỹ năng pickle |
| R058 | SL 182 | So sánh pickle/JSON | 0.5 | 1 | P chưa thực hành hai định dạng |
| R059 | SL 183-188 | Cấu trúc thư mục và duyệt file | 0 | 0.5 | Chưa đệ quy/os.walk |
| R060 | SL 187-188 | Tạo/xóa thư mục và thao tác filesystem | 0 | 0 | Chưa có bài thực hành |
| R061 | SL 196-206 | Program/process và không gian chạy riêng | 0.5 | 0.5 | Chưa kiểm tra mô hình bộ nhớ đầy đủ |
| R062 | SL 207-208 | Trạng thái tiến trình | 0 | 0 | new/ready/running/waiting/terminated |
| R063 | SL 209-210 | Cây tiến trình và tạo tiến trình con | 0.5 | 0.5 | Chưa quan sát cây/nhiều thế hệ |
| R064 | SL 211-213 | Tạo tiến trình Windows | 0 | 0 | CreateProcess/WinExec không được luyện |
| R065 | SL 214-221 | fork/exec trên UNIX | 0 | 0 | Chưa có mô hình kết quả fork và exec |
| R066 | SL 222-225 | Mục tiêu lập lịch, preemption | 0 | 0 | Thiếu dự đoán quyền CPU |
| R067 | SL 226-228 | Context switch và PCB | 0 | 0 | Thiếu truy vết chuyển trạng thái |
| R068 | SL 229-235 | Scheduler, hàng đợi và thuật toán | 0 | 0 | FCFS/SJF/priority/round-robin chưa luyện |
| R069 | SL 236-240 | stdin/stdout/stderr và redirection | 0.5 | 0.5 | Thiếu stdin, stderr và chuyển hướng đầy đủ |
| R071 | SL 245 | Background/Popen, pipe, timeout/terminate | 0.5 | 0.5 | Chưa có pipe/Popen và điều khiển vòng đời độc lập |
| R072 | SL 247-248 | Shell tương tác | 0 | 0 | Chưa có bài parser/chạy nhiều lệnh shell |
| R073 | SL 251-264 | Thread/process, bộ nhớ chia sẻ và stack riêng | 0.5 | 0.5 | Chưa kiểm tra phân biệt tài nguyên chi tiết |
| R074 | SL 265-272 | Responsiveness, hiệu năng và scalability | 0.5 | 0.5 | Chưa luyện CPU/I-O và scalability |
| R075 | SL 273 | Nondeterminism và lỗi tranh chấp | 0 | 0 | Chưa có bài race condition |
| R076 | SL 274-276 | Kiến trúc Apache/Chromium | 0 | 0 | Thiếu hoạt động so mô hình đa tiến trình/luồng |
| R077 | SL 278-286 | GIL và concurrency một/nhiều core | 0 | 0 | Chưa có bài dự đoán theo loại tác vụ |
| R078 | SL 287-291 | Subclass Thread | 0 | 0 | Chưa có bài override run |
| R080 | SL 296-297 | Lock/mutex | 0 | 0 | Chưa thực hành bảo vệ shared state |
| R081 | SL 299 | Lưu pickle+nén trong background thread | 0 | 0.5 | Chưa nối đúng yêu cầu lưu pickle nền |
| R082 | SL 302-307 | CLI/GUI và so sánh toolkit | 0.5 | 0.5 | Chưa có tiêu chí lựa chọn/so sánh toolkit trực tiếp |
| R083 | SL 309 | Cửa sổ, title và subwindow/size | 0.5 | 0.5 | Chưa subwindow và kích thước |
| R084 | SL 310-311 | Widget container/Frame | 0.5 | 0.5 | Chưa bài container có yêu cầu riêng |
| R086 | SL 314 | Radiobutton | 0 | 0 | Thiếu lựa chọn đơn |
| R087 | SL 315 | Listbox | 0 | 0 | Chưa có bài thao tác listbox |
| R088 | SL 316 | Combobox | 0 | 0 | Thiếu lựa chọn từ danh sách |
| R089 | SL 318-319 | Layout pack | 0 | 0 | Chưa luyện pack |
| R090 | SL 320-321 | Layout place | 0 | 0 | Chưa luyện place |
| R092 | SL 325 | Event loop | 0.5 | 0.5 | Chưa hoạt động riêng về vòng xử lý sự kiện |
| R093 | SL 328 | Nhập file bằng NumPy | 0 | 0 | Thiếu loadtxt/genfromtxt |
| R094 | SL 328 | Pandas CSV và khám phá DataFrame | 0 | 0 | Thiếu read_csv/head/info |
| R095 | SL 328 | Excel bằng pandas | 0 | 0 | Thiếu đọc sheet |
| R096 | SL 328 | SAS/Stata/HDF5/Matlab | 0 | 0 | Nhóm định dạng khoa học ngoài lõi |
| R097 | SL 328 | SQLAlchemy/pandas đọc DB | 0 | 0 | Chưa xử lý DataFrame từ DB |
| R098 | SL 328 | Thao tác filesystem bổ sung: cwd/rename | 0 | 0 | Chưa có nhiệm vụ |
| R099 | SL 329 | Figure/axes và nhiều subplot | 0.5 | 0.5 | Chưa bố cục nhiều subplot |
| R100 | SL 329 | Nhóm plot line/scatter/bar | 0.5 | 0.5 | Thiếu line/scatter |
| R101 | SL 329 | Phân phối: histogram/box/violin | 0 | 0 | Thiếu trực quan phân phối |
| R102 | SL 329 | Image/2D/vector fields | 0 | 0 | Chưa imshow/contour/quiver |
| R103 | SL 329 | Nhãn/limits/legend/ticks/styles | 0.5 | 0.5 | Thiếu legend, ticks, style |
| R104 | SL 329 | Lưu/hiển thị/đóng biểu đồ | 0.5 | 0.5 | Chưa savefig/close và vòng đời |
| R105 | SL 330 | String lower/title/zfill/splitlines | 0 | 0 | Chưa luyện nhóm string bổ sung |
| R106 | SL 330 | Dict min/max theo giá trị | 0 | 0 | Chưa tìm khóa có giá trị cực trị |
| R107 | SL 330 | Regex search/sub | 0 | 0 | Thiếu regex |
| R108 | SL 330 | List comprehension | 0.5 | 0.5 | Chưa giải thích/biến đổi comprehension có filter |
| R109 | SL 330 | enumerate và zip | 0.5 | 0.5 | Chưa có bài, không có enumerate |
| R110 | SL 330 | datetime/timedelta/parse/format | 0 | 0 | Thiếu xử lý ngày giờ |
| R111 | SL 330 | random | 0 | 0 | Thiếu ngẫu nhiên |
| R112 | SL 330 | Counter và most_common | 0 | 0 | Thiếu đếm tần suất |
| R113 | HF 5-14 | Cài Python/VS Code/extensions | 0 | 0 | Runtime dev không là kỹ năng học viên |
| R114 | HF 28-48,100-101 | REPL/notebook, kernel và quản lý cell | 0 | 0 | Chưa luyện tạo/chạy/lưu notebook |
| R116 | HF 25-26,63,88 | Biến, object reference và dynamic typing | 0.5 | 0.5 | Chưa tự thay reference sang object kiểu khác |
| R118 | HF 39-43 | random và ví dụ bộ bài | 0 | 0 | Thay tình huống được nhưng cơ chế random vẫn thiếu |
| R119 | HF 51-60 | Thư viện chuẩn, chọn và import module | 0.5 | 0.5 | Chưa luyện tìm/chọn module PSL theo vấn đề |
| R121 | HF 61-73 | type/dir/help để khám phá API | 0.5 | 0.5 | Chưa người học dùng type/dir/help để tìm method |
| R124 | HF 78-80 | Tuple và tính immutable | 0.5 | 0.5 | Chưa kiểm tra sửa tuple so với list |
| R127 | HF 86-87 | Membership in trên các collection | 0.5 | 0.5 | Chưa so ý nghĩa trên list/str/set/dict |
| R128 | HF 89-90 | PyPI và hệ sinh thái package | 0 | 0 | E01 không bao gồm quản lý cài đặt |
| R129 | HF 103-118 | Chia bài toán dữ liệu thành nhiệm vụ nhỏ | 0.5 | 0.5 | Chưa yêu cầu tự phân rã yêu cầu |
| R131 | HF 130-136 | upper/lower và chuỗi không thay tại chỗ | 0.5 | 0.5 | Có ý nghĩa chuỗi mới, chưa luyện upper/lower |
| R133 | HF 151-155 | Đọc traceback và xác định lỗi gọi sai method | 0.5 | 0.5 | Chưa nhiệm vụ tự đọc traceback đủ dòng |
| R134 | HF 153-173 | Method chaining và tính dễ đọc | 0.5 | 0.5 | Chưa refactor một chain khó đọc |
| R136 | HF 166-173 | Indexing list từ 0 | 0.5 | 0.5 | Chưa challenge khai thác nhiều vị trí dữ liệu tên file |
| R137 | HF 174-182 | Unpacking/multiple assignment | 0.5 | 0.5 | Chưa bài độc lập mismatch số biến/phần tử |
| R138 | HF 183-186 | Trích metadata đầy đủ từ tên file | 0.5 | 0.5 | Chưa schema tên/tuổi/cự ly/kiểu bơi đầy đủ và chuyển kiểu |
| R140 | HF 199-200 | Hằng số quy ước UPPERCASE | 0 | 0 | Chưa phân biệt quy ước và bất biến |
| R141 | HF 200-207 | readlines và đọc dòng cần thiết | 0.5 | 0.5 | Chưa thực hành đọc list dòng rồi chọn dòng0 |
| R146 | HF 245-246 | Trung bình và tái sử dụng statistics.mean | 0.5 | 0.5 | statistics.mean chỉ là lời giải được chấp nhận, chưa dạy chọn dùng |
| R148 | HF 256-260 | Ghép metadata + đọc file + thống kê thành pipeline | 0.5 | 0.5 | P23 nhận line, chưa ghép pipeline file + metadata cuối cùng |
| R150 | GUI 55-88 | Preventing the GUI from being resized | 0 | 0 | QA resize không phải bài resizable(False,False) |
| R152 | GUI 55-88 | Creating buttons and changing their text property | 0.5 | 0.5 | Chưa đổi text của chính button |
| R154 | GUI 55-88 | Setting focus and disabling widgets | 0.5 | 0.5 | Chưa bài đầy đủ cả focus/disabled |
| R155 | GUI 55-88 | Combo box widgets | 0 | 0 | Thiếu |
| R156 | GUI 55-88 | Check button initial states | 0 | 0 | Thiếu |
| R157 | GUI 55-88 | Radio button widgets | 0 | 0 | Thiếu |
| R158 | GUI 55-88 | Scrolled text widgets | 0 | 0 | Thiếu |
| R159 | GUI 55-88 | Adding several widgets in a loop | 0 | 0 | Thiếu |
| R160 | GUI 88-125 | Labels within a label frame | 0.5 | 0.5 | Chưa LabelFrame |
| R161 | GUI 88-125 | Padding around widgets | 0 | 0 | Thiếu padx/pady |
| R162 | GUI 88-125 | Widgets dynamically expand GUI | 0 | 0 | Chưa dạy sticky/weight/co giãn |
| R163 | GUI 88-125 | Frames within frames | 0 | 0 | Thiếu layout container lồng nhau |
| R164 | GUI 88-125 | Menu bars | 0 | 0 | Thiếu |
| R165 | GUI 88-125 | Tabbed widgets | 0 | 0 | Thiếu Notebook tab |
| R167 | GUI 125-156 | Message boxes information/warning/error | 0 | 0 | Status Label không là messagebox |
| R168 | GUI 125-156 | Independent message boxes | 0 | 0 | Thiếu |
| R170 | GUI 125-156 | Main window icon | 0 | 0 | Thiếu |
| R171 | GUI 125-156 | Spin box control | 0 | 0 | Thiếu |
| R172 | GUI 125-156 | Relief/sunken/raised appearance | 0 | 0 | Thiếu |
| R173 | GUI 125-156 | Tooltips using Python | 0 | 0 | Thiếu |
| R174 | GUI 125-156 | Progressbar | 0 | 0 | Thiếu |
| R175 | GUI 125-156 | Canvas widget | 0 | 0.5 | Thiếu code API canvas hoàn chỉnh trong ticket |
| R176 | GUI 156-187 | StringVar | 0.5 | 0.5 | Được cấp mẫu, chưa bài về binding/get/set riêng |
| R178 | GUI 156-187 | Module-level global variables | 0 | 0 | Chưa bài so scope/module globals |
| R179 | GUI 156-187 | Classes improving GUI | 0.5 | 0.5 | Chưa refactor GUI thành class |
| R181 | GUI 156-187 | Reusable GUI components | 0.5 | 0.5 | Chưa tạo component độc lập dùng ở nhiều view |
| R182 | GUI 187-225 | Creating beautiful charts using Matplotlib | 0.5 | 0.5 | Chưa tích hợp Tk canvas và mức tùy biến của recipe |
| R183 | GUI 187-225 | Installing Matplotlib with whl/pip | 0 | 0 | Chưa bài cài đặt |
| R186 | GUI 187-225 | Legend | 0 | 0 | Thiếu |
| R187 | GUI 187-225 | Scaling charts | 0.5 | 0.5 | Chưa luyện thay scale của biểu đồ theo nhiều tình huống |
| R188 | GUI 187-225 | Adjusting scale dynamically | 0 | 0 | Thiếu min/max động |
| R189 | GUI 225-283 | Creating multiple threads | 0.5 | 0.5 | Chưa quản lý nhiều worker |
| R191 | GUI 225-283 | Stopping a thread | 0 | 0.5 | Chưa dừng worker hợp tác |
| R193 | GUI 225-283 | Passing queues among modules | 0 | 0.5 | Chưa nhiệm vụ tổ chức queue qua module cụ thể |
| R194 | GUI 225-283 | Dialog widgets to copy files to network | 0 | 0 | Thiếu file dialog/network copy |
| R195 | GUI 225-283 | TCP/IP communication | 0 | 0.5 | Chưa code socket client/server hoàn chỉnh |
| R196 | GUI 225-283 | urlopen reading websites | 0 | 0.5 | Chưa bài urlopen thật đầy đủ |
| R197 | GUI 283-339 | Installing and connecting MySQL | 0 | 0.5 | Chưa cài server và tự tạo kết nối |
| R198 | GUI 283-339 | Configuring connection | 0 | 0.5 | Chưa cấu hình host/port/driver |
| R199 | GUI 283-339 | Designing GUI database | 0 | 0.5 | Chưa tự thiết kế mô hình dữ liệu của ứng dụng |
| R200 | GUI 283-339 | SQL INSERT | 0 | 1 | Đây là ticket E, chưa bài P 4 bước |
| R201 | GUI 283-339 | SQL UPDATE | 0 | 1 | Đây là ticket E |
| R202 | GUI 283-339 | SQL DELETE | 0 | 0 | E04 cũng thiếu DELETE |
| R203 | GUI 283-339 | Storing/retrieving MySQL via GUI | 0 | 0.5 | Chưa tích hợp CRUD GUI đầy đủ |
| R204 | GUI 283-339 | MySQL Workbench | 0 | 0 | Thiếu |
| R205 | GUI 339-409 | Widget text in different languages | 0 | 1 | Mới ticket |
| R206 | GUI 339-409 | Entire GUI language at once | 0 | 1 | Mới ticket |
| R207 | GUI 339-409 | Localizing GUI | 0 | 0 | Chưa locale/ngày giờ/số theo khu vực |
| R208 | GUI 339-409 | Preparing for internationalization | 0 | 0.5 | Chưa bộ cấu trúc quốc tế hóa như source |
| R209 | GUI 339-409 | Agile GUI design | 0 | 0.5 | Chưa bài vòng lặp yêu cầu/phản hồi/thiết kế GUI |
| R210 | GUI 339-409 | Why test GUI code | 0.5 | 0.5 | Chưa nhiệm vụ test GUI của học viên |
| R211 | GUI 339-409 | Debug watches | 0 | 0 | Thiếu |
| R212 | GUI 339-409 | Debug output levels | 0 | 0 | Thiếu logging levels |
| R213 | GUI 339-409 | Self-testing with __main__ | 0.5 | 0.5 | Chưa tự viết self-test, chỉ launch GUI |
| R214 | GUI 339-409 | Robust GUIs using unit tests | 0.5 | 0.5 | Không tính test do trợ lý/dev viết là bài unit test GUI cho người học |
| R215 | GUI 339-409 | Unit tests with Eclipse PyDev | 0 | 0 | Có thể thay IDE mới nhưng vẫn chưa có workflow tương đương |
| R216 | GUI 409-454 | Installing wxPython | 0 | 0 | Chưa lab cài đặt |
| R217 | GUI 409-454 | Creating GUI in wxPython | 0 | 0.5 | Thiếu mẫu/API và bốn bước đầy đủ |
| R218 | GUI 409-454 | Quickly adding wx controls | 0 | 0.5 | Chưa đủ nhóm controls source |
| R219 | GUI 409-454 | Embedding wx main app in Tk | 0 | 0 | Chưa bao phủ |
| R220 | GUI 409-454 | Embedding Tk GUI into wx | 0 | 0 | Chưa bao phủ |
| R221 | GUI 409-454 | Controlling two GUI frameworks | 0 | 0 | Chưa cùng ứng dụng |
| R222 | GUI 409-454 | Communication between GUIs | 0 | 0 | Thiếu |
| R223 | GUI 455-498 | PyOpenGL transforms GUI | 0 | 0.5 | Chưa setup/code OpenGL đầy đủ |
| R224 | GUI 455-498 | GUI in 3D | 0 | 0.5 | Chưa biến đổi/render 3D tự tạo |
| R225 | GUI 455-498 | Bitmaps in GUI | 0 | 0 | Chưa bitmap/OpenGL mapping |
| R226 | GUI 455-498 | PyGLet alternative to PyOpenGL | 0 | 0 | Chưa bài PyGLet |
| R227 | GUI 455-498 | GUI in colors | 0 | 0 | Thiếu màu 3D |
| R228 | GUI 455-498 | OpenGL animation | 0 | 0.5 | Có state update, chưa animation OpenGL cụ thể |
| R229 | GUI 455-498 | Tkinter slide show | 0 | 0.5 | Chưa ảnh/timer/Pillow tích hợp đầy đủ |
| R230 | GUI 499-560 | Avoiding spaghetti code | 0.5 | 0.5 | Chưa bài sửa code GUI rối với before/after |
| R231 | GUI 499-560 | __init__ to connect modules | 0 | 0.5 | Chưa bài __init__.py export; Student.__init__ là khái niệm khác |
| R232 | GUI 499-560 | Mixing procedural and OOP code | 0.5 | 0.5 | Chưa yêu cầu lựa chọn tổ chức GUI |
| R233 | GUI 499-560 | Naming convention | 0 | 0 | Chưa nhiệm vụ đổi tên có lý do |
| R234 | GUI 499-560 | When not to use OOP | 0 | 0 | Chưa hoạt động so sánh hai thiết kế |
| R235 | GUI 499-560 | Design patterns successfully | 0 | 0 | Có từ service không đồng nghĩa design pattern của source |
| R236 | GUI 499-560 | Avoiding complexity | 0.5 | 0.5 | Chưa refactor GUI khi tăng nhiều tính năng |
| R237 | GUI 499-560 | GUI with multiple notebooks | 0 | 0 | Thiếu |
