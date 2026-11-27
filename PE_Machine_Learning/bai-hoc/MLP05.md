<a id="mlp05"></a>

# MLP05 · Tính tổn thất bản lề và mục tiêu SVM

[Về mục lục](../README.md)

Với máy vectơ hỗ trợ (support vector machine, SVM), lấy nhãn −1 hoặc +1. Tổn thất bản lề (hinge loss) của một mẫu là max(0,1 − y·(Xw + b)). Nộp [vectơ tổn thất, 0,5 nhân bình phương độ dài w cộng C nhân tổng tổn thất].

Tiên quyết · ML19

### A · Dự đoán

1. Mẫu nào có biên y·(Xw+b) nhỏ hơn 1? Mẫu ở đúng biên cho tổn thất nào?
2. Ghi ba tổn thất bản lề rồi nộp giá trị mục tiêu. Tính phần phạt riêng với phần tổn thất.

### B · Chạy mẫu

```python
import numpy as np

def svm_objective(X, y, w, b, C):
    X, y, w = (np.asarray(v, dtype=float) for v in (X, y, w))
    hinge = np.maximum(0, 1 - y * (X @ w + b))
    return (hinge, float(0.5 * (w @ w) + C * hinge.sum()))

X = [[-2], [0], [2]]
y = [-1, 1, 1]
w = [1]
b = 0
C = 1
print(svm_objective(X, y, w, b, C))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Nếu nhân đôi số bản sao của mọi mẫu, phần nào trong hàm mục tiêu tăng gấp đôi?
2. Đổi riêng C trong phép tính đã có. Đại lượng nào trong hai đầu ra chắc chắn giữ nguyên?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay C rồi giải lại đề lõi.  
**D1** · `X = [[-2],[0],[2]]  y = [-1,1,1]  w = [1]  b = 0  C = 2`

Thay w rồi giải lại đề lõi.  
**D2** · `X = [[-2],[0],[2]]  y = [-1,1,1]  w = [0.5]  b = 0  C = 1`

Thay b rồi giải lại đề lõi.  
**D3** · `X = [[-2],[0],[2]]  y = [-1,1,1]  w = [1]  b = 1  C = 1`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`X = [[-1],[2]]  y = [-1,1]  w = [0]  b = 0  C = 2`

Hai điểm số bằng 0 nên mỗi tổn thất bằng 1. Phần phạt bằng 0.

**Kết quả** · `[[1,1],4]`

#### Ví dụ 2

`X = [[-2],[1]]  y = [-1,1]  w = [1]  b = 1  C = 3`

Hai biên là 1 và 2. Tổn thất bản lề bằng 0 nên mục tiêu chỉ còn 0,5.

**Kết quả** · `[[0,0],0.5]`

#### Ví dụ 3

`X = [[0],[2]]  y = [1,-1]  w = [1]  b = 0  C = 1`

Biên [0,−2] cho tổn thất [1,3]. Cộng phần phạt 0,5 vào tổng.

**Kết quả** · `[[1,3],4.5]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[-2],[1]]  y = [-1,1]  w = [1]  b = 0  C = 2`  
Kết quả tự nộp ____________________

**E2** · `X = [[-1],[0],[2]]  y = [-1,1,1]  w = [1]  b = -1  C = 2`  
Kết quả tự nộp ____________________

**E3** · `X = [[0],[2]]  y = [1,-1]  w = [0]  b = 1  C = 1`  
Kết quả tự nộp ____________________

**E4** · `X = [[-3],[1]]  y = [-1,1]  w = [0.5]  b = 0  C = 3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `svm_objective(X, y, w, b, C)`. Với ma trận n×d, n,d dương, y thuộc {−1,1}, vectơ w đúng d, C hữu hạn dương, trả (hinge từng mẫu, 0.5·||w||²+C·tổng hinge). Báo ValueError nếu kích thước, nhãn hoặc C sai. [Tệp điền mã](../thuc-hanh/MLP05.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[-3],[2]]  y = [-1,1]  w = [2]  b = 0  C = 1`  
Kết quả tự nộp ____________________

**R2** · `X = [[-2],[0],[1]]  y = [-1,1,1]  w = [1]  b = -1  C = 3`  
Kết quả tự nộp ____________________

**R3** · `X = [[1],[3]]  y = [-1,1]  w = [0]  b = -1  C = 2`  
Kết quả tự nộp ____________________

**R4** · `X = [[-2],[1]]  y = [-1,1]  w = [0.5]  b = 0  C = 2`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

So bộ phân loại tuyến tính với SVM dùng nhân đa thức bậc hai trên bốn điểm (±1,±1), nhãn dương khi tích hai tọa độ dương. Thử SVC(C=10,kernel='poly',degree=2,gamma=1,coef0=1).

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP05](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp05)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[[0,1,0],1.5]`

**D1** · `[[0,1,0],2.5]`

**D2** · `[[0,1,0],1.125]`

**D3** · `[[0,0,0],0.5]`

**E1** · `[[0,0],0.5]`

**E2** · `[[0,2,0],4.5]`

**E3** · `[[0,2],2]`

**E4** · `[[0,0.5],1.625]`

**R1** · `[[0,0],2]`

**R2** · `[[0,2,1],9.5]`

**R3** · `[[0,2],4]`

**R4** · `[[0,0.5],1.125]`

**S** · `[[0,2,0],4.5]`

Các biên của mẫu là 2, 0 và 2. Chỉ điểm giữa chịu tổn thất 1. Phần phạt trọng số bằng 0,5 nên mục tiêu bằng 1,5.

Kiểm tra dấu của nhãn trước khi lấy max. Phần tổn thất dùng tổng trên mọi mẫu, còn phần phạt chỉ tính một lần.

**Vận dụng.** Nhân đa thức phân đúng 4/4 ở dữ liệu này. Một đường thẳng không thể phân đúng cả bốn nhãn xen kẽ.

```python
import numpy as np

def svm_objective(X, y, w, b, C):
    X, y, w = (np.asarray(v, dtype=float) for v in (X, y, w))
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),) or w.shape != (X.shape[1],) or not np.isin(y, [-1,1]).all() or not np.isfinite(C) or C <= 0:
        raise ValueError("Đầu vào không hợp lệ")
    hinge = np.maximum(0, 1 - y * (X @ w + b))
    return hinge, float(0.5 * (w @ w) + C * hinge.sum())
```
