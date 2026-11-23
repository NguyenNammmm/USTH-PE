# Rà soát biên soạn AD83–AD84

Phạm vi: chỉ hai bài mới AD83 và AD84, tiếp nối AD55/AD57/AD58; không thay đổi bộ Database PE 85 bài. Ngày biên soạn: 05/11/2026. Đây là rà soát nội dung và trace suy luận; không phải xác nhận một runner PostgreSQL/C đã triển khai.

## Nguồn thực đã đọc

- `tmp/database-source/online-32.txt`: §32.8.4, §32.8.5–32.8.7, §32.8.8.1 và sơ đồ 32.10.
- `output/database-advanced/authoring-contract.md`, `context-decisions.md`, records AD83/AD84 trong `research/proposed-lessons.json`.
- AD55–AD58 để giữ ranh giới prerequisites và tránh lặp hàm cộng extension của AD58.
- Official PostgreSQL documentation 18: C functions, heap page/row layout, TOAST; source chính thức `REL_18_0` cho mcxt.c, memutils.h, mmgr/README và tuptable.h; nhánh `REL_18_STABLE` cho nodes.h và nodes/README. URLs đặt trong từng bài. Không dùng line number cố định từ nhánh đang thay đổi.

## Coverage và bằng chứng học

| Bài | Cơ chế chính | Ca biên/phản ví dụ | Chuyển giao | Algorithm/proof |
|---|---|---|---|---|
| AD83 | owner/context/switch/copy trước reset | alias qua reset; context quá dài; reset ancestor | nhãn dài nhất; bài độc lập top-two và rescan | invariant prefix và lifetime; dừng; O(n+L), payload O(m) với giả định |
| AD84 | Node prefix/tag/dispatch/deep copy | Datum 0 khác NULL; text không phải C string; layout/alignment | giữ note qua slot reuse; Multiply; copy tuple | structural induction cho clone; invariant decode/projection; dừng/chi phí |

Cả hai bài có ba ví dụ khác vai trò, C tối thiểu giải thích tại chỗ, năm nhiệm vụ, hai mức gợi ý, đáp án đầy đủ, biến thể, web mode, năm trạng thái minh họa và hai dạng hoạt động hỗ trợ. Hoạt động chuyển giao có yêu cầu mới, không chỉ đổi tên biến trong happy path.

## Khác biệt phiên bản đã xử lý

1. Parent khi tạo context là đối số API; không chép khẳng định giản lược của sách rằng parent luôn là current.
2. `MemoryContextReset` tại `REL_18_0` giữ context đích, xóa descendants; `ResetOnly` khác. Handle child không còn dùng được sau reset parent.
3. Không gọi mỗi lần return từ expression là một reset bắt buộc; mốc reset cần đọc ở caller/control flow cụ thể. Không đồng nhất cursor fetch, query và transaction.
4. Node support ở nhánh 18 có code generation/attributes, không áp quy trình sửa enum/copy/equal thủ công của sách cho mọi node hiện đại.
5. `castNode` chỉ kiểm tag qua assertion ở build phù hợp, không được mô tả là runtime validation luôn bật.
6. Không gọi heap tuple là mảng Datum trên disk. Descriptor/null bitmap/alignment/variable length tách với arrays đã deform của slot.
7. NULL flag độc lập Datum; by-reference gán chỉ là alias. Không mặc định text kết thúc NUL, detoast always-copy, mọi slot có system attrs, hoặc materialize kéo dài pointer qua reuse.

## Giới hạn bằng chứng

Các expected trong bài suy từ mô hình/contract, không gắn nhãn output engine. Chưa build C, chưa load module, chưa kiểm ABI, chưa thu plan/timing/memory dump. Không đưa code upstream vào artifact học trả phí; chỉ link primary để đối chiếu. Nếu sau này chọn lab source, cần quality gate riêng theo commit/file/license/build/run như hợp đồng của khóa. Workspace backend PostgreSQL 18 và các nút native là đặc tả cho dev; model/code-reading vẫn học hoàn toàn trên web.

## Kiểm đã thực hiện

Script Python read-only đã kiểm cả hai file có ID/title đúng, đủ bảy mục yêu cầu (gồm minh họa), ba ví dụ được đánh số, năm luyện tập đối chiếu năm đáp án, code fences cân bằng và không có ký tự thay thế Unicode. Các phép tính của trace được tính lại: 100.000 × 120 = 12.000.000, 200.000 × 80 = 16.000.000; cây đầu 5 → 7 khi sửa gốc, bản copy vẫn 5; cây chuyển giao −12 → −28, bản copy vẫn −12 theo hợp đồng mô hình. Đây là kiểm nội dung/format và số học, không phải thực thi engine/native.
