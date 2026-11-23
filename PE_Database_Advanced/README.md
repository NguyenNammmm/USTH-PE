# Database Advanced · Chặng sau 85 bài Database PE

Bộ này nối tiếp 85 bài hiện có, xây dựng từ giáo trình USTH và Database System Concepts7e. Đây là nội dung PE biên soạn cho khóa thu phí, với toàn bộ hoạt động của học viên trên web. Lời giảng tiếng Việt giữ và giải thích thuật ngữ tiếng Anh. MySQL là hệ thực hành chính; PostgreSQL hoặc hệ khác có môi trường riêng khi mục tiêu bài cần.

**Phạm vi nội dung:** 85 bài Advanced, 24 bài trọng tâm và 11 phần bổ sung USTH. Đã đối chiếu đủ 947 thân mục sách và 458 trang lecture/practice với Markdown hiện hành; 409 trang có nội dung giảng, 49 trang bìa/mục lục/chia phần được phân loại riêng. Các phần bổ sung có 151 câu hỏi kèm đáp án. Đây là nội dung và đặc tả triển khai cho dev; runner sản phẩm chưa được triển khai trong gói. Xem [phạm vi kiểm chứng](docs/verification-scope.md) và các báo cáo QA gắn với bản xuất để biết chính xác phần đã chạy/đã kiểm.

## Bốn phần bàn giao

| Phần | Đường dẫn | Vai trò |
|---|---|---|
| README | File này | Phạm vi, cách đọc và hướng tích hợp |
| PDF đầy đủ | [Database-Advanced-PE.pdf](Database-Advanced-PE.pdf) | Toàn bộ bài Advanced, ví dụ, thuật toán/lập luận, bài tập, hints, đáp án và phụ lục |
| Toàn bộ bài Markdown | [lessons/](lessons/) | 85 bài mới AD01–AD85;24 bài trọng tâm và các phần bổ sung USTH |
| HTML đặc tả | [course-spec.html](course-spec.html) | Lộ trình, nhắc tiên quyết, đọc bài, các mô hình tính lại và đặc tả web cho dev |

Thư mục `baseline/` giữ nguyên85 bài trước để truy vết và ôn kiến thức. Không có yêu cầu học lại cả bộ. Những lệnh cài/chạy native trong snapshot cũ là tài liệu đầu vào lịch sử, không phải yêu cầu học viên của chặng web này. Runner/CMS phải chuyển thao tác vận hành cũ sang capability web tương ứng khi mở bài ôn.

Mở HTML trực tiếp sau khi giữ nguyên cấu trúc thư mục. Trang chứa nội dung và model code, không cần CDN/API để đọc và tính mô hình. Nó chưa phải một backend thực thi SQL tùy ý. Khi dev nối runner, kết quả engine thật cần provenance/attempt theo contract; không thay một output chuẩn bị rồi gọi đó là lượt code mới đã chạy.

## Phạm vi nguồn và độ sâu

Nguồn đã chốt gồm 9 lecture,3 practice USTH và Database System Concepts7e:26 chương in, AppendixA,6 chương online27–32. Inventory trích947 mục/tiểu mục có cả parent và child; không diễn giải thành947 khái niệm độc lập. [Bản đồ nguồn](docs/coverage-map.md) và [báo cáo rà độ sâu](qa/independent-depth-review.md) phân biệt vị trí được gán với bằng chứng nội dung thực.

Các bài viết mới theo kiến thức, không sao chép toàn văn sách. Chặng mới giải thích sâu thuật toán/invariant/proof, nhiều ca và các điều kiện giới hạn; phần đã biết từ bộ nền có đường mở đúng bài. Nguồn raw sách/slide và clone repo phục vụ kiểm ở workspace không được đóng gói như tài sản nội dung để bán lại.

