from pathlib import Path
content = r'''# AD18 · Bảo trì summary bằng delta và bất biến

Đã học: AD72, AD01, S12. Nguồn: DSC 7e §11.2–11.3, §16.5. Môi trường: SQL/batch lab trên web và canvas delta có signed multiplicity. Mô hình tính đúng không có nghĩa MySQL có materialized-view operator cho mọi expression.

## Report không nên cộng lại cùng một sự kiện

Mỗi phút dịch vụ nhận một batch sales mới. Tính report từ đầu có thể tốn công; chỉ cộng batch vào total lại có thể nhân doanh thu khi reload. Incremental view maintenance cần biết delta biểu diễn thay đổi nào, trên base version nào, và cách update summary nhất quán với dữ liệu gốc.

View logic là một query; materialized summary là dữ liệu được lưu để trả query nhanh hơn. Nó có thể stale. MySQL có thể dùng bảng summary, routine và job do ứng dụng quản lý; không gán cú pháp CREATE MATERIALIZED VIEW của hệ khác vào MySQL. Bất biến cần giữ là summary bằng query gốc ở version đã công bố, trước khi xét số timing.

## Ví dụ 1: SUM cần trạng thái cho NULL và nhóm rỗng

Fact f=(event_id,group,amount) có (1,A,10),(2,A,NULL),(3,B,5). Nhóm A có COUNT(*)=2, COUNT(amount)=1, SUM=10, AVG=10. Để xử lý deletions đúng, giữ row_count, nonnull_count và sum_nonnull. SUM hiển thị NULL khi nonnull_count=0; group biến mất khi row_count=0 đối với GROUP BY trên các rows còn lại.

Insert (4,A,20) cho state A=(3,2,30), AVG=15. Delete event1 cho (2,1,20), AVG=20. Delete event4 còn một row NULL: state=(1,0,0 nội bộ), nhưng SUM và AVG hiển thị NULL. Delete nốt event2 mới làm group A biến mất. Một cột total đơn lẻ không phân biệt tổng0 thật, toàn NULL và không còn nhóm.

```text
apply_delta(state, amount, sign):
    row_count += sign
    if amount is not NULL:
        nonnull_count += sign
        sum_nonnull += sign * amount
    reject inconsistent negative counts at commit boundary
    if row_count == 0: remove group
    else display SUM as NULL iff nonnull_count == 0
    display AVG as sum_nonnull/nonnull_count when count > 0
```

Sign +1 là insert một occurrence, −1 là delete một occurrence. UPDATE được tách old row−1 và new row+1. Cần before image hoặc key để trừ đúng giá trị cũ. Hai rows cùng amount vẫn là hai occurrences. Nếu amount có thể âm vì refund, dấu delta là một chiều khác: refund −10 không tự là delete của sale +10.

Bất biến là summary state bằng aggregate của base multiset sau mỗi transaction/batch hoàn tất. Insert/delete sửa đúng đóng góp của occurrence đó nên bảo toàn invariant bằng induction, với điều kiện initial state được tạo đúng từ base snapshot. Chi phí đổi một group là expected O(1) với hash hoặc O(log G) với ordered index, ngoài storage/locking. Không áp chi phí ấy cho mọi aggregate.

## Ví dụ 2: AVG và MIN không có cùng delta rule

Nhóm {5,10,20} có sum35,count3. Xóa20 cho AVG=15/2=7.5. Giữ avg≈11.6667 rồi trừ20 không có nghĩa đúng. SUM và count của cùng population là sufficient state cho AVG trong mô hình này.

MIN5,count3,sum35 lại không đủ biết min sau khi xóa5. Hai multisets {5,10,20} và {5,7,23} có cùng ba số ấy nhưng min mới lần lượt10 và7. Cần multiset/index bổ sung hoặc recompute group. Phản ví dụ xác nhận rằng không có hàm từ riêng bộ state cũ ấy và giá trị bị xóa tới mọi min mới đúng.

COUNT DISTINCT còn cần membership counts: nhóm có A hai occurrences và B một occurrence. Xóa một A vẫn có distinct count2; chỉ khi countA từ1 về0 mới giảm. Cấu trúc xấp xỉ có thể phù hợp với một số report nhưng phải ghi error/deletion contract, không đổi một chỉ số exact thành approximate mà giữ nguyên nhãn và đáp án.

## Ví dụ 3: join delta có cross term

Old R có r1, old S có s1, cùng join-key k. View có r1s1. Insert đồng thời r2 và s2 cùng key: view mới có r1s1,r1s2,r2s1,r2s2; delta có ba pairs. Với old snapshots:

```text
Delta(R join S)
 = (DeltaR join oldS)
   bag-union (oldR join DeltaS)
   bag-union (DeltaR join DeltaS)
```

Chỉ dùng hai terms đầu sẽ bỏ pair mới–mới. Dùng newR join DeltaS rồi vẫn cộng cross term sẽ đếm pair ấy hai lần. Cách khác đúng là DeltaR join oldS cộng newR join DeltaS, với versions được ghi rõ. Khi có delete, signed multiplicity và thời điểm của từng base phải nhất quán.

Proof cho một tuple pair khớp predicate: multiplicity mới là (mR+δR)(mS+δS); trừ multiplicity cũ mRmS được mRδS+δRmS+δRδS. Ba terms tương ứng ba nguồn của pairs. Đó là luật bag join; dùng set UNION có thể loại occurrences hợp lệ. Không mang luật inner join sang outer join nguyên xi: outer join còn phải thêm/bỏ hàng bù khi match count chuyển0↔positive.

## Snapshot, replay và transaction

Baseline summary cần base snapshot version V. Delta tiếp theo phải bắt đầu đúng sau V, không bỏ và không lặp. Nếu đọc nhiều nguồn ở thời điểm không nhất quán, có thể không có một V duy nhất thỏa invariant. Timestamp max đơn thuần có thể bỏ ties hoặc late updates; offset/batch ID phải đi cùng dữ liệu và protocol capture.

Để reload batch B không cộng lại, dùng processed_batches(B UNIQUE) cùng transaction update base/summary hoặc protocol atomic tương ứng. Hai workers cùng B: chỉ một bên ghi key thành công; bên kia trả outcome đã xử lý theo policy. Nếu commit key trước summary, crash có thể khiến B được báo hoàn tất nhưng total chưa cộng. Nếu summary commit trước key, retry có thể cộng hai lần. Transaction cần giữ hai thay đổi không tách rời.

Transaction local không bao trùm mọi hệ ngoài. Nếu delta đến qua queue, checkpoint/ack và database commit cần replay/deduplication rõ. Exactly-once ở một operator chưa bảo đảm report không trộn versions. Readers có thể đọc snapshot cũ nhất quán trong lúc refresh; freshness label cho biết điều đang xem. Cache và materialization cần cùng quy ước version.

Reconciliation định kỳ chạy query gốc rồi so summary theo grain, NULL, multiplicity và version. Nó phát hiện lỗi đã xảy ra, không thay thiết kế atomic. Log batch, source offset và transformation version giúp định vị thay đổi nào làm invariant sai. Không gọi một lần tổng khớp là chứng minh mọi lịch cập nhật đúng.

## Chọn view nào để lưu?

Lựa chọn dựa trên workload, chi phí refresh/storage và độ mới cho phép. Một view phủ query nếu có rewrite đúng từ view đến kết quả cần, không chỉ vì cùng vài cột. Sum/count theo ngày có thể roll up AVG tháng khi cùng population; AVG ngày không count chưa đủ. View chỉ chứa paid orders không tự trả được query mọi status nếu không có nguồn bổ sung.

Lúc workload đổi, lợi ích cũ có thể mất: summary hiếm được đọc nhưng update liên tục có thể làm writes nặng hơn. Đo cả đường đọc và refresh trên cùng phiên bản, rồi kiểm lại query semantics. Materialization là tradeoff, không phải bảo đảm tăng tốc miễn phí.

## Luyện tập

1. Trace insert event4, delete event1, delete event4 của ví dụ1; ghi row_count,nonnull_count,SUM,AVG và nhóm còn hay không.
2. Dùng hai multisets có cùng min/count/sum nhưng min sau delete khác nhau để bác state MIN không đủ.
3. Old R={r1,r2}, old S={s1}, DeltaR={r3}, DeltaS={s2,s3}; mọi key là k. Liệt kê ba terms và tổng delta join.
4. Tự làm: thiết kế refresh paid revenue cho orders có update pending→paid và paid→refunded. Ghi before/after images,batch ID,transaction,freshness và test replay/correctness.

## Gợi ý

Tầng1: SQL SUM toàn NULL không giống số0 nội bộ; UPDATE cần loại đóng góp cũ trước khi thêm đóng góp mới.

Tầng2: câu3 có |DeltaR||S|+|R||DeltaS|+|DeltaR||DeltaS|=1+4+2. Câu4 xem status change như xóa/thêm vào view theo định nghĩa nghiệp vụ.

## Đáp án và lập luận

1. Sau insert: (3,2,30,15,còn). Sau xóa1: (2,1,20,20,còn). Sau xóa4: (1,0,NULL,NULL,còn). Chỉ xóa nốt row NULL mới làm group biến mất.
2. {5,10,20} và {5,7,23} đều min5,count3,sum35; delete5 cho10 và7. Chọn index/multiset hoặc recompute, cùng chi phí tương ứng.
3. Term1 r3s1; term2 r1s2,r1s3,r2s2,r2s3; term3 r3s2,r3s3. Delta7, view mới9 pairs so old2. Cross term xuất hiện đúng một lần.
4. Rubric: định nghĩa paid revenue/refund time; before/after đủ; batch chỉ apply một lần; base/summary cùng version. Reload cùng B không đổi total; đổi amount trừ old cộng new; status ra khỏi view loại đúng đóng góp. Không chấp nhận chỉ kiểm insert thuần hoặc nhìn một tổng cuối.

## Biến thể và cách kiểm

Đổi all-NULL/real-zero, group disappearance, duplicate values, simultaneous deltas và replay. Checker so query gốc và summary ở cùng base version; proof nêu induction và version trong mỗi law. Bỏ cross term thì feedback chỉ pair mới–mới bị mất. Cộng lại B thì feedback chỉ nhóm đổi khi input không làm base đổi.

## Học trên web

Canvas old/Delta/new cho xem witness pairs và có nhãn mô hình. SQL workspace chạy batch trong MySQL schema riêng rồi đọc lại state; nút replay B thử idempotence. Backend lo transaction/reset. Chỉ event engine thật mới cung cấp bằng chứng rollback/atomic trên build đó; không yêu cầu learner cài worker.

## Nguồn và đối chiếu

DSC7e §16.5 materialized views và §11.2–11.3 warehouse/OLAP; nối AD72 bằng delta laws và invariant. Fixture và lập luận ví dụ do PE biên soạn. Bảng summary MySQL là thiết kế ứng dụng, không phải tính năng materialized view của hệ khác được giả định sẵn.
'''
Path(__file__).resolve().parents[1].joinpath('lessons/AD18.md').write_text(content,encoding='utf-8')
