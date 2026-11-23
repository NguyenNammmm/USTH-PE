from pathlib import Path
text=r'''# AD73 · Big-data storage: file, shard và key-value

Đã học: B01, P01, I01. Nguồn: DSC 7e §10.1–10.2. Môi trường: storage/partition canvas và services được khai báo trong lab web. Số replicas trên hình không phải bằng chứng durability của một cluster thật.

## Nhiều bytes chưa phải toàn bộ vấn đề

Một triệu files mỗi file2KiB chỉ khoảng2GB payload nhưng tạo rất nhiều metadata entries và requests nhỏ. Một file vàiGB đọc tuần tự có thể dễ xử lý hơn tiny objects có cùng tổng dung lượng. Big data còn có tốc độ phát sinh, đa dạng cấu trúc và kiểu truy vấn. Giải pháp phải bắt đầu từ workload và đảm bảo cần giữ.

Nguồn có thể là logs, sensors, documents, transactions hoặc media. Batch tổng hợp khác key lookup latency thấp; streaming alert khác archive. Không dùng nhãn distributed để bỏ qua schema, index, consistency hoặc chi phí mạng. Các cơ chế chuyên sâu còn được học ở phần phân tán; bài này xác định trách nhiệm của lớp storage trước khi xây compute DAG.

## Ví dụ 1: copies và metadata

Distributed file system chia file thành chunks. Metadata map file tới danh sách chunk IDs có thứ tự, rồi map chunk tới locations. Client đọc từ chunk servers. Replication đặt copies ở failure domains khác nhau. Nếu metadata duy nhất mất, bytes có thể còn nhưng client không biết dựng lại file; ba bản sao data chưa đủ bảo đảm toàn dịch vụ luôn đọc được.

Model có file F=[c1,c2]. c1 ở nodes A,B,C; c2 ở B,C,D. Mất A vẫn đọc được c1 từ B/C và c2 từ B/C/D nếu metadata và kết nối còn hoạt động. Nếu sau đó B,C mất trước repair, c1 không còn copy; F không đọc đủ dù c2 vẫn còn ở D. Lịch lỗi và thời gian repair là đầu vào của kết luận, không chỉ đếm nodes hỏng cuối cùng.

Repair model: phát hiện node bị nghi unavailable, tìm chunks thiếu replicas, chọn healthy source và destination phù hợp, copy rồi kiểm checksum/version, sau đó mới thêm location mới. Bất biến là chỉ công nhận copy đủ và đúng version. Timeout chỉ làm node bị nghi, không chứng minh node chết; khi node trở lại phải xử lý stale data/ownership. Repair tốn network/disk và có thể tranh tài nguyên với workload đang phục vụ.

Chunk lớn giúp đọc tuần tự và giảm metadata trên mỗi byte, nhưng tiny files vẫn cần entries riêng hoặc một cơ chế packing có index. DFS không tự cung cấp relational transactions, FK hay secondary index trên mọi field. Append, rename và overwrite có semantics theo hệ; không suy atomicity giống nhau chỉ vì API có cùng tên.

## Ví dụ 2: shard key định tuyến công việc

Orders có keys1..8. Hash partition h(k)=k mod4 phân keys vào bốn shards. Query một key có thể route thẳng; range1..8 có thể hỏi mọi shard vì hash không giữ thứ tự. Range partition [1,3),[3,5),[5,7),[7,9) giúp quét khoảng nhưng append theo key tăng có thể dồn writes vào shard cuối.

Chọn customer_id giúp đặt orders cùng khách gần nhau cho query theo khách; một customer khổng lồ thành hot key. Chọn order_id có thể chia đều keys hơn nhưng report theo khách phải fan out. Số keys bằng nhau không bảo đảm requests bằng nhau: một key có thể nhận phần lớn traffic. Cần đo phân bố requests, bytes và chi phí thao tác, không chỉ row counts.

Rebalance không chỉ đổi công thức mod rồi để client tự thích nghi. Trong lúc copy còn có writes nên cần map version/ownership, snapshot và delta, cutover rồi retire bản cũ theo protocol. Nếu writer còn dùng old shard trong khi reader đã chuyển sang new shard chưa nhận delta, hệ có thể trả stale hoặc mất update. Consistent hashing/virtual nodes giảm phần keys phải chuyển khi membership đổi, nhưng không tự bảo đảm cutover đúng.

Một model cutover có các states: old owner nhận writes; copy snapshot tới new owner; bắt kịp delta sau snapshot; công bố map version mới; chuyển hoặc từ chối request dùng version cũ theo policy; chỉ retire old copy khi không còn cần cho recovery. Bất biến mong muốn là mỗi accepted write có một owner và không bị bỏ khỏi state được công bố. Đây là protocol cần chứng minh và test theo hệ thật, không phải một thao tác kéo tile.

## Ví dụ 3: key-value GET/PUT và lost update

Key cart:7 chứa một JSON object ở version5. Hai workers cùng GET, mỗi worker thêm một item riêng rồi PUT toàn object. Last-writer-wins có thể giữ một item và làm mất item kia dù cả hai requests nhận response thành công. API đơn giản chưa tự bảo vệ read–modify–write.

Compare-and-set model: GET trả value/version; PUT_IF_VERSION(key,newvalue,5) chỉ thành công khi current version5 và đổi thành6. Writer thứhai dùng version5 nhận conflict, đọc lại và merge/retry theo business rule. Không phải mọi JSON merge đều hợp lệ; retry cũng phải tránh cộng lại cùng một ý định. Atomic increment có thể giải counter của một key, nhưng invariant nhiều keys cần transaction hoặc protocol khác.

Pseudocode:

```text
repeat within retry budget:
    old,version = get(key)
    new = apply_intent(old,intent_id)
    if compare_and_set(key,version,new): return success
return conflict_or_retry_exhausted
```

Input gồm key, intent và policy lặp; output phải phân biệt success, conflict và lỗi chưa biết outcome. Điều kiện đúng không chỉ là loop có giới hạn: apply_intent cần idempotence phù hợp, CAS phải có semantics đã khai báo và version không tái dùng gây ABA ngoài contract. Budget bảo đảm vận hành dừng, không bảo đảm mọi caller cuối cùng thắng.

Key-value thuận lợi cho key lookups hoặc denormalized value theo workload. Query field bên trong cần scan, secondary index hoặc lớp truy vấn khác. Document store thêm truy vấn cấu trúc; wide-column store tổ chức theo row/column families. Không gọi mọi NoSQL là cùng mô hình. Secondary index còn phải được duy trì cùng base writes hoặc công bố rõ độ trễ; thêm một map không tự tạo consistency.

## Replication khác partitioning

Partitioning chia miền dữ liệu; replication tạo copies của cùng miền. Hệ có thể làm cả hai. Read replica có thể lag: đọc ở node khác sau write chưa chắc thấy write nếu không có read-your-writes contract. Quorum overlap là một điều kiện trong một số protocols; công thức W+R>N không tự chứng minh mọi implementation linearizable khi bỏ qua versions, concurrency và failures.

Parallel database còn có query operators, statistics và transaction support; distributed file store không thay các lớp ấy. SQL-on-files có thể dùng cùng dữ liệu nhưng phải bổ sung isolation/update/catalog/failure semantics. Chọn hệ cần expected guarantees, không chỉ một dòng “scale horizontally”. AD20 sẽ xét computation/retry trên input snapshot đã xác định.

## Luyện tập

1. Trên file F, chỉ ra nơi đọc sau khi mất A; xét tiếp mất B,C trước repair. Phân biệt còn data copy với còn metadata service.
2. So hash/range shards cho point lookup, range query và hot customer. Tạo workload chia đều keys nhưng lệch requests.
3. Trace hai writers GET version5 rồi PUT. Thay bằng CAS và nêu response/state của writer thua; thêm một retry có cùng intent ID.
4. Tự làm: thiết kế storage cho append logs và cart updates, cùng snapshot batch analytics. Ghi metadata, partition, replication, transaction và index nằm ở đâu; tạo một failure test và một node-return test.

## Gợi ý

Tầng1: tổng bytes không đo hết metadata; replicas không đồng nghĩa consistency; key distribution không đồng nghĩa request distribution.

Tầng2: CAS chỉ cập nhật khi version khớp. Range qua hash thường fan out. Cutover cần nối map version với state đã copy, không đổi routing trước khi dữ liệu đủ theo protocol.

## Đáp án và lập luận

1. Sau A, c1 còn B/C, c2 còn B/C/D. Sau A→B,C trước repair, c1 không còn; F thiếu một chunk. Metadata/kết nối vẫn là điều kiện riêng, không suy từ vị trí copies.
2. Hash hợp key lookup nhưng không giữ range; range có locality nhưng có thể hotspot. Một key có một triệu requests làm một shard quá tải dù row counts đều. Cần workload metrics và policy xử lý skew.
3. Writer đầu CAS5→6 thắng; writer sau CAS5 conflict. Nó đọc version6, áp ý định chưa có rồi thử lại; không ghi đè bằng object từversion5. Test cùng intent ID không thêm item hai lần khi response bị mất.
4. Rubric: tách file/log và key-value/transaction contracts, snapshot cho batch, index policy và failure states. Node cũ trở lại không được tự ghi đè version mới. Thiết kế khác được chấp nhận khi guarantees và evidence rõ; animation không thay ca cluster thật.

## Biến thể và cách kiểm

Đổi file sizes/counts, placement, hot keys, node rejoins và concurrent writes. Model checker kiểm placement/CAS/invariant theo protocol; proof cần assumptions. Bài đo thật phải có engine/version/config/events. Không lấy chi phí ngẫu nhiên của simulator làm benchmark.

## Học trên web

Canvas cho đặt chunks/shards và gửi requests, hiện map version cùng dữ liệu còn đọc được. KV lab dùng backend hoặc model CAS được ghi rõ. Learner không cài cluster; dev chuẩn bị scenario, reset và quota. Nếu chưa có engine thực cho một scenario, màn phải nói đó là mô hình theo assumptions.

## Nguồn và đối chiếu

DSC7e §10.1 motivation/sources/querying và §10.2 DFS,sharding,key-value,parallel/distributed databases,replication/consistency. Ví dụ PE làm rõ một failure schedule và CAS; các guarantees sâu hơn được tiếp tục ở phần distributed. Không thay những cơ chế ấy bằng một nhãn NoSQL chung.
'''
Path(__file__).resolve().parents[1].joinpath('lessons/AD73.md').write_text(text,encoding='utf-8')
