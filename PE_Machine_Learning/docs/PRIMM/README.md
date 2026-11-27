# Machine Learning PE · Bộ học liệu PRIMM

Bộ học liệu có 28 bài chính và 8 bài bổ sung. Các phiếu dùng số, ma trận, nhãn và đoạn mã ngắn. Bạn có thể đưa từng câu vào một hoạt động tương tác trong PE.

| Tệp | Cách dùng |
|---|---|
| [Bản HTML](Machine-Learning-PE-PRIMM.html) | Chọn phiếu, dự đoán, sửa và chạy mã Python, nộp kết quả, xem phản hồi. |
| [Bản PDF](Machine-Learning-PE-PRIMM.pdf) | In trang đề trước. Bộ S dành cho buổi sau có phụ lục đề riêng. Hai phần đáp án nằm sau phụ lục ấy. |
| [Bản Markdown](Machine-Learning-PE-PRIMM.md) | Chỉnh nội dung, tìm theo mã câu và tra đáp án trong phụ lục. |

[Sơ đồ lộ trình học](Lo-trinh-hoc.md) cho thấy thứ tự theo tuyến và bài tiên quyết của từng chủ đề.

## Trình độ đầu vào ước tính

Khóa này phù hợp với người đã học một học phần lập trình nhập môn, thường vào cuối năm nhất hoặc năm hai các ngành máy tính, dữ liệu và kỹ thuật. Đây là ước tính từ các thao tác trong bài. Để vào ML01, bạn nên tự viết được một hàm Python nhỏ, dùng danh sách, vòng lặp, điều kiện và đọc một thông báo lỗi. Với NumPy, hãy biết tạo mảng và lấy một hàng hay cột. Bạn sẽ học các thuật toán học máy (machine learning) qua từng phiếu.

Trước ML05, hãy ôn đạo hàm của hàm bậc hai. Trước ML10–ML11 và ML22, cần đọc được phép nhân ma trận, đạo hàm sigmoid và quy tắc chuỗi. Trước ML25, ôn vectơ riêng và trị riêng. Các kỹ năng này có thể học dần theo lộ trình.

## Một lượt học

Ghi dự đoán ở A, chạy và sửa mã ở B, giải thích một phép tính ở C. Ba lượt D dùng lại cùng phương pháp. Đóng mẫu trước bốn đề E và nộp riêng từng kết quả. Bạn cũng tự viết một hàm để chạy các ca kiểm. Mở F khi đạt ít nhất 3/4 vị trí E, trong đó E2 bắt buộc đúng. Nếu đã xem đáp án, dùng bộ R cùng số để chứng minh lại. Đầu buổi sau, làm S từ đầu và ghi kết quả riêng.

- **A–C** · Ghi dự đoán, chạy đoạn mã mẫu và giải thích một giá trị bằng phép tính.
- **D** · Làm ba lần với đề cố định. Nút đưa D vào ô chạy thay các đối số bằng bộ số của lượt đang chọn.
- **Ví dụ có lời giải** · Mỗi chủ đề có thêm ba bộ dữ liệu với cách tính và kết quả để đối chiếu trước khi làm E.
- **E** · Mỗi đề E1–E4 nhận một kết quả riêng. Viết thêm hàm Python và chạy các ca kiểm. Việc viết hàm có thể thực hiện trong trình duyệt hoặc bằng tệp tải xuống.
- **Làm lại** · Sau khi mở đáp án, thử Ri ở cùng vị trí với Ei. Mỗi vị trí được tính một lần. Phản hồi chỉ ra phép tính, trục hoặc quy ước cần kiểm.
- **F và S** · Khi đủ ba vị trí và đạt vị trí 2, phần vận dụng mở ra. Dành bộ S cho buổi sau và ghi kết quả riêng với E.

Khi nhập kết quả, dùng dấu chấm thập phân, ngoặc vuông cho vectơ, ma trận và các kết quả ghép. Dùng dấu ngoặc kép cho chuỗi và null cho giá trị không xác định. Với số thập phân dài, giữ ít nhất 7 chữ số sau dấu chấm. Riêng ML05, giữ đến 10 chữ số nếu cần.

## Ngân hàng ôn tập

603 câu được gắn mã theo 28 bài chính, gồm 269 câu trắc nghiệm và 334 câu tự luận hoặc viết mã. Tám bài bổ sung có các lượt D, E, R, S, phần viết hàm và bài vận dụng riêng. HTML hiện phản hồi sau lần nộp. Câu tự luận dùng lời giải để người học tự đối chiếu.

## Chạy Python

Thiết kế tham chiếu thao tác ghi dự đoán, xem kết quả và thử mã trong [bài Python của PE](https://www.programmingedu.io.vn/lesson/python_advanced?lesson=1).

Trình duyệt tải Pyodide 0.27.7 và NumPy ở lần chạy đầu. Trình duyệt lưu tiến độ và mã đã sửa trên thiết bị qua localStorage. Khi mở PDF hoặc Markdown, hãy ghi đáp án từng lượt vào phiếu riêng trước khi tra phụ lục. Có thể cài NumPy trên máy và tải tệp Python từ ô viết mã để làm việc ngoại tuyến.

## Quy mô và quy ước

Có 108 ví dụ có lời giải, 108 lượt D, 144 đề E, 144 đề làm lại R, 36 đề S và 151 ca kiểm hàm. Emulate AI đã trả về 92 đoạn gợi ý cho lời dẫn của 36 phiếu và phần đề của toàn bộ 603 câu. Bản cuối đã được biên tập tiếng Việt, đối chiếu công thức, dữ liệu và quy ước trả lời. Đáp án số trên mỗi phiếu được tính lại bằng NumPy. Các thống kê này mô tả thiết kế học liệu. Điểm E và kết quả S sau một khoảng nghỉ là hai số đo nên thu riêng khi thử nghiệm với người học.
