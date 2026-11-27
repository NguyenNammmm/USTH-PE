<a id="mlp06"></a>

# MLP06 · Dựng lại dữ liệu bằng SVD

[Về mục lục](../README.md)

Dùng phân rã giá trị kỳ dị (singular value decomposition, SVD) cho X sau khi trừ trung bình cột. Giữ k thành phần đầu, nhân lại rồi cộng trung bình từng cột. Nộp [ma trận dựng lại, tổng bình phương sai số dựng lại (SSE)].

Tiên quyết · ML25

### A · Dự đoán

1. Các điểm mẫu có tâm ở đâu? Giữ một thành phần sẽ giữ hướng trải rộng nào?
2. Dự đoán ma trận dựng lại và SSE. Khoanh tọa độ bị thay khi bỏ thành phần thứ hai.

### B · Chạy mẫu

```python
import numpy as np

def svd_reconstruct(X, k):
    X = np.asarray(X, dtype=float)
    mu = X.mean(axis=0)
    U, sigma, Vt = np.linalg.svd(X - mu, full_matrices=False)
    reconstructed = U[:, :k] * sigma[:k] @ Vt[:k] + mu
    return (reconstructed, float(np.sum((X - reconstructed) ** 2)))

X = [[1, 2], [5, 2], [3, 1], [3, 3]]
k = 1
print(svd_reconstruct(X, k))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Nếu k = 0, mỗi hàng được dựng lại bằng gì? Hãy giải thích từ bước cộng trung bình.
2. Chọn một hàng lệch khỏi trục ngang rồi tính phần đóng góp của hàng ấy vào SSE.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay k rồi giải lại đề lõi.  
**D1** · `X = [[1,2],[5,2],[3,1],[3,3]]  k = 0`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [[2,2],[4,2],[3,0],[3,4]]  k = 1`

Thay k rồi giải lại đề lõi.  
**D3** · `X = [[1,2],[5,2],[3,1],[3,3]]  k = 2`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`X = [[0,0],[4,0],[2,-1],[2,1]]  k = 1`

Tâm [2,0]. Giữ trục ngang, bỏ hai tung độ ±1 nên SSE bằng 2.

**Kết quả** · `[[[0,0],[4,0],[2,0],[2,0]],2]`

#### Ví dụ 2

`X = [[2,4],[6,8]]  k = 0`

Hai hàng cùng trả trung bình [4,6]. Mỗi hàng góp 8 vào SSE.

**Kết quả** · `[[[4,6],[4,6]],16]`

#### Ví dụ 3

`X = [[1,2],[3,2],[5,2]]  k = 1`

Mọi điểm sau trừ trung bình nằm trên trục ngang. Một thành phần giữ toàn bộ dữ liệu.

**Kết quả** · `[[[1,2],[3,2],[5,2]],0]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[-3,0],[3,0],[0,-1],[0,1]]  k = 1`  
Kết quả tự nộp ____________________

**E2** · `X = [[2,-2],[6,-2],[4,-3],[4,-1]]  k = 1`  
Kết quả tự nộp ____________________

**E3** · `X = [[1,3],[3,7]]  k = 0`  
Kết quả tự nộp ____________________

**E4** · `X = [[1,1],[3,3],[5,5]]  k = 1`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `svd_reconstruct(X, k)`. Nhận ma trận 2D hữu hạn có n,d dương, k nguyên trong [0,min(n,d)]. Trả (ma trận dựng lại hạng k sau khi trừ tâm và cộng lại trung bình, SSE). Với k=0, dựng lại từng hàng bằng mean. Báo ValueError nếu miền sai. [Tệp điền mã](../thuc-hanh/MLP06.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[-4,0],[4,0],[0,-1],[0,1]]  k = 1`  
Kết quả tự nộp ____________________

**R2** · `X = [[-3,4],[-1,4],[-2,1],[-2,7]]  k = 1`  
Kết quả tự nộp ____________________

**R3** · `X = [[0,2],[4,8]]  k = 0`  
Kết quả tự nộp ____________________

**R4** · `X = [[-1,3],[1,1],[3,-1]]  k = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Với các giá trị kỳ dị [4,2,1], chọn k nhỏ nhất giữ ít nhất 90% tổng bình phương các giá trị kỳ dị. Trình bày tỷ lệ tích lũy.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP06](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp06)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[[[1,2],[5,2],[3,2],[3,2]],2]`

**D1** · `[[[3,2],[3,2],[3,2],[3,2]],10]`

**D2** · `[[[3,2],[3,2],[3,0],[3,4]],2]`

**D3** · `[[[1,2],[5,2],[3,1],[3,3]],0]`

**E1** · `[[[-3,0],[3,0],[0,0],[0,0]],2]`

**E2** · `[[[2,-2],[6,-2],[4,-2],[4,-2]],2]`

**E3** · `[[[2,5],[2,5]],10]`

**E4** · `[[[1,1],[3,3],[5,5]],0]`

**R1** · `[[[-4,0],[4,0],[0,0],[0,0]],2]`

**R2** · `[[[-2,4],[-2,4],[-2,1],[-2,7]],2]`

**R3** · `[[[2,5],[2,5]],26]`

**R4** · `[[[-1,3],[1,1],[3,-1]],0]`

**S** · `[[[-2,-1],[4,-1],[1,-1],[1,-1]],8]`

Các điểm mẫu có tâm [3,2] và trải rộng hơn theo trục ngang. Sau khi giữ một thành phần, mọi tung độ được dựng lại bằng 2, SSE bằng 2.

Nếu kết quả có trung bình cột bằng 0 dù dữ liệu gốc đã tịnh tiến, hãy kiểm tra bước cộng lại trung bình.

**Vận dụng.** Một thành phần giữ 16/21, hai thành phần giữ 20/21. Chọn k = 2.

```python
import numpy as np

def svd_reconstruct(X, k):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or min(X.shape) == 0 or not np.isfinite(X).all() or not isinstance(k, (int, np.integer)) or not 0 <= k <= min(X.shape):
        raise ValueError("Đầu vào không hợp lệ")
    mu = X.mean(axis=0)
    U, sigma, Vt = np.linalg.svd(X - mu, full_matrices=False)
    reconstructed = (U[:, :k] * sigma[:k]) @ Vt[:k] + mu
    return reconstructed, float(np.sum((X - reconstructed)**2))
```