[USTH01](lessons/USTH01.md) bổ sung cách đọc kiến trúc/chọn công cụ;[USTH02](lessons/USTH02.md) bổ sung biểu thức,cây và ràng buộc đại số;[USTH03](lessons/USTH03.md) bổ sung SQL/Company và DDL/DML tự làm. Ba phần có35 câu hỏi kèm lời giải, được gắn với trang nguồn ở [cổng slide](docs/slide-semantic-coverage-status.md). Chúng là tài liệu tra cứu; dev chia thành lượt luyện ngắn theo kỹ năng.

[USTH04](lessons/USTH04.md) dạy join, bag/set và group/HAVING; [USTH05](lessons/USTH05.md) dạy suy FD, tìm mọi key và chuẩn hóa theo đúng giả định. Hai phần thêm 18 câu hỏi có lời giải.

[USTH06](lessons/USTH06.md) dạy đọc ERD và mapping thành bảng; [USTH07](lessons/USTH07.md) dạy index, view, procedure và trigger, ghi rõ MySQL với SQL Server. Hai phần thêm 20 câu hỏi, đưa tổng lên 73 câu có đáp án. Bảy phần nằm cùng thư mục bài Markdown và được manifest ghi riêng để giữ nguyên ID AD01–AD85. [Acceptance web cho Lecture 6–7](docs/usth67-web-acceptance.md) có fixture, capability và các ca engine phải kiểm. Lượt kiểm hiện hành có 41 ca, trong đó 15 ca chạy thật trên MySQL 8.4.13; không có lượt chạy SQL Server.

[USTH08](lessons/USTH08.md) mapping bốn ERD; [USTH09](lessons/USTH09.md) nối SDLC, AMS và quy trình thiết kế; [USTH10](lessons/USTH10.md) giữ đủ 36 nhiệm vụ của ba practice; [USTH11](lessons/USTH11.md) có 24 bài report/chart từ Lecture 9. Bốn phần thêm 78 câu có đáp án, nâng tổng phần bổ sung lên 151 câu. Lượt kiểm SQL/fixture và phản ví dụ của nhóm này có báo cáo riêng; các số liệu PE không được gọi là dump/đáp án số liệu gốc USTH.

## Dev nên xem theo thứ tự

1. [Cách học và lộ trình](docs/course-design.md).
2. Mở HTML, chọn một bài trọng tâm và thử thay input ở các model.
3. [Runner web đầy đủ](docs/web-runner-spec.md): capability, hai session, cancel/reset, query/DDL/crash isolation, attempt và checker.
4. [Thiết kế dạy và rubric](docs/teaching-contract.md), [lab từ repo](docs/repo-labs.md).
5. [Registry/kiểm định repo](research/repo-quality.md) và [license/notice](research/licenses/THIRD-PARTY-NOTICES.md).
6. Các báo cáo trong `qa/`, đọc phạm vi từng kiểm trước khi dùng nhãn đã chạy/đạt.

PDF và Markdown là bản tham khảo đầy đủ của các bài đã biên soạn. Trên màn hình học, dev chia theo ví dụ và việc người học cần làm, có nhắc lý thuyết đúng chỗ; không bắt đọc nguyên một bài dài rồi mới cho luyện. [Ví dụ chia AD85 thành các lượt học](docs/ad85-learning-sequence.md) minh họa cách chọn dạng bài theo kỹ năng, chuyển từ hỗ trợ sang tự làm và giữ lịch sử gợi ý.

## Các cơ chế được minh họa

HTML có attribute closure, conflict graph, external sort, interval dynamic programming, ROWS/RANGE, ARIES/CLR và grow-only counter. Các thuật toán tính lại trên input hữu hạn; giả định/cost unit được nêu. Mô hình DP không được gọi là một optimizer MySQL; modelARIES không được gọi là nativecrashtrace; kiểm hữu hạn không thay chứng minh tổng quát.

Practice demo có các kiểu đáp ứng khác nhau theo seed: dự đoán ID, điền expected result và chọn counterexample có giải thích. Seed và dấu mở hint/answer được giữ khi storage browser cho phép. Đây là hỗ trợ trước bài tự viết; không tự xác nhận thành thạo từ một click đúng.

