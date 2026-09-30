# Lộ trình Python theo tỷ lệ 50 30 20

Bản thiết kế lại ngày 30/09/2026. Mục tiêu: tự giải 5 dạng trong final-2026.docx, từ cơ bản tới OOP, thread và process. Chưa xác nhận đây là toàn bộ phạm vi thi hay công thức điểm qua môn. Không cam kết chắc chắn đỗ từ việc học hết nội dung.

## Tỷ lệ và cách đếm

**40 nhiệm vụ code bắt buộc: 20 cơ bản, 12 trung cấp, 8 nâng cao.** Tỷ lệ tính theo nhiệm vụ, không theo số dòng mã, thời lượng hay điểm thi. Quiz và ví dụ là thành phần của bài, không dùng để tăng mẫu số. Đề tổng duyệt và bài tự chọn ở ngoài cơ cấu 40 nhiệm vụ. Không gắn tỷ lệ 50/30/20 với thang điểm chính thức chưa có.

V2 là kho kiến thức 92 bài. V3 chọn và viết lại đường học bắt buộc theo mục tiêu thi, không đổi nhãn 92 bài để tạo tỷ lệ đẹp. Kiến thức chuyên sâu không có trong đề minh họa được giữ trong thư viện tự chọn; sẽ chuyển vào phần bắt buộc nếu đề cương đánh giá xác nhận có thi. Vì vậy không gọi lộ trình 40 nhiệm vụ là phủ toàn bộ 237 mục nguồn.

## Roadmap

| Chặng | Mã bài | Nội dung | Cửa kiểm tra đầu ra |
|---|---|---|---|
| M1 | B01-B05 | Dữ liệu và điều kiện | Đọc được biểu thức và tự viết nhánh đơn. |
| M2 | B06-B10 | Vòng lặp và hàm | Tự viết một hàm, rồi nối hai hàm. |
| M3 | B11-B15 | Đọc và ghi file | Đọc từng dòng, ghi kết quả, biết giá trị trả về. |
| M4 | B16-B20 | Ghép bài palindrome | Tự giải Ex1 với dữ liệu mới, không xem đáp án. |
| M5 | I01-I04 | Class đầu tiên | Tạo object, thêm dữ liệu, biểu diễn bằng __str__. |
| M6 | I05-I08 | Trạng thái và lớp cha | Tự viết ProgrammingLanguage; tách state hai object. |
| M7 | I09-I12 | Kế thừa và override | Tự viết C kế thừa, khởi tạo và override đúng. |
| M8 | N01-N04 | Thread và chờ kết thúc | Tạo n thread, start tất cả rồi join tất cả. |
| M9 | N05-N08 | Process và đo thời gian | Tạo m child, mỗi child n thread; parent chờ đủ rồi đo. |

## Danh mục nhiệm vụ

