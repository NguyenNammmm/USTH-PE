# Ghi chú khi đưa gói lên repo này

Gói này là bản phát hành `Database-Advanced-PE-2026-11-06` (thư mục `database-advanced`), đưa vào repo ngày 24/11/2026.
File `README.md` cùng thư mục là README của chính gói; file này chỉ nói những gì khác giữa bản gốc và bản ở đây.

## Khác biệt so với bản phát hành gốc: đúng MỘT

Địa chỉ email của một giảng viên USTH (xuất hiện 9 lần, trong 6 sổ cái QA ở `research/`: `semantic-slides-final-review.json`,
`semantic-slides-foundations.json`, `semantic-slides-lecture45-review.json`, `semantic-slides-lecture67-review.json`,
`slide-page-map.json`, `source-section-inventory.json`) được thay bằng `[email-giang-vien-da-che]`. Địa chỉ ấy không cần cho nội dung bài và repo này công khai.
Không có bài Markdown, README, `course-spec.html` hay tài liệu trong `docs/` nào chứa nó.

Hệ quả: `bytes` và `sha256` của đúng 6 tệp đó trong `release-files.json` đã được cập nhật, nên `release-files.json` vẫn khớp từng tệp
(455 tệp được liệt kê; `release-files.json` không tự liệt kê mình). Các script trong `build/` và `research/` có thể còn tham chiếu mã băm
cũ của 6 tệp này: chưa kiểm, vì chúng chạy trên máy người soạn. Bản chưa che còn ở máy người soạn.
Chưa kiểm được bên trong `Database-Advanced-PE.pdf` (chữ trong PDF bị nén); các bài Markdown dùng để dựng PDF không chứa địa chỉ ấy.

## Không bị loại bỏ gì

456 tệp = 455 tệp trong `release-files.json` + chính `release-files.json`. Theo lời khai `excluded` của gói, sách và slide gốc,
bản chép các repo, vendor/runtime/server và công cụ biên soạn đã lỗi thời không có trong gói ngay từ đầu.

## Giữ nguyên từng byte

`.gitattributes` đặt `PE_Database_Advanced/** -text` để git không đổi kiểu xuống dòng; nếu không, mã băm trong `release-files.json` sẽ lệch
trên Windows.

## Cần biết trước khi chia sẻ

- README của gói ghi đây là nội dung cho **khoá thu phí**, và nhánh này nằm trong repo **công khai**. Hạn chế truy cập là quyết định ở cấp repo, không ở cấp gói.
- Gói chưa có runner; cả 85 bài trong `manifest.json` đều ở trạng thái `authored-pending-review`.
- Nội dung xây từ giáo trình USTH và *Database System Concepts* 7e; giấy phép của các tài liệu bên thứ ba ghi ở `research/licenses/THIRD-PARTY-NOTICES.md`. Repo này chưa có tệp `LICENSE`.
