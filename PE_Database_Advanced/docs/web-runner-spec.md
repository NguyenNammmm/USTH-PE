# Đặc tả runner web cho Database Advanced

Ngày 05/11/2026. Đây là hợp đồng triển khai cho dev, chưa phải một dịch vụ đã được triển khai hoặc nghiệm thu. Phần Advanced tiếp nối bộ 85 bài Database PE. Học viên của khóa thu phí làm bài qua web; không cần tự cài database, Docker, compiler hoặc mở terminal trên máy mình. Dev có thể dùng container hoặc máy ảo ở backend để cung cấp môi trường đó.

MySQL 8.4/InnoDB là hệ chính. PostgreSQL hoặc hệ khác được mở theo mục tiêu bài và có capability riêng. Tên “SQL” trên editor không được che việc đổi hệ. Những khái niệm dùng mô hình hữu hạn vẫn có thể tính và tương tác hoàn toàn trên web; kết quả đó được ghi là kết quả mô hình. Bài yêu cầu hành vi engine phải có runner engine thật.

## 1. Bốn loại bằng chứng cần giữ riêng

| Loại | Cách tạo kết quả | Có thể kết luận gì | Không được kết luận gì |
|---|---|---|---|
| `prepared-example` | Ví dụ/trace do tác giả chuẩn bị, khóa version | Diễn biến của chính ví dụ đó | Query đã sửa vừa được chạy |
| `computed-model` | Thuật toán tính lại từ input trong phạm vi mô hình | Kết quả đúng theo giả định và miền input của mô hình | InnoDB/PostgreSQL đã thực thi cùng lịch hoặc cùng cấu trúc |
| `engine-execution` | Backend thực thi trên engine đã pin | Kết quả và quan sát của lượt engine có provenance | Đúng với mọi database, mọi lịch hoặc mọi phiên bản |
| `reviewed-argument` | Người học nộp lập luận/schema/thiết kế, reviewer chấm rubric | Những tiêu chí reviewer đã kiểm và phản hồi | Một model checker hữu hạn đã chứng minh định lý tổng quát |

Demo HTML trong bộ bàn giao có thể thực hiện hai loại đầu. Khi chưa nối backend, nút phải là “Tính mô hình” hoặc “Xem diễn biến”; không dùng nút “Chạy MySQL” trả kết quả cố định. Một lesson có thể phối hợp các loại bằng chứng, nhưng mỗi activity và mỗi result phải ghi loại của chính nó.

## 2. Kiến trúc triển khai đề xuất

Luồng chính: trình duyệt → API xác thực lượt làm → hàng đợi → bộ cấp môi trường → worker engine/model → checker → kho kết quả. API trả job handle sớm; client nhận sự kiện hoặc poll có backoff và có thể tải lại đúng job. Mất kết nối trình duyệt không đồng nghĩa SQL đã dừng.

Control plane quản lý sandbox, version và việc hủy. Data plane chạy code của activity. Học viên không nhận credential quản trị hoặc địa chỉ truy cập trực tiếp tới database. Worker không được dùng connection quản trị để chạy SQL người học. Checker và reference query chạy trong trạng thái riêng, không để lời giải sửa cùng một database rồi vô tình giúp bài làm đúng.

Các môi trường sau cần mức cô lập khác nhau:

| Capability | Môi trường tối thiểu đề xuất | Lý do |
|---|---|---|
| Đọc bảng và tự viết query | Schema/credential riêng, quyền đọc, worker có quota | Tách dữ liệu, output và thời gian |
| DDL, DML, routine, trigger | Database thử riêng, reset từ fixture, quyền theo bài | DDL không được coi là có thể rollback như mọi DML |
| Hai session và khóa | Hai connection ổn định trong cùng sandbox, observer riêng | Connection pool không được tráo session giữa các bước |
| Đo plan/benchmark | Sandbox tài nguyên riêng trong lượt đo | Tránh workload người khác làm sai phép so sánh |
| Restart/crash/recovery | Instance/data directory thử riêng, snapshot dùng một lần | Dừng engine này không ảnh hưởng lượt khác |
| Replication/XA/phân tán | Cụm riêng theo template, network được điều khiển | Lỗi nút/kết nối phải nằm trong lab của chính lượt |
| Thuật toán hoặc chứng minh | Model hữu hạn hoặc trình nộp rubric | Không cần cấp engine khi mục tiêu là lập luận |

