<a id="mlp02"></a>

# MLP02 · Lọc cột theo phương sai

[Về mục lục](../README.md)

Bộ lọc phương sai (variance filter) giữ các cột có phương sai tổng thể trên train lớn hơn cutoff. Chọn lại các cột đó trong X theo thứ tự cũ. Nộp [danh sách chỉ số cột, ma trận X sau lọc]. Chỉ số đầu là 0.

Tiên quyết · ML17

### A · Dự đoán

1. Phương sai của ba cột train là gì? Cột nào vượt ngưỡng 0,5?
2. Ghi chỉ số các cột được giữ và hàng kết quả sau lọc. Đếm số cột trước khi nộp.

### B · Chạy mẫu

```python
import numpy as np

def variance_filter(train, X, cutoff):
    train, X = (np.asarray(train, dtype=float), np.asarray(X, dtype=float))
    keep = np.flatnonzero(train.var(axis=0) > cutoff)
    return (keep, X[:, keep])

train = [[1, 0, 0], [1, 2, 4]]
X = [[8, 4, 2]]
cutoff = 0.5
print(variance_filter(train, X, cutoff))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Nếu một cột vừa bằng ngưỡng, dấu so sánh nào quyết định nó có được giữ?
2. Chọn cột thứ hai và tính tay phương sai tổng thể. Kết quả khác gì nếu dùng mẫu số n − 1?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay cutoff rồi giải lại đề lõi.  
**D1** · `train = [[1,0,0],[1,2,4]]  X = [[8,4,2]]  cutoff = 1`

Thay X rồi giải lại đề lõi.  
**D2** · `train = [[1,0,0],[1,2,4]]  X = [[2,7,8],[0,1,2]]  cutoff = 0.5`

Thay train rồi giải lại đề lõi.  
**D3** · `train = [[2,0,1],[2,4,3]]  X = [[8,4,2]]  cutoff = 0.5`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`train = [[0,2],[6,2]]  X = [[9,8]]  cutoff = 2`

Phương sai cột đầu bằng 9, cột sau bằng 0. Chỉ giữ cột đầu.

**Kết quả** · `[[0],[[9]]]`

#### Ví dụ 2

`train = [[0,0],[2,6]]  X = [[4,1],[2,5]]  cutoff = 1`

Cột đầu bằng ngưỡng nên bị bỏ, cột sau có phương sai 9.

**Kết quả** · `[[1],[[1],[5]]]`

#### Ví dụ 3

`train = [[0,0,1],[4,2,5]]  X = [[9,8,7]]  cutoff = 2`

Phương sai [4,1,4]. Giữ cột 0 và 2 theo thứ tự ban đầu.

**Kết quả** · `[[0,2],[[9,7]]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `train = [[0,2],[4,2]]  X = [[8,7]]  cutoff = 0`  
Kết quả tự nộp ____________________

**E2** · `train = [[0,0],[2,4]]  X = [[9,7]]  cutoff = 1`  
Kết quả tự nộp ____________________

**E3** · `train = [[1,4],[1,4]]  X = [[3,8]]  cutoff = 0`  
Kết quả tự nộp ____________________

**E4** · `train = [[1,0],[5,2]]  X = [[1,2],[3,4]]  cutoff = 0.5`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `variance_filter(train, X, cutoff)`. Với train 2D hữu hạn không rỗng và X 2D hữu hạn cùng số cột, giữ cột có phương sai tổng thể > cutoff hữu hạn ≥ 0. Trả (chỉ số cột, X đã chọn), cho phép 0 cột được giữ. Báo ValueError nếu kích thước hoặc cutoff sai. [Tệp điền mã](../thuc-hanh/MLP02.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `train = [[1,3],[5,3]]  X = [[2,6]]  cutoff = 0`  
Kết quả tự nộp ____________________

**R2** · `train = [[0,0],[4,2]]  X = [[7,9]]  cutoff = 1`  
Kết quả tự nộp ____________________

**R3** · `train = [[3,2],[3,2]]  X = [[8,9],[5,1]]  cutoff = 0`  
Kết quả tự nộp ____________________

**R4** · `train = [[2,0],[6,4]]  X = [[5,2],[6,3]]  cutoff = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Thử chọn một cột bằng sai số xác thực. Với train = [[0,0],[1,0],[2,1],[3,1]], y = [0,2,4,6], validation = [[4,0],[5,1]] và y = [8,10], khớp riêng từng cột bằng hồi quy có hệ số tự do.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP02](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp02)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[[1,2],[[4,2]]]`

**D1** · `[[2],[[2]]]`

**D2** · `[[1,2],[[7,8],[1,2]]]`

**D3** · `[[1,2],[[4,2]]]`

**E1** · `[[0],[[8]]]`

**E2** · `[[1],[[7]]]`

**E3** · `[[],[[]]]`

**E4** · `[[0,1],[[1,2],[3,4]]]`

**R1** · `[[0],[[2]]]`

**R2** · `[[0],[[7]]]`

**R3** · `[[],[[],[]]]`

**R4** · `[[0,1],[[5,2],[6,3]]]`

**S** · `[[0],[[8]]]`

Ba phương sai là 0, 1 và 4. Giữ cột 1 và 2 nên hàng [8,4,2] của X trở thành [4,2].

Nếu giữ thừa một cột, so lại phương sai với cutoff bằng dấu >. Tính phương sai trên train với mẫu số n.

**Vận dụng.** Cột 0 cho đường y = 2x và MSE bằng 0. Cột 1 dự đoán [1,5] và có MSE bằng 37.

```python
import numpy as np

def variance_filter(train, X, cutoff):
    train, X = np.asarray(train, dtype=float), np.asarray(X, dtype=float)
    if train.ndim != 2 or min(train.shape) == 0 or X.ndim != 2 or X.shape[1] != train.shape[1] or not np.isfinite(cutoff) or cutoff < 0 or not np.isfinite(train).all() or not np.isfinite(X).all():
        raise ValueError("Đầu vào không hợp lệ")
    keep = np.flatnonzero(train.var(axis=0) > cutoff)
    return keep, X[:, keep]
```
