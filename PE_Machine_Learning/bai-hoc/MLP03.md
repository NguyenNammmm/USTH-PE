<a id="mlp03"></a>

# MLP03 · Gộp cụm theo khoảng cách gần nhất

[Về mục lục](../README.md)

Phân cụm phân cấp kết tụ (agglomerative clustering) bắt đầu với mỗi điểm là một cụm. Ở đề lõi, dùng liên kết đơn (single linkage), khoảng cách giữa hai cụm là khoảng cách nhỏ nhất giữa hai thành viên. Mỗi lần gộp i < j, giữ vị trí i và bỏ vị trí j. Hòa khoảng cách chọn cặp vị trí (i,j) nhỏ nhất. Nộp lịch sử [độ cao, danh sách chỉ số mẫu đã sắp tăng] cho đến khi còn một cụm.

Tiên quyết · ML23

### A · Dự đoán

1. Hai chỉ số nào gộp trước? Ở bước kế tiếp, hãy ghi khoảng cách từ cụm vừa gộp đến cụm gần nhất.
2. Nộp lần lượt độ cao và các chỉ số gốc cho cả ba phép gộp.

### B · Chạy mẫu

```python
import numpy as np

def linkage_history(X, linkage):
    from itertools import combinations
    X = np.asarray(X, dtype=float)
    aggregate = min
    groups = [[i] for i in range(len(X))]
    history = []
    while len(groups) > 1:
        dist, i, j = min(((aggregate((abs(X[a] - X[b]) for a in groups[i] for b in groups[j])), i, j) for i, j in combinations(range(len(groups)), 2)))
        groups[i] = sorted(groups[i] + groups[j])
        groups.pop(j)
        history.append((float(dist), groups[i]))
    return history

X = [0, 2, 5, 6]
linkage = 'single'
print(linkage_history(X, linkage))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Sau khi gộp, chỉ số của mẫu ban đầu và vị trí hiện tại của cụm khác nhau ở chỗ nào?
2. Lấy hai cụm cuối của ví dụ. Cặp thành viên nào xác định độ cao theo liên kết đơn?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay X rồi giải lại đề lõi.  
**D1** · `X = [0,1,4,9]  linkage = "single"`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [2,4,6,8]  linkage = "single"`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [4,0,3,9]  linkage = "single"`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`X = [0,1,5]  linkage = "single"`

Gộp 0 và 1 tại độ cao 1. Cụm đó cách điểm 5 gần nhất một đoạn 5−1.

**Kết quả** · `[[1,[0,1]],[4,[0,1,2]]]`

#### Ví dụ 2

`X = [4,2,0]  linkage = "single"`

Hai cặp hòa ở độ cao 2. Chọn vị trí 0,1 trước rồi gộp điểm cuối.

**Kết quả** · `[[2,[0,1]],[2,[0,1,2]]]`

#### Ví dụ 3

`X = [1,2,8,10]  linkage = "single"`

Gộp hai điểm đầu ở độ cao 1, hai điểm sau ở 2. Hai cụm gặp tại 8−2.

**Kết quả** · `[[1,[0,1]],[2,[2,3]],[6,[0,1,2,3]]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [0,3,4,9]  linkage = "single"`  
Kết quả tự nộp ____________________

**E2** · `X = [0,2,4]  linkage = "single"`  
Kết quả tự nộp ____________________

**E3** · `X = [5,0,6,1]  linkage = "single"`  
Kết quả tự nộp ____________________

**E4** · `X = [1,7]  linkage = "single"`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `linkage_history(X, linkage)`. Trong đề lõi, dùng linkage = 'single'. X là vectơ hữu hạn có ít nhất một mẫu. Trả lịch sử theo quy tắc ở đầu phiếu. Báo ValueError cho dữ liệu hoặc phương pháp không hợp lệ. Bài F bổ sung liên kết đầy đủ. [Tệp điền mã](../thuc-hanh/MLP03.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [1,4,9,10]  linkage = "single"`  
Kết quả tự nộp ____________________

**R2** · `X = [1,4,7]  linkage = "single"`  
Kết quả tự nộp ____________________

**R3** · `X = [6,1,8,2]  linkage = "single"`  
Kết quả tự nộp ____________________

**R4** · `X = [2,10]  linkage = "single"`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Đổi sang liên kết đầy đủ (complete linkage), dùng khoảng cách lớn nhất giữa hai thành viên. Với [0,2,5,6], cắt cây ở độ cao 4 và nộp các nhóm theo cả hai phương pháp.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP03](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp03)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[[1,[2,3]],[2,[0,1]],[3,[0,1,2,3]]]`

**D1** · `[[1,[0,1]],[3,[0,1,2]],[5,[0,1,2,3]]]`

**D2** · `[[2,[0,1]],[2,[0,1,2]],[2,[0,1,2,3]]]`

**D3** · `[[1,[0,2]],[3,[0,1,2]],[5,[0,1,2,3]]]`

**E1** · `[[1,[1,2]],[3,[0,1,2]],[5,[0,1,2,3]]]`

**E2** · `[[2,[0,1]],[2,[0,1,2]]]`

**E3** · `[[1,[0,2]],[1,[1,3]],[4,[0,1,2,3]]]`

**E4** · `[[6,[0,1]]]`

**R1** · `[[1,[2,3]],[3,[0,1]],[5,[0,1,2,3]]]`

**R2** · `[[3,[0,1]],[3,[0,1,2]]]`

**R3** · `[[1,[1,3]],[2,[0,2]],[4,[0,1,2,3]]]`

**R4** · `[[8,[0,1]]]`

**S** · `[[2,[0,2]],[2,[0,1,2]],[4,[0,1,2,3]]]`

Với [0,2,5,6], hai mẫu có chỉ số 2 và 3 gộp ở độ cao 1. Hai mẫu 0 và 1 gộp ở độ cao 2. Hai cụm gặp nhau ở độ cao 3.

Khi hòa, so cặp vị trí hiện tại trước. Khi nộp kết quả, ghi chỉ số mẫu ban đầu và lấy khoảng cách nhỏ nhất giữa các thành viên.

**Vận dụng.** Liên kết đơn cho một cụm. Liên kết đầy đủ cho hai cụm chỉ số [0,1] và [2,3], chỉ gộp cả hai ở độ cao 6.

```python
import numpy as np

def linkage_history(X, linkage):
    from itertools import combinations
    X = np.asarray(X, dtype=float)
    if X.ndim != 1 or X.size == 0 or not np.isfinite(X).all() or linkage not in {"single", "complete"}:
        raise ValueError("Đầu vào không hợp lệ")
    aggregate = min if linkage == "single" else max
    groups = [[i] for i in range(len(X))]
    history = []
    while len(groups) > 1:
        dist, i, j = min((aggregate(abs(X[a] - X[b]) for a in groups[i] for b in groups[j]), i, j)
                         for i, j in combinations(range(len(groups)), 2))
        groups[i] = sorted(groups[i] + groups[j])
        groups.pop(j)
        history.append((float(dist), groups[i]))
    return history
```
