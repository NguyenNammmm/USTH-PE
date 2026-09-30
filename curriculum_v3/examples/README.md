# Mẫu bài theo độ khó

Các file .py là đáp án mẫu dành cho tác giả/dev, không cấp sẵn nguyên lời giải challenge cho người học. Đây là 3 mẫu format và 1 mẫu A04 tự chọn, không phải toàn bộ ngân hàng 40 bài.

## B09 Cơ bản Tự viết hàm kiểm tra palindrome

Mục tiêu: nhận một chuỗi và trả True/False bằng một hàm. Học trước slicing, so sánh, if và return.

Đề: viết is_palindrome(text). Chuỗi rỗng trả False; các chuỗi khác chỉ đúng khi đọc xuôi bằng đọc ngược. Không đổi hoa/thường, không bỏ khoảng trắng. Hàm không print.

Ví dụ: level -> True; python -> False; Level -> False. Dự đoán kết quả của chuỗi a trước khi chạy.

Giải thích mẫu: nhánh đầu xử lý chuỗi rỗng; biến reversed_text giữ chuỗi đảo; phép so sánh tạo giá trị bool và return đưa nó về nơi gọi. Không cần helper khác.

Phần học viên nhận:

```python
def is_palindrome(text):
    pass
```

Thực hành: tự viết hàm, rồi thử level và python. Chuyển giao: tự dự đoán rồi chạy radar, Level và chuỗi rỗng. Đáp án ở palindrome_basic.py.

Chấm: đúng cả ca thường/biên, không in, không chuẩn hóa trái hợp đồng. Giải thích vì sao Level khác level; đạt khi nối được input, phép đảo và phép so sánh. Bài tiếp theo mới nối hàm này với hàm lọc list.

## I12 Trung cấp Viết class con C

Mục tiêu: áp dụng khởi tạo lớp con, super và override đã học trong I08-I11. Cấp language_base.py, không bắt viết lại class cha trong bài này.

Đề: viết class C với constructor nhận name, year_created, paradigms, std_version. Gọi constructor cha; __str__ giữ thông tin cha và nối Standard version; compile in một thông báo dùng phiên bản hiện tại.

Ví dụ: C("C",1972,["procedural"],"C17") có str là Language[C], Year created[1972], Paradigms['procedural'], Standard version[C17]. compile() in Compiling C code using standard version C17.

Ba method có ba trách nhiệm: __init__ thiết lập state và trả None; __str__ trả chuỗi, không print; compile in một dòng và trả None. super().__str__ gọi hành vi cha; str(self) trong __str__ sẽ gọi lại chính method hiện tại.

Phần học viên nhận: import ProgrammingLanguage và ba tên method có pass. Ở bài tự kiểm tra I12 không hiện mã mẫu trước lần nộp; mẫu từng phần nằm ở I09-I11. Chuyển giao: tạo C23, kiểm lại chuỗi và thông báo. Đáp án ở inheritance_intermediate.py.

Chấm: constructor lưu đủ bốn trường, isinstance đúng, hai object độc lập, __str__ không in, compile in đúng. Học viên giải thích dữ liệu nào do class cha khởi tạo và phần nào class con bổ sung.

## N03 Nâng cao Chạy nhiều thread

Mục tiêu: nối tạo/start/join để hoàn tất n công việc. Cấp class C từ I12 và chữ ký helper; mỗi bước chỉ thêm một phần. Không đưa fork vào bài này.

Đề: bổ sung helper _compile_worker(n) và parallel_compile(n). Mỗi worker in thông báo chứa n và std_version. n phải là int dương, không bool. Khi parallel_compile trả về, mọi worker phải xong; thứ tự output không cố định.

Helper nhận n, đọc std_version, in một dòng và trả None. parallel_compile nhận n, tạo danh sách worker, start hết danh sách rồi join hết danh sách, không trả dữ liệu. args=(n,) là tuple một phần tử cấp tham số cho target; không dùng target=self._compile_worker(n) vì sẽ gọi ngay.

Ba checkpoint: (1) tạo list đúng n thread chưa chạy; (2) start toàn bộ; (3) join toàn bộ rồi báo hoàn thành. Mỗi checkpoint giải thích đối tượng Thread khác công việc đã chạy. Chuyển giao: đổi n=1 thành n=3; sửa bản start/join trong cùng vòng lặp. Đáp án ở threads_advanced.py.

Chấm: n công việc chạy ở worker thread, có đủ start trước join, tất cả hoàn thành trước khi method trả về, dữ liệu sai báo ValueError. Không suy ra đúng concurrency chỉ từ n dòng in. Không yêu cầu tăng tốc hay bắt đầu đúng cùng một thời điểm.

## A04 Mẫu sửa cho thư viện tự chọn

Mục tiêu chặng đầu: hai hàm riêng, một nén bytes bằng gzip và một khôi phục bytes. Đáp án ở compression_beginner.py.

Luồng dữ liệu: data -> compress_data -> compressed_data -> restore_data -> original_data. Mỗi hàm chỉ có một nhiệm vụ. Thử b"Hello" và bytes rỗng; điều kiện đúng là khôi phục bằng dữ liệu ban đầu. Không yêu cầu dữ liệu nén luôn nhỏ hơn.

Chưa đưa bz2/zlib, CODECS, BytesIO, ZIP và kiểm tra tên file vào chặng này. Đó là các nhiệm vụ kế tiếp trong thư viện, ngoài tỷ lệ 40 nhiệm vụ bắt buộc.