| Mã | Nhiệm vụ | Hợp đồng | Tiêu chí |
|---|---|---|---|
| B01 | Biến và kết quả | Gán name="Python", year=1991; in hai biến trên hai dòng. | 2 dòng đúng thứ tự; sửa year thành 2026 phải phản ánh giá trị mới. |
| B02 | Ghép chuỗi | Cho name="Python"; tạo message="Language: Python" bằng phép nối rồi in. | Đổi name="C" được Language: C; không hard-code cả câu. |
| B03 | Đảo chuỗi | Cho text; tạo reversed_text bằng slicing, in kết quả. | level -> level; python -> nohtyp; a -> a. |
| B04 | So sánh palindrome | Cho text không rỗng; tạo biến result so sánh text với chuỗi đảo. | level=True, abc=False, Level=False; giữ nguyên hoa/thường. |
| B05 | if và else | Từ biến result ở bài trước, in PALINDROME hoặc NOT PALINDROME bằng if/else. | Mỗi lần đúng một dòng; hai nhánh đều được kiểm. |
| B06 | Duyệt danh sách | Duyệt words=["level","python","radar"]; in từng phần tử bằng for. | 3 dòng theo thứ tự, không in cả list; list rỗng không in. |
| B07 | Lọc bằng vòng lặp | Tạo list kết quả; for/if/append để giữ các từ đối xứng không rỗng. | Giữ level,radar; giữ thứ tự và phần tử trùng; không sửa list đầu vào. |
| B08 | Tự viết một hàm | Viết is_empty(text) trả True nếu text rỗng, ngược lại False; tự gọi thử hàm. | ""=True; " "=False; "a"=False; hàm không print. |
| B09 | Hàm kiểm tra chuỗi | Viết is_palindrome(text): chuỗi rỗng trả False; còn lại so với chuỗi đảo. | "level"=True; "ab"=False; "Level"=False; không tự strip. |
| B10 | Nối hai hàm | Tự viết filter_palindromes(words), gọi is_palindrome đã viết; dùng vòng lặp rõ ràng. | ["level","ab","radar",""] -> ["level","radar"]; [] -> []. |
| B11 | Đọc file đầu tiên | Dùng with/open UTF-8 để đọc toàn bộ data.txt vào text; in text. | Nội dung đúng cả dấu tiếng Việt; chưa xử lý thiếu file ở bài này. |
| B12 | Đọc từng dòng | Duyệt file; dùng rstrip("\n") bỏ xuống dòng và thêm vào list. | Giữ khoảng trắng hai đầu; không bỏ ký tự thường; giữ dòng cuối không newline. |
| B13 | Ghi một kết quả | Ghi mỗi từ của list được cấp vào palindromes.txt bằng mode w, mỗi từ một dòng. | Ghi đè file cũ; list rỗng tạo file rỗng; đầu vào không bị sửa. |
| B14 | Đưa phần đọc vào hàm | Viết read_lines(path) trả list chuỗi đã bỏ ký tự xuống dòng; không print. | File rỗng trả []; UTF-8 đúng; thiếu file giữ FileNotFoundError. |
| B15 | Đưa phần ghi vào hàm | Viết write_lines(path, lines) dùng with và mode w; thêm newline sau từng chuỗi. | Mỗi phần tử một dòng; không append vào lần chạy trước; trả None. |
| B16 | Sửa lỗi print và return | Sửa filter_palindromes đang chỉ print để nơi gọi nhận list; sửa lỗi return đặt trong for. | Xét đủ mọi từ; stdout rỗng; list rỗng trả []. |
| B17 | Nối đọc với lọc | Dùng read_lines đã cấp và is_palindrome đã học; tự viết phần lọc kết quả từ file. | Dữ liệu level/python/radar -> level/radar; chưa ghi file. |
| B18 | Nối lọc với ghi | Cho sẵn list chuỗi; dùng filter_palindromes và write_lines để xuất kết quả. | File chỉ có chuỗi đối xứng; giữ thứ tự và trùng lặp. |
| B19 | Ex1 có hỗ trợ | Hoàn thành khung gồm read_lines, is_palindrome, write_lines và phần điều phối for/if. | Fixture có chuỗi đúng/sai/rỗng/Unicode; output đúng; file nguồn không đổi. |
| B20 | Ex1 tự làm | Tự viết chương trình đọc data.txt và ghi palindromes.txt từ fixture mới, tối đa 3 hàm tự viết. | Không cấp lời giải; kiểm dòng cuối không newline, file rỗng, thứ tự, chữ hoa/thường; giải thích luồng dữ liệu. |
| I01 | Đọc thuộc tính object | Cho sẵn ProgrammingLanguage; tạo object Python/1991/["procedural"], in các thuộc tính. | Đúng 3 trường; thay object bằng C/1972 dùng cùng mã truy cập. |
| I02 | Viết constructor | Tự viết __init__(name,year_created,paradigms) lưu ba thuộc tính; copy list đầu vào. | Thuộc tính đúng; sửa list bên ngoài không đổi object. |
| I03 | Thêm một paradigm | Trong class đã cấp, viết add_paradigms(self,paradigm) bằng append. | Thêm vào cuối; giữ trùng nếu nhập trùng; trả None. Đây là quy ước v3. |
| I04 | Viết __str__ | Trong class đã cấp, viết __str__ trả Language[name], Year created[year], Paradigms[list]. | Trả str, không print; định dạng dùng repr của list như trong đáp án mẫu. |
| I05 | Hai object độc lập | Sửa class có list dùng chung để thêm paradigm vào object A không đổi object B. | Tạo hai object từ cùng list nguồn; thay A không đổi B hay list nguồn. |
| I06 | Phân biệt print và str | Sửa __str__ đang print; viết đoạn gọi print(obj) và lưu text=str(obj). | text là str đúng; gọi str(obj) không tự in; print(obj) in một dòng. |
| I07 | Ex2 tự làm | Tự viết ProgrammingLanguage với __init__, add_paradigms, __str__; không nhìn lời giải. | Kiểm đủ 3 phương thức, list riêng, trường dữ liệu và format đã công bố. |
| I08 | Lớp con đầu tiên | Cho class cha; khai báo class C(ProgrammingLanguage), chưa thêm thuộc tính; tạo một object C. | isinstance với class cha=True; dùng được phương thức cha; giải thích kế thừa. |
| I09 | super và thuộc tính mới | Cho class cha; viết C.__init__(name,year_created,paradigms,std_version) dùng super(). | 4 thuộc tính đúng; std_version khác nhau không ảnh hưởng nhau. |
| I10 | Override __str__ | Cho C có constructor; override __str__ bằng super().__str__ và phần Standard version[...]. | Giữ đủ trường cha; thêm đúng trường std_version; không gọi đệ quy str(self). |
| I11 | Viết compile | Thêm compile(self) in Compiling C code using standard version [giá trị phiên bản]. | Một dòng đúng phiên bản; gọi lại dùng trạng thái hiện tại; không biên dịch C thật. |
| I12 | Ex3 tự làm | Cho class cha đã kiểm; tự viết class C với constructor, __str__ và compile. | Đạt cả khởi tạo, kế thừa, override và thông báo; khoảng 15-25 dòng mới. |
| N01 | Một thread | Cho compile() đã có; tạo một Thread(target=obj.compile), start rồi join. | Target là callable, không gọi sẵn; công việc chạy trong thread con. |
| N02 | Nhiều thread | Tạo n thread trong list; vòng lặp thứ nhất start, vòng lặp thứ hai join. | n=1,3 chạy đúng n lần; không start/join từng thread nối đuôi. |
| N03 | Ex4 có hỗ trợ | Trong C đã cấp, viết parallel_compile(n); mỗi thread gọi helper in thông báo có n và std_version. | Đúng n công việc; start toàn bộ trước join; hàm chỉ trả khi tất cả xong; không chấm thứ tự output. |
| N04 | Ex4 tự làm và sửa lỗi | Viết lại parallel_compile(n) từ khung rỗng; thêm kiểm tra n là int dương, không bool. | n=0,-1,True -> ValueError theo v3; kiểm worker chạy thật và toàn bộ được join. |
| N05 | Một process con | Trong script POSIX cấp sẵn, dùng fork; child in thông báo rồi _exit(0); parent waitpid. | Phân biệt pid==0; parent chỉ tiếp tục sau child; chạy trong Linux/WSL. |
| N06 | Tạo m process | Chỉ parent tiếp tục vòng lặp tạo m child; lưu pid và waitpid từng child sau khi tạo đủ. | m=1,2 có đúng m child; child thoát, không nhân đôi cây process; kiểm exit status. |
| N07 | Mỗi process chạy n thread | Cho C và parallel_compile; mỗi child gọi parallel_compile(n), rồi thoát; parent chờ đủ m child. | m=2,n=3 có 2 child và 6 worker; fork từ parent đơn luồng; không suy số thread chỉ từ số dòng in. |
| N08 | Ex5 tự làm | Viết benchmark(self,m,n) dùng time.time và os.fork theo đề; bắt đầu đo trước tạo child, kết thúc sau wait đủ. | m,n int dương không bool; trả thời gian; child có n thread; lỗi child được báo; không bắt nhiều worker phải nhanh hơn. |

