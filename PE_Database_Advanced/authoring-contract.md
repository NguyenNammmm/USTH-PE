# Hợp đồng biên soạn phần Advanced nối tiếp85 bài

Đọc context-decisions.md trước. Các mã AD là bài mới; old85 chỉ được dùng làm phần đã học/nhắc lại. Không thay phần Advanced bằng đổi tiêu đề hoặc kéo dài các đoạn nhập môn.

## Độ sâu phải được thể hiện trong nội dung

Mỗi bài có một câu hỏi/vấn đề cụ thể đủ để thấy lý do cần kiến thức. Dữ liệu, ký hiệu và giả định được định nghĩa trước khi dùng. Lời giảng đi từ một ca cụ thể tới cách làm tổng quát, sau đó thử thay một điều kiện để thấy giới hạn. Viết tiếng Việt nối mạch như mẫu NP02; thuật ngữ tiếng Anh ổn định. Không lặp hàng loạt câu mở đầu, nhãn cảm giác hoặc lời quảng bá.

Có ít nhất ba ví dụ/ca có vai trò khác nhau: ca làm rõ cơ chế, ca biên/phản ví dụ, ca thay dữ liệu hoặc yêu cầu. Một trace thuật toán hoặc một lập luận có số liệu đủ là ví dụ; ba đoạn gọiAPI cùng loại chưa đủ. Query có schema+fixture hoặc relation nhỏ định nghĩa đầy đủ, expected chính xác hoặc quan sát cần kiểm. Không bịa output/time/plan hoặc coi một trace chuẩn bị là lượt thực thi mới.

Với thuật toán, phải có input/output và tiền điều kiện, pseudocode, ít nhất một trace, bất biến hoặc tính chất được duy trì, điều kiện dừng, lập luận đúng và chi phí theo giả định. Nếu nguồn có định lý/chứng minh, giải thích các bước chính đủ để người học tái dựng; chỉ nói “đã được chứng minh” hoặc trỏ link không đáp ứng yêu cầu. Nêu rõ phần nào là mô hình đơn giản và phần nào cần kiến thức bổ sung. Không gọi kiểm vài input là chứng minh tổng quát.

Với hệ/DBMS, phân biệt mô hình sách với implementation cụ thể, phiên bản, cấu hình và loại bằng chứng. MySQL không được gọi là ARIES giáo khoa hoặc snapshot isolation chỉ dựa tên REPEATABLE READ; phải mô tả hành vi kiểm. Nội dung PostgreSQL cần dùng nguồnversionriêng khi có khác biệt sách. XML/RDF/graph/object phải có hoạt động và lời giải thật, không chỉ tên API.

## Cấu trúc tối thiểu của file bài

`lessons/ADxx.md`, bắt đầu `# ADxx · Tên bài`. Dòng đầu ghi kiến thức đã học từ old/new IDs, nguồn chương/mục và môi trường web phù hợp. Sau đó lời giảng có tiêu đề khi cần để tìm.

- `## Luyện tập`: ít nhất bốn nhiệm vụ thực chất; chọn các dạng hợp kỹ năng. Có một bài tự làm/tình huống mới không lộ lời giải trước mặt, và một ca phải giải thích/sửa/counterexample. Không cố định MCQ→drag→fill cho mọi bài.
- `## Gợi ý`: ít nhất hai mức, trỏ khái niệm/địa chỉ lỗi trước khi chỉ bước. Không chép đáp án ngay tại đề.
- `## Đáp án và lập luận`: trả lời đủ từng câu, nêu giả định và tiêu chí với câu mở; lời giải code phải khớp input/output/return contract.
- `## Biến thể và cách kiểm`: biến thể hợp tiên quyết, ca biên và misconception-specific feedback; phân biệt testcode với rubric.
- `## Học trên web`: mô tả thao tác người học trong web: editor, hai session, modelcanvas, nộp proof hoặc xem trace. Không yêu cầu learner cài MySQL/Docker/terminal. Backend của dev chịu trách nhiệm chạyengine.
- `## Nguồn và đối chiếu`: sourceprovidedchapter.section và primarydoc URLs thực đã kiểm; repo chỉ gắn sau qualitygate theo exactfile/commit.

Key lessons có thêm `## Minh họa theo trạng thái`,3–6trạng thái đủ dữ liệu cho animation/model, loại bằng chứng, hai hoạt động có hỗ trợ khác dạng và nhiệm vụ chuyển giao. Phần này phải bổ sung cho bài, không thay lời giảng. Bài thường cũng có toàn bộ nội dung ở trên.

Khuyến nghị1.000–1.800từ tiếng Việt mỗi bài, keycó thểdài hơn. Đây không phải quota để nhồi chữ hoặc cắt nội dung; tách thêm bài nếu một file phải gộp quá nhiều cơ chế. Không tạo một outline800từđểđánh dấu chương dài đãđủ.

## Phân công và ranh giới file

Root quản lý manifest, fixtures, README, PDF/HTML và QA. Mỗi agent chỉ ghi các ID được giao và báo source/coverage gap hoặc đề xuất bài con cho root. Giữ nguyên bộ output/database-pe. Sourceclone/rawbook ởtmp; không đónggói toàn văn sách haycácbundlestrangweb. Nếu được phépdùng mộtphầnrepo, giữlicense/noticeđúngphầnvàghi biếnđổi.

Đã có fixture `fixtures/advanced_core.sql` dùngschema `pe_advanced_core` gồm purchases,purchase_lines,payments,accounts,on_call,jobs,metrics,plan_orders. Bảng plan20.000dòng doqa/verify_mysql_labs.py tạo; các hoạt động dùng nó cầnfixturegen tương ứng. Không giả mọi labSQLđãđượckiểm nếu khôngevidencetrongQA.
