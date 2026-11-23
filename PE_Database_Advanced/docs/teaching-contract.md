# Hợp đồng nội dung cho Database Advanced

Ngày05/11/2026. Đây là phần tiếp nối bộ85 bài Database PE đã có. Người học đã gặp SQL, mô hình quan hệ, thiết kế và các chủ đề hệ thống ở bộ trước; phần mới đi sâu vào cách lập luận, thực thi, đo và kiểm giới hạn. Không bắt đầu lại bằng một khóa SELECT cho người chưa biết database.

Nguồn cần giữ đủ là9 lecture,3 practice USTH và Database System Concepts7e:26 chương in, AppendixA, online27–32. Mỗi kiến thức trong phạm vi cần có chỗ giảng và chỗ luyện phù hợp trong hệ85 bài cộng phần Advanced. Không được dùng nhãn chương ở manifest để thay bằng chứng rằng nội dung đã được giải thích. Chỗ bộ trước chỉ giới thiệu khái niệm phải được bổ sung độ sâu; thuật toán và chứng minh có trong nguồn không bị chuyển thành một dòng “đọc thêm”.

Khóa thu phí, giảng tiếng Việt tự nhiên và giải thích thuật ngữ tiếng Anh lần đầu. Mọi hoạt động được giao có đường thực hiện trên web. MySQL làm chính; PostgreSQL hoặc hệ khác được chỉ rõ khi cần. Đầu ra lần này là README, PDF đầy đủ của phần bàn giao, thư mục bài Markdown và HTML đặc tả/demo cho dev; không nhận đã tích hợp production.

## 1. Định nghĩa “đủ để tự học”

Một mục đạt yêu cầu khi người học hiểu bài toán cần giải, đọc được giả định, theo được một lời giải đầy đủ và tự thử một tình huống chưa thấy nguyên đáp án. Độ dài hay số heading không đủ làm bằng chứng. Với một mục đã được bộ85 bài giảng đủ sâu, phần Advanced có thể dẫn đúng bài cũ và nhắc ý cần dùng; không cần viết lại cùng một đoạn chỉ để tăng số bài.

Người biên tập phải kiểm các câu hỏi sau trên nội dung thực:

1. Khái niệm được định nghĩa với đối tượng và phạm vi nào? Ví dụ “đúng” là đúng với một instance, mọi instance hợp lệ, một schedule hay engine đã pin?
2. Vì sao cơ chế cần có? Có phản ví dụ cho cách nghĩ sai hoặc cho việc bỏ một giả định không?
3. Người học có dữ liệu, schema, lịch, log hoặc input đủ để làm lại ví dụ không? Có kết quả/quan sát cần đối chiếu không?
4. Thuật toán có input/output, quy tắc từng bước, điều kiện dừng và trường hợp biên không? Nếu có chứng minh, có các bước suy luận nối được từ giả định đến kết luận không?
5. Bài tập có ít nhất một nhiệm vụ tự làm bằng input/ràng buộc mới, gợi ý theo tầng và đáp án/tiêu chí tương ứng không?
6. Người học có thể hoàn tất phần thao tác qua web với loại bằng chứng được ghi đúng không? Bài cần reviewer có đường nộp và nhận phản hồi không?

Một mục có thể cần nhiều bài; một bài có thể nối nhiều mục nếu chúng cùng phục vụ một việc. Không đặt giới hạn số bài trước rồi nén cả chương optimizer/recovery vào một bài quá ngắn để vừa con số đó.

## 2. Bảng phủ kiến thức là công cụ kiểm, không phải lời hứa thay nội dung

Đơn vị kiểm nhỏ hơn chương: mục sách, thuật toán, định lý/lập luận, chủ đề slide và yêu cầu lab. Registry nguồn ghi source ID, section/page hoặc slide/lab task, mô tả kiến thức, bài85 liên quan, phần Advanced, vị trí lời giảng, ví dụ, hoạt động và mức kiểm.

Mỗi dòng dùng một trong bốn trạng thái:

| Trạng thái | Điều kiện | Cách xử lý |
|---|---|---|
| `covered-in-base` | Bài85 có giải thích, ví dụ và nhiệm vụ đủ cho chính mục đó | Dẫn chính xác bài/mục cũ; không bắt học lại |
| `deepened-in-advanced` | Khái niệm đã giới thiệu nhưng thuật toán/proof/ứng dụng chưa đủ | Ghi phần bổ sung và bài Advanced chứa nó |
| `new-in-advanced` | Chưa có nội dung đủ trong85 bài | Viết lời giảng, ví dụ, bài tập, đáp án đầy đủ |
| `unresolved` | Chưa đọc/kiểm đủ hoặc mapping còn quá rộng | Giữ là việc chưa hoàn thành; không đổi thành covered từ một keyword |