## Repo đã chọn

- Hermitage: lịch isolation được biên tập và chạy lại bằng hai kết nối MySQL8.4.13; không nhập nguyên kết luận của bản MySQL5.6.
- Chinook: fixture MySQL được kiểm số lượng/FK/Decimal/running totals; đề mới và oracle doPE biên soạn.
- E-commerce optimizer demo: chỉ nhận phần đã sửa và kiểm bổ sung. Năm test gốc vẫn pass khi helper luôn trả `[]`, nên checker upstream không đạt để dùng nguyên trạng.
- BusTub: đã clone/đọc source và license nhưng chưa build/test C++; để ngoài bài bắt buộc. Không phân phối lời giải course của sinh viên.

Registry ghi exactcommit/filehash, license, scope được nhận và giới hạn. MIT/CC BY grants phải được giữ cùng phần dùng; việc khóa thu phí không thay các quyền cần tôn trọng. Không có tuyên bố một repo đạt toàn bộ chỉ từ số sao hoặc một lần chạy xanh.

## Chạy trên web nghĩa là gì?

Học viên thao tác editor, modelcanvas, hai lane session, form nộp proof hoặc project trong website. Backend cấp environment/credential/quota đúng bài; học viên không cài DBMS,Docker hoặc compiler cá nhân. Dev có thể dùng hạ tầng đó ở server.

Các môi trường độc lập gồm MySQL single-query, DDL/DML, hai-session, measurement, disposablecrash/restore, cluster và PostgreSQL/extension theo nhu cầu. Schema riêng không tự cô lập performance/crash; spec yêu cầu instance/resource isolation khi mục tiêu cần. Chưa có capability thật thì trả trạng thái chưa hỗ trợ, không giảPASS bằng animation.

## Fixture và kiểm chứng

`fixtures/advanced_core.sql` cùng generator trong verifier tạo dữ liệu mới ở `pe_advanced_core`. [Company Advanced overlay](fixtures/company_advanced_overlay.sql) bổ sung trườngMinit mà Practice1 gốc có nhưng fixture nền thiếu; không sửa snapshot85 bài. BảnCompany/Northwind vẫn là PE dựng lại, không được gọi là dump hoặc barem gốc USTH.

Báo cáo engine có các nhóm PE mới, selected-repo, routine/Company/Northwind và hai nhóm bổ sung USTH được ghi riêng trong `qa/`. Các nhóm có phạm vi khác nhau, không cộng số ca thành lời hứa mọi SQL trong 85 bài đã chạy. Native PostgreSQL/C extension/crash/cluster chỉ được nhận đã kiểm khi có artifact riêng; code-reading và model giữ nhãn tương ứng. Bản Review-v2 cũ là mốc lịch sử; đối chiếu hash của từng file hiện hành trong [release-files.json](release-files.json) đi kèm gói này.

`qa/` còn có kiểm model, cấu trúc, nguồn, nội dung và các lượt rà độc lập. Kiểm phần mềm/PDF không chứng minh hiệu quả học tập. Chưa có pilot để xác lập ngưỡng mastery hoặc thời lượng tối ưu. Đọc [phạm vi xác minh](docs/verification-scope.md) trước khi đưa vào nghiệm thu production.

## Dữ liệu tích hợp

`manifest.json` giữ ID mới, module, key, old/new prerequisites, source sections và đề xuất thứ tự hợp lệ. FileMarkdown là nội dung tác giả; đề/rubric cần chuyển thành activityrecords có version/seed/capability trongCMS. Source inventory và repo registry giữ provenance. `baseline/snapshot-provenance.json` chứng minh các bài nền được sao giữ nguyên.

Script QA/build trong gói là công cụ biên soạn trên máy hiện tại; runtimepath/port cần được dev cấu hình, không đưa nguyên lệnh đó thành thao tác của học viên. Không có mật khẩu, server portable, vendor thư viện hoặc toàn văn giáo trình trong phần phát hành.
