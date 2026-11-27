<a id="mlp07"></a>

# MLP07 · Cập nhật một bước của bản đồ tự tổ chức

[Về mục lục](../README.md)

Trong bản đồ tự tổ chức (self-organizing map, SOM), chọn nút có vectơ trọng số gần x nhất theo Euclid, hòa lấy chỉ số nhỏ. Cập nhật nút thắng và mọi nút có khoảng cách chỉ số đến nó không quá radius bằng W + lr·(x − W). Nộp [chỉ số nút thắng, ma trận trọng số mới].

Tiên quyết · ML23

### A · Dự đoán

1. Nút nào gần 5 nhất? Với radius = 1, những nút nào sẽ đổi trọng số?
2. Ghi chỉ số thắng và tất cả các hàng trọng số sau cập nhật. Hàng nào giữ nguyên?

### B · Chạy mẫu

```python
import numpy as np

def som_step(weights, x, lr, radius):
    weights, x = (np.asarray(weights, dtype=float), np.asarray(x, dtype=float))
    winner = int(np.argmin(np.sum((weights - x) ** 2, axis=1)))
    mask = np.abs(np.arange(len(weights)) - winner) <= radius
    result = weights.copy()
    result[mask] += lr * (x - result[mask])
    return (winner, result)

weights = [[0], [4], [8], [12]]
x = [5]
lr = 0.5
radius = 1
print(som_step(weights, x, lr, radius))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Hai loại khoảng cách dùng để chọn nút thắng và chọn hàng xóm được tính trên những dữ liệu nào?
2. Lấy một nút kề nút thắng và tự tính quãng dịch chuyển của nó. Kiểm tra dấu của x − W.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay x rồi giải lại đề lõi.  
**D1** · `weights = [[0],[4],[8],[12]]  x = [8]  lr = 0.5  radius = 1`

Thay lr rồi giải lại đề lõi.  
**D2** · `weights = [[0],[4],[8],[12]]  x = [5]  lr = 0.25  radius = 1`

Thay radius rồi giải lại đề lõi.  
**D3** · `weights = [[0],[4],[8],[12]]  x = [5]  lr = 0.5  radius = 0`

### Ba ví dụ có lời giải

Dùng cùng đề lõi. Hãy thử tính trước rồi đối chiếu từng ví dụ.

#### Ví dụ 1

`weights = [[0],[3],[7]]  x = [4]  lr = 0.5  radius = 1`

Nút 1 thắng. Cả ba nút trong bán kính 1, dịch nửa quãng đường về 4.

**Kết quả** · `[1,[[2],[3.5],[5.5]]]`

#### Ví dụ 2

`weights = [[0],[4],[8]]  x = [2]  lr = 1  radius = 0`

Hai nút đầu cách đều, chọn nút 0. Chỉ nút đó cập nhật tới 2.

**Kết quả** · `[0,[[2],[4],[8]]]`

#### Ví dụ 3

`weights = [[1],[5],[10],[20]]  x = [9]  lr = 0.25  radius = 1`

Nút 2 thắng. Chỉ các nút 1, 2, 3 dịch một phần tư quãng đường về 9.

**Kết quả** · `[2,[[1],[6],[9.75],[17.25]]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `weights = [[1],[5],[9]]  x = [6]  lr = 0.5  radius = 1`  
Kết quả tự nộp ____________________

**E2** · `weights = [[0],[4],[8]]  x = [2]  lr = 0.5  radius = 1`  
Kết quả tự nộp ____________________

**E3** · `weights = [[-2],[1],[5]]  x = [4]  lr = 1  radius = 0`  
Kết quả tự nộp ____________________

**E4** · `weights = [[1],[4],[7],[10]]  x = [3]  lr = 0.25  radius = 1`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `som_step(weights, x, lr, radius)`. weights là ma trận (số node, số đặc trưng) hữu hạn không rỗng, x là vectơ tương ứng. Các node nằm trên lưới 1D theo chỉ số. Chọn winner bằng Euclid, hòa lấy chỉ số nhỏ. Cập nhật node cách winner ≤ radius nguyên không âm với lr trong [0,1]. Trả (winner, weights mới), báo ValueError nếu miền sai. [Tệp điền mã](../thuc-hanh/MLP07.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `weights = [[2],[6],[10]]  x = [7]  lr = 0.5  radius = 1`  
Kết quả tự nộp ____________________

**R2** · `weights = [[1],[5],[9]]  x = [3]  lr = 0.5  radius = 1`  
Kết quả tự nộp ____________________

**R3** · `weights = [[-3],[0],[4]]  x = [3]  lr = 1  radius = 0`  
Kết quả tự nộp ____________________

**R4** · `weights = [[2],[4],[6],[8]]  x = [5]  lr = 0.25  radius = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Từ trọng số [[0],[4],[8]], dùng hai đầu vào [1,7], radius lần lượt 1 rồi 0 và lr đều bằng 0,5. Chạy hai bước, sau đó đảo thứ tự đầu vào nhưng giữ lịch radius.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP07](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp07)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[1,[[2.5],[4.5],[6.5],[12]]]`

**D1** · `[2,[[0],[6],[8],[10]]]`

**D2** · `[1,[[1.25],[4.25],[7.25],[12]]]`

**D3** · `[1,[[0],[4.5],[8],[12]]]`

**E1** · `[1,[[3.5],[5.5],[7.5]]]`

**E2** · `[0,[[1],[3],[8]]]`

**E3** · `[2,[[-2],[1],[4]]]`

**E4** · `[1,[[1.5],[3.75],[6],[10]]]`

**R1** · `[1,[[4.5],[6.5],[8.5]]]`

**R2** · `[0,[[2],[4],[9]]]`

**R3** · `[2,[[-3],[0],[3]]]`

**R4** · `[1,[[2.75],[4.25],[5.75],[8]]]`

**S** · `[1,[[0],[7.5],[12]]]`

Nút 1 thắng. Ba trọng số đầu dịch nửa quãng đường về 5, trở thành 2,5, 4,5 và 6,5. Nút cuối giữ giá trị 12.

Khi hai nút cách đều x, giữ nút có chỉ số nhỏ hơn. Bán kính lân cận được đo theo vị trí nút trên lưới.

**Vận dụng.** Theo thứ tự ban đầu, trọng số cuối là [[0.5],[2.5],[7.5]]. Khi đảo thứ tự, kết quả là [[0.5],[5.5],[7.5]].

```python
import numpy as np

def som_step(weights, x, lr, radius):
    weights, x = np.asarray(weights, dtype=float), np.asarray(x, dtype=float)
    if weights.ndim != 2 or min(weights.shape) == 0 or x.shape != (weights.shape[1],) or not np.isfinite(weights).all() or not np.isfinite(x).all() or not 0 <= lr <= 1 or not isinstance(radius, (int, np.integer)) or radius < 0:
        raise ValueError("Đầu vào không hợp lệ")
    winner = int(np.argmin(np.sum((weights-x)**2, axis=1)))
    mask = np.abs(np.arange(len(weights)) - winner) <= radius
    result = weights.copy()
    result[mask] += lr * (x - result[mask])
    return winner, result
```
