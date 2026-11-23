# PE_Python_DA — Python cho Data Analyst

Giáo trình đang chạy trên [programmingedu.io.vn](https://programmingedu.io.vn): **179 bài, 11 module**. Từ 23/11/2026 đây là **nơi duy nhất để soạn và sửa nội dung**; nền tảng ([pe-usth](https://github.com/ProgrammingEdu-USTH/pe-usth)) chỉ dựng, chấm và nạp.

Bài được viết thành bài ĐỌC-HIỂU: lời giảng ngắn, đoạn code kèm kết quả in ra, câu luyện tập kèm đáp án mẫu. Mọi ví dụ nối vào một câu chuyện chung, hành trình mở một quán cà phê ([CAU-CHUYEN.md](CAU-CHUYEN.md)). Lớp luyện tập (trắc nghiệm và bài tập có ca chấm) nằm riêng ở `source/practice.json`.

## Có gì ở đây

| Đường dẫn | Là gì |
|---|---|
| `source/course.json` | **Nguồn chính.** `groups` (11 module) và `lessons` (179 bài): lời giảng, code, kết quả, câu luyện tập, nguồn tham khảo. |
| `source/practice.json` | Lớp luyện tập theo từng bài: `mcq` (đáp án đúng, giải thích từng lựa chọn) và `exercises` (đề, lời giải tham chiếu, ca chấm, gợi ý). |
| `thuatngu.json` | Sổ thuật ngữ: thuật ngữ nào gọi tiếng Việt hay tiếng Anh, chú giải mẫu, bài nào dùng đầu tiên. |
| `boi-canh.json` | Miền ví dụ máy đọc được (tên bảng, cột, nhân vật của quán). |
| `mcq-bo-code.json` | Câu trắc nghiệm nào gắn kèm đoạn code nào. |
| `van-phong-moc.json` | Mốc của cổng văn phong: số lỗi từng luật hiện có, chỉ được giảm. |
| `SCHEMA.md` | Đặc tả định dạng bài. |
| `LUOC-DO.md` | Lược đồ bộ dữ liệu "Sổ của Quán Hạt Rang": bảng nào có cột gì, đơn vị gì, bài nào dùng. |
| `CAU-CHUYEN.md` | Câu chuyện xuyên suốt và bài nào nối với bài trước ở đâu. |
| `VAN-PHONG.md` | Luật văn phong (độ dài câu, thuật ngữ, chú giải) mà cổng kiểm thi hành. |
| `figures/` | 80 hình biểu đồ (PNG) mà bài trỏ tới. |
| `data/` | Các file dữ liệu bài học đọc được, kèm `NOTICE.md` ghi nguồn và giấy phép. |
| `tools/dong_bo.py` | Chép hai chiều giữa gói này và cây của pe-usth, đúng từng byte. |

Số màn đọc, số câu hỏi, số bài chấm do bộ dựng tính chứ không khai tay; số đó trôi nên không chép vào đây. Muốn số hiện tại, xem bảng "Mốc nền" trong `AGENTS.md` của pe-usth.

## Quy trình sửa nội dung

Bộ dựng (`build.py`), các cổng kiểm (cấu trúc, văn phong, chạy code trong trình duyệt, chấm bài tập) và việc nạp vào DB **vẫn nằm ở pe-usth** và đọc nội dung từ cây của pe-usth. Vì vậy quy trình chuyển tiếp là:

1. Sửa trong thư mục này, commit.
2. Chép sang pe-usth: `py PE_Python_DA/tools/dong_bo.py --nen-tang <thư mục pe-usth> --day`. Bỏ `--day` để chỉ kiểm: công cụ in tệp khác hoặc thiếu và thoát 1 nếu có.
3. Ở pe-usth: dựng lại gói và chạy các cổng theo `AGENTS.md` của pe-usth (`build.py`, `check.py --strict`, `check_vanphong.py --doi-chieu`, `check-pyodide.mjs`, `check-practice.mjs`). Thêm hoặc bớt câu giảng thì cổng văn phong đòi sửa số trong `VAN-PHONG.md` mục 2.
4. Nếu bước 3 sửa `VAN-PHONG.md` hoặc `van-phong-moc.json`, chép về: `... dong_bo.py --nen-tang <pe-usth> --lay`, rồi commit ở đây.
5. Nội dung chỉ tới người học sau khi người phụ trách nền tảng nạp vào DB. Sửa xong ở đây chưa có nghĩa là người học đã thấy.

**Việc chưa làm:** chuyển bộ dựng và các cổng kiểm về đây để không phải chép qua lại. Chúng gắn với nền tảng (`check_vanphong.py` đọc `ci.yml` và gói đã dựng, `gen_dulieu.py` ghi thẳng vào `frontend/public`), nên chuyển phải sửa code chứ không chép được.

## Giới hạn cần biết

- **Đáp án nằm trong repo công khai.** `source/practice.json` có đáp án trắc nghiệm, lời giải tham chiếu và ca chấm. Chỉ dùng cho người soạn; đừng đưa dữ liệu học viên, khoá truy cập hay thông tin hạ tầng vào repo.
- **Nguồn và giấy phép.** Nguồn của từng bài ghi ở các trường `provenance`, `sources` và `sourcePages` trong `source/course.json`: có bài đối chiếu trang slide USTH, có bài do người soạn viết riêng; ghi chú từng bài nói rõ phần nào là mới. Module 11 (TH01–TH07) viết trực tiếp trên bộ dữ liệu CC0 `coffee-sales-cc0.csv`. Slide và sách nguồn không có trong repo. Repo chưa có tệp `LICENSE`. Giấy phép của từng bộ dữ liệu: `data/NOTICE.md`.
- **Ba liên kết trong tài liệu không mở được trên GitHub** vì trỏ tới công cụ hoặc đường dẫn của pe-usth: `LUOC-DO.md` tới `gen_dulieu.py` (bộ sinh dữ liệu, ở `pe-usth/scripts/pe-da/`) và tới `NOTICE.md`; `data/NOTICE.md` tới `LUOC-DO.md`. Cố ý chưa sửa để bản ở đây còn giống hệt bản ở pe-usth.
- **Chưa có trong gói:** bản đã dựng (`lessons.json`) và các vết từng bước (`traces.json`), vì chúng do công cụ của pe-usth sinh ra và dựng lại được từ nội dung ở đây. Hình do bộ dựng chép từ gói gốc trên máy người soạn nên `figures/` là bản chép của ảnh đã dùng.

Nạp lần đầu từ pe-usth, nhánh `main` tại `eefb1944` (23/11/2026); 96 tệp, đối chiếu mã băm từng tệp với bản đó.
