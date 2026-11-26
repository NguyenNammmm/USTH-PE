# Machine Learning PE · Thực hành PRIMM

36 bài · 324 hoạt động PRIMM · 603 câu ôn · 151 ca kiểm Make 1

## Cách học

Mỗi bài có năm bước. Đọc mã mẫu và ghi đầu ra dự đoán. Chạy mã rồi so kết quả. Lần theo phép tính ở chỗ còn vướng. Thay từng yếu tố trong mã và chạy lại. Cuối cùng, tự viết hàm và dùng ca kiểm trong đề để đối chiếu.

| Ô | Việc cần làm |
|---|---|
| A · Predict | Ghi đầu ra dự đoán. |
| B · Run | Chạy mã và so kết quả. |
| C · Investigate | Lần theo phép tính. |
| D · Modify | Thử từng thay đổi. |
| E · Make 1 | Tự viết hàm rồi chạy ca kiểm. |
| F · Make 2 | Tự giải với dữ liệu mới. |

[Bài nghiên cứu PRIMM](https://kclpure.kcl.ac.uk/ws/portalfiles/portal/79583213/version_pure_primm_1.pdf) · [Đối chiếu Drive](#doi-chieu)

<a id="muc-luc"></a>

## Mục lục

- [ML01 · Biểu diễn dữ liệu dạng bảng và không gian vector](#ml01) · [Ôn tập](#ml01-on-tap)
- [ML02 · Thống kê mô tả và ma trận hiệp phương sai](#ml02) · [Ôn tập](#ml02-on-tap)
- [ML03 · Chuẩn hóa dữ liệu và tránh data leakage](#ml03) · [Ôn tập](#ml03-on-tap)
- [ML04 · Hồi quy tuyến tính và hàm mất mát bình phương](#ml04) · [Ôn tập](#ml04-on-tap)
- [ML05 · Batch Gradient Descent và bước cập nhật](#ml05) · [Ôn tập](#ml05-on-tap)
- [ML06 · Batch, SGD và mini-batch](#ml06) · [Ôn tập](#ml06-on-tap)
- [ML07 · Hồi quy đa biến và Normal Equations](#ml07) · [Ôn tập](#ml07-on-tap)
- [ML08 · Đặc trưng đa thức và nguy cơ quá khớp](#ml08) · [Ôn tập](#ml08-on-tap)
- [ML09 · Tính sigmoid, xác suất và ranh giới quyết định tuyến tính/phi tuyến](#ml09) · [Ôn tập](#ml09-on-tap)
- [ML10 · Tính cross-entropy và gradient cho hồi quy logistic](#ml10) · [Ôn tập](#ml10-on-tap)
- [ML11 · Dựng gradient, Hessian và một bước Newton đa biến](#ml11) · [Ôn tập](#ml11-on-tap)
- [ML12 · Phân loại bằng k-NN từ khoảng cách và biểu quyết láng giềng](#ml12) · [Ôn tập](#ml12-on-tap)
- [ML13 · Tổ chức train/validation/test và thực hiện K-fold/LOOCV đúng vai trò](#ml13) · [Ôn tập](#ml13-on-tap)
- [ML14 · Tính và diễn giải MAE, MSE, RMSE và R²](#ml14) · [Ôn tập](#ml14-on-tap)
- [ML15 · Tính metric phân loại từ confusion matrix và chọn metric theo chi phí lỗi](#ml15) · [Ôn tập](#ml15-on-tap)
- [ML16 · Giải thích sự thay đổi TPR/FPR theo threshold và ý nghĩa AUC](#ml16) · [Ôn tập](#ml16-on-tap)
- [ML17 · Chẩn đoán underfitting/overfitting qua sai số train và dữ liệu mới](#ml17) · [Ôn tập](#ml17-on-tap)
- [ML18 · Thêm phạt L2, không phạt bias và giải thích hiệu ứng shrinkage](#ml18) · [Ôn tập](#ml18-on-tap)
- [ML19 · Tính net input và thiết kế perceptron cho một cổng logic](#ml19) · [Ôn tập](#ml19-on-tap)
- [ML20 · So sánh sigmoid, tanh, ReLU và vai trò phi tuyến/đạo hàm](#ml20) · [Ôn tập](#ml20-on-tap)
- [ML21 · Tính lan truyền tiến qua tầng ẩn và tầng ra với shape nhất quán](#ml21) · [Ôn tập](#ml21-on-tap)
- [ML22 · Tính delta và gradient trọng số bằng quy tắc chuỗi](#ml22) · [Ôn tập](#ml22-on-tap)
- [ML23 · Thực hiện một vòng Lloyd K-Means và theo dõi SSE nội cụm](#ml23) · [Ôn tập](#ml23-on-tap)
- [ML24 · Đánh giá phân cụm bằng so sánh cặp và phân biệt internal/external validation](#ml24) · [Ôn tập](#ml24-on-tap)
- [ML25 · Thực hiện PCA qua trừ tâm, covariance, eigen decomposition và projection](#ml25) · [Ôn tập](#ml25-on-tap)
- [ML26 · Tính impurity và chọn split cho cây quyết định](#ml26) · [Ôn tập](#ml26-on-tap)
- [ML27 · Giải thích Bagging và Random Forest giảm phương sai bằng bootstrap và feature subsampling](#ml27) · [Ôn tập](#ml27-on-tap)
- [ML28 · Tích hợp pipeline hồi quy và phân loại](#ml28) · [Ôn tập](#ml28-on-tap)
- [MLP01 · Chuẩn bị dữ liệu · Danh mục, dữ liệu thiếu và rời rạc hóa](#mlp01)
- [MLP02 · Chọn đặc trưng · Filter, wrapper và embedded](#mlp02)
- [MLP03 · Phân cụm phân cấp · Single và complete linkage](#mlp03)
- [MLP04 · DBSCAN · Core, border và noise](#mlp04)
- [MLP05 · SVM · Margin, hinge loss và kernel](#mlp05)
- [MLP06 · SVD · Chiếu và dựng lại dữ liệu](#mlp06)
- [MLP07 · Self-Organizing Map · Chọn và cập nhật prototype](#mlp07)
- [MLP08 · Đánh giá phân cụm · Davies–Bouldin và NMI](#mlp08)

<a id="ml01"></a>

## ML01 · Biểu diễn dữ liệu dạng bảng và không gian vector

[Mục lục](#muc-luc) · M1 · Cơ sở toán, dữ liệu và tiền xử lý · Tiên quyết Bài mở đầu

<a id="ml01-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Đặt mỗi mẫu trên một hàng. Ma trận X có shape (n, d), với n mẫu và d đặc trưng.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Viết chính xác shape, hàng thứ hai và cột đầu được in.
2. **P2** · Tính ba tích vô hướng bằng tay và ghi chúng theo thứ tự chương trình.

<a id="ml01-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[2, 7], [4, 9], [6, 3]])
print(X.shape, X[1].tolist(), X[:, 0].tolist())
print((X @ np.array([2, -1])).tolist())
~~~

[Xem kết quả mẫu](#ml01-ket-qua)

<a id="ml01-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Đánh dấu trục mẫu và trục đặc trưng trên X. Giải thích vì sao X[1] và X[:, 0] có độ dài khác nhau.
2. **I2** · Viết shape của X, vector hệ số và kết quả phép @. Chỉ ra cặp kích thước phải khớp.

[Đối chiếu cách giải thích](#ml01-giai-thich)

<a id="ml01-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Thêm hàng [1, 5]. Giữ nguyên vector hệ số và kiểm phần tử cuối bằng −3.
2. **MO2** · Thêm cột hằng 1 ở đầu. In shape (3, 3) và đổi vector hệ số để ba điểm số giữ nguyên.
3. **MO3** · Thay X bằng X.T. Viết phép nhân để nhận hai điểm số từ trọng số [1, 0, -1]. Kiểm kết quả [-4, 4].

<a id="ml01-make"></a>

### E · Make 1 · Viết hàm

**`score_rows(X, w, b)`**

Nhận ma trận số 2D có ít nhất một hàng và một cột, vector w có đúng d phần tử và bias b dạng số. Trả về mảng 1D của Xw + b. Báo ValueError nếu shape không hợp lệ.

Điền hàm. Chạy `python ML01.py`.

[Mã khởi đầu và 4 ca kiểm](#ml01-starter) · [Lời giải](#ml01-loi-giai)

<a id="ml01-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm ghép hai ma trận theo hàng. Với [[1, 2]] và [[3, 4], [5, 6]], trả shape (3, 2). Viết ca kiểm từ chối [[7]] khi ghép với ma trận hai cột.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml01-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml01-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
(3, 2) [4, 9] [2, 4, 6]
[-3, -1, 9]
~~~

</details>

<details class="answer" id="ml01-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

X có shape (3,2). Hàng 1 là [4,9], cột 0 là [2,4,6]. Score lần lượt là −3, −1 và 9. Điều kiện nhân là hai cột của X khớp hai phần tử của w.

</details>

<details class="answer" id="ml01-starter" data-starter="ML01">
<summary>E · Mã khởi đầu và ca kiểm · ML01.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def score_rows(X, w, b):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(score_rows([[2, 1], [-1, 3]], [2, -1], 5), [8, 0])


def case_02():
    same(score_rows([[4]], [0.5], -2), [0])


def case_03():
    rejects(score_rows, [1, 2], [1, 2], 0)


def case_04():
    rejects(score_rows, [[1, 2]], [1], 0)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml01-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def score_rows(X, w, b):
    X, w = np.asarray(X), np.asarray(w)
    if X.ndim != 2 or min(X.shape) == 0 or w.shape != (X.shape[1],):
        raise ValueError("Shape không hợp lệ")
    return X @ w + b
~~~

</details>

<a id="ml01-on-tap"></a>

### Ôn tập ML01

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML01-mcq-1

X = [[40,2],[55,3],[70,4]] có shape nào?

- **A** · (2, 3)
- **B** · (3, 2)
- **C** · (6,)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Hàng là mẫu, cột là thuộc tính.

- **A** · Đảo số mẫu và số thuộc tính.
- **B** · Đúng: ba hàng, hai cột.
- **C** · Đó là dạng flatten, không phải shape ma trận ban đầu.

</details>

##### ML01-mcq-2

Biểu thức nào lấy toàn bộ cột có chỉ số 1 của X?

- **A** · X[1, :]
- **B** · X[:, 1]
- **C** · X[0, 1]

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Dấu : ở chiều hàng giữ toàn bộ mẫu.

- **A** · Chỉ lấy mẫu thứ hai.
- **B** · Đúng: lấy tất cả hàng ở cột 1.
- **C** · Chỉ lấy một giá trị.

</details>

##### ML01-mcq-3

Thêm một cột bias vào X shape (n,d) tạo shape nào?

- **A** · (n+1,d)
- **B** · (n,d+1)
- **C** · (d,n)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Bias là một đặc trưng bổ sung cho từng mẫu.

- **A** · Thêm hàng, không phải cột.
- **B** · Đúng: mỗi mẫu có thêm một giá trị bias.
- **C** · Đảo trục không liên quan.

</details>

##### ML01-mcq-4

Một mẫu có 4 thuộc tính số. Vector của mẫu nằm trong không gian nào?

- **A** · R⁴
- **B** · Rᴺ với N là số mẫu
- **C** · R¹ vì chỉ có một mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Số chiều vector mẫu bằng số thuộc tính d.

- **A** · Mỗi thuộc tính là một tọa độ: có bốn tọa độ.
- **B** · N đếm mẫu, không xác định số chiều của từng mẫu.
- **C** · Một mẫu vẫn có thể có nhiều thuộc tính.

</details>

##### ML01-mcq-5

X có shape (6,2). X[2] biểu diễn gì theo quy ước hàng là mẫu?

- **A** · Đặc trưng thứ ba của mọi mẫu
- **B** · Vector hai thuộc tính của mẫu thứ ba
- **C** · Hai mẫu đầu tiên

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

X[i] lấy vector thuộc tính của mẫu i.

- **A** · Chỉ số đầu tiên chọn hàng; X chỉ có hai cột.
- **B** · Index bắt đầu từ 0, nên hàng 2 là mẫu thứ ba.
- **C** · Chọn một hàng không lấy hai mẫu.

</details>

##### ML01-mcq-6

X có shape (6,2). Muốn giữ cột đầu dưới dạng ma trận (6,1), chọn cách nào?

- **A** · X[:,0]
- **B** · X[0,:]
- **C** · X[:,0:1]

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Giữ một chiều bằng lát cắt khác với chọn một chỉ số.

- **A** · Chỉ số cột đơn làm kết quả thành vector shape (6,).
- **B** · Đây là hàng đầu, shape (2,).
- **C** · Lát cắt cột giữ trục thứ hai, shape (6,1).

</details>

##### ML01-mcq-7

X có 6 mẫu, mỗi mẫu 2 đặc trưng. Các phần tử đang được lưu theo chuyển vị, với shape (2,6). Dùng biểu thức nào để đưa mẫu trở lại trục hàng?

- **A** · X.T
- **B** · X.flatten()
- **C** · Giữ nguyên vì đều có 12 số

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Phải kiểm cả shape lẫn ý nghĩa từng trục.

- **A** · Chuyển vị đổi hai trục thành (6,2).
- **B** · Flatten tạo vector 1D, mất cách tổ chức mẫu và thuộc tính.
- **C** · Cùng số phần tử không có nghĩa cùng semantics.

</details>

##### ML01-mcq-8

Hai cột lần lượt là x₁ và x₂. Đổi thứ tự hai cột mà giữ tên cũ gây ra lỗi gì?

- **A** · Số mẫu tự tăng
- **B** · Giá trị được hiểu thành sai thuộc tính
- **C** · Không có vấn đề vì shape không đổi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thứ tự và ý nghĩa đặc trưng là một phần của hợp đồng dữ liệu.

- **A** · Đổi cột không tạo thêm hàng.
- **B** · Giá trị x₁ bị gắn với tên x₂ và ngược lại.
- **C** · Shape chỉ mô tả kích thước, không xác nhận tên cột.

</details>

##### ML01-mcq-9

Muốn ghép cột bias vào ma trận X shape (6,2) bằng np.hstack, cột toàn 1 cần shape nào?

- **A** · (6,)
- **B** · (1,6)
- **C** · (6,1)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Các khối ghép ngang phải cùng số hàng và số chiều.

- **A** · Vector 1D không cùng số chiều với X trong hstack này.
- **B** · Đây là một hàng có sáu cột.
- **C** · Một giá trị bias cho mỗi hàng: sáu hàng, một cột.

</details>

##### ML01-mcq-10

X có shape (0,2) mang thông tin nào dù không có mẫu?

- **A** · Định nghĩa hai cột đặc trưng nhưng không có hàng quan sát
- **B** · Có hai mẫu
- **C** · Không có số chiều

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Dữ liệu rỗng vẫn có thể giữ schema hai cột,khác mảng rỗng 1D.

- **A** · Dữ liệu rỗng vẫn có thể giữ schema hai cột,khác mảng rỗng 1D.
- **B** · Nhầm cột với hàng.
- **C** · Shape vẫn có hai trục.

</details>

#### Tự luận và viết mã

##### ML01-practice-1

Bảng X có 8 mẫu, mỗi mẫu 3 đặc trưng. X có shape nào? Giải thích hai trục.

<details>
<summary>Đáp án và cách kiểm</summary>

(8,3): tám hàng là tám mẫu; ba cột là ba thuộc tính. Mỗi mẫu là vector thuộc R³.

</details>

##### ML01-practice-2

X=[[40,2],[55,3],[70,4]]. Viết code lấy mẫu thứ hai và giải thích kết quả.

<details>
<summary>Đáp án và cách kiểm</summary>

X[1] là [55,3], gồm hai giá trị đặc trưng 55 và 3. Index bắt đầu từ 0.

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
print(X[1].tolist())
```
Kết quả: [55, 3]

</details>

##### ML01-practice-3

Cho X=[[40,2],[55,3],[70,4]]. Lấy toàn bộ cột đầu. Kết quả có shape nào?

<details>
<summary>Đáp án và cách kiểm</summary>

X[:,0] trả vector [40,55,70], shape (3,).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
a=X[:,0]
print(a.tolist())
print(a.shape)
```
Kết quả: [40, 55, 70]
(3,)

</details>

##### ML01-practice-4

So sánh shape của X[:,0] và X[:,0:1] khi X có ba hàng, hai cột.

<details>
<summary>Đáp án và cách kiểm</summary>

Chọn chỉ số cột tạo (3,); lát cắt cột giữ ma trận (3,1).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
print(X[:,0].shape)
print(X[:,0:1].shape)
```
Kết quả: (3,)
(3, 1)

</details>

##### ML01-practice-5

Ghép cột toàn 1 ở bên trái X=[[40,2],[55,3]]. In ma trận và shape mới.

<details>
<summary>Đáp án và cách kiểm</summary>

Cột bias có một số 1 cho mỗi mẫu; ma trận mới có shape (2,3).

```python
import numpy as np
X=np.array([[40,2],[55,3]])
B=np.column_stack([np.ones(len(X),dtype=int),X])
print(B.tolist())
print(B.shape)
```
Kết quả: [[1, 40, 2], [1, 55, 3]]
(2, 3)

</details>

##### ML01-practice-6

Tính khoảng cách Euclid giữa hai mẫu (30,6) và (25,3). Viết kết quả với bốn chữ số thập phân.

<details>
<summary>Đáp án và cách kiểm</summary>

Khoảng cách sqrt((30−25)²+(6−3)²)=sqrt(34)≈5.8310.

```python
import numpy as np
a=np.array([30.,6.]); b=np.array([25.,3.])
print(f"{np.sqrt(np.sum((a-b)**2)):.4f}")
```
Kết quả: 5.8310

</details>

##### ML01-practice-7

Trong khoảng cách giữa (30,6) và (25,3), tọa độ đầu đóng góp bao nhiêu vào tổng bình phương khoảng cách? Vì sao cần chú ý đơn vị?

<details>
<summary>Đáp án và cách kiểm</summary>

Tọa độ đầu góp 25 trong tổng 34, tức khoảng 73.53%. Đặc trưng có thang đo lớn có thể chi phối khoảng cách; chuẩn hóa được học ở ML03.

</details>

##### ML01-practice-8

Có một mẫu duy nhất gồm hai thuộc tính. So sánh np.array([40,2]) với np.array([[40,2]]).

<details>
<summary>Đáp án và cách kiểm</summary>

Mảng đầu là vector shape (2,); mảng sau là ma trận dữ liệu có một hàng, shape (1,2).

```python
import numpy as np
print(np.array([40,2]).shape)
print(np.array([[40,2]]).shape)
```
Kết quả: (2,)
(1, 2)

</details>

##### ML01-practice-9

Một ma trận có shape (4,3). Sau chuyển vị, số phần tử và shape là gì? Chuyển vị có tạo mẫu quan sát mới không?

<details>
<summary>Đáp án và cách kiểm</summary>

Shape mới (3,4), vẫn 12 phần tử. Chuyển vị đổi cách bố trí trục, không thu thập thêm mẫu quan sát.

```python
import numpy as np
X=np.arange(12).reshape(4,3)
print(X.T.shape)
print(X.T.size)
```
Kết quả: (3, 4)
12

</details>

##### ML01-practice-10

Hai ma trận cùng shape (6,2) có chắc biểu diễn cùng ý nghĩa dữ liệu không? Cho một phản ví dụ.

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Một ma trận có cột x₁, x₂; ma trận kia có cột x₂, x₁. Shape giống nhau nhưng thứ tự và ý nghĩa đặc trưng khác nhau.

</details>

##### ML01-practice-11

Từ X=[[40,2],[55,3],[70,4]], giữ hai mẫu cuối mà vẫn giữ cả hai đặc trưng. Viết code và nêu shape.

<details>
<summary>Đáp án và cách kiểm</summary>

X[1:,:] giữ hàng 1 và 2, shape (2,2).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
Y=X[1:,:]
print(Y.tolist())
print(Y.shape)
```
Kết quả: [[55, 3], [70, 4]]
(2, 2)

</details>

##### ML01-practice-12

Sau khi thêm bias vào X shape (5,2), một bạn báo ma trận mới shape (6,2). Bạn ấy đã nhầm gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Đã tăng số hàng như thêm một mẫu. Bias là thêm một thuộc tính cho từng mẫu nên shape đúng là (5,3), cột bias gồm năm số 1.

</details>

<a id="ml02"></a>

## ML02 · Thống kê mô tả và ma trận hiệp phương sai

[Mục lục](#muc-luc) · M1 · Cơ sở toán, dữ liệu và tiền xử lý · Tiên quyết [ML01](#ml01)

<a id="ml02-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tính trung bình từng cột rồi trừ trung bình khỏi mỗi hàng để được C. Dùng C.T @ C / (n−1) để tính ma trận hiệp phương sai mẫu.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính vector trung bình và ba hàng sau khi trừ tâm.
2. **P2** · Dự đoán phương sai mẫu hai cột và hiệp phương sai. Hai đặc trưng biến thiên cùng hay ngược chiều?

<a id="ml02-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[1., 2.], [3., 6.], [5., 10.]])
mu = X.mean(axis=0)
C = X - mu
print(mu.tolist())
print((C.T @ C / (len(X) - 1)).tolist())
~~~

[Xem kết quả mẫu](#ml02-ket-qua)

<a id="ml02-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Theo dõi shape của C.T, C và C.T @ C. Xác định phần tử đường chéo.
2. **I2** · So sánh tổng tích chéo với kết quả sau khi chia. Phân biệt quy ước mẫu n−1 và quy ước tổng thể n.

[Đối chiếu cách giải thích](#ml02-giai-thich)

<a id="ml02-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi dấu cột thứ hai. Kiểm đường chéo không đổi và hiệp phương sai bằng −8.
2. **MO2** · Cộng [10, -3] cho mọi hàng. Kiểm trung bình dịch tương ứng và covariance giữ nguyên.
3. **MO3** · Thêm cột hằng 7. Kiểm hàng và cột cuối của covariance đều bằng 0.

<a id="ml02-make"></a>

### E · Make 1 · Viết hàm

**`sample_cov(X)`**

Nhận ma trận số với n ≥ 2 và d ≥ 1. Tính covariance mẫu, trả ma trận (d, d). Báo ValueError khi đầu vào sai shape.

Điền hàm. Chạy `python ML02.py`.

[Mã khởi đầu và 4 ca kiểm](#ml02-starter) · [Lời giải](#ml02-loi-giai)

<a id="ml02-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm đổi covariance thành correlation bằng độ lệch chuẩn trên đường chéo. Với [[4, -2], [-2, 1]] thu [[1, -1], [-1, 1]]. Báo lỗi nếu phương sai bằng 0.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml02-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml02-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[3.0, 6.0]
[[4.0, 8.0], [8.0, 16.0]]
~~~

</details>

<details class="answer" id="ml02-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Mean [3,6], C có các hàng [−2,−4], [0,0], [2,4]. Covariance [[4,8],[8,16]]. Chia cho n cho 2/3 các giá trị theo quy ước mẫu.

</details>

<details class="answer" id="ml02-starter" data-starter="ML02">
<summary>E · Mã khởi đầu và ca kiểm · ML02.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def sample_cov(X):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(sample_cov([[1, 2], [3, 0]]), [[2, -2], [-2, 2]])


def case_02():
    same(sample_cov([[2], [4], [6]]), [[4]])


def case_03():
    same(sample_cov([[2, 1], [2, 3]]), [[0, 0], [0, 2]])


def case_04():
    rejects(sample_cov, [[1, 2]])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml02-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def sample_cov(X):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[0] < 2 or X.shape[1] == 0:
        raise ValueError("Cần ít nhất hai mẫu và một đặc trưng")
    centered = X - X.mean(axis=0)
    return centered.T @ centered / (len(X) - 1)
~~~

</details>

<a id="ml02-on-tap"></a>

### Ôn tập ML02

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML02-mcq-1

Trong C, phần tử đường chéo C[j,j] là gì?

- **A** · trung bình cột j
- **B** · phương sai mẫu của cột j
- **C** · số mẫu n

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Hiệp phương sai của một biến với chính nó là phương sai.

- **A** · Trung bình không phải hiệp phương sai.
- **B** · Đúng.
- **C** · n không phải đại lượng trong đường chéo.

</details>

##### ML02-mcq-2

Vì sao dùng n-1 trong hiệp phương sai mẫu?

- **A** · để đổi đơn vị dữ liệu
- **B** · đó là ước lượng mẫu theo quy ước
- **C** · để mọi covariance nằm trong [-1,1]

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

n-1 là quy ước hiệu chỉnh cho mẫu.

- **A** · Mẫu số không đổi đơn vị.
- **B** · Đúng trong công thức mẫu.
- **C** · Đó là tính chất correlation, không phải covariance.

</details>

##### ML02-mcq-3

Điều nào luôn đúng với ma trận hiệp phương sai?

- **A** · đối xứng và PSD
- **B** · mọi phần tử đều dương
- **C** · định thức luôn bằng 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

C = XcᵀXc/(n-1) nên đối xứng và PSD.

- **A** · Đúng về mặt toán học.
- **B** · Covariance có thể âm.
- **C** · Không có tính chất này.

</details>

##### ML02-mcq-4

X có 5 mẫu và 3 thuộc tính. Ma trận covariance theo thuộc tính có shape nào?

- **A** · (5,5)
- **B** · (3,3)
- **C** · (5,3)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mỗi cặp trong ba thuộc tính cho một phần tử, nên C là 3×3.

- **A** · Đó là kích thước theo mẫu, không theo thuộc tính.
- **B** · Mỗi cặp trong ba thuộc tính cho một phần tử, nên C là 3×3.
- **C** · Đây là shape dữ liệu ban đầu.

</details>

##### ML02-mcq-5

Hai mẫu một chiều là 1 và 3. Phương sai mẫu bằng bao nhiêu?

- **A** · 1
- **B** · 4
- **C** · 2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mean=2, tổng bình phương sai lệch=2; chia n−1=1 được 2.

- **A** · Đây là kết quả chia cho n thay vì n−1.
- **B** · 4 là khoảng cách giữa hai giá trị khi bình phương, không phải tổng quanh mean.
- **C** · Mean=2, tổng bình phương sai lệch=2; chia n−1=1 được 2.

</details>

##### ML02-mcq-6

Với x=[1,2,3], y=[3,2,1], dấu covariance mẫu là gì?

- **A** · Âm
- **B** · Dương
- **C** · Luôn bằng 0 vì mean bằng nhau

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Sai lệch hai biến ngược dấu, tổng tích âm.

- **A** · Sai lệch hai biến ngược dấu, tổng tích âm.
- **B** · Hai cột biến thiên ngược chiều.
- **C** · Mean bằng nhau không quyết định covariance.

</details>

##### ML02-mcq-7

Cộng 100 vào mọi giá trị của một cột có làm thay đổi covariance mẫu không?

- **A** · Có, tăng 100
- **B** · Không, nếu các cột và mẫu còn lại giữ nguyên
- **C** · Covariance luôn thành 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tâm hóa loại bỏ hằng số cộng, nên covariance không đổi.

- **A** · Độ lệch so với mean không tăng 100 vì mean cũng tăng 100.
- **B** · Tâm hóa loại bỏ hằng số cộng, nên covariance không đổi.
- **C** · Dịch chuyển không làm mất biến thiên.

</details>

##### ML02-mcq-8

Một cột có mọi giá trị bằng 7. Phương sai và covariance của nó với cột khác là gì?

- **A** · Phương sai 7 và covariance 7
- **B** · Không xác định dù có ít nhất hai mẫu
- **C** · Đều bằng 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mọi sai lệch của cột hằng bằng 0.

- **A** · Giá trị trung bình không phải phương sai.
- **B** · Công thức covariance vẫn xác định nếu n≥2.
- **C** · Mọi sai lệch của cột hằng bằng 0.

</details>

##### ML02-mcq-9

Sau tâm hóa dữ liệu theo cột, tổng giá trị mỗi cột bằng gì về mặt toán học?

- **A** · 0
- **B** · Số mẫu n
- **C** · Mean ban đầu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tổng (xᵢ−mean)=0; số thực máy có thể có sai số nhỏ.

- **A** · Tổng (xᵢ−mean)=0; số thực máy có thể có sai số nhỏ.
- **B** · Tâm hóa không tạo cột toàn 1.
- **C** · Mean ban đầu đã bị trừ đi.

</details>

##### ML02-mcq-10

Với n=3 mẫu,mẫu số covariance mẫu là gì?

- **A** · 2
- **B** · 3
- **C** · Số đặc trưng bất kỳ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Theo công thức mẫu đang học,dùng n−1.

- **A** · Theo công thức mẫu đang học,dùng n−1.
- **B** · Đó là mẫu số n của quy ước khác.
- **C** · Mẫu số dựa số mẫu.

</details>

#### Tự luận và viết mã

##### ML02-practice-1

Tính mean của từng cột X=[[1,4],[3,8]].

<details>
<summary>Đáp án và cách kiểm</summary>

Hai mean lần lượt là 2 và 6.

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
print(X.mean(axis=0).tolist())
```
Kết quả: [2.0, 6.0]

</details>

##### ML02-practice-2

Tâm hóa X=[[1,4],[3,8]] theo cột.

<details>
<summary>Đáp án và cách kiểm</summary>

Trừ vector mean [2,6] ở mỗi hàng, được [[−1,−2],[1,2]].

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
print((X-X.mean(axis=0)).tolist())
```
Kết quả: [[-1.0, -2.0], [1.0, 2.0]]

</details>

##### ML02-practice-3

Tính phương sai mẫu của [1,3].

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=2; tổng bình phương sai lệch=2; chia 1 được 2.

```python
import numpy as np
x=np.array([1.,3.])
print(float(np.var(x,ddof=1)))
```
Kết quả: 2.0

</details>

##### ML02-practice-4

Tính covariance mẫu của x=[1,3], y=[4,8].

<details>
<summary>Đáp án và cách kiểm</summary>

Sai lệch x=[−1,1], y=[−2,2]; tổng tích=4; chia 1 được 4.

```python
import numpy as np
x=np.array([1.,3.]);y=np.array([4.,8.])
print(float(np.sum((x-x.mean())*(y-y.mean()))/(len(x)-1)))
```
Kết quả: 4.0

</details>

##### ML02-practice-5

Dựng ma trận covariance của X=[[1,4],[3,8]].

<details>
<summary>Đáp án và cách kiểm</summary>

Hai phương sai là 2 và 8; covariance là 4, nên C=[[2,4],[4,8]].

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
Z=X-X.mean(axis=0)
print((Z.T@Z/(len(X)-1)).tolist())
```
Kết quả: [[2.0, 4.0], [4.0, 8.0]]

</details>

##### ML02-practice-6

Tính covariance của x=[1,2,3], y=[3,2,1].

<details>
<summary>Đáp án và cách kiểm</summary>

Mean hai cột đều 2; tổng tích sai lệch=−2, chia 2 được −1.

```python
import numpy as np
print(float(np.cov([1.,2.,3.],[3.,2.,1.],ddof=1)[0,1]))
```
Kết quả: -1.0

</details>

##### ML02-practice-7

Vì sao C đối xứng? Giải thích từ tổng tích sai lệch.

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi tích (xᵢj−mean_j)(xᵢk−mean_k) không đổi khi đổi j,k, nên C_jk=C_kj.

</details>

##### ML02-practice-8

Có thể áp dụng công thức covariance mẫu n−1 cho một mẫu duy nhất không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không theo công thức đang dùng: n−1=0. Cần ít nhất hai mẫu; phải báo giới hạn thay vì coi kết quả là 0.

</details>

##### ML02-practice-9

Cột x=[7,7,7] có phương sai mẫu bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=7, mọi sai lệch bằng 0 nên phương sai bằng 0.

```python
import numpy as np
print(float(np.var([7.,7.,7.],ddof=1)))
```
Kết quả: 0.0

</details>

##### ML02-practice-10

Chứng minh covariance không đổi khi cộng hằng số c vào một cột.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean mới là mean+c; (xᵢ+c)−(mean+c)=xᵢ−mean. Từng tích sai lệch và tổng không đổi.

</details>

##### ML02-practice-11

Nhân một cột với 2 thì phương sai và covariance với cột không đổi khác biến đổi ra sao?

<details>
<summary>Đáp án và cách kiểm</summary>

Sai lệch cột được nhân 2. Phương sai nhân 4; covariance với cột còn lại nhân 2.

</details>

##### ML02-practice-12

C=[[2,−1],[−1,2]] có phần tử âm. Điều đó có tự mâu thuẫn tính PSD không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. PSD nói vᵀCv≥0 với mọi v, không đòi mọi phần tử C không âm. Với v=[1,1], vᵀCv=2.

```python
import numpy as np
C=np.array([[2.,-1.],[-1.,2.]])
v=np.array([1.,1.])
print(float(v@C@v))
```
Kết quả: 2.0

</details>

<a id="ml03"></a>

## ML03 · Chuẩn hóa dữ liệu và tránh data leakage

[Mục lục](#muc-luc) · M1 · Cơ sở toán, dữ liệu và tiền xử lý · Tiên quyết [ML01](#ml01), [ML02](#ml02)

<a id="ml03-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Ước lượng tham số của bộ chuẩn hóa trên tập train. Dùng lại các tham số đó cho validation và test. Giá trị Min–Max của dữ liệu mới có thể nằm ngoài [0, 1].

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính hai hàng train sau biến đổi.
2. **P2** · Tính tay hàng test. Thành phần nào vượt 1 và thành phần nào âm?

<a id="ml03-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
train = np.array([[0., 2.], [4., 6.]])
test = np.array([[5., 0.]])
low = train.min(axis=0)
span = train.max(axis=0) - low
print(((train - low) / span).tolist())
print(((test - low) / span).tolist())
~~~

[Xem kết quả mẫu](#ml03-ket-qua)

<a id="ml03-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Ghi shape của low và span. Mô tả phép broadcasting theo hàng.
2. **I2** · Chỉ ra hai dòng học tham số. Giải thích hệ quả của việc ghép test vào train trước hai dòng này.

[Đối chiếu cách giải thích](#ml03-giai-thich)

<a id="ml03-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi test thành [[2, 4], [8, 10]]. Kiểm hai hàng ra [0.5, 0.5] và [2, 2].
2. **MO2** · Thay cột thứ hai của train bằng hằng 2. Thêm nhánh báo ValueError trước khi chia.
3. **MO3** · Dùng Z-score với std tổng thể cho dữ liệu gốc. Kiểm hàng test bằng [1.5, -2]. So với mean normalization (x−mean)/range và kiểm kết quả [0.75, −1].

<a id="ml03-make"></a>

### E · Make 1 · Viết hàm

**`scale_from_train(train, X)`**

Trả về Min–Max của X theo từng cột từ train. Hai ma trận 2D có cùng số cột dương, train có ít nhất một hàng, X có thể có 0 hàng. Báo ValueError cho cột train hằng hoặc shape sai.

Điền hàm. Chạy `python ML03.py`.

[Mã khởi đầu và 4 ca kiểm](#ml03-starter) · [Lời giải](#ml03-loi-giai)

<a id="ml03-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm điền NaN bằng trung vị học trên train. Train [[1, 6], [3, NaN], [9, 2]] và X [[NaN, NaN], [8, 0]] cho [[3, 4], [8, 0]]. Báo ValueError nếu một cột train thiếu toàn bộ.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml03-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml03-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[[0.0, 0.0], [1.0, 1.0]]
[[1.25, -0.5]]
~~~

</details>

<details class="answer" id="ml03-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Low=[0,2], span=[4,4]. Hai hàng train thành [0,0] và [1,1]. Test thành [1.25,−0.5]. Ghép test trước khi fit làm thống kê chịu tác động của dữ liệu đánh giá.

</details>

<details class="answer" id="ml03-starter" data-starter="ML03">
<summary>E · Mã khởi đầu và ca kiểm · ML03.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def scale_from_train(train, X):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(scale_from_train([[1, 10], [3, 20]], [[0, 25]]), [[-0.5, 1.5]])


def case_02():
    same(scale_from_train([[0], [4]], [[2], [4]]), [[0.5], [1]])


def case_03():
    same(scale_from_train([[0], [4]], np.empty((0, 1))), np.empty((0, 1)))


def case_04():
    rejects(scale_from_train, [[1, 1], [1, 2]], [[2, 3]])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml03-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def scale_from_train(train, X):
    train, X = np.asarray(train, dtype=float), np.asarray(X, dtype=float)
    if train.ndim != 2 or X.ndim != 2 or min(train.shape) == 0 or X.shape[1] != train.shape[1]:
        raise ValueError("Shape không hợp lệ")
    low = train.min(axis=0)
    span = train.max(axis=0) - low
    if np.any(span == 0):
        raise ValueError("Cột train hằng")
    return (X - low) / span
~~~

</details>

<a id="ml03-on-tap"></a>

### Ôn tập ML03

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML03-mcq-1

Tham số Min–Max nên tính từ đâu?

- **A** · toàn bộ train và test
- **B** · chỉ train
- **C** · chỉ test

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Test phải được giữ chưa thấy khi học tham số.

- **A** · Làm rò thông tin test.
- **B** · Đúng; sau đó áp dụng cho dữ liệu khác.
- **C** · Không thể đánh giá khách quan.

</details>

##### ML03-mcq-2

Train mean=50,std=10; test=70. Z-score bằng?

- **A** · 2
- **B** · 0.2
- **C** · 70

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Z-score đo số độ lệch chuẩn so với mean train.

- **A** · Đúng: (70-50)/10.
- **B** · Đảo tử số và mẫu số.
- **C** · Chưa chuẩn hóa.

</details>

##### ML03-mcq-3

Min–Max test có thể ngoài [0,1] khi nào?

- **A** · khi test nằm ngoài khoảng train
- **B** · không bao giờ
- **C** · chỉ khi dùng Z-score

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Không kẹp test tùy tiện vì sẽ làm mất thông tin.

- **A** · Đúng và đó là tín hiệu cần giữ nguyên.
- **B** · Sai nếu dữ liệu mới vượt miền train.
- **C** · Không liên quan.

</details>

##### ML03-mcq-4

Train=[10,20]. Giá trị test=5 được Min–Max bằng bao nhiêu?

- **A** · −0.5
- **B** · 0
- **C** · 0.5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

(5−10)/(20−10)=−0.5.

- **A** · (5−10)/(20−10)=−0.5.
- **B** · Không tự kẹp giá trị test về 0.
- **C** · Sai dấu vì test nằm dưới min train.

</details>

##### ML03-mcq-5

Theo công thức z=(x−mean)/std, dữ liệu train có mean=8, std=2. Giá trị x=8 cho z nào?

- **A** · 1
- **B** · 0
- **C** · 8

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tại mean, tử số bằng 0.

- **A** · 1 ứng với một độ lệch chuẩn phía trên mean.
- **B** · Tại mean, tử số bằng 0.
- **C** · Chưa thực hiện phép biến đổi.

</details>

##### ML03-mcq-6

Vì sao một cột train hằng cần quy định riêng khi dùng Min–Max?

- **A** · Vì có quá nhiều mẫu
- **B** · Vì max luôn âm
- **C** · Vì max−min bằng 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Công thức trực tiếp chia cho 0; bài này quy định báo lỗi.

- **A** · Số mẫu không gây vấn đề này.
- **B** · Cột hằng có thể âm hoặc dương.
- **C** · Công thức trực tiếp chia cho 0; bài này quy định báo lỗi.

</details>

##### ML03-mcq-7

Chuẩn hóa từng cột độc lập nghĩa là gì?

- **A** · Mỗi thuộc tính dùng thống kê của chính cột train đó
- **B** · Mỗi hàng dùng min và max riêng
- **C** · Mọi cột luôn dùng chung một khoảng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mỗi đặc trưng có thang đo và thống kê riêng.

- **A** · Mỗi đặc trưng có thang đo và thống kê riêng.
- **B** · Đây là thao tác theo mẫu, khác mục tiêu scaling từng đặc trưng.
- **C** · Dùng chung một khoảng có thể giữ sự chênh thang đo giữa các cột.

</details>

##### ML03-mcq-8

Theo quy ước mean normalization trong tài liệu, (x−mean)/max có gì khác Min–Max?

- **A** · Hai công thức luôn giống nhau
- **B** · Dùng mean ở tử và max ở mẫu, thay vì min và max−min
- **C** · Chỉ khác tên biến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Đây là hai phép biến đổi khác nhau; phải ghi rõ quy ước đang dùng.

- **A** · Ví dụ train [10,20] cho các kết quả khác nhau.
- **B** · Đây là hai phép biến đổi khác nhau; phải ghi rõ quy ước đang dùng.
- **C** · Thay đại lượng trong công thức làm đổi phép biến đổi.

</details>

##### ML03-mcq-9

Train đã học mean/std; một lô test mới có mean khác. Khi áp dụng mô hình, nên làm gì?

- **A** · Tính lại mean/std từ lô test
- **B** · Ghép train và test rồi tính lại
- **C** · Giữ mean/std train để biến đổi lô test

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Dùng cùng tham số để giữ hợp đồng biến đổi giữa train và dữ liệu mới.

- **A** · Tính lại làm thay hệ tọa độ so với lúc học.
- **B** · Dùng test để học thống kê gây leakage trong đánh giá.
- **C** · Dùng cùng tham số để giữ hợp đồng biến đổi giữa train và dữ liệu mới.

</details>

##### ML03-mcq-10

Train=[10,20],test=[30]. Nếu lấy min/max của riêng test,công thức gặp gì?

- **A** · Khoảng test bằng 0 và còn sai quy trình fit scaler
- **B** · Kết quả đúng bắt buộc là 2
- **C** · Bảo đảm không có leakage

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cần dùng train min=10,max=20 để được 2.

- **A** · Cần dùng train min=10,max=20 để được 2.
- **B** · 2 dùng thống kê train,chứ không từ test một phần tử.
- **C** · Fit trên test không đúng quy trình.

</details>

#### Tự luận và viết mã

##### ML03-practice-1

Min–Max train=[10,20], test=[15,30]. Tính hai kết quả.

<details>
<summary>Đáp án và cách kiểm</summary>

Min=10,max=20; kết quả [0.5,2.0].

```python
import numpy as np
train=np.array([10.,20.]);test=np.array([15.,30.])
print(((test-train.min())/(train.max()-train.min())).tolist())
```
Kết quả: [0.5, 2.0]

</details>

##### ML03-practice-2

Min–Max train=[−10,10], test=[−20,0,20].

<details>
<summary>Đáp án và cách kiểm</summary>

Khoảng bằng 20; kết quả [−0.5,0.5,1.5].

```python
import numpy as np
train=np.array([-10.,10.]);test=np.array([-20.,0.,20.])
print(((test-train.min())/(train.max()-train.min())).tolist())
```
Kết quả: [-0.5, 0.5, 1.5]

</details>

##### ML03-practice-3

Với mean train=50,std train=10, tính Z-score của test=[40,50,70].

<details>
<summary>Đáp án và cách kiểm</summary>

Các kết quả là [−1,0,2].

```python
import numpy as np
print(((np.array([40.,50.,70.])-50)/10).tolist())
```
Kết quả: [-1.0, 0.0, 2.0]

</details>

##### ML03-practice-4

Chuẩn hóa theo cột: train=[[0,10],[10,30]], mẫu mới=[[5,20]].

<details>
<summary>Đáp án và cách kiểm</summary>

Min=[0,10],max=[10,30]; mẫu mới biến đổi thành [[0.5,0.5]].

```python
import numpy as np
T=np.array([[0.,10.],[10.,30.]])
X=np.array([[5.,20.]])
print(((X-T.min(axis=0))/(T.max(axis=0)-T.min(axis=0))).tolist())
```
Kết quả: [[0.5, 0.5]]

</details>

##### ML03-practice-5

Vì sao test vượt max train không chứng minh chương trình Min–Max bị lỗi?

<details>
<summary>Đáp án và cách kiểm</summary>

Thống kê lấy từ train nên test có thể nằm ngoài khoảng đã thấy. Giá trị lớn hơn 1 đúng theo công thức; không tự kẹp trừ khi có quy ước riêng.

</details>

##### ML03-practice-6

Phân tích lỗi: chia dữ liệu sau khi tính min/max trên toàn bộ dữ liệu.

<details>
<summary>Đáp án và cách kiểm</summary>

Thông tin từ test đã tham gia thống kê scaling. Cần chia trước, học thống kê trên train, rồi dùng nguyên thống kê đó cho các phần còn lại.

</details>

##### ML03-practice-7

Theo công thức (x−mean)/max trong tài liệu, train=[10,20] cho kết quả nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=15,max=20; kết quả [−0.25,0.25]. Đây không phải Min–Max.

```python
import numpy as np
x=np.array([10.,20.])
print(((x-x.mean())/x.max()).tolist())
```
Kết quả: [-0.25, 0.25]

</details>

##### ML03-practice-8

So sánh Min–Max và mean normalization của train=[10,20].

<details>
<summary>Đáp án và cách kiểm</summary>

Min–Max cho [0,1]; quy ước (x−mean)/max cho [−0.25,0.25]. Không thay công thức này bằng công thức kia mà không đổi mô tả.

</details>

##### ML03-practice-9

Train=[4,4,4]. Vì sao Min–Max trực tiếp không hợp lệ?

<details>
<summary>Đáp án và cách kiểm</summary>

max=min=4, mẫu số 0. Theo hợp đồng bài tập cần ValueError; thực tế có thể chọn quy tắc xử lý feature hằng khác nhưng phải ghi rõ.

</details>

##### ML03-practice-10

Một cột train có std=0. Công thức Z-score gặp vấn đề gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Chia cho 0. Cần quy định cách xử lý cột hằng; không âm thầm xem NaN hay Inf là dữ liệu chuẩn hóa hợp lệ.

</details>

##### ML03-practice-11

Train có hai thuộc tính, dữ liệu mới có ba thuộc tính. Có nên broadcasting cho chạy rồi dùng kết quả không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Dữ liệu mới phải có cùng số cột, ý nghĩa và thứ tự đặc trưng để dùng thống kê train. Shape không khớp là lỗi hợp đồng cần xử lý.

</details>

##### ML03-practice-12

Kiểm tra tính tái sử dụng thống kê: train=[0,4], hai lô test [2] và [6].

<details>
<summary>Đáp án và cách kiểm</summary>

Dùng cùng min=0,max=4, hai kết quả là [0.5] và [1.5]; không fit lại từng lô test.

```python
import numpy as np
lo,hi=0.,4.
for test in [[2.],[6.]]:
    print(((np.array(test)-lo)/(hi-lo)).tolist())
```
Kết quả: [0.5]
[1.5]

</details>

<a id="ml04"></a>

## ML04 · Hồi quy tuyến tính và hàm mất mát bình phương

[Mục lục](#muc-luc) · M2 · Hồi quy tuyến tính và tối ưu hóa · Tiên quyết [ML01](#ml01)

<a id="ml04-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Dùng ŷ = wx + b để dự đoán. Lấy trung bình bình phương sai số, rồi chia cho 2 để tính J.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán ba giá trị ŷ và ba residual theo quy ước ŷ − y.
2. **P2** · Tính J dưới dạng phân số rồi dự đoán số được in.

<a id="ml04-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([0., 1., 2.])
y = np.array([1., 3., 4.])
prediction = 2 * x + 1
residual = prediction - y
print(prediction.tolist(), residual.tolist())
print(round(np.mean(residual ** 2) / 2, 6))
~~~

[Xem kết quả mẫu](#ml04-ket-qua)

<a id="ml04-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Đánh dấu phép tính xảy ra trên từng mẫu và phép gộp qua mọi mẫu.
2. **I2** · Giải thích vì sao residual trái dấu cho cùng đóng góp vào J. So sánh J với MSE.

[Đối chiếu cách giải thích](#ml04-giai-thich)

<a id="ml04-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi w thành 1. Kiểm J = 1/3, rồi so với J gốc.
2. **MO2** · Đổi b thành 0. Kiểm J = 1/3 và ghi mẫu nào có residual bằng 0.
3. **MO3** · In MAE cạnh J. Với tham số gốc, kiểm MAE = 1/3 và J = 1/6.

<a id="ml04-make"></a>

### E · Make 1 · Viết hàm

**`half_mse(x, y, w, b)`**

Nhận hai vector số cùng độ dài dương. Trả J dạng float theo công thức trên. Báo ValueError nếu shape hoặc số phần tử không hợp lệ.

Điền hàm. Chạy `python ML04.py`.

[Mã khởi đầu và 4 ca kiểm](#ml04-starter) · [Lời giải](#ml04-loi-giai)

<a id="ml04-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm chọn cặp (w, b) từ danh sách ứng viên theo J nhỏ nhất, hòa thì lấy cặp đầu. Với x=[0,1], y=[1,3] và [(0,0),(2,1),(3,1)], trả (2,1).

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml04-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml04-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[1.0, 3.0, 5.0] [0.0, 0.0, 1.0]
0.166667
~~~

</details>

<details class="answer" id="ml04-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

ŷ=[1,3,5], residual=[0,0,1]. J=1/6 và MSE=1/3. Bình phương đưa cả hai dấu về cùng số không âm.

</details>

<details class="answer" id="ml04-starter" data-starter="ML04">
<summary>E · Mã khởi đầu và ca kiểm · ML04.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def half_mse(x, y, w, b):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(half_mse([0, 2], [0, 4], 2, 0), 0)


def case_02():
    same(half_mse([0, 2], [1, 1], 1, 0), 0.5)


def case_03():
    same(half_mse([2], [1], -1, 1), 2)


def case_04():
    rejects(half_mse, [], [], 0, 0)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml04-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def half_mse(x, y, w, b):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or x.size == 0 or x.shape != y.shape:
        raise ValueError("Cần hai vector cùng độ dài dương")
    return float(np.mean((w * x + b - y) ** 2) / 2)
~~~

</details>

<a id="ml04-on-tap"></a>

### Ôn tập ML04

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML04-mcq-1

Với a=.08,b=0,x=[20,40],y=[1.6,3.2], E bằng?

- **A** · 0
- **B** · 0.5
- **C** · 3.2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Hai residual đều bằng 0.

- **A** · Đúng vì dự đoán khớp cả hai điểm.
- **B** · Không phải tổng residual bình phương.
- **C** · Đó là một giá trị y.

</details>

##### ML04-mcq-2

Vì sao có 1/2 trong E?

- **A** · đổi đơn vị
- **B** · triệt tiêu hệ số 2 khi đạo hàm
- **C** · đảm bảo E âm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Đạo hàm của bình phương sinh hệ số 2.

- **A** · Không.
- **B** · Đúng.
- **C** · E vẫn không âm.

</details>

##### ML04-mcq-3

Khi X thiếu hạng, điều gì có thể xảy ra?

- **A** · nhiều theta cùng tối ưu
- **B** · MSE luôn âm
- **C** · mọi dự đoán đều khác nhau

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tham số không nhất thiết duy nhất.

- **A** · Đúng.
- **B** · MSE không âm.
- **C** · Có thể cùng dự đoán.

</details>

##### ML04-mcq-4

Mô hình y_hat=0.08x, x=20, y=2. Residual theo quy ước y_hat−y là?

- **A** · −0.4
- **B** · 0.4
- **C** · 1.6

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

1.6−2=−0.4.

- **A** · 1.6−2=−0.4.
- **B** · Đây là y−y_hat, ngược quy ước.
- **C** · Đây là dự đoán, chưa trừ y.

</details>

##### ML04-mcq-5

Với một mẫu có residual bằng −2, E=Σe²/(2m) bằng bao nhiêu?

- **A** · −2
- **B** · 2
- **C** · 4

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

4/(2×1)=2.

- **A** · Bình phương residual không âm.
- **B** · 4/(2×1)=2.
- **C** · 4 là bình phương residual, chưa chia 2m.

</details>

##### ML04-mcq-6

Nếu mọi residual đều bằng 0, kết luận nào đúng?

- **A** · E âm
- **B** · E không xác định
- **C** · Mô hình khớp các mẫu đang xét và E=0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mọi số hạng bằng 0; không suy ra dự đoán tốt trên dữ liệu mới.

- **A** · Tổng bình phương không âm.
- **B** · Với m>0 công thức xác định.
- **C** · Mọi số hạng bằng 0; không suy ra dự đoán tốt trên dữ liệu mới.

</details>

##### ML04-mcq-7

Đổi dấu tất cả residual có làm thay đổi E không?

- **A** · Không
- **B** · Có, E đổi dấu
- **C** · E luôn tăng gấp đôi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Bình phương loại bỏ dấu của từng residual.

- **A** · Bình phương loại bỏ dấu của từng residual.
- **B** · Hàm mất mát không có dấu residual.
- **C** · Không có hệ số 2 mới nào xuất hiện.

</details>

##### ML04-mcq-8

So với MSE=Σe²/m, hàm E=Σe²/(2m) có giá trị nào trên cùng dữ liệu?

- **A** · Gấp đôi MSE
- **B** · Bằng một nửa MSE
- **C** · Bằng MSE trong mọi trường hợp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

E=MSE/2; hệ số dương không đổi vị trí cực tiểu.

- **A** · Hệ số mẫu số lớn gấp đôi làm giá trị nhỏ đi.
- **B** · E=MSE/2; hệ số dương không đổi vị trí cực tiểu.
- **C** · Chỉ bằng nhau khi cả hai bằng 0.

</details>

##### ML04-mcq-9

Một mô hình có training E=0. Điều nào chưa được chứng minh?

- **A** · Residual train bằng 0
- **B** · Training MSE bằng 0
- **C** · Sai số trên test cũng bằng 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Chưa có bằng chứng về dữ liệu chưa dùng để học.

- **A** · Tổng bình phương bằng 0 buộc mọi residual bằng 0.
- **B** · MSE=2E nên cũng bằng 0.
- **C** · Chưa có bằng chứng về dữ liệu chưa dùng để học.

</details>

##### ML04-mcq-10

Residual [−1,1] có mean=0. Có thể kết luận cost bình phương bằng 0 không?

- **A** · Không,cost theo 2m bằng 0.5
- **B** · Có vì sai số triệt tiêu
- **C** · Không xác định vì có số âm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Phân biệt mean residual với mean squared residual.

- **A** · Phân biệt mean residual với mean squared residual.
- **B** · Bình phương trước khi cộng nên không triệt tiêu.
- **C** · Bình phương số âm hoàn toàn xác định.

</details>

#### Tự luận và viết mã

##### ML04-practice-1

Tính dự đoán và residual cho x=20,y=2,a=0.08,b=0.

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán 1.6; residual y_hat−y=−0.4.

```python
x,y,a,b=20.,2.,.08,0.
print(round(a*x+b,4))
print(round(a*x+b-y,4))
```
Kết quả: 1.6
-0.4

</details>

##### ML04-practice-2

Tính E với residual [1,−1] theo mẫu số 2m.

<details>
<summary>Đáp án và cách kiểm</summary>

Tổng bình phương=2,m=2 nên E=0.5.

```python
import numpy as np
e=np.array([1.,-1.])
print(float(np.sum(e**2)/(2*len(e))))
```
Kết quả: 0.5

</details>

##### ML04-practice-3

x=[20,40],y=[1.6,3.2],a=b=0. Tính E.

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán bằng 0; E=(2.56+10.24)/4=3.2.

```python
import numpy as np
y=np.array([1.6,3.2])
print(round(float(np.sum(y**2)/(2*len(y))),4))
```
Kết quả: 3.2

</details>

##### ML04-practice-4

Với cùng dữ liệu x=[20,40],y=[1.6,3.2], tính E khi a=0.08,b=0.

<details>
<summary>Đáp án và cách kiểm</summary>

Hai dự đoán khớp nhãn; E=0.

```python
import numpy as np
x=np.array([20.,40.]);y=np.array([1.6,3.2])
print(float(np.mean((.08*x-y)**2)/2))
```
Kết quả: 0.0

</details>

##### ML04-practice-5

Mẫu đơn x=1.5,y=2.5,a=1,b=1 có E bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán 2.5 nên residual=0,E=0.

```python
x,y,a,b=1.5,2.5,1.,1.
print((a*x+b-y)**2/2)
```
Kết quả: 0.0

</details>

##### ML04-practice-6

Vì sao đổi quy ước residual không đổi hàm mất mát bình phương nhưng cần nhất quán khi tính đạo hàm?

<details>
<summary>Đáp án và cách kiểm</summary>

e và −e có cùng bình phương. Khi đạo hàm phải tính cả đạo hàm của residual theo tham số; đổi dấu residual mà giữ công thức gradient cũ có thể làm cập nhật sai chiều.

</details>

##### ML04-practice-7

So sánh E của residual [0,2] với [1,1].

<details>
<summary>Đáp án và cách kiểm</summary>

E lần lượt 1 và 0.5. Cùng tổng residual là 2 không có nghĩa cùng tổng bình phương.

```python
import numpy as np
for e in [[0.,2.],[1.,1.]]:
    print(float(np.mean(np.array(e)**2)/2))
```
Kết quả: 1.0
0.5

</details>

##### ML04-practice-8

Lặp đôi toàn bộ tập dữ liệu có làm thay đổi E ở cùng tham số không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Tổng bình phương và số mẫu cùng nhân 2 nên tỷ số không đổi.

</details>

##### ML04-practice-9

Với m=3 và tổng bình phương residual=12, tính E và MSE.

<details>
<summary>Đáp án và cách kiểm</summary>

E=12/6=2; MSE=12/3=4.

```python
m,sse=3,12.
print(sse/(2*m))
print(sse/m)
```
Kết quả: 2.0
4.0

</details>

##### ML04-practice-10

Vì sao phải từ chối dữ liệu rỗng khi tính E theo công thức đang dùng?

<details>
<summary>Đáp án và cách kiểm</summary>

m=0 làm mẫu số bằng 0. Không coi NaN hay giá trị tự gán là một cost hợp lệ.

</details>

##### ML04-practice-11

Hàm cost nhận x có 2 phần tử còn y có 1 phần tử. Vì sao không nên để NumPy tự broadcast?

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi x cần đúng nhãn y tương ứng. Broadcasting có thể chạy nhưng sẽ so cả hai dự đoán với cùng nhãn ngoài ý định, che lỗi dữ liệu.

</details>

##### ML04-practice-12

Hàm cost lồi theo a,b có bảo đảm tham số tối ưu duy nhất không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Tính duy nhất cần ma trận thiết kế [x,1] đủ hạng cột. Nếu mọi x bằng nhau thì nhiều cặp a,b có thể tạo cùng dự đoán.

</details>

<a id="ml05"></a>

## ML05 · Batch Gradient Descent và bước cập nhật

[Mục lục](#muc-luc) · M2 · Hồi quy tuyến tính và tối ưu hóa · Tiên quyết [ML04](#ml04)

<a id="ml05-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tính cả hai gradient từ cùng bộ tham số cũ. Sau đó cập nhật đồng thời w và b.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính error và hai gradient trên cả batch.
2. **P2** · Dự đoán w, b sau cập nhật. Viết dấu của mỗi độ thay đổi.

<a id="ml05-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([0., 2.])
y = np.array([1., 5.])
w, b, lr = 0., 0., 0.1
error = w * x + b - y
dw, db = np.mean(error * x), np.mean(error)
next_w, next_b = w - lr * dw, b - lr * db
print(dw, db)
print(round(next_w, 3), round(next_b, 3))
~~~

[Xem kết quả mẫu](#ml05-ket-qua)

<a id="ml05-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao dw có x còn db không có x.
2. **I2** · Tính J trước và sau bước cập nhật. Đối chiếu với thay đổi tham số vừa dự đoán.

[Đối chiếu cách giải thích](#ml05-giai-thich)

<a id="ml05-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đặt lr=0. Kiểm w và b đều giữ nguyên.
2. **MO2** · Đặt lr=2. Tính lại J và kiểm J tăng từ 6.5 lên 116.5.
3. **MO3** · Chạy 5 bước bằng vòng lặp với lr=0.1. Lưu J sau từng bước và kiểm mỗi giá trị nhỏ hơn giá trị liền trước.

<a id="ml05-make"></a>

### E · Make 1 · Viết hàm

**`gd_step(x, y, w, b, lr)`**

Nhận hai vector số cùng độ dài dương. Với lr hữu hạn không âm, trả tuple (w_mới, b_mới). Báo ValueError nếu shape sai hoặc lr ngoài miền.

Điền hàm. Chạy `python ML05.py`.

[Mã khởi đầu và 4 ca kiểm](#ml05-starter) · [Lời giải](#ml05-loi-giai)

<a id="ml05-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm Batch GD chạy tối đa k bước và dừng khi chuẩn gradient ≤ tol. Với x=[0,2], y=[1,5], khởi tạo (2,1) và tol=0, hàm dừng ngay với 0 bước.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml05-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml05-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
-5.0 -3.0
0.5 0.3
~~~

</details>

<details class="answer" id="ml05-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Residual [−1,−5], gradient (−5,−3), bộ tham số mới (0.5,0.3). J từ 6.5 xuống 3.545. Cả dw và db phải đọc residual cũ.

</details>

<details class="answer" id="ml05-starter" data-starter="ML05">
<summary>E · Mã khởi đầu và ca kiểm · ML05.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def gd_step(x, y, w, b, lr):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(gd_step([1, 3], [2, 4], 0, 0, 0.1), [0.7, 0.3])


def case_02():
    same(gd_step([1, 2], [3, 5], 2, 1, 0.5), [2, 1])


def case_03():
    same(gd_step([1], [2], 3, 4, 0), [3, 4])


def case_04():
    rejects(gd_step, [1], [1], 0, 0, -1)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml05-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def gd_step(x, y, w, b, lr):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or x.size == 0 or x.shape != y.shape or not np.isfinite(lr) or lr < 0:
        raise ValueError("Đầu vào không hợp lệ")
    error = w * x + b - y
    return float(w - lr * np.mean(error * x)), float(b - lr * error.mean())
~~~

</details>

<a id="ml05-on-tap"></a>

### Ôn tập ML05

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML05-mcq-1

Gradient batch dùng bao nhiêu mẫu?

- **A** · mẫu đầu
- **B** · toàn bộ batch
- **C** · không mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

BGD dùng toàn bộ dữ liệu.

- **A** · Đó là SGD.
- **B** · Đúng.
- **C** · Không thể tính gradient.

</details>

##### ML05-mcq-2

Alpha quá lớn có thể?

- **A** · phân kỳ
- **B** · luôn chính xác hơn
- **C** · đổi nhãn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Bước nhảy vượt qua vùng giảm.

- **A** · Đúng.
- **B** · Không.
- **C** · Alpha không đổi nhãn.

</details>

##### ML05-mcq-3

Cập nhật đồng thời nghĩa là?

- **A** · mọi theta dùng gradient cũ
- **B** · theta0 cập nhật rồi mới tính theta1
- **C** · chỉ cập nhật bias

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Vector update dùng cùng gradient.

- **A** · Đúng.
- **B** · Sai thứ tự.
- **C** · Không.

</details>

##### ML05-mcq-4

x=[20,40],y=[1.6,3.2],a=b=0. Gradient d_a bằng bao nhiêu?

- **A** · −80
- **B** · −2.4
- **C** · 80

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

((-1.6)×20+(-3.2)×40)/2=−80.

- **A** · ((-1.6)×20+(-3.2)×40)/2=−80.
- **B** · −2.4 là gradient theo b.
- **C** · Sai dấu vì residual ban đầu âm.

</details>

##### ML05-mcq-5

Với dữ liệu trên và alpha=0.001, b mới bằng bao nhiêu?

- **A** · −0.0024
- **B** · 0.0024
- **C** · 0.08

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

d_b=−2.4 nên b_new=0−0.001×(−2.4).

- **A** · Cập nhật phải trừ gradient âm.
- **B** · d_b=−2.4 nên b_new=0−0.001×(−2.4).
- **C** · 0.08 là a mới, không phải b.

</details>

##### ML05-mcq-6

Cập nhật đồng thời a,b đòi hỏi điều gì?

- **A** · Cập nhật a trước rồi dùng a mới tính d_b
- **B** · Luôn giữ b bằng 0
- **C** · Tính cả hai gradient từ cùng tham số cũ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Hai thành phần gradient thuộc cùng một điểm tham số.

- **A** · Đó là cập nhật nối tiếp, khác một bước Batch GD đã định nghĩa.
- **B** · Bias vẫn phải được cập nhật khi bài có bias.
- **C** · Hai thành phần gradient thuộc cùng một điểm tham số.

</details>

##### ML05-mcq-7

Nếu gradient tại tham số hiện tại bằng vector 0, bước GD hữu hạn sẽ làm gì?

- **A** · Giữ nguyên tham số
- **B** · Tự giảm cost xuống âm
- **C** · Đổi ngẫu nhiên trọng số

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

theta_new=theta−alpha×0=theta.

- **A** · theta_new=theta−alpha×0=theta.
- **B** · Cost bình phương không âm.
- **C** · GD không tự thêm cập nhật ngẫu nhiên trong công thức này.

</details>

##### ML05-mcq-8

Learning rate quá lớn có thể gây điều gì?

- **A** · Luôn hội tụ nhanh hơn
- **B** · Vượt quá vùng cải thiện và có thể phân kỳ
- **C** · Tự biến thành normal equations

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Bước nhảy lớn có thể làm cost tăng; cần theo dõi diễn biến.

- **A** · Không có bảo đảm này.
- **B** · Bước nhảy lớn có thể làm cost tăng; cần theo dõi diễn biến.
- **C** · Đây là hai phương pháp khác nhau.

</details>

##### ML05-mcq-9

Trong Batch GD, gradient của một bước được tính từ đâu?

- **A** · Một mẫu bất kỳ duy nhất
- **B** · Chỉ mẫu có residual lớn nhất
- **C** · Toàn bộ tập train đang dùng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Gradient batch tổng hợp mọi mẫu rồi chia m.

- **A** · Đó gần với SGD chứ không phải batch đầy đủ.
- **B** · Công thức không loại các mẫu residual nhỏ.
- **C** · Gradient batch tổng hợp mọi mẫu rồi chia m.

</details>

##### ML05-mcq-10

Một implementation cập nhật a_new đúng nhưng dùng a_new để tính gradient b. Có còn là bước batch đồng thời đã định nghĩa không?

- **A** · Không
- **B** · Có vì cả hai được cập nhật
- **C** · Có nếu alpha nhỏ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Gradient hai thành phần phải từ cùng tham số cũ.

- **A** · Gradient hai thành phần phải từ cùng tham số cũ.
- **B** · Thứ tự dùng tham số thay đổi điểm tính gradient.
- **C** · Nhỏ không biến hai thuật toán thành giống hệt.

</details>

#### Tự luận và viết mã

##### ML05-practice-1

Tính d_a,d_b cho x=[20,40],y=[1.6,3.2],a=b=0.

<details>
<summary>Đáp án và cách kiểm</summary>

d_a=−80,d_b=−2.4.

```python
import numpy as np
x=np.array([20.,40.]);y=np.array([1.6,3.2]);e=-y
print(round(float(np.mean(e*x)),4))
print(round(float(e.mean()),4))
```
Kết quả: -80.0
-2.4

</details>

##### ML05-practice-2

Từ gradient trên và alpha=0.001, cập nhật đồng thời a,b.

<details>
<summary>Đáp án và cách kiểm</summary>

a_new=0.08,b_new=0.0024.

```python
a,b,da,db,alpha=0.,0.,-80.,-2.4,.001
print(a-alpha*da)
print(b-alpha*db)
```
Kết quả: 0.08
0.0024

</details>

##### ML05-practice-3

Dự đoán sau bước trên có khớp chính xác y=[1.6,3.2] không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Có bias mới 0.0024 nên dự đoán [1.6024,3.2024]. a=0.08 riêng lẻ không chứng minh cả mô hình khớp.

```python
import numpy as np
x=np.array([20.,40.])
print(np.round(.08*x+.0024,4).tolist())
```
Kết quả: [1.6024, 3.2024]

</details>

##### ML05-practice-4

x=[1,2],y=[2,3],a=b=0,alpha=0.1. Tính một bước cập nhật.

<details>
<summary>Đáp án và cách kiểm</summary>

d_a=−4,d_b=−2.5 nên a_new=0.4,b_new=0.25.

```python
import numpy as np
x=np.array([1.,2.]);y=np.array([2.,3.]);e=-y
print(round(float(-.1*np.mean(e*x)),4))
print(round(float(-.1*e.mean()),4))
```
Kết quả: 0.4
0.25

</details>

##### ML05-practice-5

Với x=[1,2],y=[2,3], hãy tính b_new nếu lỡ dùng a_new=0.4 trước khi tính gradient b. So với cập nhật đồng thời.

<details>
<summary>Đáp án và cách kiểm</summary>

Dùng a mới cho residual [−1.6,−2.2], mean=−1.9 nên b_new=0.19, khác đáp án đồng thời 0.25.

```python
import numpy as np
x=np.array([1.,2.]);y=np.array([2.,3.])
print(round(float(-.1*np.mean(.4*x-y)),4))
```
Kết quả: 0.19

</details>

##### ML05-practice-6

Tại a=2,b=0 với x=[1,2],y=[2,4], gradient và cập nhật bằng gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Residual=0 nên cả hai gradient bằng 0, tham số vẫn là a=2,b=0.

</details>

##### ML05-practice-7

Một mẫu x=2,y=5,a=1,b=1,alpha=0.1. Tính cập nhật.

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán=3,residual=−2,d_a=−4,d_b=−2. a_new=1.4,b_new=1.2.

```python
x,y,a,b,alpha=2.,5.,1.,1.,.1
e=a*x+b-y
print(a-alpha*e*x)
print(b-alpha*e)
```
Kết quả: 1.4
1.2

</details>

##### ML05-practice-8

Vì sao thay sum residual bằng mean residual làm bước cập nhật ít phụ thuộc trực tiếp số mẫu hơn?

<details>
<summary>Đáp án và cách kiểm</summary>

Mean chia cho m. Nếu lặp đôi toàn bộ dữ liệu, sum tăng gấp đôi nhưng mean không đổi; gradient của hàm E dùng mẫu số m.

</details>

##### ML05-practice-9

Giữ gradient [−4,−2.5], so sánh độ lớn bước với alpha=0.1 và alpha=0.01.

<details>
<summary>Đáp án và cách kiểm</summary>

Bước lần lượt [0.4,0.25] và [0.04,0.025]. Giảm alpha mười lần làm bước nhỏ mười lần tại cùng gradient.

</details>

##### ML05-practice-10

Một bước làm cost giảm có đủ chứng minh thuật toán đã hội tụ không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Cần theo dõi qua các bước và điều kiện dừng cụ thể; một lần giảm không chứng minh đã tới cực tiểu.

</details>

##### ML05-practice-11

Vì sao không làm tròn tham số sau mỗi bước chỉ để output dễ đọc?

<details>
<summary>Đáp án và cách kiểm</summary>

Làm tròn thay đổi trạng thái thuật toán và có thể làm bước nhỏ biến mất. Giữ độ chính xác tính toán, chỉ định dạng khi hiển thị.

</details>

##### ML05-practice-12

X=[[1,1],[1,2]],theta=[0,0],y=[2,3],alpha=0.1. Tính theta mới và chỉ rõ thứ tự bias/slope.

<details>
<summary>Đáp án và cách kiểm</summary>

Gradient=[−2.5,−4] nên theta_new=[0.25,0.4]. Cột đầu là bias, cột sau là đặc trưng; không đổi chỗ hai hệ số.

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]])
theta=np.zeros(2);y=np.array([2.,3.])
print(np.round(theta-.1*(X.T@(X@theta-y)/len(y)),4).tolist())
```
Kết quả: [0.25, 0.4]

</details>

<a id="ml06"></a>

## ML06 · Batch, SGD và mini-batch

[Mục lục](#muc-luc) · M2 · Hồi quy tuyến tính và tối ưu hóa · Tiên quyết [ML05](#ml05)

<a id="ml06-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** So sánh Batch, SGD và mini-batch theo số mẫu trong mỗi lần cập nhật. Trong bài này, một epoch đi qua mỗi chỉ số đúng một lần.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Ghi từng batch theo thứ tự và dự đoán số mẫu batch cuối.
2. **P2** · Tính ba trung bình gradient. Kiểm xem trung bình không trọng số của chúng có bằng trung bình của cả g.

<a id="ml06-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
order = np.array([3, 1, 4, 0, 2])
g = np.array([2., -1., 4., 3., 7.])
size = 2
for start in range(0, len(order), size):
    batch = order[start:start + size]
    print(batch.tolist(), g[batch].mean())
~~~

[Xem kết quả mẫu](#ml06-ket-qua)

<a id="ml06-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vai trò của order khi X và y có cùng thứ tự hàng.
2. **I2** · Giải thích vì sao gradient trung bình ở đây chỉ minh họa cách gộp. Trong SGD thật, gradient được tính lại sau mỗi lần cập nhật.

[Đối chiếu cách giải thích](#ml06-giai-thich)

<a id="ml06-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi size thành 1. Kiểm 5 lượt và gradient lượt đầu là 3.
2. **MO2** · Đổi size thành 5. Kiểm một lượt có gradient trung bình 3.
3. **MO3** · Dùng numpy.random.default_rng(11).permutation(5) để tạo order. Chạy hai lần với cùng seed rồi kiểm các batch giống nhau.

<a id="ml06-make"></a>

### E · Make 1 · Viết hàm

**`split_batches(order, size)`**

Nhận một list hoán vị các chỉ số 0..n−1 và size là số nguyên dương. Trả list các list liên tiếp, giữ batch cuối. Cho phép order rỗng. Báo ValueError nếu size không dương hoặc order có chỉ số thiếu/trùng.

Điền hàm. Chạy `python ML06.py`.

[Mã khởi đầu và 5 ca kiểm](#ml06-starter) · [Lời giải](#ml06-loi-giai)

<a id="ml06-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm thực hiện một epoch GD theo batch. Với x=[1,2], y=[2,4], lr=0.1 và khởi tạo (0,0), kiểm order [0,1], size=1 cho (0.88,0.54), và size=2 cho (0.5,0.3).

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml06-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml06-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[3, 1] 1.0
[4, 0] 4.5
[2] 4.0
~~~

</details>

<details class="answer" id="ml06-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Các batch [3,1], [4,0], [2] có mean 1, 4.5, 4. Trung bình đơn của ba mean là 19/6. Trung bình trên cả 5 mẫu là 3.

</details>

<details class="answer" id="ml06-starter" data-starter="ML06">
<summary>E · Mã khởi đầu và ca kiểm · ML06.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def split_batches(order, size):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    assert split_batches([2, 0, 1], 2) == [[2, 0], [1]]


def case_02():
    assert split_batches([], 1) == []


def case_03():
    assert split_batches([1, 0], 9) == [[1, 0]]


def case_04():
    rejects(split_batches, [0, 0], 2)


def case_05():
    rejects(split_batches, [0], 0)


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml06-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def split_batches(order, size):
    if not isinstance(size, (int, np.integer)) or size < 1 or sorted(order) != list(range(len(order))):
        raise ValueError("Size hoặc hoán vị không hợp lệ")
    return [order[start:start + size] for start in range(0, len(order), size)]
~~~

</details>

<a id="ml06-on-tap"></a>

### Ôn tập ML06

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML06-mcq-1

Tạo batch bằng permutation và phân biệt BGD, SGD, mini-batch: lựa chọn đúng?

- **A** · Bỏ qua kiểm tra shape
- **B** · Thực hiện đúng công thức và kiểm tra điều kiện
- **C** · Dùng thư viện thay thế thuật toán

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thuật toán cần đúng công thức và hợp đồng dữ liệu.

- **A** · Dễ tạo lỗi im lặng.
- **B** · Đúng.
- **C** · Không phù hợp mục tiêu.

</details>

##### ML06-mcq-2

Trường hợp biên nào cần xử lý?

- **A** · input rỗng hoặc batch không hợp lệ
- **B** · không có trường hợp biên
- **C** · chỉ đổi tên biến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Kiểm tra biên giúp tránh kết quả sai.

- **A** · Đúng.
- **B** · Sai.
- **C** · Không.

</details>

##### ML06-mcq-3

Kết quả đúng phụ thuộc vào?

- **A** · shape và kiểu dữ liệu
- **B** · màu giao diện
- **C** · hard-code đáp án

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Shape và dữ liệu quyết định phép tính.

- **A** · Đúng.
- **B** · Không.
- **C** · Không được.

</details>

##### ML06-mcq-4

Có 10 mẫu, batch_size=4, giữ batch cuối. Một epoch có bao nhiêu batch?

- **A** · 2
- **B** · 3
- **C** · 4

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Các kích thước là 4,4,2.

- **A** · Hai batch chỉ dùng tám mẫu.
- **B** · Các kích thước là 4,4,2.
- **C** · Batch size không phải số batch.

</details>

##### ML06-mcq-5

X và y phải được xáo trộn thế nào để giữ cặp mẫu–nhãn?

- **A** · Dùng cùng một permutation chỉ số
- **B** · Xáo độc lập từng mảng
- **C** · Chỉ xáo y

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cùng chỉ số giữ đúng nhãn của mỗi hàng.

- **A** · Cùng chỉ số giữ đúng nhãn của mỗi hàng.
- **B** · Hai permutation khác nhau có thể gắn nhầm nhãn.
- **C** · Đổi riêng nhãn phá cặp dữ liệu.

</details>

##### ML06-mcq-6

Với 8 mẫu, mini-batch size=1 tương ứng cách lấy gradient nào?

- **A** · Toàn bộ tám mẫu mỗi bước
- **B** · Hai mẫu mỗi bước
- **C** · Một mẫu mỗi bước như SGD

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mỗi bước dùng gradient từ một mẫu.

- **A** · Đó là batch đầy đủ.
- **B** · Batch size đã cho là 1.
- **C** · Mỗi bước dùng gradient từ một mẫu.

</details>

##### ML06-mcq-7

Nếu batch_size bằng số mẫu, mỗi epoch có bao nhiêu lần cập nhật?

- **A** · Một
- **B** · Bằng số mẫu
- **C** · Không có cập nhật

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Toàn tập nằm trong một batch.

- **A** · Toàn tập nằm trong một batch.
- **B** · Nhầm một bước trên mỗi mẫu với batch đầy đủ.
- **C** · Có một batch hợp lệ.

</details>

##### ML06-mcq-8

Cố định random seed có tác dụng gì trong ví dụ tạo permutation?

- **A** · Bảo đảm mô hình tốt hơn
- **B** · Giúp tái lập thứ tự với cùng môi trường và chuỗi lời gọi
- **C** · Bảo đảm mỗi lần gọi generator đang tồn tại đều trả cùng permutation

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Seed giúp lặp lại thí nghiệm khi trạng thái và lời gọi được giữ.

- **A** · Seed không bảo đảm chất lượng mô hình.
- **B** · Seed giúp lặp lại thí nghiệm khi trạng thái và lời gọi được giữ.
- **C** · Generator tiến trạng thái qua các lần gọi.

</details>

##### ML06-mcq-9

Batch cuối có 2 mẫu thay vì 4. Gradient trung bình của batch này nên chia cho số nào?

- **A** · 4 như cấu hình ban đầu
- **B** · Tổng số mẫu toàn khóa
- **C** · 2 là số mẫu thực tế trong batch

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Dùng số mẫu thực tế của batch.

- **A** · Chia 4 làm sai gradient trung bình của batch ngắn.
- **B** · Đó không phải trung bình batch hiện tại.
- **C** · Dùng số mẫu thực tế của batch.

</details>

##### ML06-mcq-10

Có 9 mẫu,batch size 4,nếu bỏ batch cuối thì mỗi epoch dùng bao nhiêu mẫu?

- **A** · 8
- **B** · 9
- **C** · 4

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Quy tắc drop-last làm mất mẫu phần dư trong epoch đó;phải công bố.

- **A** · Quy tắc drop-last làm mất mẫu phần dư trong epoch đó;phải công bố.
- **B** · Đã bỏ một mẫu phần dư.
- **C** · Có hai batch đầy đủ.

</details>

#### Tự luận và viết mã

##### ML06-practice-1

Chia 11 mẫu thành batch size 4, giữ phần dư. Nêu kích thước và số bước mỗi epoch.

<details>
<summary>Đáp án và cách kiểm</summary>

Các batch có 4,4,3 mẫu; có 3 bước cập nhật.

```python
n,b=11,4
print([min(b,n-i) for i in range(0,n,b)])
```
Kết quả: [4, 4, 3]

</details>

##### ML06-practice-2

Có 5 mẫu, batch size 8. Nếu giữ batch cuối thì có dùng được hết dữ liệu không?

<details>
<summary>Đáp án và cách kiểm</summary>

Có. Một batch chứa cả 5 mẫu; batch size là giới hạn chia, không buộc mọi batch đủ 8.

</details>

##### ML06-practice-3

Cho idx=[2,0,1], X=[10,20,30], y=[1,2,3]. Tính X[idx],y[idx].

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả [30,10,20] và [3,1,2]; mỗi nhãn đi cùng mẫu tương ứng.

```python
import numpy as np
idx=np.array([2,0,1]);X=np.array([10,20,30]);y=np.array([1,2,3])
print(X[idx].tolist())
print(y[idx].tolist())
```
Kết quả: [30, 10, 20]
[3, 1, 2]

</details>

##### ML06-practice-4

Giải thích vì sao xáo trộn độc lập X và y có thể khiến loss vẫn tính được nhưng học sai.

<details>
<summary>Đáp án và cách kiểm</summary>

Shape vẫn khớp nên phép toán chạy, nhưng nhãn không còn thuộc đúng mẫu. Tính hợp lệ kích thước không bảo đảm cặp dữ liệu đúng.

</details>

##### ML06-practice-5

Chia idx=[4,1,3,0,2] thành batch size 2, giữ phần dư.

<details>
<summary>Đáp án và cách kiểm</summary>

Các nhóm chỉ số là [4,1],[3,0],[2].

```python
idx=[4,1,3,0,2]
print([idx[i:i+2] for i in range(0,len(idx),2)])
```
Kết quả: [[4, 1], [3, 0], [2]]

</details>

##### ML06-practice-6

Một epoch trên 12 mẫu, batch size lần lượt 12,3,1 có bao nhiêu bước?

<details>
<summary>Đáp án và cách kiểm</summary>

Lần lượt 1,4,12 bước. Không có nghĩa các phương pháp đạt cùng tham số sau một epoch vì tham số cập nhật giữa các batch.

```python
n=12
for b in [12,3,1]:
    print(len(range(0,n,b)))
```
Kết quả: 1
4
12

</details>

##### ML06-practice-7

Tạo hai generator mới cùng seed rồi gọi permutation(6) một lần mỗi generator. Kết quả có giống nhau không?

<details>
<summary>Đáp án và cách kiểm</summary>

Có trong cùng môi trường NumPy và cùng chuỗi lời gọi. Không cần hard-code permutation để kiểm tính tái lập.

```python
import numpy as np
a=np.random.default_rng(7).permutation(6)
b=np.random.default_rng(7).permutation(6)
print(bool(np.array_equal(a,b)))
```
Kết quả: True

</details>

##### ML06-practice-8

Gradient theo từng mẫu của một batch ngắn là [2,6]. Tính gradient trung bình và bước theta mới khi theta=1,alpha=0.1.

<details>
<summary>Đáp án và cách kiểm</summary>

Gradient=4; theta_new=1−0.1×4=0.6.

```python
g=sum([2.,6.])/2
print(g)
print(round(1.-.1*g,4))
```
Kết quả: 4.0
0.6

</details>

##### ML06-practice-9

Vì sao batch_size=0 cần bị từ chối thay vì cố tạo batch?

<details>
<summary>Đáp án và cách kiểm</summary>

Kích thước batch phải là số nguyên dương; bước range bằng 0 không hợp lệ và không định nghĩa được cách tiến qua dữ liệu.

</details>

##### ML06-practice-10

Nêu khác nhau giữa một step và một epoch.

<details>
<summary>Đáp án và cách kiểm</summary>

Step là một lần cập nhật từ batch hiện tại. Epoch là một lượt đi qua tập train theo quy tắc duyệt; có thể gồm nhiều step.

</details>

##### ML06-practice-11

Trong một epoch dùng permutation, cần kiểm bất biến nào để biết không mất hoặc lặp mẫu?

<details>
<summary>Đáp án và cách kiểm</summary>

Ghép tất cả chỉ số batch phải chứa mỗi chỉ số từ 0 đến n−1 đúng một lần nếu không sampling có hoàn lại hoặc bỏ batch cuối.

```python
idx=[4,1,3,0,2];batches=[idx[i:i+2] for i in range(0,len(idx),2)]
flat=[j for batch in batches for j in batch]
print(sorted(flat)==list(range(5)))
```
Kết quả: True

</details>

##### ML06-practice-12

Vì sao gradient mini-batch có thể dao động khác gradient toàn tập?

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi batch chỉ chứa một phần dữ liệu, có phân bố và residual khác nhau; gradient ước lượng có biến thiên giữa batch. Không từ đó kết luận mọi bước đều giảm loss toàn tập.

</details>

<a id="ml07"></a>

## ML07 · Hồi quy đa biến và Normal Equations

[Mục lục](#muc-luc) · M2 · Hồi quy tuyến tính và tối ưu hóa · Tiên quyết [ML04](#ml04), [ML05](#ml05)

<a id="ml07-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Thêm cột 1 để biểu diễn hệ số chặn. Normal equations cho nghiệm duy nhất khi ma trận thiết kế đủ hạng cột. Dùng lstsq vẫn tìm được nghiệm bình phương tối thiểu khi thiếu hạng.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Đoán shape và hạng của A. Chỉ ra cột bias.
2. **P2** · Suy ra intercept cùng hai hệ số từ ba điểm đầu. Dự đoán cả vector ŷ.

<a id="ml07-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0., 0.], [1., 0.], [0., 1.], [1., 1.]])
y = np.array([1., 3., 0., 2.])
A = np.column_stack([np.ones(len(X)), X])
w = np.linalg.solve(A.T @ A, A.T @ y)
print(A.shape, np.linalg.matrix_rank(A))
print(w.round(6).tolist(), (A @ w).round(6).tolist())
~~~

[Xem kết quả mẫu](#ml07-ket-qua)

<a id="ml07-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Viết shape của A.T @ A và A.T @ y trước khi gọi solve.
2. **I2** · Giải thích vì sao lặp một cột dẫn tới vô số hệ số có thể cho cùng ŷ.

[Đối chiếu cách giải thích](#ml07-giai-thich)

<a id="ml07-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Bỏ cột 1. Fit lại và kiểm dự đoán tại [0,0] bằng 0 thay vì 1.
2. **MO2** · Thay cột thứ hai của X bằng cột thứ nhất. In rank(A) và kiểm hạng còn 2.
3. **MO3** · Trong biến thể thiếu hạng, đổi `solve` sang `lstsq(A, y, rcond=None)`. Kiểm hai hệ số cột trùng bằng nhau.

<a id="ml07-make"></a>

### E · Make 1 · Viết hàm

**`fit_linear(X, y)`**

Nhận X 2D hữu hạn với n,d ≥ 1 và y 1D cùng số hàng. Trả vector hệ số gồm intercept đứng đầu, dùng nghiệm chuẩn Euclid nhỏ nhất trong các nghiệm khớp bình phương tối thiểu. Báo ValueError nếu shape sai.

Điền hàm. Chạy `python ML07.py`.

[Mã khởi đầu và 4 ca kiểm](#ml07-starter) · [Lời giải](#ml07-loi-giai)

<a id="ml07-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm dùng hệ số đã fit để dự đoán cho batch X mới. Với hệ số [1,2,−3] và X=[[2,1],[0,2]], kiểm kết quả [2,−5]. Báo lỗi nếu số cột sai.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml07-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml07-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
(4, 3) 3
[1.0, 2.0, -1.0] [1.0, 3.0, 0.0, 2.0]
~~~

</details>

<details class="answer" id="ml07-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

A có shape (4,3) và hạng 3. Nghiệm [1,2,−1] cho [1,3,0,2]. Cột lặp làm hai hệ số chỉ xác định được qua tổng của chúng.

</details>

<details class="answer" id="ml07-starter" data-starter="ML07">
<summary>E · Mã khởi đầu và ca kiểm · ML07.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def fit_linear(X, y):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(fit_linear([[0], [1], [2]], [2, 5, 8]), [2, 3])


def case_02():
    same(fit_linear([[0, 0], [1, 1], [2, 2]], [1, 3, 5]), [1, 1, 1])


def case_03():
    same(fit_linear([[0, 0], [1, 0], [0, 1]], [1, 3, -2]), [1, 2, -3])


def case_04():
    rejects(fit_linear, [[1], [2]], [1])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml07-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def fit_linear(X, y):
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),):
        raise ValueError("Shape không hợp lệ")
    A = np.column_stack([np.ones(len(X)), X])
    return np.linalg.lstsq(A, y, rcond=None)[0]
~~~

</details>

<a id="ml07-on-tap"></a>

### Ôn tập ML07

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML07-mcq-1

Design matrix, bias, solve và lstsq cho hồi quy đa biến: lựa chọn đúng?

- **A** · Bỏ qua kiểm tra shape
- **B** · Thực hiện đúng công thức và kiểm tra điều kiện
- **C** · Dùng thư viện thay thế thuật toán

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thuật toán cần đúng công thức và hợp đồng dữ liệu.

- **A** · Dễ tạo lỗi im lặng.
- **B** · Đúng.
- **C** · Không phù hợp mục tiêu.

</details>

##### ML07-mcq-2

Trường hợp biên nào cần xử lý?

- **A** · input rỗng hoặc batch không hợp lệ
- **B** · không có trường hợp biên
- **C** · chỉ đổi tên biến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Kiểm tra biên giúp tránh kết quả sai.

- **A** · Đúng.
- **B** · Sai.
- **C** · Không.

</details>

##### ML07-mcq-3

Kết quả đúng phụ thuộc vào?

- **A** · shape và kiểu dữ liệu
- **B** · màu giao diện
- **C** · hard-code đáp án

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Shape và dữ liệu quyết định phép tính.

- **A** · Đúng.
- **B** · Không.
- **C** · Không được.

</details>

##### ML07-mcq-4

X là ma trận thiết kế shape (10,3). X.T@X có shape nào?

- **A** · (10,10)
- **B** · (3,3)
- **C** · (10,3)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

(3,10) nhân (10,3) cho (3,3).

- **A** · Đó là shape của X@X.T.
- **B** · (3,10) nhân (10,3) cho (3,3).
- **C** · Đây là shape X, không phải Gram matrix.

</details>

##### ML07-mcq-5

Công thức inverse của normal equations cho nghiệm duy nhất khi nào?

- **A** · X đủ hạng cột
- **B** · Chỉ cần có nhiều số trong X
- **C** · Mọi nhãn phải khác nhau

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Khi đó X.T@X khả nghịch trong số học chính xác.

- **A** · Khi đó X.T@X khả nghịch trong số học chính xác.
- **B** · Số phần tử không xác định tính độc lập cột.
- **C** · Nhãn trùng không tự gây suy biến ma trận thiết kế.

</details>

##### ML07-mcq-6

Nếu X có hai cột giống hệt nhau, điều gì xảy ra với công thức inverse chuẩn?

- **A** · Luôn có inverse
- **B** · Đổi y sẽ làm X.T@X khả nghịch
- **C** · X không đủ hạng cột, Gram matrix suy biến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Công thức inverse không áp dụng; least squares vẫn có thể có nhiều nghiệm.

- **A** · Hai cột trùng tạo phụ thuộc tuyến tính.
- **B** · Gram matrix chỉ phụ thuộc X.
- **C** · Công thức inverse không áp dụng; least squares vẫn có thể có nhiều nghiệm.

</details>

##### ML07-mcq-7

Với X đã có cột bias bên trái, theta[0] biểu diễn gì?

- **A** · Hệ số chặn
- **B** · Số mẫu
- **C** · Gradient đầu tiên

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cột toàn 1 nhân theta[0] tạo thành phần chặn.

- **A** · Cột toàn 1 nhân theta[0] tạo thành phần chặn.
- **B** · Theta chứa hệ số mô hình, không chứa số mẫu.
- **C** · Theta là tham số, không phải gradient.

</details>

##### ML07-mcq-8

Vì sao dùng solve(A,b) thay inv(A)@b khi A khả nghịch?

- **A** · Để mọi hệ suy biến tự có nghiệm duy nhất
- **B** · Giải trực tiếp hệ mà không cần tạo inverse tường minh
- **C** · Để bỏ qua kiểm tra shape

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Đây thường là lựa chọn tốt hơn về thực thi và số học; normal equations vẫn có hạn chế điều kiện số.

- **A** · Solve vẫn cần hệ hợp lệ và có thể thất bại khi suy biến.
- **B** · Đây thường là lựa chọn tốt hơn về thực thi và số học; normal equations vẫn có hạn chế điều kiện số.
- **C** · Shape vẫn phải khớp.

</details>

##### ML07-mcq-9

Nếu Gram matrix suy biến, có thể nói bài toán least squares không có nghiệm tối ưu không?

- **A** · Có, mọi trường hợp đều vô nghiệm
- **B** · Có, vì y luôn không hữu hạn
- **C** · Không; vấn đề là tính duy nhất và công thức inverse

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Có thể dùng lstsq/pseudoinverse để chọn nghiệm; không dùng inverse chuẩn.

- **A** · Least squares tuyến tính vẫn có nghiệm tối ưu.
- **B** · Tính hữu hạn y là vấn đề khác.
- **C** · Có thể dùng lstsq/pseudoinverse để chọn nghiệm; không dùng inverse chuẩn.

</details>

##### ML07-mcq-10

X đủ hạng cột có đồng nghĩa normal equations luôn ổn định số hoàn hảo không?

- **A** · Không
- **B** · Có,mọi phép tính máy là chính xác
- **C** · Có nếu dùng inv thay solve

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Điều kiện khả nghịch toán học khác độ điều kiện số và sai số tính toán.

- **A** · Điều kiện khả nghịch toán học khác độ điều kiện số và sai số tính toán.
- **B** · Số thực máy có sai số.
- **C** · Tạo inverse không bảo đảm ổn định hơn.

</details>

#### Tự luận và viết mã

##### ML07-practice-1

X shape (7,3),y shape (7,). Nêu shape của X.T@y và theta.

<details>
<summary>Đáp án và cách kiểm</summary>

X.T@y là vector (3,); theta là vector (3,). Nếu X đã chứa bias thì ba thành phần đã gồm bias.

</details>

##### ML07-practice-2

Tính X.T@X với X=[[1,1],[1,2]].

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả [[2,3],[3,5]].

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]])
print((X.T@X).tolist())
```
Kết quả: [[2.0, 3.0], [3.0, 5.0]]

</details>

##### ML07-practice-3

Với X=[[1,1],[1,2]],y=[2,4], tính X.T@y.

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả [6,10].

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]]);y=np.array([2.,4.])
print((X.T@y).tolist())
```
Kết quả: [6.0, 10.0]

</details>

##### ML07-practice-4

Giải normal equations cho X=[[1,1],[1,2]],y=[2,4].

<details>
<summary>Đáp án và cách kiểm</summary>

Theta=[0,2], nên dự đoán là 0+2x.

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]]);y=np.array([2.,4.])
t=np.linalg.solve(X.T@X,X.T@y)
print(np.round(t,6).tolist())
```
Kết quả: [0.0, 2.0]

</details>

##### ML07-practice-5

Không có bias: X=[[2],[4]],y=[3,6]. Tính theta.

<details>
<summary>Đáp án và cách kiểm</summary>

Theta=(4+16)⁻¹(6+24)=1.5.

```python
import numpy as np
X=np.array([[2.],[4.]]);y=np.array([3.,6.])
print(np.linalg.solve(X.T@X,X.T@y).tolist())
```
Kết quả: [1.5]

</details>

##### ML07-practice-6

Kiểm tra rank của X=[[1,2],[2,4]]. Vì sao không dùng inverse chuẩn?

<details>
<summary>Đáp án và cách kiểm</summary>

Rank=1<2 vì cột hai gấp đôi cột một; Gram matrix suy biến.

```python
import numpy as np
X=np.array([[1.,2.],[2.,4.]])
print(int(np.linalg.matrix_rank(X)))
```
Kết quả: 1

</details>

##### ML07-practice-7

X có 2 hàng và 3 cột. Có thể đủ hạng cột không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Rank không vượt min(2,3)=2 nên không thể bằng 3; không áp dụng công thức inverse của Gram matrix.

</details>

##### ML07-practice-8

Nêu lỗi khi kiểm X.shape != y.shape để xác định số mẫu khớp nhau.

<details>
<summary>Đáp án và cách kiểm</summary>

X là 2D nên shape là (m,d), y là 1D nên shape là (m,). Hai tuple vốn khác nhau. Phải kiểm ndim rồi so X.shape[0] với y.shape[0].

</details>

##### ML07-practice-9

Vì sao np.linalg.matrix_rank(A) < A.shape là điều kiện sai?

<details>
<summary>Đáp án và cách kiểm</summary>

A.shape là tuple kích thước, không phải số cột. Với A vuông, so rank với A.shape[0] sau khi kiểm A là ma trận vuông.

</details>

##### ML07-practice-10

Với một đặc trưng x=[20,40], thêm bias rồi giải y=[1.6,3.2].

<details>
<summary>Đáp án và cách kiểm</summary>

Theta xấp xỉ [0,0.08]. Không làm tròn bên trong solver chỉ để trông giống đáp án.

```python
import numpy as np
x=np.array([20.,40.]);X=np.column_stack([np.ones(2),x]);y=np.array([1.6,3.2])
t=np.linalg.solve(X.T@X,X.T@y)
print(bool(np.allclose(t,[0.,.08],rtol=1e-9,atol=1e-12)))
```
Kết quả: True

</details>

##### ML07-practice-11

Đổi thứ tự cột trong X nhưng dùng nguyên theta cũ có bảo toàn dự đoán không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không nói chung. Cần hoán vị theta tương ứng với hoán vị cột; các hệ số phải gắn đúng đặc trưng.

</details>

##### ML07-practice-12

Giải least squares cho dữ liệu có cột trùng bằng lstsq. Có thể tính dự đoán hữu hạn dù inverse không tồn tại không?

<details>
<summary>Đáp án và cách kiểm</summary>

Có. lstsq chọn một nghiệm least squares; ví dụ hai cột giống nhau có thể chia đều hệ số. Điều này không khôi phục tính duy nhất của toàn bộ hệ số.

```python
import numpy as np
X=np.array([[1.,1.],[2.,2.],[3.,3.]]);y=np.array([2.,4.,6.])
t=np.linalg.lstsq(X,y,rcond=None)[0]
print(bool(np.allclose(X@t,y)))
```
Kết quả: True

</details>

<a id="ml08"></a>

## ML08 · Đặc trưng đa thức và nguy cơ quá khớp

[Mục lục](#muc-luc) · M2 · Hồi quy tuyến tính và tối ưu hóa · Tiên quyết [ML07](#ml07)

<a id="ml08-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Hồi quy đa thức tuyến tính theo hệ số. Tăng bậc rồi so sai số train và validation để thấy ảnh hưởng của độ phức tạp.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Viết ba hàng của design matrix cho mỗi bậc.
2. **P2** · Dự đoán bậc nào fit đúng ba điểm và ŷ tại x=2 của bậc đó.

<a id="ml08-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([-1., 0., 1.])
y = np.array([1., 0., 1.])
x_new = np.array([2.])
for degree in [1, 2]:
    A = np.vander(x, degree + 1, increasing=True)
    w = np.linalg.lstsq(A, y, rcond=None)[0]
    y_new = np.vander(x_new, degree + 1, increasing=True) @ w
    print(A.shape, round(np.mean((A @ w - y)**2), 6), y_new.round(6).tolist())
~~~

[Xem kết quả mẫu](#ml08-ket-qua)

<a id="ml08-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Chỉ ra cột đại diện cho từng lũy thừa. Giải thích increasing=True giữ cột 1 đầu tiên.
2. **I2** · Tách phần fit trên x,y khỏi phép dự đoán trên x_new. Vì sao train MSE một mình chưa đủ chọn bậc?

[Đối chiếu cách giải thích](#ml08-giai-thich)

<a id="ml08-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Thêm bậc 0. Kiểm dự đoán 2/3 và train MSE 2/9.
2. **MO2** · Đổi y thành [−1,0,1]. Kiểm cả bậc 1 và 2 cho ŷ(2) ≈ 2.
3. **MO3** · Giữ y gốc, đặt validation (2,0). Tính MSE validation cho hai bậc và so với thứ tự trên train.

<a id="ml08-make"></a>

### E · Make 1 · Viết hàm

**`poly_features(x, degree)`**

Nhận vector 1D và degree là số nguyên không âm. Trả ma trận với cột x⁰ đến xᵈ, cho phép x rỗng. Báo ValueError nếu x sai chiều hoặc degree âm.

Điền hàm. Chạy `python ML08.py`.

[Mã khởi đầu và 4 ca kiểm](#ml08-starter) · [Lời giải](#ml08-loi-giai)

<a id="ml08-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm chọn bậc từ [0,1,2] theo MSE validation rồi trả (bậc, loss). Dùng train như mẫu, validation x=[−2,2], y=[4,4]. Kiểm bậc 2 và loss xấp xỉ 0.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml08-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml08-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
(3, 2) 0.222222 [0.666667]
(3, 3) 0.0 [4.0]
~~~

</details>

<details class="answer" id="ml08-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Với x=−1,0,1, các hàng bậc 1 là [1,−1],[1,0],[1,1]. Bậc 2 nối [1,0,1] theo từng hàng. Bậc 2 fit đúng và dự đoán 4 tại 2.

</details>

<details class="answer" id="ml08-starter" data-starter="ML08">
<summary>E · Mã khởi đầu và ca kiểm · ML08.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def poly_features(x, degree):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(poly_features([-2, 0, 2], 3), [[1,-2,4,-8],[1,0,0,0],[1,2,4,8]])


def case_02():
    same(poly_features([4, -1], 0), [[1], [1]])


def case_03():
    same(poly_features([], 2), np.empty((0, 3)))


def case_04():
    rejects(poly_features, [[2]], 2)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml08-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def poly_features(x, degree):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or degree < 0:
        raise ValueError("Đầu vào không hợp lệ")
    return np.vander(x, degree + 1, increasing=True)
~~~

</details>

<a id="ml08-on-tap"></a>

### Ôn tập ML08

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML08-mcq-1

Polynomial features, basis expansion và overfitting: lựa chọn đúng?

- **A** · Bỏ qua kiểm tra shape
- **B** · Thực hiện đúng công thức và kiểm tra điều kiện
- **C** · Dùng thư viện thay thế thuật toán

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thuật toán cần đúng công thức và hợp đồng dữ liệu.

- **A** · Dễ tạo lỗi im lặng.
- **B** · Đúng.
- **C** · Không phù hợp mục tiêu.

</details>

##### ML08-mcq-2

Trường hợp biên nào cần xử lý?

- **A** · input rỗng hoặc batch không hợp lệ
- **B** · không có trường hợp biên
- **C** · chỉ đổi tên biến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Kiểm tra biên giúp tránh kết quả sai.

- **A** · Đúng.
- **B** · Sai.
- **C** · Không.

</details>

##### ML08-mcq-3

Kết quả đúng phụ thuộc vào?

- **A** · shape và kiểu dữ liệu
- **B** · màu giao diện
- **C** · hard-code đáp án

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Shape và dữ liệu quyết định phép tính.

- **A** · Đúng.
- **B** · Không.
- **C** · Không được.

</details>

##### ML08-mcq-4

Một biến x được mở rộng thành [1,x,x²]. Với n mẫu, ma trận thiết kế có shape nào?

- **A** · (n,3)
- **B** · (3,n)
- **C** · (n,2)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Ba cột gồm bias và hai lũy thừa.

- **A** · Ba cột gồm bias và hai lũy thừa.
- **B** · Đảo hai trục mẫu/đặc trưng.
- **C** · Đã bỏ qua cột bias.

</details>

##### ML08-mcq-5

Mô hình theta0+theta1*x+theta2*x² có tuyến tính theo tham số không?

- **A** · Không vì có x²
- **B** · Có vì mỗi theta chỉ xuất hiện bậc nhất
- **C** · Chỉ khi theta2=0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Các cột 1,x,x² cố định; dự đoán là tích ma trận với theta.

- **A** · Phi tuyến theo x khác phi tuyến theo theta.
- **B** · Các cột 1,x,x² cố định; dự đoán là tích ma trận với theta.
- **C** · Không cần ép hệ số bậc hai bằng 0.

</details>

##### ML08-mcq-6

Tăng bậc đa thức bảo đảm điều gì về sai số trên test?

- **A** · Luôn giảm
- **B** · Luôn bằng 0
- **C** · Không bảo đảm giảm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cần đánh giá trên dữ liệu chưa dùng huấn luyện.

- **A** · Mô hình phức tạp có thể overfit.
- **B** · Khớp train không bảo đảm khớp test.
- **C** · Cần đánh giá trên dữ liệu chưa dùng huấn luyện.

</details>

##### ML08-mcq-7

Với x=2, hàng đặc trưng bậc ba gồm bias là gì?

- **A** · [1,2,4,8]
- **B** · [2,4,6]
- **C** · [1,2,3,4]

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Lần lượt x⁰,x¹,x²,x³.

- **A** · Lần lượt x⁰,x¹,x²,x³.
- **B** · Nhân x với số mũ không phải lấy lũy thừa.
- **C** · Đây không phải các lũy thừa của 2.

</details>

##### ML08-mcq-8

Vì sao phải giữ cùng quy tắc mở rộng cột cho train và test?

- **A** · Để test có cùng số hàng với train
- **B** · Để mỗi hệ số gắn đúng cùng đặc trưng khi dự đoán
- **C** · Để mọi giá trị test bằng train

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thứ tự và định nghĩa cột tạo hợp đồng với theta.

- **A** · Số mẫu hai tập có thể khác nhau.
- **B** · Thứ tự và định nghĩa cột tạo hợp đồng với theta.
- **C** · Không cần và không nên ép dữ liệu hai tập giống nhau.

</details>

##### ML08-mcq-9

Tạo hai cột bias giống nhau trong ma trận thiết kế gây vấn đề gì?

- **A** · Tăng gấp đôi số mẫu
- **B** · Tự giảm overfitting
- **C** · Tạo cột phụ thuộc tuyến tính

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Hai cột giống nhau làm mất đủ hạng cột; inverse chuẩn có thể không dùng được.

- **A** · Thêm cột không thêm hàng.
- **B** · Không có bảo đảm giảm overfitting.
- **C** · Hai cột giống nhau làm mất đủ hạng cột; inverse chuẩn có thể không dùng được.

</details>

##### ML08-mcq-10

Hai cột x và x² có luôn độc lập tuyến tính trên mọi tập mẫu không?

- **A** · Không
- **B** · Có vì ký hiệu khác nhau
- **C** · Chỉ cần số mẫu chẵn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cần kiểm dữ liệu thực tế,chẳng hạn toàn x=1 tạo hai cột giống nhau.

- **A** · Cần kiểm dữ liệu thực tế,chẳng hạn toàn x=1 tạo hai cột giống nhau.
- **B** · Trên dữ liệu đặc biệt như x toàn 1 chúng trùng nhau.
- **C** · Chẵn lẻ không quyết định rank.

</details>

#### Tự luận và viết mã

##### ML08-practice-1

Tạo ma trận [1,x,x²] cho x=[0,1,2].

<details>
<summary>Đáp án và cách kiểm</summary>

Các hàng là [1,0,0],[1,1,1],[1,2,4].

```python
import numpy as np
x=np.array([0.,1.,2.])
print(np.column_stack([np.ones(len(x)),x,x**2]).tolist())
```
Kết quả: [[1.0, 0.0, 0.0], [1.0, 1.0, 1.0], [1.0, 2.0, 4.0]]

</details>

##### ML08-practice-2

Với theta=[1,2,3], tính dự đoán tại x=2 theo [1,x,x²].

<details>
<summary>Đáp án và cách kiểm</summary>

1+2×2+3×4=17.

```python
import numpy as np
print(float(np.array([1.,2.,4.])@np.array([1.,2.,3.])))
```
Kết quả: 17.0

</details>

##### ML08-practice-3

Tạo hàng bậc ba gồm bias cho x=−2.

<details>
<summary>Đáp án và cách kiểm</summary>

[1,−2,4,−8]; số mũ lẻ giữ dấu âm.

```python
x=-2
print([x**i for i in range(4)])
```
Kết quả: [1, -2, 4, -8]

</details>

##### ML08-practice-4

Dữ liệu có 5 mẫu, mở rộng một biến đến bậc 4 có bias. Nêu shape và số hệ số.

<details>
<summary>Đáp án và cách kiểm</summary>

Ma trận (5,5); có 5 hệ số. Điều này chưa tự chứng minh ma trận đủ hạng.

</details>

##### ML08-practice-5

So sánh x**2 và 2*x tại x=[1,2,3].

<details>
<summary>Đáp án và cách kiểm</summary>

Bình phương [1,4,9] khác nhân đôi [2,4,6].

```python
import numpy as np
x=np.array([1,2,3])
print((x**2).tolist())
print((2*x).tolist())
```
Kết quả: [1, 4, 9]
[2, 4, 6]

</details>

##### ML08-practice-6

Dự đoán cho X_poly=[[1,0,0],[1,1,1],[1,2,4]],theta=[1,2,1].

<details>
<summary>Đáp án và cách kiểm</summary>

Các dự đoán là [1,4,9].

```python
import numpy as np
X=np.array([[1.,0.,0.],[1.,1.,1.],[1.,2.,4.]])
print((X@np.array([1.,2.,1.])).tolist())
```
Kết quả: [1.0, 4.0, 9.0]

</details>

##### ML08-practice-7

Giải thích vì sao polynomial regression vẫn dùng được mô hình y_hat=X_poly@theta.

<details>
<summary>Đáp án và cách kiểm</summary>

Các phép lũy thừa được tính thành cột dữ liệu trước. Mô hình sau đó cộng tuyến tính các cột với trọng số theta; phi tuyến nằm ở ánh xạ x sang đặc trưng.

</details>

##### ML08-practice-8

Hai mô hình bậc 1 và 6 có train error lần lượt 2 và 0. Có đủ dữ liệu để chọn bậc 6 không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Chỉ biết bậc 6 khớp train hơn, chưa có bằng chứng về tổng quát hóa. Cần đánh giá theo quy trình dữ liệu riêng sẽ học ở ML13.

</details>

##### ML08-practice-9

Một bạn chỉ tạo [x,x²] cho test trong khi train dùng [1,x,x²]. Lỗi là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Thiếu bias làm số cột không khớp theta ba phần tử. Cần áp dụng cùng phép tạo đặc trưng ở hai nơi.

</details>

##### ML08-practice-10

Tại x=10, so sánh độ lớn x và x⁴. Vì sao cần chú ý thang đo?

<details>
<summary>Đáp án và cách kiểm</summary>

x=10,x⁴=10000. Các cột có độ lớn chênh lệch có thể gây vấn đề tối ưu/số học; cần dùng đúng quy trình scaling đã học.

</details>

##### ML08-practice-11

x=[1,1,1], tạo [1,x,x²]. Có đủ hạng cột không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không, ba cột đều giống nhau, rank chỉ 1.

```python
import numpy as np
x=np.ones(3);X=np.column_stack([np.ones(3),x,x**2])
print(int(np.linalg.matrix_rank(X)))
```
Kết quả: 1

</details>

##### ML08-practice-12

Mở rộng bậc 0 cho n mẫu có ý nghĩa mô hình gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Chỉ có cột toàn 1 nên mô hình dự đoán hằng theta0 cho mọi mẫu; không phụ thuộc x.

</details>

<a id="ml09"></a>

## ML09 · Tính sigmoid, xác suất và ranh giới quyết định tuyến tính/phi tuyến

[Mục lục](#muc-luc) · M3 · Phân loại và tối ưu bậc hai · Tiên quyết [ML04](#ml04)

<a id="ml09-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Dùng sigmoid để đổi logit z thành xác suất p. Với ngưỡng 0.5, p ≥ 0.5 tương đương z ≥ 0.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính ba logit, rồi dự đoán nhãn.
2. **P2** · Điểm nào có xác suất lớn nhất? Viết phương trình ranh giới cho ngưỡng 0.5.

<a id="ml09-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0., 0.], [1., 0.], [0., 1.]])
z = X @ np.array([2., -2.]) - 1
p = np.exp(-np.logaddexp(0, -z))
print(z.tolist(), p.round(4).tolist())
print((p >= 0.5).astype(int).tolist())
~~~

[Xem kết quả mẫu](#ml09-ket-qua)

<a id="ml09-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích công thức exp(−logaddexp(0, −z)) tương đương sigmoid. Đối chiếu p(0) = 0.5.
2. **I2** · Phân biệt thứ tự xác suất với nhãn sau threshold. Chỉ ra thao tác làm mất thông tin thứ tự trong cùng một nhãn.

[Đối chiếu cách giải thích](#ml09-giai-thich)

<a id="ml09-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi bias thành 0. Kiểm mẫu [0,0] có p=0.5 và nhãn 1.
2. **MO2** · Đổi ngưỡng thành 0.8. Kiểm ba nhãn gốc trở thành [0,0,0].
3. **MO3** · Thêm đặc trưng x₁². Dùng logit x₁²−x₂ và ba điểm [−2,1], [0,1], [2,1]. Kiểm nhãn [1,0,1].

<a id="ml09-make"></a>

### E · Make 1 · Viết hàm

**`logistic_labels(logits, threshold)`**

Nhận vector logit 1D hữu hạn, ngưỡng thuộc (0, 1). Tính sigmoid theo cách ổn định rồi trả vector 0/1, bằng ngưỡng thì gán 1. Báo ValueError nếu miền sai.

Điền hàm. Chạy `python ML09.py`.

[Mã khởi đầu và 4 ca kiểm](#ml09-starter) · [Lời giải](#ml09-loi-giai)

<a id="ml09-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm tìm hoành độ biên quyết định một chiều cho z=wx+b, w≠0 và ngưỡng tùy ý. Với w=2, b=−1, threshold=0.5, trả x=0.5. Với threshold=0.75, kiểm x=(1+ln(3))/2.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml09-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml09-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[-1.0, 1.0, -3.0] [0.2689, 0.7311, 0.0474]
[0, 1, 0]
~~~

</details>

<details class="answer" id="ml09-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Logit [−1,1,−3] cho nhãn [0,1,0]. Xác suất cao nhất ở [1,0]. Biên có phương trình 2x₁−2x₂−1=0.

</details>

<details class="answer" id="ml09-starter" data-starter="ML09">
<summary>E · Mã khởi đầu và ca kiểm · ML09.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def logistic_labels(logits, threshold):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(logistic_labels([-1000, 0, 1000], 0.5), [0, 1, 1])


def case_02():
    same(logistic_labels([-1, 0, 1, 2], 0.8), [0, 0, 0, 1])


def case_03():
    same(logistic_labels([0], 0.1), [1])


def case_04():
    rejects(logistic_labels, [0], 1)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml09-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def logistic_labels(logits, threshold):
    logits = np.asarray(logits, dtype=float)
    if logits.ndim != 1 or not np.all(np.isfinite(logits)) or not 0 < threshold < 1:
        raise ValueError("Logit hoặc threshold không hợp lệ")
    p = np.exp(-np.logaddexp(0, -logits))
    return (p >= threshold).astype(int)
~~~

</details>

<a id="ml09-on-tap"></a>

### Ôn tập ML09

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML09-mcq-1

Đầu vào z của sigmoid có miền toán học nào?

- **A** · Toàn bộ số thực
- **B** · Chỉ [0,1]
- **C** · Chỉ số nguyên

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tổ hợp tuyến tính có thể âm,dương hoặc 0.

- **A** · Tổ hợp tuyến tính có thể âm,dương hoặc 0.
- **B** · Đó là miền xác suất,không phải logit.
- **C** · z có thể liên tục.

</details>

##### ML09-mcq-2

Sigmoid biến z=ln(3) thành p nào?

- **A** · 3
- **B** · 0.75
- **C** · 0.25

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

exp(−ln3)=1/3 nên 1/(1+1/3)=3/4.

- **A** · Chưa ánh xạ qua sigmoid.
- **B** · exp(−ln3)=1/3 nên 1/(1+1/3)=3/4.
- **C** · Đó là sigmoid(−ln3).

</details>

##### ML09-mcq-3

Nếu đổi w,b thành −w,−b thì xác suất sigmoid mới là gì?

- **A** · p+1
- **B** · −p
- **C** · 1−p

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Sigmoid(−z)=1−sigmoid(z).

- **A** · Có thể vượt 1.
- **B** · Xác suất không âm.
- **C** · Sigmoid(−z)=1−sigmoid(z).

</details>

##### ML09-mcq-4

Sigmoid tại z=0 bằng bao nhiêu?

- **A** · 0
- **B** · 0.5
- **C** · 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

1/(1+exp(0))=1/2.

- **A** · Sigmoid hữu hạn luôn dương.
- **B** · 1/(1+exp(0))=1/2.
- **C** · Sigmoid tại 0 không phải 1.

</details>

##### ML09-mcq-5

Với quy tắc dự đoán 1 khi p≥0.5, z=−2 cho lớp nào?

- **A** · 0
- **B** · 1
- **C** · Không thể xác định vì không có y thật

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Sigmoid tăng và z<0 cho p<0.5.

- **A** · Sigmoid tăng và z<0 cho p<0.5.
- **B** · Sai dấu so với ngưỡng.
- **C** · Dự đoán không cần biết nhãn thật.

</details>

##### ML09-mcq-6

Một mô hình cho p=0.8. Cách hiểu nào đúng?

- **A** · Chắc chắn nhãn thật bằng 1
- **B** · Mô hình đúng 80% trên toàn bộ test
- **C** · Đây là xác suất lớp 1 do mô hình ước lượng cho mẫu này

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Đó là ý nghĩa đầu ra mô hình, không phải bằng chứng hiệu chuẩn xác suất.

- **A** · Xác suất không phải bảo đảm sự kiện.
- **B** · Một dự đoán không xác định accuracy toàn tập.
- **C** · Đó là ý nghĩa đầu ra mô hình, không phải bằng chứng hiệu chuẩn xác suất.

</details>

##### ML09-mcq-7

Nếu z=b+w1*x1+w2*x2, ranh giới p=0.5 tương ứng điều kiện nào?

- **A** · z=0
- **B** · z=0.5
- **C** · z=1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Sigmoid(0)=0.5.

- **A** · Sigmoid(0)=0.5.
- **B** · Nhầm xác suất với đầu vào sigmoid.
- **C** · Sigmoid(1) lớn hơn 0.5.

</details>

##### ML09-mcq-8

Giữ p của mọi mẫu, tăng ngưỡng dự đoán lớp 1 từ 0.5 lên 0.8 sẽ có tác động nào?

- **A** · Mọi mẫu tự có p cao hơn
- **B** · Tập mẫu dự đoán 1 không thể tăng
- **C** · Số dự đoán 1 bắt buộc giảm đúng một nửa

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Điều kiện chặt hơn nên chỉ giữ nguyên hoặc giảm số dự đoán 1.

- **A** · Ngưỡng không thay đổi xác suất mô hình.
- **B** · Điều kiện chặt hơn nên chỉ giữ nguyên hoặc giảm số dự đoán 1.
- **C** · Mức thay đổi phụ thuộc phân bố p.

</details>

##### ML09-mcq-9

Dùng đặc trưng x² trong z có cho phép ranh giới phi tuyến theo x gốc không?

- **A** · Không bao giờ
- **B** · Chỉ khi sigmoid bị bỏ đi
- **C** · Có

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

z tuyến tính theo đặc trưng mở rộng có thể phi tuyến theo tọa độ gốc.

- **A** · Phi tuyến theo x có thể xuất hiện qua ánh xạ đặc trưng.
- **B** · Sigmoid vẫn ánh xạ z sang xác suất.
- **C** · z tuyến tính theo đặc trưng mở rộng có thể phi tuyến theo tọa độ gốc.

</details>

##### ML09-mcq-10

Tại cùng mẫu,z tăng từ 0 lên 1 thì sigmoid thay đổi ra sao?

- **A** · Tăng từ 0.5 lên khoảng 0.7311
- **B** · Giảm từ 0.5 xuống 0
- **C** · Giữ nguyên vì nhãn chưa đổi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Sigmoid là hàm tăng.

- **A** · Sigmoid là hàm tăng.
- **B** · Sigmoid tăng theo z.
- **C** · Xác suất có thể đổi dù nhãn threshold giữ nguyên.

</details>

#### Tự luận và viết mã

##### ML09-practice-1

Tính sigmoid tại z=0.

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả 0.5.

```python
import numpy as np
print(float(1/(1+np.exp(0.))))
```
Kết quả: 0.5

</details>

##### ML09-practice-2

Tính sigmoid tại z=[−2,0,2], làm tròn bốn chữ số để hiển thị.

<details>
<summary>Đáp án và cách kiểm</summary>

Xấp xỉ [0.1192,0.5,0.8808].

```python
import numpy as np
z=np.array([-2.,0.,2.])
print(np.round(1/(1+np.exp(-z)),4).tolist())
```
Kết quả: [0.1192, 0.5, 0.8808]

</details>

##### ML09-practice-3

p=[0.2,0.5,0.9], quy tắc lớp 1 nếu p≥0.5. Dự đoán nhãn.

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả [0,1,1]; p đúng ngưỡng thuộc lớp 1 theo quy ước đề.

```python
import numpy as np
p=np.array([.2,.5,.9])
print((p>=.5).astype(int).tolist())
```
Kết quả: [0, 1, 1]

</details>

##### ML09-practice-4

Với b=−3,w=2, tìm ranh giới p=0.5 theo x.

<details>
<summary>Đáp án và cách kiểm</summary>

−3+2x=0 nên x=1.5. Phía x lớn hơn có z>0 và p>0.5.

</details>

##### ML09-practice-5

Tại x=2,b=−3,w=2, tính z và sigmoid, làm tròn bốn chữ số.

<details>
<summary>Đáp án và cách kiểm</summary>

z=1,p≈0.7311.

```python
import numpy as np
z=-3.+2.*2.
print(z)
print(round(float(1/(1+np.exp(-z))),4))
```
Kết quả: 1.0
0.7311

</details>

##### ML09-practice-6

Với p=[0.4,0.6,0.8], so sánh dự đoán ở ngưỡng 0.5 và 0.8, dùng ≥.

<details>
<summary>Đáp án và cách kiểm</summary>

Hai bộ nhãn là [0,1,1] và [0,0,1].

```python
import numpy as np
p=np.array([.4,.6,.8])
for threshold in [.5,.8]:
    print((p>=threshold).astype(int).tolist())
```
Kết quả: [0, 1, 1]
[0, 0, 1]

</details>

##### ML09-practice-7

Vì sao không lấy y_hat=z làm xác suất khi dùng logistic regression?

<details>
<summary>Đáp án và cách kiểm</summary>

z có thể là bất kỳ số thực nào, kể cả âm hoặc lớn hơn 1. Sigmoid ánh xạ z sang khoảng (0,1).

</details>

##### ML09-practice-8

Dùng đồng nhất thức sigmoid(−z)=1−sigmoid(z) để kiểm tra z=2.

<details>
<summary>Đáp án và cách kiểm</summary>

Hai phía bằng nhau trong dung sai số học; không so chuỗi thập phân.

```python
import numpy as np
s=lambda z:1/(1+np.exp(-z))
print(bool(np.isclose(s(-2.),1-s(2.))))
```
Kết quả: True

</details>

##### ML09-practice-9

Với z=x1+x2−3, nêu hai điểm trên ranh giới p=0.5.

<details>
<summary>Đáp án và cách kiểm</summary>

Ví dụ (1,2),(2,1), vì tổng hai tọa độ bằng 3. Đây là đường thẳng theo hai thuộc tính gốc.

</details>

##### ML09-practice-10

Với z=x²−1 và ngưỡng 0.5, tìm các điểm ranh giới trên trục x.

<details>
<summary>Đáp án và cách kiểm</summary>

z=0 cho x=−1 và x=1; lớp 1 ở |x|≥1 theo quy tắc ≥, lớp 0 khi |x|<1.

</details>

##### ML09-practice-11

Mẫu có p=0.7 nhưng nhãn thật 0. Có thể kết luận code sigmoid sai không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Xác suất mô hình không bảo đảm nhãn từng mẫu. Cần tách lỗi tính toán khỏi dự đoán sai của mô hình.

</details>

##### ML09-practice-12

X=[[1,0],[1,2]],theta=[−1,1]. Tính z và dự đoán ngưỡng 0.5.

<details>
<summary>Đáp án và cách kiểm</summary>

z=[−1,1]; dự đoán [0,1]. Cột đầu là bias.

```python
import numpy as np
X=np.array([[1.,0.],[1.,2.]]);theta=np.array([-1.,1.])
z=X@theta
print(z.tolist())
print((1/(1+np.exp(-z))>=.5).astype(int).tolist())
```
Kết quả: [-1.0, 1.0]
[0, 1]

</details>

<a id="ml10"></a>

## ML10 · Tính cross-entropy và gradient cho hồi quy logistic

[Mục lục](#muc-luc) · M3 · Phân loại và tối ưu bậc hai · Tiên quyết [ML09](#ml09)

<a id="ml10-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tính binary cross-entropy bằng trung bình loss của từng mẫu. Tính từ logit bằng softplus để tránh log(0) và giảm nguy cơ tràn số.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán p cho hai logit bằng 0 và loss trung bình.
2. **P2** · Tính từng p−y, rồi tính gradient intercept và gradient đặc trưng.

<a id="ml10-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
A = np.array([[1., 0.], [1., 2.]])
y = np.array([0., 1.])
w = np.array([0., 0.])
z = A @ w
p = np.exp(-np.logaddexp(0, -z))
losses = np.logaddexp(0, (1 - 2 * y) * z)
print(p.tolist(), round(losses.mean(), 6))
print((A.T @ (p - y) / len(y)).tolist())
~~~

[Xem kết quả mẫu](#ml10-ket-qua)

<a id="ml10-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Chỉ ra liên hệ giữa logit có dấu đúng và loss. Vì sao tích (1−2y)z âm khi mô hình dự đoán đúng với độ tin cậy cao?
2. **I2** · Giải thích vai trò của A.T. So sánh shape của p−y và vector gradient.

[Đối chiếu cách giải thích](#ml10-giai-thich)

<a id="ml10-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi w thành [0,1]. Kiểm loss giảm so với ln(2).
2. **MO2** · Gán y=[1,0] và giữ w gốc. Kiểm loss giữ nguyên còn gradient đặc trưng đổi dấu.
3. **MO3** · Thử z=[−1000,1000], y=[0,1] rồi đảo nhãn. Kiểm loss trung bình lần lượt gần 0 và bằng 1000.

<a id="ml10-make"></a>

### E · Make 1 · Viết hàm

**`bce_and_gradient(A, y, w)`**

A là ma trận thiết kế n×d có n,d dương. y là vector nhị phân n phần tử, w là vector d phần tử. Trả tuple (loss trung bình, gradient theo w). Báo ValueError nếu shape hoặc nhãn sai.

Điền hàm. Chạy `python ML10.py`.

[Mã khởi đầu và 3 ca kiểm](#ml10-starter) · [Lời giải](#ml10-loi-giai)

<a id="ml10-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự kiểm gradient bằng sai phân trung tâm, h=10⁻⁵, trên A=[[1,0],[1,2]], y=[0,1], w=[0.1,−0.2]. Báo chênh lệch tuyệt đối lớn nhất và kiểm nhỏ hơn 10⁻⁶.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml10-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml10-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0.5, 0.5] 0.693147
[0.0, -0.5]
~~~

</details>

<details class="answer" id="ml10-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Cả hai p=0.5, loss ln(2), residual xác suất [0.5,−0.5]. Gradient [0,−0.5]. Chia cho số mẫu vì loss là trung bình.

</details>

<details class="answer" id="ml10-starter" data-starter="ML10">
<summary>E · Mã khởi đầu và ca kiểm · ML10.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def bce_and_gradient(A, y, w):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    loss, g = bce_and_gradient([[1, 1], [1, 3]], [0, 1], [0, 0])
    same(loss, np.log(2))
    same(g, [0, -0.5])


def case_02():
    loss, g = bce_and_gradient([[1], [-1]], [1, 0], [-1000])
    same(loss, 1000)
    same(g, [-1])


def case_03():
    rejects(bce_and_gradient, [[1]], [2], [0])


CASES = [case_01, case_02, case_03]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml10-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def bce_and_gradient(A, y, w):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    if A.ndim != 2 or min(A.shape) == 0 or y.shape != (len(A),) or w.shape != (A.shape[1],) or not np.isin(y, [0, 1]).all():
        raise ValueError("Shape hoặc nhãn không hợp lệ")
    z = A @ w
    p = np.exp(-np.logaddexp(0, -z))
    loss = np.logaddexp(0, (1 - 2 * y) * z).mean()
    return float(loss), A.T @ (p - y) / len(y)
~~~

</details>

<a id="ml10-on-tap"></a>

### Ôn tập ML10

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML10-mcq-1

BCE của nhãn y=0 là hàm nào theo p?

- **A** · −ln(1−p)
- **B** · −ln(p)
- **C** · p−y

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Thay y=0 vào công thức BCE.

- **A** · Thay y=0 vào công thức BCE.
- **B** · Đây là nhánh y=1.
- **C** · Đó là residual xác suất.

</details>

##### ML10-mcq-2

Với y=1 và p tăng từ 0.4 lên 0.6,BCE làm gì?

- **A** · Bắt buộc không đổi vì vẫn cùng dữ liệu
- **B** · Giảm
- **C** · Tăng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

−ln(p) giảm khi p tăng.

- **A** · Loss phụ thuộc p.
- **B** · −ln(p) giảm khi p tăng.
- **C** · Xác suất dành cho nhãn thật tăng nên loss giảm.

</details>

##### ML10-mcq-3

X shape (8,3),p−y shape (8,). Gradient mean BCE có shape nào?

- **A** · (8,)
- **B** · (8,3)
- **C** · (3,)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

X.T@(p−y)/8 trả một gradient cho mỗi hệ số.

- **A** · Đó là residual theo mẫu.
- **B** · Đó là shape X.
- **C** · X.T@(p−y)/8 trả một gradient cho mỗi hệ số.

</details>

##### ML10-mcq-4

Với nhãn y=1, binary cross-entropy của một mẫu là biểu thức nào?

- **A** · −log(p)
- **B** · −log(1−p)
- **C** · log(p)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Thay y=1 vào −y log(p)−(1−y)log(1−p).

- **A** · Thay y=1 vào −y log(p)−(1−y)log(1−p).
- **B** · Đây là loss khi y=0.
- **C** · Sai dấu, log(p) âm với p trong (0,1).

</details>

##### ML10-mcq-5

y=0. Dự đoán p=0.1 hay p=0.9 có loss nhỏ hơn?

- **A** · p=0.9
- **B** · p=0.1
- **C** · Hai giá trị luôn bằng nhau

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

−log(0.9) nhỏ hơn −log(0.1).

- **A** · Độ tin cậy cao vào lớp sai bị phạt mạnh.
- **B** · −log(0.9) nhỏ hơn −log(0.1).
- **C** · Loss phụ thuộc xác suất gán cho nhãn đúng.

</details>

##### ML10-mcq-6

Với p=sigmoid(X@theta), gradient mean BCE theo theta là?

- **A** · X.T@(y−p)/m
- **B** · p−y không cần X
- **C** · X.T@(p−y)/m

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Đây là gradient của mean BCE logistic không có regularization.

- **A** · Đảo dấu gradient; trừ nó sẽ đi sai hướng.
- **B** · Chưa ánh xạ residual mẫu về không gian tham số.
- **C** · Đây là gradient của mean BCE logistic không có regularization.

</details>

##### ML10-mcq-7

Clipping p trước log chủ yếu nhằm mục đích gì?

- **A** · Tránh log(0) khi xác suất máy biểu diễn chạm 0 hoặc 1
- **B** · Bảo đảm mô hình luôn đúng nhãn
- **C** · Tự sửa data leakage

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đây là biện pháp ổn định tính toán; epsilon cần rõ ràng.

- **A** · Đây là biện pháp ổn định tính toán; epsilon cần rõ ràng.
- **B** · Clipping không cải thiện nhãn thật hay bảo đảm chất lượng.
- **C** · Leakage thuộc quy trình dữ liệu.

</details>

##### ML10-mcq-8

Nếu p và y đều có m phần tử, vector p−y có shape nào?

- **A** · (d,) với d là số hệ số
- **B** · (m,)
- **C** · (m,m) trong mọi trường hợp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mỗi mẫu đóng góp một residual xác suất.

- **A** · Đó là shape gradient sau nhân X.T, không phải residual.
- **B** · Mỗi mẫu đóng góp một residual xác suất.
- **C** · Chỉ có thể vô tình thành ma trận khi shape bị broadcast sai.

</details>

##### ML10-mcq-9

Dự đoán sai rất tự tin có thể tạo BCE lớn hơn dự đoán sai ít tự tin không?

- **A** · Không vì đều sai một nhãn
- **B** · Không vì BCE luôn trong [0,1]
- **C** · Có

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Xác suất gán cho nhãn đúng càng gần 0, −log càng lớn.

- **A** · BCE xét độ tin cậy chứ không chỉ nhãn sau threshold.
- **B** · BCE không bị chặn trên bởi 1.
- **C** · Xác suất gán cho nhãn đúng càng gần 0, −log càng lớn.

</details>

##### ML10-mcq-10

Nhãn y=1,p tiến gần 0 thì BCE thay đổi ra sao?

- **A** · Tăng không bị chặn trong công thức lý tưởng
- **B** · Tiến về 0
- **C** · Luôn bằng 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

−log(p) tăng khi p tiến về 0 từ bên phải.

- **A** · −log(p) tăng khi p tiến về 0 từ bên phải.
- **B** · Dự đoán đang sai ngày càng tự tin.
- **C** · BCE không giới hạn ở 1.

</details>

#### Tự luận và viết mã

##### ML10-practice-1

Tính BCE khi y=1,p=0.8, dùng log tự nhiên và in sáu chữ số.

<details>
<summary>Đáp án và cách kiểm</summary>

−log(0.8)≈0.223144.

```python
import numpy as np
print(f"{-np.log(.8):.6f}")
```
Kết quả: 0.223144

</details>

##### ML10-practice-2

Tính BCE khi y=0,p=0.2. So với y=1,p=0.8.

<details>
<summary>Đáp án và cách kiểm</summary>

−log(1−0.2)=−log(0.8), bằng nhau.

```python
import numpy as np
print(f"{-np.log(1-.2):.6f}")
```
Kết quả: 0.223144

</details>

##### ML10-practice-3

y=[1,0],p=[0.8,0.3]. Tính mean BCE.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean của −log(0.8) và −log(0.7), xấp xỉ 0.289909.

```python
import numpy as np
y=np.array([1.,0.]);p=np.array([.8,.3])
print(f"{-np.mean(y*np.log(p)+(1-y)*np.log(1-p)):.6f}")
```
Kết quả: 0.289909

</details>

##### ML10-practice-4

So sánh loss của y=1 tại p=0.9 và p=0.1.

<details>
<summary>Đáp án và cách kiểm</summary>

Lần lượt khoảng 0.105361 và 2.302585; dự đoán sai tự tin bị phạt mạnh.

```python
import numpy as np
for p in [.9,.1]:
    print(f"{-np.log(p):.6f}")
```
Kết quả: 0.105361
2.302585

</details>

##### ML10-practice-5

X=[[1,0],[1,1]],theta=[0,0],y=[0,1]. Tính p và gradient.

<details>
<summary>Đáp án và cách kiểm</summary>

p=[0.5,0.5]; residual=[0.5,−0.5]; gradient=[0,−0.25].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);y=np.array([0.,1.]);p=np.full(2,.5)
print(p.tolist())
print((X.T@(p-y)/len(y)).tolist())
```
Kết quả: [0.5, 0.5]
[0.0, -0.25]

</details>

##### ML10-practice-6

Dùng gradient [0,−0.25],theta=[0,0],alpha=0.1 để cập nhật.

<details>
<summary>Đáp án và cách kiểm</summary>

Theta mới [0,0.025].

```python
import numpy as np
theta=np.zeros(2);g=np.array([0.,-.25])
print((theta-.1*g).tolist())
```
Kết quả: [0.0, 0.025]

</details>

##### ML10-practice-7

Vì sao y shape (m,1) và p shape (m,) có thể làm p−y sai?

<details>
<summary>Đáp án và cách kiểm</summary>

Broadcasting có thể tạo ma trận (m,m), không còn một residual trên mỗi mẫu. Phải chuẩn hóa và kiểm shape trước khi tính.

</details>

##### ML10-practice-8

Đặt eps=1e−6, clip p=[0,1] vào [eps,1−eps]. Kiểm loss hữu hạn.

<details>
<summary>Đáp án và cách kiểm</summary>

Sau clipping không có log(0); loss hữu hạn, nhưng giá trị vẫn phụ thuộc eps.

```python
import numpy as np
p=np.clip(np.array([0.,1.]),1e-6,1-1e-6);y=np.array([1.,0.])
loss=-np.mean(y*np.log(p)+(1-y)*np.log(1-p))
print(bool(np.isfinite(loss)))
```
Kết quả: True

</details>

##### ML10-practice-9

Vì sao không thay log tự nhiên bằng log10 mà giữ nguyên công thức gradient như cũ?

<details>
<summary>Đáp án và cách kiểm</summary>

Đổi cơ số nhân loss với hằng số 1/ln(10), gradient cũng phải nhân cùng hằng số. Giữ công thức cũ sẽ không còn là đạo hàm của loss vừa định nghĩa.

</details>

##### ML10-practice-10

Lặp đôi toàn bộ các mẫu có làm mean BCE ở cùng tham số thay đổi không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Tổng loss và m cùng nhân đôi; mean giữ nguyên.

</details>

##### ML10-practice-11

p=0.5 ở mọi mẫu thì BCE mỗi mẫu bằng bao nhiêu dù y=0 hay y=1?

<details>
<summary>Đáp án và cách kiểm</summary>

Đều bằng −ln(0.5)=ln(2)≈0.693147.

```python
import numpy as np
print(f"{-np.log(.5):.6f}")
```
Kết quả: 0.693147

</details>

##### ML10-practice-12

Một mô hình đổi p của nhãn thật 1 từ 0.6 thành 0.9. Nhãn threshold 0.5 giữ nguyên; BCE thay đổi thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

BCE giảm từ −ln(0.6) xuống −ln(0.9), dù nhãn dự đoán không đổi. Accuracy một mẫu không mô tả hết thay đổi của xác suất.

</details>

<a id="ml11"></a>

## ML11 · Dựng gradient, Hessian và một bước Newton đa biến

[Mục lục](#muc-luc) · M3 · Phân loại và tối ưu bậc hai · Tiên quyết [ML10](#ml10)

<a id="ml11-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Giải hệ HΔ = g rồi cập nhật w thành w−Δ. Dựng Hessian từ ma trận thiết kế và các trọng số p(1−p).

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính p ở w=0, rồi dự đoán hai phần tử gradient.
2. **P2** · Dự đoán Hessian và tham số sau một bước. Giải hệ 2×2 bằng tay.

<a id="ml11-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
A = np.array([[1., -1.], [1., 1.]])
y = np.array([0., 1.])
w = np.zeros(2)
p = np.exp(-np.logaddexp(0, -(A @ w)))
g = A.T @ (p - y) / len(y)
H = A.T @ ((p * (1 - p))[:, None] * A) / len(y)
print(g.tolist(), H.tolist())
print((w - np.linalg.solve(H, g)).tolist())
~~~

[Xem kết quả mẫu](#ml11-ket-qua)

<a id="ml11-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Theo dõi p(1−p)[:,None] nhân theo hàng nào. Viết shape của H.
2. **I2** · Giải thích tại sao hai cột giống nhau khiến `solve` không có nghiệm duy nhất.

[Đối chiếu cách giải thích](#ml11-giai-thich)

<a id="ml11-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi nhãn thành [1,0]. Kiểm H như cũ và bước cập nhật đổi dấu.
2. **MO2** · Đặt cột hai bằng cột một. Kiểm hạng H bằng 1 và xử lý `LinAlgError`.
3. **MO3** · Cộng 0.25I vào H gốc trước khi solve. Kiểm bước ra [0,1] và so độ dài với bước gốc.

<a id="ml11-make"></a>

### E · Make 1 · Viết hàm

**`newton_step(A, y, w, damping=0.0)`**

Với design matrix 2D đủ kích thước, y nhị phân, w đúng số cột và damping hữu hạn ≥ 0, trả vector tham số sau một bước theo H+damping·I. Báo ValueError với đầu vào sai. Cho phép LinAlgError nếu hệ suy biến.

Điền hàm. Chạy `python ML11.py`.

[Mã khởi đầu và 4 ca kiểm](#ml11-starter) · [Lời giải](#ml11-loi-giai)

<a id="ml11-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm so một bước Newton với một bước GD lr=1 trên A=[[1,−1],[1,1]], y=[0,1], w=[0,0]. Đối chiếu hệ số mới 2 và 0.5, rồi tính loss sau hai bước riêng.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml11-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml11-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0.0, -0.5] [[0.25, 0.0], [0.0, 0.25]]
[0.0, 2.0]
~~~

</details>

<details class="answer" id="ml11-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

p=[0.5,0.5], g=[0,−0.5], H=0.25I. Vì Δ=[0,−2], tham số mới là [0,2].

</details>

<details class="answer" id="ml11-starter" data-starter="ML11">
<summary>E · Mã khởi đầu và ca kiểm · ML11.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def newton_step(A, y, w, damping=0.0):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(newton_step([[1, -2], [1, 2]], [0, 1], [0, 0]), [0, 1])


def case_02():
    same(newton_step([[1, 1], [1, 1]], [1, 1], [0, 0], 0.5), [0.5, 0.5])


def case_03():
    rejects(newton_step, [[1]], [1], [0], -0.1)


def case_04():
    with np.testing.assert_raises(np.linalg.LinAlgError):
        newton_step([[1, 1], [1, 1]], [0, 1], [0, 0])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml11-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def newton_step(A, y, w, damping=0.0):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    if A.ndim != 2 or min(A.shape) == 0 or y.shape != (len(A),) or w.shape != (A.shape[1],) or not np.isin(y, [0, 1]).all() or not np.isfinite(damping) or damping < 0:
        raise ValueError("Đầu vào không hợp lệ")
    p = np.exp(-np.logaddexp(0, -(A @ w)))
    g = A.T @ (p - y) / len(y)
    H = A.T @ ((p * (1 - p))[:, None] * A) / len(y)
    return w - np.linalg.solve(H + damping * np.eye(len(w)), g)
~~~

</details>

<a id="ml11-on-tap"></a>

### Ôn tập ML11

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML11-mcq-1

f(t)=t²/2 tại t=2 có bước Newton mới là gì?

- **A** · 0
- **B** · 1
- **C** · 4

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

g=2,H=1,t_new=2−2=0.

- **A** · g=2,H=1,t_new=2−2=0.
- **B** · Đó có thể là GD với alpha khác,không phải bước Newton ở đây.
- **C** · Đi sai chiều.

</details>

##### ML11-mcq-2

H là ma trận 3×3 còn g có 2 phần tử. Nên làm gì?

- **A** · Bỏ hàng cuối H
- **B** · Báo sai shape trước giải
- **C** · Tự thêm số 0 vào g

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Gradient và Hessian phải thuộc cùng vector tham số.

- **A** · Tự bỏ tham số.
- **B** · Gradient và Hessian phải thuộc cùng vector tham số.
- **C** · Thay bài toán không có căn cứ.

</details>

##### ML11-mcq-3

Trong logistic Hessian,H=X.T@W@X/m,W nên có shape nào?

- **A** · (d,d)
- **B** · (m,d)
- **C** · (m,m)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mỗi phần tử đường chéo tương ứng một mẫu.

- **A** · W chứa trọng số theo mẫu,không theo tham số.
- **B** · Không phải đường chéo theo mẫu.
- **C** · Mỗi phần tử đường chéo tương ứng một mẫu.

</details>

##### ML11-mcq-4

Bước Newton cho vector theta với gradient g và Hessian H khả nghịch là?

- **A** · theta−solve(H,g)
- **B** · theta−H@g
- **C** · theta+g

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Giải H delta=g, rồi trừ delta khỏi theta.

- **A** · Giải H delta=g, rồi trừ delta khỏi theta.
- **B** · Nhân H không phải áp dụng nghịch đảo Hessian.
- **C** · Đó không phải công thức Newton.

</details>

##### ML11-mcq-5

Theta có d phần tử. Hessian theo theta có shape nào?

- **A** · (m,d)
- **B** · (d,d)
- **C** · (m,)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mỗi cặp tham số có một đạo hàm bậc hai.

- **A** · Đây thường là shape dữ liệu X.
- **B** · Mỗi cặp tham số có một đạo hàm bậc hai.
- **C** · Đây là shape theo mẫu, không phải theo cặp tham số.

</details>

##### ML11-mcq-6

Trong logistic regression, trọng số W_ii của Hessian bằng gì?

- **A** · y_i
- **B** · p_i−y_i
- **C** · p_i(1−p_i)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Đạo hàm sigmoid là p(1−p).

- **A** · Nhãn không phải đạo hàm sigmoid.
- **B** · Đây là residual dùng trong gradient.
- **C** · Đạo hàm sigmoid là p(1−p).

</details>

##### ML11-mcq-7

Hessian suy biến thì có thể cứ gọi inverse để lấy bước Newton chuẩn không?

- **A** · Không; cần xử lý suy biến theo phương pháp đã quy định
- **B** · Có, inverse luôn trả nghiệm chính xác
- **C** · Chỉ cần đổi tên biến H

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Công thức chuẩn cần hệ giải được; không che lỗi bằng kết quả giả.

- **A** · Công thức chuẩn cần hệ giải được; không che lỗi bằng kết quả giả.
- **B** · Inverse không tồn tại khi suy biến.
- **C** · Tên biến không thay tính chất toán học.

</details>

##### ML11-mcq-8

Nếu loss và gradient dùng mean theo m, Hessian logistic nhất quán nên là?

- **A** · X.T@W@X không chia m
- **B** · X.T@W@X/m
- **C** · W@X.T/m

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cả gradient và Hessian đều thuộc cùng mean loss.

- **A** · Thiếu hệ số so với mean gradient.
- **B** · Cả gradient và Hessian đều thuộc cùng mean loss.
- **C** · Thường sai shape và công thức.

</details>

##### ML11-mcq-9

Newton hội tụ bậc hai có phải bảo đảm từ mọi điểm khởi tạo trên mọi hàm không?

- **A** · Có, không cần giả định
- **B** · Có, kể cả Hessian không tồn tại
- **C** · Không; cần điều kiện gần nghiệm và tính trơn/khả nghịch phù hợp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Hành vi cục bộ khác bảo đảm toàn cục.

- **A** · Đó là kết luận quá mức.
- **B** · Phương pháp cần đạo hàm bậc hai phù hợp.
- **C** · Hành vi cục bộ khác bảo đảm toàn cục.

</details>

##### ML11-mcq-10

Trong bài Newton,tại gradient bằng 0 và Hessian khả nghịch,bước delta là gì?

- **A** · Vector 0
- **B** · Vector toàn 1
- **C** · Không thể giải dù H khả nghịch

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Solve(H,0)=0,tham số không đổi.

- **A** · Solve(H,0)=0,tham số không đổi.
- **B** · H delta=0 có nghiệm duy nhất 0.
- **C** · Giả định đã bảo đảm giải được.

</details>

#### Tự luận và viết mã

##### ML11-practice-1

H=[[2,0],[0,4]],g=[2,8]. Tìm delta giải H delta=g.

<details>
<summary>Đáp án và cách kiểm</summary>

Delta=[1,2].

```python
import numpy as np
H=np.diag([2.,4.]);g=np.array([2.,8.])
print(np.linalg.solve(H,g).tolist())
```
Kết quả: [1.0, 2.0]

</details>

##### ML11-practice-2

Theta=[3,5],delta=[1,2]. Tính bước Newton.

<details>
<summary>Đáp án và cách kiểm</summary>

Theta mới=[2,3].

```python
import numpy as np
print((np.array([3.,5.])-np.array([1.,2.])).tolist())
```
Kết quả: [2.0, 3.0]

</details>

##### ML11-practice-3

Với f(t)=(t−3)²/2, tại t=0 tính gradient,Hessian và t mới.

<details>
<summary>Đáp án và cách kiểm</summary>

g=−3,H=1,t_new=0−(−3)/1=3.

```python
t=0.
g=t-3;H=1.
print(g)
print(H)
print(t-g/H)
```
Kết quả: -3.0
1.0
3.0

</details>

##### ML11-practice-4

p=[0.5,0.8]. Tính p(1−p), làm tròn để hiển thị.

<details>
<summary>Đáp án và cách kiểm</summary>

Các trọng số là [0.25,0.16].

```python
import numpy as np
p=np.array([.5,.8])
print(np.round(p*(1-p),4).tolist())
```
Kết quả: [0.25, 0.16]

</details>

##### ML11-practice-5

X=[[1,0],[1,1]],p=[0.5,0.5]. Tính Hessian mean logistic.

<details>
<summary>Đáp án và cách kiểm</summary>

H=[[0.25,0.125],[0.125,0.125]].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);p=np.full(2,.5)
H=X.T@np.diag(p*(1-p))@X/len(p)
print(H.tolist())
```
Kết quả: [[0.25, 0.125], [0.125, 0.125]]

</details>

##### ML11-practice-6

Với X,p trên, y=[0,1],theta=[0,0], tính một bước Newton.

<details>
<summary>Đáp án và cách kiểm</summary>

g=[0,−0.25]; delta=[2,−4]; theta mới=[−2,4].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);p=np.full(2,.5);y=np.array([0.,1.])
g=X.T@(p-y)/2;H=X.T@np.diag(p*(1-p))@X/2
print((-np.linalg.solve(H,g)).tolist())
```
Kết quả: [-2.0, 4.0]

</details>

##### ML11-practice-7

Giải thích vì sao trừ H@g không tương đương trừ solve(H,g).

<details>
<summary>Đáp án và cách kiểm</summary>

Solve tìm delta sao cho H delta=g. Nhân H tạo vector H g khác phép nghịch đảo tác động lên g, trừ những trường hợp đặc biệt.

</details>

##### ML11-practice-8

Nếu theta có 3 phần tử nhưng H shape (2,2), nên làm gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Báo lỗi shape và kiểm lại design matrix/tham số; không cắt theta hoặc thêm số để phép tính chạy.

</details>

##### ML11-practice-9

H=[[1,1],[1,1]] có khả nghịch không? Kiểm rank.

<details>
<summary>Đáp án và cách kiểm</summary>

Rank=1<2 nên suy biến; bước Newton chuẩn không xác định duy nhất bằng inverse.

```python
import numpy as np
print(int(np.linalg.matrix_rank([[1.,1.],[1.,1.]])))
```
Kết quả: 1

</details>

##### ML11-practice-10

Tại p=0.5, trọng số p(1−p) bằng 0.25. Khi p tiến gần 0 hay 1, trọng số thay đổi ra sao?

<details>
<summary>Đáp án và cách kiểm</summary>

Tiến gần 0. Điều này có thể làm độ cong nhỏ và hệ Newton khó giải hơn; không mặc định H luôn ổn định.

</details>

##### ML11-practice-11

Vì sao nên giữ gradient và Hessian cùng quy ước tổng hoặc trung bình?

<details>
<summary>Đáp án và cách kiểm</summary>

Chúng phải là đạo hàm của cùng một loss. Chia m cho chỉ một trong hai làm tỷ lệ bước Newton sai.

</details>

##### ML11-practice-12

Kiểm chứng H delta=g sau khi giải với H=[[2,1],[1,3]],g=[1,2].

<details>
<summary>Đáp án và cách kiểm</summary>

Dùng allclose kiểm phần dư thay vì so chuỗi số thực.

```python
import numpy as np
H=np.array([[2.,1.],[1.,3.]]);g=np.array([1.,2.])
delta=np.linalg.solve(H,g)
print(bool(np.allclose(H@delta,g)))
```
Kết quả: True

</details>

<a id="ml12"></a>

## ML12 · Phân loại bằng k-NN từ khoảng cách và biểu quyết láng giềng

[Mục lục](#muc-luc) · M3 · Phân loại và tối ưu bậc hai · Tiên quyết [ML01](#ml01)

<a id="ml12-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Chọn k mẫu có khoảng cách nhỏ nhất rồi biểu quyết nhãn. Quy định trước cách xử lý hòa để lần chạy sau cho cùng kết quả.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính bốn khoảng cách bình phương và chỉ số ba láng giềng.
2. **P2** · Đếm phiếu của từng nhãn, rồi dự đoán kết quả cho k=3 và k=1.

<a id="ml12-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0., 0.], [2., 1.], [3., 0.], [1., 4.]])
y = np.array([0, 1, 1, 0])
q = np.array([1., 1.])
d2 = ((X - q)**2).sum(axis=1)
near = np.argsort(d2, kind="stable")[:3]
print(d2.tolist(), near.tolist())
print(int(np.bincount(y[near]).argmax()))
~~~

[Xem kết quả mẫu](#ml12-ket-qua)

<a id="ml12-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao dùng d² cho thứ tự Euclid giống dùng căn bậc hai.
2. **I2** · Xác định quy tắc hòa của stable sort và argmax. Hai quy tắc giải quyết hai loại hòa nào?

[Đối chiếu cách giải thích](#ml12-giai-thich)

<a id="ml12-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi k=4. Kiểm hòa phiếu và nhãn 0.
2. **MO2** · Thay Euclid bằng Manhattan. Kiểm hai mẫu cuối cùng có khoảng cách cùng bằng 3.
3. **MO3** · Nhân tọa độ thứ hai của X và q với 10. Đổi k=1, dự đoán trước rồi kiểm điểm [2,1] gần nhất.

<a id="ml12-make"></a>

### E · Make 1 · Viết hàm

**`knn_one(X, y, q, k)`**

Nhận X ma trận n×d, q vector d, y vector nhãn nguyên 0/1 và k nguyên trong [1,n]. Dùng Euclid, hòa khoảng cách lấy chỉ số trước, hòa phiếu lấy 0. Báo ValueError nếu shape, nhãn hoặc k sai.

Điền hàm. Chạy `python ML12.py`.

[Mã khởi đầu và 4 ca kiểm](#ml12-starter) · [Lời giải](#ml12-loi-giai)

<a id="ml12-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết k-NN có trọng số 1/(d+1) cho nhãn 0/1. Với X=[[0],[4],[5]], y=[1,0,0], q=[0], k=3, kiểm nhãn có trọng số là 1 dù đa số thường là 0.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml12-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml12-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2.0, 1.0, 5.0, 9.0] [1, 0, 2]
1
~~~

</details>

<details class="answer" id="ml12-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

d²=[2,1,5,9]. Ba chỉ số theo độ gần [1,0,2]. k=3 có 2 phiếu lớp 1 và 1 phiếu lớp 0. k=1 cũng ra 1.

</details>

<details class="answer" id="ml12-starter" data-starter="ML12">
<summary>E · Mã khởi đầu và ca kiểm · ML12.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def knn_one(X, y, q, k):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(knn_one([[0], [1], [9]], [0, 1, 1], [0.9], 1), 1)


def case_02():
    same(knn_one([[1], [-1]], [1, 0], [0], 1), 1)


def case_03():
    same(knn_one([[1], [-1]], [1, 0], [0], 2), 0)


def case_04():
    rejects(knn_one, [[1]], [0], [1], 2)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml12-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def knn_one(X, y, q, k):
    X, q, y = np.asarray(X, dtype=float), np.asarray(q, dtype=float), np.asarray(y)
    if X.ndim != 2 or X.shape[1] == 0 or q.shape != (X.shape[1],) or y.shape != (len(X),) or not np.isin(y, [0, 1]).all() or not isinstance(k, (int, np.integer)) or not 1 <= k <= len(X):
        raise ValueError("Đầu vào không hợp lệ")
    d2 = ((X - q) ** 2).sum(axis=1)
    near = np.argsort(d2, kind="stable")[:k]
    return int(2 * y[near].sum() > k)
~~~

</details>

<a id="ml12-on-tap"></a>

### Ôn tập ML12

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML12-mcq-1

k-NN được gọi lazy learning chủ yếu vì sao?

- **A** · Phần lớn tính khoảng cách được thực hiện lúc truy vấn
- **B** · Không cần dữ liệu train
- **C** · Không cần kiểm tra input

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Không fit một bộ hệ số cố định như hồi quy tuyến tính chuẩn.

- **A** · Không fit một bộ hệ số cố định như hồi quy tuyến tính chuẩn.
- **B** · Cần đặc trưng và nhãn train.
- **C** · Vẫn cần shape,k và miền dữ liệu hợp lệ.

</details>

##### ML12-mcq-2

Dự đoán k=1 tại một điểm train có nhãn duy nhất và không có điểm trùng trái nhãn thường ra gì?

- **A** · Mean mọi nhãn train
- **B** · Nhãn của điểm đó
- **C** · Luôn lớp 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Khoảng cách tới chính điểm đó bằng 0.

- **A** · Đó không phải 1-NN.
- **B** · Khoảng cách tới chính điểm đó bằng 0.
- **C** · Không phụ thuộc quy tắc này.

</details>

##### ML12-mcq-3

Với vector d chiều,khoảng cách Manhattan được tính thế nào?

- **A** · Căn tổng sai lệch bình phương
- **B** · Tổng sai lệch có dấu
- **C** · Tổng trị tuyệt đối sai lệch tọa độ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

L1 cộng |x_j−z_j|.

- **A** · Đó là Euclid.
- **B** · Có thể triệt tiêu dù hai vector khác nhau.
- **C** · L1 cộng |x_j−z_j|.

</details>

##### ML12-mcq-4

Khoảng cách Euclid giữa (0,0) và (3,4) là?

- **A** · 7
- **B** · 5
- **C** · 25

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

sqrt(9+16)=5.

- **A** · 7 là khoảng cách Manhattan.
- **B** · sqrt(9+16)=5.
- **C** · 25 là bình phương khoảng cách.

</details>

##### ML12-mcq-5

Với k=3, nhãn ba láng giềng là [1,0,1]. Dự đoán biểu quyết đa số là?

- **A** · 1
- **B** · 0
- **C** · Không thể xác định

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Lớp 1 có hai phiếu, lớp 0 có một phiếu.

- **A** · Lớp 1 có hai phiếu, lớp 0 có một phiếu.
- **B** · Lớp 0 không chiếm đa số.
- **C** · Không có hòa phiếu ở ví dụ nhị phân này.

</details>

##### ML12-mcq-6

Khi hai đặc trưng có thang đo rất khác nhau, khoảng cách k-NN có thể ra sao?

- **A** · Tự động không đổi theo đơn vị
- **B** · Luôn bằng 0
- **C** · Bị đặc trưng thang đo lớn chi phối

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Scaling có thể cần thiết; thống kê scaling phải học từ train.

- **A** · Đổi đơn vị có thể thay thứ tự láng giềng.
- **B** · Thang đo không khiến mọi điểm trùng nhau.
- **C** · Scaling có thể cần thiết; thống kê scaling phải học từ train.

</details>

##### ML12-mcq-7

Nếu k lớn hơn số mẫu train thì nên xử lý thế nào trong bài có hợp đồng 1≤k≤n?

- **A** · Báo input không hợp lệ
- **B** · Nhân bản mẫu train để đủ k
- **C** · Dùng nhãn test để đủ k

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đó là vi phạm hợp đồng; không âm thầm sửa dữ liệu.

- **A** · Đó là vi phạm hợp đồng; không âm thầm sửa dữ liệu.
- **B** · Nhân bản thay đổi biểu quyết.
- **C** · Dùng nhãn test gây leakage.

</details>

##### ML12-mcq-8

Trong k-NN, thông tin nào cần dùng khi dự đoán một mẫu mới?

- **A** · Chỉ nhãn thật của mẫu mới
- **B** · Đặc trưng và nhãn của train, cùng đặc trưng mẫu mới
- **C** · Chỉ chỉ số thứ tự của mẫu mới

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tính khoảng cách rồi biểu quyết nhãn các láng giềng train.

- **A** · Nhãn thật mẫu mới chưa biết và không được dùng để dự đoán.
- **B** · Tính khoảng cách rồi biểu quyết nhãn các láng giềng train.
- **C** · Chỉ số không thay thế dữ liệu thuộc tính.

</details>

##### ML12-mcq-9

Hai lớp hòa phiếu khi k=4. Điều gì cần có để kết quả tái lập?

- **A** · Giấu tình huống này khỏi test
- **B** · Luôn trả lớp của test
- **C** · Quy tắc phá hòa được công bố

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Có thể chọn lớp theo quy tắc cố định; phải ghi rõ và kiểm thử.

- **A** · Test phải kiểm hành vi đã định nghĩa.
- **B** · Dùng nhãn test là sai quy trình.
- **C** · Có thể chọn lớp theo quy tắc cố định; phải ghi rõ và kiểm thử.

</details>

##### ML12-mcq-10

Khoảng cách Euclid giữa hai vector giống hệt nhau bằng gì?

- **A** · 0
- **B** · 1
- **C** · Không xác định

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tổng bình phương mọi sai lệch bằng 0.

- **A** · Tổng bình phương mọi sai lệch bằng 0.
- **B** · Không có sai lệch tọa độ.
- **C** · Công thức xác định trên dữ liệu hữu hạn.

</details>

#### Tự luận và viết mã

##### ML12-practice-1

Tính khoảng cách Euclid giữa (1,2) và (4,6).

<details>
<summary>Đáp án và cách kiểm</summary>

sqrt((4−1)²+(6−2)²)=5.

```python
import numpy as np
x=np.array([1.,2.]);z=np.array([4.,6.])
print(float(np.sqrt(np.sum((x-z)**2))))
```
Kết quả: 5.0

</details>

##### ML12-practice-2

Tính Manhattan giữa (1,2) và (4,6).

<details>
<summary>Đáp án và cách kiểm</summary>

|4−1|+|6−2|=7.

```python
import numpy as np
print(float(np.abs(np.array([1.,2.])-np.array([4.,6.])).sum()))
```
Kết quả: 7.0

</details>

##### ML12-practice-3

Train một chiều [0,3,8], truy vấn 2. Nêu khoảng cách và chỉ số gần nhất.

<details>
<summary>Đáp án và cách kiểm</summary>

Khoảng cách [2,1,6]; chỉ số 1 gần nhất.

```python
import numpy as np
X=np.array([0.,3.,8.]);d=np.abs(X-2.)
print(d.tolist())
print(int(np.argmin(d)))
```
Kết quả: [2.0, 1.0, 6.0]
1

</details>

##### ML12-practice-4

Train X=[0,3,8],y=[0,1,0],query=2,k=1. Dự đoán là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Điểm 3 gần nhất, nhãn 1; dự đoán 1.

</details>

##### ML12-practice-5

Ba láng giềng có nhãn [0,1,1]. Tính số phiếu và dự đoán.

<details>
<summary>Đáp án và cách kiểm</summary>

Lớp 0: một phiếu, lớp 1: hai phiếu, dự đoán 1.

```python
labels=[0,1,1]
print(labels.count(0))
print(labels.count(1))
```
Kết quả: 1
2

</details>

##### ML12-practice-6

Khoảng cách [0.4,0.1,0.7,0.2],k=2. Chọn chỉ số hai láng giềng.

<details>
<summary>Đáp án và cách kiểm</summary>

Chỉ số [1,3], tương ứng 0.1 và 0.2.

```python
import numpy as np
d=np.array([.4,.1,.7,.2])
print(np.argsort(d)[:2].tolist())
```
Kết quả: [1, 3]

</details>

##### ML12-practice-7

Vì sao cần cùng thứ tự cột giữa train và query?

<details>
<summary>Đáp án và cách kiểm</summary>

Khoảng cách phải trừ các thuộc tính tương ứng; đảo cột có thể so x₁ của train với x₂ của query dù shape vẫn hợp lệ.

</details>

##### ML12-practice-8

Nêu nguy cơ dùng k=1 với dữ liệu có điểm nhiễu.

<details>
<summary>Đáp án và cách kiểm</summary>

Một nhãn nhiễu gần query có thể quyết định hoàn toàn dự đoán. Không kết luận k lớn hơn luôn tốt; cần quy trình chọn k và đánh giá phù hợp.

</details>

##### ML12-practice-9

Với k=4,nhãn [0,1,0,1], áp dụng quy tắc hòa chọn lớp số nhỏ hơn.

<details>
<summary>Đáp án và cách kiểm</summary>

Hai phiếu mỗi lớp; theo quy tắc đã cho, dự đoán 0. Đây là quy ước bài tập chứ không phải mọi k-NN đều dùng như vậy.

</details>

##### ML12-practice-10

Hai điểm train cách query bằng nhau, chỉ được lấy một điểm. Vì sao cần quy tắc thứ tự?

<details>
<summary>Đáp án và cách kiểm</summary>

Nếu cắt top-k tại khoảng cách hòa thì lựa chọn có thể phụ thuộc thứ tự sort. Cần quy tắc xác định, chẳng hạn khoảng cách rồi chỉ số train.

</details>

##### ML12-practice-11

Vì sao không dùng query label để chọn metric Euclid hay Manhattan?

<details>
<summary>Đáp án và cách kiểm</summary>

Nhãn thật của dữ liệu đánh giá không được tham gia lựa chọn cách dự đoán; nếu chọn theo test label thì đánh giá bị leakage.

</details>

##### ML12-practice-12

Query=[0,0], train=[[1,0],[0,2],[3,4]]. Tính vector khoảng cách Euclid.

<details>
<summary>Đáp án và cách kiểm</summary>

Các khoảng cách [1,2,5].

```python
import numpy as np
X=np.array([[1.,0.],[0.,2.],[3.,4.]])
print(np.sqrt(np.sum(X**2,axis=1)).tolist())
```
Kết quả: [1.0, 2.0, 5.0]

</details>

<a id="ml13"></a>

## ML13 · Tổ chức train/validation/test và thực hiện K-fold/LOOCV đúng vai trò

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML04](#ml04)

<a id="ml13-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Trong K-fold, mỗi mẫu làm validation đúng một lần. Fit bộ chuẩn hóa và mô hình riêng trong từng fold. Giữ test ngoài vòng chọn mô hình.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Viết danh sách validation của ba fold. Fold nào chỉ có một mẫu?
2. **P2** · Dự đoán train fold thứ hai và tổng số lượt validation trên cả vòng.

<a id="ml13-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
indices = np.array([4, 0, 2, 1, 3])
folds = np.array_split(indices, 3)
for i, valid in enumerate(folds):
    train = np.concatenate([fold for j, fold in enumerate(folds) if i != j])
    print(train.tolist(), valid.tolist())
~~~

[Xem kết quả mẫu](#ml13-ket-qua)

<a id="ml13-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Đối chiếu train ∩ valid trong mỗi fold. Chỉ ra chỗ khiến mỗi chỉ số chỉ làm validation một lần.
2. **I2** · Mô tả vị trí fit scaler trong vòng lặp. Phân biệt việc chọn tham số bằng CV với đánh giá test cuối.

[Đối chiếu cách giải thích](#ml13-giai-thich)

<a id="ml13-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi K=5. Kiểm mỗi fold validation có một mẫu, tức LOOCV.
2. **MO2** · Đổi K=2. Kiểm kích thước validation 3 và 2 với thứ tự như cũ.
3. **MO3** · Tính ba validation mean cho y=[0,10,20,30,40]. So trung bình ba mean với trung bình có trọng số theo số mẫu.

<a id="ml13-make"></a>

### E · Make 1 · Viết hàm

**`kfold_indices(order, k)`**

order là list hoán vị 0..n−1, k nguyên trong [2,n]. Trả list (train, valid), mỗi phần là list chỉ số theo order. Khi n không chia hết, các fold valid đầu có thêm một mẫu. Báo ValueError nếu k hoặc order sai.

Điền hàm. Chạy `python ML13.py`.

[Mã khởi đầu và 4 ca kiểm](#ml13-starter) · [Lời giải](#ml13-loi-giai)

<a id="ml13-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết CV cho baseline luôn dự đoán trung bình y_train. Với y=[0,2,4,6], order=[0,1,2,3] và K=2, kiểm MAE validation của mỗi fold bằng 4.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml13-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml13-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2, 1, 3] [4, 0]
[4, 0, 3] [2, 1]
[4, 0, 2, 1] [3]
~~~

</details>

<details class="answer" id="ml13-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Validation lần lượt [4,0], [2,1], [3]. Train fold thứ hai là [4,0,3]. Có 5 lượt validation, mỗi chỉ số xuất hiện đúng một lần.

</details>

<details class="answer" id="ml13-starter" data-starter="ML13">
<summary>E · Mã khởi đầu và ca kiểm · ML13.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def kfold_indices(order, k):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    assert kfold_indices([2, 0, 1], 2) == [([1], [2, 0]), ([2, 0], [1])]


def case_02():
    assert kfold_indices([1, 0], 2) == [([0], [1]), ([1], [0])]


def case_03():
    rejects(kfold_indices, [0, 0], 2)


def case_04():
    rejects(kfold_indices, [0, 1], 3)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml13-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def kfold_indices(order, k):
    if not isinstance(k, (int, np.integer)) or not 2 <= k <= len(order) or sorted(order) != list(range(len(order))):
        raise ValueError("Số fold hoặc hoán vị không hợp lệ")
    folds = [fold.tolist() for fold in np.array_split(order, k)]
    splits = []
    for i, valid in enumerate(folds):
        train = [index for j, fold in enumerate(folds) if i != j for index in fold]
        splits.append((train, valid))
    return splits
~~~

</details>

<a id="ml13-on-tap"></a>

### Ôn tập ML13

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML13-mcq-1

K=5 trên 25 mẫu chia đều,mỗi mẫu thuộc validation bao nhiêu lần trong một lượt CV?

- **A** · Một
- **B** · Năm
- **C** · Không lần nào

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Các fold validation phân hoạch tập dữ liệu.

- **A** · Các fold validation phân hoạch tập dữ liệu.
- **B** · Năm là số fold toàn lượt,không phải số lần mỗi mẫu giữ lại.
- **C** · Mỗi mẫu phải có lượt được đánh giá ngoài train fold.

</details>

##### ML13-mcq-2

Đặc trưng cùng một người xuất hiện ở train và validation có thể gây gì?

- **A** · Tự tăng số feature
- **B** · Đánh giá lạc quan nếu mục tiêu là tổng quát sang người mới
- **C** · Bảo đảm dữ liệu độc lập

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cách chia cần phù hợp đơn vị tổng quát hóa.

- **A** · Không liên quan số cột.
- **B** · Cách chia cần phù hợp đơn vị tổng quát hóa.
- **C** · Cùng thực thể có thể chia sẻ thông tin.

</details>

##### ML13-mcq-3

Sau khi chọn cấu hình bằng CV,có thể fit lại trên toàn phần train ban đầu trước test riêng không?

- **A** · Không,chỉ được giữ model fold cuối
- **B** · Có và dùng thêm nhãn test để fit
- **C** · Có,theo quy trình đã chốt

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

CV chọn cấu hình;fit cuối dùng phần dữ liệu huấn luyện được phép.

- **A** · Model fold cuối không bắt buộc là model cuối.
- **B** · Test vẫn phải giữ riêng.
- **C** · CV chọn cấu hình;fit cuối dùng phần dữ liệu huấn luyện được phép.

</details>

##### ML13-mcq-4

Vai trò chính của tập test riêng là gì?

- **A** · Chọn mọi hyperparameter bằng cách thử lặp lại
- **B** · Ước lượng hiệu năng sau khi đã chốt lựa chọn mô hình
- **C** · Thay tập train để tính gradient

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Test được giữ riêng để đánh giá cuối theo quy trình đã định.

- **A** · Thử chọn trên test làm test tham gia tối ưu.
- **B** · Test được giữ riêng để đánh giá cuối theo quy trình đã định.
- **C** · Gradient học từ train, không từ test.

</details>

##### ML13-mcq-5

Trong K-fold, mỗi fold đánh giá cần mô hình khởi tạo/huấn luyện thế nào?

- **A** · Huấn luyện độc lập từ dữ liệu train của fold đó
- **B** · Kế thừa trọng số đã học trên toàn bộ dữ liệu
- **C** · Chỉ dự đoán từ model fold đầu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Không mang thông tin fold validation sang lần huấn luyện khác.

- **A** · Không mang thông tin fold validation sang lần huấn luyện khác.
- **B** · Đã học dữ liệu validation của fold sẽ gây leakage.
- **C** · Mỗi fold có train khác nhau, phải fit lại.

</details>

##### ML13-mcq-6

Có 12 mẫu và K=3 chia đều. Mỗi lần dùng bao nhiêu mẫu train/validation?

- **A** · 4 train,8 validation
- **B** · 12 train,4 validation
- **C** · 8 train,4 validation

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Một phần ba giữ lại, hai phần ba dùng train.

- **A** · Đảo vai trò phần giữ lại và phần gộp.
- **B** · Validation không đồng thời nằm trong train của cùng fold.
- **C** · Một phần ba giữ lại, hai phần ba dùng train.

</details>

##### ML13-mcq-7

Scaler trong một fold cần fit ở đâu?

- **A** · Chỉ train của fold
- **B** · Toàn bộ dữ liệu trước khi chia fold
- **C** · Validation của fold

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Sau đó dùng thống kê ấy biến đổi train và validation.

- **A** · Sau đó dùng thống kê ấy biến đổi train và validation.
- **B** · Thông tin validation tham gia thống kê.
- **C** · Không học bước tiền xử lý từ validation.

</details>

##### ML13-mcq-8

LOOCV với n mẫu có bao nhiêu lần fit theo quy trình chuẩn?

- **A** · 1
- **B** · n
- **C** · n−1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mỗi lượt giữ một mẫu, tổng cộng n lượt.

- **A** · Một lần fit không đủ n lượt giữ một mẫu.
- **B** · Mỗi lượt giữ một mẫu, tổng cộng n lượt.
- **C** · n−1 là số mẫu train mỗi lượt.

</details>

##### ML13-mcq-9

K-fold trên train ban đầu có khiến test riêng không còn cần được giữ độc lập không?

- **A** · Có, có thể dùng test để chọn fold tốt nhất
- **B** · Có, gộp mọi nhãn test vào train ngay khi chọn K
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cross-validation dùng để chọn mô hình trong vùng train; test riêng vẫn giữ vai trò cuối.

- **A** · Chọn theo test vẫn gây leakage.
- **B** · Chưa hoàn tất đánh giá mà dùng test để học làm sai vai trò.
- **C** · Cross-validation dùng để chọn mô hình trong vùng train; test riêng vẫn giữ vai trò cuối.

</details>

##### ML13-mcq-10

Có 10 mẫu,K=3 thì bắt buộc mọi fold phải có đúng 10/3 mẫu không?

- **A** · Không,kích thước phải nguyên và có thể lệch một mẫu
- **B** · Có,dùng số mẫu lẻ
- **C** · Không thể dùng K-fold khi n không chia hết K

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Ví dụ các kích thước 4,3,3 giữ đủ dữ liệu.

- **A** · Ví dụ các kích thước 4,3,3 giữ đủ dữ liệu.
- **B** · Không thể có một phần mẫu.
- **C** · Có thể chia fold gần đều.

</details>

#### Tự luận và viết mã

##### ML13-practice-1

Có 20 mẫu,giữ 5 mẫu test riêng. Còn bao nhiêu mẫu cho train/validation và lựa chọn mô hình?

<details>
<summary>Đáp án và cách kiểm</summary>

Còn 15 mẫu; 5 mẫu test không tham gia bước lựa chọn.

```python
print(20-5)
```
Kết quả: 15

</details>

##### ML13-practice-2

Với 12 mẫu,K=3 chia đều, liệt kê ba tập validation liên tiếp theo chỉ số.

<details>
<summary>Đáp án và cách kiểm</summary>

[0,1,2,3],[4,5,6,7],[8,9,10,11]. Đây chỉ là ví dụ minh họa cách chia, chưa phải khuyến nghị bỏ shuffle cho mọi dữ liệu.

```python
indices=list(range(12))
print([indices[i:i+4] for i in range(0,12,4)])
```
Kết quả: [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

</details>

##### ML13-practice-3

Validation có chỉ số [0,1] trong tập [0,1,2,3,4,5]. Tìm train indices.

<details>
<summary>Đáp án và cách kiểm</summary>

Train=[2,3,4,5], không có giao với validation.

```python
all_idx=list(range(6));val={0,1}
print([i for i in all_idx if i not in val])
```
Kết quả: [2, 3, 4, 5]

</details>

##### ML13-practice-4

Ba fold có validation MSE bằng 1,2,3 và cùng kích thước. Tính trung bình.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=2. Không gọi đây là test MSE của một test set riêng.

```python
scores=[1.,2.,3.]
print(sum(scores)/len(scores))
```
Kết quả: 2.0

</details>

##### ML13-practice-5

LOOCV với 5 mẫu: mỗi lượt train bao nhiêu mẫu, tổng bao nhiêu lần fit?

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi lượt train 4 mẫu và validation 1 mẫu; tổng cộng 5 lần fit.

</details>

##### ML13-practice-6

Một chương trình fit model trên toàn bộ dữ liệu rồi mới chia K fold để dự đoán. Vì sao đánh giá sai?

<details>
<summary>Đáp án và cách kiểm</summary>

Mô hình đã thấy các mẫu gọi là validation. Đổi chỉ số khi dự đoán không xóa thông tin đã học; phải fit độc lập theo train từng fold.

</details>

##### ML13-practice-7

Train fold=[10,20],validation=[30]. Tính Min–Max đúng cho validation.

<details>
<summary>Đáp án và cách kiểm</summary>

Dùng lo=10,hi=20 từ train fold; kết quả 2.0.

```python
train=[10.,20.];value=30.
print((value-min(train))/(max(train)-min(train)))
```
Kết quả: 2.0

</details>

##### ML13-practice-8

Vì sao mang trọng số model fold trước sang fold sau có thể làm leakage?

<details>
<summary>Đáp án và cách kiểm</summary>

Validation fold sau có thể từng nằm trong train fold trước. Trọng số đã mang thông tin đó, nên fold sau không còn đánh giá từ một lần fit độc lập.

</details>

##### ML13-practice-9

Năm fold validation có một mẫu bị xuất hiện hai lần và một mẫu không xuất hiện. Có đạt phân hoạch K-fold thông thường không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Mỗi mẫu phải thuộc validation đúng một lần trong một lượt K-fold; cần kiểm trùng và thiếu chỉ số.

</details>

##### ML13-practice-10

Kiểm tra coverage của các fold [[0,1],[2,3],[4,5]].

<details>
<summary>Đáp án và cách kiểm</summary>

Ghép lại có đủ sáu chỉ số và không trùng.

```python
folds=[[0,1],[2,3],[4,5]]
flat=[i for f in folds for i in f]
print(sorted(flat)==list(range(6)) and len(flat)==len(set(flat)))
```
Kết quả: True

</details>

##### ML13-practice-11

Tại sao không chỉ chọn mô hình có điểm tốt nhất trên một fold riêng lẻ?

<details>
<summary>Đáp án và cách kiểm</summary>

Điểm một fold có thể phụ thuộc cách chia; cần tổng hợp theo quy trình CV thay vì chọn lần chia may mắn. Sau lựa chọn thường fit lại trên phần train cho phép và đánh giá test riêng.

</details>

##### ML13-practice-12

Một ca fold có train rỗng khi K=1. Cần xử lý thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

K-fold thông thường cần ít nhất 2 fold và đủ dữ liệu; phải từ chối K không hợp lệ trước khi fit, không biến lỗi môi trường này thành điểm đánh giá.

</details>

<a id="ml14"></a>

## ML14 · Tính và diễn giải MAE, MSE, RMSE và R²

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML04](#ml04)

<a id="ml14-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tính MAE từ sai số tuyệt đối, MSE từ sai số bình phương và RMSE từ căn của MSE. R² so SSE của mô hình với SSE khi dự đoán bằng trung bình y.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính residual, MAE và MSE dưới dạng phân số.
2. **P2** · Tính SSE, SST và R². Dự đoán RMSE nằm giữa 1 và 2 hay ngoài khoảng.

<a id="ml14-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
y = np.array([0., 2., 4.])
yhat = np.array([0., 1., 6.])
e = yhat - y
mse = np.mean(e**2)
r2 = 1 - np.sum(e**2) / np.sum((y - y.mean())**2)
print(e.tolist())
print(np.round([np.abs(e).mean(), mse, np.sqrt(mse), r2], 6).tolist())
~~~

[Xem kết quả mẫu](#ml14-ket-qua)

<a id="ml14-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Chỉ ra mẫu đóng góp mạnh nhất vào SSE. So đơn vị của MAE, RMSE và MSE.
2. **I2** · Giải thích r2 dương, bằng 0 hoặc âm dựa vào SSE so với SST.

[Đối chiếu cách giải thích](#ml14-giai-thich)

<a id="ml14-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đặt yhat bằng y. Kiểm 3 lỗi bằng 0 và R²=1.
2. **MO2** · Dự đoán hằng y.mean(). Kiểm R²=0. Đổi hằng thành 10 và kiểm R² âm.
3. **MO3** · Dùng y=[2,2,2]. In SST rồi bổ sung quy ước trả None cho R² khi SST=0.

<a id="ml14-make"></a>

### E · Make 1 · Viết hàm

**`regression_metrics(y, yhat)`**

Hai vector số cùng độ dài dương. Trả tuple (MAE, MSE, RMSE, R²). Dùng None cho R² nếu y hằng. Báo ValueError khi shape sai.

Điền hàm. Chạy `python ML14.py`.

[Mã khởi đầu và 4 ca kiểm](#ml14-starter) · [Lời giải](#ml14-loi-giai)

<a id="ml14-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm chọn giữa hai vector dự đoán theo MAE hoặc MSE. Với y=[0,0,0], A=[0,0,6], B=[3,3,3], kiểm MAE chọn A và MSE chọn B.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml14-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml14-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0.0, -1.0, 2.0]
[1.0, 1.666667, 1.290994, 0.375]
~~~

</details>

<details class="answer" id="ml14-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Residual [0,−1,2], MAE=1, MSE=5/3, RMSE=√(5/3), SSE=5, SST=8 và R²=3/8.

</details>

<details class="answer" id="ml14-starter" data-starter="ML14">
<summary>E · Mã khởi đầu và ca kiểm · ML14.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def regression_metrics(y, yhat):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(regression_metrics([1, 3], [1, 5]), [1, 2, np.sqrt(2), -1])


def case_02():
    assert regression_metrics([2, 2], [2, 2]) == (0, 0, 0, None)


def case_03():
    same(regression_metrics([0, 2], [1, 1]), [1, 1, 1, 0])


def case_04():
    rejects(regression_metrics, [], [])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml14-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def regression_metrics(y, yhat):
    y, yhat = np.asarray(y, dtype=float), np.asarray(yhat, dtype=float)
    if y.ndim != 1 or y.size == 0 or y.shape != yhat.shape:
        raise ValueError("Cần hai vector cùng độ dài dương")
    e = yhat - y
    mse = np.mean(e ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    r2 = None if sst == 0 else float(1 - np.sum(e ** 2) / sst)
    return float(np.abs(e).mean()), float(mse), float(np.sqrt(mse)), r2
~~~

</details>

<a id="ml14-on-tap"></a>

### Ôn tập ML14

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML14-mcq-1

Residual [0,0] trên tập có nhãn biến thiên cho RMSE bao nhiêu?

- **A** · 0
- **B** · 1
- **C** · Không xác định dù có hai mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mean bình phương 0 rồi căn bằng 0.

- **A** · Mean bình phương 0 rồi căn bằng 0.
- **B** · Không có sai lệch.
- **C** · RMSE vẫn xác định.

</details>

##### ML14-mcq-2

Với cùng tập dữ liệu,RMSE có thể nhỏ hơn MAE không theo công thức chuẩn?

- **A** · Không thể so vì khác đơn vị
- **B** · Không,trừ sai số số học
- **C** · Luôn nhỏ hơn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Bất đẳng thức RMS≥AM áp dụng trên |residual|.

- **A** · Cả hai cùng đơn vị y.
- **B** · Bất đẳng thức RMS≥AM áp dụng trên |residual|.
- **C** · RMS không nhỏ hơn mean trị tuyệt đối.

</details>

##### ML14-mcq-3

Báo MSE=9 có đồng nghĩa mọi residual đều bằng 3 không?

- **A** · Có vì căn MSE=3
- **B** · Chỉ khi số mẫu chẵn
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Nhiều phân bố residual khác nhau có cùng mean bình phương.

- **A** · RMSE là đại lượng tổng hợp,không phải từng residual.
- **B** · Chẵn lẻ không quyết định.
- **C** · Nhiều phân bố residual khác nhau có cùng mean bình phương.

</details>

##### ML14-mcq-4

Residual là [−2,2]. MAE bằng bao nhiêu?

- **A** · 0
- **B** · 2
- **C** · 4

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mean(|e|)=(2+2)/2=2.

- **A** · Hai dấu không được triệt tiêu trong trị tuyệt đối.
- **B** · Mean(|e|)=(2+2)/2=2.
- **C** · 4 là MSE của ví dụ.

</details>

##### ML14-mcq-5

Residual [−2,2] có MSE và RMSE là gì?

- **A** · MSE=4,RMSE=2
- **B** · MSE=2,RMSE=4
- **C** · Cả hai bằng 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mean bình phương=4, căn bậc hai=2.

- **A** · Mean bình phương=4, căn bậc hai=2.
- **B** · Đã đảo và tính sai công thức.
- **C** · Residual trái dấu không triệt tiêu sau bình phương.

</details>

##### ML14-mcq-6

Nếu đại lượng y được đo theo đơn vị u, RMSE có đơn vị nào?

- **A** · u²
- **B** · Không có đơn vị
- **C** · u

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Lấy căn MSE đưa đơn vị về cùng y.

- **A** · Đó là đơn vị MSE.
- **B** · RMSE vẫn mang đơn vị của nhãn.
- **C** · Lấy căn MSE đưa đơn vị về cùng y.

</details>

##### ML14-mcq-7

R² âm có thể xảy ra khi nào trên tập đánh giá có SST>0?

- **A** · SSE của model lớn hơn SST của dự đoán hằng mean y
- **B** · Không bao giờ vì R² là bình phương
- **C** · Chỉ khi số mẫu âm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

R²=1−SSE/SST nên có thể âm.

- **A** · R²=1−SSE/SST nên có thể âm.
- **B** · Tên R² không bảo đảm không âm trong đánh giá dự đoán.
- **C** · Số mẫu không âm và không liên quan lập luận này.

</details>

##### ML14-mcq-8

Nếu mọi nhãn thật bằng nhau, công thức R²=1−SSE/SST gặp gì?

- **A** · Luôn trả 1
- **B** · SST=0 nên cần quy định hành vi
- **C** · Luôn trả 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Phải nêu quy ước hoặc báo không xác định.

- **A** · Trường hợp 0/0 chưa tự xác định là 1.
- **B** · Phải nêu quy ước hoặc báo không xác định.
- **C** · Không được tự gán 0 nếu chưa định nghĩa.

</details>

##### ML14-mcq-9

So với MAE, MSE nhấn mạnh residual lớn hơn vì sao?

- **A** · Vì bỏ mọi residual nhỏ
- **B** · Vì chỉ đếm dấu residual
- **C** · Vì bình phương làm đóng góp tăng nhanh theo độ lớn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Sai lệch gấp đôi góp bình phương gấp bốn.

- **A** · MSE vẫn dùng mọi residual.
- **B** · MSE không giữ dấu sau bình phương.
- **C** · Sai lệch gấp đôi góp bình phương gấp bốn.

</details>

##### ML14-mcq-10

Nếu residual mọi mẫu đều bằng 2 thì MAE,MSE,RMSE lần lượt là gì?

- **A** · 2,4,2
- **B** · 2,2,2
- **C** · 0,4,2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Các trung bình của giá trị hằng giữ đúng công thức.

- **A** · Các trung bình của giá trị hằng giữ đúng công thức.
- **B** · MSE bình phương nên bằng 4.
- **C** · Trị tuyệt đối residual không bằng 0.

</details>

#### Tự luận và viết mã

##### ML14-practice-1

y=[1,3],pred=[2,1]. Tính residual theo pred−y.

<details>
<summary>Đáp án và cách kiểm</summary>

Residual=[1,−2].

```python
import numpy as np
y=np.array([1.,3.]);pred=np.array([2.,1.])
print((pred-y).tolist())
```
Kết quả: [1.0, -2.0]

</details>

##### ML14-practice-2

Tính MAE cho residual [1,−2].

<details>
<summary>Đáp án và cách kiểm</summary>

(1+2)/2=1.5.

```python
import numpy as np
print(float(np.mean(np.abs([1.,-2.]))))
```
Kết quả: 1.5

</details>

##### ML14-practice-3

Tính MSE và RMSE cho residual [1,−2], in RMSE sáu chữ số.

<details>
<summary>Đáp án và cách kiểm</summary>

MSE=2.5; RMSE=sqrt(2.5)≈1.581139.

```python
import numpy as np
mse=np.mean(np.array([1.,-2.])**2)
print(float(mse))
print(f"{np.sqrt(mse):.6f}")
```
Kết quả: 2.5
1.581139

</details>

##### ML14-practice-4

y=[1,2,3],pred=[1,2,3]. Tính MAE,MSE,RMSE và R².

<details>
<summary>Đáp án và cách kiểm</summary>

Ba sai số bằng 0; SST>0 nên R²=1.

```python
import numpy as np
y=np.array([1.,2.,3.]);e=np.zeros(3)
print(float(np.mean(np.abs(e))))
print(float(np.mean(e**2)))
print(float(np.sqrt(np.mean(e**2))))
print(float(1-np.sum(e**2)/np.sum((y-y.mean())**2)))
```
Kết quả: 0.0
0.0
0.0
1.0

</details>

##### ML14-practice-5

y=[1,2,3],pred=[2,2,2]. Tính R².

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán bằng mean y, SSE=SST=2 nên R²=0.

```python
import numpy as np
y=np.array([1.,2.,3.]);pred=np.full(3,2.)
print(float(1-np.sum((pred-y)**2)/np.sum((y-y.mean())**2)))
```
Kết quả: 0.0

</details>

##### ML14-practice-6

y=[1,2,3],pred=[0,0,0]. Tính R².

<details>
<summary>Đáp án và cách kiểm</summary>

SSE=14,SST=2 nên R²=1−7=−6.

```python
import numpy as np
y=np.array([1.,2.,3.])
print(float(1-np.sum(y**2)/np.sum((y-y.mean())**2)))
```
Kết quả: -6.0

</details>

##### ML14-practice-7

Vì sao E=Σe²/(2m) trong bài hồi quy không được báo là MSE nguyên giá trị?

<details>
<summary>Đáp án và cách kiểm</summary>

MSE=Σe²/m=2E. Chúng có cùng vị trí cực tiểu khi dữ liệu cố định nhưng giá trị khác nhau.

</details>

##### ML14-practice-8

So sánh MAE của residual [0,4] với [2,2], và MSE tương ứng.

<details>
<summary>Đáp án và cách kiểm</summary>

MAE đều 2; MSE lần lượt 8 và 4, phản ánh ảnh hưởng của residual lớn.

```python
import numpy as np
for e in [[0.,4.],[2.,2.]]:
    a=np.array(e)
    print((float(np.abs(a).mean()),float((a*a).mean())))
```
Kết quả: (2.0, 8.0)
(2.0, 4.0)

</details>

##### ML14-practice-9

Tất cả y=[5,5]. Vì sao R² cần xử lý riêng ngay cả khi dự đoán đúng?

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=5 và SST=0. Khi SSE=0, công thức có 0/0; cần ghi không xác định hoặc quy ước rõ ràng thay vì dùng phép chia trực tiếp.

</details>

##### ML14-practice-10

Nhân cả y và pred với 1000. MAE, RMSE, MSE và R² thay đổi thế nào nếu SST ban đầu dương?

<details>
<summary>Đáp án và cách kiểm</summary>

MAE và RMSE nhân 1000; MSE nhân 1000000. R² giữ nguyên nếu SST>0 vì cả SSE và SST nhân cùng hệ số bình phương.

</details>

##### ML14-practice-11

Một báo cáo dùng lỗi tính trên dữ liệu đã fit rồi gọi là test MSE. Sai ở đâu?

<details>
<summary>Đáp án và cách kiểm</summary>

Sai tên tập đánh giá. Đây là training MSE; phải giữ dữ liệu đánh giá riêng và ghi đúng tập dùng để tính.

</details>

##### ML14-practice-12

Nếu m=0 thì có thể báo mean error=0 để tránh lỗi không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Chưa có quan sát để lấy trung bình; phải từ chối hoặc báo không có dữ liệu theo hợp đồng đã định.

</details>

<a id="ml15"></a>

## ML15 · Tính metric phân loại từ confusion matrix và chọn metric theo chi phí lỗi

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML09](#ml09)

<a id="ml15-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Đếm TP, FP, FN và TN. Dùng số đếm để tính accuracy, precision, recall và F1. Ghi quy ước cho trường hợp mẫu số bằng 0.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Gán từng mẫu vào một ô rồi dự đoán bốn số đếm.
2. **P2** · Tính ba metric được in. Tính thêm F1 từ precision và recall.

<a id="ml15-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
y = np.array([1, 1, 1, 0, 0, 0])
p = np.array([1, 1, 0, 1, 0, 0])
tp = int(((y == 1) & (p == 1)).sum())
fp = int(((y == 0) & (p == 1)).sum())
fn = int(((y == 1) & (p == 0)).sum())
tn = len(y) - tp - fp - fn
print(tp, fp, fn, tn)
print(np.round([(tp+tn)/len(y), tp/(tp+fp), tp/(tp+fn)], 6).tolist())
~~~

[Xem kết quả mẫu](#ml15-ket-qua)

<a id="ml15-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích mẫu số precision theo nhãn dự đoán, recall theo nhãn thật.
2. **I2** · Tìm dòng cần đổi để dùng lớp 0 làm positive. Xác định bốn ô hoán đổi như thế nào.

[Đối chiếu cách giải thích](#ml15-giai-thich)

<a id="ml15-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi mẫu thứ ba sang dự đoán 1. Kiểm recall thành 1 và precision bằng 3/4. Tính thêm specificity = TN/(TN+FP) và kiểm bằng 2/3.
2. **MO2** · Dự đoán mọi mẫu bằng 0. Thêm quy ước precision=0 và kiểm recall=0.
3. **MO3** · Dùng 9 nhãn 0 và 1 nhãn 1, dự đoán toàn 0. Kiểm accuracy=0.9 và F1 lớp 1 bằng 0.

<a id="ml15-make"></a>

### E · Make 1 · Viết hàm

**`binary_metrics(y, p)`**

Hai vector 0/1 cùng độ dài dương, positive=1. Trả tuple (accuracy, precision, recall, F1), chia cho 0 thì dùng 0. Báo ValueError nếu miền hoặc shape sai.

Điền hàm. Chạy `python ML15.py`.

[Mã khởi đầu và 5 ca kiểm](#ml15-starter) · [Lời giải](#ml15-loi-giai)

<a id="ml15-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm tính macro-F1 từ F1 của hai lớp. Với y=[1,0,0,0] và p=[0,0,0,0], kiểm F1 lớp 0=6/7 và macro-F1=3/7.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml15-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml15-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
2 1 1 2
[0.666667, 0.666667, 0.666667]
~~~

</details>

<details class="answer" id="ml15-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

TP=2, FP=1, FN=1, TN=2. Accuracy, precision, recall và F1 đều 2/3. Nếu lớp 0 là positive, đổi TP↔TN và FP↔FN.

</details>

<details class="answer" id="ml15-starter" data-starter="ML15">
<summary>E · Mã khởi đầu và ca kiểm · ML15.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def binary_metrics(y, p):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(binary_metrics([1,1,0,0], [1,0,1,0]), [0.5,0.5,0.5,0.5])


def case_02():
    same(binary_metrics([1,0,0,0], [0,0,0,0]), [0.75,0,0,0])


def case_03():
    same(binary_metrics([1,1,0], [1,0,0]), [2/3,1,0.5,2/3])


def case_04():
    same(binary_metrics([0], [0]), [1,0,0,0])


def case_05():
    rejects(binary_metrics, [1], [2])


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml15-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def binary_metrics(y, p):
    y, p = np.asarray(y), np.asarray(p)
    if y.ndim != 1 or y.size == 0 or y.shape != p.shape or not np.isin(y, [0, 1]).all() or not np.isin(p, [0, 1]).all():
        raise ValueError("Cần hai vector nhị phân hợp lệ")
    tp = int(np.count_nonzero((y == 1) & (p == 1)))
    actual, predicted = int(y.sum()), int(p.sum())
    precision = tp / predicted if predicted else 0
    recall = tp / actual if actual else 0
    f1 = 2 * tp / (actual + predicted) if actual + predicted else 0
    return float((y == p).mean()), precision, recall, f1
~~~

</details>

<a id="ml15-on-tap"></a>

### Ôn tập ML15

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML15-mcq-1

True=1,pred=0 thuộc count nào?

- **A** · FN
- **B** · FP
- **C** · TN

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Âm dự đoán sai trên mẫu dương thật.

- **A** · Âm dự đoán sai trên mẫu dương thật.
- **B** · FP là true=0,pred=1.
- **C** · TN cần true=pred=0.

</details>

##### ML15-mcq-2

True=0,pred=0 thuộc count nào?

- **A** · FN
- **B** · TN
- **C** · TP

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cả nhãn thật và dự đoán đều âm.

- **A** · FN cần true=1.
- **B** · Cả nhãn thật và dự đoán đều âm.
- **C** · TP cần lớp dương.

</details>

##### ML15-mcq-3

Precision=1 có bảo đảm recall=1 không?

- **A** · Có vì mọi dự đoán dương đúng
- **B** · Có nếu có FP
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Ví dụ TP=1,FP=0,FN=9 cho precision=1,recall=0.1.

- **A** · Vẫn có thể bỏ sót nhiều mẫu dương.
- **B** · Precision=1 với mẫu số dương đòi FP=0.
- **C** · Ví dụ TP=1,FP=0,FN=9 cho precision=1,recall=0.1.

</details>

##### ML15-mcq-4

Mẫu thật là lớp 0 nhưng dự đoán 1 được gọi là gì khi lớp dương=1?

- **A** · FN
- **B** · FP
- **C** · TP

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Dự đoán dương sai: false positive.

- **A** · FN là thật 1 nhưng dự đoán 0.
- **B** · Dự đoán dương sai: false positive.
- **C** · TP cần thật và dự đoán đều dương.

</details>

##### ML15-mcq-5

Precision được tính theo công thức nào?

- **A** · TP/(TP+FP)
- **B** · TP/(TP+FN)
- **C** · (TP+TN)/N

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mẫu số là toàn bộ dự đoán dương.

- **A** · Mẫu số là toàn bộ dự đoán dương.
- **B** · Đây là recall.
- **C** · Đây là accuracy.

</details>

##### ML15-mcq-6

Recall có ý nghĩa nào?

- **A** · Tỷ lệ dự đoán dương là đúng
- **B** · Tỷ lệ toàn bộ mẫu được dự đoán đúng
- **C** · Tỷ lệ mẫu dương thật được tìm thấy

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Recall=TP/(TP+FN).

- **A** · Đó là precision.
- **B** · Đó là accuracy.
- **C** · Recall=TP/(TP+FN).

</details>

##### ML15-mcq-7

TP=3,FP=1,FN=2. F1 theo dạng đếm trực tiếp bằng?

- **A** · 2/3
- **B** · 3/4
- **C** · 3/5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

2TP/(2TP+FP+FN)=6/9=2/3.

- **A** · 2TP/(2TP+FP+FN)=6/9=2/3.
- **B** · Đây là precision.
- **C** · Đây là recall.

</details>

##### ML15-mcq-8

Dữ liệu có 99 âm,1 dương; luôn dự đoán âm. Accuracy là 99% nhưng điều gì xảy ra?

- **A** · Recall dương là 100%
- **B** · Recall dương là 0%
- **C** · Đã chứng minh model hữu ích cho tìm ca dương

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

TP=0,FN=1 nên recall=0.

- **A** · Không tìm được mẫu dương nào.
- **B** · TP=0,FN=1 nên recall=0.
- **C** · Accuracy cao do mất cân bằng, chưa đáp ứng mục tiêu tìm dương.

</details>

##### ML15-mcq-9

Nếu không có dự đoán dương, precision theo công thức trực tiếp gặp vấn đề gì?

- **A** · Luôn bằng 1
- **B** · Luôn bằng recall
- **C** · TP+FP=0, cần quy định hành vi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Có thể báo không xác định hoặc quy ước zero_division rõ ràng.

- **A** · Không tự gán 1.
- **B** · Hai metric có mẫu số khác nhau.
- **C** · Có thể báo không xác định hoặc quy ước zero_division rõ ràng.

</details>

##### ML15-mcq-10

Tăng TN trong khi TP,FP,FN giữ nguyên ảnh hưởng precision/recall ra sao?

- **A** · Cả hai giữ nguyên
- **B** · Cả hai bắt buộc tăng
- **C** · Precision tăng còn recall giảm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Precision và recall chỉ dùng TP/FP hoặc TP/FN.

- **A** · Precision và recall chỉ dùng TP/FP hoặc TP/FN.
- **B** · TN không nằm trong hai mẫu số đó.
- **C** · Không có thay đổi TP,FP,FN.

</details>

#### Tự luận và viết mã

##### ML15-practice-1

y=[1,1,0,0],pred=[1,0,1,0]. Đếm TP,FP,FN,TN.

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi loại có đúng một mẫu.

```python
y=[1,1,0,0];pred=[1,0,1,0]
print([sum(a==t and b==p for a,b in zip(y,pred)) for t,p in [(1,1),(0,1),(1,0),(0,0)]])
```
Kết quả: [1, 1, 1, 1]

</details>

##### ML15-practice-2

TP=3,FP=1,FN=2,TN=4. Tính accuracy.

<details>
<summary>Đáp án và cách kiểm</summary>

(3+4)/(3+1+2+4)=0.7.

```python
tp,fp,fn,tn=3,1,2,4
print((tp+tn)/(tp+fp+fn+tn))
```
Kết quả: 0.7

</details>

##### ML15-practice-3

Với cùng counts, tính precision và recall.

<details>
<summary>Đáp án và cách kiểm</summary>

Precision=3/4=0.75; recall=3/5=0.6.

```python
tp,fp,fn=3,1,2
print(tp/(tp+fp))
print(tp/(tp+fn))
```
Kết quả: 0.75
0.6

</details>

##### ML15-practice-4

Với cùng counts, tính F1 và in sáu chữ số.

<details>
<summary>Đáp án và cách kiểm</summary>

F1=6/9≈0.666667.

```python
tp,fp,fn=3,1,2
print(f"{2*tp/(2*tp+fp+fn):.6f}")
```
Kết quả: 0.666667

</details>

##### ML15-practice-5

Confusion matrix quy ước hàng=true [0,1],cột=pred [0,1]. TP=3,FP=1,FN=2,TN=4. Viết ma trận.

<details>
<summary>Đáp án và cách kiểm</summary>

[[TN,FP],[FN,TP]]=[[4,1],[2,3]]. Phải ghi quy ước trục.

```python
tn,fp,fn,tp=4,1,2,3
print([[tn,fp],[fn,tp]])
```
Kết quả: [[4, 1], [2, 3]]

</details>

##### ML15-practice-6

Có 10 mẫu dương thật, mô hình tìm được 6. Recall là bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

TP=6,FN=4; recall=6/10=0.6.

```python
print(6/10)
```
Kết quả: 0.6

</details>

##### ML15-practice-7

Mô hình báo dương 8 mẫu trong đó 2 mẫu sai. Precision bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

TP=6,FP=2; precision=6/8=0.75.

```python
print((8-2)/8)
```
Kết quả: 0.75

</details>

##### ML15-practice-8

Vì sao không dùng trung bình cộng precision và recall thay cho F1 đã định nghĩa?

<details>
<summary>Đáp án và cách kiểm</summary>

F1 là trung bình điều hòa 2PR/(P+R), không phải (P+R)/2. Cần giữ đúng định nghĩa; hai cách khác nhau khi P khác R.

</details>

##### ML15-practice-9

Không có nhãn dương thật. Recall có tự bằng 0 theo công thức không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không: TP+FN=0 nên công thức trực tiếp không xác định. Nếu chọn trả 0 phải ghi đây là quy ước, không phải kết quả phép chia.

</details>

##### ML15-practice-10

TP=0,FP=2,FN=3. F1 theo công thức đếm bằng bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

Mẫu số=5>0,tử số=0 nên F1=0 dù không có TP.

```python
tp,fp,fn=0,2,3
print(2*tp/(2*tp+fp+fn))
```
Kết quả: 0.0

</details>

##### ML15-practice-11

Trong bài toán bỏ sót ca dương có chi phí cao, metric nào cần theo dõi trực tiếp?

<details>
<summary>Đáp án và cách kiểm</summary>

Recall và số FN giúp theo dõi bỏ sót. Vẫn cần xem FP/precision và chi phí thực tế; không kết luận tối ưu chỉ từ một metric.

</details>

##### ML15-practice-12

Đổi quy ước lớp dương từ 1 sang 0 có giữ nguyên precision/recall không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không nói chung. Counts dương/âm đổi vai trò; phải nêu rõ lớp dương trước khi tính và diễn giải metric.

</details>

<a id="ml16"></a>

## ML16 · Giải thích sự thay đổi TPR/FPR theo threshold và ý nghĩa AUC

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML15](#ml15)

<a id="ml16-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Dựng một điểm ROC (FPR, TPR) cho mỗi ngưỡng. Xử lý các mẫu cùng điểm số trong cùng một lượt. Khi tính AUC theo cặp, cặp hòa đóng góp nửa điểm.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán bốn điểm ROC và đánh dấu bước có hòa điểm.
2. **P2** · Tính AUC bằng cách so bốn cặp dương–âm, cho 0.5 điểm mỗi cặp hòa.

<a id="ml16-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
y = np.array([1, 0, 1, 0])
score = np.array([0.9, 0.8, 0.8, 0.1])
for t in [float("inf"), 0.9, 0.8, 0.1]:
    p = score >= t
    fpr = np.mean(p[y == 0])
    tpr = np.mean(p[y == 1])
    print(fpr, tpr)
~~~

[Xem kết quả mẫu](#ml16-ket-qua)

<a id="ml16-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Nêu vì sao hạ threshold làm TPR/FPR không giảm. Giải thích vai trò điểm (0,0).
2. **I2** · Đối chiếu kết quả so cặp với tổng diện tích hình thang theo FPR.

[Đối chiếu cách giải thích](#ml16-giai-thich)

<a id="ml16-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Cộng 7 vào score và mọi threshold hữu hạn. Kiểm ROC giữ nguyên.
2. **MO2** · Đặt tất cả score=0.5. Kiểm ROC nối (0,0) tới (1,1), AUC=0.5.
3. **MO3** · Đổi score của mẫu âm thứ hai (chỉ số 3) thành 1.0. Tính lại điểm ROC và kiểm AUC giảm từ 0.875 xuống 0.375.

<a id="ml16-make"></a>

### E · Make 1 · Viết hàm

**`roc_curve_points(y, score)`**

Nhận vector nhãn 0/1 có cả hai lớp và vector score hữu hạn cùng shape. Trả ma trận hai cột FPR và TPR cho threshold +∞ rồi các score phân biệt theo thứ tự giảm. Báo ValueError nếu miền hoặc shape sai.

Điền hàm. Chạy `python ML16.py`.

[Mã khởi đầu và 4 ca kiểm](#ml16-starter) · [Lời giải](#ml16-loi-giai)

<a id="ml16-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm tính AUC bằng tổng hình thang từ các điểm ROC. Kiểm AUC=1 cho [(0,0),(0,1),(1,1)] và AUC=0 cho [(0,0),(1,0),(1,1)].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml16-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml16-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
0.0 0.0
0.0 0.5
0.5 1.0
1.0 1.0
~~~

</details>

<details class="answer" id="ml16-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

ROC là [(0,0),(0,0.5),(0.5,1),(1,1)]. Mức 0.8 thêm cùng lúc một mẫu dương và một mẫu âm. AUC=(3+0.5)/4=0.875.

</details>

<details class="answer" id="ml16-starter" data-starter="ML16">
<summary>E · Mã khởi đầu và ca kiểm · ML16.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def roc_curve_points(y, score):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(roc_curve_points([1, 0, 1, 0], [0.9, 0.8, 0.8, 0.1]), [[0,0],[0,0.5],[0.5,1],[1,1]])


def case_02():
    same(roc_curve_points([0, 1], [4, 4]), [[0,0],[1,1]])


def case_03():
    same(roc_curve_points([0, 1], [2, 1]), [[0,0],[1,0],[1,1]])


def case_04():
    rejects(roc_curve_points, [1, 1], [0.4, 0.8])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml16-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def roc_curve_points(y, score):
    y, score = np.asarray(y), np.asarray(score, dtype=float)
    if y.ndim != 1 or score.shape != y.shape or set(y) != {0, 1} or not np.isfinite(score).all():
        raise ValueError("Cần score hữu hạn và đủ hai lớp")
    rows = [(0., 0.)]
    for t in np.unique(score)[::-1]:
        positive = score >= t
        rows.append((positive[y == 0].mean(), positive[y == 1].mean()))
    return np.asarray(rows)
~~~

</details>

<a id="ml16-on-tap"></a>

### Ôn tập ML16

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML16-mcq-1

ROC điểm (0,1) có nghĩa gì?

- **A** · Không false positive và tìm hết positive
- **B** · Không true positive
- **C** · Mọi mẫu dự đoán dương

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Trục x=FPR=0,trục y=TPR=1.

- **A** · Trục x=FPR=0,trục y=TPR=1.
- **B** · TPR=1 nghĩa tìm đủ positive.
- **C** · Khi đó FPR thường bằng 1 nếu có negative.

</details>

##### ML16-mcq-2

AUC=1 có tự chứng minh p=0.9 được hiệu chuẩn đúng 90% không?

- **A** · Chỉ khi có hai lớp
- **B** · Không
- **C** · Có vì ranking hoàn hảo

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

AUC đo thứ hạng,không trực tiếp đo hiệu chuẩn.

- **A** · Có hai lớp cần để tính ROC nhưng không bảo đảm calibration.
- **B** · AUC đo thứ hạng,không trực tiếp đo hiệu chuẩn.
- **C** · Ranking và calibration là khác nhau.

</details>

##### ML16-mcq-3

Nếu giữ nhãn và đảo dấu mọi score,không có ties,AUC mới là gì?

- **A** · AUC cũ+1
- **B** · Luôn 0.5
- **C** · 1−AUC cũ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mỗi cặp thắng thành thua và ngược lại.

- **A** · Có thể vượt miền [0,1].
- **B** · Thứ tự bị đảo hoàn toàn,chưa chắc ngẫu nhiên.
- **C** · Mỗi cặp thắng thành thua và ngược lại.

</details>

##### ML16-mcq-4

Trục ngang và trục dọc của ROC thông thường lần lượt là gì?

- **A** · FPR và TPR
- **B** · Precision và Recall
- **C** · TP và FP chưa chuẩn hóa

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

ROC vẽ TPR theo FPR khi đổi ngưỡng.

- **A** · ROC vẽ TPR theo FPR khi đổi ngưỡng.
- **B** · Đó là một hệ trục khác, không phải ROC.
- **C** · ROC dùng tỷ lệ, không chỉ counts.

</details>

##### ML16-mcq-5

FPR được tính bằng công thức nào?

- **A** · FP/(TP+FP)
- **B** · FP/(FP+TN)
- **C** · FN/(TP+FN)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mẫu số là toàn bộ mẫu âm thật.

- **A** · Đây là tỷ lệ sai trong dự đoán dương, không phải FPR.
- **B** · Mẫu số là toàn bộ mẫu âm thật.
- **C** · Đây là tỷ lệ bỏ sót dương.

</details>

##### ML16-mcq-6

Giữ nguyên score và giảm ngưỡng dự đoán dương, điều gì xảy ra với TPR/FPR nếu mẫu số đều khác 0?

- **A** · Cả hai bắt buộc giảm
- **B** · TPR tăng nhưng FPR bắt buộc giảm
- **C** · Cả hai không giảm, nhưng có thể giữ nguyên

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Tập dự đoán dương mở rộng; các count TP,FP không giảm.

- **A** · Ngưỡng thấp hơn không loại dự đoán dương cũ.
- **B** · Thêm dự đoán dương cũng có thể thêm FP.
- **C** · Tập dự đoán dương mở rộng; các count TP,FP không giảm.

</details>

##### ML16-mcq-7

AUC đo tính chất nào trực tiếp hơn accuracy ở một ngưỡng cố định?

- **A** · Khả năng xếp hạng score giữa lớp dương và âm
- **B** · Số lần chạy gradient
- **C** · Độ chính xác tại ngưỡng 0.5 duy nhất

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

AUC tổng hợp sự phân tách theo thứ hạng qua các ngưỡng.

- **A** · AUC tổng hợp sự phân tách theo thứ hạng qua các ngưỡng.
- **B** · Đây không phải metric tối ưu hóa theo số bước.
- **C** · Accuracy ở một ngưỡng khác AUC.

</details>

##### ML16-mcq-8

Một tập đánh giá chỉ có nhãn dương. Có tính được ROC đầy đủ theo công thức thường dùng không?

- **A** · Có vì mọi TPR bằng 1
- **B** · Không; không có mẫu âm để xác định FPR
- **C** · Có và AUC bắt buộc bằng 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

FP+TN=0 nên FPR không xác định.

- **A** · TPR còn phụ thuộc ngưỡng; thiếu mẫu âm vẫn là vấn đề.
- **B** · FP+TN=0 nên FPR không xác định.
- **C** · Không tự gán AUC hoàn hảo.

</details>

##### ML16-mcq-9

Hai mẫu khác lớp có score bằng nhau. Trong cách tính AUC theo cặp với quy ước tie=0.5, cặp đó đóng góp bao nhiêu?

- **A** · 1
- **B** · 0
- **C** · 0.5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Hai score hòa được tính nửa điểm theo quy ước đã nêu.

- **A** · Đó là đóng góp khi dương có score cao hơn âm.
- **B** · Đó là khi dương xếp thấp hơn âm.
- **C** · Hai score hòa được tính nửa điểm theo quy ước đã nêu.

</details>

##### ML16-mcq-10

Dương có score thấp hơn mọi âm trong tập có cả hai lớp. AUC theo cặp bằng bao nhiêu?

- **A** · 0
- **B** · 1
- **C** · 0.5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mọi cặp dương–âm nhận 0 điểm.

- **A** · Mọi cặp dương–âm nhận 0 điểm.
- **B** · Thứ tự hoàn toàn ngược.
- **C** · Không có cặp hòa hay thắng.

</details>

#### Tự luận và viết mã

##### ML16-practice-1

TP=8,FN=2,FP=3,TN=7. Tính TPR và FPR.

<details>
<summary>Đáp án và cách kiểm</summary>

TPR=8/10=0.8; FPR=3/10=0.3.

```python
tp,fn,fp,tn=8,2,3,7
print(tp/(tp+fn))
print(fp/(fp+tn))
```
Kết quả: 0.8
0.3

</details>

##### ML16-practice-2

y=[1,0,1,0],score=[0.9,0.8,0.4,0.1]. Dùng ngưỡng 0.5 và quy tắc ≥, tính TPR/FPR.

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán [1,1,0,0]; TP=1,FP=1,FN=1,TN=1 nên cả hai tỷ lệ 0.5.

```python
y=[1,0,1,0];score=[.9,.8,.4,.1];pred=[int(s>=.5) for s in score]
tp=sum(t==1 and p==1 for t,p in zip(y,pred));fp=sum(t==0 and p==1 for t,p in zip(y,pred))
print(pred)
print((tp/2,fp/2))
```
Kết quả: [1, 1, 0, 0]
(0.5, 0.5)

</details>

##### ML16-practice-3

Vẫn dữ liệu trên, giảm ngưỡng về 0.3.

<details>
<summary>Đáp án và cách kiểm</summary>

Dự đoán [1,1,1,0]; TPR=1,FPR=0.5.

```python
y=[1,0,1,0];score=[.9,.8,.4,.1];pred=[int(s>=.3) for s in score]
print(pred)
print((sum(t==1 and p==1 for t,p in zip(y,pred))/2,sum(t==0 and p==1 for t,p in zip(y,pred))/2))
```
Kết quả: [1, 1, 1, 0]
(1.0, 0.5)

</details>

##### ML16-practice-4

Nếu ngưỡng lớn hơn mọi score, ROC ở điểm nào khi hai lớp đều có mặt?

<details>
<summary>Đáp án và cách kiểm</summary>

Không mẫu nào dự đoán dương: FP=TP=0 nên (FPR,TPR)=(0,0).

</details>

##### ML16-practice-5

Nếu ngưỡng thấp hơn mọi score, ROC ở điểm nào khi hai lớp đều có mặt?

<details>
<summary>Đáp án và cách kiểm</summary>

Mọi mẫu đều dự đoán dương nên (FPR,TPR)=(1,1).

</details>

##### ML16-practice-6

Dương score=[0.9,0.4],âm score=[0.8,0.1]. Tính AUC theo cặp, tie=0.5.

<details>
<summary>Đáp án và cách kiểm</summary>

Bốn cặp: 0.9 thắng hai lần,0.4 thắng một lần; AUC=3/4=0.75.

```python
positive=[.9,.4];negative=[.8,.1]
credit=sum(1. if u>v else .5 if u==v else 0. for u in positive for v in negative)
print(credit/(len(positive)*len(negative)))
```
Kết quả: 0.75

</details>

##### ML16-practice-7

Dương score=[0.5],âm score=[0.5]. Tính AUC theo quy ước tie=0.5.

<details>
<summary>Đáp án và cách kiểm</summary>

Một cặp hòa, AUC=0.5.

```python
u,v=.5,.5
print(1. if u>v else .5 if u==v else 0.)
```
Kết quả: 0.5

</details>

##### ML16-practice-8

Một hệ xếp mọi mẫu dương trên mọi mẫu âm có AUC theo cặp bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

AUC=1 vì mọi cặp dương–âm đều có score dương cao hơn. Điều này không tự quyết định ngưỡng vận hành.

</details>

##### ML16-practice-9

Các score được cộng cùng một hằng số có đổi thứ hạng và AUC không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không nếu phép cộng không tạo lỗi số học. Thứ tự và quan hệ hòa giữ nguyên; ngưỡng số cụ thể có thể cần đổi tương ứng.

</details>

##### ML16-practice-10

Tại sao AUC cao không bảo đảm mọi ngưỡng đều phù hợp?

<details>
<summary>Đáp án và cách kiểm</summary>

Một ngưỡng vẫn có thể tạo quá nhiều FP hoặc FN. Cần chọn theo chi phí lỗi và dữ liệu validation, giữ test độc lập.

</details>

##### ML16-practice-11

Tập test chỉ có một lớp. Nên ghi AUC thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Báo không xác định hoặc lỗi input theo hợp đồng. Không gán 0.5 hay 1 rồi trình bày như đo được ROC hợp lệ.

</details>

##### ML16-practice-12

TPR có tên metric nào đã học ở ML15?

<details>
<summary>Đáp án và cách kiểm</summary>

TPR=TP/(TP+FN), chính là recall/sensitivity của lớp dương theo cùng quy ước nhãn.

</details>

<a id="ml17"></a>

## ML17 · Chẩn đoán underfitting/overfitting qua sai số train và dữ liệu mới

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML08](#ml08), [ML13](#ml13)

<a id="ml17-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Chọn độ phức tạp bằng sai số validation. Sai số train thấp cùng khoảng cách lớn đến validation là dấu hiệu quá khớp.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán khoảng cách validation−train ở từng bậc.
2. **P2** · Chọn bậc theo validation và theo train. Đánh dấu hai bậc có dấu hiệu underfitting và overfitting rõ nhất.

<a id="ml17-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
degree = np.array([0, 1, 2, 3])
train = np.array([9., 4., 1., 0.])
valid = np.array([10., 5., 2., 8.])
print((valid - train).tolist())
print(int(degree[valid.argmin()]), int(degree[train.argmin()]))
~~~

[Xem kết quả mẫu](#ml17-ket-qua)

<a id="ml17-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao khoảng cách nhỏ ở bậc 0 vẫn có thể là underfitting.
2. **I2** · Xác định bậc cần đánh giá test nếu vòng chọn mô hình chỉ dùng train và validation. Viết một lý do giữ test ngoài vòng.

[Đối chiếu cách giải thích](#ml17-giai-thich)

<a id="ml17-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đặt lỗi validation bậc 3 thành 1.5. Kiểm lựa chọn chuyển sang 3.
2. **MO2** · Đặt lỗi validation bậc 1 và 2 cùng bằng 2. Đổi thứ tự dòng và thêm quy tắc chọn bậc nhỏ. Kiểm vẫn chọn 1.
3. **MO3** · Trừ một baseline đủ tốt khỏi mọi lỗi validation rồi so thứ hạng. Dùng baseline=2 để thấy mô hình nào tốt ngang baseline.

<a id="ml17-make"></a>

### E · Make 1 · Viết hàm

**`pick_degree(degrees, train_loss, val_loss)`**

Nhận ba vector cùng độ dài dương. Bậc nguyên không âm và phân biệt. Loss hữu hạn không âm. Trả (bậc có val_loss nhỏ nhất, val_loss−train_loss của bậc đó), hòa thì lấy bậc nhỏ. Báo ValueError cho đầu vào sai.

Điền hàm. Chạy `python ML17.py`.

[Mã khởi đầu và 4 ca kiểm](#ml17-starter) · [Lời giải](#ml17-loi-giai)

<a id="ml17-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự fit ba mô hình đa thức bậc 0,1,2 như ML08. Dùng train x=[−1,0,1], y=[1,0,1] và validation x=[−2,2], y=[0,0]. Lập bảng lỗi rồi kiểm bậc 0 và 1 hòa trong sai số số học, bậc 2 có validation MSE 16.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml17-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml17-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[1.0, 1.0, 1.0, 8.0]
2 3
~~~

</details>

<details class="answer" id="ml17-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Khoảng cách [1,1,1,8]. Theo validation chọn bậc 2, theo train chọn bậc 3. Bậc 0 có hai loss cao, bậc 3 có train loss nhỏ và validation loss cao hơn rõ rệt.

</details>

<details class="answer" id="ml17-starter" data-starter="ML17">
<summary>E · Mã khởi đầu và ca kiểm · ML17.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def pick_degree(degrees, train_loss, val_loss):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(pick_degree([3,0,2,1], [0,9,1,4], [8,10,2,5]), [2,1])


def case_02():
    same(pick_degree([4,1], [0,2], [3,3]), [1,1])


def case_03():
    same(pick_degree([2], [2], [1]), [2,-1])


def case_04():
    rejects(pick_degree, [1,1], [1,2], [2,1])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml17-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def pick_degree(degrees, train_loss, val_loss):
    degrees = np.asarray(degrees)
    train, valid = np.asarray(train_loss, dtype=float), np.asarray(val_loss, dtype=float)
    if degrees.ndim != 1 or not degrees.size or train.shape != degrees.shape or valid.shape != degrees.shape:
        raise ValueError("Shape không hợp lệ")
    if degrees.dtype.kind not in "iu" or np.any(degrees < 0) or np.unique(degrees).size != degrees.size:
        raise ValueError("Bậc không hợp lệ")
    if not np.isfinite(train).all() or not np.isfinite(valid).all() or np.any(train < 0) or np.any(valid < 0):
        raise ValueError("Loss không hợp lệ")
    i = np.lexsort((degrees, valid))[0]
    return int(degrees[i]), float(valid[i] - train[i])
~~~

</details>

<a id="ml17-on-tap"></a>

### Ôn tập ML17

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML17-mcq-1

Một model dự đoán hằng có thể underfit quan hệ phức tạp vì sao?

- **A** · Khả năng biểu diễn bị hạn chế
- **B** · Vì luôn có training loss=0
- **C** · Vì mọi model hằng overfit

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Không thể phản ánh nhiều dạng thay đổi theo đặc trưng.

- **A** · Không thể phản ánh nhiều dạng thay đổi theo đặc trưng.
- **B** · Không đúng nói chung.
- **C** · Không phải kết luận mặc định.

</details>

##### ML17-mcq-2

Độ phức tạp tăng nhưng validation không cải thiện. Có nên chọn chỉ vì train tốt hơn?

- **A** · Có nếu bỏ test khỏi báo cáo
- **B** · Không theo tiêu chí validation đang dùng
- **C** · Có,mọi train tốt hơn đều tổng quát tốt hơn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Lựa chọn cần theo tiêu chí đánh giá đã quy định.

- **A** · Không giải quyết chất lượng model.
- **B** · Lựa chọn cần theo tiêu chí đánh giá đã quy định.
- **C** · Đó là suy luận sai từ fit train.

</details>

##### ML17-mcq-3

Khác phân bố giữa train và validation có thể tạo khoảng cách lỗi lớn không?

- **A** · Không,gap chỉ do overfitting
- **B** · Chỉ khi label là chuỗi
- **C** · Có

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cần kiểm dữ liệu ngoài giả thuyết độ phức tạp.

- **A** · Gap có nhiều nguyên nhân.
- **B** · Không liên quan kiểu biểu diễn nhãn.
- **C** · Cần kiểm dữ liệu ngoài giả thuyết độ phức tạp.

</details>

##### ML17-mcq-4

Train error cao và validation error cũng cao gợi ý điều gì?

- **A** · Underfitting là một khả năng cần kiểm tra
- **B** · Chắc chắn overfitting
- **C** · Chắc chắn test bị lộ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Có thể mô hình chưa đủ khả năng hoặc chưa được tối ưu tốt; không chỉ dựa hai số để kết luận tuyệt đối.

- **A** · Có thể mô hình chưa đủ khả năng hoặc chưa được tối ưu tốt; không chỉ dựa hai số để kết luận tuyệt đối.
- **B** · Overfitting thường có khoảng cách train thấp,validation cao.
- **C** · Hai số này không chứng minh leakage.

</details>

##### ML17-mcq-5

Train error rất thấp nhưng validation error cao gợi ý nguy cơ nào?

- **A** · Mô hình chắc chắn hoàn hảo
- **B** · Overfitting hoặc khác biệt dữ liệu cần chẩn đoán
- **C** · Không cần thêm đánh giá

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Khoảng cách lớn cần xem độ phức tạp,quy trình và phân bố dữ liệu.

- **A** · Khớp train không bảo đảm tổng quát hóa.
- **B** · Khoảng cách lớn cần xem độ phức tạp,quy trình và phân bố dữ liệu.
- **C** · Validation đang đưa tín hiệu vấn đề.

</details>

##### ML17-mcq-6

Để chọn độ phức tạp mô hình, nên dùng dữ liệu nào?

- **A** · Test lặp lại cho đến khi tốt
- **B** · Chỉ training loss nhỏ nhất
- **C** · Validation hoặc CV trong phần train

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Đây là vai trò dữ liệu dùng lựa chọn mô hình.

- **A** · Test sẽ tham gia lựa chọn,gây đánh giá lạc quan.
- **B** · Chỉ train có thể ưu tiên mô hình quá phức tạp.
- **C** · Đây là vai trò dữ liệu dùng lựa chọn mô hình.

</details>

##### ML17-mcq-7

Thêm đặc trưng bất kỳ có luôn cải thiện chất lượng ngoài train không?

- **A** · Không
- **B** · Có vì có nhiều thông tin hơn
- **C** · Có nếu số cột là số chẵn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đặc trưng nhiễu hoặc không phù hợp có thể làm tổng quát hóa kém.

- **A** · Đặc trưng nhiễu hoặc không phù hợp có thể làm tổng quát hóa kém.
- **B** · Nhiều cột không đồng nghĩa nhiều tín hiệu hữu ích.
- **C** · Tính chẵn lẻ không quyết định chất lượng.

</details>

##### ML17-mcq-8

Bias/variance trong phân tích mô hình có giống cột bias toàn 1 không?

- **A** · Giống hoàn toàn
- **B** · Không, đây là các khái niệm khác nhau
- **C** · Variance là số hàng X

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Bias mô hình trong phân tích lỗi không phải hệ số chặn của design matrix.

- **A** · Tên bias dùng trong hai ngữ cảnh khác nhau.
- **B** · Bias mô hình trong phân tích lỗi không phải hệ số chặn của design matrix.
- **C** · Variance không phải kích thước dữ liệu.

</details>

##### ML17-mcq-9

Mô hình có validation loss thấp nhất trên một lần chia có được bảo đảm tốt nhất mọi dữ liệu tương lai không?

- **A** · Có
- **B** · Có nếu train loss=0
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cần xem biến thiên do cách chia và phạm vi dữ liệu.

- **A** · Một phép đo hữu hạn không bảo đảm mọi tương lai.
- **B** · Train khớp tuyệt đối vẫn có thể overfit.
- **C** · Cần xem biến thiên do cách chia và phạm vi dữ liệu.

</details>

##### ML17-mcq-10

Hai tập train và validation có các dòng sao chép cùng một mẫu. Khoảng cách loss nhỏ có chứng minh generalization tốt không?

- **A** · Không,cần kiểm leakage giữa hai tập
- **B** · Có vì score hai tập giống nhau
- **C** · Có nếu mô hình nhiều tham số

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Phải kiểm đơn vị mẫu và cách chia để đánh giá dữ liệu mới.

- **A** · Phải kiểm đơn vị mẫu và cách chia để đánh giá dữ liệu mới.
- **B** · Sự trùng mẫu có thể làm đánh giá lạc quan.
- **C** · Không giải quyết độc lập dữ liệu.

</details>

#### Tự luận và viết mã

##### ML17-practice-1

Mô hình A: train MSE=1,validation=8; B: train=2,validation=3. Nếu quy trình validation hợp lệ, nên ưu tiên mô hình nào theo validation MSE?

<details>
<summary>Đáp án và cách kiểm</summary>

Ưu tiên B theo tiêu chí đã cho, dù train MSE cao hơn. Chưa dùng test để thay đổi lựa chọn.

</details>

##### ML17-practice-2

Tính khoảng cách validation−train cho A=(1,8),B=(2,3).

<details>
<summary>Đáp án và cách kiểm</summary>

A có gap=7; B gap=1. Gap hỗ trợ chẩn đoán nhưng vẫn cần mức sai số tuyệt đối và ngữ cảnh.

```python
for train,val in [(1.,8.),(2.,3.)]:
    print(val-train)
```
Kết quả: 7.0
1.0

</details>

##### ML17-practice-3

Mô hình bậc 1,3,8 có validation MSE=[5,2,7]. Chọn bậc theo tiêu chí nhỏ nhất,không dùng test.

<details>
<summary>Đáp án và cách kiểm</summary>

Chọn bậc 3. Không chọn bậc 8 chỉ vì linh hoạt hơn.

```python
degrees=[1,3,8];scores=[5.,2.,7.]
print(degrees[min(range(len(scores)),key=lambda i:scores[i])])
```
Kết quả: 3

</details>

##### ML17-practice-4

Train và validation error đều cao. Nêu hai hướng kiểm tra trước khi kết luận chỉ cần tăng bậc.

<details>
<summary>Đáp án và cách kiểm</summary>

Kiểm tối ưu đã hội tụ chưa,feature/nhãn/shape có đúng không; sau đó xét mô hình có đủ khả năng biểu diễn quan hệ không. Dữ liệu hoặc code sai cũng có thể tạo lỗi cao.

</details>

##### ML17-practice-5

Vì sao không sửa hyperparameter sau mỗi lần xem test score?

<details>
<summary>Đáp án và cách kiểm</summary>

Khi quyết định phụ thuộc test thì test trở thành dữ liệu lựa chọn. Cần validation/CV để chọn,giữ test cho đánh giá cuối.

</details>

##### ML17-practice-6

Một feature chứa kết quả xảy ra sau thời điểm cần dự đoán. Train/validation score rất tốt có đủ tin không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Có nguy cơ leakage vì thông tin chưa tồn tại lúc dự đoán thực tế. Cần kiểm thời điểm và nguồn từng feature.

</details>

##### ML17-practice-7

Sau khi thêm feature ngẫu nhiên,train error giảm nhưng validation tăng. Diễn giải có căn cứ.

<details>
<summary>Đáp án và cách kiểm</summary>

Mô hình tận dụng thêm độ linh hoạt để khớp train nhưng chưa có bằng chứng feature giúp tổng quát hóa; cần cân nhắc bỏ hoặc đánh giá theo quy trình ổn định.

</details>

##### ML17-practice-8

Tại sao train MSE=0 chưa đủ gọi mô hình tốt?

<details>
<summary>Đáp án và cách kiểm</summary>

Mục tiêu là dự đoán dữ liệu chưa dùng để học. Ghi nhớ train có thể đạt 0 nhưng sai ngoài train,đặc biệt khi mô hình quá phức tạp.

</details>

##### ML17-practice-9

Ba lần chia cho model A có validation MSE=[1,5,3]. Tính mean và khoảng min–max.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=3,min=1,max=5. Các kết quả dao động nên không chỉ chọn lần tốt nhất để báo cáo.

```python
scores=[1.,5.,3.]
print(sum(scores)/len(scores))
print((min(scores),max(scores)))
```
Kết quả: 3.0
(1.0, 5.0)

</details>

##### ML17-practice-10

Mô hình hằng dự đoán cùng một giá trị cho quan hệ thật cong rõ. Có thể gặp loại thiếu phù hợp nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Có thể underfit do không biểu diễn được sự thay đổi theo x. Cần đánh giá và kiểm dữ liệu; không chỉ dùng tên mô hình để kết luận mọi bài toán.

</details>

##### ML17-practice-11

Giải thích vì sao càng nhiều tham số không đồng nghĩa càng tốt.

<details>
<summary>Đáp án và cách kiểm</summary>

Nhiều tham số tăng khả năng khớp cả tín hiệu và nhiễu. Chất lượng cần được đo ngoài dữ liệu huấn luyện và cân nhắc độ phức tạp phù hợp.

</details>

##### ML17-practice-12

Hai model cùng validation MSE=2 nhưng một model có train MSE=0.1,một model=1.8. Có đủ để kết luận model nào luôn tốt hơn không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Validation score đang ngang nhau theo tiêu chí cho trước; có thể xét độ ổn định,độ phức tạp và chi phí theo quy trình. Không tự suy từ train gap ra bảo đảm tuyệt đối.

</details>

<a id="ml18"></a>

## ML18 · Thêm phạt L2, không phạt bias và giải thích hiệu ứng shrinkage

[Mục lục](#muc-luc) · M4 · Đánh giá và điều chuẩn · Tiên quyết [ML17](#ml17), [ML05](#ml05)

<a id="ml18-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Thêm λ‖w‖² vào SSE và bỏ hệ số chặn khỏi phần phạt. Với đặc trưng đã trừ tâm như ví dụ, tăng λ kéo hệ số về 0.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán intercept khi x đã trừ tâm. Intercept có đổi theo λ?
2. **P2** · Tính hệ số slope ở λ=0, 2 và 6 từ hệ chéo.

<a id="ml18-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([-1., 0., 1.])
y = np.array([1., 3., 5.])
A = np.column_stack([np.ones(len(x)), x])
for lam in [0., 2., 6.]:
    w = np.linalg.solve(A.T @ A + lam * np.diag([0., 1.]), A.T @ y)
    print(lam, w.round(6).tolist())
~~~

[Xem kết quả mẫu](#ml18-ket-qua)

<a id="ml18-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Xác định phần tử nào giữ intercept khỏi penalty. Giải thích hệ quả nếu thay diag([0,1]) bằng I.
2. **I2** · So train SSE ở hai đầu λ. Giải thích vì sao shrinkage có thể cải thiện lỗi validation dù train SSE tăng.

[Đối chiếu cách giải thích](#ml18-giai-thich)

<a id="ml18-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi y thành [11,13,15]. Kiểm intercept tăng 10, slope giữ nguyên.
2. **MO2** · Bật phạt intercept và dùng λ=2. Kiểm intercept giảm từ 3 xuống 1.8.
3. **MO3** · Thêm vào A một bản sao của cột x. Dùng λ=2 và kiểm hai slope đều bằng 2/3.

<a id="ml18-make"></a>

### E · Make 1 · Viết hàm

**`ridge_fit(X, y, lam)`**

X 2D có ít nhất một hàng và một cột, y là vector cùng số hàng, λ hữu hạn không âm. Trả vector [intercept, các hệ số] tối thiểu hóa SSE + λ·Σwⱼ², bỏ phạt intercept. λ=0 dùng nghiệm `lstsq`. Báo ValueError nếu shape hoặc λ sai.

Điền hàm. Chạy `python ML18.py`.

[Mã khởi đầu và 4 ca kiểm](#ml18-starter) · [Lời giải](#ml18-loi-giai)

<a id="ml18-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự mở rộng gradient logistic của ML10 bằng penalty λ·Σwⱼ²/2, bỏ w₀. Với A=[[1,0],[1,2]], y=[0,1], w=[1,2], λ=0.5, kiểm phần tăng của gradient là [0,1].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml18-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml18-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
0.0 [3.0, 2.0]
2.0 [3.0, 1.0]
6.0 [3.0, 0.5]
~~~

</details>

<details class="answer" id="ml18-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Intercept luôn 3. Slope lần lượt 2,1,0.5. Nếu phạt bias, phương trình intercept từ 3b=9 thành (3+λ)b=9.

</details>

<details class="answer" id="ml18-starter" data-starter="ML18">
<summary>E · Mã khởi đầu và ca kiểm · ML18.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def ridge_fit(X, y, lam):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(ridge_fit([[-2], [0], [2]], [0, 4, 8], 8), [4,1])


def case_02():
    same(ridge_fit([[0],[0]], [1,5], 100), [3,0])


def case_03():
    same(ridge_fit([[0,0],[1,1],[2,2]], [1,3,5], 0), [1,1,1])


def case_04():
    rejects(ridge_fit, [[1]], [2], -1)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml18-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def ridge_fit(X, y, lam):
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),) or not np.isfinite(lam) or lam < 0:
        raise ValueError("Đầu vào không hợp lệ")
    A = np.column_stack([np.ones(len(X)), X])
    if lam == 0:
        return np.linalg.lstsq(A, y, rcond=None)[0]
    penalty = np.eye(A.shape[1])
    penalty[0, 0] = 0
    return np.linalg.solve(A.T @ A + lam * penalty, A.T @ y)
~~~

</details>

<a id="ml18-on-tap"></a>

### Ôn tập ML18

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML18-mcq-1

Penalty L2 của w=[0,0] là gì với lambda hữu hạn?

- **A** · 0
- **B** · lambda
- **C** · Không xác định

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tổng w_j²=0.

- **A** · Tổng w_j²=0.
- **B** · Không có thành phần hệ số khác 0.
- **C** · Tổng bình phương xác định.

</details>

##### ML18-mcq-2

Ridge có bảo đảm mọi hệ số khác 0 bị xóa chính xác không?

- **A** · Chỉ bias bị xóa
- **B** · Không
- **C** · Có,đó là định nghĩa L2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Shrinkage không đồng nghĩa tự động chọn feature bằng đặt 0.

- **A** · Bias trong bài không bị phạt.
- **B** · Shrinkage không đồng nghĩa tự động chọn feature bằng đặt 0.
- **C** · L2 thường co hệ số,không tạo sparsity như quy tắc threshold bắt buộc.

</details>

##### ML18-mcq-3

Nếu loss tính tổng còn penalty giữ nguyên,khi tăng số mẫu thì tỷ trọng tương đối penalty có đổi không?

- **A** · Không trong mọi trường hợp
- **B** · Mọi tham số tự bằng 0
- **C** · Có thể đổi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cần công bố normalization để lambda có ý nghĩa nhất quán.

- **A** · Data term tổng phụ thuộc số mẫu.
- **B** · Không suy ra.
- **C** · Cần công bố normalization để lambda có ý nghĩa nhất quán.

</details>

##### ML18-mcq-4

Với E=mean(e²)/2+lambda*sum(w²)/2, phần gradient L2 theo w là gì?

- **A** · lambda*w
- **B** · 2*lambda*w
- **C** · lambda

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đạo hàm lambda*w²/2 là lambda*w theo quy ước đã nêu.

- **A** · Đạo hàm lambda*w²/2 là lambda*w theo quy ước đã nêu.
- **B** · Hệ số 1/2 đã triệt tiêu 2.
- **C** · Đạo hàm phụ thuộc giá trị w.

</details>

##### ML18-mcq-5

Trong bài này, L2 có phạt bias b không?

- **A** · Chỉ phạt bias
- **B** · Không
- **C** · Có, mọi tham số bắt buộc bị phạt

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Penalty chỉ tổng trên các hệ số đặc trưng.

- **A** · Ngược quy ước đang dùng.
- **B** · Penalty chỉ tổng trên các hệ số đặc trưng.
- **C** · Quy ước bài loại bias khỏi penalty.

</details>

##### ML18-mcq-6

Lambda=0 làm thay đổi mục tiêu thế nào?

- **A** · Mọi hệ số bằng 0
- **B** · Không thể huấn luyện
- **C** · Trở về loss không phạt

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Term L2 bằng 0.

- **A** · Không có penalty không buộc hệ số bằng 0.
- **B** · Loss gốc vẫn xác định.
- **C** · Term L2 bằng 0.

</details>

##### ML18-mcq-7

Tăng lambda rất lớn có thể gây điều gì?

- **A** · Underfitting do hệ số bị co quá mạnh
- **B** · Luôn cải thiện test
- **C** · Tự thêm đặc trưng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Phạt mạnh có thể hạn chế mô hình quá mức.

- **A** · Phạt mạnh có thể hạn chế mô hình quá mức.
- **B** · Không có bảo đảm này.
- **C** · Lambda không sinh cột dữ liệu.

</details>

##### ML18-mcq-8

Vì sao cần chú ý scaling khi dùng L2?

- **A** · Vì bias phải là số nguyên
- **B** · Penalty tác động lên hệ số vốn phụ thuộc đơn vị đặc trưng
- **C** · L2 tự bỏ mọi khác biệt đơn vị

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cùng dự đoán có thể cần hệ số rất khác khi đổi đơn vị.

- **A** · Không có điều kiện đó.
- **B** · Cùng dự đoán có thể cần hệ số rất khác khi đổi đơn vị.
- **C** · Không tự động.

</details>

##### ML18-mcq-9

Có nên chọn lambda bằng test score lặp lại không?

- **A** · Có, test là nơi tối ưu
- **B** · Chỉ chọn lambda lớn nhất
- **C** · Không, dùng validation/CV

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Giữ test riêng cho đánh giá cuối.

- **A** · Làm test tham gia lựa chọn.
- **B** · Không có cơ sở luôn tốt.
- **C** · Giữ test riêng cho đánh giá cuối.

</details>

#### Tự luận và viết mã

##### ML18-practice-1

w=[3,4],lambda=0.2. Tính penalty lambda*sum(w²)/2.

<details>
<summary>Đáp án và cách kiểm</summary>

0.2×25/2=2.5.

```python
import numpy as np
w=np.array([3.,4.]);print(float(.2*np.sum(w*w)/2))
```
Kết quả: 2.5

</details>

##### ML18-practice-2

Với cùng w, tính gradient riêng của penalty.

<details>
<summary>Đáp án và cách kiểm</summary>

lambda*w=[0.6,0.8].

```python
import numpy as np
print(np.round(.2*np.array([3.,4.]),4).tolist())
```
Kết quả: [0.6, 0.8]

</details>

##### ML18-practice-3

Data loss=1.5,penalty=2.5. Tổng mục tiêu tối ưu là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

4.0; khi báo metric dữ liệu cần phân biệt data loss với loss có penalty.

```python
print(1.5+2.5)
```
Kết quả: 4.0

</details>

##### ML18-practice-4

Gradient data theo w là [1,−1],w=[2,3],lambda=0.1. Tính gradient tổng.

<details>
<summary>Đáp án và cách kiểm</summary>

[1.2,−0.7].

```python
import numpy as np
print((np.array([1.,-1.])+.1*np.array([2.,3.])).tolist())
```
Kết quả: [1.2, -0.7]

</details>

##### ML18-practice-5

w=2,gradient data=0,alpha=0.1,lambda=0.5. Tính w mới.

<details>
<summary>Đáp án và cách kiểm</summary>

2−0.1×0.5×2=1.9.

```python
w=2.;print(w-.1*.5*w)
```
Kết quả: 1.9

</details>

##### ML18-practice-6

Nếu bias b=10 và w=0,penalty trong quy ước loại bias là bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

Bằng 0 dù b lớn; không tính b² vào tổng penalty.

</details>

##### ML18-practice-7

Chỉ từ training data loss tăng sau thêm L2 có kết luận regularization thất bại không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. L2 có thể đánh đổi fit train để cải thiện validation; cần đo ngoài train và nêu loss nào đang báo.

</details>

##### ML18-practice-8

Nêu khác biệt lambda và learning rate alpha.

<details>
<summary>Đáp án và cách kiểm</summary>

Lambda thay mục tiêu qua penalty; alpha điều khiển bước tối ưu. Đổi alpha không tương đương đổi regularization.

</details>

##### ML18-practice-9

Theo quy ước penalty lambda*sum(w²)/(2m), gradient phạt là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

lambda*w/m. Khác quy ước không chia m; phải giữ công thức loss và gradient khớp nhau.

</details>

##### ML18-practice-10

Vì sao không tự phạt bias chỉ vì nó nằm trong theta[0]?

<details>
<summary>Đáp án và cách kiểm</summary>

Cần thực hiện đúng hợp đồng bài: theta[0] là bias phải loại khỏi penalty. Vị trí mảng không thay định nghĩa toán học.

</details>

##### ML18-practice-11

Mô hình đã underfit rõ. Tăng penalty có chắc sửa được không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Penalty mạnh hơn có thể hạn chế thêm khả năng fit; cần kiểm tra dữ liệu,tối ưu và độ phức tạp.

</details>

##### ML18-practice-12

Các lambda=[0,0.1,1] có validation MSE=[4,2,3]. Chọn theo tiêu chí đã cho.

<details>
<summary>Đáp án và cách kiểm</summary>

Chọn 0.1; chưa dùng test để đổi lựa chọn.

```python
lam=[0,.1,1];score=[4,2,3]
print(lam[min(range(3),key=lambda i:score[i])])
```
Kết quả: 0.1

</details>

<a id="ml19"></a>

## ML19 · Tính net input và thiết kế perceptron cho một cổng logic

[Mục lục](#muc-luc) · M5 · Mạng nơ-ron · Tiên quyết [ML09](#ml09)

<a id="ml19-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tính z = x·w+b rồi áp dụng hàm bước. Trong bài này, z ≥ 0 nhận nhãn 1.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính bốn net input và bốn nhãn theo đúng thứ tự hàng.
2. **P2** · Xác định bảng chân trị hiện thực phép AND hay OR. Ghi b làm mẫu nào âm.

<a id="ml19-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0,0], [0,1], [1,0], [1,1]])
w = np.array([1, 1])
b = -1.5
z = X @ w + b
print(z.tolist())
print((z >= 0).astype(int).tolist())
~~~

[Xem kết quả mẫu](#ml19-ket-qua)

<a id="ml19-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Diễn giải w và b bằng bất đẳng thức phân loại. Mẫu nào gần biên nhất?
2. **I2** · Giải thích kết quả khi z=0 theo quy ước của chương trình. Vì sao điều này quan trọng ở dữ liệu rời rạc?

[Đối chiếu cách giải thích](#ml19-giai-thich)

<a id="ml19-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi b thành −0.5. Kiểm kết quả [0,1,1,1].
2. **MO2** · Dùng w=[−1,−1] và b=1.5. Kiểm kết quả [1,1,1,0].
3. **MO3** · Dùng b=−1. Kiểm hai net input bằng 0 nhận nhãn 1. Đổi điều kiện sang >0 và so lại hai nhãn.

<a id="ml19-make"></a>

### E · Make 1 · Viết hàm

**`perceptron(X, w, b)`**

Nhận ma trận 2D có ít nhất một cột và vector w có đúng số cột. Trả vector nhị phân theo z≥0. Báo ValueError nếu kích thước sai.

Điền hàm. Chạy `python ML19.py`.

[Mã khởi đầu và 4 ca kiểm](#ml19-starter) · [Lời giải](#ml19-loi-giai)

<a id="ml19-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết một lượt cập nhật perceptron theo w←w+lr·(y−p)x và b←b+lr·(y−p). Duyệt X=[[0],[1]], y=[0,1], khởi đầu w=b=0, lr=1. Kiểm cuối lượt w=[1], b=0 và giải thích vì sao cần lượt khác.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml19-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml19-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[-1.5, -0.5, -0.5, 0.5]
[0, 0, 0, 1]
~~~

</details>

<details class="answer" id="ml19-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

z=[−1.5,−0.5,−0.5,0.5], nhãn [0,0,0,1] là AND. Mẫu ở biên z=0 nhận lớp 1 theo quy ước đề.

</details>

<details class="answer" id="ml19-starter" data-starter="ML19">
<summary>E · Mã khởi đầu và ca kiểm · ML19.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def perceptron(X, w, b):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(perceptron([[0,0],[1,0],[1,1]], [2,-1], -1), [0,1,1])


def case_02():
    same(perceptron([[-1],[0],[2]], [1], 0), [0,1,1])


def case_03():
    same(perceptron([[2],[3]], [0], -1), [0,0])


def case_04():
    rejects(perceptron, [[1,2]], [1], 0)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml19-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def perceptron(X, w, b):
    X, w = np.asarray(X), np.asarray(w)
    if X.ndim != 2 or X.shape[1] == 0 or w.shape != (X.shape[1],):
        raise ValueError("Shape không hợp lệ")
    return (X @ w + b >= 0).astype(int)
~~~

</details>

<a id="ml19-on-tap"></a>

### Ôn tập ML19

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML19-mcq-1

Perceptron với w=0,b=−1 cho output nào ở mọi x hữu hạn theo >=0?

- **A** · 0
- **B** · 1
- **C** · Phụ thuộc x

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Net=−1 nên step trả 0.

- **A** · Net=−1 nên step trả 0.
- **B** · Net luôn âm.
- **C** · w=0 loại mọi ảnh hưởng x.

</details>

##### ML19-mcq-2

Với w=[1,1],b=−0.5,input (0,0) có net gì?

- **A** · 0.5
- **B** · −0.5
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tổng trọng số bằng 0 rồi cộng −0.5.

- **A** · Sai dấu bias.
- **B** · Tổng trọng số bằng 0 rồi cộng −0.5.
- **C** · Đã bỏ bias.

</details>

##### ML19-mcq-3

Trong perceptron hai input,một output,w và b có bao nhiêu scalar?

- **A** · 2
- **B** · 4
- **C** · 3

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Hai trọng số và một bias.

- **A** · Thiếu bias.
- **B** · Không có bốn tham số ở cấu hình này.
- **C** · Hai trọng số và một bias.

</details>

##### ML19-mcq-4

Perceptron với net=w@x+b dùng bias để làm gì?

- **A** · Dịch ngưỡng quyết định
- **B** · Thêm mẫu dữ liệu
- **C** · Bảo đảm mọi bài toán phân tách tuyến tính

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Bias cho phép biên không phải đi qua gốc.

- **A** · Bias cho phép biên không phải đi qua gốc.
- **B** · Bias không tạo mẫu.
- **C** · Không có bảo đảm đó.

</details>

##### ML19-mcq-5

Theo quy tắc output=1 nếu net>=0,net=0 cho nhãn nào?

- **A** · Không xác định
- **B** · 1
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Dấu bằng thuộc lớp 1.

- **A** · Điểm biên đã được quy định.
- **B** · Dấu bằng thuộc lớp 1.
- **C** · Sai với quy tắc >= đã cho.

</details>

##### ML19-mcq-6

w=[1,1],b=−1.5 tạo cổng gì trên input nhị phân?

- **A** · OR
- **B** · XOR
- **C** · AND

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Chỉ (1,1) có net dương.

- **A** · OR cần nhận cả (1,0).
- **B** · Một perceptron tuyến tính không tách XOR.
- **C** · Chỉ (1,1) có net dương.

</details>

##### ML19-mcq-7

Một perceptron tuyến tính đơn có biểu diễn XOR hai bit không?

- **A** · Không
- **B** · Có chỉ cần b=0
- **C** · Có nếu đổi tên nhãn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

XOR không phân tách tuyến tính trong hai input gốc.

- **A** · XOR không phân tách tuyến tính trong hai input gốc.
- **B** · Không có đường thẳng tách đúng bốn điểm XOR.
- **C** · Đổi tên không thay cấu trúc phân tách.

</details>

##### ML19-mcq-8

net của x=[2,3],w=[1,−1],b=2 là gì?

- **A** · 7
- **B** · 1
- **C** · −1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

2−3+2=1.

- **A** · Đã mất dấu trọng số thứ hai.
- **B** · 2−3+2=1.
- **C** · Đã bỏ hoặc sai bias.

</details>

##### ML19-mcq-9

Tăng mọi w và b cùng hệ số dương có đổi nhãn step ở các net hữu hạn không?

- **A** · Luôn đổi tất cả
- **B** · Chỉ đổi số mẫu
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cùng nhân dương giữ dấu và quy tắc biên.

- **A** · Dấu net giữ nguyên.
- **B** · Phép nhân không tạo mẫu.
- **C** · Cùng nhân dương giữ dấu và quy tắc biên.

</details>

#### Tự luận và viết mã

##### ML19-practice-1

Tính net với x=[2,3],w=[1,−1],b=2.

<details>
<summary>Đáp án và cách kiểm</summary>

Net=1.

```python
import numpy as np
print(float(np.array([1.,-1.])@np.array([2.,3.])+2))
```
Kết quả: 1.0

</details>

##### ML19-practice-2

Lập bảng AND với w=[1,1],b=−1.5,step>=0.

<details>
<summary>Đáp án và cách kiểm</summary>

Output theo (0,0),(0,1),(1,0),(1,1) là [0,0,0,1].

```python
inputs=[(0,0),(0,1),(1,0),(1,1)]
print([int(x+y-1.5>=0) for x,y in inputs])
```
Kết quả: [0, 0, 0, 1]

</details>

##### ML19-practice-3

Tạo OR bằng w=[1,1],b=−0.5.

<details>
<summary>Đáp án và cách kiểm</summary>

Output [0,1,1,1].

```python
inputs=[(0,0),(0,1),(1,0),(1,1)]
print([int(x+y-.5>=0) for x,y in inputs])
```
Kết quả: [0, 1, 1, 1]

</details>

##### ML19-practice-4

Với net=[−0.1,0,0.1],step>=0 trả gì?

<details>
<summary>Đáp án và cách kiểm</summary>

[0,1,1].

```python
print([int(z>=0) for z in [-.1,0.,.1]])
```
Kết quả: [0, 1, 1]

</details>

##### ML19-practice-5

Một bạn bỏ bias của perceptron AND nói trên. Input (0,0) sẽ được dự đoán gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Net=0 nên ra 1 theo >=0,không đúng bảng AND.

```python
print(int(0+0>=0))
```
Kết quả: 1

</details>

##### ML19-practice-6

Viết đường biên với w=[2,−1],b=1.

<details>
<summary>Đáp án và cách kiểm</summary>

2x1−x2+1=0,hay x2=2x1+1.

</details>

##### ML19-practice-7

Kiểm tra x=(1,3) nằm trên biên 2x1−x2+1=0.

<details>
<summary>Đáp án và cách kiểm</summary>

Net=0,thuộc lớp 1 nếu step>=0.

```python
z=2*1-3+1
print(z)
print(int(z>=0))
```
Kết quả: 0
1

</details>

##### ML19-practice-8

Vì sao phải công bố cách xử lý net=0?

<details>
<summary>Đáp án và cách kiểm</summary>

Hai implementation dùng >0 và >=0 cho nhãn khác nhau tại biên; test cần khớp quy ước.

</details>

##### ML19-practice-9

Phân biệt net input với output của perceptron.

<details>
<summary>Đáp án và cách kiểm</summary>

Net là tổng có trọng số cộng bias,có thể là số thực bất kỳ; output step là nhãn theo ngưỡng.

</details>

##### ML19-practice-10

Nếu w dài 3 nhưng x dài 2,nên xử lý ra sao?

<details>
<summary>Đáp án và cách kiểm</summary>

Báo lỗi shape; không tự bỏ trọng số hay thêm thuộc tính giả.

</details>

##### ML19-practice-11

Giải thích vì sao không thêm XOR thành nhãn test đúng rồi gọi perceptron đã học được.

<details>
<summary>Đáp án và cách kiểm</summary>

Phải có một bộ tham số và quy tắc dự đoán tạo đúng output; hard-code nhãn theo test không chứng minh mô hình tuyến tính biểu diễn được XOR.

</details>

##### ML19-practice-12

Nhân w=[1,1],b=−1.5 với 2. Kiểm bảng AND.

<details>
<summary>Đáp án và cách kiểm</summary>

Bộ mới [2,2],b=−3 vẫn cho [0,0,0,1].

```python
print([int(2*x+2*y-3>=0) for x,y in [(0,0),(0,1),(1,0),(1,1)]])
```
Kết quả: [0, 0, 0, 1]

</details>

<a id="ml20"></a>

## ML20 · So sánh sigmoid, tanh, ReLU và vai trò phi tuyến/đạo hàm

[Mục lục](#muc-luc) · M5 · Mạng nơ-ron · Tiên quyết [ML19](#ml19)

<a id="ml20-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Dùng sigmoid, tanh hoặc ReLU để đưa tính phi tuyến vào mạng. Khi tính gradient trong bài, dùng giá trị 0 tại điểm gãy của ReLU.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Viết đầu ra của ba hàm ở z=0. Hàm nào có đầu ra âm ở z=−2?
2. **P2** · Dự đoán hàm nào có derivative bằng 1 ở z=2, rồi giải thích vì sao.

<a id="ml20-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
z = np.array([-2., 0., 2.])
s = np.exp(-np.logaddexp(0, -z))
t = np.tanh(z)
r = np.maximum(0, z)
print(np.round([s, t, r], 4).tolist())
print(np.round([s*(1-s), 1-t*t, (z>0).astype(float)], 4).tolist())
~~~

[Xem kết quả mẫu](#ml20-ket-qua)

<a id="ml20-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Chỉ ra mỗi dòng dùng z hay dùng đầu ra activation để tính derivative.
2. **I2** · So derivative sigmoid ở 0 và ở hai đầu. Dự đoán điều xảy ra khi nhân nhiều derivative nhỏ trong backprop.

[Đối chiếu cách giải thích](#ml20-giai-thich)

<a id="ml20-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi z thành [−1000,0,1000]. Kiểm sigmoid hữu hạn và đạt gần hai biên 0,1.
2. **MO2** · Đổi ReLU thành Leaky ReLU hệ số 0.1. Với z gốc, kiểm đầu ra đầu tiên −0.2 và derivative 0.1.
3. **MO3** · Đặt z=[−1,1], kiểm `ReLU(z+1)` khác `ReLU(z)+1`. Ghi đúng hai vector.

<a id="ml20-make"></a>

### E · Make 1 · Viết hàm

**`activation_and_derivative(z, kind)`**

Với mảng số z bất kỳ shape, trả tuple hai mảng cùng shape (activation, derivative) cho kind thuộc 'sigmoid', 'tanh', 'relu'. ReLU dùng đạo hàm 0 tại 0. Kind khác báo ValueError.

Điền hàm. Chạy `python ML20.py`.

[Mã khởi đầu và 4 ca kiểm](#ml20-starter) · [Lời giải](#ml20-loi-giai)

<a id="ml20-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm kiểm derivative bằng sai phân trung tâm cho z=[−2,−0.5,0.5,2], h=10⁻⁵. Với tanh và sigmoid, kiểm sai lệch lớn nhất dưới 10⁻⁶. Giải thích vì sao bỏ 0 khi kiểm ReLU.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml20-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml20-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[[0.1192, 0.5, 0.8808], [-0.964, 0.0, 0.964], [0.0, 0.0, 2.0]]
[[0.105, 0.25, 0.105], [0.0707, 1.0, 0.0707], [0.0, 0.0, 1.0]]
~~~

</details>

<details class="answer" id="ml20-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Tại 0, sigmoid=0.5, tanh=0 và ReLU=0. Tanh âm tại −2. ReLU có derivative 1 tại 2, còn hai hàm kia có derivative nhỏ hơn 1.

</details>

<details class="answer" id="ml20-starter" data-starter="ML20">
<summary>E · Mã khởi đầu và ca kiểm · ML20.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def activation_and_derivative(z, kind):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(activation_and_derivative([-1,0,2], 'relu'), [[0,0,2],[0,0,1]])


def case_02():
    same(activation_and_derivative([-1000,0,1000], 'sigmoid'), [[0,0.5,1],[0,0.25,0]])


def case_03():
    a,g = activation_and_derivative([[0,2]], 'tanh')
    same(a, [[0,np.tanh(2)]])
    same(g, [[1,1-np.tanh(2)**2]])


def case_04():
    rejects(activation_and_derivative, [1], 'linear')


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml20-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def activation_and_derivative(z, kind):
    z = np.asarray(z, dtype=float)
    if kind == "sigmoid":
        value = np.exp(-np.logaddexp(0, -z))
        return value, value * (1 - value)
    if kind == "tanh":
        value = np.tanh(z)
        return value, 1 - value**2
    if kind == "relu":
        return np.maximum(0, z), (z > 0).astype(float)
    raise ValueError("Activation không hợp lệ")
~~~

</details>

<a id="ml20-on-tap"></a>

### Ôn tập ML20

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML20-mcq-1

Tanh output t=0 có đạo hàm bao nhiêu?

- **A** · 1
- **B** · 0
- **C** · 0.25

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đạo hàm tanh là 1−t².

- **A** · Đạo hàm tanh là 1−t².
- **B** · 1−0²=1.
- **C** · Đó là sigmoid derivative tại output 0.5.

</details>

##### ML20-mcq-2

ReLU tại z=−3 bằng bao nhiêu?

- **A** · 3
- **B** · 0
- **C** · −3

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

max(0,−3)=0.

- **A** · ReLU không phải trị tuyệt đối.
- **B** · max(0,−3)=0.
- **C** · Phần âm bị chặn thành 0.

</details>

##### ML20-mcq-3

Sigmoid tại z rất dương tiến tới giá trị nào trong toán học?

- **A** · 0
- **B** · Vô cực
- **C** · 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Giới hạn khi z tiến +vô cực là 1.

- **A** · Đó là phía z rất âm.
- **B** · Sigmoid bị chặn trên.
- **C** · Giới hạn khi z tiến +vô cực là 1.

</details>

##### ML20-mcq-4

ReLU(z) được định nghĩa thế nào?

- **A** · max(0,z)
- **B** · min(0,z)
- **C** · 1/(1+exp(−z))

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

ReLU bằng 0 khi z âm và bằng z khi z dương.

- **A** · ReLU bằng 0 khi z âm và bằng z khi z dương.
- **B** · Sai nửa trục giữ lại.
- **C** · Đó là sigmoid.

</details>

##### ML20-mcq-5

Tanh tại z=0 bằng gì?

- **A** · 1
- **B** · 0
- **C** · 0.5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tanh đối xứng lẻ qua gốc.

- **A** · Tanh(0) không bão hòa dương.
- **B** · Tanh đối xứng lẻ qua gốc.
- **C** · Đó là sigmoid(0).

</details>

##### ML20-mcq-6

Đạo hàm sigmoid theo output s là gì?

- **A** · 1−s²
- **B** · s²
- **C** · s(1−s)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Áp dụng đạo hàm sigmoid.

- **A** · Đó là đạo hàm tanh theo output.
- **B** · Thiếu thành phần 1−s.
- **C** · Áp dụng đạo hàm sigmoid.

</details>

##### ML20-mcq-7

ReLU có đạo hàm cổ điển duy nhất tại 0 không?

- **A** · Không
- **B** · Có và luôn bằng 1
- **C** · Có và mọi framework bắt buộc dùng 0.5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cần nêu quy ước dùng khi triển khai tại điểm gãy.

- **A** · Cần nêu quy ước dùng khi triển khai tại điểm gãy.
- **B** · Hai đạo hàm một phía khác nhau.
- **C** · Không có quy tắc bắt buộc đó.

</details>

##### ML20-mcq-8

Nếu nhiều tầng affine không có phi tuyến, toàn mạng tương đương gì?

- **A** · Một bộ K-Means
- **B** · Một phép affine
- **C** · Mọi hàm phi tuyến

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Phép hợp các affine có thể rút gọn thành một affine.

- **A** · Không liên quan.
- **B** · Phép hợp các affine có thể rút gọn thành một affine.
- **C** · Ghép affine vẫn affine.

</details>

##### ML20-mcq-9

Sigmoid bão hòa gần 0 hoặc 1 ảnh hưởng gradient thế nào?

- **A** · Đạo hàm luôn lớn hơn 1
- **B** · Tự làm dữ liệu hết NaN
- **C** · Đạo hàm nhỏ,có thể góp phần vanishing gradient

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Tích nhiều đạo hàm nhỏ có thể làm gradient giảm mạnh.

- **A** · s(1−s) không lớn hơn 0.25.
- **B** · Activation không sửa mọi input không hợp lệ.
- **C** · Tích nhiều đạo hàm nhỏ có thể làm gradient giảm mạnh.

</details>

#### Tự luận và viết mã

##### ML20-practice-1

Tính ReLU cho [−2,0,3].

<details>
<summary>Đáp án và cách kiểm</summary>

[0,0,3].

```python
import numpy as np
print(np.maximum(0,np.array([-2.,0.,3.])).tolist())
```
Kết quả: [0.0, 0.0, 3.0]

</details>

##### ML20-practice-2

Tính sigmoid(0),tanh(0),ReLU(0).

<details>
<summary>Đáp án và cách kiểm</summary>

Lần lượt 0.5,0,0.

```python
import numpy as np
print(float(1/(1+np.exp(0.))))
print(float(np.tanh(0.)))
print(float(np.maximum(0,0.)))
```
Kết quả: 0.5
0.0
0.0

</details>

##### ML20-practice-3

Output sigmoid s=0.5. Tính đạo hàm.

<details>
<summary>Đáp án và cách kiểm</summary>

s(1−s)=0.25.

```python
s=.5
print(s*(1-s))
```
Kết quả: 0.25

</details>

##### ML20-practice-4

Output tanh t=0.6. Tính đạo hàm.

<details>
<summary>Đáp án và cách kiểm</summary>

1−t²=0.64.

```python
t=.6
print(round(1-t*t,4))
```
Kết quả: 0.64

</details>

##### ML20-practice-5

Theo quy ước ReLU derivative tại 0 bằng 0,tính đạo hàm cho [−2,0,3].

<details>
<summary>Đáp án và cách kiểm</summary>

[0,0,1].

```python
import numpy as np
z=np.array([-2.,0.,3.])
print((z>0).astype(int).tolist())
```
Kết quả: [0, 0, 1]

</details>

##### ML20-practice-6

So sánh sigmoid derivative tại output 0.5 và 0.99.

<details>
<summary>Đáp án và cách kiểm</summary>

0.25 và 0.0099; output gần bão hòa có đạo hàm nhỏ hơn.

```python
for s in [.5,.99]:
    print(round(s*(1-s),4))
```
Kết quả: 0.25
0.0099

</details>

##### ML20-practice-7

Tại sao ReLU output không phải xác suất hợp lệ nói chung?

<details>
<summary>Đáp án và cách kiểm</summary>

Output có thể lớn hơn 1. ReLU không tự chuẩn hóa thành xác suất.

</details>

##### ML20-practice-8

Viết miền giá trị sigmoid và tanh trên đầu vào thực hữu hạn về mặt toán học.

<details>
<summary>Đáp án và cách kiểm</summary>

Sigmoid trong (0,1),tanh trong (−1,1). Số học máy có thể làm tròn tới biên.

</details>

##### ML20-practice-9

Rút gọn hai tầng h=2x+1,o=3h−4 không có activation.

<details>
<summary>Đáp án và cách kiểm</summary>

o=6x−1 vẫn affine.

```python
x=2.
h=2*x+1
print(3*h-4)
print(6*x-1)
```
Kết quả: 11.0
11.0

</details>

##### ML20-practice-10

Tích năm đạo hàm đều bằng 0.1 có độ lớn bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

10⁻5; đây là minh họa nhân nhiều hệ số nhỏ,chưa phải đo gradient của một mạng cụ thể.

```python
print(f"{.1**5:.5f}")
```
Kết quả: 0.00001

</details>

##### ML20-practice-11

Vì sao không kết luận ReLU luôn tốt hơn sigmoid cho mọi tầng?

<details>
<summary>Đáp án và cách kiểm</summary>

Lựa chọn phụ thuộc vai trò tầng và bài toán; output nhị phân cần diễn giải xác suất có thể dùng sigmoid,ReLU có điểm gãy và vùng gradient 0.

</details>

##### ML20-practice-12

Một neuron ReLU có net âm cho mọi mẫu. Gradient theo net ở các mẫu ấy là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Bằng 0 trong vùng âm;nó có thể không nhận cập nhật từ đường truyền này. Không coi đây là mọi neuron của mạng đều ngừng học.

</details>

<a id="ml21"></a>

## ML21 · Tính lan truyền tiến qua tầng ẩn và tầng ra với shape nhất quán

[Mục lục](#muc-luc) · M5 · Mạng nơ-ron · Tiên quyết [ML20](#ml20)

<a id="ml21-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Ở mỗi tầng, áp dụng biến đổi affine rồi dùng hàm kích hoạt theo thiết kế mạng. Mỗi hàng là một mẫu. Mỗi neuron có một hệ số chặn.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính hai hàng Z1 và H bằng tay, đánh dấu phần tử bị ReLU đưa về 0.
2. **P2** · Dự đoán shape và hai giá trị đầu ra Y.

<a id="ml21-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[1., -1.], [2., 1.]])
W1 = np.array([[1., 2.], [1., -1.]])
b1 = np.array([0., -1.])
W2 = np.array([[2.], [-1.]])
b2 = np.array([1.])
Z1 = X @ W1 + b1
H = np.maximum(0, Z1)
Y = H @ W2 + b2
print(Z1.tolist(), H.tolist())
print(Y.shape, Y.tolist())
~~~

[Xem kết quả mẫu](#ml21-ket-qua)

<a id="ml21-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Viết shape của mọi ma trận và bias. Giải thích bias được broadcast theo trục nào.
2. **I2** · Chỉ ra tại sao hai tầng affine liên tiếp có thể gộp thành một affine khi bỏ ReLU.

[Đối chiếu cách giải thích](#ml21-giai-thich)

<a id="ml21-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đặt b1=[0,0]. Kiểm Y thành [−2,4] với X gốc.
2. **MO2** · Bỏ ReLU rồi kiểm Y bằng Y gốc cho X hiện tại. Thêm hàng [−1,−2] để quan sát khác biệt.
3. **MO3** · Thêm neuron đầu ra với trọng số [0,1], bias 0. Kiểm cột mới bằng [2,2] và Y có shape (2,2).

<a id="ml21-make"></a>

### E · Make 1 · Viết hàm

**`forward(X, W1, b1, W2, b2)`**

Thực hiện X @ W1 + b1, ReLU, rồi H @ W2 + b2. Trả ma trận 2D kể cả khi chỉ có 1 mẫu hay 1 neuron đầu ra. Các bias là vector 1D đúng độ dài. Báo ValueError khi shape không tương thích.

Điền hàm. Chạy `python ML21.py`.

[Mã khởi đầu và 4 ca kiểm](#ml21-starter) · [Lời giải](#ml21-loi-giai)

<a id="ml21-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết mạng 2 tầng tính XOR từ hai neuron ReLU. Gợi ý dùng tổng s=x₁+x₂. Với các hàng [0,0],[1,0],[0,1],[1,1], kiểm đầu ra [0,1,1,0].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml21-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml21-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[[0.0, 2.0], [3.0, 2.0]] [[0.0, 2.0], [3.0, 2.0]]
(2, 1) [[-1.0], [5.0]]
~~~

</details>

<details class="answer" id="ml21-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Z1=H=[[0,2],[3,2]], Y=[[-1],[5]] shape (2,1). b1 (2,) cộng vào mọi hàng ẩn, b2 (1,) cộng vào mọi hàng đầu ra.

</details>

<details class="answer" id="ml21-starter" data-starter="ML21">
<summary>E · Mã khởi đầu và ca kiểm · ML21.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def forward(X, W1, b1, W2, b2):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(forward([[1,-1],[2,1]], [[1,2],[1,-1]], [0,-1], [[2],[-1]], [1]), [[-1],[5]])


def case_02():
    same(forward([[-3],[2]], [[1]], [1], [[2,3]], [4,5]), [[4,5],[10,14]])


def case_03():
    same(forward([[3]], [[1]], [-3], [[2]], [1]), [[1]])


def case_04():
    rejects(forward, [[1]], [[2]], 0, [[3]], [4])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml21-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def forward(X, W1, b1, W2, b2):
    X, W1, b1, W2, b2 = (np.asarray(v, dtype=float) for v in (X, W1, b1, W2, b2))
    if any(m.ndim != 2 for m in (X, W1, W2)):
        raise ValueError("Cần ma trận 2D")
    if X.shape[1] != W1.shape[0] or b1.shape != (W1.shape[1],) or W1.shape[1] != W2.shape[0] or b2.shape != (W2.shape[1],):
        raise ValueError("Shape không tương thích")
    return np.maximum(0, X @ W1 + b1) @ W2 + b2
~~~

</details>

<a id="ml21-on-tap"></a>

### Ôn tập ML21

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML21-mcq-1

Tầng dense d=4,h=2 có bao nhiêu trọng số chưa tính bias?

- **A** · 8
- **B** · 6
- **C** · 2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Ma trận 4×2 chứa tám phần tử.

- **A** · Ma trận 4×2 chứa tám phần tử.
- **B** · Đó là tổng d+h,không phải số liên kết đầy đủ.
- **C** · Đó là số neuron output tầng.

</details>

##### ML21-mcq-2

Với hai mẫu giống hệt,forward xác định cùng weights và không có thành phần ngẫu nhiên cho kết quả thế nào?

- **A** · Một output bị bỏ
- **B** · Hai output giống nhau
- **C** · Bắt buộc khác vì vị trí hàng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cùng input và cùng phép biến đổi xác định cho cùng output.

- **A** · Không có quy tắc bỏ hàng.
- **B** · Cùng input và cùng phép biến đổi xác định cho cùng output.
- **C** · Affine/activation này không dựa index hàng.

</details>

##### ML21-mcq-3

Output sigmoid cho một nhãn nhị phân cần so ngưỡng trên đại lượng nào?

- **A** · Trọng số W1 bất kỳ
- **B** · Số neuron ẩn
- **C** · Xác suất sau sigmoid

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Quy tắc threshold áp dụng output xác suất.

- **A** · W1 không phải xác suất dự đoán của mẫu.
- **B** · Không phải score của mẫu.
- **C** · Quy tắc threshold áp dụng output xác suất.

</details>

##### ML21-mcq-4

X shape (n,d),W1 shape (d,h). X@W1 có shape gì?

- **A** · (n,h)
- **B** · (d,n)
- **C** · (h,h)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mỗi mẫu tạo h net input tầng ẩn.

- **A** · Mỗi mẫu tạo h net input tầng ẩn.
- **B** · Không khớp phép nhân.
- **C** · Sai số hàng.

</details>

##### ML21-mcq-5

Bias tầng ẩn gồm h phần tử được cộng thế nào?

- **A** · Chỉ cộng vào hàng đầu
- **B** · Cùng bias h chiều cho mỗi hàng mẫu
- **C** · Mỗi mẫu tự sinh số neuron khác nhau

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Broadcasting đúng theo trục mẫu là chủ ý của hợp đồng này.

- **A** · Bias áp dụng cho mọi mẫu.
- **B** · Broadcasting đúng theo trục mẫu là chủ ý của hợp đồng này.
- **C** · Kiến trúc h cố định.

</details>

##### ML21-mcq-6

H shape (n,h),W2 shape (h,1). Output trước activation có shape gì?

- **A** · (1,n)
- **B** · (h,1)
- **C** · (n,1)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Từng hàng mẫu cho một output.

- **A** · Đã đảo trục.
- **B** · Đó là shape W2.
- **C** · Từng hàng mẫu cho một output.

</details>

##### ML21-mcq-7

Tầng ẩn phi tuyến có vai trò gì so với chỉ affine?

- **A** · Cho phép phép hợp biểu diễn quan hệ phi tuyến
- **B** · Tự thay y thật
- **C** · Bảo đảm accuracy 100%

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Nếu bỏ mọi phi tuyến,các affine rút gọn thành một affine.

- **A** · Nếu bỏ mọi phi tuyến,các affine rút gọn thành một affine.
- **B** · Không được đổi nhãn.
- **C** · Không có bảo đảm này.

</details>

##### ML21-mcq-8

Feed-forward có cập nhật trọng số không theo định nghĩa pha tính dự đoán?

- **A** · Chỉ cập nhật bias
- **B** · Không,pha này tính activations/output với trọng số hiện tại
- **C** · Có,sửa luôn W theo y

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Forward tách khỏi backward và update.

- **A** · Không đúng định nghĩa pha forward.
- **B** · Forward tách khỏi backward và update.
- **C** · Đó thuộc bước tính gradient/tối ưu.

</details>

##### ML21-mcq-9

W1 có 3 cột,W2 có 4 hàng thì nối tầng có hợp lệ không?

- **A** · Có vì đều là ma trận
- **B** · Có nếu thêm một nhãn
- **C** · Không,số neuron ẩn phải khớp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Output width tầng trước phải bằng input width tầng sau.

- **A** · Số chiều bên trong phải bằng nhau.
- **B** · Nhãn không sửa shape trọng số.
- **C** · Output width tầng trước phải bằng input width tầng sau.

</details>

#### Tự luận và viết mã

##### ML21-practice-1

X có 5 mẫu,2 thuộc tính,tầng ẩn 3 neuron,output 1 neuron. Nêu shape W1,b1,W2,b2 theo quy ước hàng là mẫu.

<details>
<summary>Đáp án và cách kiểm</summary>

W1=(2,3),b1=(3,),W2=(3,1),b2=(1,).

</details>

##### ML21-practice-2

x=[[1,2]],W1=[[1,0],[0,1]],b1=[−2,1]. Tính z1.

<details>
<summary>Đáp án và cách kiểm</summary>

z1=[[-1,3]].

```python
import numpy as np
X=np.array([[1.,2.]]);W=np.eye(2);b=np.array([-2.,1.])
print((X@W+b).tolist())
```
Kết quả: [[-1.0, 3.0]]

</details>

##### ML21-practice-3

Áp dụng ReLU lên z1=[[-1,3]].

<details>
<summary>Đáp án và cách kiểm</summary>

h=[[0,3]].

```python
import numpy as np
print(np.maximum(0,np.array([[-1.,3.]])).tolist())
```
Kết quả: [[0.0, 3.0]]

</details>

##### ML21-practice-4

h=[[0,3]],W2=[[2],[1]],b2=[−1]. Tính net output.

<details>
<summary>Đáp án và cách kiểm</summary>

z2=[[2]].

```python
import numpy as np
h=np.array([[0.,3.]])
print((h@np.array([[2.],[1.]])+np.array([-1.])).tolist())
```
Kết quả: [[2.0]]

</details>

##### ML21-practice-5

Áp dụng sigmoid lên output net=2,in bốn chữ số.

<details>
<summary>Đáp án và cách kiểm</summary>

Xấp xỉ 0.8808.

```python
import numpy as np
print(round(float(1/(1+np.exp(-2.))),4))
```
Kết quả: 0.8808

</details>

##### ML21-practice-6

Một batch có hai mẫu,weight identity,bias=[1,−1]. Tính affine cho [[0,2],[3,4]].

<details>
<summary>Đáp án và cách kiểm</summary>

Kết quả [[1,1],[4,3]].

```python
import numpy as np
X=np.array([[0.,2.],[3.,4.]])
print((X@np.eye(2)+np.array([1.,-1.])).tolist())
```
Kết quả: [[1.0, 1.0], [4.0, 3.0]]

</details>

##### ML21-practice-7

Vì sao cần giữ net z trước activation nếu sắp tính backprop?

<details>
<summary>Đáp án và cách kiểm</summary>

Đạo hàm activation có thể cần z hoặc output activation; lưu cache giúp tính backward đúng theo cùng forward.

</details>

##### ML21-practice-8

Đầu vào một mẫu shape (2,) có nhất thiết cùng shape output với (1,2) không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Vector 1D có thể làm mất trục batch trong kết quả. Cần quy định rõ API nhận batch 2D hay một mẫu 1D.

</details>

##### ML21-practice-9

Nếu đổi thứ tự mẫu trong batch nhưng không đổi weight,mỗi output tương ứng thay đổi thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Với các affine và activation độc lập theo hàng,output hoán vị theo cùng thứ tự mẫu; không tự hoán vị nhãn riêng.

</details>

##### ML21-practice-10

Đếm tham số mạng d=2,h=3,output=1 có bias cả hai tầng.

<details>
<summary>Đáp án và cách kiểm</summary>

W1 có6,b1 có3,W2 có3,b2 có1,tổng13.

```python
d,h,o=2,3,1
print(d*h+h+h*o+o)
```
Kết quả: 13

</details>

##### ML21-practice-11

Bỏ phi tuyến giữa hai affine có thể vẫn tạo đường biên XOR đúng bằng mạng tuyến tính thuần không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Hợp affine vẫn affine nên không tạo khả năng biểu diễn XOR trong không gian input gốc bằng một ngưỡng tuyến tính.

</details>

##### ML21-practice-12

Một bạn dùng W1.T thay W1 chỉ vì phép nhân báo lỗi. Cần kiểm gì trước?

<details>
<summary>Đáp án và cách kiểm</summary>

Đối chiếu quy ước hàng/cột và số input/output neuron; transpose tùy tiện có thể chạy nhưng đổi ý nghĩa kiến trúc.

</details>

<a id="ml22"></a>

## ML22 · Tính delta và gradient trọng số bằng quy tắc chuỗi

[Mục lục](#muc-luc) · M5 · Mạng nơ-ron · Tiên quyết [ML21](#ml21)

<a id="ml22-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Truyền gradient từ loss về các tầng trước bằng quy tắc chuỗi. Tính mọi gradient trước khi cập nhật trọng số.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính h và p từ hai preactivation. Dự đoán d2 và d1.
2. **P2** · Viết bốn gradient theo thứ tự w1,b1,w2,b2.

<a id="ml22-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x, y = 2., 1.
w1, b1, w2, b2 = 0., 0., 2., -1.
h = np.exp(-np.logaddexp(0, -(w1*x + b1)))
p = np.exp(-np.logaddexp(0, -(w2*h + b2)))
d2 = p - y
d1 = d2 * w2 * h * (1 - h)
print(h, p, d2, d1)
print([d1*x, d1, d2*h, d2])
~~~

[Xem kết quả mẫu](#ml22-ket-qua)

<a id="ml22-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Lần theo đường từ loss BCE về w1. Xác định thừa số bắt nguồn từ đạo hàm sigmoid tầng ẩn.
2. **I2** · Giải thích vì sao d1 cần w2 cũ. Tính tham số mới khi lr=0.1 sau khi đã có đủ gradient.

[Đối chiếu cách giải thích](#ml22-giai-thich)

<a id="ml22-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi y thành 0, giữ x và tham số. Kiểm cả bốn gradient đổi dấu.
2. **MO2** · Đặt w2=0. Kiểm gradient tầng ẩn bằng 0 và gradient tầng ra vẫn khác 0.
3. **MO3** · Đặt x=0 ở ví dụ gốc. Kiểm gradient w1=0, còn gradient b1=−0.25.

<a id="ml22-make"></a>

### E · Make 1 · Viết hàm

**`backprop_1d(x, y, params)`**

x,y là hai vector cùng độ dài dương, y nhị phân, params có đúng bốn số (w1,b1,w2,b2). Với một neuron sigmoid mỗi tầng và BCE trung bình, trả mảng bốn gradient tương ứng. Báo ValueError nếu shape hoặc y sai.

Điền hàm. Chạy `python ML22.py`.

[Mã khởi đầu và 4 ca kiểm](#ml22-starter) · [Lời giải](#ml22-loi-giai)

<a id="ml22-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết loss BCE của mạng rồi kiểm cả bốn gradient bằng sai phân trung tâm, h=10⁻⁵. Dùng x=[−1,2], y=[0,1], params=[0.1,−0.2,0.3,0.4]. Kiểm sai lệch lớn nhất dưới 10⁻⁶.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml22-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml22-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
0.5 0.5 -0.5 -0.25
[np.float64(-0.5), np.float64(-0.25), np.float64(-0.25), np.float64(-0.5)]
~~~

</details>

<details class="answer" id="ml22-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

h=p=0.5, d2=−0.5, d1=−0.25. Gradient (−0.5,−0.25,−0.25,−0.5). Sau bước lr=0.1, tham số là (0.05,0.025,2.025,−0.95).

</details>

<details class="answer" id="ml22-starter" data-starter="ML22">
<summary>E · Mã khởi đầu và ca kiểm · ML22.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def backprop_1d(x, y, params):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(backprop_1d([2], [1], [0,0,2,-1]), [-0.5,-0.25,-0.25,-0.5])


def case_02():
    same(backprop_1d([0,2], [0,1], [0,0,2,-1]), [-0.25,0,0,0])


def case_03():
    same(backprop_1d([2], [0], [0,0,0,0]), [0,0,0.25,0.5])


def case_04():
    rejects(backprop_1d, [1], [3], [0,0,1,0])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml22-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def backprop_1d(x, y, params):
    x, y, params = (np.asarray(v, dtype=float) for v in (x, y, params))
    if x.ndim != 1 or x.size == 0 or x.shape != y.shape or params.shape != (4,) or not np.isin(y, [0, 1]).all():
        raise ValueError("Đầu vào không hợp lệ")
    w1, b1, w2, b2 = params
    h = np.exp(-np.logaddexp(0, -(w1*x + b1)))
    p = np.exp(-np.logaddexp(0, -(w2*h + b2)))
    d2 = p - y
    d1 = d2 * w2 * h * (1 - h)
    return np.array([(d1*x).mean(), d1.mean(), (d2*h).mean(), d2.mean()])
~~~

</details>

<a id="ml22-on-tap"></a>

### Ôn tập ML22

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML22-mcq-1

Nếu alpha=0 trong công thức update thì tham số đổi thế nào về đại số?

- **A** · Không đổi
- **B** · Thành 0
- **C** · Đổi dấu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

W_new=W−0×g=W;API có thể từ chối alpha=0 nếu hợp đồng đòi dương.

- **A** · W_new=W−0×g=W;API có thể từ chối alpha=0 nếu hợp đồng đòi dương.
- **B** · Nhân gradient với 0 chứ không nhân tham số với 0.
- **C** · Không có phép đổi dấu đó.

</details>

##### ML22-mcq-2

Với loss theo output,u là upstream và activation derivative=0.25,delta bằng gì?

- **A** · u+0.25
- **B** · 0.25u
- **C** · u/0.25

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Nhân upstream với đạo hàm activation.

- **A** · Không cộng hai đạo hàm.
- **B** · Nhân upstream với đạo hàm activation.
- **C** · Quy tắc chuỗi nhân,không chia.

</details>

##### ML22-mcq-3

Một weight không có đường phụ thuộc tới loss hiện tại có gradient gì?

- **A** · 1
- **B** · Bằng weight
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Đạo hàm bằng 0 nếu loss không phụ thuộc weight đó.

- **A** · Không có đóng góp thay đổi loss.
- **B** · Không có quy tắc này.
- **C** · Đạo hàm bằng 0 nếu loss không phụ thuộc weight đó.

</details>

##### ML22-mcq-4

Nếu delta2 shape (n,o),W2 shape (h,o),gradient truyền về activation ẩn có shape gì?

- **A** · (n,h) qua delta2@W2.T
- **B** · (h,n) qua W2@delta2
- **C** · (n,o) không cần weight

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Nhân với chuyển vị weight đưa gradient về h neuron ẩn.

- **A** · Nhân với chuyển vị weight đưa gradient về h neuron ẩn.
- **B** · Thường sai phép nhân hoặc quy ước batch.
- **C** · Chưa truyền qua ánh xạ output.

</details>

##### ML22-mcq-5

Trong backprop,cần dùng trọng số output cũ hay đã update để tính delta ẩn của cùng lượt?

- **A** · Trọng số ngẫu nhiên mới
- **B** · Trọng số của forward hiện tại
- **C** · Trọng số vừa update trước khi tính delta ẩn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tính toàn bộ gradient trước khi update tham số.

- **A** · Không còn đạo hàm mạng đã chạy.
- **B** · Tính toàn bộ gradient trước khi update tham số.
- **C** · Làm gradient không còn thuộc cùng điểm tham số.

</details>

##### ML22-mcq-6

Theo batch mean loss,gradient bias tầng là gì khi delta chứa đạo hàm loss từng mẫu?

- **A** · Sum theo trục neuron
- **B** · Luôn bằng 0
- **C** · Mean delta theo trục mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Tổng đóng góp các mẫu rồi chia n theo quy ước mean.

- **A** · Không cho vector bias đúng chiều.
- **B** · Bias vẫn ảnh hưởng output.
- **C** · Tổng đóng góp các mẫu rồi chia n theo quy ước mean.

</details>

##### ML22-mcq-7

Với sigmoid output s,đạo hàm activation là gì?

- **A** · s*(1−s)
- **B** · 1−s
- **C** · s

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đạo hàm cần nhân theo quy tắc chuỗi.

- **A** · Đạo hàm cần nhân theo quy tắc chuỗi.
- **B** · Thiếu thừa số s.
- **C** · Không phải đạo hàm sigmoid.

</details>

##### ML22-mcq-8

Gradient weight W1 shape (d,h) có shape gì?

- **A** · (n,h)
- **B** · (d,h)
- **C** · (h,d) trong mọi quy ước

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Cập nhật từng trọng số cần gradient tương ứng.

- **A** · Đó là shape theo batch,không phải tham số.
- **B** · Cập nhật từng trọng số cần gradient tương ứng.
- **C** · Theo quy ước W1 này,gradient phải cùng shape W1.

</details>

##### ML22-mcq-9

Với loss mean,delta đã chia n trước đó,có nên chia n thêm lần nữa khi dựng gradient không?

- **A** · Có,bất kỳ công thức nào cũng chia hai lần
- **B** · Chỉ chia hai lần cho bias
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Phải theo dõi normalization nằm ở đâu,chỉ áp dụng đúng một lần.

- **A** · Làm gradient nhỏ sai hệ số n.
- **B** · Cả hai gradient phải cùng quy ước.
- **C** · Phải theo dõi normalization nằm ở đâu,chỉ áp dụng đúng một lần.

</details>

#### Tự luận và viết mã

##### ML22-practice-1

H=[[1,2],[3,4]],delta2=[[1],[−1]]. Tính H.T@delta2/2.

<details>
<summary>Đáp án và cách kiểm</summary>

Gradient W2=[[-1],[-1]].

```python
import numpy as np
H=np.array([[1.,2.],[3.,4.]]);delta=np.array([[1.],[-1.]])
print((H.T@delta/2).tolist())
```
Kết quả: [[-1.0], [-1.0]]

</details>

##### ML22-practice-2

Delta=[[1,3],[3,5]],tính mean theo mẫu làm gradient bias.

<details>
<summary>Đáp án và cách kiểm</summary>

[2,4].

```python
import numpy as np
print(np.array([[1.,3.],[3.,5.]]).mean(axis=0).tolist())
```
Kết quả: [2.0, 4.0]

</details>

##### ML22-practice-3

Một sigmoid có output 0.5,gradient từ phía sau là 2. Tính gradient theo net.

<details>
<summary>Đáp án và cách kiểm</summary>

2×0.5×0.5=0.5.

```python
s=.5;upstream=2.
print(upstream*s*(1-s))
```
Kết quả: 0.5

</details>

##### ML22-practice-4

Delta output=[[2]],W2=[[1],[−3]]. Tính gradient theo activation ẩn trước nhân đạo hàm activation.

<details>
<summary>Đáp án và cách kiểm</summary>

[[2,−6]].

```python
import numpy as np
print((np.array([[2.]])@np.array([[1.],[-3.]]).T).tolist())
```
Kết quả: [[2.0, -6.0]]

</details>

##### ML22-practice-5

Activation ẩn sigmoid=[0.5,0.5],upstream=[2,−6]. Tính delta ẩn.

<details>
<summary>Đáp án và cách kiểm</summary>

[0.5,−1.5].

```python
import numpy as np
s=np.array([.5,.5]);g=np.array([2.,-6.])
print((g*s*(1-s)).tolist())
```
Kết quả: [0.5, -1.5]

</details>

##### ML22-practice-6

X=[[1,2]],delta1=[[0.5,−1.5]]. Tính gradient W1 cho một mẫu.

<details>
<summary>Đáp án và cách kiểm</summary>

[[0.5,−1.5],[1,−3]].

```python
import numpy as np
print((np.array([[1.,2.]]).T@np.array([[.5,-1.5]])).tolist())
```
Kết quả: [[0.5, -1.5], [1.0, -3.0]]

</details>

##### ML22-practice-7

Vì sao không cập nhật W2 ngay sau tính gradient W2 rồi dùng nó tính gradient W1?

<details>
<summary>Đáp án và cách kiểm</summary>

Gradient W1 phải thuộc cùng mạng và tham số đã dùng forward. Dùng W2 mới làm trộn hai điểm tham số.

</details>

##### ML22-practice-8

Theo quy ước delta là đạo hàm từng mẫu chưa chia n,viết gradient W=X.T@delta/n. Nếu dùng sum loss thì khác gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Gradient sum không chia n. Cả loss,delta và gradient phải nhất quán để tránh nhân/chia n sai.

</details>

##### ML22-practice-9

Phân biệt forward cache và nhãn y trong backprop.

<details>
<summary>Đáp án và cách kiểm</summary>

Cache chứa input/net/activation của lượt forward; y xác định sai số theo loss. Không thay activation bằng nhãn khi nhân đạo hàm.

</details>

##### ML22-practice-10

W=2,gradient=−3,alpha=0.1. Tính cập nhật.

<details>
<summary>Đáp án và cách kiểm</summary>

W_new=2.3.

```python
print(2.-.1*(-3.))
```
Kết quả: 2.3

</details>

##### ML22-practice-11

Một neuron ReLU net âm có đạo hàm activation 0. Upstream khác 0 thì delta theo net ra sao?

<details>
<summary>Đáp án và cách kiểm</summary>

Bằng 0 ở điểm đó do nhân đạo hàm activation; không được bỏ thừa số activation chỉ vì upstream khác 0.

</details>

##### ML22-practice-12

Vì sao phép nhân elementwise trong delta không thay bằng @ tùy ý?

<details>
<summary>Đáp án và cách kiểm</summary>

Delta thường nhân đạo hàm từng neuron cùng vị trí. @ trộn/tổng theo chiều ma trận,có thể sai shape hoặc nghĩa dù đôi lúc chạy được.

</details>

<a id="ml23"></a>

## ML23 · Thực hiện một vòng Lloyd K-Means và theo dõi SSE nội cụm

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML01](#ml01)

<a id="ml23-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Gán từng điểm vào tâm cụm gần nhất. Tính lại tâm bằng trung bình các điểm trong cụm. Đo SSE nội cụm bằng tổng bình phương khoảng cách Euclid đến tâm.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính khoảng cách bình phương cho x=2 và x=7 rồi viết vector nhãn.
2. **P2** · Dự đoán hai centroid mới và SSE trước, sau khi dời tâm với cùng nhãn.

<a id="ml23-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0.], [2.], [7.], [9.]])
centers = np.array([[0.], [7.]])
d2 = ((X[:, None, :] - centers[None, :, :])**2).sum(axis=2)
labels = d2.argmin(axis=1)
updated = np.array([X[labels == k].mean(axis=0) for k in range(len(centers))])
print(labels.tolist(), updated.ravel().tolist())
print(d2[np.arange(len(X)), labels].sum(), ((X - updated[labels])**2).sum())
~~~

[Xem kết quả mẫu](#ml23-ket-qua)

<a id="ml23-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Ghi shape của tensor hiệu và của d2. Giải thích trục dùng trong argmin.
2. **I2** · Giải thích vì sao trung bình tối thiểu hóa SSE trong một cụm đã gán.

[Đối chiếu cách giải thích](#ml23-giai-thich)

<a id="ml23-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi tâm ban đầu thành [2,9]. Kiểm một vòng cho cùng centroid cuối và cùng nhãn với ví dụ.
2. **MO2** · Đổi tâm thành [0,0]. Giữ tâm cũ cho cụm rỗng, kiểm nhãn đều bằng 0 và tâm mới [4.5,0].
3. **MO3** · Dùng X=[[0,0],[0,2],[6,0],[6,2]], tâm [[0,0],[6,0]]. Kiểm hai tâm cuối [[0,1],[6,1]] và SSE=4.

<a id="ml23-make"></a>

### E · Make 1 · Viết hàm

**`lloyd_step(X, centers)`**

Nhận X và centers là hai ma trận 2D hữu hạn, không rỗng, cùng số cột dương. Trả (labels, centers_mới, SSE sau cập nhật với labels vừa gán). Hòa khoảng cách chọn chỉ số cụm nhỏ. Cụm rỗng giữ tâm cũ. Báo ValueError khi shape hoặc giá trị sai.

Điền hàm. Chạy `python ML23.py`.

[Mã khởi đầu và 4 ca kiểm](#ml23-starter) · [Lời giải](#ml23-loi-giai)

<a id="ml23-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự chạy Lloyd đến khi nhãn ổn định hoặc đủ 20 vòng. Với X=[[0],[2],[8],[10]] và tâm [0,2], kiểm SSE qua các vòng là 104/3, 4 rồi 4. Ghi rõ cách phát hiện hội tụ.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml23-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml23-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0, 0, 1, 1] [1.0, 8.0]
8.0 4.0
~~~

</details>

<details class="answer" id="ml23-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Tại x=2, d²=[4,25]; tại x=7, d²=[49,0]. Nhãn [0,0,1,1], tâm sau cập nhật [1,8], SSE từ 8 xuống 4.

</details>

<details class="answer" id="ml23-starter" data-starter="ML23">
<summary>E · Mã khởi đầu và ca kiểm · ML23.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def lloyd_step(X, centers):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    labels, centers, sse = lloyd_step([[0],[2],[7],[9]], [[0],[7]])
    same(labels, [0,0,1,1])
    same(centers, [[1],[8]])
    same(sse, 4)


def case_02():
    labels, centers, sse = lloyd_step([[0],[1],[2]], [[0],[2]])
    same(labels, [0,0,1])
    same(centers, [[0.5],[2]])
    same(sse, 0.5)


def case_03():
    labels, centers, sse = lloyd_step([[0],[4]], [[0],[0]])
    same(centers, [[2],[0]])
    same(sse, 8)


def case_04():
    rejects(lloyd_step, [[0]], [[0,1]])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml23-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def lloyd_step(X, centers):
    X, centers = np.asarray(X, dtype=float), np.asarray(centers, dtype=float)
    if X.ndim != 2 or centers.ndim != 2 or min(X.shape) == 0 or min(centers.shape) == 0 or X.shape[1] != centers.shape[1] or not np.isfinite(X).all() or not np.isfinite(centers).all():
        raise ValueError("Đầu vào không hợp lệ")
    d2 = ((X[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
    labels = d2.argmin(axis=1)
    updated = centers.copy()
    for i in range(len(centers)):
        members = X[labels == i]
        if len(members):
            updated[i] = members.mean(axis=0)
    return labels, updated, float(((X - updated[labels]) ** 2).sum())
~~~

</details>

<a id="ml23-on-tap"></a>

### Ôn tập ML23

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML23-mcq-1

Nếu một cụm chỉ chứa mẫu [2,5],tâm mean mới là gì?

- **A** · [2,5]
- **B** · [0,0]
- **C** · [5,2]

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mean một vector là chính vector đó.

- **A** · Mean một vector là chính vector đó.
- **B** · Không có bước trừ mẫu để về 0.
- **C** · Không đổi thứ tự đặc trưng.

</details>

##### ML23-mcq-2

Đổi tên cụm 0 và 1 cùng đổi centroid tương ứng có đổi SSE không?

- **A** · Chỉ khi cụm cân bằng
- **B** · Không
- **C** · Có vì tên số khác

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Hoán vị tên không đổi phân hoạch hay khoảng cách.

- **A** · Không cần cân bằng.
- **B** · Hoán vị tên không đổi phân hoạch hay khoảng cách.
- **C** · SSE dùng khoảng cách tới tâm tương ứng.

</details>

##### ML23-mcq-3

Nếu SSE âm lớn sau phép tính khoảng cách bình phương,nên nghi gì?

- **A** · Đã tìm cực tiểu tốt hơn 0
- **B** · Thuật toán luôn cho SSE âm
- **C** · Lỗi tính toán hoặc triển khai

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Kiểm dtype,công thức và dữ liệu trước khi báo kết quả.

- **A** · Tổng bình phương không âm.
- **B** · Sai định nghĩa.
- **C** · Kiểm dtype,công thức và dữ liệu trước khi báo kết quả.

</details>

##### ML23-mcq-4

Bước assignment của K-Means làm gì?

- **A** · Gán mỗi mẫu cho centroid gần nhất
- **B** · Cập nhật nhãn thật
- **C** · Chọn ngẫu nhiên mọi centroid sau mỗi bước

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Giữ centroid hiện tại và so khoảng cách.

- **A** · Giữ centroid hiện tại và so khoảng cách.
- **B** · K-Means không cần nhãn thật để fit.
- **C** · Không phải assignment chuẩn.

</details>

##### ML23-mcq-5

Centroid mới của một cụm không rỗng được tính thế nào trong Lloyd Euclid bình phương?

- **A** · Tổng nhãn các mẫu
- **B** · Trung bình vector các mẫu trong cụm
- **C** · Mẫu đầu tiên bất kỳ

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mean tối thiểu tổng khoảng cách bình phương trong cụm cố định.

- **A** · Không dùng nhãn thật.
- **B** · Mean tối thiểu tổng khoảng cách bình phương trong cụm cố định.
- **C** · Không tối thiểu SSE nói chung.

</details>

##### ML23-mcq-6

SSE nội cụm cộng đại lượng nào?

- **A** · Khoảng cách giữa mọi cặp centroid
- **B** · Số mẫu có nhãn dự đoán sai
- **C** · Bình phương khoảng cách mẫu đến centroid được gán

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

SSE đo độ phân tán quanh tâm cụm.

- **A** · Đó không phải SSE mục tiêu này.
- **B** · Clustering không có nhãn dự đoán đúng/sai như classifier.
- **C** · SSE đo độ phân tán quanh tâm cụm.

</details>

##### ML23-mcq-7

Cụm rỗng sau assignment cần xử lý thế nào?

- **A** · Theo quy tắc được công bố
- **B** · Lấy mean rỗng rồi chấp nhận NaN
- **C** · Tự xóa mẫu test

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Có thể giữ tâm cũ hoặc khởi tạo lại theo quy tắc cụ thể.

- **A** · Có thể giữ tâm cũ hoặc khởi tạo lại theo quy tắc cụ thể.
- **B** · NaN không phải centroid hợp lệ.
- **C** · Không liên quan và thay dữ liệu.

</details>

##### ML23-mcq-8

K-Means có bảo đảm luôn tìm cực tiểu toàn cục không?

- **A** · Có nếu có hai đặc trưng
- **B** · Không
- **C** · Có nếu dùng đúng NumPy

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Kết quả có thể phụ thuộc khởi tạo và cực tiểu địa phương.

- **A** · Số chiều hai không bảo đảm.
- **B** · Kết quả có thể phụ thuộc khởi tạo và cực tiểu địa phương.
- **C** · Thư viện không thay bảo đảm thuật toán.

</details>

##### ML23-mcq-9

Tại sao cần scaling phù hợp trước K-Means?

- **A** · Để số mẫu bằng K
- **B** · Để tự biết nhãn đúng
- **C** · Khoảng cách có thể bị thuộc tính thang đo lớn chi phối

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

K-Means dùng khoảng cách giữa các vector.

- **A** · Scaling không đổi số mẫu.
- **B** · Scaling không cung cấp nhãn.
- **C** · K-Means dùng khoảng cách giữa các vector.

</details>

#### Tự luận và viết mã

##### ML23-practice-1

Mẫu một chiều x=3,tâm [0,10]. Gán vào tâm nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Tâm 0 vì khoảng cách 3<7.

```python
centers=[0.,10.];x=3.
print(min(range(2),key=lambda j:abs(x-centers[j])))
```
Kết quả: 0

</details>

##### ML23-practice-2

Cụm gồm [1,3,5],tính tâm mới.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=3.

```python
print(sum([1.,3.,5.])/3)
```
Kết quả: 3.0

</details>

##### ML23-practice-3

Cụm vector [[0,2],[2,4]],tính centroid.

<details>
<summary>Đáp án và cách kiểm</summary>

[1,3].

```python
import numpy as np
print(np.array([[0.,2.],[2.,4.]]).mean(axis=0).tolist())
```
Kết quả: [1.0, 3.0]

</details>

##### ML23-practice-4

Tính SSE của cụm [1,3,5] với tâm 3.

<details>
<summary>Đáp án và cách kiểm</summary>

4+0+4=8.

```python
import numpy as np
x=np.array([1.,3.,5.]);print(float(np.sum((x-3)**2)))
```
Kết quả: 8.0

</details>

##### ML23-practice-5

Dữ liệu [0,2,8,10],tâm cũ [0,10]. Assignment và update một vòng.

<details>
<summary>Đáp án và cách kiểm</summary>

Hai cụm [0,2],[8,10];tâm mới [1,9].

```python
import numpy as np
x=np.array([0.,2.,8.,10.]);c=np.array([0.,10.])
labels=np.argmin((x[:,None]-c[None,:])**2,axis=1)
print(labels.tolist())
print([float(x[labels==i].mean()) for i in range(2)])
```
Kết quả: [0, 0, 1, 1]
[1.0, 9.0]

</details>

##### ML23-practice-6

Tính SSE trước và sau update của ví dụ trên.

<details>
<summary>Đáp án và cách kiểm</summary>

SSE trước=8,sau=4.

```python
import numpy as np
x=np.array([0.,2.,8.,10.])
for c in [[0.,10.],[1.,9.]]:
    d=(x[:,None]-np.array(c)[None,:])**2
    print(float(d.min(axis=1).sum()))
```
Kết quả: 8.0
4.0

</details>

##### ML23-practice-7

Vì sao không trung bình nhãn cụm để tính centroid?

<details>
<summary>Đáp án và cách kiểm</summary>

Nhãn cụm là mã gán,chỉ số không mang tọa độ. Centroid phải lấy mean vector đặc trưng của các mẫu được gán.

</details>

##### ML23-practice-8

Một mẫu cách hai centroid bằng nhau. Cần quy định gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Cách phá hòa,chẳng hạn chọn chỉ số tâm nhỏ hơn. Quy tắc giúp tái lập và kiểm thử assignment.

</details>

##### ML23-practice-9

Nêu hai điều kiện dừng thường dùng và giới hạn của chúng.

<details>
<summary>Đáp án và cách kiểm</summary>

Giới hạn số vòng và độ dịch tâm dưới tolerance; cũng có thể kiểm nhãn không đổi. Phải nêu tolerance và xử lý cụm rỗng; dừng không chứng minh cực tiểu toàn cục.

</details>

##### ML23-practice-10

Vì sao so sánh hai lần chạy cần giữ cùng dữ liệu và ghi seed?

<details>
<summary>Đáp án và cách kiểm</summary>

Khởi tạo ảnh hưởng kết quả; giữ dữ liệu/seed giúp tách ảnh hưởng thuật toán khỏi thay đổi thí nghiệm.

</details>

##### ML23-practice-11

K=1 trên [0,2,4],centroid và SSE tối ưu là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Tâm=2,SSE=8.

```python
import numpy as np
x=np.array([0.,2.,4.]);c=x.mean()
print(float(c))
print(float(np.sum((x-c)**2)))
```
Kết quả: 2.0
8.0

</details>

##### ML23-practice-12

Có thể gọi SSE train nhỏ là bằng chứng phân cụm có ý nghĩa nghiệp vụ không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. SSE chỉ phản ánh mục tiêu khoảng cách trên dữ liệu/thang đo đã chọn;cần diễn giải cụm và đánh giá phù hợp.

</details>

<a id="ml24"></a>

## ML24 · Đánh giá phân cụm bằng so sánh cặp và phân biệt internal/external validation

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML23](#ml23)

<a id="ml24-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** So quan hệ cùng cụm của từng cặp điểm. Rand tính cả cặp được tách trong cả hai phân hoạch. Mẫu số Jaccard gồm các cặp cùng cụm ở ít nhất một phân hoạch.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Liệt kê sáu cặp chỉ số và phân loại thành a,b,c,d.
2. **P2** · Tính Rand và Jaccard. Dự đoán vì sao hai số khác nhau.

<a id="ml24-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
from itertools import combinations
truth = [0, 0, 1, 1]
pred = [2, 2, 2, 3]
counts = {(a,b): 0 for a in (False,True) for b in (False,True)}
for i, j in combinations(range(len(truth)), 2):
    counts[truth[i] == truth[j], pred[i] == pred[j]] += 1
a, b, c, d = [counts[key] for key in [(True,True),(True,False),(False,True),(False,False)]]
print(a, b, c, d)
print((a+d)/(a+b+c+d), a/(a+b+c))
~~~

[Xem kết quả mẫu](#ml24-ket-qua)

<a id="ml24-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Đổi tên nhãn của pred theo ánh xạ song ánh. Giải thích vì sao chỉ số giữ nguyên.
2. **I2** · Giải thích vì sao hai metric này thuộc external validation nếu truth là nhãn tham chiếu. Nêu dữ liệu cần cho silhouette, một metric internal.

[Đối chiếu cách giải thích](#ml24-giai-thich)

<a id="ml24-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Thay pred bằng [9,9,8,8]. Kiểm Rand=Jaccard=1.
2. **MO2** · Thay pred bằng [0,1,2,3]. Kiểm Rand=4/6 và Jaccard=0.
3. **MO3** · Cho cả hai phân hoạch đều là singleton. Kiểm a+b+c=0 và bổ sung quy ước Jaccard=1 cho hai tập cặp rỗng.

<a id="ml24-make"></a>

### E · Make 1 · Viết hàm

**`pair_scores(a, b)`**

Hai vector nhãn nguyên 1D cùng độ dài, tối thiểu hai phần tử. Trả (Rand, Jaccard). Dùng Jaccard=1 nếu cả hai không có cặp cùng cụm. Báo ValueError nếu đầu vào sai shape.

Điền hàm. Chạy `python ML24.py`.

[Mã khởi đầu và 4 ca kiểm](#ml24-starter) · [Lời giải](#ml24-loi-giai)

<a id="ml24-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết silhouette cho một điểm trong cụm có ít nhất hai điểm, khoảng cách Euclid. Với X=[0,2,8,10], nhãn [0,0,1,1], tính silhouette tại chỉ số 0. Kiểm a=2, b=9 và s=7/9.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml24-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml24-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
1 1 2 2
0.5 0.25
~~~

</details>

<details class="answer" id="ml24-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

a=1,b=1,c=2,d=2. Rand=3/6 và Jaccard=1/4. Đổi tên nhãn giữ nguyên các phép so cùng cụm.

</details>

<details class="answer" id="ml24-starter" data-starter="ML24">
<summary>E · Mã khởi đầu và ca kiểm · ML24.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def pair_scores(a, b):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(pair_scores([0,0,1,1], [2,2,2,3]), [0.5,0.25])


def case_02():
    same(pair_scores([0,1,2], [8,3,4]), [1,1])


def case_03():
    same(pair_scores([0,0,0], [8,8,2]), [1/3,1/3])


def case_04():
    rejects(pair_scores, [0], [0])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml24-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def pair_scores(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.ndim != 1 or a.shape != b.shape or a.size < 2:
        raise ValueError("Cần hai phân hoạch cùng độ dài ≥ 2")
    i, j = np.triu_indices(a.size, k=1)
    left, right = a[i] == a[j], b[i] == b[j]
    union = np.count_nonzero(left | right)
    match = np.count_nonzero(left & right)
    return float((left == right).mean()), match / union if union else 1.0
~~~

</details>

<a id="ml24-on-tap"></a>

### Ôn tập ML24

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML24-mcq-1

Rand Index đếm cả cặp khác cụm trong hai phân hoạch vào tử không?

- **A** · Có
- **B** · Không,Jaccard và Rand giống nhau
- **C** · Chỉ khi mã cụm giống tên

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đồng thuận gồm cả cùng-cùng và khác-khác.

- **A** · Đồng thuận gồm cả cùng-cùng và khác-khác.
- **B** · Rand có phần d mà Jaccard cùng cụm loại bỏ.
- **C** · Tên cụm không quan trọng.

</details>

##### ML24-mcq-2

Với n=2 có bao nhiêu cặp không thứ tự?

- **A** · 0
- **B** · 1
- **C** · 2

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Chỉ một cặp (0,1).

- **A** · Có cặp giữa hai mẫu khác nhau.
- **B** · Chỉ một cặp (0,1).
- **C** · Đã đếm cả hai hướng.

</details>

##### ML24-mcq-3

Mã cụm [0,0,1] và [0,1,1] có cùng phân hoạch không?

- **A** · Có vì đều hai cụm
- **B** · Có vì cùng số mẫu
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Quan hệ của cặp (0,1) và (1,2) đã đổi.

- **A** · Số cụm bằng nhau không đủ.
- **B** · Số mẫu bằng nhau không đủ.
- **C** · Quan hệ của cặp (0,1) và (1,2) đã đổi.

</details>

##### ML24-mcq-4

Đánh giá external clustering thường cần thêm gì?

- **A** · Nhãn tham chiếu
- **B** · Chỉ màu centroid
- **C** · Luôn cần test classification accuracy

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

External so cấu trúc phân cụm với nhãn tham chiếu.

- **A** · External so cấu trúc phân cụm với nhãn tham chiếu.
- **B** · Màu hiển thị không phải nhãn tham chiếu.
- **C** · Metric phân cụm khác accuracy classifier.

</details>

##### ML24-mcq-5

Rand Index xét đơn vị nào?

- **A** · Số chiều đặc trưng
- **B** · Cặp mẫu
- **C** · Chỉ từng centroid

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Xét cùng/khác cụm ở hai phân hoạch.

- **A** · Không đo sự đồng thuận phân cụm.
- **B** · Xét cùng/khác cụm ở hai phân hoạch.
- **C** · Không phải định nghĩa pair counting.

</details>

##### ML24-mcq-6

Có n=4 mẫu thì số cặp không thứ tự là bao nhiêu?

- **A** · 12
- **B** · 4
- **C** · 6

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

n(n−1)/2=6.

- **A** · 12 đếm cả hai hướng.
- **B** · Đó là số mẫu.
- **C** · n(n−1)/2=6.

</details>

##### ML24-mcq-7

Hai kết quả chỉ đổi tên cụm có bị pair metric coi khác không?

- **A** · Không
- **B** · Có vì nhãn số thay đổi
- **C** · Chỉ nếu có đúng hai cụm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Quan hệ cùng/khác cụm của mọi cặp vẫn giữ nguyên.

- **A** · Quan hệ cùng/khác cụm của mọi cặp vẫn giữ nguyên.
- **B** · Tên cụm chỉ là mã.
- **C** · Lập luận không phụ thuộc số cụm.

</details>

##### ML24-mcq-8

Jaccard theo cặp cùng cụm loại phần nào khỏi mẫu số?

- **A** · Mọi cặp bất đồng
- **B** · Các cặp khác cụm trong cả hai phân hoạch
- **C** · Cặp cùng cụm trong cả hai

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Jaccard cùng cụm dùng a/(a+b+c),không tính d.

- **A** · Bất đồng vẫn thuộc hợp.
- **B** · Jaccard cùng cụm dùng a/(a+b+c),không tính d.
- **C** · Đó là phần giao cần giữ.

</details>

##### ML24-mcq-9

Chỉ một mẫu thì metric theo tất cả cặp gặp gì?

- **A** · Luôn bằng 100%
- **B** · Luôn bằng −1
- **C** · Không có cặp,cần quy định hành vi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Không báo phép chia 0 như metric thực đo.

- **A** · Không tự suy ra từ mẫu số 0.
- **B** · Không đúng định nghĩa.
- **C** · Không báo phép chia 0 như metric thực đo.

</details>

#### Tự luận và viết mã

##### ML24-practice-1

Có 5 mẫu. Tính số cặp không thứ tự.

<details>
<summary>Đáp án và cách kiểm</summary>

5×4/2=10.

```python
n=5
print(n*(n-1)//2)
```
Kết quả: 10

</details>

##### ML24-practice-2

Hai phân hoạch [0,0,1] và [5,5,7] có cùng quan hệ cặp không?

<details>
<summary>Đáp án và cách kiểm</summary>

Có,cặp (0,1) cùng cụm;hai cặp còn lại khác cụm trong cả hai.

</details>

##### ML24-practice-3

Với true=[0,0,1],pred=[0,1,1],liệt kê ba cặp và đồng thuận.

<details>
<summary>Đáp án và cách kiểm</summary>

(0,1) bất đồng,(0,2) đồng thuận khác cụm,(1,2) bất đồng;Rand=1/3.

</details>

##### ML24-practice-4

Tính Rand cho ví dụ trên bằng đếm cặp.

<details>
<summary>Đáp án và cách kiểm</summary>

Một trong ba cặp đồng thuận.

```python
from itertools import combinations
t=[0,0,1];p=[0,1,1];pairs=list(combinations(range(3),2))
print(f"{sum((t[i]==t[j])==(p[i]==p[j]) for i,j in pairs)/len(pairs):.6f}")
```
Kết quả: 0.333333

</details>

##### ML24-practice-5

Gọi a=2 cặp cùng cụm cả hai,b=1 chỉ cùng true,c=1 chỉ cùng pred,d=2 khác cả hai. Tính Rand.

<details>
<summary>Đáp án và cách kiểm</summary>

(a+d)/(a+b+c+d)=4/6.

```python
a,b,c,d=2,1,1,2
print(f"{(a+d)/(a+b+c+d):.6f}")
```
Kết quả: 0.666667

</details>

##### ML24-practice-6

Với cùng a,b,c,d,tính Jaccard cùng cụm.

<details>
<summary>Đáp án và cách kiểm</summary>

a/(a+b+c)=2/4=0.5.

```python
a,b,c=2,1,1
print(a/(a+b+c))
```
Kết quả: 0.5

</details>

##### ML24-practice-7

Vì sao không so trực tiếp mã cụm dự đoán với nhãn tham chiếu bằng == từng mẫu?

<details>
<summary>Đáp án và cách kiểm</summary>

Mã cụm có thể hoán vị tùy ý mà vẫn cùng phân hoạch. So tên số đánh đồng vấn đề nhận dạng tên với cấu trúc nhóm.

</details>

##### ML24-practice-8

External score tốt có đủ chứng minh cụm có hình dạng gọn trong không gian đặc trưng không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. External so với nhãn tham chiếu;độ gọn/khoảng cách nội tại là khía cạnh khác.

</details>

##### ML24-practice-9

Internal validation có dùng nhãn tham chiếu bắt buộc không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không theo nghĩa internal;dùng dữ liệu và cấu trúc cụm. Cần nêu metric cụ thể,không tự tạo nhãn chuẩn từ chính output rồi coi external score cao là bằng chứng.

</details>

##### ML24-practice-10

Hai phân hoạch mọi mẫu tách riêng có Jaccard cùng cụm theo a/(a+b+c) ra sao?

<details>
<summary>Đáp án và cách kiểm</summary>

Không có cặp cùng cụm ở cả hai,mẫu số 0. Phải công bố quy ước hoặc báo không xác định;không mặc định phép chia cho kết quả 1.

</details>

##### ML24-practice-11

Nếu một nhãn bị thiếu,có nên âm thầm loại mẫu chỉ ở một trong hai phân hoạch không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Hai mảng phải tham chiếu cùng tập mẫu theo cùng thứ tự;lọc cần áp dụng đồng bộ và ghi phạm vi đánh giá.

</details>

##### ML24-practice-12

Một cặp cùng true nhưng khác pred đóng góp thế nào vào Rand và Jaccard?

<details>
<summary>Đáp án và cách kiểm</summary>

Là bất đồng:không vào tử Rand;vào mẫu số Jaccard nhưng không vào tử. Đây là cặp bị tách so với tham chiếu.

</details>

<a id="ml25"></a>

## ML25 · Thực hiện PCA qua trừ tâm, covariance, eigen decomposition và projection

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML02](#ml02)

<a id="ml25-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Trừ trung bình train rồi phân rã ma trận hiệp phương sai. Chiếu dữ liệu lên các vector riêng ứng với trị riêng lớn nhất. Đảo dấu vector riêng vẫn giữ nguyên không gian con.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính trung bình, hai phương sai mẫu và covariance ngoài đường chéo.
2. **P2** · Dự đoán trục chính, tỷ lệ phương sai được giữ và trị tuyệt đối tọa độ sau chiếu.

<a id="ml25-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[-2., 0.], [0., 1.], [0., -1.], [2., 0.]])
mu = X.mean(axis=0)
C = X - mu
cov = C.T @ C / (len(X) - 1)
v, U = np.linalg.eigh(cov)
u = U[:, -1]
print(v.round(6).tolist(), round(v[-1]/v.sum(), 6))
print(np.abs(C @ u).tolist())
~~~

[Xem kết quả mẫu](#ml25-ket-qua)

<a id="ml25-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Chỉ ra thứ tự eigenvalue trả về từ eigh. Vì sao mã lấy cột cuối của U?
2. **I2** · Đảo dấu u trên giấy. Xác định phần thay đổi trong projection và phần giữ nguyên nếu chiếu ngược.

[Đối chiếu cách giải thích](#ml25-giai-thich)

<a id="ml25-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Cộng [3,4] vào mọi hàng. Kiểm eigenvalues và tọa độ tuyệt đối giữ nguyên.
2. **MO2** · Nhân cột thứ hai với 3. Kiểm trục chính chuyển sang đặc trưng thứ hai và tỷ lệ thành 18/26.
3. **MO3** · Chiếu với K=2 rồi dựng lại bằng `Z @ U.T + mu`. Kiểm sai số dựng lại bằng 0 trong dung sai số học.

<a id="ml25-make"></a>

### E · Make 1 · Viết hàm

**`pca_fit(X, k)`**

Nhận train 2D hữu hạn, ít nhất hai hàng và một cột, k nguyên trong [1,d]. Trả (mu, U_top, ratios), các cột U_top sắp theo eigenvalue giảm dần. Ratios dùng tổng phương sai của mọi thành phần. Nếu tổng bằng 0, trả các ratio bằng 0. Kiểm theo projector để chấp nhận cả hai dấu hợp lệ.

Điền hàm. Chạy `python ML25.py`.

[Mã khởi đầu và 4 ca kiểm](#ml25-starter) · [Lời giải](#ml25-loi-giai)

<a id="ml25-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết transform và reconstruct dùng mu,U_top đã học, không fit lại. Train [[1,1],[3,3]], K=1, X mới [[4,2],[5,5]]. Kiểm dựng lại [[3,3],[5,5]].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml25-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml25-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0.666667, 2.666667] 0.8
[2.0, 0.0, 0.0, 2.0]
~~~

</details>

<details class="answer" id="ml25-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Mu=[0,0]. Covariance diag(8/3,2/3). Trục chính là trục thứ nhất, giữ 0.8 phương sai và tọa độ tuyệt đối [2,0,0,2].

</details>

<details class="answer" id="ml25-starter" data-starter="ML25">
<summary>E · Mã khởi đầu và ca kiểm · ML25.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def pca_fit(X, k):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    mu, U, ratio = pca_fit([[-2,0],[0,1],[0,-1],[2,0]], 1)
    same(mu, [0,0])
    same(U @ U.T, [[1,0],[0,0]])
    same(ratio, [0.8])


def case_02():
    mu, U, ratio = pca_fit([[1,1],[3,3]], 1)
    same(mu, [2,2])
    same(U @ U.T, [[0.5,0.5],[0.5,0.5]])
    same(ratio, [1])


def case_03():
    same(pca_fit([[2,2],[2,2]], 2)[2], [0,0])


def case_04():
    rejects(pca_fit, [[0,1]], 1)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml25-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def pca_fit(X, k):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or len(X) < 2 or not isinstance(k, (int, np.integer)) or not 1 <= k <= X.shape[1] or not np.isfinite(X).all():
        raise ValueError("Đầu vào không hợp lệ")
    mu = X.mean(axis=0)
    C = X - mu
    eig, U = np.linalg.eigh(C.T @ C / (len(X) - 1))
    eig = eig[::-1].clip(min=0)
    ratios = eig[:k] / eig.sum() if eig.sum() else np.zeros(k)
    return mu, U[:, ::-1][:, :k], ratios
~~~

</details>

<a id="ml25-on-tap"></a>

### Ôn tập ML25

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML25-mcq-1

Giữ toàn bộ d hướng trực chuẩn PCA và mean có thể tái tạo dữ liệu tâm hóa trong số học chính xác không?

- **A** · Có
- **B** · Không vì luôn mất ít nhất một chiều
- **C** · Chỉ khi không có mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Projection trên cơ sở trực chuẩn đầy đủ giữ mọi tọa độ.

- **A** · Projection trên cơ sở trực chuẩn đầy đủ giữ mọi tọa độ.
- **B** · Không giảm chiều khi giữ đủ cơ sở.
- **C** · Không cần trường hợp đó.

</details>

##### ML25-mcq-2

Eigenvalue 0 của covariance biểu thị gì theo hướng đó?

- **A** · Mọi feature gốc đều hằng
- **B** · Không có phương sai dữ liệu tâm hóa theo hướng đó
- **C** · Tâm cụm bằng 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Phương sai projection bằng eigenvalue tương ứng.

- **A** · Chỉ một hướng không đủ kết luận mọi cột hằng.
- **B** · Phương sai projection bằng eigenvalue tương ứng.
- **C** · Không phải centroid.

</details>

##### ML25-mcq-3

PCA có tự dùng nhãn y để chọn hướng dự báo tốt nhất không theo thuật toán đang học?

- **A** · Có vì mọi ML cần y
- **B** · Có nếu y là số
- **C** · Không

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

PCA tối đa phương sai X,không tối ưu trực tiếp loss dự đoán y.

- **A** · PCA là phép biến đổi không giám sát này.
- **B** · Kiểu số không thay thuật toán.
- **C** · PCA tối đa phương sai X,không tối ưu trực tiếp loss dự đoán y.

</details>

##### ML25-mcq-4

PCA theo covariance bắt đầu bằng bước nào trong bài?

- **A** · Trừ mean theo cột train
- **B** · Trừ mean riêng của từng hàng
- **C** · Đổi nhãn thành số cụm

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tâm hóa mỗi đặc trưng trước covariance.

- **A** · Tâm hóa mỗi đặc trưng trước covariance.
- **B** · Đó không phải tâm hóa đặc trưng đang dùng.
- **C** · PCA không cần nhãn này.

</details>

##### ML25-mcq-5

Eigenvector được chọn theo eigenvalue nào để giữ phương sai lớn nhất?

- **A** · Âm nhất
- **B** · Lớn nhất
- **C** · Nhỏ nhất

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Eigenvalue biểu diễn phương sai theo hướng tương ứng.

- **A** · Covariance lý tưởng là PSD.
- **B** · Eigenvalue biểu diễn phương sai theo hướng tương ứng.
- **C** · Giữ phương sai ít nhất.

</details>

##### ML25-mcq-6

Xc shape (n,d),V_k shape (d,k). Projection có shape gì?

- **A** · (d,n)
- **B** · (k,k)
- **C** · (n,k)

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Xc@V_k giữ n mẫu và k tọa độ mới.

- **A** · Sai thứ tự trục.
- **B** · Sai số hàng.
- **C** · Xc@V_k giữ n mẫu và k tọa độ mới.

</details>

##### ML25-mcq-7

Tổng explained variance ratio của mọi thành phần khi tổng phương sai dương bằng gì?

- **A** · 1
- **B** · Số mẫu n
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Tổng lambda_i/sum(lambda)=1.

- **A** · Tổng lambda_i/sum(lambda)=1.
- **B** · Tỷ lệ được chuẩn hóa bởi tổng eigenvalue.
- **C** · Không nếu tổng phương sai dương.

</details>

##### ML25-mcq-8

Đổi dấu một eigenvector làm PCA tương đương về phương sai không?

- **A** · Chỉ với một mẫu
- **B** · Có
- **C** · Không vì eigenvalue đổi dấu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Tọa độ projection đổi dấu tương ứng nhưng cùng hướng trục.

- **A** · Không phụ thuộc điều kiện đó.
- **B** · Tọa độ projection đổi dấu tương ứng nhưng cùng hướng trục.
- **C** · Đổi dấu vector không đổi eigenvalue.

</details>

##### ML25-mcq-9

Dữ liệu test khi áp dụng PCA đã fit cần dùng mean nào?

- **A** · Mean riêng test
- **B** · Mean từ test label
- **C** · Mean train đã fit

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Giữ cùng mean và các vector hướng train.

- **A** · Đổi tâm khác hệ tọa độ đã học.
- **B** · PCA này không dùng nhãn test.
- **C** · Giữ cùng mean và các vector hướng train.

</details>

#### Tự luận và viết mã

##### ML25-practice-1

X=[[1,2],[3,4]],tính mean và Xc.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=[2,3],Xc=[[-1,−1],[1,1]].

```python
import numpy as np
X=np.array([[1.,2.],[3.,4.]])
print(X.mean(axis=0).tolist())
print((X-X.mean(axis=0)).tolist())
```
Kết quả: [2.0, 3.0]
[[-1.0, -1.0], [1.0, 1.0]]

</details>

##### ML25-practice-2

Eigenvalues=[4,1]. Tính explained variance ratio.

<details>
<summary>Đáp án và cách kiểm</summary>

[0.8,0.2].

```python
import numpy as np
v=np.array([4.,1.]);print((v/v.sum()).tolist())
```
Kết quả: [0.8, 0.2]

</details>

##### ML25-practice-3

Eigenvalues theo thứ tự giảm [6,3,1]. Giữ ít nhất 90% cần bao nhiêu thành phần?

<details>
<summary>Đáp án và cách kiểm</summary>

Hai thành phần vì (6+3)/10=0.9.

```python
import numpy as np
v=np.array([6.,3.,1.]);c=np.cumsum(v)/v.sum()
print(int(np.searchsorted(c,.9)+1))
```
Kết quả: 2

</details>

##### ML25-practice-4

Xc=[[1,2],[3,4]],V_k=[[1],[0]]. Tính projection.

<details>
<summary>Đáp án và cách kiểm</summary>

[[1],[3]],shape (2,1).

```python
import numpy as np
print((np.array([[1.,2.],[3.,4.]])@np.array([[1.],[0.]])).tolist())
```
Kết quả: [[1.0], [3.0]]

</details>

##### ML25-practice-5

Vì sao np.linalg.eigh phù hợp covariance thực đối xứng?

<details>
<summary>Đáp án và cách kiểm</summary>

Hàm dành cho ma trận Hermitian/đối xứng,trả hệ eigenvalue/eigenvector phù hợp cấu trúc. Vẫn cần sắp thứ tự theo mục tiêu PCA.

</details>

##### ML25-practice-6

eigh trả eigenvalues tăng dần. Nếu lấy cột đầu mà muốn giữ phương sai lớn nhất,sai ở đâu?

<details>
<summary>Đáp án và cách kiểm</summary>

Đã chọn hướng phương sai nhỏ nhất. Cần sắp giảm dần và hoán vị cột eigenvector tương ứng.

</details>

##### ML25-practice-7

Dữ liệu mọi cột hằng có explained variance ratio theo lambda/sum(lambda) thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Tổng phương sai bằng 0 nên tỷ lệ không xác định trực tiếp. Cần quy định riêng thay vì chấp nhận NaN.

</details>

##### ML25-practice-8

Eigenvector v và −v có cùng tái tạo nếu tọa độ projection đổi dấu theo không?

<details>
<summary>Đáp án và cách kiểm</summary>

Có,zvᵀ=(-z)(−v)ᵀ. Không ép eigenvector cùng dấu với một output mẫu rồi báo sai toán học.

</details>

##### ML25-practice-9

X shape (10,4),giữ k=2. Tính số tọa độ ban đầu và sau projection.

<details>
<summary>Đáp án và cách kiểm</summary>

Ban đầu 40,sau 20,không tính mean và các vector hướng cần lưu.

```python
n,d,k=10,4,2
print(n*d)
print(n*k)
```
Kết quả: 40
20

</details>

##### ML25-practice-10

Có nên fit PCA riêng trên test rồi đưa tọa độ vào model học trên PCA train không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Các hướng và mean có thể khác nhau;model cần cùng phép biến đổi đã fit trên train.

</details>

##### ML25-practice-11

Một thuộc tính đơn vị lớn có phương sai lớn. PCA covariance có tự bỏ ảnh hưởng đơn vị không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Scale ảnh hưởng covariance và hướng PCA;quy trình scaling trước PCA phải nêu rõ và học từ train.

</details>

##### ML25-practice-12

Nếu hai eigenvalues bằng nhau,có thể yêu cầu mọi thư viện trả đúng từng vector giống hệt không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Có thể có nhiều cơ sở trực chuẩn trong cùng không gian con. Kiểm không gian/phương sai hoặc tái tạo phù hợp hơn so vector từng phần tử.

</details>

<a id="ml26"></a>

## ML26 · Tính impurity và chọn split cho cây quyết định

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML01](#ml01)

<a id="ml26-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Chọn điểm chia làm giảm độ hỗn tạp nhiều nhất sau khi tính trọng số theo kích thước nhánh. Chỉ xét điểm chia tạo hai nhánh có mẫu.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính Gini của node gốc. Viết nhãn ở hai nhánh khi t=0.5.
2. **P2** · Tính gain cho ba ứng viên và chọn ngưỡng tốt nhất.

<a id="ml26-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([0., 1., 2., 3.])
y = np.array([0, 0, 1, 1])
def gini(labels):
    p = labels.mean()
    return 2*p*(1-p)
for t in [0.5, 1.5, 2.5]:
    left = x <= t
    after = (left.sum()*gini(y[left]) + (~left).sum()*gini(y[~left])) / len(y)
    print(t, round(gini(y) - after, 6))
~~~

[Xem kết quả mẫu](#ml26-ket-qua)

<a id="ml26-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao phải lấy trọng số theo kích thước nhánh. So loss chia sai khi t=0.5.
2. **I2** · Đổi quy tắc ≤ sang <. Cho một giá trị t mà quy tắc đổi cách gán. Vì sao ngưỡng giữa giá trị khác nhau tránh điểm train bằng ngưỡng?

[Đối chiếu cách giải thích](#ml26-giai-thich)

<a id="ml26-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi y thành [0,1,1,1]. Kiểm t=0.5 cho gain 0.375.
2. **MO2** · Dùng y=[0,0,0,0]. Kiểm mọi gain bằng 0 và quy định dừng tách.
3. **MO3** · Thay Gini bằng entropy log₂, bỏ các hạng p=0. Với dữ liệu gốc, kiểm gain ở t=1.5 bằng 1 bit.

<a id="ml26-make"></a>

### E · Make 1 · Viết hàm

**`best_gini_split(x, y)`**

Nhận vector x hữu hạn và vector y nhị phân cùng độ dài dương. Thử các điểm giữa hai giá trị x phân biệt liền nhau. Trả (threshold, gain) dương lớn nhất, hòa lấy ngưỡng nhỏ. Dùng dung sai 10⁻¹² khi so các gain. Nếu không có gain vượt dung sai, trả None. Báo ValueError nếu đầu vào sai.

Điền hàm. Chạy `python ML26.py`.

[Mã khởi đầu và 6 ca kiểm](#ml26-starter) · [Lời giải](#ml26-loi-giai)

<a id="ml26-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết decision stump dùng threshold tìm được, mỗi lá biểu quyết đa số (hòa → 0). Train x=[0,1,3,4], y=[0,0,1,1]. Kiểm dự đoán cho x=[−1,2,5] bằng [0,0,1].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml26-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml26-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
0.5 0.166667
1.5 0.5
2.5 0.166667
~~~

</details>

<details class="answer" id="ml26-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Gini gốc 0.5. Với t=0.5, nhánh trái [0], phải [0,1,1]. Gain lần lượt 1/6,1/2,1/6; chọn 1.5.

</details>

<details class="answer" id="ml26-starter" data-starter="ML26">
<summary>E · Mã khởi đầu và ca kiểm · ML26.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def best_gini_split(x, y):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(best_gini_split([0,1,2,3], [0,0,1,1]), [1.5,0.5])


def case_02():
    same(best_gini_split([0,1,2], [0,1,0]), [0.5,1/9])


def case_03():
    same(best_gini_split([2,0,0,2], [1,0,0,1]), [1,0.5])


def case_04():
    assert best_gini_split([1,1], [0,1]) is None


def case_05():
    assert best_gini_split([0,1], [1,1]) is None


def case_06():
    rejects(best_gini_split, [0,1], [0,2])


CASES = [case_01, case_02, case_03, case_04, case_05, case_06]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml26-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def best_gini_split(x, y):
    x, y = np.asarray(x, dtype=float), np.asarray(y)
    if x.ndim != 1 or not x.size or x.shape != y.shape or not np.isfinite(x).all() or not np.isin(y, [0, 1]).all():
        raise ValueError("Đầu vào không hợp lệ")
    def gini(labels):
        p = labels.mean()
        return 2 * p * (1 - p)
    candidates = np.unique(x)
    parent = gini(y)
    best = None
    for a, b in zip(candidates[:-1], candidates[1:]):
        t = a / 2 + b / 2
        if t >= b:
            t = a
        left = x <= t
        gain = parent - (left.sum()*gini(y[left]) + (~left).sum()*gini(y[~left]))/len(y)
        if gain > 1e-12 and (best is None or gain > best[1] + 1e-12):
            best = float(t), float(gain)
    return best
~~~

</details>

<a id="ml26-on-tap"></a>

### Ôn tập ML26

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML26-mcq-1

Node có counts [0,5] có Gini bằng gì?

- **A** · 0
- **B** · 0.5
- **C** · 5

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Node thuần lớp.

- **A** · Node thuần lớp.
- **B** · Đó là hai lớp cân bằng.
- **C** · Count không phải impurity.

</details>

##### ML26-mcq-2

Thay log2 bằng ln có đổi thứ tự split theo information gain khi cùng dữ liệu không?

- **A** · Không thể tính entropy với ln
- **B** · Không nếu tính nhất quán
- **C** · Có,luôn đảo thứ tự

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mọi entropy/gain nhân cùng hệ số dương.

- **A** · Có thể,đơn vị khác.
- **B** · Mọi entropy/gain nhân cùng hệ số dương.
- **C** · Đổi cơ số chỉ nhân hằng số dương.

</details>

##### ML26-mcq-3

Tại node bốn mẫu,chia hai nhánh thuần lớp thì weighted Gini con bao nhiêu?

- **A** · 1
- **B** · Phụ thuộc tên lớp
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Tổng có trọng số của hai số 0 bằng 0.

- **A** · Mỗi nhánh impurity 0.
- **B** · Không phụ thuộc mã tên.
- **C** · Tổng có trọng số của hai số 0 bằng 0.

</details>

##### ML26-mcq-4

Gini của một node có tỷ lệ lớp p_j là gì?

- **A** · 1−sum(p_j²)
- **B** · sum(p_j)
- **C** · −sum(log(p_j))

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Gini bằng 0 ở node thuần lớp.

- **A** · Gini bằng 0 ở node thuần lớp.
- **B** · Tổng tỷ lệ bằng 1,không đo impurity.
- **C** · Thiếu trọng số p và không phải Gini.

</details>

##### ML26-mcq-5

Node hai lớp cân bằng có Gini bao nhiêu?

- **A** · 1
- **B** · 0.5
- **C** · 0

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Thay p0=p1=0.5.

- **A** · Hai lớp cân bằng cho 1−0.25−0.25.
- **B** · Thay p0=p1=0.5.
- **C** · Chỉ node thuần lớp có Gini 0.

</details>

##### ML26-mcq-6

So impurity sau split hai nhánh kích thước khác nhau cần làm gì?

- **A** · Luôn cộng hai impurity rồi chia 2
- **B** · Chỉ dùng nhánh lớn
- **C** · Trung bình có trọng số theo số mẫu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Mỗi nhánh đóng góp theo tỷ lệ mẫu.

- **A** · Sai khi nhánh khác cỡ.
- **B** · Bỏ ảnh hưởng nhánh nhỏ.
- **C** · Mỗi nhánh đóng góp theo tỷ lệ mẫu.

</details>

##### ML26-mcq-7

Information gain bằng gì?

- **A** · Entropy cha trừ entropy con có trọng số
- **B** · Entropy con trừ cha
- **C** · Tổng nhãn lớp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cùng định nghĩa entropy và cơ số log.

- **A** · Cùng định nghĩa entropy và cơ số log.
- **B** · Đảo dấu.
- **C** · Không đo giảm impurity.

</details>

##### ML26-mcq-8

Nhánh không có mẫu sau split có nên lấy tỷ lệ lớp bằng phép chia 0 không?

- **A** · Gán toàn nhánh lớp 1
- **B** · Không,cần xử lý/ngăn split rỗng
- **C** · Có nếu để NaN tự truyền

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Quy tắc split phải có ca biên rõ.

- **A** · Bịa dữ liệu nhánh.
- **B** · Quy tắc split phải có ca biên rõ.
- **C** · Không phải đánh giá hợp lệ.

</details>

##### ML26-mcq-9

Cây chia quá sâu có nguy cơ gì?

- **A** · Bảo đảm tốt nhất test
- **B** · Mọi node tự thành linear regression
- **C** · Overfitting

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Có thể ghi nhớ các nhóm rất nhỏ/nhiễu.

- **A** · Không có bảo đảm.
- **B** · Khác mô hình.
- **C** · Có thể ghi nhớ các nhóm rất nhỏ/nhiễu.

</details>

#### Tự luận và viết mã

##### ML26-practice-1

Node thuần một lớp có Gini và entropy bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

Cả hai bằng 0;hạng 0 log0 lấy giới hạn bằng 0.

</details>

##### ML26-practice-2

Tính Gini với tỷ lệ [0.5,0.5].

<details>
<summary>Đáp án và cách kiểm</summary>

0.5.

```python
p=[.5,.5]
print(1-sum(x*x for x in p))
```
Kết quả: 0.5

</details>

##### ML26-practice-3

Tính Gini với tỷ lệ [0.75,0.25].

<details>
<summary>Đáp án và cách kiểm</summary>

1−0.5625−0.0625=0.375.

```python
p=[.75,.25]
print(1-sum(x*x for x in p))
```
Kết quả: 0.375

</details>

##### ML26-practice-4

Nhánh trái 3 mẫu Gini=0,phải 1 mẫu Gini=0.5. Tính impurity sau split.

<details>
<summary>Đáp án và cách kiểm</summary>

3/4×0+1/4×0.5=0.125.

```python
print(3/4*0+1/4*.5)
```
Kết quả: 0.125

</details>

##### ML26-practice-5

Cha Gini=0.5,con weighted Gini=0.125. Tính giảm impurity.

<details>
<summary>Đáp án và cách kiểm</summary>

0.375.

```python
print(.5-.125)
```
Kết quả: 0.375

</details>

##### ML26-practice-6

Entropy log2 của hai lớp cân bằng là bao nhiêu?

<details>
<summary>Đáp án và cách kiểm</summary>

1 bit.

```python
import math
print(-sum(p*math.log2(p) for p in [.5,.5]))
```
Kết quả: 1.0

</details>

##### ML26-practice-7

Split A weighted Gini=0.2,B=0.3,cùng cha. Chọn theo giảm Gini.

<details>
<summary>Đáp án và cách kiểm</summary>

Chọn A vì impurity con thấp hơn,cùng impurity cha nên gain cao hơn.

</details>

##### ML26-practice-8

Feature x=[1,2,3,4],ngưỡng 2.5. Liệt kê chỉ số trái với <= và phải với >.

<details>
<summary>Đáp án và cách kiểm</summary>

Trái [0,1],phải [2,3].

```python
x=[1,2,3,4]
print([i for i,v in enumerate(x) if v<=2.5])
print([i for i,v in enumerate(x) if v>2.5])
```
Kết quả: [0, 1]
[2, 3]

</details>

##### ML26-practice-9

Vì sao tên lớp 0 và 1 đổi chỗ không làm Gini đổi?

<details>
<summary>Đáp án và cách kiểm</summary>

Gini dùng bình phương tỷ lệ lớp;hoán vị các tỷ lệ không đổi tổng.

</details>

##### ML26-practice-10

Nếu split tạo hai nhánh nhưng giữ nguyên tỷ lệ lớp như cha,impurity giảm thế nào?

<details>
<summary>Đáp án và cách kiểm</summary>

Bằng 0 vì weighted impurity con bằng impurity cha.

</details>

##### ML26-practice-11

Tại sao không chọn ngưỡng theo test label?

<details>
<summary>Đáp án và cách kiểm</summary>

Ngưỡng là phần model đã học;test phải giữ ngoài fitting và lựa chọn để đánh giá độc lập.

</details>

##### ML26-practice-12

Một node có counts [1,3]. Tính tỷ lệ và Gini.

<details>
<summary>Đáp án và cách kiểm</summary>

Tỷ lệ [0.25,0.75],Gini=0.375.

```python
c=[1,3];p=[x/sum(c) for x in c]
print(p)
print(1-sum(x*x for x in p))
```
Kết quả: [0.25, 0.75]
0.375

</details>

<a id="ml27"></a>

## ML27 · Giải thích Bagging và Random Forest giảm phương sai bằng bootstrap và feature subsampling

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML26](#ml26)

<a id="ml27-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Bagging tạo mẫu bootstrap bằng cách lấy có hoàn lại. Random Forest còn chọn ngẫu nhiên tập đặc trưng ứng viên tại mỗi node. Gộp dự đoán phân loại bằng biểu quyết.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Liệt kê mẫu xuất hiện lặp lại và mẫu OOB của từng cây.
2. **P2** · Đếm phiếu theo cột rồi dự đoán hai nhãn.

<a id="ml27-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
bags = np.array([[0,0,2,3], [1,2,2,3], [0,1,1,2]])
votes = np.array([[1,0], [0,1], [1,1]])
for bag in bags:
    oob = np.setdiff1d(np.arange(4), bag)
    print(oob.tolist())
print((votes.sum(axis=0) * 2 > len(votes)).astype(int).tolist())
~~~

[Xem kết quả mẫu](#ml27-ket-qua)

<a id="ml27-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao một bootstrap dài n có thể không phủ hết n hàng.
2. **I2** · Phân biệt bốc mẫu theo hàng cho từng cây với bốc đặc trưng ứng viên theo cột tại mỗi node.

[Đối chiếu cách giải thích](#ml27-giai-thich)

<a id="ml27-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đảo thứ tự các cây ở cả bags và votes. Kiểm nhãn gộp giữ nguyên.
2. **MO2** · Bỏ cây cuối. Kiểm hai dự đoán đều hòa và theo mã nhận nhãn 0.
3. **MO3** · Tạo 3 bootstrap cỡ 4 bằng `rng.integers(0, 4, size=(3,4))`. Dùng cùng seed ở hai lần chạy và kiểm cả bag lẫn OOB giống nhau.

<a id="ml27-make"></a>

### E · Make 1 · Viết hàm

**`oob_vote(bags, votes, n)`**

bags là ma trận B×n các chỉ số bootstrap 0..n−1. votes là ma trận B×n nhãn dự đoán 0/1 của mỗi cây trên n hàng train. Với mỗi hàng, chỉ gộp phiếu từ cây mà hàng là OOB, hòa lấy 0. Trả vector nhãn, dùng −1 nếu chưa có cây OOB. Báo ValueError nếu miền hoặc shape sai.

Điền hàm. Chạy `python ML27.py`.

[Mã khởi đầu và 4 ca kiểm](#ml27-starter) · [Lời giải](#ml27-loi-giai)

<a id="ml27-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự dựng ensemble 5 decision stumps từ ML26. Với mỗi cây lấy bootstrap có hoàn lại và chọn một cột bằng RNG seed cố định. Dùng X=[[0,0],[0,1],[1,0],[1,1]], y=[0,0,1,1]. Kiểm cùng seed cho cùng các mẫu/cột/dự đoán. Dùng fixture xác định chọn cột 0 và đủ bốn hàng cho 3 cây để kiểm nhãn gộp khớp y.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml27-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml27-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[1]
[0]
[3]
[1, 1]
~~~

</details>

<details class="answer" id="ml27-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Hàng lặp lần lượt 0,2,1. Các tập OOB là [1],[0],[3]. Mỗi mẫu minh họa có hai phiếu 1, nhãn gộp [1,1].

</details>

<details class="answer" id="ml27-starter" data-starter="ML27">
<summary>E · Mã khởi đầu và ca kiểm · ML27.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def oob_vote(bags, votes, n):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(oob_vote([[0,0,2],[1,1,2],[0,1,2]], [[1,1,1],[1,1,0],[0,0,0]], 3), [1,1,-1])


def case_02():
    same(oob_vote([[0,0],[0,0]], [[1,1],[1,0]], 2), [-1,0])


def case_03():
    same(oob_vote([[0]], [[1]], 1), [-1])


def case_04():
    rejects(oob_vote, [[0,2]], [[0,1]], 2)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml27-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def oob_vote(bags, votes, n):
    bags, votes = np.asarray(bags), np.asarray(votes)
    if n < 1 or bags.ndim != 2 or bags.shape[1] != n or votes.shape != bags.shape or bags.dtype.kind not in "iu" or np.any((bags < 0) | (bags >= n)) or not np.isin(votes, [0, 1]).all():
        raise ValueError("Bag hoặc phiếu không hợp lệ")
    oob = np.ones(bags.shape, dtype=bool)
    oob[np.arange(len(bags))[:, None], bags] = False
    count = oob.sum(axis=0)
    ones = (oob * votes).sum(axis=0)
    return np.where(count == 0, -1, (2 * ones > count).astype(int))
~~~

</details>

<a id="ml27-on-tap"></a>

### Ôn tập ML27

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML27-mcq-1

Bootstrap sample có thể không chứa một mẫu train nào đó không?

- **A** · Có
- **B** · Không vì luôn dùng mọi mẫu phân biệt
- **C** · Chỉ nếu không có seed

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

n lượt lấy có hoàn lại không bảo đảm phủ đủ n mẫu gốc.

- **A** · n lượt lấy có hoàn lại không bảo đảm phủ đủ n mẫu gốc.
- **B** · Có hoàn lại tạo mẫu lặp và mẫu vắng.
- **C** · Seed không ngăn vắng mẫu.

</details>

##### ML27-mcq-2

Trung bình dự đoán [1,1,7] bằng gì?

- **A** · 7
- **B** · 3
- **C** · 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

(1+1+7)/3=3.

- **A** · Đó là giá trị lớn nhất.
- **B** · (1+1+7)/3=3.
- **C** · Đó là median,không phải mean.

</details>

##### ML27-mcq-3

Random Forest có phải gọi một model có sẵn bị cấm trong bài tự triển khai không?

- **A** · Bắt buộc dùng scikit-learn
- **B** · Chỉ đổi tên một cây thành forest
- **C** · Không,có thể học/triển khai thành phần bằng Python và NumPy

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Khái niệm thuật toán tách khỏi thư viện triển khai.

- **A** · Yêu cầu khóa không dùng thư viện đó.
- **B** · Một cây không tự thành ensemble.
- **C** · Khái niệm thuật toán tách khỏi thư viện triển khai.

</details>

##### ML27-mcq-4

Bootstrap lấy mẫu từ train theo cách nào?

- **A** · Có hoàn lại
- **B** · Không bao giờ lặp mẫu
- **C** · Chỉ lấy test

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Mỗi lần chọn có thể chọn lại một mẫu.

- **A** · Mỗi lần chọn có thể chọn lại một mẫu.
- **B** · Bootstrap cho phép lặp.
- **C** · Không được dùng test để fit.

</details>

##### ML27-mcq-5

Bagging hồi quy thường gộp dự đoán bằng gì?

- **A** · Chỉ chọn model cuối
- **B** · Trung bình các dự đoán
- **C** · Tổng nhãn test

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Mean giảm biến thiên khi các sai số không hoàn toàn tương quan.

- **A** · Không phải phép gộp bagging thông thường.
- **B** · Mean giảm biến thiên khi các sai số không hoàn toàn tương quan.
- **C** · Không dùng test label.

</details>

##### ML27-mcq-6

Random Forest tạo đa dạng ngoài bootstrap bằng gì?

- **A** · Đổi nhãn thật ngẫu nhiên để fit
- **B** · Bắt mọi cây cùng đúng một split
- **C** · Lấy tập con feature ứng viên khi chia node

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Feature subsampling giúp giảm tương quan giữa cây.

- **A** · Không phải cơ chế đúng.
- **B** · Làm các cây giống nhau.
- **C** · Feature subsampling giúp giảm tương quan giữa cây.

</details>

##### ML27-mcq-7

Mọi model trong ensemble có lỗi giống hệt nhau thì averaging có tự loại lỗi đó không?

- **A** · Không
- **B** · Có,luôn hết lỗi
- **C** · Chỉ cần tăng số model vô hạn

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Đa dạng và mức tương quan ảnh hưởng lợi ích ensemble.

- **A** · Đa dạng và mức tương quan ảnh hưởng lợi ích ensemble.
- **B** · Lỗi chung giữ lại qua trung bình.
- **C** · Nếu dự đoán giống hệt thì mean vẫn thế.

</details>

##### ML27-mcq-8

Tập bootstrap có n lượt chọn thì có bắt buộc n mẫu phân biệt không?

- **A** · Có nếu seed cố định
- **B** · Không
- **C** · Có theo định nghĩa

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Lượt chọn khác số mẫu duy nhất.

- **A** · Seed không loại trùng.
- **B** · Lượt chọn khác số mẫu duy nhất.
- **C** · Có hoàn lại cho phép trùng.

</details>

##### ML27-mcq-9

Với phân loại đa số,nhãn [1,0,1] gộp thành gì?

- **A** · 0
- **B** · Trung bình nhãn 2/3 là nhãn mới
- **C** · 1

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Lớp 1 chiếm đa số.

- **A** · Lớp 1 có hai phiếu.
- **B** · Cần phân biệt score tổng hợp và nhãn biểu quyết.
- **C** · Lớp 1 chiếm đa số.

</details>

#### Tự luận và viết mã

##### ML27-practice-1

Ba model hồi quy dự đoán [2,4,6]. Bagging mean là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

4.

```python
print(sum([2.,4.,6.])/3)
```
Kết quả: 4.0

</details>

##### ML27-practice-2

Hai model dự đoán hai mẫu: [1,3] và [3,5]. Gộp theo mẫu.

<details>
<summary>Đáp án và cách kiểm</summary>

Mean=[2,4].

```python
import numpy as np
print(np.array([[1.,3.],[3.,5.]]).mean(axis=0).tolist())
```
Kết quả: [2.0, 4.0]

</details>

##### ML27-practice-3

Bootstrap indices=[1,1,3,0] trên X=[10,20,30,40]. Nêu mẫu lấy được và số mẫu duy nhất.

<details>
<summary>Đáp án và cách kiểm</summary>

[20,20,40,10];3 mẫu duy nhất.

```python
X=[10,20,30,40];idx=[1,1,3,0]
print([X[i] for i in idx])
print(len(set(idx)))
```
Kết quả: [20, 20, 40, 10]
3

</details>

##### ML27-practice-4

Với bootstrap indices trên và n=4,chỉ số nào không được chọn?

<details>
<summary>Đáp án và cách kiểm</summary>

Chỉ số 2.

```python
idx=[1,1,3,0]
print(sorted(set(range(4))-set(idx)))
```
Kết quả: [2]

</details>

##### ML27-practice-5

Vì sao phải bootstrap X và y bằng cùng indices?

<details>
<summary>Đáp án và cách kiểm</summary>

Giữ đúng cặp mẫu–nhãn;resample riêng hai mảng sẽ làm model học nhãn sai.

</details>

##### ML27-practice-6

Nếu mọi model dự đoán 5,mean của 100 model là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

Vẫn 5;tăng số model giống hệt không thay output.

```python
print(sum([5.]*100)/100)
```
Kết quả: 5.0

</details>

##### ML27-practice-7

Nhãn ba cây [0,1,1],tính majority vote.

<details>
<summary>Đáp án và cách kiểm</summary>

1.

```python
labels=[0,1,1]
print(max(set(labels),key=labels.count))
```
Kết quả: 1

</details>

##### ML27-practice-8

Tại sao không tạo đa dạng bằng cách cố ý sửa đáp án train tùy tiện?

<details>
<summary>Đáp án và cách kiểm</summary>

Làm sai mục tiêu học. Đa dạng bagging đến từ sampling và giới hạn feature theo thuật toán,không bịa nhãn.

</details>

##### ML27-practice-9

Một feature set có d=10,cấu hình mỗi split xem 3 feature. Có phải toàn cây chỉ được dùng đúng 3 feature cố định không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không theo Random Forest thường dùng;tập ứng viên có thể được lấy lại ở mỗi split. Phải đọc cấu hình và thuật toán cụ thể.

</details>

##### ML27-practice-10

Nêu điều cần ghi để tái lập ensemble mô phỏng.

<details>
<summary>Đáp án và cách kiểm</summary>

Dữ liệu/thứ tự mẫu,seed,số model,cách resample,feature sampling và quy tắc tổng hợp/phá hòa.

</details>

##### ML27-practice-11

Có thể dùng test label để chọn ra cây tốt nhất rồi gọi đó là bagging không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Vừa dùng test để lựa chọn,vừa thay phép gộp ensemble bằng chọn model;không đúng quy trình đã định.

</details>

<a id="ml28"></a>

## ML28 · Tích hợp pipeline hồi quy và phân loại

[Mục lục](#muc-luc) · M6 · Phân cụm, giảm chiều, cây và ensemble · Tiên quyết [ML03](#ml03), [ML07](#ml07), [ML09](#ml09), [ML13](#ml13), [ML15](#ml15)

<a id="ml28-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Chia dữ liệu rồi fit bộ chuẩn hóa và mô hình trên train. Dùng các tham số đã fit để dự đoán và đánh giá trên tập độc lập.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính mu và std train, rồi dự đoán ŷ ở x=8 dựa vào quan hệ train.
2. **P2** · Nếu y_test được đổi thành 18, dự đoán phần nào của chương trình thay đổi và MAE mới.

<a id="ml28-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0.], [2.], [4.], [8.]])
y = np.array([1., 5., 9., 17.])
train, test = [0,1,2], [3]
mu, std = X[train].mean(axis=0), X[train].std(axis=0)
A_train = np.column_stack([np.ones(len(train)), (X[train]-mu)/std])
w = np.linalg.lstsq(A_train, y[train], rcond=None)[0]
A_test = np.column_stack([np.ones(len(test)), (X[test]-mu)/std])
yhat = A_test @ w
print(mu.tolist(), std.round(6).tolist())
print(yhat.round(6).tolist(), round(np.mean(np.abs(yhat-y[test])), 6))
~~~

[Xem kết quả mẫu](#ml28-ket-qua)

<a id="ml28-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Đánh dấu ranh giới train/test, dòng nào dùng fit và dòng nào chỉ transform. Chỉ ra vì sao y_test không tác động vào w.
2. **I2** · Giải thích cách chèn validation khi muốn chọn mô hình. Chỉ ra khi nào được tính điểm trên test.

[Đối chiếu cách giải thích](#ml28-giai-thich)

<a id="ml28-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi X_test thành [[10]] và giữ y_test gốc. Kiểm ŷ=21 và MAE=4.
2. **MO2** · Thêm cột hằng 7. Thay std=0 của cột này bằng 1 trước khi chia. Kiểm dự đoán giữ nguyên.
3. **MO3** · Thêm đa thức bậc 2 rồi chọn theo validation mới có x=6 và y=13. Báo quy tắc khi các loss bằng nhau trong dung sai.

<a id="ml28-make"></a>

### E · Make 1 · Viết hàm

**`regression_pipeline(X_train, y_train, X_test, y_test)`**

Nhận hai ma trận 2D hữu hạn không rỗng cùng số cột dương và hai vector đích hữu hạn tương ứng. Fit Z-score tổng thể trên train (std=0 đổi thành 1), rồi fit least squares có intercept. Trả (dự đoán test, MAE test). Báo ValueError với đầu vào không hợp lệ.

Điền hàm. Chạy `python ML28.py`.

[Mã khởi đầu và 5 ca kiểm](#ml28-starter) · [Lời giải](#ml28-loi-giai)

<a id="ml28-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự dựng pipeline phân loại logistic dùng ML03, ML09, ML10, ML15. Train X=[[−2],[−1],[1],[2]], y=[0,0,1,1]. Fit scaler trên train, chạy 100 bước GD lr=0.5 từ tham số 0. Validation X=[[−0.5],[0.5]], y=[0,1], chọn ngưỡng trong [0.3,0.5,0.7] theo F1, hòa ưu tiên 0.5. Test X=[[−3],[3]], y=[0,1]. Kiểm chọn 0.5, dự đoán [0,1], F1=1.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

[Ôn thêm theo mã bài](#ml28-on-tap)

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="ml28-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2.0] [1.632993]
[17.0] 0.0
~~~

</details>

<details class="answer" id="ml28-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Mu=[2], std=[√(8/3)]. Train nằm trên y=2x+1, dự đoán 17. Đổi y_test sang 18 chỉ đổi MAE thành 1.

</details>

<details class="answer" id="ml28-starter" data-starter="ML28">
<summary>E · Mã khởi đầu và ca kiểm · ML28.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def regression_pipeline(X_train, y_train, X_test, y_test):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    p,m = regression_pipeline([[0,7],[2,7],[4,7]], [1,5,9], [[8,7],[10,7]], [18,20])
    same(p, [17,21])
    same(m, 1)


def case_02():
    p,m = regression_pipeline([[2],[2]], [1,5], [[3]], [4])
    same(p, [3])
    same(m, 1)


def case_03():
    p,m = regression_pipeline([[0],[2]], [0,2], [[4]], [12])
    same(p, [4])
    same(m, 8)


def case_04():
    rejects(regression_pipeline, [[0]], [0], [[1,2]], [0])


def case_05():
    rejects(regression_pipeline, [[float('nan')]], [0], [[1]], [0])


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="ml28-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def regression_pipeline(X_train, y_train, X_test, y_test):
    X_train, y_train, X_test, y_test = (np.asarray(v, dtype=float) for v in (X_train, y_train, X_test, y_test))
    if X_train.ndim != 2 or X_test.ndim != 2 or min(X_train.shape) == 0 or not len(X_test) or X_train.shape[1] != X_test.shape[1] or y_train.shape != (len(X_train),) or y_test.shape != (len(X_test),):
        raise ValueError("Shape không hợp lệ")
    if not all(np.isfinite(v).all() for v in (X_train, y_train, X_test, y_test)):
        raise ValueError("Cần dữ liệu hữu hạn")
    mu = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    scale = np.where(std == 0, 1, std)
    train = np.column_stack([np.ones(len(X_train)), (X_train-mu)/scale])
    test = np.column_stack([np.ones(len(X_test)), (X_test-mu)/scale])
    pred = test @ np.linalg.lstsq(train, y_train, rcond=None)[0]
    return pred, float(np.abs(pred - y_test).mean())
~~~

</details>

<a id="ml28-on-tap"></a>

### Ôn tập ML28

Làm câu hỏi trước. Mở đáp án sau khi đã thử giải. Sửa phép tính hoặc giả định sai rồi thử lại với dữ liệu mới.

#### Trắc nghiệm

##### ML28-mcq-1

Khi báo cáo kết quả hồi quy, đơn vị y cần được ghi ở đâu?

- **A** · Trong mô tả dữ liệu và diễn giải metric
- **B** · Bỏ qua vì mọi kết quả hồi quy cùng đơn vị
- **C** · Chỉ ghi seed

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Dự đoán và MAE/RMSE dùng cùng đơn vị với y.

- **A** · Ghi đơn vị trong mô tả dữ liệu và khi diễn giải metric.
- **B** · Đơn vị của y phụ thuộc dữ liệu và ảnh hưởng cách đọc kết quả.
- **C** · Seed không thay metadata đơn vị.

</details>

##### ML28-mcq-2

Đầu ra thật của runner không khớp expected,có nên sửa expected theo actual ngay để đạt PASS không?

- **A** · Có nếu còn thiếu số câu
- **B** · Không,phải kiểm công thức và nguồn của cả hai
- **C** · Có,máy luôn đúng thuật toán

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Expected là oracle phải có căn cứ,không lấy actual làm chuẩn tự động.

- **A** · Số lượng không thay bằng chứng.
- **B** · Expected là oracle phải có căn cứ,không lấy actual làm chuẩn tự động.
- **C** · Code chạy vẫn có thể sai.

</details>

##### ML28-mcq-3

Một kết quả trên dữ liệu mô phỏng cần giới hạn kết luận gì?

- **A** · Chứng minh hiệu năng trên mọi tập dữ liệu mới
- **B** · Chứng minh luôn đạt cùng metric ở mọi seed
- **C** · Chỉ chứng minh hành vi trên dữ liệu/quy trình mô phỏng đã nêu

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Không biến mô phỏng thành bằng chứng thực nghiệm ngoài phạm vi.

- **A** · Suy rộng cần dữ liệu đánh giá đại diện cho miền quan tâm.
- **B** · Seed khác có thể đổi dữ liệu và kết quả.
- **C** · Không biến mô phỏng thành bằng chứng thực nghiệm ngoài phạm vi.

</details>

##### ML28-mcq-4

Thống kê chuẩn hóa trong capstone cần học ở đâu?

- **A** · Train,hoặc train của từng fold
- **B** · Train và test gộp lại
- **C** · Test riêng

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Giữ test ngoài mọi bước fit.

- **A** · Giữ test ngoài mọi bước fit.
- **B** · Gây leakage trong đánh giá.
- **C** · Không học tiền xử lý từ test.

</details>

##### ML28-mcq-5

Dữ liệu tự sinh minh họa một pipeline nên được mô tả thế nào?

- **A** · Giấu seed để trông tự nhiên
- **B** · Ghi rõ là dữ liệu mô phỏng
- **C** · Gọi là dữ liệu quan sát

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Không biến mô phỏng thành kết quả thực nghiệm thực tế.

- **A** · Cản tái lập và dễ gây hiểu nhầm.
- **B** · Không biến mô phỏng thành kết quả thực nghiệm thực tế.
- **C** · Không có bằng chứng dữ liệu thực.

</details>

##### ML28-mcq-6

Quy tắc xác định nhãn phân loại cần được chốt lúc nào?

- **A** · Sau khi xem test để cho điểm tốt
- **B** · Luôn lấy giá trị dự đoán hồi quy làm tròn
- **C** · Định nghĩa rõ theo bài toán trước đánh giá

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Ngưỡng/quy tắc tạo nhãn phải minh bạch và không tối ưu bằng test.

- **A** · Làm metric bị lựa chọn theo kết quả.
- **B** · Không có định nghĩa nhãn thực phù hợp.
- **C** · Ngưỡng/quy tắc tạo nhãn phải minh bạch và không tối ưu bằng test.

</details>

##### ML28-mcq-7

K-fold capstone có cần train lại model ở mỗi fold không?

- **A** · Có
- **B** · Không,fit toàn dữ liệu một lần
- **C** · Chỉ thay tên fold

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án A**

Cả preprocessing và model fit theo train fold.

- **A** · Cả preprocessing và model fit theo train fold.
- **B** · Model đã thấy validation.
- **C** · Không tạo đánh giá độc lập.

</details>

##### ML28-mcq-8

Metric tính trên train có thể báo là test metric không?

- **A** · Có nếu model hội tụ
- **B** · Không
- **C** · Có nếu số đẹp

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án B**

Ghi chính xác nguồn dự đoán và nhãn.

- **A** · Hội tụ không thay tập đánh giá.
- **B** · Ghi chính xác nguồn dự đoán và nhãn.
- **C** · Tên tập không phụ thuộc kết quả.

</details>

##### ML28-mcq-9

Nếu test chỉ có một lớp,ROC/AUC nên làm gì?

- **A** · Tự gán AUC=1
- **B** · Dùng training AUC rồi đổi tên
- **C** · Báo không xác định theo quy tắc đã ghi

<details>
<summary>Đáp án và cách kiểm</summary>

**Đáp án C**

Cần cả hai lớp để ROC thông thường xác định đầy đủ.

- **A** · Thiếu lớp không chứng minh ranking hoàn hảo.
- **B** · Sai phạm vi đánh giá.
- **C** · Cần cả hai lớp để ROC thông thường xác định đầy đủ.

</details>

#### Tự luận và viết mã

##### ML28-practice-1

Pipeline gồm chia dữ liệu,fit scaler,train model,test. Sắp thứ tự tránh leakage.

<details>
<summary>Đáp án và cách kiểm</summary>

Chia train/test trước;fit scaler trên train;biến đổi hai tập bằng scaler train;fit model trên train;đánh giá test riêng.

</details>

##### ML28-practice-2

X có shape (40,3),y có 39 phần tử. Nên làm gì trước huấn luyện?

<details>
<summary>Đáp án và cách kiểm</summary>

Từ chối shape không khớp và tìm lỗi ghép dữ liệu;không cắt bỏ mẫu tùy tiện để qua test.

</details>

##### ML28-practice-3

Một cột có NaN. Nếu chọn điền mean,cần lấy mean từ đâu?

<details>
<summary>Đáp án và cách kiểm</summary>

Chỉ train của split/fold;áp dụng cùng giá trị đã học cho validation/test. Cần nêu quy tắc cho cột train toàn NaN.

</details>

##### ML28-practice-4

Định nghĩa lớp 1 là y ≥ 3. Với y=[2,3,4], vector nhãn là gì?

<details>
<summary>Đáp án và cách kiểm</summary>

[0,1,1]. Quy tắc y ≥ 3 đưa trường hợp đúng bằng ngưỡng vào lớp 1.

```python
y=[2.,3.,4.]
print([int(v>=3.) for v in y])
```
Kết quả: [0, 1, 1]

</details>

##### ML28-practice-5

Test y=[2,4],pred=[3,3]. Tính MAE và MSE.

<details>
<summary>Đáp án và cách kiểm</summary>

Residual [1,−1],MAE=1,MSE=1.

```python
import numpy as np
y=np.array([2.,4.]);pred=np.array([3.,3.]);e=pred-y
print(float(np.abs(e).mean()))
print(float((e*e).mean()))
```
Kết quả: 1.0
1.0

</details>

##### ML28-practice-6

Test classification y=[1,0,1],pred=[1,1,0]. Đếm TP,FP,FN.

<details>
<summary>Đáp án và cách kiểm</summary>

Mỗi count bằng 1;precision=recall=F1=0.5.

```python
y=[1,0,1];pred=[1,1,0]
print([sum(t==a and p==b for t,p in zip(y,pred)) for a,b in [(1,1),(0,1),(1,0)]])
```
Kết quả: [1, 1, 1]

</details>

##### ML28-practice-7

Một fold không có mẫu dương. Nên che lỗi bằng F1=1 không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Báo counts và áp dụng quy tắc mẫu số rõ ràng;không biến giới hạn dữ liệu thành thành tích tốt.

</details>

##### ML28-practice-8

Ba mô hình hồi quy dự đoán [2.8,3.0,3.2] cho cùng mẫu. Tính dự đoán ensemble bằng trung bình.

<details>
<summary>Đáp án và cách kiểm</summary>

3.0, cùng đơn vị với y.

```python
print(round(sum([2.8,3.,3.2])/3,6))
```
Kết quả: 3.0

</details>

##### ML28-practice-9

Một tập dữ liệu chỉ có sáu mẫu. Vì sao điểm test cao chưa đủ kết luận mô hình tổng quát hóa tốt?

<details>
<summary>Đáp án và cách kiểm</summary>

Số mẫu nhỏ khiến metric nhạy với cách chia. Cần thêm dữ liệu độc lập và phù hợp với tập dữ liệu mà mô hình sẽ gặp.

</details>

##### ML28-practice-10

Cần lưu những gì để người khác tái lập capstone mô phỏng?

<details>
<summary>Đáp án và cách kiểm</summary>

Code sinh dữ liệu/seed,schema/đơn vị,quy tắc nhãn,các chỉ số split,tham số scaler/model,quy tắc metric và kết quả thật.

</details>

##### ML28-practice-11

Nếu thử nhiều lựa chọn rồi chọn theo test tốt nhất,có thể báo test là đánh giá độc lập không?

<details>
<summary>Đáp án và cách kiểm</summary>

Không. Test đã tham gia lựa chọn;phải ghi rõ giới hạn và cần dữ liệu đánh giá độc lập mới nếu muốn kết luận tổng quát hóa.

</details>

<a id="mlp01"></a>

## MLP01 · Chuẩn bị dữ liệu · Danh mục, dữ liệu thiếu và rời rạc hóa

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML03](#ml03)

<a id="mlp01-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Mã hóa danh mục thành các đặc trưng số. Học danh sách giá trị danh mục từ train. Quy định cách mã hóa giá trị mới trước khi áp dụng cho dữ liệu khác.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán thứ tự hai mức và hàng mã hóa của từng giá trị trong X.
2. **P2** · Xác định bucket cho −2,0,3,5. Hai điểm đúng mép bin đi về phía nào?

<a id="mlp01-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
train = np.array(["b", "a", "b"])
X = np.array(["a", "c", "b"])
levels = np.unique(train)
O = (X[:, None] == levels[None, :]).astype(int)
bins = np.searchsorted([0., 5.], [-2., 0., 3., 5.], side="right")
print(levels.tolist(), O.tolist())
print(bins.tolist())
~~~

[Xem kết quả mẫu](#mlp01-ket-qua)

<a id="mlp01-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Phân biệt danh mục 'a','b' với mã thứ tự. Giải thích vì sao dùng 0 và 1 làm mã cho cả cột có thể tạo khoảng cách tùy ý.
2. **I2** · Giải thích vì sao mức 'c' không tạo thêm cột. Nêu cách báo cáo tỷ lệ hàng rơi vào mức chưa thấy.

[Đối chiếu cách giải thích](#mlp01-giai-thich)

<a id="mlp01-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi train thành ['b','b','c']. Kiểm 'a' rơi vào vector 0 và 'c' nhận [0,1].
2. **MO2** · Đổi `side` thành `left`. Kiểm bucket mới [0,0,1,1].
3. **MO3** · Thêm cột 'unknown' với giá trị 1 cho hàng mã hóa toàn 0. Kiểm hàng 'c' thành [0,0,1].

<a id="mlp01-make"></a>

### E · Make 1 · Viết hàm

**`encode_categories(train, values)`**

Nhận hai list chuỗi, train không rỗng. Trả (list mức phân biệt xếp tăng, ma trận one-hot của values). Mức lạ thành hàng 0, values có thể rỗng. Báo ValueError nếu train rỗng hoặc đầu vào sai chiều.

Điền hàm. Chạy `python MLP01.py`.

[Mã khởi đầu và 4 ca kiểm](#mlp01-starter) · [Lời giải](#mlp01-loi-giai)

<a id="mlp01-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết bước tiền xử lý ghép one-hot với cột số. Học trung vị từ train [2,NaN,6], rồi điền giá trị NaN của [NaN,8] thành [4,8]. Học các mức train ['b','a','b'], mã hóa ['c','a']. Kiểm ma trận cuối [[4,0,0],[8,1,0]].

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp01-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
['a', 'b'] [[1, 0], [0, 0], [0, 1]]
[0, 1, 1, 2]
~~~

</details>

<details class="answer" id="mlp01-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Mức ['a','b'], ma trận [[1,0],[0,0],[0,1]]. Các bucket là [0,1,1,2], điểm bằng mép đi sang bucket cao hơn với side='right'.

</details>

<details class="answer" id="mlp01-starter" data-starter="MLP01">
<summary>E · Mã khởi đầu và ca kiểm · MLP01.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def encode_categories(train, values):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    levels, rows = encode_categories(['b','x','b'], ['x','a','b'])
    assert levels == ['b','x']
    same(rows, [[0,1],[0,0],[1,0]])


def case_02():
    same(encode_categories(['a'],[])[1], np.empty((0,1)))


def case_03():
    rejects(encode_categories, [], ['a'])


def case_04():
    rejects(encode_categories, [['m']], ['m'])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp01-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def encode_categories(train, values):
    train, values = np.asarray(train, dtype=str), np.asarray(values, dtype=str)
    if train.ndim != 1 or not train.size or values.ndim != 1:
        raise ValueError("Đầu vào không hợp lệ")
    levels = np.unique(train)
    return levels.tolist(), (values[:, None] == levels[None, :]).astype(int)
~~~

</details>

<a id="mlp02"></a>

## MLP02 · Chọn đặc trưng · Filter, wrapper và embedded

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML17](#ml17)

<a id="mlp02-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Filter chấm đặc trưng độc lập với mô hình. Wrapper so các tập con bằng điểm validation. Embedded lấy thông tin từ quá trình fit, như hệ số L1 hoặc độ quan trọng của cây.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính phương sai tổng thể từng cột. Dự đoán chỉ số hai cột được giữ.
2. **P2** · Nếu ngưỡng tăng thành 1, dự đoán shape bảng sau lọc.

<a id="mlp02-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[0., 1., 10.], [0., 2., 0.], [0., 3., 10.]])
scores = X.var(axis=0)
keep = np.flatnonzero(scores > 0.5)
print(scores.round(6).tolist(), keep.tolist())
print(X[:, keep].tolist())
~~~

[Xem kết quả mẫu](#mlp02-ket-qua)

<a id="mlp02-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao variance không dùng y và bị tác động bởi thang đo. Cột variance lớn có chắc dự đoán tốt?
2. **I2** · Phân biệt chọn các cột gốc với chiếu PCA. Chỉ ra dữ liệu nào được phép dùng để xếp hạng.

[Đối chiếu cách giải thích](#mlp02-giai-thich)

<a id="mlp02-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Nhân cột giữa với 0.1 và giữ ngưỡng. Kiểm chỉ còn cột 2.
2. **MO2** · Dùng điểm tuyệt đối correlation với y=[1,2,3]. Cho điểm 0 với cột hằng. Kiểm cột 1 có score cao nhất.
3. **MO3** · Thay filter bằng quy tắc embedded `abs(w)>0.1` trên hệ số giả định [0,−0.8,0.02]. Kiểm giữ cột 1 và nêu hệ số phải được fit ở đâu.

<a id="mlp02-make"></a>

### E · Make 1 · Viết hàm

**`variance_filter(train, X, cutoff)`**

Với train 2D hữu hạn không rỗng và X 2D hữu hạn cùng số cột, giữ cột có phương sai tổng thể > cutoff hữu hạn ≥ 0. Trả (chỉ số cột, X đã chọn), cho phép 0 cột được giữ. Báo ValueError nếu shape hoặc cutoff sai.

Điền hàm. Chạy `python MLP02.py`.

[Mã khởi đầu và 4 ca kiểm](#mlp02-starter) · [Lời giải](#mlp02-loi-giai)

<a id="mlp02-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết một lượt forward selection theo validation MSE. Fit least squares có intercept lần lượt trên từng cột train [[0,0],[1,0],[2,1],[3,1]], y=[0,2,4,6]. Validation [[4,0],[5,1]], y=[8,10]. Kiểm chọn cột 0 và MSE gần 0. Mở rộng so với Lasso hoặc độ quan trọng cây ở cùng split.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp02-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[0.0, 0.666667, 22.222222] [1, 2]
[[1.0, 10.0], [2.0, 0.0], [3.0, 10.0]]
~~~

</details>

<details class="answer" id="mlp02-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Variance [0,2/3,200/9], giữ cột 1 và 2. Cutoff 1 còn một cột nên shape (3,1). Chỉ cần thống kê train để quyết định cột.

</details>

<details class="answer" id="mlp02-starter" data-starter="MLP02">
<summary>E · Mã khởi đầu và ca kiểm · MLP02.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def variance_filter(train, X, cutoff):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    idx, out = variance_filter([[1,0,0],[1,2,1]], [[8,4,2]], 0.25)
    same(idx,[1])
    same(out,[[4]])


def case_02():
    idx, out = variance_filter([[2,2],[2,2]], [[9,9]], 0)
    same(idx,[])
    same(out,np.empty((1,0)))


def case_03():
    same(variance_filter([[0],[2]], [[100]], 0)[1], [[100]])


def case_04():
    rejects(variance_filter, [[1,2]], [[2]], 0)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp02-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def variance_filter(train, X, cutoff):
    train, X = np.asarray(train, dtype=float), np.asarray(X, dtype=float)
    if train.ndim != 2 or min(train.shape) == 0 or X.ndim != 2 or X.shape[1] != train.shape[1] or not np.isfinite(cutoff) or cutoff < 0 or not np.isfinite(train).all() or not np.isfinite(X).all():
        raise ValueError("Đầu vào không hợp lệ")
    keep = np.flatnonzero(train.var(axis=0) > cutoff)
    return keep, X[:, keep]
~~~

</details>

<a id="mlp03"></a>

## MLP03 · Phân cụm phân cấp · Single và complete linkage

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML23](#ml23)

<a id="mlp03-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Bắt đầu với mỗi điểm là một cụm. Để đo khoảng cách giữa hai cụm, single linkage lấy khoảng cách nhỏ nhất giữa các cặp điểm và complete linkage lấy lớn nhất.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Liệt kê khoảng cách giữa các điểm và dự đoán cặp gộp đầu ở độ cao 1.
2. **P2** · Dự đoán lần gộp sau và phân hoạch còn hai cụm.

<a id="mlp03-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
from itertools import combinations
X = [0., 2., 5., 6.]
groups = [[i] for i in range(len(X))]
while len(groups) > 2:
    pairs = [(min(abs(X[a]-X[b]) for a in groups[i] for b in groups[j]), i, j)
             for i,j in combinations(range(len(groups)), 2)]
    distance, i, j = min(pairs)
    merged = sorted(groups[i]+groups[j])
    groups[i] = merged
    groups.pop(j)
    print(distance, merged)
print(groups)
~~~

[Xem kết quả mẫu](#mlp03-ket-qua)

<a id="mlp03-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao lần lặp tìm cặp cụm theo chỉ số chứ không chỉ cặp mẫu trực tiếp.
2. **I2** · So single và complete cho hai cụm cuối [0,1] và [2,3]. Với X gốc, tính hai giá trị 3 và 6.

[Đối chiếu cách giải thích](#mlp03-giai-thich)

<a id="mlp03-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi điều kiện dừng thành một cụm. Kiểm độ cao lần cuối bằng 3.
2. **MO2** · Đặt X=[0,1,2]. Kiểm hai cặp cùng khoảng cách 1 và chỉ số nhỏ được chọn trước.
3. **MO3** · Thử X=[0,1,3,5.5]. Kiểm single gộp [0,1,2] ở lượt hai, complete gộp [2,3].

<a id="mlp03-make"></a>

### E · Make 1 · Viết hàm

**`linkage_history(X, linkage)`**

Nhận vector 1D hữu hạn có ít nhất một mẫu và linkage 'single' hoặc 'complete'. Trả list (độ cao, list chỉ số của cụm vừa gộp) đến khi còn một cụm. Giữ vị trí i sau khi gộp i<j, hòa độ cao chọn (i,j) nhỏ nhất. Báo ValueError nếu đầu vào sai.

Điền hàm. Chạy `python MLP03.py`.

[Mã khởi đầu và 5 ca kiểm](#mlp03-starter) · [Lời giải](#mlp03-loi-giai)

<a id="mlp03-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết cắt cây tại độ cao h, áp dụng các lần gộp có độ cao ≤ h. Với [0,2,5,6], h=4, kiểm single cho một cụm và complete cho hai cụm.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp03-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
1.0 [2, 3]
2.0 [0, 1]
[[0, 1], [2, 3]]
~~~

</details>

<details class="answer" id="mlp03-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Gộp [2,3] ở độ cao 1 rồi [0,1] ở độ cao 2. Hai cụm cuối là [[0,1],[2,3]]. Khoảng cách single là 3 và complete là 6.

</details>

<details class="answer" id="mlp03-starter" data-starter="MLP03">
<summary>E · Mã khởi đầu và ca kiểm · MLP03.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def linkage_history(X, linkage):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    assert linkage_history([0,2,5,6], 'single') == [(1,[2,3]),(2,[0,1]),(3,[0,1,2,3])]


def case_02():
    assert linkage_history([0,2,5,6], 'complete')[-1] == (6,[0,1,2,3])


def case_03():
    assert linkage_history([0,1,2], 'single')[0] == (1,[0,1])


def case_04():
    assert linkage_history([5], 'single') == []


def case_05():
    rejects(linkage_history, [0,1], 'unknown')


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp03-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
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
~~~

</details>

<a id="mlp04"></a>

## MLP04 · DBSCAN · Core, border và noise

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML23](#ml23)

<a id="mlp04-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Một điểm là core nếu vùng bán kính eps có ít nhất min_samples điểm, tính cả chính nó. Điểm kề core có thể là border. Các điểm còn lại là noise.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Đếm hàng x=0.5 và 8 có bao nhiêu điểm trong vùng lân cận. Dự đoán các chỉ số core.
2. **P2** · Liệt kê các điểm border và noise. Dự đoán số cụm nếu mở rộng từ từng core.

<a id="mlp04-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([0., 0.5, 1., 4., 4.5, 5., 8.])
adj = np.abs(x[:,None]-x[None,:]) <= 0.5
core = adj.sum(axis=1) >= 3
print(adj.sum(axis=1).tolist(), core.tolist())
print((adj[:,core].any(axis=1) & ~core).tolist())
~~~

[Xem kết quả mẫu](#mlp04-ket-qua)

<a id="mlp04-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao đường chéo của adj là True. Nêu khác biệt giữa < eps và ≤ eps.
2. **I2** · Chỉ ra lý do chỉ core được dùng để lan ra thêm điểm. Border ở giữa hai nhóm có nhất thiết nhập chúng thành một cụm?

[Đối chiếu cách giải thích](#mlp04-giai-thich)

<a id="mlp04-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi eps thành 0.49. Kiểm mọi điểm thành noise khi min_samples=3.
2. **MO2** · Đổi min_samples thành 2, giữ eps=0.5. Kiểm có 6 core và 1 noise.
3. **MO3** · Đặt x=[0,0.5,1,1.5,2] và eps=0.5. Kiểm core ở [0.5,1,1.5] nối thành một cụm dù khoảng cách hai đầu lớn hơn eps.

<a id="mlp04-make"></a>

### E · Make 1 · Viết hàm

**`dbscan_1d(x, eps, min_samples)`**

Nhận vector 1D hữu hạn, eps hữu hạn không âm, min_samples nguyên dương. Duyệt core theo chỉ số tăng. Với mỗi core chưa nhãn, mở rộng qua các core kề, gán lân cận chưa nhãn vào cụm hiện tại. Nhãn cụm bắt đầu từ 0, nhiễu −1. Trả vector nhãn và báo ValueError nếu miền sai.

Điền hàm. Chạy `python MLP04.py`.

[Mã khởi đầu và 5 ca kiểm](#mlp04-starter) · [Lời giải](#mlp04-loi-giai)

<a id="mlp04-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự thay phép đo bằng khoảng cách Euclid 2D. Với X=[[0,0],[0,1],[1,1],[5,5]], eps=1, min_samples=3, kiểm [0,0,0,−1]. Thêm một ca chỉ một border chen giữa hai cụm core và ghi quy tắc gán.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp04-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2, 3, 2, 2, 3, 2, 1] [False, True, False, False, True, False, False]
[True, False, True, True, False, True, False]
~~~

</details>

<details class="answer" id="mlp04-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Số láng giềng [2,3,2,2,3,2,1]. Core ở chỉ số 1 và 4, border ở 0,2,3,5, noise ở 6. Hai core không nối với nhau nên tạo hai cụm.

</details>

<details class="answer" id="mlp04-starter" data-starter="MLP04">
<summary>E · Mã khởi đầu và ca kiểm · MLP04.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def dbscan_1d(x, eps, min_samples):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(dbscan_1d([0,0.5,1,4,4.5,5,8], 0.5, 3), [0,0,0,1,1,1,-1])


def case_02():
    same(dbscan_1d([0,0.5,1,1.5,2], 0.5, 3), [0,0,0,0,0])


def case_03():
    same(dbscan_1d([0,3,3], 0, 2), [-1,0,0])


def case_04():
    same(dbscan_1d([], 1, 1), [])


def case_05():
    rejects(dbscan_1d, [1], -1, 2)


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp04-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
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
~~~

</details>

<a id="mlp05"></a>

## MLP05 · SVM · Margin, hinge loss và kernel

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML19](#ml19)

<a id="mlp05-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Dùng nhãn −1 hoặc +1. Điểm có functional margin y(w·x+b) dưới 1 chịu hinge loss. Tham số C điều chỉnh mức phạt.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính từng functional margin và hinge loss.
2. **P2** · Dự đoán mục tiêu với C=2. Xác định một điểm dự đoán sai và một điểm đúng ngay trên biên margin.

<a id="mlp05-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[-2.], [-0.5], [1.], [2.]])
y = np.array([-1., 1., 1., 1.])
w = np.array([1.])
b, C = 0., 2.
signed = y * (X @ w + b)
hinge = np.maximum(0, 1 - signed)
print(signed.tolist(), hinge.tolist())
print(0.5*(w @ w) + C*hinge.sum())
~~~

[Xem kết quả mẫu](#mlp05-ket-qua)

<a id="mlp05-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Phân biệt z=0 với y·z=1. Với w=1, tính khoảng cách giữa hai đường margin.
2. **I2** · Chỉ ra phần phạt trọng số và phần phạt vi phạm. Giải thích điều có thể xảy ra khi C tăng.

[Đối chiếu cách giải thích](#mlp05-giai-thich)

<a id="mlp05-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi C thành 1 và giữ tham số. Kiểm mục tiêu bằng 2.
2. **MO2** · Đổi riêng nhãn của x=−0.5 sang −1. Kiểm hinge của nó giảm còn 0.5, tổng mục tiêu còn 1.5.
3. **MO3** · Viết kernel đa thức (u·v+1)² cho u=[1,2] và v=[2,1]. Kiểm giá trị 25; so với kernel tuyến tính cho giá trị 4.

<a id="mlp05-make"></a>

### E · Make 1 · Viết hàm

**`svm_objective(X, y, w, b, C)`**

Với ma trận n×d, n,d dương, y thuộc {−1,1}, vector w đúng d, C hữu hạn dương, trả (hinge từng mẫu, 0.5·||w||²+C·tổng hinge). Báo ValueError nếu shape, nhãn hoặc C sai.

Điền hàm. Chạy `python MLP05.py`.

[Mã khởi đầu và 4 ca kiểm](#mlp05-starter) · [Lời giải](#mlp05-loi-giai)

<a id="mlp05-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự fit SVM tuyến tính và SVM kernel đa thức bậc 2 bằng scikit-learn. Dùng bốn điểm (±1,±1), nhãn +1 khi x₁x₂>0. Với `SVC(C=10,kernel='poly',degree=2,gamma=1,coef0=1)`, kiểm đúng bốn điểm. Mô hình tuyến tính không đạt 4/4. Viết kết luận về khả năng biểu diễn trên dữ liệu này.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp05-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2.0, -0.5, 1.0, 2.0] [0.0, 1.5, 0.0, 0.0]
3.5
~~~

</details>

<details class="answer" id="mlp05-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Functional margin [2,−0.5,1,2], hinge [0,1.5,0,0], mục tiêu 3.5. x=−0.5 dự đoán sai, x=1 đúng ngay biên margin. Hai biên cách 2/‖w‖=2.

</details>

<details class="answer" id="mlp05-starter" data-starter="MLP05">
<summary>E · Mã khởi đầu và ca kiểm · MLP05.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def svm_objective(X, y, w, b, C):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    h,obj = svm_objective([[-1],[1]], [-1,1], [1], 0, 3)
    same(h,[0,0])
    same(obj,0.5)


def case_02():
    h,obj = svm_objective([[0],[2]], [-1,1], [0], 1, 2)
    same(h,[2,0])
    same(obj,4)


def case_03():
    h,obj = svm_objective([[-0.25],[1]], [-1,1], [1], 0, 1)
    same(h,[0.75,0])
    same(obj,1.25)


def case_04():
    rejects(svm_objective, [[0]], [0], [1], 0, 1)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp05-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def svm_objective(X, y, w, b, C):
    X, y, w = (np.asarray(v, dtype=float) for v in (X, y, w))
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),) or w.shape != (X.shape[1],) or not np.isin(y, [-1,1]).all() or not np.isfinite(C) or C <= 0:
        raise ValueError("Đầu vào không hợp lệ")
    hinge = np.maximum(0, 1 - y * (X @ w + b))
    return hinge, float(0.5 * (w @ w) + C * hinge.sum())
~~~

</details>

<a id="mlp06"></a>

## MLP06 · SVD · Chiếu và dựng lại dữ liệu

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML25](#ml25)

<a id="mlp06-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Trừ tâm rồi phân rã C = UΣVᵀ. Các cột của V cho trục PCA. Bình phương giá trị kỳ dị rồi chia n−1 để tính phương sai mẫu theo trục.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Tính shape U, sigma, Vt và Z. Dự đoán ý nghĩa hai σ².
2. **P2** · Xác định trục bị bỏ khi k=1, rồi tính tổng lỗi dựng lại bình phương.

<a id="mlp06-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
X = np.array([[-2.,0.], [2.,0.], [0.,1.], [0.,-1.]])
C = X - X.mean(axis=0)
U, sigma, Vt = np.linalg.svd(C, full_matrices=False)
Z = C @ Vt[:1].T
reconstructed = Z @ Vt[:1]
print((sigma**2 / (len(X)-1)).round(6).tolist())
print(round(np.sum((C-reconstructed)**2), 6))
~~~

[Xem kết quả mẫu](#mlp06-ket-qua)

<a id="mlp06-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao hàng của Vt nằm trong không gian đặc trưng còn cột U nằm trong không gian mẫu.
2. **I2** · Đổi dấu hàng Vt đầu tiên và đổi dấu tọa độ Z tương ứng. Kiểm reconstruction giữ nguyên.

[Đối chiếu cách giải thích](#mlp06-giai-thich)

<a id="mlp06-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Giữ hai thành phần. Kiểm lỗi dựng lại gần 0.
2. **MO2** · Nhân cột 2 với 3. Kiểm thành phần bị bỏ là cột 1 và lỗi dựng lại bằng 8.
3. **MO3** · Cộng [4,7] vào tất cả hàng. Khôi phục bằng cách cộng lại trung bình. Kiểm SSE giữ nguyên.

<a id="mlp06-make"></a>

### E · Make 1 · Viết hàm

**`svd_reconstruct(X, k)`**

Nhận ma trận 2D hữu hạn có n,d dương, k nguyên trong [0,min(n,d)]. Trả (ma trận dựng lại hạng k sau khi trừ tâm và cộng lại trung bình, SSE). Với k=0, dựng lại từng hàng bằng mean. Báo ValueError nếu miền sai.

Điền hàm. Chạy `python MLP06.py`.

[Mã khởi đầu và 4 ca kiểm](#mlp06-starter) · [Lời giải](#mlp06-loi-giai)

<a id="mlp06-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự viết hàm chọn k nhỏ nhất giữ ít nhất 90% tổng σ². Với σ=[4,2,1], kiểm k=2. Đối chiếu tỉ lệ tích lũy với eigenvalues covariance của ML25 trên cùng ma trận.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp06-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[2.666667, 0.666667]
2.0
~~~

</details>

<details class="answer" id="mlp06-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

U (4,2), sigma (2,), Vt (2,2), Z (4,1). Hai σ² là 8 và 2. Bỏ trục thứ hai tạo SSE 2.

</details>

<details class="answer" id="mlp06-starter" data-starter="MLP06">
<summary>E · Mã khởi đầu và ca kiểm · MLP06.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def svd_reconstruct(X, k):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    R,sse = svd_reconstruct([[-2,0],[2,0],[0,1],[0,-1]], 1)
    same(R,[[-2,0],[2,0],[0,0],[0,0]])
    same(sse,2)


def case_02():
    R,sse = svd_reconstruct([[1,3],[3,7]], 0)
    same(R,[[2,5],[2,5]])
    same(sse,10)


def case_03():
    same(svd_reconstruct([[2,5,7]], 1)[0], [[2,5,7]])


def case_04():
    rejects(svd_reconstruct, [[1,2]], 2)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp06-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def svd_reconstruct(X, k):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or min(X.shape) == 0 or not np.isfinite(X).all() or not isinstance(k, (int, np.integer)) or not 0 <= k <= min(X.shape):
        raise ValueError("Đầu vào không hợp lệ")
    mu = X.mean(axis=0)
    U, sigma, Vt = np.linalg.svd(X - mu, full_matrices=False)
    reconstructed = (U[:, :k] * sigma[:k]) @ Vt[:k] + mu
    return reconstructed, float(np.sum((X - reconstructed)**2))
~~~

</details>

<a id="mlp07"></a>

## MLP07 · Self-Organizing Map · Chọn và cập nhật prototype

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML23](#ml23)

<a id="mlp07-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Tìm prototype gần mẫu nhất. Cập nhật prototype thắng và các láng giềng theo khoảng cách trên lưới.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán chỉ số prototype thắng và ba vị trí được cập nhật.
2. **P2** · Tính trọng số mới của mỗi prototype. Prototype xa trên lưới có được đổi không?

<a id="mlp07-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
w = np.array([0., 4., 8., 12.])
x, lr, radius = 5., 0.5, 1
winner = int(np.argmin(np.abs(w-x)))
neighbor = np.abs(np.arange(len(w))-winner) <= radius
next_w = w + lr*neighbor*(x-w)
print(winner, neighbor.tolist(), next_w.tolist())
~~~

[Xem kết quả mẫu](#mlp07-ket-qua)

<a id="mlp07-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · So khoảng cách dữ liệu dùng chọn winner với khoảng cách theo chỉ số lưới dùng chọn láng giềng.
2. **I2** · Giải thích vai trò của lr và radius. So sánh radius=0 với cập nhật tâm trực tuyến.

[Đối chiếu cách giải thích](#mlp07-giai-thich)

<a id="mlp07-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Đổi radius=0. Kiểm kết quả [0,4.5,8,12].
2. **MO2** · Đổi x=6. Kiểm hai prototype hòa và chỉ số 1 thắng.
3. **MO3** · Giữ x=5, radius=1, đổi lr=1. Kiểm ba prototype trong vùng lân cận bằng 5.

<a id="mlp07-make"></a>

### E · Make 1 · Viết hàm

**`som_step(weights, x, lr, radius)`**

weights là ma trận (số node, số đặc trưng) hữu hạn không rỗng, x là vector tương ứng. Các node nằm trên lưới 1D theo chỉ số. Chọn winner bằng Euclid, hòa lấy chỉ số nhỏ. Cập nhật node cách winner ≤ radius nguyên không âm với lr trong [0,1]. Trả (winner, weights mới), báo ValueError nếu miền sai.

Điền hàm. Chạy `python MLP07.py`.

[Mã khởi đầu và 4 ca kiểm](#mlp07-starter) · [Lời giải](#mlp07-loi-giai)

<a id="mlp07-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự chạy hai bước trên weights=[[0],[4],[8]], radius lần lượt [1,0], lr=[0.5,0.5] và x=[1,7]. Kiểm trọng số cuối [[0.5],[2.5],[7.5]]. Sau đó đảo thứ tự hai x và so kết quả.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp07-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
1 [True, True, True, False] [2.5, 4.5, 6.5, 12.0]
~~~

</details>

<details class="answer" id="mlp07-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Winner là chỉ số 1. Mask [True,True,True,False]. Trọng số mới [2.5,4.5,6.5,12].

</details>

<details class="answer" id="mlp07-starter" data-starter="MLP07">
<summary>E · Mã khởi đầu và ca kiểm · MLP07.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def som_step(weights, x, lr, radius):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    i,W = som_step([[0],[4],[8],[12]],[5],0.5,1)
    assert i == 1
    same(W,[[2.5],[4.5],[6.5],[12]])


def case_02():
    i,W = som_step([[0,0],[2,0],[4,0]],[1,0],1,0)
    assert i == 0
    same(W,[[1,0],[2,0],[4,0]])


def case_03():
    same(som_step([[0],[4]], [1], 0, 2)[1], [[0],[4]])


def case_04():
    rejects(som_step, [[0]], [0], 1.1, 0)


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp07-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
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
~~~

</details>

<a id="mlp08"></a>

## MLP08 · Đánh giá phân cụm · Davies–Bouldin và NMI

[Mục lục](#muc-luc) · Bài bổ sung từ Drive · Tiên quyết [ML24](#ml24)

<a id="mlp08-predict"></a>

### A · Predict · Dự đoán

**Mục tiêu.** Với mỗi cụm, lấy tỷ số lớn nhất giữa tổng độ phân tán của hai cụm và khoảng cách hai tâm. Lấy trung bình các giá trị đó để tính Davies–Bouldin.

Đọc mã ở ô B. Ghi dự đoán trước khi chạy.

1. **P1** · Dự đoán hai tâm, hai độ phân tán và DB dưới dạng phân số.
2. **P2** · Nếu dời cụm thứ hai sang xa thêm 8 đơn vị, dự đoán chiều thay đổi của DB.

<a id="mlp08-run"></a>

### B · Run · Chạy mẫu

Chạy mã mẫu. Ghi giá trị, thứ tự và shape của đầu ra. So với dự đoán.

~~~python
import numpy as np
x = np.array([0., 2., 8., 10.])
labels = np.array([5, 5, 7, 7])
groups = [x[labels == i] for i in np.unique(labels)]
centers = np.array([g.mean() for g in groups])
scatter = np.array([np.abs(g-c).mean() for g,c in zip(groups, centers)])
ratio = (scatter[0] + scatter[1])/abs(centers[0]-centers[1])
print(centers.tolist(), scatter.tolist(), ratio)
~~~

[Xem kết quả mẫu](#mlp08-ket-qua)

<a id="mlp08-investigate"></a>

### C · Investigate · Lần theo mã

1. **I1** · Giải thích vì sao DB là internal validation. So với NMI dùng nhãn tham chiếu từ một phân hoạch khác.
2. **I2** · Giải thích tại sao nhân mọi khoảng cách với cùng số dương giữ nguyên DB.

[Đối chiếu cách giải thích](#mlp08-giai-thich)

<a id="mlp08-modify"></a>

### D · Modify · Sửa mã

Sao chép mã mẫu cho từng lượt. Dự đoán trước, chạy lại rồi ghi điều thay đổi.

1. **MO1** · Nhân x với 2. Kiểm DB giữ nguyên.
2. **MO2** · Đổi x thành [0,2,4,6]. Kiểm DB tăng lên 0.5.
3. **MO3** · Thêm nhóm thứ ba x=[20,22]. Lập bảng tỷ số từng cặp. Kiểm nhóm 3 có tỷ số lớn nhất bằng 1/6.

<a id="mlp08-make"></a>

### E · Make 1 · Viết hàm

**`davies_bouldin_1d(x, labels)`**

Với x 1D hữu hạn, labels nguyên cùng shape, có 2..n−1 cụm và mọi tâm phân biệt, trả DB cho khoảng cách tuyệt đối. Độ phân tán là trung bình khoảng cách tới tâm. Báo ValueError khi shape, số cụm hoặc tâm sai điều kiện.

Điền hàm. Chạy `python MLP08.py`.

[Mã khởi đầu và 5 ca kiểm](#mlp08-starter) · [Lời giải](#mlp08-loi-giai)

<a id="mlp08-transfer"></a>

### F · Make 2 · Bài chuyển giao

Tự lập bảng chéo hai phân hoạch và tính NMI theo trung bình số học 2·I/(Hₐ+Hᵦ). Với a=[0,0,1,1] và b=[2,2,3,3], kiểm NMI=1. Với b=[2,3,2,3], kiểm NMI=0. Dùng NMI=1 khi cả hai entropy bằng 0.

Làm bài trong tệp riêng. Thêm một ca mới và ghi kết quả kỳ vọng.

### Kết quả, mã khởi đầu và lời giải

<details class="answer" id="mlp08-ket-qua">
<summary>B · Kết quả khi chạy mẫu</summary>

~~~text
[1.0, 9.0] [1.0, 1.0] 0.25
~~~

</details>

<details class="answer" id="mlp08-giai-thich">
<summary>C · Giải thích Predict và Investigate</summary>

Hai tâm [1,9], scatter [1,1], DB=2/8=0.25. Khi dời cụm thứ hai xa thêm 8, DB giảm xuống 1/8.

</details>

<details class="answer" id="mlp08-starter" data-starter="MLP08">
<summary>E · Mã khởi đầu và ca kiểm · MLP08.py</summary>

~~~python
"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def davies_bouldin_1d(x, labels):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(davies_bouldin_1d([0,2,8,10],[9,9,2,2]), 0.25)


def case_02():
    same(davies_bouldin_1d([0,2,8,10,20,22],[0,0,1,1,2,2]), 2/9)


def case_03():
    same(davies_bouldin_1d([0,0,5],[1,1,2]), 0)


def case_04():
    rejects(davies_bouldin_1d, [0,1,2], [0,1,0])


def case_05():
    rejects(davies_bouldin_1d, [0,1], [0,1])


CASES = [case_01, case_02, case_03, case_04, case_05]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
~~~

</details>

<details class="answer" id="mlp08-loi-giai">
<summary>E · Lời giải tham khảo Make 1</summary>

~~~python
import numpy as np

def davies_bouldin_1d(x, labels):
    x, labels = np.asarray(x, dtype=float), np.asarray(labels)
    if x.ndim != 1 or labels.shape != x.shape or not np.isfinite(x).all():
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
~~~

</details>

<a id="doi-chieu"></a>

## Đối chiếu với tài liệu Drive

### Kết luận

**Commit `dd6cfd7` khớp bộ giáo trình 603 câu trên Drive. Phạm vi slide USTH rộng hơn bộ 28 bài.** Bản đồ 28 hàng trong CSV khớp mã, tên bài, module và danh sách khái niệm của `source/course.json`. Tệp `ML_603_lessons_final.json` trên Drive trùng từng byte với `reference/studio-lessons.json` trong commit. SHA-256 của cả hai là `6448f5b248903ef0d8ff3e61bc2e589a5940083d62b90d6084d6463742fb9784`. [Commit gốc](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/commit/dd6cfd7652f0f5ba39179cdc9293a7016dc2bf99) · [JSON 603 câu](https://drive.google.com/file/d/1Fj2sOc134m_uvpMIhvTJcT8Qmzm2mFWe/view) · [CSV 28 bài](https://drive.google.com/file/d/1_UP5P5Mbu81srvNQYy1L8O3L3BS4Ce8_/view) · [Thư mục Drive](https://drive.google.com/drive/folders/1fwg-IDH1LrU0ekEIzx9e873vrnZH8Yhc)

**Phần thực hành của commit thiếu triển khai ở 20 bài.** Từ ML09 đến ML28, `referenceSolution` của bài S4 chỉ chuyển đầu vào thành mảng, kiểm tra rỗng rồi trả lại mảng nguyên. Ví dụ, ML09 chưa tính sigmoid, ML23 chưa gán hoặc cập nhật centroid và ML28 chưa fit mô hình hay đánh giá. Ví dụ Run của ba bài ML06–ML08 chỉ in một câu, còn 20 bài ML09–ML28 chỉ in shape (1, 2). Bản PRIMM có mã thực hiện mục tiêu từng bài và ca kiểm kết quả số, kích thước hoặc điều kiện biên. [Dữ liệu bài gốc](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/blob/dd6cfd7652f0f5ba39179cdc9293a7016dc2bf99/PE_Machine_Learning/source/practice.json) · [PRIMM ML09](#ml09) · [PRIMM ML23](#ml23) · [PRIMM ML28](#ml28)

### Đối chiếu ML01–ML28 theo nội dung

Số trang tính từ đầu tệp PDF, kể cả trang bìa. Số slide tính theo thứ tự ở tệp PowerPoint. “Khớp” ở bảng này dùng cho phạm vi khái niệm, công thức và mục tiêu luyện tập chính của bài.

| Mã | Kết luận đối với commit | Bằng chứng trong Drive |
|---|---|---|
| ML01 | Khớp mẫu, thuộc tính và biểu diễn ma trận. | [Statistics and PCA, tr. 3–5, 12](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) · [Data Preparation, slide 3–10](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) |
| ML02 | Khớp mean, phương sai và covariance. Cần ghi rõ quy ước mẫu hay tổng thể. | [Statistics and PCA, tr. 8–16](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) |
| ML03 | Khớp scaling. Fit tham số trên train là phần triển khai thêm; phần chuẩn bị dữ liệu trong Drive còn rộng hơn. | [Linear Regression, tr. 30](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) · [Data Preparation, slide 11–19](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) |
| ML04 | Khớp mô hình tuyến tính và loss bình phương có hệ số 1/2. | [Linear Regression, tr. 4–7, 11](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) |
| ML05 | Khớp gradient, learning rate và một bước cập nhật. | [Linear Regression, tr. 8–13, 16–18](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) |
| ML06 | Khớp Batch, SGD, mini-batch; Run gốc thiếu ví dụ thuật toán. | [Linear Regression, tr. 14–15, 27](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) |
| ML07 | Khớp hồi quy nhiều đầu vào và normal equations; cần thêm xử lý thiếu hạng. | [Linear Regression, tr. 19–26](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) |
| ML08 | Khớp đặc trưng đa thức và nguy cơ overfitting khi tăng độ phức tạp. | [Linear Regression, tr. 28](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) · [Regularization, tr. 4–6](https://drive.google.com/file/d/1s-fp_QfzrXUGIcht4pD4DzJKYPFIuEPH/view) |
| ML09 | Khớp sigmoid, xác suất và biên quyết định. | [Logistic Regression, tr. 6–13](https://drive.google.com/file/d/1NExWp4Vy3LgQFIKbQlbddu-9aHoYvTlp/view) |
| ML10 | Khớp binary cross-entropy và gradient. Tính trực tiếp từ logit là phần triển khai số. | [Logistic Regression, tr. 15–21](https://drive.google.com/file/d/1NExWp4Vy3LgQFIKbQlbddu-9aHoYvTlp/view) |
| ML11 | Khớp Newton đa biến và Hessian. Dừng theo gradient hoặc độ thay đổi tham số phù hợp hơn yêu cầu loss bằng 0. | [Logistic Regression, tr. 24–33](https://drive.google.com/file/d/1NExWp4Vy3LgQFIKbQlbddu-9aHoYvTlp/view) |
| ML12 | Khớp k-NN, khoảng cách và biểu quyết; cần quy tắc xử lý hòa khi chấm. | [Classification, tr. 17–19](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML13 | Khớp vai trò train/validation/test và K-fold; LOOCV là trường hợp leave-p-out với p=1. | [Model Evaluation, tr. 4](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view) · [Classification, tr. 12–15](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML14 | Khớp MAE, MSE và R². RMSE là phần bổ sung trực tiếp từ MSE. | [Model Evaluation, tr. 5–8](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view) |
| ML15 | Khớp confusion matrix, accuracy, precision, recall và F-score. Slide còn có specificity, đã thêm vào Modify. | [Model Evaluation, tr. 9–12](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view) · [Classification, tr. 53](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML16 | Khớp đường ROC và AUC. PRIMM có thêm ca điểm hòa và yêu cầu đủ hai lớp. | [Classification, tr. 54–55](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML17 | Khớp underfitting và overfitting; chọn đặc trưng cần một bài thực hành riêng. | [Regularization, tr. 4–11](https://drive.google.com/file/d/1s-fp_QfzrXUGIcht4pD4DzJKYPFIuEPH/view) · [Classification, tr. 9–15](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML18 | Khớp L2 trong hồi quy tuyến tính. Slide còn có L2 cho logistic bằng GD/Newton; bản mới luyện gradient có L2 ở Make 2. | [Regularization, tr. 13–21](https://drive.google.com/file/d/1s-fp_QfzrXUGIcht4pD4DzJKYPFIuEPH/view) · [Regularization bản 25 trang, tr. 23–25](https://drive.google.com/file/d/1SXs57Xq__HMQMjSpyDWDeRIR4g0WWsAN/view) |
| ML19 | Khớp net input và perceptron. Slide Classification dùng nhãn −1/+1 cho học perceptron; bài mới ghi rõ quy ước 0/1 và thêm một epoch cập nhật. | [Neural Network, tr. 11](https://drive.google.com/file/d/1Ws9rF2oD2eAFzPiL2f4-b1Ji4h8ydk7k/view) · [Classification, tr. 23–29](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) |
| ML20 | Khớp vai trò activation; ReLU tại 0 dùng quy ước gradient nêu trong bài. | [Neural Network, tr. 11–12, 17](https://drive.google.com/file/d/1Ws9rF2oD2eAFzPiL2f4-b1Ji4h8ydk7k/view) |
| ML21 | Khớp tầng ẩn, bias và feed-forward; thêm kiểm shape cho batch. | [Neural Network, tr. 13–17](https://drive.google.com/file/d/1Ws9rF2oD2eAFzPiL2f4-b1Ji4h8ydk7k/view) |
| ML22 | Khớp lan truyền ngược theo quy tắc chuỗi. Bài mới ghi rõ loss BCE và kiểm gradient bằng sai phân. | [Neural Network, tr. 18–23](https://drive.google.com/file/d/1Ws9rF2oD2eAFzPiL2f4-b1Ji4h8ydk7k/view) · [Neural Network và Model Evaluation, tr. 18–24](https://drive.google.com/file/d/1abU5ln7cSDAUk8Mv9It5FzYalqI4rNgk/view) |
| ML23 | Khớp các bước gán cụm/cập nhật tâm K-means. PRIMM kiểm SSE và quy tắc cụm rỗng. | [Clustering, tr. 27–34](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) |
| ML24 | Khớp Rand và Jaccard, có phân biệt internal/external. Bản bổ sung luyện Davies–Bouldin và NMI. | [Clustering, tr. 44–53](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) |
| ML25 | Khớp trừ tâm, covariance, eigenvector và projection. SVD có mục riêng trong Drive. | [Statistics and PCA, tr. 17–20, 22–38](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) |
| ML26 | Khớp split, Gini, entropy và information gain. | [Ensemble Models, tr. 9–11, 14–26](https://drive.google.com/file/d/13RwLiEQo8sAYKu-cjVoyz9986Z4zWAQt/view) |
| ML27 | Khớp bootstrap, cây và lấy mẫu đặc trưng theo node. OOB là bài thực hành mở rộng. | [Ensemble Models, tr. 7–8, 12–15, 27–28](https://drive.google.com/file/d/13RwLiEQo8sAYKu-cjVoyz9986Z4zWAQt/view) |
| ML28 | Bài tích hợp do giáo trình PE xây dựng từ nhiều phần của Drive. Bản mới thực hiện pipeline hồi quy và giao bài chuyển giao phân loại. | [Linear Regression](https://drive.google.com/file/d/1cOMMhA0ho0tqOEgaNVEkm2Uu1awCZtQ9/view) · [Logistic Regression](https://drive.google.com/file/d/1NExWp4Vy3LgQFIKbQlbddu-9aHoYvTlp/view) · [Model Evaluation, tr. 4–12](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view) |

### Kiến thức bổ sung theo slide

| Phần có trong Drive | Bài luyện bổ sung |
|---|---|
| Biểu diễn danh mục, dữ liệu thiếu và rời rạc hóa. [Data Preparation, slide 3–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) | [MLP01](#mlp01) |
| Chọn đặc trưng bằng filter, wrapper, embedded. [Feature Selection, slide 13–31](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) | [MLP02](#mlp02) |
| Phân cụm tích tụ và linkage. [Clustering, tr. 12–22](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP03](#mlp03) |
| DBSCAN và core/border/noise. [Clustering, tr. 23–26](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP04](#mlp04) |
| SVM, margin, soft margin và kernel. [Classification, tr. 30–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) | [MLP05](#mlp05) |
| SVD và dựng lại ma trận. [Statistics and PCA, tr. 36–38](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) | [MLP06](#mlp06) |
| Self-Organizing Map. [Clustering, tr. 35–43](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP07](#mlp07) |
| Davies–Bouldin và NMI. [Clustering, tr. 44–52](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP08](#mlp08) |

### Các điểm cần giữ rõ khi dạy

- **Quy ước và cách diễn giải.** Hiệp phương sai bằng 0 chưa đủ kết luận hai biến độc lập. Dùng đúng mẫu số cho phương sai mẫu/tổng thể, ghi hệ số 1/2 trong loss ML04 và quy ước λ trong Ridge. Với R², dự đoán tệ hơn mốc dự đoán bằng mean có thể cho R² âm. [Statistics and PCA, tr. 9–16](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) · [Model Evaluation, tr. 8](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view)
- **Lựa chọn mô hình và độ tổng quát.** Chọn siêu tham số và tập đặc trưng bằng validation hoặc CV. Slide wrapper gọi tập chấm trong vòng chọn là “test”; vai trò của nó là validation. Tập test cuối cần độc lập. Random Forest vẫn có thể overfit, đặc biệt khi dữ liệu hoặc quy trình đánh giá có vấn đề. [Feature Selection, slide 22–24](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) · [Ensemble Models, tr. 28](https://drive.google.com/file/d/13RwLiEQo8sAYKu-cjVoyz9986Z4zWAQt/view)
- **Phạm vi bổ sung.** Hai slide nhập môn có tổng quan ngành, phân biệt học có/không/bán giám sát và quy trình khai phá dữ liệu. Trong Drive còn có biến đổi dữ liệu ảnh/văn bản, ví dụ kernel dual đầy đủ và chi tiết thuật toán SOM. Gói thực hành mới tập trung vào phép tính lõi và các điểm thiếu lớn được nêu ở bảng trên. [Introduction, tr. 10–22](https://drive.google.com/file/d/1BK1s7InGNzpFWBHOx-2snV_U8-skGBl4/view) · [Data Mining Introduction, slide 16–26](https://docs.google.com/presentation/d/1J0TSOBcRdXKbvNK3AY45H-mYmDUv43eD/edit) · [Data Preparation, slide 10–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) · [Classification, tr. 40–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view)

### Bằng chứng kiểm tra

- Kiểm cấu trúc nguồn của commit đạt đủ 28 mã, 6 module, 603 câu và 168 test gốc. Chạy lại 181 đoạn lời giải có mã của ngân hàng câu hỏi và 168 ca S4 bằng CPython. Tất cả khớp kết quả gốc, kể cả các ca S4 chỉ thử hành vi kiểm đầu vào. Bảng đối chiếu rà khái niệm và các vấn đề thực hành chính. Từng đáp án lý thuyết trong 603 câu chưa được thẩm định riêng.
- Bản PRIMM có 36 bài. Chạy 36 mã mẫu và 151 ca Make 1 trên lời giải tham khảo. Kiểm thêm một số ca Modify và Make 2, gồm pipeline phân loại ML28 và so sánh kernel SVM. 603 câu ôn giữ mã và đáp án lựa chọn. Các câu có ngữ cảnh lĩnh vực được biên tập sang dữ liệu vô danh. Make 2 dùng ca kiểm ghi trong đề để người học tự đối chiếu.
- Hai tệp `4.ModelEvaluation.pdf` và `4. ModelEvaluation.pdf` có cùng SHA-256. Hai bản Regularization và hai bản Neural Network có số trang khác nhau; đã dùng các phần tương ứng theo số trang mỗi tệp.