“Có nhắc B+ tree” chưa đủ bao phủ search, insert, split, delete/merge, invariant, cost và biến thể index nếu nguồn giảng các ý đó. “Có nhắc ARIES” chưa đủ bao phủ analysis/redo/undo, dirty-page table, transaction table, LSN và việc crash lại trong recovery. Ví dụ minh họa không phải chứng minh tổng quát; test hữu hạn không phải định lý.

Tài liệu viết lại theo kiến thức, dùng ví dụ PE mới và giữ nguồn để đối chiếu. Không tái bản nguyên văn sách hoặc tự nhận đã cung cấp đáp án chính thức của giáo trình/USTH. Quyền sử dụng tài liệu người dùng cung cấp không tự mở quyền sao chép bài thi hoặc code bên ngoài chưa có license phù hợp.

## 3. Đường vào Advanced và phần nhắc lại

Đường vào theo kỹ năng, không chỉ theo cờ đã click hết85 bài. Chọn một nhiệm vụ nhỏ phù hợp với chặng sắp học: đọc grain và NULL trước query rewrite; closure/lossless trước proof chuẩn hóa; logarit/buffer trước index cost; schedule/transaction trước concurrency; message/quorum trước phân tán.

Một câu MCQ đúng chỉ chứng minh câu đó. Nếu cần tự viết query, sửa lịch hoặc lập luận, phải có nhiệm vụ tương ứng với input mới. Người đã làm được đi tiếp; người mắc mở reminder gắn đúng bài85 đang thiếu rồi quay lại cùng nhiệm vụ. Không đẩy người học về đầu khóa chỉ vì thiếu một khái niệm.

Reminder ngắn gồm: khái niệm đang cần, một ví dụ nhỏ, một lỗi dễ nhầm và link tới bài nền. Nếu cần nhiều định nghĩa mới để giải thích reminder, tách bài cầu nối. Toán và cấu trúc dữ liệu bổ sung chỉ dạy đúng nơi dùng; không giả định đã biết C++ vì đã học SQL.

## 4. Hợp đồng một bài Markdown

Metadata dành cho biên tập/dev; giao diện học chỉ đưa phần giúp người học giải việc đang làm.

```yaml
id: ADV-ID
version: editorial-version
title: Tên cụ thể theo việc cần làm
module: advanced-module
priorLessonRefs: [BASE-ID]
advancedPrerequisites: [ADV-PRIOR-ID]
sourceRefs:
  - sourceId: DSC7e
    section: chapter.section
    knowledgeAtomIds: [source-atom-id]
objectives:
  - Hành vi có thể quan sát, với phạm vi cụ thể
evidenceModes: [computed-model, engine-execution, reviewed-argument]
runtimeProfiles: [activity-specific-capability]
keyLesson: false
adaptationRefs: []
```

Các ID trên minh họa cấu trúc, không phải ID bài đã ban hành. Linter release phải chặn placeholder và link tiên quyết không tồn tại.

Nội dung một bài đi từ tình huống có dữ liệu đến giải thích và tự làm. Không buộc mọi bài có cùng các nhãn mở bài; vẫn phải tìm được các thành phần sau:

- Một context thật sự dẫn tới vấn đề. Ví dụ hai người cùng đặt chỗ, query trả đúng nhưng plan đọc quá nhiều trang, hoặc phân rã schema giữ lossless nhưng làm mất cách kiểm FD tại chỗ.
- Lời giải thích kết nối, định nghĩa trước khi dùng. Một hình hoặc khối code phải được giải thích điều gì thay đổi và tại sao.
- Hai đến ba ví dụ ngắn có mục đích khác nhau: ca bình thường; ca biên/phản ví dụ; thay input hoặc giả định. Với thuật toán/phần chứng minh, thêm ví dụ đủ bước khi cần, không cắt bước vì đã đạt ba khối code.
- Quy tắc, giả định và giới hạn. Chỉ rõ mô hình sách, SQL logic và engine thực có thể khác nhau ở đâu.
- Luyện tập gồm nhiệm vụ có hỗ trợ và ít nhất một nhiệm vụ chuyển giao độc lập. Dạng bài theo kỹ năng, không theo một khuôn cố định.
- Gợi ý theo tầng, đáp án hoặc rubric sau câu hỏi; phân biệt đáp án tham khảo với một cách đúng duy nhất.
- Điều cần giữ lại và bằng chứng cụ thể để người học biết mình có thể làm gì tiếp.

