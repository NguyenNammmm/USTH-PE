<a id="mlp01"></a>

# MLP01 · Mã hóa một thuộc tính phân loại

[Về mục lục](../README.md)

Mã hóa một-nóng (one-hot encoding) dùng một cột cho mỗi mức học được từ train. Sắp các mức theo thứ tự từ điển. Với mức mới ở values, ghi một hàng toàn 0. Nộp [danh sách mức, ma trận mã hóa] theo thứ tự values.

Tiên quyết · ML03

### A · Dự đoán

1. Cột nào dành cho a? Hàng ứng với c chứa những giá trị nào?
2. Ghi danh sách mức trước rồi ghi ma trận ba hàng, theo đúng thứ tự values.

### B · Chạy mẫu

```python
import numpy as np

def encode_categories(train, values):
    train, values = (np.asarray(train, dtype=str), np.asarray(values, dtype=str))
    levels = np.unique(train)
    return (levels.tolist(), (values[:, None] == levels[None, :]).astype(int))

train = ['b', 'a', 'b']
values = ['a', 'c', 'b']
print(encode_categories(train, values))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#doi-chieu)

### C · Lần theo mã

1. Nếu values bắt đầu bằng một mức chưa thấy, vì sao số cột vẫn giữ nguyên?
2. Nếu values chỉ chứa mức mới, bạn vẫn biết số cột nhờ dữ liệu nào?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay values rồi giải lại đề lõi.  
**D1** · `train = ["b","a","b"]  values = ["b","c"]`

Thay train rồi giải lại đề lõi.  
**D2** · `train = ["c","a","c"]  values = ["a","c","b"]`

Thay values rồi giải lại đề lõi.  
**D3** · `train = ["b","a","b"]  values = ["a","a","b"]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `train = ["x","y","x"]  values = ["y","x"]`  
Kết quả tự nộp ____________________

**E2** · `train = ["z","a","z"]  values = ["k","a","z"]`  
Kết quả tự nộp ____________________

**E3** · `train = ["r"]  values = ["r","m"]`  
Kết quả tự nộp ____________________

**E4** · `train = ["b","a","c"]  values = ["c","a"]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `encode_categories(train, values)`. Nhận hai list chuỗi, train không rỗng. Trả (list mức phân biệt xếp tăng, ma trận one-hot của values). Mức lạ thành hàng 0, values có thể rỗng. Báo ValueError nếu train rỗng hoặc đầu vào sai chiều. [Tệp điền mã](../thuc-hanh/MLP01.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `train = ["m","p","m"]  values = ["p","m"]`  
Kết quả tự nộp ____________________

**R2** · `train = ["j","c","j"]  values = ["x","j","c"]`  
Kết quả tự nộp ____________________

**R3** · `train = ["k"]  values = ["t","k"]`  
Kết quả tự nộp ____________________

**R4** · `train = ["y","w","x"]  values = ["x","y"]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Ghép thêm một cột số có giá trị thiếu trước bước một-nóng. Dùng trung vị tập huấn luyện [2,4,6], mức huấn luyện ['b','a','b'], cột số mới [NaN,8] và mức mới ['c','a'].

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của MLP01](../docs/PRIMM/Machine-Learning-PE-PRIMM.md#kiem-lai-mlp01)

<a id="doi-chieu"></a>

### Đối chiếu sau khi đã nộp

**B** · `[["a","b"],[[1,0],[0,0],[0,1]]]`

**D1** · `[["a","b"],[[0,1],[0,0]]]`

**D2** · `[["a","c"],[[1,0],[0,1],[0,0]]]`

**D3** · `[["a","b"],[[1,0],[1,0],[0,1]]]`

**E1** · `[["x","y"],[[0,1],[1,0]]]`

**E2** · `[["a","z"],[[0,0],[1,0],[0,1]]]`

**E3** · `[["r"],[[1],[0]]]`

**E4** · `[["a","b","c"],[[0,0,1],[1,0,0]]]`

**R1** · `[["m","p"],[[0,1],[1,0]]]`

**R2** · `[["c","j"],[[0,0],[0,1],[1,0]]]`

**R3** · `[["k"],[[0],[1]]]`

**R4** · `[["w","x","y"],[[0,1,0],[0,0,1]]]`

**S** · `[["a","t"],[[0,0],[0,1],[1,0]]]`

Train chứa a và b, nên hai cột lần lượt là a, b. Ba hàng cho a, c, b là [1,0], [0,0], [0,1].

Nếu mức lạ sinh thêm một cột, hãy dựng danh sách mức chỉ từ train. Kiểm tra thứ tự từ điển trước khi gán cột.

**Vận dụng.** Trung vị là 4, cột danh mục lần lượt là a, b. Hai hàng ghép là [[4,0,0],[8,1,0]].

```python
import numpy as np

def encode_categories(train, values):
    train, values = np.asarray(train, dtype=str), np.asarray(values, dtype=str)
    if train.ndim != 1 or not train.size or values.ndim != 1:
        raise ValueError("Đầu vào không hợp lệ")
    levels = np.unique(train)
    return levels.tolist(), (values[:, None] == levels[None, :]).astype(int)
```
