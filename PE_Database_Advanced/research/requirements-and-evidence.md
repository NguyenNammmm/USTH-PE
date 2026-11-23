# Yêu cầu và bằng chứng hoàn tất

Đây là checklist giữ nguyên phạm vi người dùng: khóa Advanced tiếp nối85 bài Database PE, đủ kiến thức của sách và slide, tự học có giải thích/ví dụ/thuật toán/chứng minh khi nguồn có, bài tập và đáp án. Người học làm mọi hoạt động trên web; MySQL chính, hệ khác khi cần. Đầu ra là README, một PDF, toàn bộ bài Markdown và HTML đặc tả tương tác.

| Yêu cầu | Bằng chứng hiện hành | Trạng thái |
|---|---|---|
| Đủ kiến thức sách và slide | 947 thân mục sách, 448 trang lecture, 10 trang practice; ledger và source/lesson hash hiện hành | Hai cổng đã đóng: 947/947 mục và 458/458 trang; 409 trang giảng, 49 trang không giảng |
| Nối tiếp85 bài nền | `baseline/` giữ nguyên hash85 bài, prerequisite DAG và mapping từng bài nền sang bài Advanced | Đã có; không bắt học lại cả bộ |
| Tự học ở mức Advanced | 85 bài AD01–AD85, 24 bài trọng tâm, 11 phần bổ sung USTH có 151 câu/đáp án | Lời giảng, ví dụ, thuật toán/lập luận và luyện tập được đối chiếu theo từng thân mục nguồn |
| Repo tìm/pull thật và kiểm chất lượng | Bốn commit được clone; registry/file hashes/licenses; test gốc và mutation;21 kiểm phần chọn | Nhận ba phần chuyển thể có giới hạn; BusTub để ngoài runtime |
| Phù hợp khóa thu phí | MIT/CC BY notices và mô tả phần dùng/thay đổi; không phân phối sách/raw clone/audio | Có hồ sơ theo đúng phần được chọn |
| Lab được biên tập lên web | Bảy activity contract, `activities.json`, seed/support/independent task/oracle/capability/evidence, links từ bài | Có đặc tả và demo hỗ trợ; chưa triển khai backend |
| Mọi thao tác learner trên web | `docs/web-runner-spec.md`: editor, hai session, observer, cancel/reset, sandbox/quota, engine/model/proof grading | Đã đặc tả. Deployment không nằm trong đầu ra lần này |
| MySQL chính, hệ khác khi cần | Engine provenance8.4.13; PostgreSQL/C/crash/cluster có capability và giới hạn riêng | Các ca được nêu đã kiểm; không nhận model là native |
| README | Đường vào bốn đầu ra, cách tích hợp và phạm vi xác minh | Phân biệt nội dung đủ nguồn với learner runner chưa triển khai |
| Một PDF có toàn bộ bài/key lessons | PDF builder: 85 bài, 11 phần bổ sung, 24 minh họa, mục lục/bookmarks; QA text/glyph/bounds/render | Chỉ nhận bản xuất có hash khớp báo cáo hiện hành; render lấy mẫu, bounds toàn bộ |
| Toàn bộ bài Markdown | 96 file hiện hành; snapshot 85 file nền giữ nguyên; luyện/đáp án và link | Manifest, nguồn và package checks giữ bằng chứng hiện hành |
| HTML đặc tả tương tác | Toàn bộ Markdown nhúng; bảy models, ba dạng hỗ trợ, source map và runner spec | DOM logic có báo cáo gắn hash HTML; browser bị URL policy chặn nên chưa nhận layout browser thật |
| QA trung thực | Phân tách semantic/engine/model/DOM/render/proof, hash và giới hạn | Source-content flag không chứng nhận hiệu quả học tập hoặc deployment |

## Cách đóng yêu cầu đầy đủ

Một mục chỉ được nhận đủ khi đã đọc source body và hình/thuật toán liên quan, chỉ ra đúng đoạn giảng, ví dụ/lập luận và luyện tập/đáp án tương ứng, rồi kiểm các witness còn khớp hash. Parent và child có phạm vi riêng. Kiến thức nền chỉ được tính nếu chính nội dung nền đã được đọc và đáp ứng mục ấy; không suy từ tên bài.

Lecture/practice phải kiểm các khái niệm, hình, yêu cầu và thực hành thật. Page map chưa là semantic proof. Khi còn `partial`, `unreviewed`, hash cũ hoặc mục thiếu, goal vẫn active và `manifest.allContentComplete=false`. Không thu nhỏ yêu cầu để vừa số bài đã tạo.

## Các nhóm thực thi tách riêng

- 32 ca PE trên MySQL;21 ca phần repo chọn;33 ca routine/Company/Northwind.
- 26 ca design/PG bổ sung gồm10 model và16 MySQL;13 kiểm đúng fixture Chinook được đóng gói.
- USTH06/07 có 41 ca, trong đó 15 ca MySQL; USTH08–11 có 106 ca, trong đó 78 ca MySQL. Một sửa ba đoạn lời giải thích sau lượt native được kiểm bằng tái dựng đúng hash cũ và chứng minh 37 SQL blocks không đổi ở `qa/usth-editorial-freshness.json`.
- Các nhóm model hữu hạn, DOM, cấu trúc và render có báo cáo riêng. Chúng không được cộng thành số SQL hoặc chứng minh thuật toán tổng quát.

Không có production web runner, native PostgreSQL/C ABI hoặc crash/cluster artifact được gắn nhãn đã thực thi trong gói. Đây là giới hạn bằng chứng được ghi, không phải cách thay thế mục tiêu đầy đủ nội dung nguồn.