Tác giả không viết “hãy chạy rồi xem” khi không cung cấp schema/input hoặc không nói cần quan sát gì. Không để người học tự đoán ý nghĩa cột, đơn vị, thứ tự, ties, cách xử lý NULL hay điều kiện đúng của thuật toán.

## 5. Hợp đồng thuật toán

Thuật toán phải có tên và bài toán, input hợp lệ, output mong muốn, cấu trúc trạng thái, từng bước cập nhật và điều kiện dừng. Pseudocode có quy ước đủ rõ để làm bằng tay hoặc tính trong model web; không cần ép mọi thuật toán thành SQL.

Mỗi thuật toán có ít nhất một trace nhỏ đủ bước. Trace ghi trạng thái trước/sau và lý do áp quy tắc. Các bước lặp giống nhau có thể gom khi đã nói rõ quy tắc; không bỏ điểm làm thay đổi nhánh. Người học phải có một input mới để tự trace hoặc hoàn thiện thuật toán, rồi một ca biên làm lộ lỗi thường gặp.

Nếu nguồn phân tích độ phức tạp, bài nêu đơn vị và giả định: số tuple, page/block, buffer page, fanout, round message hoặc thời gian. Đếm I/O theo mô hình không được đổi nhãn thành thời gian chạy MySQL. Best/worst/average hoặc expected chỉ dùng khi thực sự đã xác định phân bố/giả định tương ứng.

Phần đúng đắn cần giải thích invariant hoặc lập luận mà nguồn dùng. Tách termination, soundness và completeness/optimality khi chúng là các yêu cầu khác nhau. Một vòng lặp dừng chưa chứng minh cho đáp án đúng; một cách sinh lời giải đúng chưa chứng minh đã tìm hết hoặc tìm tối ưu.

Checklist biên tập cho những nhóm thường bị rút gọn quá mức:

| Nhóm | Nội dung cần kiểm khi có trong nguồn | Hoạt động phù hợp trên web |
|---|---|---|
| FD và thiết kế | Closure, minimality, cover, lossless/preservation; giả định của thuật toán synthesis/decomposition | Tự suy diễn, tìm counterexample, bước chase, proof có rubric |
| Index và lưu trữ | Invariant nút/page, search/update/split/merge, fanout/cost và trường hợp trùng | Step-through, sửa một bước sai, tạo cây mới, đối chiếu engine riêng |
| Query processing | External sort, join, buffer/memory conditions, pipeline/materialization | Gán buffer, tính số pass/I/O, trace tuple, thực nghiệm có provenance |
| Optimization | Tương đương biểu thức, estimate, search/pruning, physical properties | Tìm rewrite sai, phản ví dụ NULL/bag, chọn plan và bảo vệ giả định |
| Concurrency | Conflict/view/model assumptions, protocol, serialization/locking/MVCC | Graph, trace/đổi lịch, lab hai session thật, giải thích outcome |
| Recovery | Durable prefix, WAL, checkpoint, redo/undo và restartability | Chọn record, sửa log/page, model crash, engine experiment riêng |
| Phân tán | Partition/skew, replication, commit/consensus, fault model/quorum | Message trace, phản ví dụ, mô hình topology và lab backend khi cần |
| Calculus và dữ liệu khác | Safety/domain independence, biểu diễn và thao tác đúng ngữ nghĩa | Chuyển biểu thức, tìm query không an toàn, ví dụ trên hệ được chỉ rõ |

Bảng là yêu cầu rà soát, không thay danh sách mục nguồn. Nếu source audit phát hiện một thuật toán hoặc lập luận ngoài bảng, vẫn phải đưa nó vào dòng phủ tương ứng.

## 6. Hợp đồng chứng minh và phản ví dụ

Mỗi lập luận có phát biểu điều cần chứng minh, giả định, ký hiệu, đối tượng lượng hóa và kết luận. Giải thích từ ngữ như “mọi”, “tồn tại”, “nếu” và “chỉ nếu” đúng nơi cần; không biến chúng thành khẩu hiệu học thuộc.

Cấu trúc tối thiểu cho một proof độc lập:

