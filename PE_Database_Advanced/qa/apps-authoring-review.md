# AD60/AD81/AD82/AD85 — review nội dung và bằng chứng

Ngày 05/11/2026. Phạm vi biên soạn: bốn bài mới, Company Advanced overlay và engine evidence riêng. Không sửa old85, không nhập repo ngoài, không có ví hoặc tiền thật, không có production runner.

## Đối chiếu nguồn thực

- AD60: đọc trực tiếp toàn văn trích của Practice1–3 bằng pypdf và xem hình Practice1 trang5 bằng pypdfium2 trong bộ nhớ. Đọc Z01/Z02 và DDL của cả hai fixture nền. Kiểm đủ30 mã yêu cầu Northwind và sáu shape Company; phát hiện EMPLOYEE.Minit trong nguồn bị thiếu ở fixture PE. Overlay thêm riêng trong pe_advanced_company, không sửa baseline. Sáu PK, tám FK nguồn và FK partner bổ sung được phân biệt với NOT NULL/CHECK/UNIQUE do PE chọn.
- AD81: đọc sách cung cấp §26.1–26.3.3, đối chiếu lookup/Merkle §26.5.1. Bài có canonical encoding, giả định hash/preimage/collision, hash chain/checkpoint, Sign/Verify, cây Merkle cân bằng với input/output/pseudocode/trace/invariant/chi phí và UTXO validator với duplicate-input/double-spend/conservation proof. Chọn lịch sử chung chuyển tới AD54, không lặp bài đồng thuận.
- AD82: đọc sách §26.5.1–26.8, gồm mọi tiểu mục smart contract, external input, autonomy, cross-chain, consensus/query/fault/scalability và12 hướng ứng dụng. Có nonce/balance state machine, replay proof, gas termination dưới giả định bước có cost dương, oracle truth gap, query membership/completeness/watermark và read-model stale counterexample. Nội dung hệ của sách năm2019 được ghi lịch sử, không dùng làm benchmark hiện tại.
- AD85: đọc §5.2.1–5.3.3. Có caller transaction ownership, parameter/cursor/handler/error path, multi-row trigger và statement rollback, current-read caveat cho invariant liên dòng, DDL implicit commit, DELIMITER client/API, external routine/sandbox và giới hạn MySQL khác SQL chuẩn.

Các bài đều có ít nhất ba ca làm việc, bốn hoặc năm nhiệm vụ thực chất, hai mức gợi ý, đủ đáp án/lập luận, biến thể nhắm lỗi cụ thể và hoạt động web. Độ dài lớn hơn bài đơn vì AD60 là capstone hai miền và AD82 phải bao phủ tám tiểu mục cùng ứng dụng; không thay bằng danh sách API hay mapping rỗng.

## Engine QA đã thực hiện

Lượt trong `apps-mysql-verification.json` chạy thật trên MySQL8.4.13, loopback task-local, bằng PyMySQL. Kết quả33 kiểm tra đều pass. Schema được dùng: pe_advanced_appsqa, pe_advanced_company, pe_advanced_northwind; không kết nối ghi old85/company_pe/northwind_pe hay core schema đang phục vụ QA khác. File JSON giữ version/SQL mode/isolation, trạng thái actual/expected, danh sách FK và hash các file nguồn.

Các kiểm tra có ý nghĩa gồm credit overflow sau debit còn pending, caller rollback phục hồi; cursor200/0/20; một request khi12→8 và không lặp khi8→7; lỗi CHECK ở UPDATE nhiều dòng bỏ cả request trigger nhưng giữ INSERT trước đó tới khi rollback transaction; DDL commit DML trước nó; server API từ chối DELIMITER. Company kiểm round-trip Minit='T'/NULL, sáu PK và chín FK gồm partner, witness cycle qua được FK. Northwind report đúng ba customer với customer không đơn/đơn trống/thu thiếu, và fanout sai2080/2080 trên đơn31.

Lần kết nối đầu trong sandbox bị WinError10013 trước khi bất kỳ SQL chạy. Lượt đã được cho phép mở socket tới task-local server sau đó chạy toàn bộ33 kiểm tra thành công. Đây không phải lỗi SQL bị che đi.

## Phân biệt bằng chứng và giới hạn

Engine QA không thực thi blockchain, không đo query plan/benchmark, không kiểm lịch hai session của AD60 và không chứng minh cryptographic security. Hash/Merkle/ledger/gas có lập luận mô hình và rubric; UI tương tác chỉ là yêu cầu cho dev. Candidate index, fixture20.000 dòng và rental transfer task chưa có engine evidence ở file QA này. Mọi biến thể bổ sung cần QA riêng trước khi nhận là engine-tested.

Primary docs đã mở ngày05/11/2026: MySQL8.4 handlers/cursors/triggers/restrictions/implicit-commit/defining-programs/EXPLAIN; Bitcoin Developer Guide transactions; NIST FIPS186-5; RFC9162 §2.1; Ethereum smart-contracts và oracles. Chỉ diễn giải phần hỗ trợ claim tương ứng; không sao chép mã ngoài hay phát biểu quyền sử dụng repo chưa qua gate.

Không còn khoảng trống source cơ chế đã biết trong bốn bài được giao. Những hạng mục chưa triển khai/kiểm kể trên được ghi rõ là đề xuất hoặc giới hạn, không được tính là production completion.