## Format bài mới

Mỗi nhiệm vụ có một mục tiêu chính. Trình tự: nêu vấn đề và fixture -> dự đoán ví dụ ngắn -> giải thích các bước -> tự viết hoặc sửa đoạn mã -> thử biến thể -> giải thích cơ chế. Ở bài tổng hợp, học viên nhận đề và dữ liệu mới trước; chỉ mở gợi ý sau lần nộp, ghi riêng assisted.

Mỗi hàm mới phải có tên/mục đích, tham số, dữ liệu trả về, tác dụng phụ và một ví dụ gọi. Mẫu code không dùng dấu chấm phẩy để dồn lệnh, không viết hàm một dòng. Comment giải thích lý do; không diễn giải từng ký tự gây dài dòng.

| Mức | Phần học viên tự viết | Hàm/phương thức | Hỗ trợ |
|---|---|---|---|
| Cơ bản | Thường 5-15 dòng; tích hợp B19-B20 có thể 25-30 dòng | 1 rồi 2; tối đa 3 ở Ex1 | Ví dụ nhỏ, tên biến rõ, trace từng bước |
| Trung cấp | Thường 10-25 dòng mới | Một class 2-3 phương thức, tách từng nhiệm vụ | Cấp class cha khi học class con |
| Nâng cao | Thường 15-40 dòng mới | Thêm một method hoặc script nhỏ mỗi nhiệm vụ | Cấp phần class đã học; lab POSIX cho fork |