1. Nêu bài toán hoặc mệnh đề bằng ký hiệu và lời thường.
2. Ghi giả định và phần không được giả định. Ví dụ một FD là ràng buộc trên mọi instance hợp lệ, không suy ra chỉ vì sample hiện tại chưa vi phạm.
3. Đi từng bước với lý do: định nghĩa, luật suy diễn, invariant, quy nạp, phản chứng hoặc construction đã được giới thiệu.
4. Nếu là mệnh đề hai chiều, chứng minh cả hai chiều. Nếu chỉ là sufficient condition, không gọi nó là equivalence.
5. Đặt một ca nhỏ hoặc hình để kiểm trực giác; nói rõ vai trò minh họa, không thay proof.
6. Cho phản ví dụ khi bỏ giả định quan trọng và một bài tự làm đổi schema/schedule/tham số.

Rubric proof kiểm: hiểu đúng phát biểu; giả định đầy đủ; bước suy luận hợp lệ; phủ mọi trường hợp cần thiết; kết luận đúng phạm vi. Phản hồi chỉ chỗ thiếu hoặc bước không theo được. Không chấm từ việc người học có lặp đúng tên định lý hoặc dùng giống văn mẫu.

Model checker hữu hạn có thể bác mệnh đề bằng counterexample trong miền nó tìm. Không tìm thấy phản ví dụ trong giới hạn không tự thành proof tổng quát. Giao diện nêu domain/bound đã duyệt và trả `no-counterexample-within-bound` khi đúng nghĩa; không ghi “đã chứng minh” cho kết quả ấy.

## 7. Luân phiên hoạt động theo kỹ năng

Không giao mọi bài cùng chuỗi MCQ → kéo thả → điền → code. Chọn thao tác giúp nhìn ra cấu trúc đang học, rồi giảm hỗ trợ. Một bài có thể bắt đầu bằng đọc plan, một bài bằng lịch gây lỗi, một bài bằng một proof thiếu giả định.

| Kỹ năng | Bước hỗ trợ có thể dùng | Bằng chứng độc lập cần có |
|---|---|---|
| Đọc và sửa query | Dự đoán tuple, chọn vùng sai, ghép biểu thức | Query trên fixture mới và giải thích ca từng sai |
| Thiết kế dữ liệu | Phân loại ràng buộc, anomaly, cặp tuple phản ví dụ | Schema/FD/mapping mới với giả định và kiểm hành vi |
| Thuật toán | Hoàn thiện bước, trace trạng thái, sửa invariant bị phá | Tự chạy trên input mới và giải thích đúng đắn/chi phí |
| Proof | Ghép một lý do, tìm bước không hợp lệ | Lập luận hoặc phản ví dụ mới, được chấm rubric |
| Performance | So plan có provenance, chỉ estimate lệch, chọn phép đo | Query/index đúng và báo cáo phép đo/giới hạn |
| Transaction | Dự đoán read view, sắp event phụ thuộc | Lịch engine thật hoặc mô hình theo mục tiêu, kèm invariant |
| Phân tán | Theo message, chọn quorum, phát hiện assumption thiếu | Kịch bản lỗi mới và kết luận đúng fault model |

Một dạng khác giao diện chưa phải khác kỹ năng. Đổi tên bảng và số ngưỡng chưa đủ tạo chuyển giao nếu người học vẫn chỉ nhớ vị trí đáp án. Ngược lại, không cần thay dạng chỉ để tạo cảm giác mới khi một cách thực hành đang phù hợp.

Seed chọn trong các biến thể đã được biên soạn và kiểm. Nó có thể đổi dữ liệu, phân bố, topology, schedule hợp lệ hoặc yêu cầu nghiệp vụ tương đương, giữ prerequisite và độ khó đã khai báo. Reload giữ seed; chọn đề mới tạo attempt mới. Đáp án tính từ cùng fixture/version và được kiểm độc lập ca nhỏ. Không sinh ngẫu nhiên một proof rồi coi model output là oracle tổng quát.

## 8. Gợi ý, đáp án và nhiệm vụ chuyển giao

Gợi ý1 nhắc lại thông tin đang cần xét: grain, loại read, FD, durable prefix hoặc điều kiện buffer. Gợi ý2 chỉ vùng thao tác hay quy tắc có thể dùng, chưa chép toàn bộ lời giải. Với bài proof/thiết kế, gợi ý có thể hỏi một giả định đang thiếu thay vì đề nghị một câu SQL.

