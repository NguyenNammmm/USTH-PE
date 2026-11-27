<a id="mlp08"></a>

# MLP08 · Đo độ tách cụm bằng Davies–Bouldin

[Về mục lục](../README.md)

Chỉ số Davies–Bouldin (Davies–Bouldin index, DB) dùng độ phân tán từng cụm là khoảng cách tuyệt đối trung bình đến tâm. Với mỗi cụm i, tính tỷ số (Sᵢ + Sⱼ)/khoảng cách hai tâm cho mọi j khác i, giữ tỷ số lớn nhất. Nộp trung bình của các giá trị lớn nhất ấy. Dùng ít nhất hai cụm có tâm phân biệt.

Tiên quyết · ML24

### A · Dự đoán

1. Ba tâm của bộ mẫu nằm ở đâu? Với cụm cuối, cụm nào cho tỷ số lớn nhất?
2. Ghi tỷ số lớn nhất cho mỗi trong ba cụm rồi nộp trung bình của ba số đó.

### B · Chạy mẫu

```python
import numpy as np

def davies_bouldin_1d(x, labels):
    x, labels = (np.asarray(x, dtype=float), np.asarray(labels))
    levels = np.unique(labels)
    groups = [x[labels == level] for level in levels]
    centers = np.array([g.mean() for g in groups])
    scatter = np.array([np.abs(g - c).mean() for g, c in zip(groups, centers)])
    dist = np.abs(centers[:, None] - centers)
    np.fill_diagonal(dist, np.inf)
    return float(np.max((scatter[:, None] + scatter) / dist, axis=1).mean())

x = [0, 2, 8, 10, 20, 22]
labels = [0, 0, 1, 1, 2, 2]
print(davies_bouldin_1d(x, labels))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Vì sao phải chọn tỷ số lớn nhất riêng cho từng cụm trước khi lấy trung bình?
2. Cụm cuối chọn cụm nào để so? Dùng khoảng cách giữa hai tâm để giải thích.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay x rồi giải lại đề lõi.  
**D1** · `x = [0,4,8,10,16,20]  labels = [0,0,1,1,2,2]`

Thay labels rồi giải lại đề lõi.  
**D2** · `x = [0,2,8,10,20,22]  labels = [2,2,1,1,0,0]`

Thay x rồi giải lại đề lõi.  
**D3** · `x = [-1,1,5,7,10,14]  labels = [0,0,1,1,2,2]`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`x = [0,2,5,7]  labels = [0,0,1,1]`

Hai tâm cách 5. Mỗi độ phân tán bằng 1 nên tỷ số là 2/5.

**Kết quả** · `0.4`

#### Ví dụ 2

`x = [0,2,4,6,12,14]  labels = [0,0,1,1,2,2]`

Ba tâm 1, 5 và 13. Hai cụm đầu chọn nhau cho 1/2, cụm cuối chọn tâm 5 cho 1/4.

**Kết quả** · `0.4166666666667`

#### Ví dụ 3

`x = [3,3,9,11]  labels = [1,1,2,2]`

Hai tâm 3 và 10, độ phân tán 0 và 1. Cả hai cụm dùng tỷ số 1/7.

**Kết quả** · `0.1428571428571`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [0,2,6,8,15,19]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**E2** · `x = [0,2,4,6,20,22]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**E3** · `x = [-4,-2,1,3,9,15]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**E4** · `x = [1,4,7,11]  labels = [0,0,1,1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `davies_bouldin_1d(x, labels)`. Với x 1D hữu hạn, labels nguyên cùng kích thước, có 2..n−1 cụm và mọi tâm phân biệt, trả một giá trị DB dùng khoảng cách tuyệt đối. Độ phân tán là trung bình khoảng cách tới tâm. Báo ValueError khi kích thước, số cụm hoặc tâm sai điều kiện. [Tệp điền mã](../thuc-hanh/MLP08.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [1,3,8,10,19,23]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**R2** · `x = [1,3,5,7,23,25]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**R3** · `x = [-5,-1,2,4,11,17]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

**R4** · `x = [0,4,8,10]  labels = [0,0,1,1]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Chuyển sang thông tin tương hỗ chuẩn hóa (normalized mutual information, NMI) với trung bình số học của hai entropy. So a = [0,0,1,1] với b = [2,2,3,3], rồi với c = [2,3,2,3].

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP08](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp08)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `0.2222222222222`

**D1** · `0.3968253968254`

**D2** · `0.2222222222222`

**D3** · `0.4444444444444`

**E1** · `0.3222222222222`

**E2** · `0.375`

**E3** · `0.4`

**E4** · `0.5384615384615`

**R1** · `0.2738095238095`

**R2** · `0.3703703703704`

**R3** · `0.4545454545455`

**R4** · `0.4285714285714`

**S** · `0.4`

Ba tâm là 1, 9 và 21, độ phân tán đều bằng 1. Các tỷ số lớn nhất là 1/4, 1/4 và 1/6. Điểm DB bằng 2/9.

Nếu chỉ có một tỷ số cho bài ba cụm, hãy lập từng hàng của bảng so sánh. Loại đường chéo rồi lấy giá trị lớn nhất trên từng hàng.

**Vận dụng.** NMI(a,b) bằng 1 vì phân hoạch chỉ đổi tên. NMI(a,c) bằng 0 vì bảng chéo có bốn ô cùng tần số.

```python
import numpy as np

def davies_bouldin_1d(x, labels):
    x, labels = np.asarray(x, dtype=float), np.asarray(labels)
    if x.ndim != 1 or labels.shape != x.shape or labels.dtype.kind not in "iu" or not np.isfinite(x).all():
        raise ValueError("Đầu vào không hợp lệ")
    levels = np.unique(labels)
    if not 2 <= len(levels) < len(x):
        raise ValueError("Cần từ 2 đến n-1 cụm")
    groups = [x[labels == level] for level in levels]
    centers = np.array([g.mean() for g in groups])
    scatter = np.array([np.abs(g-c).mean() for g,c in zip(groups, centers)])
    if len(np.unique(centers)) != len(centers):
        raise ValueError("Tâm cụm phải phân biệt")
    dist = np.abs(centers[:, None] - centers)
    np.fill_diagonal(dist, np.inf)
    return float(np.max((scatter[:, None] + scatter) / dist, axis=1).mean())
```