Số dòng là ngân sách thiết kế, không phải tiêu chí chấm học viên. Bài quá dài phải tách mục tiêu hoặc cấp scaffold, không rút thành one-liner. Không đặt mức 2-3 hàm cho mọi bài: một hàm chứa 10 cơ chế mới vẫn quá tải.

## Chuẩn sẵn sàng thi đề xuất

1. Hoàn thành B20, I07, I12, N04, N08 bằng mã tự viết, trên fixture chưa thấy; mỗi bài có rubric cơ chế và test riêng.
2. Làm hai đề biến thể đủ 5 dạng, trong thời gian và điều kiện thi do giảng viên xác nhận. Hai lần không xem đáp án, không dùng AI/gợi ý; chấm trên thang chính thức khi có.
3. Đạt hoặc vượt điểm qua môn với biên dự phòng do giảng viên thống nhất, đồng thời đáp ứng mọi điểm sàn bắt buộc. Trước khi biết thang điểm, chỉ báo đạt/chưa đạt từng kỹ năng, không gán nhãn bảo đảm qua môn.
4. Nếu trượt gate, quay lại nhiệm vụ gốc tương ứng; không mở thêm wx/OpenGL để bù điểm yếu hàm, OOP hoặc vòng đời worker.

## Hợp đồng đề được chuẩn hóa

- Ex1: bản luyện phân biệt hoa/thường, giữ khoảng trắng, chỉ bỏ CR/LF cuối dòng, bỏ chuỗi rỗng; giữ thứ tự và trùng lặp. Các quy tắc này là thiết kế bổ sung cần giảng viên xác nhận.
- Ex2: sửa tên magic method thành __init__/__str__; thống nhất ProgrammingLanguage; list paradigms thuộc riêng từng object; add_paradigms cho thêm trùng. Format: Language[Python], Year created[1991], Paradigms['procedural'] (phần paradigms dùng repr(list), không bọc thêm cặp ngoặc ngoài).
- Ex3: thống nhất compile và std_version; __str__ nối , Standard version[C17]. compile in Compiling C code using standard version C17.
- Ex4: mỗi worker in Compiling C code using 3 threads with standard version C17 khi n=3. Không yêu cầu thứ tự, không hứa in đúng cùng thời điểm. start tất cả rồi join tất cả.
- Ex5: dùng os.fork và time.time theo đề; chạy lab Linux/WSL; parent đơn luồng tạo child, child mới tạo thread. Child không tiếp tục vòng fork của parent. Thời gian kết thúc sau khi waitpid đủ child. Không dùng stdout ngắn làm bằng chứng tăng tốc biên dịch.

## Xử lý A03 và A04 theo feedback

A03 curses ở thư viện tự chọn cho tới khi xác nhận thi: hiện một dòng -> q thoát -> ba lựa chọn -> thay selected -> Enter -> resize. Mỗi nhiệm vụ chỉ thêm một cơ chế, không đưa tất cả vào một hàm mẫu đầu tiên.

A04 nén ở thư viện tự chọn: gzip round-trip -> tự viết hai hàm -> if/elif chọn codec -> ZIP trên đĩa -> BytesIO/refactor nâng cao. Không mở đầu bằng dictionary module CODECS và chuỗi helper. Hai hàm dễ đọc ở examples/compression_beginner.py là mẫu sửa format, không nằm trong 40 bài để tỷ lệ không thay đổi.

C14 của v2 phải học sau P10 khi còn yêu cầu tự viết hàm. Không dùng thứ tự hiện tại của v2 làm thứ tự bắt buộc cho v3.

## Bàn giao và kiểm tra lại

roadmap_50_30_20.json chứa 40 hợp đồng bài và tiêu chí; lesson_format_v3.json là schema biên tập. Đây là blueprint, chưa phải ngân hàng 40 bài đầy đủ ví dụ/quiz/đáp án/test ẩn. examples/ chứa 3 mẫu theo mức + 1 mẫu sửa A04 để dev và tác giả thống nhất format. Bản v2 được giữ nguyên.

Kiểm tra nội dung khi triển khai: tỷ lệ đúng 20/12/8; mọi điều kiện học trước đã có; không có cú pháp mới chưa giải thích; học viên tự viết code ở mỗi bài; 5 dạng đề có gate độc lập; runtime POSIX nghiệm thu riêng; tỷ lệ PASS tự động không thay thế giải thích hoặc điểm thi.

Tài liệu kỹ thuật đối chiếu: https://docs.python.org/3/library/threading.html#threading.Thread.join và https://docs.python.org/3/library/os.html#os.fork .