Mở đáp án là lượt học có hỗ trợ và được giữ trong attempt. Sau đó dùng tình huống khác để lấy bằng chứng độc lập. Không cho bấm lại đúng seed đã mở lời giải rồi coi là tự làm chỉ vì lần bấm sau không mở hint.

Đáp án phải giải chính đề đã hỏi, không chỉ nêu tên API hoặc một con số. Với query, có output contract và ca kiểm; với thuật toán, có trace và giải thích; với proof, có lập luận hoặc tiêu chí chấp nhận; với hệ thống, có assumptions và outcome có thể khác. Bài thiết kế có nhiều lời giải đúng cần chỉ ra điều kiện chấp nhận, không ép cùng hình với mẫu.

Nhiệm vụ chuyển giao giữ kỹ năng cần kiểm nhưng thay yếu tố đủ làm lộ việc học thuộc: nhiều nhóm/NULL/ties khác, schema/FD khác, buffer khác, lịch khác, phân bố skew khác hoặc fault point mới. Hidden case không được tự thêm một quy tắc nghiệp vụ mà đề chưa công bố.

## 9. Bài trọng tâm và minh họa

Bài trọng tâm được chọn vì có bước chuyển khó hoặc sai lầm có hệ quả, không vì nó nằm ở đầu mỗi chương. Ngoài nội dung chung, bài có lời giải từng bước đủ rõ, hình/trạng thái và ít nhất hai hoạt động hỗ trợ khác dạng trước nhiệm vụ độc lập. Các bài còn lại vẫn phải tự học được.

Minh họa thuật toán giữ một trạng thái hiện tại và cho bước trước/tiếp khi phù hợp. Chỉ highlight dữ liệu thực sự đang dùng. Sau khi sửa input, tính lại hoặc báo trace chuẩn bị sẵn không còn áp dụng; không giữ hình cũ rồi giả đồng bộ với code mới.

Minh họa phải nêu model hay trace đo thật. Model B+ tree có capacity do bài chọn không được gọi là cấu trúc page hiện tại của InnoDB. Thứ tự logic SELECT không được gọi là thứ tự vật lý optimizer. Lịch graph không được nhận là mọi interleaving engine đều như vậy. Mỗi minh họa có nhãn, nội dung thay cho màu và đường dùng bằng bàn phím.

Motion phục vụ giải thích thay đổi trạng thái; không dùng video loop làm điều kiện duy nhất để đọc dữ liệu. Có thể dừng, xem từng bước và đọc trạng thái dưới dạng text. Reduced-motion không làm mất nội dung. Nếu dùng video cho một ví dụ cố định, nhãn nói rõ đó là ví dụ biên soạn trước.

## 10. Tích hợp repo qua cổng chất lượng

Repo chỉ được tích hợp sau khi xác minh quyền sử dụng phù hợp khóa thu phí, phạm vi license của code/data, commit, khả năng chạy lại, tính đúng của đề/oracle và sự phù hợp học thuật. Một repo có README hay nhiều stars chưa đủ. Kết quả gate phải nêu rõ đã kiểm phần nào, trên hệ nào và giới hạn nào còn lại.

Bài được biên tập thành trải nghiệm web với prompt/dữ liệu/gợi ý/test phù hợp khóa. Không yêu cầu học viên tự clone hoặc chạy Docker. Nếu upstream có toolchain phức tạp, dev cấp workspace/backend tương ứng hoặc chỉ chọn phần đã chuyển đổi và kiểm được; không gọi bản model chuyển đổi là đã chạy nguyên engine upstream.

Mỗi adaptation giữ source URL, commit SHA, path/line hoặc asset gốc, license/notice, tác giả và thay đổi. Phần tự biên soạn có ownership riêng, nhưng không xóa attribution của code/data được giữ. Repo bị loại hoặc có điều kiện vẫn có lý do trong báo cáo; không lén đưa vào exercise bank ở cuối quá trình.

Quyết định pedagogical và quyết định license là hai gate riêng. Repo kỹ thuật tốt nhưng chưa đủ quyền không tích hợp; repo có quyền rõ nhưng oracle sai cũng không tích hợp. Kết quả gate không phải nhận định pháp lý tổng quát về mọi cách dùng tương lai; release phải giữ đúng phạm vi file và cách dùng đã kiểm.

## 11. Bốn đầu ra và tiêu chí hoàn tất