Một schema riêng trên server dùng chung giúp tách tên/dữ liệu, nhưng không tự cô lập CPU, buffer pool, disk hoặc thao tác dừng server. Dev không được dùng mức cô lập đó để quảng bá bài đo hiệu năng hoặc crash như thí nghiệm độc lập.

## 3. Registry capability và version

Mỗi build công bố registry do server sinh từ probe đã chạy. Registry ghi image/runtime digest thực tế; nhãn `mysql-8.4` chưa đủ làm version tái lập. Bản MySQL 8.4.13 đã dùng ở bộ 85 bài là bằng chứng cũ, không chứng nhận mọi worker Advanced tương lai.

```json
{
  "capabilityId": "mysql84.two-session.innodb.v1",
  "engine": "mysql",
  "engineVersion": "8.4.x-exact-patch-from-probe",
  "imageDigest": "sha256:recorded-by-release-pipeline",
  "storageEngine": "InnoDB",
  "charset": "utf8mb4",
  "collation": "declared-and-tested",
  "timeZone": "+00:00",
  "sqlMode": ["ONLY_FULL_GROUP_BY", "STRICT_TRANS_TABLES"],
  "sessions": 2,
  "observer": true,
  "features": ["transactions", "locking-read", "wait-observation"],
  "probeVersion": "mysql84-capability-probes-v1",
  "probeResultId": "release-owned-result",
  "availability": "ready"
}
```

Các giá trị version/digest/collation ở ví dụ là vị trí cần điền trong pipeline, không phải artifact image đã được cung cấp. Release không hợp lệ nếu còn các chuỗi mô tả này. Activity lưu capability yêu cầu và các giả định hẹp hơn: isolation, autocommit, schema/index, lock timeout, số session. Khi thiếu capability, giao diện báo “Môi trường bài này chưa sẵn sàng”, giữ draft và cho xem phần lý thuyết. Không đổi engine âm thầm hoặc chuyển lỗi hạ tầng thành người học làm sai.

