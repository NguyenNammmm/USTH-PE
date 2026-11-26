# PE Machine Learning

Gói nguồn giáo trình Machine Learning PE gồm 28 bài ML01–ML28 trong 6 module.
Tên thư mục `PE_Machine_Learning` theo cùng quy ước đặt tên với
`PE_Python_DA` và `PE_Database_Advanced` trong repository giáo trình của sếp.

Gói này là nguồn biên soạn độc lập để bàn giao và đối chiếu. Nguồn nội dung
gốc vẫn nằm ở `pe-ml-codex`; thư mục này không thay thế, không chỉnh sửa và
không tự động nhập vào website.

## Học liệu PRIMM

[Mở hướng dẫn và các bản HTML, PDF, Markdown](docs/PRIMM/README.md). Bộ này gồm 36 phiếu PRIMM và 603 câu ôn tập. [Nguồn phiếu](source/primm.json) và [ghi chú thiết kế](docs/HANDOVER-THIET-KE-BAI-HOC.md) dành cho người biên soạn.

Từ thư mục `PE_Machine_Learning`, dùng Python 3.10 trở lên để dựng và kiểm lại học liệu.

```powershell
python -m pip install numpy markdown-it-py
python -X utf8 tools/dung_primm.py
python -X utf8 tools/dung_primm.py --check
```

Dùng nút **In giáo trình** trong HTML để xuất PDF. Có thể in tự động bằng Node.js, Playwright và Chrome với `node tools/in_primm.cjs`.

## Cấu trúc

- `source/course.json`: nhóm module, tên bài, mức, tiên quyết, khái niệm,
  bài đọc và câu hỏi tự luận theo cấu trúc nguồn Python DA.
- `source/practice.json`: MCQ với `correctOption`, phản hồi từng lựa chọn;
  bài code với `starter`, `referenceSolution`, `hints`, `tests`.
- `source/questions.json`: ngân hàng 603 câu ôn đã biên tập cho PRIMM
  (269 MCQ và 334 câu tự luận), giữ mã bài và mã câu hỏi.
- `reference/studio-lessons.json`: bundle Studio gốc, giữ nguyên từng byte;
  có đầy đủ S1–S4, bao gồm scaffold và các trường runtime.
- `reference/course-catalog.json`: metadata catalog gốc.
- `reference/provenance.json`: nguồn và checksum đối chiếu.
- `docs/`: giáo trình hiệu đính và các quy cách ML hiện có.
- `SCHEMA.md`: quy tắc ánh xạ và giới hạn.
- `tools/dong_goi.py`, `tools/kiem_tra.py`: xuất lại và kiểm định.

## Quy ước bàn giao

`source/course.json` là danh mục biên soạn: module, thứ tự, tên bài, mức độ,
tiên quyết, khái niệm, bài đọc và tự luận. `source/practice.json` là phần luyện
tập: MCQ có ID lựa chọn và feedback riêng, cùng bài code có starter, lời giải,
gợi ý và test. `reference/studio-lessons.json` là bản lưu đầy đủ của bundle
`studio-lesson/v2`, vì vậy các trường S1–S4, scaffold và runtime không bị mất
khi chuyển sang cách tổ chức source/practice.

Mỗi bài có `id` duy nhất; thứ tự trong `groups[].ids`, `course.lessons` và
`practice.lessons` đều là ML01 đến ML28. Mức dùng ba giá trị `Cơ bản`, `Trung
cấp`, `Nâng cao`; tiên quyết chỉ tham chiếu mã ML trong cùng khóa.

## Kiểm tra

```bash
python3 tools/kiem_tra.py
```

Kết quả kiểm tra hợp lệ phải bắt đầu bằng `PACKAGE_PASS`. Có thể dựng lại gói
nguồn bằng:

```bash
python3 tools/dong_goi.py
python3 tools/kiem_tra.py
```

Đây là gói bàn giao nguồn nội dung, không phải website hoặc một khóa đã nhập
database. Gói nguồn có thể kiểm tra cục bộ bằng các lệnh dưới đây.
Các kiểm tra của gói Studio dùng dữ liệu tham chiếu gốc. Bản PRIMM có trình dựng và kiểm tra riêng.

## Giới hạn nghiệm thu

603 câu S2 hiện có được bảo toàn (269 MCQ, 334 tự luận). 28 bài thực hành
và các test có sẵn được mang sang nguyên vẹn. Kiểm định gói không thay thế
review sư phạm: một số scaffold/sandbox cũ còn đơn giản và cần rà soát độ sâu
so với mục tiêu bài học trước khi tuyên bố hoàn chỉnh nội dung.
Không coi `PACKAGE_PASS` là PASS trên browser, Pyodide, XP/tiến độ hoặc
pipeline Python DA; các trạng thái đó cần được kiểm thử riêng trên hệ thống
đích.