| Đầu ra | Phải có | Bằng chứng kiểm |
|---|---|---|
| README | Phần Advanced nối85 ở đâu; nguồn; mục tiêu; cách dùng; repo được chọn/loại; môi trường và giới hạn | Link tồn tại, phạm vi khớp manifest và bằng chứng thực tế |
| PDF đầy đủ | Lời giảng/ví dụ/bài tập/gợi ý/đáp án của phần bàn giao; bài trọng tâm; mapping và phụ lục cần dùng | Text coverage, mục lục/bookmark, render kiểm bố cục và ký hiệu |
| Thư mục Markdown | Một bài một file, metadata/source/prerequisite, nội dung tự học và luyện đủ | Linter/schema, nội dung kiểm bằng người/agent độc lập, source atom audit |
| HTML đặc tả | Lộ trình nhắc prerequisite, xem bài, demo tính lại, kiểu hoạt động và runner contract cho dev | Logic test và browser khi khả dụng; nhãn mô hình/engine đúng |

Phần bàn giao phải nói rõ tài liệu nào là tham chiếu bộ85 và tài liệu nào đã được kèm. Link tới một path trên máy tác giả không được giả là người nhận có file. Nếu gói mới không chứa bộ85, README ghi điều kiện cần có và dùng đường dẫn/URL ổn định do dev quyết định; không suy bản PDF Advanced tự thân đã tái bản toàn khóa nền.

Độ phủ cần kiểm từng yêu cầu nguồn. Mỗi thuật toán/proof được yêu cầu có vị trí nội dung, ví dụ và hoạt động; không được đánh dấu đủ chỉ từ một kiểm keyword. Câu hỏi và đáp án khớp nhau, fixture và mọi file được nhắc có đích thực. Nguồn/phần tích hợp có hash/version. Không còn placeholder hoặc phần “đang biên soạn” trong bản hoàn tất.

## 12. Quy trình QA nội dung và kỹ thuật

1. Đọc source atom và bài85 liên quan trước khi viết phần Advanced; phân biệt giới thiệu với giải thích đủ sâu.
2. Kiểm tay ví dụ nhỏ. Chạy SQL trên đúng engine khi kết luận là engine execution; mô hình có test riêng cho giả định/miền input.
3. Đọc độc lập đáp án và thử một lời giải đúng khác cách viết, một lỗi điển hình và một ca biên. Ghi giới hạn kiểm thay vì suy mọi snippet đã chạy.
4. Với proof, reviewer kiểm logic/các chiều/giả định; với thuật toán kiểm termination/invariant và trace. Compile hay output khớp không thay các bước ấy.
5. Kiểm release: source mapping, ID/prerequisite, link, ký hiệu, ảnh, đáp án, phiên bản PDF/HTML và attribution.
6. Pilot bằng nhiệm vụ mới sau thời gian học, sửa wording/hint từ chỗ người học kẹt. Thời lượng, quota và ngưỡng đánh giá ban đầu là đề xuất, chưa phải thang đo mastery đã kiểm định.

Software pass không chứng minh hiệu quả dạy học. Số màn xem, số click, streak hoặc điểm hài lòng không thay bằng chứng tự giải một trường hợp mới. Pilot cần tách lỗi kiến thức, lỗi hiểu đề, lỗi thao tác và lỗi môi trường để sửa đúng phần.

## 13. Cách viết

Dùng câu trực tiếp, nối từ dữ liệu vừa thấy sang quy tắc đang giải thích. Giữ thuật ngữ khi cần phân biệt chính xác, nhưng giải nghĩa bằng đối tượng cụ thể. Tránh các nhãn như “bàn thí nghiệm”, “vết có trần” hoặc câu bóng bẩy không giúp làm bài. Không nhồi kết luận đạo lý sau mỗi ví dụ.

Ví dụ giọng văn phù hợp: “Hai giao dịch cùng đọc số chỗ còn lại là1. Nếu cả hai đều ghi lại0 mà không kiểm điều kiện chung, hệ thống có thể nhận hai lượt đặt chỗ. Trước khi sửa query, hãy chỉ ra thao tác nào cần được xem như một quyết định chung.” Sau đó đưa dữ liệu, lịch, query và giả định cần thiết; không kết thúc ở phép ví von.

Phần dev có thể dùng tên trường và state machine để triển khai chính xác. Phần learner chỉ hiển thị điều giúp người học hiểu, thao tác hoặc đánh giá kết quả. Hai lớp văn bản không trộn khiến bài giảng trở thành tài liệu kiến trúc API.