MySQL và PostgreSQL dùng manifest khác nhau. Không suy hành vi snapshot/locking từ việc hai hệ có cùng tên mức isolation. PostgreSQL 18 được dùng làm baseline tài liệu đối chiếu; dev phải pin patch thực tế trước nghiệm thu. [MySQL 8.4 isolation](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) và [PostgreSQL 18 isolation](https://www.postgresql.org/docs/18/transaction-iso.html) là nguồn kiểm ngữ nghĩa, không phải nhãn engine thay thế cho nhau.

## 4. Dữ liệu activity, attempt và kết quả

Activity biên soạn trước, không để client tự gửi expected hoặc tự chọn quyền. Các trường dưới là hợp đồng đề xuất; dev có thể dùng stack hiện có miễn giữ ngữ nghĩa.

```typescript
type EvidenceMode =
  | "prepared-example" | "computed-model"
  | "engine-execution" | "reviewed-argument";

type Activity = {
  id: string;
  version: string;
  skillIds: string[];
  prerequisites: string[];
  evidenceMode: EvidenceMode;
  capabilityId?: string;
  fixtureId: string;
  fixtureVersion: string;
  generatorVersion?: string;
  responseMode: "query" | "schedule" | "model" | "argument" | "artifact";
  supportLevel: "worked" | "completion" | "independent";
  contractId: string;
  checkerVersion: string;
  referenceVersion: string;
  sourceRefs: string[];
  adaptationRefs: string[];
};

type Attempt = {
  id: string;
  ownerId: string;
  activityId: string;
  activityVersion: string;
  seed: string;
  fixtureHash: string;
  draftRevision: number;
  draftHash: string;
  hintsOpened: string[];
  solutionRevealedAt?: string;
  createdAt: string;
};

type JobOutcome =
  | "cases-passed" | "semantic-mismatch" | "syntax-error"
  | "expected-engine-error" | "unexpected-engine-error"
  | "resource-limit" | "cancelled" | "infrastructure-error"
  | "needs-review";
```

`cases-passed` có nghĩa đạt những ca trong contract; không tự đổi thành “mastered”. `expected-engine-error` có thể là bằng chứng đúng của lab deadlock. Reviewer hoặc checker activity quyết định tiêu chí; một mã lỗi xuất hiện tình cờ không tự đủ điểm. Support được server ghi theo attempt/seed/version, và chỉ tăng trong lượt đó. Đổi tab hay tải lại trang không xóa việc đã mở đáp án.

Result bất biến sau khi hoàn tất và gắn đúng draft hash. Sửa query sau pass làm UI bỏ nhãn kết quả áp dụng cho bản nháp hiện tại; vẫn giữ kết quả cũ trong lịch sử. Submit bản mới tạo revision/job mới. Không ghi đè lịch sử bằng đáp án reference chạy sau đó.

Kết quả dạng bảng phải giữ kiểu và NULL:

```json
{
  "jobId": "job-public-handle",
  "attemptId": "attempt-owned-by-current-learner",
  "draftRevision": 3,
  "draftHash": "sha256-of-submitted-source",
  "outcome": "cases-passed",
  "evidenceMode": "engine-execution",
  "runtimeManifestHash": "sha256-of-pinned-runtime-manifest",
  "fixtureHash": "sha256-of-executed-fixture",
  "columns": [
    {"name": "customer_id", "type": "INTEGER", "nullable": false},
    {"name": "paid_total", "type": "DECIMAL(12,2)", "nullable": true}
  ],
  "rows": [[1, {"decimal": "198.00"}], [2, null]],
  "rowCount": 2,
  "truncated": false,
  "supportUsed": ["hint-1"],
  "solutionRevealed": false,
  "cleanupState": "verified",
  "caseSummary": {"passed": 4, "total": 4}
}
```

DECIMAL truyền theo biểu diễn thập phân chính xác; không ép sang floating point JavaScript để so tiền. Output bị cắt phải có `truncated=true`, tổng số dòng nếu biết và cách xem thêm trong quota. Không chấm query đúng bằng cách chỉ so 100 dòng đầu đã cắt. Hidden fixture không được lộ toàn bộ nhưng phản hồi cần có phản ví dụ đủ hiểu lỗi theo chính sách activity.

## 5. API và vòng đời job

| Thao tác | Endpoint đề xuất | Hợp đồng |
|---|---|---|
| Mở bài | `GET /activities/{id}?version=...` | Trả prompt/schema/public fixture/capability; không trả secret hoặc oracle kín |
| Tạo lượt | `POST /attempts` | Server chọn/kiểm activity version, seed và chủ sở hữu |
| Lưu draft | `PUT /attempts/{id}/draft` | Có revision hoặc ETag để phát hiện ghi đè; lưu không tự chạy |
| Chạy | `POST /attempts/{id}/jobs` | Nhận draft revision/hash, mode; idempotency key ngăn click đúp tạo hai lượt ngoài ý muốn |
| Theo dõi | `GET /jobs/{id}` hoặc event stream | Có sequence number; đọc lại được sau reconnect |
| Hủy | `POST /jobs/{id}/cancel` | Yêu cầu hủy; chưa tự khẳng định worker đã ngừng |
| Gợi ý/đáp án | `POST /attempts/{id}/support-events` | Server ghi reveal trước khi trả nội dung |
| Đề mới | `POST /attempts/{id}/variants` | Tạo attempt mới; giữ lịch sử seed cũ và mức hỗ trợ của seed đó |
| Nộp lập luận | `POST /attempts/{id}/review-submissions` | Khóa revision, gắn rubric version và artifact hash |

Đọc/hủy job kiểm ownership tại server, không chỉ dựa vào URL khó đoán. Event stream chỉ cung cấp event của sandbox được phép. Không lộ schema học viên khác qua raw observer hoặc thông báo lỗi backend.

Execution state: `queued → provisioning → preparing → running → cleaning → finished`. Hủy từ bước đang chạy đi qua `cancelling → cleaning`; cleanup chưa xong thì chưa được đưa sandbox về pool. Nếu không xác minh được cleanup, chuyển `quarantined`, ghi infrastructure error và cấp sandbox mới khi retry. Outcome và execution state là hai trường riêng: đã biết query sai không có nghĩa có thể bỏ cleanup.

Retry mạng dùng cùng idempotency key để nhận cùng job, không chạy SQL lại một cách mù. Retry thao tác nghiệp vụ do serialization/deadlock là attempt con có quan hệ với lần trước và phải chạy lại transaction phù hợp; client không được tự nhân các lệnh chuyển tiền vì HTTP timeout.

## 6. Thực thi SQL, quyền và reset

Trước khi chạy, worker nạp fixture khóa version vào sandbox và xác minh schema/data hash hoặc các invariant chuẩn. Runner gắn database đích từ lease; không chấp nhận tên database hệ thống do client tự chọn. Bài SELECT chỉ có quyền đọc các object trong bài. Bài DDL/DML được cấp quyền trong database thử của chính lượt. Routine/trigger dùng profile riêng, với quyền và security context đã kiểm; không mở rộng quyền toàn server cho học viên chỉ để một demo chạy được.

Parser cần hiểu statement và dialect. `DELIMITER`, `SOURCE`, `\G` là lệnh/cách hiển thị phía client MySQL, không gửi nguyên xi qua API driver. Editor có thể hỗ trợ snippet delimiter bằng parser đã kiểm, hoặc tác giả định nghĩa một routine như một statement đầy đủ. Chuỗi bắt đầu bằng `SELECT` hoặc `WITH` không phải hàng rào quyền; engine role, sandbox và giới hạn tài nguyên mới là lớp thực thi.

Các bài chưa yêu cầu file/network không nhận quyền đọc file server, nạp plugin/UDF hoặc xuất dữ liệu ra filesystem ngoài sandbox. Worker không có network tùy ý tới dịch vụ thật. Các request tải dataset dùng asset đã duyệt và hash ở control plane; không cho SQL người học biến backend thành trình tải URL.

Reset sau lab dùng rebuild từ fixture/snapshot, không chỉ chạy `ROLLBACK`. MySQL có nhóm DDL implicit commit; một số thao tác temporary không commit nhưng cũng không rollback được. Atomic DDL không đồng nghĩa người dùng có thể rollback một chuỗi DDL tùy ý. Dev phải kiểm riêng ca tạo bảng, ALTER, TRUNCATE, routine và trigger đã được cấp trong profile. [MySQL implicit commit](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html), [atomic DDL](https://dev.mysql.com/doc/refman/8.4/en/atomic-ddl.html).

Hủy query dùng connection quản lý thuộc lease, sau đó rollback/đóng tất cả session liên quan và xác minh trạng thái. `KILL QUERY` dừng statement nhưng để connection tồn tại; nó không tự reset mọi transaction, session variable hoặc temporary object. Không trả connection vừa bị hủy về pool cho người khác. [MySQL KILL](https://dev.mysql.com/doc/refman/8.4/en/kill.html).

## 7. Lab hai session: orchestration bằng bằng chứng

Giao diện có Session A, Session B, schema/data hiện dùng và timeline sự kiện. Người học có thể dự đoán, bấm bước được phép hoặc sửa một cell SQL. Backend giữ hai connection cố định đến hết lượt. Bước được gửi bất đồng bộ; query đang đợi không chặn event loop của API.

Không dùng `sleep(1)` để suy ra “A chắc đã lấy khóa”. Scheduler chỉ cho bước phụ thuộc chạy sau event xác minh: statement hoàn tất, lock/wait cần thiết được observer thấy hoặc assertion trạng thái đạt. Time limit là deadline lỗi, không phải cách chứng minh thứ tự. Observer cần lọc theo connection/object thuộc lease; một truy vấn Performance Schema toàn server không được đưa thẳng tới browser. Các bảng `data_locks` và `data_lock_waits` có thể cung cấp bằng chứng theo cấu hình đã probe. [Ví dụ deadlock chính thức MySQL](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlock-example.html).

Template lịch là DAG có dependency, không chỉ danh sách thời gian. Ví dụ `A2` có thể được dispatch rồi ở trạng thái running-waiting; phải có observer/barrier chứng nhận để tiếp tục `B2`. Không gọi `await A2` trước `B2` khi A2 đang chờ B2 giải phóng khóa. Không biến mọi câu SELECT thành observer vì việc đọc hoặc locking read có thể thay đổi chính lịch đang thử.

Ví dụ lab deadlock được biên soạn mới:

```sql
CREATE TABLE accounts (
  id INT PRIMARY KEY,
  balance INT NOT NULL
) ENGINE=InnoDB;
INSERT INTO accounts VALUES (1,100),(2,100);
```

| Bước | Session | Hành động | Điều kiện trước / event cần giữ |
|---|---|---|---|
| A0 | A | Bắt đầu transaction; trừ 10 ở id1 | A0 hoàn tất, A còn transaction mở |
| B0 | B | Bắt đầu transaction; trừ 20 ở id2 | B0 hoàn tất, B còn transaction mở |
| A1 | A | Cộng 10 ở id2 | Dispatch bất đồng bộ; observer thấy A đợi B |
| B1 | B | Cộng 20 ở id1 | Chỉ dispatch sau wait A→B đã được xác minh |
| D | Engine | Giải quyết deadlock | Ghi SQLSTATE/mã lỗi, transaction bị abort, statement nào đã xong |
| C | Session còn lại | Commit sau khi các statement của nó xong | Không commit session chưa xử lý đúng lỗi |
| V | Observer | Đọc trạng thái bằng connection xác minh mới | Tổng balance phải là200; trạng thái đúng với transaction đã commit |

Không chấm cứng A hoặc B phải là victim. Nếu A chuyển 10 thành công còn B abort, kết quả là90/110. Nếu B chuyển20 thành công còn A abort, kết quả là120/80. Sau khi retry toàn bộ transaction bị abort trong điều kiện không còn xung đột, kết quả hai chuyển tiền là110/90. Bài yêu cầu người học giải thích vì sao không chỉ retry câu UPDATE cuối.

Với InnoDB, deadlock làm rollback toàn transaction. Lock wait timeout thường chỉ rollback statement theo cấu hình mặc định; worker ghi cấu hình thực tế, không dùng chung một handler giả định cho mọi lỗi. Để lượt kế tiếp sạch, runner chủ động kết thúc transaction còn mở và rebuild fixture. [InnoDB error handling](https://dev.mysql.com/doc/refman/8.4/en/innodb-error-handling.html). Cách chọn victim và thời gian chờ không được dùng làm barem cố định. [Xử lý deadlock](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlocks-handling.html).

Timeline lưu event monotonic của scheduler và engine observation riêng. “Đã gửi câu lệnh” khác “câu lệnh đã chạy”, “đã bị chặn” và “đã commit”. Với kết quả nondeterministic, contract chấp nhận tập outcome hợp lệ kèm invariant và event bắt buộc; không so stdout duy nhất.

## 8. EXPLAIN, optimizer và đo hiệu năng

Ba nhãn phải tách rõ: chi phí tính trong mô hình sách, plan do optimizer dự kiến và dữ liệu thực thi đo được. Một animation B+ tree không phải trace page thực của InnoDB; một số `cost` không phải mili giây đo thực tế.

Trong MySQL8.4, `EXPLAIN ANALYZE` thực thi statement và trả thông tin iterator trong TREE; JSON không phải format được hỗ trợ cho lệnh này. Đường JSON của `EXPLAIN` thường không được dùng như parser thay thế cho mọi output ANALYZE. Adapter giữ raw TREE kèm engine version và chỉ trích các trường đã có test parser. [MySQL EXPLAIN](https://dev.mysql.com/doc/refman/8.4/en/explain.html).

Một run plan cần ghi: query hash; schema/index definitions; row counts và distribution; generator/seed; statistics freshness; engine/runtime/config; loại run cold/warm theo định nghĩa; số lượt; timeout; raw plan và metric có đơn vị. Không gán “cold” chỉ vì tab browser vừa mở. Không ép flush cache toàn server dùng chung để tạo cold run.

Đề độc lập có thể yêu cầu chọn index rồi bảo vệ quyết định bằng plan và result invariant. Checker kiểm query vẫn đúng trước; sau đó kiểm tiêu chí plan/cost đã công bố hoặc rubric. Không dùng “phải nhanh hơn2ms” trên hạ tầng dùng chung làm chuẩn qua bài. Nếu một bài cần ngưỡng, pin workload, tài nguyên, quy trình và biên nhiễu; pilot ngưỡng đó trước.

MySQL hint `MAX_EXECUTION_TIME` không phải giới hạn phổ quát cho mọi statement; nó có phạm vi và điều kiện riêng. Backend vẫn cần deadline ngoài engine và cleanup đã xác minh. Không để việc người học bỏ hint vô hiệu hóa quota. [Optimizer hints MySQL8.4](https://dev.mysql.com/doc/refman/8.4/en/optimizer-hints.html).

Đối chiếu PostgreSQL dùng adapter riêng và format máy đọc của hệ đó. `EXPLAIN ANALYZE` cũng chạy query; DML/side effect không biến thành vô hại vì đang ở màn plan. Lab đo dùng fixture bỏ được. [PostgreSQL18 Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html). Không lấy plan mẫu trên docs làm output đo mới của học viên.

## 9. Recovery, lỗi và hệ phân tán

Bài WAL/ARIES có hai mức hoạt động. Mô hình log cho sửa record, di chuyển checkpoint/flush, crash rồi tính redo/undo; giả định steal/force, pageLSN, durable prefix và record semantics phải công khai. Model checker kiểm invariant trong mô hình ấy. Khi bài yêu cầu recovery thật, backend cấp instance thử riêng, điều khiển fault point được duyệt, restart và đọc lại dữ liệu/constraint từ connection mới. Không dùng animation hoặc một file JSON sau restart làm bằng chứng engine đã phục hồi.

Fault contract ghi loại lỗi: abort transaction, kết thúc process, restart engine, mất một file/snapshot mô phỏng, hay gián đoạn network. Các lỗi đó không tương đương; kill process không chứng minh khôi phục sau mọi media failure hoặc mất điện. Không cho học viên gửi đường dẫn host hay lệnh shell tùy ý để gây lỗi. Control plane chọn action từ danh sách template đã kiểm.

Distributed lab có topology/version rõ, participant IDs ổn định, event message/timeout và network policy trong sandbox. Mô hình2PC phải cho thấy trạng thái prepared/in-doubt; mô hình consensus phải giữ giả định fault/quorum. Không dùng một backend SQL đơn để nhận đã thực thi replication hoặc consensus trên nhiều nút. Bài chỉ cần suy luận có thể hoàn tất trên model web, nhưng nhãn bằng chứng vẫn là model.

## 10. Checker và bài lập luận

Query tương đương được chấp nhận theo contract trên nhiều fixture. Mặc định so multiset, giữ duplicate và NULL; chỉ so sequence/tie-break khi đề yêu cầu. Cột/alias, DECIMAL, collation và tolerance float được khai báo trước. Hidden test phải kiểm cùng yêu cầu đã công bố, không thêm nghiệp vụ bất ngờ. Một query trả hằng số khớp sample phải bị fixture mới làm lộ.

DDL kiểm hành vi constraint và schema; DML kiểm post-state/invariant; routine kiểm tham số và side effect; concurrency kiểm event/invariant/outcome set. Tách ca public phục vụ học khỏi ca xác minh chuyển giao. Reference và checker phải có thử query đúng khác cách viết, query sai điển hình và ca rỗng/NULL/ties theo mục tiêu. Không dùng reference duy nhất làm nguồn chân lý mà không có kiểm tay ca nhỏ.

Chứng minh/thiết kế có rubric trên web, kèm input text/công thức/sơ đồ và revision. Checker hữu hạn có thể kiểm closure, counterexample, graph cycle hoặc một bước thuật toán, nhưng không tự tuyên bố mọi chứng minh bằng văn xuôi đã đúng. Với bài có reviewer, hiển thị `needs-review`; reviewer giữ rubric version, nhận xét từng tiêu chí và cho sửa/nộp lại. Một hình ERD hợp lệ về cú pháp chưa chứng minh phù hợp yêu cầu nghiệp vụ.

## 11. Quota ban đầu và trạng thái lỗi

Các con số sau là **đề xuất để pilot**, không phải số đã benchmark: query thông thường wall5s, tối đa2.000 dòng hiển thị; lịch hai session deadline30s; provision60s; benchmark theo template tối đa90s. Giới hạn CPU/RAM/disk do profile riêng quy định. Bài workload lớn cần profile lớn hơn và được hiển thị trước lượt chạy, không lặng lẽ bỏ timeout của toàn khóa.

Lỗi trả về có category, message đọc được, statement/cell liên quan và cách thử lại. Syntax error chỉ dòng/cột khi driver có. Semantic mismatch cho counterexample và khác biệt dòng thừa/thiếu. Infrastructure error giữ draft và không trừ lượt kỹ năng. Timeout báo việc đã hủy hay còn cleaning; không cho chạy lượt mới trên sandbox chưa sạch. Không hiển thị stacktrace có secret hoặc đường dẫn host cho học viên.

Trình duyệt có trạng thái tải nội dung, cấp môi trường, chạy, đợi khóa và hủy riêng. Nút retry chỉ thực hiện lại đúng phần lỗi. User rời bài có thể quay lại draft/job; sau deadline sandbox có thể hết lease, nhưng báo rõ cần tái tạo môi trường, không mất câu trả lời và gợi ý đã mở.

## 12. Repo và khóa thu phí

Chỉ mở adaptation đã qua gate license, dữ liệu, chất lượng và tái lập ở registry repo. Giữ commit SHA, đường dẫn file gốc, license/notice, tác giả, phạm vi trích/adapt, thay đổi và kết quả kiểm. Không suy quyền sử dụng từ việc repo public hoặc có nhiều stars. Repo chưa rõ quyền hay không chạy lại được đặt ở trạng thái chưa tích hợp.

Một repo tốt về kỹ thuật chưa tự phù hợp cấp độ. Nếu cần C++ hoặc hạ tầng ngoài kiến thức đầu vào, chọn ý/ca kiểm thích hợp rồi biên soạn bài web với prerequisite và attribution; không đưa nguyên một project khó vào sau SELECT rồi gọi là lộ trình. Không lấy public student solutions làm đáp án giảng dạy mặc định.

Các script upstream chỉ chạy trong môi trường kiểm có chủ đích sau khi đọc. Khi đưa vào release, giữ phần code/data thực sự cần và notices tương ứng. Nếu chỉ dùng một ý để viết bài mới, vẫn ghi nguồn nghiên cứu và quyết định biên tập; không trình bày là bài đã import và chạy nguyên repo.

## 13. Backlog có thể nghiệm thu

| Mức | Ticket | Trigger và hành vi cần có | Bằng chứng nghiệm thu |
|---|---|---|---|
| P0 | Lease và quyền | Hai học viên chạy cùng activity | Không đọc/sửa/hủy được tài nguyên của nhau; fixture có version/hash |
| P0 | Attempt/version | Sửa draft sau pass, reload, mở đáp án rồi quay lại seed | Result cũ không áp vào draft mới; draft/seed/reveal được giữ đúng |
| P0 | Checker SQL | Query đúng khác cú pháp; query sai NULL/duplicate | Query đúng đạt; từng misconception có ca bắt cụ thể |
| P0 | Cancel/reset | Query lâu hoặc mất client | Worker dừng theo deadline, cleanup xác minh, lượt sau sạch |
| P0 | DDL profile | CREATE/ALTER/TRUNCATE rồi reset | Fixture trở lại đúng; không nhận rollback đơn thuần là reset |
| P0 | Nhãn bằng chứng | Sửa code ở demo prepared/model | Không tạo result engine giả; capability thiếu được báo riêng |
| P1 | Hai session | Tạo lịch deadlock được mô tả | Có2 connection, wait được observer thấy, không hard-code victim, invariant đúng |
| P1 | Plan adapter | Đổi index/dataset và chạy ANALYZE | Raw plan/version được lưu; parser chịu được format đã kiểm; không gắn cost=ms |
| P1 | Model thuật toán | Đổi FD/log/schedule ở mô hình | Tính lại từ input, bắt ca biên; có giả định và miền được hỗ trợ |
| P1 | Review lập luận | Nộp proof/schema mới | Rubric version, nhận xét từng tiêu chí, revision và trạng thái needs-review |
| P1 | Accessibility | Làm bài không kéo chuột, ở màn hẹp | Mọi hành động có click/bàn phím; dữ liệu/đề vẫn mở; không chỉ dùng màu |
| P2 | Recovery/cluster | Chọn fault point trong template | Instance/cụm riêng, fault log, restart/state check thật và cleanup |
| P2 | Pilot | Hoàn thành rồi làm ca mới sau khoảng nghỉ | Đo khả năng chuyển giao và lỗi theo kỹ năng; không suy từ số click |

Thứ tự P0/P1/P2 là ưu tiên triển khai đề xuất, không cho phép bỏ nội dung sách được yêu cầu. Activity chưa có runner tương ứng có thể được biên soạn và xem lý thuyết, nhưng không quảng bá là lab engine đã sẵn sàng. Trước phát hành khóa đầy đủ phải có đường hoàn tất trên web đúng mức bằng chứng cho tất cả activity được giao.

## 14. Ma trận kiểm trước phát hành

1. SQL: ca rỗng, NULL, duplicate, ties và boundary; query đúng tương đương; query sai chủ đích. Ghi coverage từng activity, không suy từ một bài mẫu ra toàn khóa.
2. Session: xác minh isolation/autocommit trước lịch; timeout/deadlock khác nhau; observer đúng lease; cancel khi đang đợi; victim là tập hợp outcome hợp lệ.
3. State: double-submit/idempotency, reconnect khi job chạy, out-of-order event, edit sau pass, fixture/content version thay đổi, reveal giữ khi quay lại.
4. Resource: query tiêu tốn, output lớn, fixture lỗi, worker crash, orphan lease; kiểm không có job cũ sống và không dùng lại sandbox chưa sạch.
5. Model: miền input hợp lệ, input ngoài miền có báo lỗi, termination, invariant và kiểm độc lập ca nhỏ. Đổi input phải làm visual/result tương ứng đổi.
6. Proof/rubric: nhiều đáp án đúng, phản ví dụ, thiếu giả định; ít nhất hai reviewer thử một mẫu để thống nhất tiêu chí trước pilot.
7. Release: license/attribution/commit của phần tích hợp; hash nội dung/fixture/checker; mọi link/ảnh; PDF và HTML đúng bản hiện tại.

Các kiểm này là yêu cầu cho dev. Báo cáo hiện có phải ghi riêng phần đã chạy thật, phần kiểm mô hình, phần rà nội dung và phần còn cần nghiệm thu. Tài liệu này không nhận đã triển khai API, sandbox hoặc kiểm production.

## Nguồn kỹ thuật đã đối chiếu

Đọc ngày05/11/2026. Các quyết định API, quota, profile và UX phía trên là đề xuất thiết kế của PE; chúng không phải cấu trúc API do MySQL/PostgreSQL cung cấp sẵn.

- [MySQL8.4 EXPLAIN](https://dev.mysql.com/doc/refman/8.4/en/explain.html): phân biệt plan và execution, TREE của ANALYZE.
- [MySQL8.4 isolation](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html): snapshot/locking theo hệ và mức isolation.
- [MySQL8.4 deadlock example](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlock-example.html): quan sát locks và waits.
- [MySQL8.4 error handling](https://dev.mysql.com/doc/refman/8.4/en/innodb-error-handling.html): scope rollback khi lỗi.
- [MySQL8.4 deadlock handling](https://dev.mysql.com/doc/refman/8.4/en/innodb-deadlocks-handling.html): ứng dụng cần xử lý/retry.
- [MySQL8.4 implicit commit](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html) và [atomic DDL](https://dev.mysql.com/doc/refman/8.4/en/atomic-ddl.html): giới hạn rollback/reset.
- [MySQL8.4 KILL](https://dev.mysql.com/doc/refman/8.4/en/kill.html): statement/connection là hai phạm vi khác nhau.
- [MySQL8.4 optimizer hints](https://dev.mysql.com/doc/refman/8.4/en/optimizer-hints.html): giới hạn và phạm vi hint thời gian.
- [PostgreSQL18 isolation](https://www.postgresql.org/docs/18/transaction-iso.html), [Using EXPLAIN](https://www.postgresql.org/docs/18/using-explain.html) và [client defaults](https://www.postgresql.org/docs/18/runtime-config-client.html): đối chiếu engine, timeout và cấu hình phiên.
