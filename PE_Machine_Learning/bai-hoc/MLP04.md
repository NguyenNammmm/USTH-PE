<a id="mlp04"></a>

# MLP04 · Gán nhãn cụm mật độ trong một chiều

[Về mục lục](../README.md)

Khi phân cụm theo mật độ có nhiễu (DBSCAN, density-based spatial clustering of applications with noise), lân cận gồm mọi điểm cách không quá eps, kể cả chính nó. Điểm lõi (core) có ít nhất min_samples điểm trong lân cận. Duyệt lõi theo chỉ số tăng, nối các lõi kề nhau và gán các điểm biên (border) chưa nhãn. Nộp vectơ nhãn, cụm đầu mang số 0, nhiễu mang số −1.

Tiên quyết · ML23

### A · Dự đoán

1. Những điểm nào là lõi ở bán kính 0,5? Điểm 8 có thể nhận nhãn từ lõi nào?
2. Ghi một nhãn cho mỗi điểm theo thứ tự ban đầu. Đánh dấu vị trí nào mang nhãn nhiễu.

### B · Chạy mẫu

```python
import numpy as np

def dbscan_1d(x, eps, min_samples):
    from collections import deque
    x = np.asarray(x, dtype=float)
    adj = np.abs(x[:, None] - x[None, :]) <= eps
    core = adj.sum(axis=1) >= min_samples
    labels = np.full(len(x), -1)
    cluster = 0
    for i in np.flatnonzero(core):
        if labels[i] >= 0:
            continue
        labels[i] = cluster
        queue = deque([i])
        while queue:
            current = queue.popleft()
            new = np.flatnonzero(adj[current] & (labels == -1))
            labels[new] = cluster
            queue.extend(new[core[new]])
        cluster += 1
    return labels

x = [0, 0.5, 1, 4, 4.5, 5, 8]
eps = 0.5
min_samples = 3
print(dbscan_1d(x, eps, min_samples))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Theo dõi một điểm biên vừa nhận nhãn. Vì sao thuật toán chỉ tiếp tục mở rộng từ các điểm lõi?
2. Từ điểm 0,5, lần theo các hàng được gán cụm nhưng không đưa vào hàng đợi mở rộng.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay eps rồi giải lại đề lõi.  
**D1** · `x = [0,0.5,1,4,4.5,5,8]  eps = 1  min_samples = 3`

Thay min_samples rồi giải lại đề lõi.  
**D2** · `x = [0,0.5,1,4,4.5,5,8]  eps = 0.5  min_samples = 2`

Thay x rồi giải lại đề lõi.  
**D3** · `x = [0,1,2,3,7]  eps = 0.5  min_samples = 3`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`x = [0,1,2,7]  eps = 1  min_samples = 3`

Chỉ tọa độ 1 là lõi. Nó nhận hai điểm biên 0 và 2. Điểm 7 là nhiễu.

**Kết quả** · `[0,0,0,-1]`

#### Ví dụ 2

`x = [0,2,4,6,20]  eps = 2  min_samples = 3`

Các lõi 2 và 4 nối nhau. Hai đầu mút 0 và 6 nhận cùng cụm.

**Kết quả** · `[0,0,0,0,-1]`

#### Ví dụ 3

`x = [4,0,4,0,8]  eps = 0  min_samples = 2`

Chỉ các điểm trùng nhau nối được. Nhóm tọa độ 4 nhận nhãn 0 do duyệt chỉ số tăng.

**Kết quả** · `[0,1,0,1,-1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [0,1,2,6,9]  eps = 1  min_samples = 3`  
Kết quả tự nộp ____________________

**E2** · `x = [0,1,2,3,4,10]  eps = 1  min_samples = 3`  
Kết quả tự nộp ____________________

**E3** · `x = [0,0,4,4,9]  eps = 0  min_samples = 2`  
Kết quả tự nộp ____________________

**E4** · `x = [4,5,0,1,9]  eps = 1  min_samples = 2`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `dbscan_1d(x, eps, min_samples)`. Nhận vectơ 1D hữu hạn, eps hữu hạn không âm, min_samples nguyên dương. Duyệt core theo chỉ số tăng. Với mỗi core chưa nhãn, mở rộng qua các core kề, gán lân cận chưa nhãn vào cụm hiện tại. Nhãn cụm bắt đầu từ 0, nhiễu −1. Trả vectơ nhãn và báo ValueError nếu miền sai. [Tệp điền mã](../thuc-hanh/MLP04.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [8,1,2,3,11]  eps = 1  min_samples = 3`  
Kết quả tự nộp ____________________

**R2** · `x = [13,2,3,4,5,6]  eps = 1  min_samples = 3`  
Kết quả tự nộp ____________________

**R3** · `x = [2,2,11,6,6]  eps = 0  min_samples = 2`  
Kết quả tự nộp ____________________

**R4** · `x = [12,5,6,1,2]  eps = 1  min_samples = 2`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Mở rộng sang khoảng cách Euclid hai chiều. Với X = [[0,0],[0,1],[1,1],[5,5]], eps = 1 và min_samples = 3, nộp nhãn và chỉ ra điểm lõi.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP04](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp04)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[0,0,0,1,1,1,-1]`

**D1** · `[0,0,0,1,1,1,-1]`

**D2** · `[0,0,0,1,1,1,-1]`

**D3** · `[-1,-1,-1,-1,-1]`

**E1** · `[0,0,0,-1,-1]`

**E2** · `[0,0,0,0,0,-1]`

**E3** · `[0,0,1,1,-1]`

**E4** · `[0,0,1,1,-1]`

**R1** · `[-1,0,0,0,-1]`

**R2** · `[-1,0,0,0,0,0]`

**R3** · `[0,0,-1,1,1]`

**R4** · `[-1,0,0,1,1]`

**S** · `[0,0,0,0,-1]`

Các điểm 0,5 và 4,5 là lõi. Mỗi lõi nhận hai điểm biên, tạo hai cụm. Điểm 8 nằm ngoài cả hai cụm.

Hãy tiếp tục thăm tất cả lõi nối được. Chỉ đếm điểm lõi sẽ bỏ sót nhãn của điểm biên và của cả chuỗi lõi.

**Vận dụng.** Nhãn [0,0,0,−1]. Điểm [0,1] có đủ ba thành viên trong lân cận, hai điểm còn lại của cụm là điểm biên.

```python
import numpy as np

def dbscan_1d(x, eps, min_samples):
    from collections import deque
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or not np.isfinite(x).all() or not np.isfinite(eps) or eps < 0 or not isinstance(min_samples, (int, np.integer)) or min_samples < 1:
        raise ValueError("Đầu vào không hợp lệ")
    adj = np.abs(x[:, None] - x[None, :]) <= eps
    core = adj.sum(axis=1) >= min_samples
    labels = np.full(len(x), -1)
    cluster = 0
    for i in np.flatnonzero(core):
        if labels[i] >= 0:
            continue
        labels[i] = cluster
        queue = deque([i])
        while queue:
            current = queue.popleft()
            new = np.flatnonzero(adj[current] & (labels == -1))
            labels[new] = cluster
            queue.extend(new[core[new]])
        cluster += 1
    return labels
```
