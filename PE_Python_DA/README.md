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
| `data/` | Các file dữ liệu bài học đọc được (tầng 2 của bộ sinh dữ liệu), kèm `NOTICE.md` ghi nguồn và giấy phép. |
| `dulieu/` | Tầng 0 và tầng 1 của bộ dữ liệu: tài liệu cho người soạn, do `gen_dulieu.py` sinh. |
| `check_vanphong.py` | **Cổng văn phong.** Đọc `source/` và `thuatngu.json`, đối chiếu từng luật với `van-phong-moc.json`. Chạy độc lập, không cần nền tảng. |
| `gen_dulieu.py` | Bộ sinh dữ liệu "Sổ của Quán Hạt Rang", seed cố định: chạy lại phải ra đúng từng byte thứ đang có ở `dulieu/` và `data/`. |
| `tools/anh-xa.json` | Ánh xạ giữa tệp trong gói và đường dẫn bên pe-usth. Một nguồn duy nhất, cả hai bên cùng đọc. |
| `tools/dong_bo.py` | Chép giữa gói này và một bản pe-usth có sẵn trên máy, đúng từng byte (xem phần quy trình). |

Số màn đọc, số câu hỏi, số bài chấm do bộ dựng tính chứ không khai tay; số đó trôi nên không chép vào đây. Muốn số hiện tại, xem bảng "Mốc nền" trong `AGENTS.md` của pe-usth.

## Quy trình sửa nội dung

**Mọi việc soạn và kiểm nội dung làm ở đây.** Các cổng chạy được từ nội dung thuần nằm trong gói này và chạy độc lập (Windows dùng `py -I`, Linux dùng `python -I`):

```
python -I PE_Python_DA/check_vanphong.py --doi-chieu   # văn phong: chỉ đỏ khi một luật TĂNG
python -I PE_Python_DA/gen_dulieu.py                   # sinh lại dữ liệu; git status phải sạch
```

Workflow `.github/workflows/noi-dung.yml` chạy lại đúng các cổng đó (cộng kiểm JSON và ánh xạ) trên mỗi push và pull request đụng tới `PE_Python_DA/`. Cổng văn phong tự đòi sửa `VAN-PHONG.md` mục 2 khi số câu giảng đổi; việc đó cũng làm ở đây, không còn vòng chép ngược từ nền tảng.

**Đưa nội dung sang nền tảng** là bước của repo pe-usth, tại một commit đã merge ở đây:

1. Merge nội dung vào `main` ở đây, ghi lại SHA.
2. Ở pe-usth: `node scripts/giao-trinh.mjs lay --sha <SHA>`. Lệnh lấy đúng các tệp trong `tools/anh-xa.json` tại SHA đó, ghi chúng vào cây của pe-usth và ghim SHA vào `scripts/pe-da/giao-trinh.json`. Không cần clone repo này.
3. Cũng ở pe-usth: dựng lại gói và chạy các cổng của nền tảng theo `AGENTS.md` của pe-usth (`build.py`, `check.py --strict`, `check-pyodide.mjs`, `check-practice.mjs`), rồi nạp DB. Nội dung chỉ tới người học sau khi người phụ trách nền tảng nạp; merge ở đây chưa có nghĩa là người học đã thấy.
4. `node scripts/giao-trinh.mjs` (không tham số) ở pe-usth kiểm bản chép đúng với SHA đã ghim. Sửa thẳng `scripts/pe-da/source/` ở pe-usth mà không qua đây sẽ làm lệnh đó đỏ.

`tools/dong_bo.py` là đường tắt khi bạn có sẵn cả hai repo trên máy và muốn thử một thay đổi chưa merge: `py PE_Python_DA/tools/dong_bo.py --nen-tang <thư mục pe-usth>` chỉ kiểm, thêm `--day` để chép sang pe-usth, `--lay` để chép về. Đừng dùng nó thay cho quy trình trên khi đưa nội dung thật lên.

**Ở lại pe-usth có chủ đích, không phải việc dở:** `build.py` (dựng gói theo định dạng của nền tảng, biết module nào chạy được trong trình duyệt), kiểm chạy code trong Pyodide, chấm bài tập, sinh vết từng bước (`gen_traces.py`, dùng bộ ghi vết của nền tảng) và nạp DB. Chúng cần runtime và định dạng gói của nền tảng; nội dung không phụ thuộc vào chúng.

## Giới hạn cần biết

- **Đáp án nằm trong repo công khai.** `source/practice.json` có đáp án trắc nghiệm, lời giải tham chiếu và ca chấm. Chỉ dùng cho người soạn; đừng đưa dữ liệu học viên, khoá truy cập hay thông tin hạ tầng vào repo.
- **Nguồn và giấy phép.** Nguồn của từng bài ghi ở các trường `provenance`, `sources` và `sourcePages` trong `source/course.json`: có bài đối chiếu trang slide USTH, có bài do người soạn viết riêng; ghi chú từng bài nói rõ phần nào là mới. Module 11 (TH01–TH07) viết trực tiếp trên bộ dữ liệu CC0 `coffee-sales-cc0.csv`. Slide và sách nguồn không có trong repo. Repo chưa có tệp `LICENSE`. Giấy phép của từng bộ dữ liệu: `data/NOTICE.md`.
- **Hai liên kết trong tài liệu không mở được trên GitHub** vì trỏ theo đường dẫn của pe-usth: `LUOC-DO.md` tới `NOTICE.md` và `data/NOTICE.md` tới `LUOC-DO.md`. Cố ý chưa sửa vì các tệp này được chép nguyên văn sang pe-usth; sửa chúng thì phải sửa ở cả hai cây cùng lúc.
- **Chưa có trong gói:** bản đã dựng (`lessons.json`) và các vết từng bước (`traces.json`), vì chúng do công cụ của pe-usth sinh ra và dựng lại được từ nội dung ở đây. Hình do bộ dựng chép từ gói gốc trên máy người soạn nên `figures/` là bản chép của ảnh đã dùng.
- **Hai chỗ gỡ phụ thuộc trong script.** `check_vanphong.py` và `gen_dulieu.py` có bản chép ở `pe-usth/scripts/pe-da/` và chạy ở đó không đổi hành vi. Chúng phân biệt hai nơi bằng việc có `build.py` ngay cạnh hay không: ở pe-usth cổng văn phong còn đối chiếu trần lint với `ci.yml` của nền tảng, ở đây thì bỏ bước đó; bộ sinh dữ liệu ghi tầng 2 vào `frontend/public/static/da-dulieu/` ở pe-usth và vào `data/` ở đây.

Nạp lần đầu từ pe-usth, nhánh `main` tại `eefb1944` (23/11/2026); đối chiếu mã băm từng tệp với bản đó. Hai script ở trên và `dulieu/` được chép sau đó, rồi sửa như đã nói.
