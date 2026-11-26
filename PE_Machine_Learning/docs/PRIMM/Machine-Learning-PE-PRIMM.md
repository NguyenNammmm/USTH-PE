# Machine Learning PE · Thực hành PRIMM

36 phiếu · 28 bài chính và 8 bài bổ sung · 603 câu ôn tập

## Trước khi bắt đầu

Khóa này phù hợp với người đã học một học phần lập trình nhập môn, thường vào cuối năm nhất hoặc năm hai các ngành máy tính, dữ liệu và kỹ thuật. Đây là ước tính từ các thao tác trong bài. Để vào ML01, bạn nên tự viết được một hàm Python nhỏ, dùng danh sách, vòng lặp, điều kiện và đọc một thông báo lỗi. Với NumPy, hãy biết tạo mảng và lấy một hàng hay cột. Bạn sẽ học các thuật toán học máy (machine learning) qua từng phiếu.

Trước ML05, hãy ôn đạo hàm của hàm bậc hai. Trước ML10–ML11 và ML22, cần đọc được phép nhân ma trận, đạo hàm sigmoid và quy tắc chuỗi. Trước ML25, ôn vectơ riêng và trị riêng. Các kỹ năng này có thể học dần theo lộ trình.

### Tự kiểm đầu vào

1. Viết hàm Python tính trung bình một danh sách số khác rỗng. Thử với [2,4,6].

2. Với X = np.array([[1,4],[3,8],[5,2]]), ghi X.shape và X[:,1].tolist().

3. Tính tích vô hướng của [2,−1] và [3,4], rồi cộng 1.

4. Tại w = 2, đạo hàm của (w − 1)²/2 bằng bao nhiêu?

Nếu tự làm được ba câu đầu, hãy bắt đầu ML01. Nếu còn vướng Python hoặc mảng, ôn lại kỹ năng tương ứng. Câu 4 giúp bạn chuẩn bị cho ML05.

## Cách học

Ghi dự đoán ở A, chạy và sửa mã ở B, giải thích một phép tính ở C. Ba lượt D dùng lại cùng phương pháp. Đóng mẫu trước bốn đề E và nộp riêng từng kết quả. Bạn cũng tự viết một hàm để chạy các ca kiểm. Mở F khi đạt ít nhất 3/4 vị trí E, trong đó E2 bắt buộc đúng. Nếu đã xem đáp án, dùng bộ R cùng số để chứng minh lại. Đầu buổi sau, làm S từ đầu và ghi kết quả riêng.

Khi nhập kết quả, dùng dấu chấm thập phân, ngoặc vuông cho vectơ, ma trận và các kết quả ghép. Dùng dấu ngoặc kép cho chuỗi và null cho giá trị không xác định. Với số thập phân dài, giữ ít nhất 7 chữ số sau dấu chấm. Riêng ML05, giữ đến 10 chữ số nếu cần.

### Thuật ngữ dùng trong phiếu

- **Mẫu (sample)** · Một hàng dữ liệu.

- **Đặc trưng (feature)** · Một đại lượng dùng để mô tả mỗi mẫu.

- **Kích thước (shape)** · Dãy độ dài các trục của mảng.

- **Trục (axis)** · Chiều được chọn khi lấy tổng hoặc trung bình.

- **Tập huấn luyện, xác thực, kiểm tra (train, validation, test)** · Dùng lần lượt để học tham số, chọn cấu hình và đánh giá cuối.

- **Hệ số tự do (bias, intercept)** · Số hạng được cộng vào điểm có trọng số.

- **Gradient** · Vectơ đạo hàm riêng của một đại lượng vô hướng.

- **Lô (batch)** · Nhóm mẫu dùng trong một phép tính hay một lần cập nhật.

- **Ngưỡng (threshold)** · Mốc dùng để đưa ra quyết định.

- **Tổn thất (loss)** · Đại lượng lượng hóa sai khác giữa dự đoán và mục tiêu.

- **Tham số (parameter)** · Đại lượng của mô hình có thể được ước lượng từ dữ liệu.

- **Siêu tham số (hyperparameter)** · Cấu hình như tốc độ học, số láng giềng hoặc mức phạt.

## Mục lục

- [ML01 · Chấm điểm từng hàng](#ml01) · [Câu ôn](#on-ml01)

- [ML02 · Hiệp phương sai mẫu](#ml02) · [Câu ôn](#on-ml02)

- [ML03 · Chuẩn hóa từ tập huấn luyện](#ml03) · [Câu ôn](#on-ml03)

- [ML04 · Tính tổn thất của một đường thẳng](#ml04) · [Câu ôn](#on-ml04)

- [ML05 · Cập nhật trọng số trong một bước](#ml05) · [Câu ôn](#on-ml05)

- [ML06 · Chia một dãy chỉ số thành các lô](#ml06) · [Câu ôn](#on-ml06)

- [ML07 · Khớp đường hồi quy có hệ số tự do](#ml07) · [Câu ôn](#on-ml07)

- [ML08 · Tạo ma trận đặc trưng đa thức](#ml08) · [Câu ôn](#on-ml08)

- [ML09 · Từ điểm logit đến nhãn nhị phân](#ml09) · [Câu ôn](#on-ml09)

- [ML10 · Tổn thất và gradient của hồi quy logistic](#ml10) · [Câu ôn](#on-ml10)

- [ML11 · Một bước Newton cho hồi quy logistic](#ml11) · [Câu ôn](#on-ml11)

- [ML12 · Bỏ phiếu bằng các láng giềng gần nhất](#ml12) · [Câu ôn](#on-ml12)

- [ML13 · Chia tập theo K phần](#ml13) · [Câu ôn](#on-ml13)

- [ML14 · Đo sai số hồi quy](#ml14) · [Câu ôn](#on-ml14)

- [ML15 · Đo chất lượng phân loại nhị phân](#ml15) · [Câu ôn](#on-ml15)

- [ML16 · Dựng các điểm trên đường ROC](#ml16) · [Câu ôn](#on-ml16)

- [ML17 · Chọn bậc mô hình bằng sai số xác thực](#ml17) · [Câu ôn](#on-ml17)

- [ML18 · Khớp hồi quy có phạt L2](#ml18) · [Câu ôn](#on-ml18)

- [ML19 · Gán nhãn bằng perceptron](#ml19) · [Câu ôn](#on-ml19)

- [ML20 · Tính ReLU và đạo hàm](#ml20) · [Câu ôn](#on-ml20)

- [ML21 · Lan truyền tiến qua hai tầng](#ml21) · [Câu ôn](#on-ml21)

- [ML22 · Lan truyền ngược trên cả lô](#ml22) · [Câu ôn](#on-ml22)

- [ML23 · Một vòng phân cụm Lloyd](#ml23) · [Câu ôn](#on-ml23)

- [ML24 · So sánh hai phân hoạch theo cặp](#ml24) · [Câu ôn](#on-ml24)

- [ML25 · Khớp các trục chính của PCA](#ml25) · [Câu ôn](#on-ml25)

- [ML26 · Tìm điểm chia Gini tốt nhất](#ml26) · [Câu ôn](#on-ml26)

- [ML27 · Gộp phiếu từ các cây chưa thấy mẫu](#ml27) · [Câu ôn](#on-ml27)

- [ML28 · Chuẩn hóa, dự đoán và đo MAE](#ml28) · [Câu ôn](#on-ml28)

- [MLP01 · Mã hóa một thuộc tính phân loại](#mlp01)

- [MLP02 · Lọc cột theo phương sai](#mlp02)

- [MLP03 · Gộp cụm theo khoảng cách gần nhất](#mlp03)

- [MLP04 · Gán nhãn cụm mật độ trong một chiều](#mlp04)

- [MLP05 · Tính tổn thất bản lề và mục tiêu SVM](#mlp05)

- [MLP06 · Dựng lại dữ liệu bằng SVD](#mlp06)

- [MLP07 · Cập nhật một bước của bản đồ tự tổ chức](#mlp07)

- [MLP08 · Đo độ tách cụm bằng Davies–Bouldin](#mlp08)

[Đề kiểm lại ở buổi sau](#kiem-lai) · [Đối chiếu bài và tài liệu USTH](#doi-chieu)

Ghi câu trả lời trước khi mở [đáp án phiếu](#dap-an-phieu) hoặc [đáp án ngân hàng](#loi-giai-ngan-hang).

<a id="ml01"></a>

## ML01 · Chấm điểm từng hàng

Mỗi hàng của X là một mẫu, mỗi cột là một đặc trưng (feature). Nhân từng hàng với vectơ trọng số w bằng tích vô hướng (dot product), rồi cộng hệ số tự do (bias) b. Nộp một vectơ điểm theo thứ tự hàng.

Tiên quyết · Tự kiểm đầu vào

### A · Dự đoán

1. Ghi số điểm mà chương trình sẽ trả. Ở hàng đầu, hệ số nào nhân với 7?
2. Ghi ba điểm theo thứ tự ba hàng. Bạn dự đoán hàng nào sẽ có điểm nhỏ nhất?

### B · Chạy mẫu

```python
import numpy as np

def score_rows(X, w, b):
    X, w = (np.asarray(X), np.asarray(w))
    return X @ w + b

X = [[2, 7], [4, 9], [6, 3]]
w = [2, -1]
b = 1
print(score_rows(X, w, b))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml01)

### C · Lần theo mã

1. Vì sao chỉ cộng b sau khi đã cộng các tích của một hàng?
2. Thử cộng 1 vào b. Dựa vào phép tính của một hàng để giải thích vì sao tất cả điểm cùng tăng 1.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay b rồi giải lại đề lõi.  
**D1** · `X = [[2,7],[4,9],[6,3]]  w = [2,-1]  b = -2`

Thay w rồi giải lại đề lõi.  
**D2** · `X = [[2,7],[4,9],[6,3]]  w = [1,3]  b = 1`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[0,2],[-1,4]]  w = [2,-1]  b = 1`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[1,0],[2,-1]]  w = [3,2]  b = -1`  
Kết quả tự nộp ____________________

**E2** · `X = [[2,-1],[-1,3]]  w = [2,-2]  b = 4`  
Kết quả tự nộp ____________________

**E3** · `X = [[0],[3],[-2]]  w = [-2]  b = 3`  
Kết quả tự nộp ____________________

**E4** · `X = [[1,1],[1,-1]]  w = [0,2]  b = 0`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `score_rows(X, w, b)`. Nhận ma trận số 2D có ít nhất một hàng và một cột, vectơ w có đúng d phần tử và hệ số tự do b dạng số. Trả về mảng 1D của Xw + b. Báo ValueError nếu kích thước không hợp lệ. [Tệp điền mã](../../thuc-hanh/ML01.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[2,1],[3,0]]  w = [4,1]  b = -3`  
Kết quả tự nộp ____________________

**R2** · `X = [[1,-2],[3,1]]  w = [2,1]  b = -4`  
Kết quả tự nộp ____________________

**R3** · `X = [[4],[0],[-1]]  w = [3]  b = 2`  
Kết quả tự nộp ____________________

**R4** · `X = [[0,2],[-2,1]]  w = [1,0]  b = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Sửa hàm để trả cả điểm và chỉ số hàng có điểm cao nhất. Khi hòa, chọn hàng đầu. Với X = [[1,0],[0,1],[1,1]], w = [1,1], b = 0, nộp hai kết quả rồi tạo thêm một ca hòa.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML01](#kiem-lai-ml01)

Ôn cùng thao tác · [ML01-practice-2](#ml01-practice-2) · [ML01-practice-5](#ml01-practice-5)


<a id="ml02"></a>

## ML02 · Hiệp phương sai mẫu

Từ bảng X có ít nhất hai hàng, tính ma trận hiệp phương sai mẫu (sample covariance). Trừ đi trung bình của từng cột ngay trong cột đó. Với n hàng, chia tổng tích độ lệch cho n − 1. Nộp ma trận vuông theo thứ tự cột của X.

Tiên quyết · ML01

### A · Dự đoán

1. Đầu ra có mấy hàng? Hai ô đối xứng ngoài đường chéo có quan hệ gì?
2. Trước khi chạy, ghi ma trận hiệp phương sai gồm bốn ô. Bạn dự đoán ô ngoài đường chéo mang dấu gì?

### B · Chạy mẫu

```python
import numpy as np

def sample_cov(X):
    X = np.asarray(X, dtype=float)
    centered = X - X.mean(axis=0)
    return centered.T @ centered / (len(X) - 1)

X = [[1, 2], [3, 0], [5, 4]]
print(sample_cov(X))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml02)

### C · Lần theo mã

1. Hãy chọn một ô ngoài đường chéo và viết các tích độ lệch tạo ra ô đó.
2. Từ cột thứ nhất [1,3,5], tính riêng phương sai rồi kiểm tra nó nằm ở đâu trong ma trận kết quả.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay X rồi giải lại đề lõi.  
**D1** · `X = [[1,3],[2,1],[3,-1]]`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [[0,1],[2,5]]`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[1],[4],[7]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[0,1],[2,3],[4,5]]`  
Kết quả tự nộp ____________________

**E2** · `X = [[2,4],[4,0]]`  
Kết quả tự nộp ____________________

**E3** · `X = [[3,0],[3,2],[3,4]]`  
Kết quả tự nộp ____________________

**E4** · `X = [[-3],[0],[3]]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `sample_cov(X)`. Nhận ma trận số với n ≥ 2 và d ≥ 1. Tính hiệp phương sai mẫu, trả ma trận (d, d). Báo ValueError khi đầu vào sai kích thước. [Tệp điền mã](../../thuc-hanh/ML02.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[1,0],[2,3],[3,6]]`  
Kết quả tự nộp ____________________

**R2** · `X = [[-2,5],[2,1]]`  
Kết quả tự nộp ____________________

**R3** · `X = [[7,0],[7,5],[7,10]]`  
Kết quả tự nộp ____________________

**R4** · `X = [[0],[2],[5]]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một bộ dữ liệu được coi là toàn bộ tổng thể. Sửa đúng một mẫu số rồi tính lại hiệp phương sai của [[1,2],[3,0]]. So với kết quả mẫu ở cùng dữ liệu.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML02](#kiem-lai-ml02)

Ôn cùng thao tác · [ML02-practice-4](#ml02-practice-4) · [ML02-practice-5](#ml02-practice-5)


<a id="ml03"></a>

## ML03 · Chuẩn hóa từ tập huấn luyện

Với phép chuẩn hóa cực tiểu–cực đại (min–max scaling), tìm min và max của mỗi cột trên tập huấn luyện (training set) rồi áp dụng cho X. Nộp ma trận có cùng kích thước với X. Giá trị ngoài khoảng huấn luyện có thể nhỏ hơn 0 hoặc lớn hơn 1.

Tiên quyết · ML01, ML02

### A · Dự đoán

1. Ô nào của X nằm ngoài khoảng đã thấy ở cột tương ứng của train?
2. Ghi hai hàng kết quả. Đánh dấu phần tử mà bạn dự đoán sẽ lớn hơn 1.

### B · Chạy mẫu

```python
import numpy as np

def scale_from_train(train, X):
    train, X = (np.asarray(train, dtype=float), np.asarray(X, dtype=float))
    low = train.min(axis=0)
    span = train.max(axis=0) - low
    return (X - low) / span

train = [[0, 2], [4, 6]]
X = [[2, 3], [4, 8]]
print(scale_from_train(train, X))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml03)

### C · Lần theo mã

1. Nếu thêm một hàng vào X, min và max dùng để biến đổi các hàng cũ có đổi không? Giải thích.
2. Hãy tính ô ở hàng đầu, cột thứ hai bằng min và max của đúng cột ấy trong train.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay X rồi giải lại đề lõi.  
**D1** · `train = [[0,2],[4,6]]  X = [[1,5],[3,9]]`

Thay train rồi giải lại đề lõi.  
**D2** · `train = [[-2,0],[2,8]]  X = [[2,3],[4,8]]`

Thay X rồi giải lại đề lõi.  
**D3** · `train = [[0,2],[4,6]]  X = [[-2,10]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `train = [[0],[8]]  X = [[2],[6]]`  
Kết quả tự nộp ____________________

**E2** · `train = [[2,0],[6,4]]  X = [[0,8],[4,-2]]`  
Kết quả tự nộp ____________________

**E3** · `train = [[-2,10],[2,18]]  X = [[0,14],[1,12]]`  
Kết quả tự nộp ____________________

**E4** · `train = [[1,2],[5,8]]  X = [[5,2]]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `scale_from_train(train, X)`. Trả về Min–Max của X theo từng cột từ train. Hai ma trận 2D có cùng số cột dương, train có ít nhất một hàng, X có thể có 0 hàng. Báo ValueError cho cột train hằng hoặc kích thước sai. [Tệp điền mã](../../thuc-hanh/ML03.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `train = [[3],[9]]  X = [[5],[6]]`  
Kết quả tự nộp ____________________

**R2** · `train = [[0,-2],[8,2]]  X = [[-4,6],[2,-3]]`  
Kết quả tự nộp ____________________

**R3** · `train = [[-4,6],[0,10]]  X = [[-3,9]]`  
Kết quả tự nộp ____________________

**R4** · `train = [[2,3],[6,9]]  X = [[2,9]]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một chương trình lấy min và max riêng từ lô kiểm tra [10,20]. Huấn luyện dùng [0,10]. Hãy cho hai kết quả đang bị nhầm lẫn rồi sửa chương trình.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML03](#kiem-lai-ml03)

Ôn cùng thao tác · [ML03-practice-1](#ml03-practice-1) · [ML03-practice-4](#ml03-practice-4)


<a id="ml04"></a>

## ML04 · Tính tổn thất của một đường thẳng

Từ x, y, w và b, tính phần dư (residual) theo thứ tự dự đoán trừ giá trị thực. Nộp một số J bằng một nửa trung bình bình phương các phần dư. Mỗi mẫu có cùng trọng số.

Tiên quyết · ML01

Giữ bộ x = [0,2], y = [1,5], w = 0, b = 0 cho ML05. Ghi hai phần dư của lượt B để mang sang bài kế.

### A · Dự đoán

1. Hai dự đoán khi w và b cùng bằng 0 là gì? Hãy ghi hai phần dư.
2. Bình phương hai phần dư và dự đoán một giá trị J duy nhất.

### B · Chạy mẫu

```python
import numpy as np

def half_mse(x, y, w, b):
    x, y = (np.asarray(x, dtype=float), np.asarray(y, dtype=float))
    return float(np.mean((w * x + b - y) ** 2) / 2)

x = [0, 2]
y = [1, 5]
w = 0
b = 0
print(half_mse(x, y, w, b))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml04)

### C · Lần theo mã

1. Dòng nào trong mã quyết định chia cho số mẫu? Hệ số 1/2 xuất hiện ở đâu?
2. Nếu cộng hai phần dư trước rồi mới bình phương, bạn thu được đại lượng nào khác với công thức trong mã?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay w rồi giải lại đề lõi.  
**D1** · `x = [0,2]  y = [1,5]  w = 1  b = 0`

Thay b rồi giải lại đề lõi.  
**D2** · `x = [0,2]  y = [1,5]  w = 0  b = 2`

Thay y rồi giải lại đề lõi.  
**D3** · `x = [0,2]  y = [-1,3]  w = 0  b = 0`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [1,3]  y = [1,5]  w = 2  b = -1`  
Kết quả tự nộp ____________________

**E2** · `x = [-1,2]  y = [0,5]  w = 1  b = 1`  
Kết quả tự nộp ____________________

**E3** · `x = [0,2,4]  y = [1,2,5]  w = 1  b = 0`  
Kết quả tự nộp ____________________

**E4** · `x = [-2,1]  y = [-4,2]  w = 2  b = 0`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `half_mse(x, y, w, b)`. Nhận hai vectơ số x và y cùng độ dài dương cùng hai hệ số w, b. Trả J = mean((w*x+b−y)²)/2 dưới dạng số. Báo ValueError nếu kích thước hoặc số phần tử không hợp lệ. [Tệp điền mã](../../thuc-hanh/ML04.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [0,3]  y = [2,7]  w = 2  b = 1`  
Kết quả tự nộp ____________________

**R2** · `x = [-1,3]  y = [0,7]  w = 2  b = 0`  
Kết quả tự nộp ____________________

**R3** · `x = [1,2,4]  y = [2,4,7]  w = 1  b = 1`  
Kết quả tự nộp ____________________

**R4** · `x = [-3,2]  y = [-6,3]  w = 2  b = 0`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Hai mô hình có phần dư [0,2] và [1,1]. So sánh chúng theo J rồi theo sai số tuyệt đối trung bình. Giải thích khác biệt.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML04](#kiem-lai-ml04)

Ôn cùng thao tác · [ML04-practice-3](#ml04-practice-3) · [ML04-practice-4](#ml04-practice-4)


<a id="ml05"></a>

## ML05 · Cập nhật trọng số trong một bước

Dùng hạ gradient trên cả lô (batch gradient descent) để cập nhật đường thẳng w·x + b. Trước hết, tính sai số của từng mẫu từ w và b ban đầu. Giữ nguyên các sai số ấy khi tính hai gradient, rồi mới cập nhật hai tham số bằng tốc độ học lr. Nộp [w_mới, b_mới] sau đúng một bước.

Tiên quyết · ML04

Dùng lại x = [0,2], y = [1,5], w = b = 0 từ ML04. Hãy tìm hai phần dư của bài trước rồi dùng chúng để tính mức thay đổi của w và b.

### A · Dự đoán

1. Hai sai số ban đầu bằng bao nhiêu? Tham số nào sẽ tăng sau bước cập nhật?
2. Hãy tính cả hai gradient rồi ghi cặp [w_mới,b_mới] mà dòng cuối sẽ in.

### B · Chạy mẫu

```python
import numpy as np

def gd_step(x, y, w, b, lr):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    residual = w * x + b - y
    grad_w = np.mean(residual * x)
    grad_b = np.mean(residual)
    w_new = w - lr * grad_w
    b_new = b - lr * grad_b
    return float(w_new), float(b_new)

x = [0, 2]
y = [1, 5]
w = 0
b = 0
lr = 0.1
print(gd_step(x, y, w, b, lr))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml05)

### C · Lần theo mã

1. Nếu cập nhật w trước rồi tính lại sai số cho b, phép tính nào sẽ thay đổi?
2. Phần dư của mẫu x = 0 ảnh hưởng thế nào đến gradient theo w và gradient theo b?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Đổi tốc độ học từ 0,1 lên 0,2. Hai gradient có đổi không?  
**D1** · `x = [0,2]  y = [1,5]  w = 0  b = 0  lr = 0.2`

Bắt đầu với w = 1 và b = 0,5. Tính lại cả hai gradient từ bộ tham số này.  
**D2** · `x = [0,2]  y = [1,5]  w = 1  b = 0.5  lr = 0.1`

Thay hai giá trị đích bằng −1 và 3. Giữ tốc độ học cùng bộ tham số ban đầu.  
**D3** · `x = [0,2]  y = [-1,3]  w = 0  b = 0  lr = 0.1`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁹.

**E1** · `x = [1,3]  y = [3,7]  w = 0  b = 0  lr = 0.1`  
Kết quả tự nộp ____________________

**E2** · `x = [-1,2]  y = [0,5]  w = 1  b = 1  lr = 0.2`  
Kết quả tự nộp ____________________

**E3** · `x = [-2,1]  y = [-5,1]  w = 2  b = -1  lr = 0.3`  
Kết quả tự nộp ____________________

**E4** · `x = [-2,2]  y = [1,-1]  w = 0  b = 0  lr = 0.2`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `gd_step(x, y, w, b, lr)`. Nhận hai vectơ số cùng độ dài dương. Với lr hữu hạn không âm, trả tuple (w_mới, b_mới). Báo ValueError nếu kích thước sai hoặc lr ngoài miền. [Tệp điền mã](../../thuc-hanh/ML05.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [0,3]  y = [2,8]  w = 0  b = 0  lr = 0.2`  
Kết quả tự nộp ____________________

**R2** · `x = [1,3]  y = [0,5]  w = 1  b = 0  lr = 0.25`  
Kết quả tự nộp ____________________

**R3** · `x = [-1,2]  y = [-1,5]  w = 2  b = 1  lr = 0.3`  
Kết quả tự nộp ____________________

**R4** · `x = [-3,3]  y = [2,-2]  w = 0  b = 0  lr = 0.1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một chương trình cập nhật w, tính lại phần dư bằng w mới rồi mới cập nhật b. Tái hiện lỗi với x = [−1,2], y = [0,5], w = b = 1, lr = 0,2. Nộp cặp sai, cặp đúng và dòng mã cần dời.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML05](#kiem-lai-ml05)

Ôn cùng thao tác · [ML05-practice-4](#ml05-practice-4) · [ML05-practice-7](#ml05-practice-7)


<a id="ml06"></a>

## ML06 · Chia một dãy chỉ số thành các lô

Chia hoán vị order thành các lô nhỏ (mini-batch) liên tiếp, mỗi lô tối đa size phần tử. Nộp danh sách các lô theo thứ tự đã cho, kể cả lô cuối ngắn hơn size.

Tiên quyết · ML05

### A · Dự đoán

1. Lô thứ hai bắt đầu bằng chỉ số nào? Lô cuối dài bằng bao nhiêu?
2. Viết từng lô có ngoặc riêng, kể cả lô cuối nếu nó chỉ còn một phần tử.

### B · Chạy mẫu

```python
import numpy as np

def split_batches(order, size):
    return [order[start:start + size] for start in range(0, len(order), size)]

order = [3, 0, 4, 1, 2]
size = 2
print(split_batches(order, size))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml06)

### C · Lần theo mã

1. Giải thích vì sao việc sắp lại order trước khi cắt có thể thay đổi mọi lô.
2. Ghép các lô trở lại. Vì sao kết quả phải khớp từng phần tử với order ban đầu?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Đổi kích thước lô từ 2 lên 3 rồi cắt lại cùng hoán vị.  
**D1** · `order = [3,0,4,1,2]  size = 3`

Thay order rồi giải lại đề lõi.  
**D2** · `order = [4,2,0,3,1]  size = 2`

Thay size rồi giải lại đề lõi.  
**D3** · `order = [3,0,4,1,2]  size = 1`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `order = [2,0,1,3]  size = 2`  
Kết quả tự nộp ____________________

**E2** · `order = [3,1,4,0,2]  size = 3`  
Kết quả tự nộp ____________________

**E3** · `order = [4,0,2,1,3]  size = 2`  
Kết quả tự nộp ____________________

**E4** · `order = [1,0]  size = 3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `split_batches(order, size)`. Nhận một list hoán vị các chỉ số 0..n−1 và size là số nguyên dương. Trả list các list liên tiếp, giữ batch cuối. Cho phép order rỗng. Báo ValueError nếu size không dương hoặc order có chỉ số thiếu/trùng. [Tệp điền mã](../../thuc-hanh/ML06.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `order = [1,3,0,2]  size = 2`  
Kết quả tự nộp ____________________

**R2** · `order = [0,3,1,4,2]  size = 2`  
Kết quả tự nộp ____________________

**R3** · `order = [3,2,0,1]  size = 3`  
Kết quả tự nộp ____________________

**R4** · `order = [2,0,1]  size = 5`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Cho order = [1,0,2], size = 2 và gradient theo chỉ số g = [2,8,5]. Sửa hàm để trả thêm gradient trung bình của mỗi lô.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML06](#kiem-lai-ml06)

Ôn cùng thao tác · [ML06-practice-5](#ml06-practice-5) · [ML06-practice-1](#ml06-practice-1)


<a id="ml07"></a>

## ML07 · Khớp đường hồi quy có hệ số tự do

Khớp bình phương tối thiểu (least squares) từ X và y. Thêm cột toàn 1 ở bên trái và gọi cùng bộ giải lstsq cho mọi lượt. Nộp vectơ hệ số với hệ số tự do đứng đầu. Khi có nhiều nghiệm, lấy nghiệm có chuẩn Euclid nhỏ nhất.

Tiên quyết · ML04, ML05

### A · Dự đoán

1. Hàng toàn 0 của X cho biết hệ số nào? Mỗi hàng còn lại giúp tìm hệ số nào?
2. Từ ba hàng của X, suy ra hệ số tự do và hai trọng số. Ghi chúng theo thứ tự hàm trả về.

### B · Chạy mẫu

```python
import numpy as np

def fit_linear(X, y):
    X, y = (np.asarray(X, dtype=float), np.asarray(y, dtype=float))
    A = np.column_stack([np.ones(len(X)), X])
    return np.linalg.lstsq(A, y, rcond=None)[0]

X = [[0, 0], [1, 0], [0, 1]]
y = [2, 5, 1]
print(fit_linear(X, y))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml07)

### C · Lần theo mã

1. Nếu hai cột giống nhau, điều gì xảy ra khi chuyển một phần trọng số từ cột này sang cột kia?
2. Kiểm tra nghiệm bằng cách thay vào hàng [0,1]. Giá trị y ở hàng ấy xác nhận hệ số nào?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay y rồi giải lại đề lõi.  
**D1** · `X = [[0,0],[1,0],[0,1]]  y = [1,3,4]`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [[0,0],[2,0],[0,1]]  y = [2,5,1]`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[1,0],[1,1],[0,1]]  y = [2,5,1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[0],[1],[2]]  y = [3,5,7]`  
Kết quả tự nộp ____________________

**E2** · `X = [[0,0],[1,1],[2,2]]  y = [2,6,10]`  
Kết quả tự nộp ____________________

**E3** · `X = [[0,0],[1,0],[0,2]]  y = [1,0,7]`  
Kết quả tự nộp ____________________

**E4** · `X = [[-1],[0],[1]]  y = [1,3,2]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `fit_linear(X, y)`. Nhận X 2D hữu hạn với n,d ≥ 1 và y 1D cùng số hàng. Trả vectơ hệ số gồm hệ số tự do đứng đầu, dùng nghiệm chuẩn Euclid nhỏ nhất trong các nghiệm khớp bình phương tối thiểu. Báo ValueError nếu kích thước sai. [Tệp điền mã](../../thuc-hanh/ML07.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[0],[2],[4]]  y = [-1,5,11]`  
Kết quả tự nộp ____________________

**R2** · `X = [[0,0],[2,2],[3,3]]  y = [1,5,7]`  
Kết quả tự nộp ____________________

**R3** · `X = [[0,0],[2,0],[0,1]]  y = [3,1,5]`  
Kết quả tự nộp ____________________

**R4** · `X = [[-2],[0],[2]]  y = [0,1,5]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Hai cột của X = [[0,0],[1,1],[2,2]] giống nhau, y = [1,3,5]. Giải thích vì sao lấy nghịch đảo của A.T @ A thất bại nhưng lstsq vẫn dự đoán được. Cho hai bộ hệ số cùng khớp và chỉ ra nghiệm có chuẩn nhỏ nhất.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML07](#kiem-lai-ml07)

Ôn cùng thao tác · [ML07-practice-4](#ml07-practice-4) · [ML07-practice-12](#ml07-practice-12)


<a id="ml08"></a>

## ML08 · Tạo ma trận đặc trưng đa thức

Với mỗi giá trị x, tạo một hàng gồm các lũy thừa từ bậc 0 đến degree. Nộp ma trận đặc trưng đa thức (polynomial features), cột đầu là 1 và cột cuối là x mũ degree.

Tiên quyết · ML07

### A · Dự đoán

1. Nếu degree bằng 2, một hàng có mấy cột? Ghi hàng ứng với x = −2.
2. Lập ba hàng ứng với −2, 0 và 2. Ghi rõ kích thước kết quả.

### B · Chạy mẫu

```python
import numpy as np

def poly_features(x, degree):
    x = np.asarray(x, dtype=float)
    return np.vander(x, degree + 1, increasing=True)

x = [-2, 0, 2]
degree = 2
print(poly_features(x, degree))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml08)

### C · Lần theo mã

1. Tại sao cột bậc 0 của hàng ứng với x = 0 vẫn bằng 1 trong ma trận thiết kế?
2. So sánh hai hàng ứng với −2 và 2. Vì sao có hai cột trùng giá trị và một cột khác dấu?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay degree rồi giải lại đề lõi.  
**D1** · `x = [-2,0,2]  degree = 3`

Thay x rồi giải lại đề lõi.  
**D2** · `x = [-1,1,3]  degree = 2`

Thay degree rồi giải lại đề lõi.  
**D3** · `x = [-2,0,2]  degree = 0`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [-1,2]  degree = 3`  
Kết quả tự nộp ____________________

**E2** · `x = [0,-2,3]  degree = 2`  
Kết quả tự nộp ____________________

**E3** · `x = [2,4]  degree = 0`  
Kết quả tự nộp ____________________

**E4** · `x = [-3,1]  degree = 1`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `poly_features(x, degree)`. Nhận vectơ 1D và degree là số nguyên không âm. Trả ma trận với cột x⁰ đến xᵈ, cho phép x rỗng. Báo ValueError nếu x sai chiều hoặc degree âm. [Tệp điền mã](../../thuc-hanh/ML08.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [1,-3]  degree = 3`  
Kết quả tự nộp ____________________

**R2** · `x = [-1,0,4]  degree = 2`  
Kết quả tự nộp ____________________

**R3** · `x = [-3,7,1]  degree = 0`  
Kết quả tự nộp ____________________

**R4** · `x = [2,0,-1]  degree = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Dùng cơ sở [1,x,x²] để dự đoán với hệ số [1,2,−1]. Ghi hai dự đoán cho x = [−1,2] rồi cho biết điều gì xảy ra nếu đảo thứ tự các cột mà giữ nguyên hệ số.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML08](#kiem-lai-ml08)

Ôn cùng thao tác · [ML08-practice-1](#ml08-practice-1) · [ML08-practice-3](#ml08-practice-3)


<a id="ml09"></a>

## ML09 · Từ điểm logit đến nhãn nhị phân

Nhận điểm logit, đổi từng điểm thành xác suất qua hàm sigmoid, rồi so với ngưỡng (threshold). Gán nhãn 1 nếu xác suất bằng hoặc vượt ngưỡng. Nộp vectơ nhãn 0/1 theo thứ tự đầu vào.

Tiên quyết · ML04

Ở ví dụ chung với ML10 và ML11, A = [[1,−1],[1,0],[1,2]] và w = [0,1]. Tích A @ w chính là ba logit của lượt B. Dùng y = [0,1,1] ở bài kế.

### A · Dự đoán

1. Logit 0 cho xác suất nào? Khi ngưỡng là 0,5, nhãn của nó bằng bao nhiêu?
2. Dự đoán các nhãn cho ba logit. Đánh dấu nhãn nào phụ thuộc vào quy tắc bằng ngưỡng.

### B · Chạy mẫu

```python
import numpy as np

def logistic_labels(logits, threshold):
    logits = np.asarray(logits, dtype=float)
    p = np.exp(-np.logaddexp(0, -logits))
    return (p >= threshold).astype(int)

logits = [-1, 0, 2]
threshold = 0.5
print(logistic_labels(logits, threshold))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml09)

### C · Lần theo mã

1. Dòng xử lý trường hợp bằng ngưỡng dùng phép so sánh nào? Vì sao phải so trên thang xác suất?
2. Nếu ngưỡng nâng lên 0,75, mẫu có logit 0 đổi nhãn thế nào? Dùng chính xác suất đã tính.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay threshold rồi giải lại đề lõi.  
**D1** · `logits = [-1,0,2]  threshold = 0.75`

Thay logits rồi giải lại đề lõi.  
**D2** · `logits = [-3,0,1]  threshold = 0.5`

Thay threshold rồi giải lại đề lõi.  
**D3** · `logits = [-1,0,2]  threshold = 0.25`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `logits = [-2,1,3]  threshold = 0.7`  
Kết quả tự nộp ____________________

**E2** · `logits = [-3,0,2,0]  threshold = 0.5`  
Kết quả tự nộp ____________________

**E3** · `logits = [2,-2,1]  threshold = 0.8`  
Kết quả tự nộp ____________________

**E4** · `logits = [0,2,-1]  threshold = 0.3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `logistic_labels(logits, threshold)`. Nhận vectơ logit 1D hữu hạn, ngưỡng thuộc (0, 1). Tính sigmoid theo cách ổn định rồi trả vectơ 0/1, bằng ngưỡng thì gán 1. Báo ValueError nếu miền sai. [Tệp điền mã](../../thuc-hanh/ML09.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `logits = [-4,1,4]  threshold = 0.8`  
Kết quả tự nộp ____________________

**R2** · `logits = [1,0,-2,0]  threshold = 0.5`  
Kết quả tự nộp ____________________

**R3** · `logits = [-3,1,3]  threshold = 0.85`  
Kết quả tự nộp ____________________

**R4** · `logits = [1,-1,0]  threshold = 0.4`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Đổi từ logit tuyến tính sang z = x² − 1. Dùng ngưỡng 0,5, tìm hai điểm biên và nhãn tại x = [−2,0,1].

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML09](#kiem-lai-ml09)

Ôn cùng thao tác · [ML09-practice-3](#ml09-practice-3) · [ML09-practice-6](#ml09-practice-6)


<a id="ml10"></a>

## ML10 · Tổn thất và gradient của hồi quy logistic

Với ma trận thiết kế A, nhãn y và hệ số w, tính tổn thất entropy chéo nhị phân (binary cross-entropy, BCE) trung bình và gradient theo w. Nộp [giá trị tổn thất, vectơ gradient] theo thứ tự cột của A.

Tiên quyết · ML09

Dùng lại A = [[1,−1],[1,0],[1,2]], w = [0,1] và các xác suất của ML09. Ghép chúng với y = [0,1,1] để tính gradient cho ML11.

### A · Dự đoán

1. Với hàng [1,0], điểm logit và xác suất dự đoán bằng bao nhiêu?
2. Dự đoán dấu của hai thành phần gradient, rồi ghi BCE trung bình và vectơ gradient.

### B · Chạy mẫu

```python
import numpy as np

def bce_and_gradient(A, y, w):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    z = A @ w
    p = np.exp(-np.logaddexp(0, -z))
    loss = np.logaddexp(0, (1 - 2 * y) * z).mean()
    return (float(loss), A.T @ (p - y) / len(y))

A = [[1, -1], [1, 0], [1, 2]]
y = [0, 1, 1]
w = [0, 1]
print(bce_and_gradient(A, y, w))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml10)

### C · Lần theo mã

1. Trong tích A chuyển vị nhân (p − y), một hàng đóng góp gì cho mỗi hệ số? Chia cho số nào?
2. Chọn hàng có nhãn 1 ở logit 0. So đóng góp của nó vào BCE với đóng góp vào gradient.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay y rồi giải lại đề lõi.  
**D1** · `A = [[1,-1],[1,0],[1,2]]  y = [1,0,1]  w = [0,1]`

Thay w rồi giải lại đề lõi.  
**D2** · `A = [[1,-1],[1,0],[1,2]]  y = [0,1,1]  w = [0,0]`

Thay A rồi giải lại đề lõi.  
**D3** · `A = [[1,-2],[1,1],[1,3]]  y = [0,1,1]  w = [0,1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `A = [[1,-2],[1,2]]  y = [0,1]  w = [0,0]`  
Kết quả tự nộp ____________________

**E2** · `A = [[1,0],[1,2],[1,4]]  y = [1,0,0]  w = [0,0]`  
Kết quả tự nộp ____________________

**E3** · `A = [[1,-1],[1,1]]  y = [1,0]  w = [0,1]`  
Kết quả tự nộp ____________________

**E4** · `A = [[1,1],[1,3]]  y = [0,0]  w = [1,0]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `bce_and_gradient(A, y, w)`. A là ma trận thiết kế n×d có n,d dương. y là vectơ nhị phân n phần tử, w là vectơ d phần tử. Trả tuple (loss trung bình, gradient theo w). Báo ValueError nếu kích thước hoặc nhãn sai. [Tệp điền mã](../../thuc-hanh/ML10.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `A = [[1,-3],[1,3]]  y = [1,0]  w = [0,0]`  
Kết quả tự nộp ____________________

**R2** · `A = [[1,1],[1,3],[1,5]]  y = [0,1,1]  w = [0,0]`  
Kết quả tự nộp ____________________

**R3** · `A = [[1,-2],[1,1]]  y = [1,0]  w = [0,-1]`  
Kết quả tự nộp ____________________

**R4** · `A = [[1,0],[1,4]]  y = [1,1]  w = [-1,0]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Kiểm gradient bằng sai phân trung tâm khi A = [[1],[1]], y = [1,0], w = [1]. So đạo hàm xấp xỉ của BCE trung bình với kết quả giải tích, dùng bước h = 10⁻⁵.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML10](#kiem-lai-ml10)

Ôn cùng thao tác · [ML10-practice-3](#ml10-practice-3) · [ML10-practice-5](#ml10-practice-5)


<a id="ml11"></a>

## ML11 · Một bước Newton cho hồi quy logistic

Tính gradient g và ma trận đạo hàm bậc hai (Hessian) H của BCE trung bình tại w. Giải hệ (H + damping·I)s = g rồi nộp vectơ w − s. Trong các lượt luyện, damping bằng 0 và hệ có nghiệm duy nhất.

Tiên quyết · ML10

Ở bộ mẫu, A, y và w giống ML10. Lấy lại gradient ở bài ấy và dựng thêm Hessian tại cùng w.

### A · Dự đoán

1. Mỗi hàng của A tạo một xác suất. H có kích thước nào nếu A có hai cột?
2. Ghi vectơ w sau khi giải hệ ở lượt B. Bạn dự đoán thành phần nào tăng?

### B · Chạy mẫu

```python
import numpy as np

def newton_step(A, y, w, damping=0.0):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    p = np.exp(-np.logaddexp(0, -(A @ w)))
    g = A.T @ (p - y) / len(y)
    H = A.T @ ((p * (1 - p))[:, None] * A) / len(y)
    return w - np.linalg.solve(H + damping * np.eye(len(w)), g)

A = [[1, -1], [1, 0], [1, 2]]
y = [0, 1, 1]
w = [0, 1]
damping = 0
print(newton_step(A, y, w, damping))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml11)

### C · Lần theo mã

1. Vì sao lấy trực tiếp w − g có thể cho kết quả khác w − s?
2. Thay bước hiệu chỉnh vào H·s rồi đối chiếu với g. Phép kiểm tra này phát hiện được lỗi nào khi dùng H @ g?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay y rồi giải lại đề lõi.  
**D1** · `A = [[1,-1],[1,0],[1,2]]  y = [1,0,1]  w = [0,1]  damping = 0`

Thay w rồi giải lại đề lõi.  
**D2** · `A = [[1,-1],[1,0],[1,2]]  y = [0,1,1]  w = [0,0]  damping = 0`

Thay A rồi giải lại đề lõi.  
**D3** · `A = [[1,-2],[1,0],[1,3]]  y = [0,1,1]  w = [0,1]  damping = 0`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `A = [[1,-2],[1,2]]  y = [0,1]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

**E2** · `A = [[1,0],[1,2]]  y = [0,1]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

**E3** · `A = [[1,-1],[1,1]]  y = [1,0]  w = [0,1]  damping = 0`  
Kết quả tự nộp ____________________

**E4** · `A = [[1,0],[1,1],[1,3]]  y = [1,0,1]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `newton_step(A, y, w, damping=0.0)`. Với ma trận thiết kế 2D đủ kích thước, y nhị phân, w đúng số cột và damping hữu hạn ≥ 0, trả vectơ tham số sau một bước theo H+damping·I. Báo ValueError với đầu vào sai. Cho phép LinAlgError nếu hệ suy biến. [Tệp điền mã](../../thuc-hanh/ML11.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `A = [[1,-3],[1,3]]  y = [1,0]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

**R2** · `A = [[1,1],[1,3]]  y = [0,1]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

**R3** · `A = [[1,-1],[1,2]]  y = [1,0]  w = [1,0]  damping = 0`  
Kết quả tự nộp ____________________

**R4** · `A = [[1,-2],[1,1],[1,4]]  y = [0,1,0]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Với A = [[1,1],[1,1]], y = [1,1], w = [0,0], giải thích vì sao H suy biến. Thử lại với damping = 0,5 và ghi tham số mới.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML11](#kiem-lai-ml11)

Ôn cùng thao tác · [ML11-practice-5](#ml11-practice-5) · [ML11-practice-6](#ml11-practice-6)


<a id="ml12"></a>

## ML12 · Bỏ phiếu bằng các láng giềng gần nhất

Phân lớp theo k láng giềng gần nhất (k-nearest neighbors). Xếp các hàng của X theo khoảng cách Euclid đến q. Nếu bằng khoảng cách, giữ hàng xuất hiện trước. Nộp một nhãn 0 hoặc 1 sau khi bỏ phiếu. Hai bên bằng phiếu thì chọn 0.

Tiên quyết · ML01

### A · Dự đoán

1. Ba hàng nào gần q nhất? Hãy ghi chỉ số của chúng trước khi đếm nhãn.
2. Đếm phiếu trong ba hàng vừa chọn rồi ghi nhãn mà hàm sẽ trả.

### B · Chạy mẫu

```python
import numpy as np

def knn_one(X, y, q, k):
    X, q, y = (np.asarray(X, dtype=float), np.asarray(q, dtype=float), np.asarray(y))
    d2 = ((X - q) ** 2).sum(axis=1)
    near = np.argsort(d2, kind='stable')[:k]
    return int(2 * y[near].sum() > k)

X = [[0], [2], [5], [8]]
y = [1, 0, 1, 0]
q = [3]
k = 3
print(knn_one(X, y, q, k))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml12)

### C · Lần theo mã

1. Nếu hai hàng cách q như nhau và chỉ còn một chỗ, dòng nào quyết định hàng được chọn?
2. Lấy k = 1 trên cùng dữ liệu. Khoảng cách vẫn giữ nguyên nhưng bước nào của phép bỏ phiếu thay đổi?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay k rồi giải lại đề lõi.  
**D1** · `X = [[0],[2],[5],[8]]  y = [1,0,1,0]  q = [3]  k = 1`

Thay q rồi giải lại đề lõi.  
**D2** · `X = [[0],[2],[5],[8]]  y = [1,0,1,0]  q = [6]  k = 3`

Thay y rồi giải lại đề lõi.  
**D3** · `X = [[0],[2],[5],[8]]  y = [0,1,0,1]  q = [3]  k = 3`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[0],[3],[8]]  y = [1,0,1]  q = [2]  k = 1`  
Kết quả tự nộp ____________________

**E2** · `X = [[-1],[1],[4]]  y = [1,0,0]  q = [0]  k = 1`  
Kết quả tự nộp ____________________

**E3** · `X = [[1],[4],[6],[9]]  y = [0,1,0,1]  q = [5]  k = 2`  
Kết quả tự nộp ____________________

**E4** · `X = [[0,0],[2,1],[3,3]]  y = [0,1,1]  q = [1,1]  k = 3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `knn_one(X, y, q, k)`. Nhận X ma trận n×d, q vectơ d, y vectơ nhãn nguyên 0/1 và k nguyên trong [1,n]. Dùng Euclid, hòa khoảng cách lấy chỉ số trước, hòa phiếu lấy 0. Báo ValueError nếu kích thước, nhãn hoặc k sai. [Tệp điền mã](../../thuc-hanh/ML12.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[1],[4],[9]]  y = [0,1,0]  q = [3]  k = 1`  
Kết quả tự nộp ____________________

**R2** · `X = [[2],[-2],[6]]  y = [0,1,1]  q = [0]  k = 1`  
Kết quả tự nộp ____________________

**R3** · `X = [[-2],[2],[5],[8]]  y = [0,1,1,0]  q = [3]  k = 2`  
Kết quả tự nộp ____________________

**R4** · `X = [[0,1],[3,1],[3,4]]  y = [0,0,1]  q = [3,2]  k = 3`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Đổi từ Euclid sang Manhattan. Với q = [0,0], hai hàng [3,0] và [2,2] mang nhãn 0 và 1, k = 1, nộp nhãn theo từng phép đo.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML12](#kiem-lai-ml12)

Ôn cùng thao tác · [ML12-practice-4](#ml12-practice-4) · [ML12-practice-6](#ml12-practice-6)


<a id="ml13"></a>

## ML13 · Chia tập theo K phần

Kiểm định chéo K phần (K-fold cross-validation) dùng lần lượt mỗi đoạn của order làm tập xác thực. Nếu chia có dư, các đoạn đầu nhận thêm một hàng. Nộp danh sách các cặp [chỉ số huấn luyện, chỉ số xác thực], cùng thứ tự như order.

Tiên quyết · ML04

### A · Dự đoán

1. Năm mẫu chia ba phần thì mỗi tập xác thực dài bao nhiêu?
2. Liệt kê ba cặp [huấn luyện,xác thực]. Kiểm tra phần nào nhận mẫu dư.

### B · Chạy mẫu

```python
import numpy as np

def kfold_indices(order, k):
    folds = [fold.tolist() for fold in np.array_split(order, k)]
    splits = []
    for i, valid in enumerate(folds):
        train = [index for j, fold in enumerate(folds) if i != j for index in fold]
        splits.append((train, valid))
    return splits

order = [3, 0, 4, 1, 2]
k = 3
print(kfold_indices(order, k))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml13)

### C · Lần theo mã

1. Một hàng xuất hiện trong bao nhiêu tập xác thực sau khi duyệt hết k lượt?
2. Chọn chỉ số 3 và theo nó qua ba lượt. Nó xuất hiện trong tập huấn luyện mấy lần?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay k rồi giải lại đề lõi.  
**D1** · `order = [3,0,4,1,2]  k = 2`

Thay order rồi giải lại đề lõi.  
**D2** · `order = [4,2,0,3,1]  k = 3`

Thay k rồi giải lại đề lõi.  
**D3** · `order = [3,0,4,1,2]  k = 5`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `order = [2,0,1,3]  k = 2`  
Kết quả tự nộp ____________________

**E2** · `order = [3,1,4,0,2]  k = 2`  
Kết quả tự nộp ____________________

**E3** · `order = [4,0,2,1,3]  k = 3`  
Kết quả tự nộp ____________________

**E4** · `order = [1,0,2]  k = 3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `kfold_indices(order, k)`. order là list hoán vị 0..n−1, k nguyên trong [2,n]. Trả list (train, valid), mỗi phần là list chỉ số theo order. Khi n không chia hết, các fold valid đầu có thêm một mẫu. Báo ValueError nếu k hoặc order sai. [Tệp điền mã](../../thuc-hanh/ML13.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `order = [1,3,0,2]  k = 2`  
Kết quả tự nộp ____________________

**R2** · `order = [0,3,1,4,2]  k = 3`  
Kết quả tự nộp ____________________

**R3** · `order = [3,2,0,1]  k = 3`  
Kết quả tự nộp ____________________

**R4** · `order = [2,0,1]  k = 3`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Ba tập xác thực có kích thước 2, 2, 1 và MSE tương ứng 1, 4, 9. Tính MSE trên cả năm mẫu rồi so với trung bình ba điểm số.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML13](#kiem-lai-ml13)

Ôn cùng thao tác · [ML13-practice-2](#ml13-practice-2) · [ML13-practice-3](#ml13-practice-3)


<a id="ml14"></a>

## ML14 · Đo sai số hồi quy

Từ y và dự đoán yhat, nộp bốn đại lượng theo thứ tự [sai số tuyệt đối trung bình (MAE), sai số bình phương trung bình (MSE), căn MSE (RMSE), hệ số xác định (R²)]. Nếu y hằng, ghi null cho R².

Tiên quyết · ML04

### A · Dự đoán

1. Phần dư nào có độ lớn lớn nhất? Nó đóng góp bao nhiêu cho tổng bình phương?
2. Từ ba phần dư, ghi bốn chỉ số theo thứ tự đề yêu cầu. Giữ đủ chữ số khi lấy căn.

### B · Chạy mẫu

```python
import numpy as np

def regression_metrics(y, yhat):
    y, yhat = (np.asarray(y, dtype=float), np.asarray(yhat, dtype=float))
    e = yhat - y
    mse = np.mean(e ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    r2 = None if sst == 0 else float(1 - np.sum(e ** 2) / sst)
    return (float(np.abs(e).mean()), float(mse), float(np.sqrt(mse)), r2)

y = [1, 3, 5]
yhat = [2, 3, 3]
print(regression_metrics(y, yhat))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml14)

### C · Lần theo mã

1. R² dùng độ lệch của y so với trung bình nào? Điều gì xảy ra khi mọi y bằng nhau?
2. So [1,3,5] với dự đoán hằng bằng trung bình của y. Điều gì trong công thức R² giúp so với mốc này?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay yhat rồi giải lại đề lõi.  
**D1** · `y = [1,3,5]  yhat = [1,4,7]`

Thay y rồi giải lại đề lõi.  
**D2** · `y = [0,2,6]  yhat = [2,3,3]`

Thay yhat rồi giải lại đề lõi.  
**D3** · `y = [1,3,5]  yhat = [1,3,5]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `y = [0,2]  yhat = [1,4]`  
Kết quả tự nộp ____________________

**E2** · `y = [3,3,3]  yhat = [3,4,2]`  
Kết quả tự nộp ____________________

**E3** · `y = [2,5,8]  yhat = [1,4,7]`  
Kết quả tự nộp ____________________

**E4** · `y = [-1,1]  yhat = [1,-1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `regression_metrics(y, yhat)`. Hai vectơ số cùng độ dài dương. Trả tuple (MAE, MSE, RMSE, R²). Dùng None cho R² nếu y hằng. Báo ValueError khi kích thước sai. [Tệp điền mã](../../thuc-hanh/ML14.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `y = [1,4]  yhat = [1,6]`  
Kết quả tự nộp ____________________

**R2** · `y = [5,5]  yhat = [4,7]`  
Kết quả tự nộp ____________________

**R3** · `y = [0,3,6]  yhat = [2,4,5]`  
Kết quả tự nộp ____________________

**R4** · `y = [-2,2]  yhat = [2,-2]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một người nhân cả y lẫn dự đoán với 10. Với y = [1,3], dự đoán [1,5], hãy kiểm các hệ số thay đổi của MAE, MSE, RMSE và R².

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML14](#kiem-lai-ml14)

Ôn cùng thao tác · [ML14-practice-4](#ml14-practice-4) · [ML14-practice-8](#ml14-practice-8)


<a id="ml15"></a>

## ML15 · Đo chất lượng phân loại nhị phân

Lấy 1 làm lớp dương. Bạn có hai vectơ, y ghi nhãn thực và p ghi nhãn dự đoán. Từ đó, nộp bốn số theo thứ tự [tỷ lệ đúng (accuracy), độ chuẩn xác (precision), độ bao phủ (recall), điểm F1]. Nếu mẫu số của đại lượng nào bằng 0, ghi 0 ở đúng vị trí ấy. TP và TN là số dương đúng và âm đúng. FP và FN là số dương giả và âm giả.

Tiên quyết · ML09

### A · Dự đoán

1. Bao nhiêu mẫu được dự đoán là dương? Bao nhiêu mẫu thực sự dương?
2. Ghi [accuracy,precision,recall,F1] từ bốn số đếm của chính bộ mẫu.

### B · Chạy mẫu

```python
import numpy as np

def binary_metrics(y, p):
    y, p = (np.asarray(y), np.asarray(p))
    tp = int(np.count_nonzero((y == 1) & (p == 1)))
    actual, predicted = (int(y.sum()), int(p.sum()))
    precision = tp / predicted if predicted else 0
    recall = tp / actual if actual else 0
    f1 = 2 * tp / (actual + predicted) if actual + predicted else 0
    return (float((y == p).mean()), precision, recall, f1)

y = [1, 1, 0, 0, 0]
p = [1, 0, 1, 0, 0]
print(binary_metrics(y, p))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml15)

### C · Lần theo mã

1. Khi bỏ sót một mẫu dương, mẫu số của precision và recall được hình thành từ những nhóm nào?
2. Ở lượt B, ba điểm cuối bằng nhau. Dựa vào các số đếm để chỉ ra điều gì khiến precision bằng recall trong riêng bộ này.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay p rồi giải lại đề lõi.  
**D1** · `y = [1,1,0,0,0]  p = [1,1,1,0,0]`

Thay y rồi giải lại đề lõi.  
**D2** · `y = [1,0,1,0,0]  p = [1,0,1,0,0]`

Thay p rồi giải lại đề lõi.  
**D3** · `y = [1,1,0,0,0]  p = [0,0,0,0,0]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `y = [1,1,0,1]  p = [1,0,1,1]`  
Kết quả tự nộp ____________________

**E2** · `y = [1,1,1,0]  p = [1,0,0,0]`  
Kết quả tự nộp ____________________

**E3** · `y = [0,1,0]  p = [0,0,0]`  
Kết quả tự nộp ____________________

**E4** · `y = [0,0,1,1,0]  p = [1,0,1,1,1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `binary_metrics(y, p)`. Hai vectơ 0/1 cùng độ dài dương, lớp dương là 1. Trả tuple (accuracy, precision, recall, F1), chia cho 0 thì dùng 0. Báo ValueError nếu miền hoặc kích thước sai. [Tệp điền mã](../../thuc-hanh/ML15.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `y = [0,1,1,0]  p = [0,1,1,0]`  
Kết quả tự nộp ____________________

**R2** · `y = [1,0,1,1,1]  p = [1,0,0,0,1]`  
Kết quả tự nộp ____________________

**R3** · `y = [0,0,1,0]  p = [0,0,0,0]`  
Kết quả tự nộp ____________________

**R4** · `y = [1,0,0,0]  p = [1,1,1,0]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một âm giả tốn 5 đơn vị, một dương giả tốn 1. So mô hình A có (FP,FN) = (4,1) với B có (1,2). Chọn mô hình và giải thích.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML15](#kiem-lai-ml15)

Ôn cùng thao tác · [ML15-practice-3](#ml15-practice-3) · [ML15-practice-4](#ml15-practice-4)


<a id="ml16"></a>

## ML16 · Dựng các điểm trên đường ROC

Dựng đường đặc trưng hoạt động (ROC) từ nhãn nhị phân và điểm dự đoán. Bắt đầu ở [0,0], rồi hạ ngưỡng qua các điểm phân biệt từ cao xuống thấp. Nộp các cặp [tỷ lệ dương giả (FPR), tỷ lệ dương đúng (TPR)]. Nhận mọi điểm bằng ngưỡng.

Tiên quyết · ML15

### A · Dự đoán

1. Điểm cao nhất thuộc lớp nào? Tọa độ nào của đường ROC thay đổi trước?
2. Liệt kê các ngưỡng phân biệt từ cao xuống thấp rồi dự đoán toàn bộ các cặp [FPR,TPR].

### B · Chạy mẫu

```python
import numpy as np

def roc_curve_points(y, score):
    y, score = (np.asarray(y), np.asarray(score, dtype=float))
    rows = [(0.0, 0.0)]
    for t in np.unique(score)[::-1]:
        positive = score >= t
        rows.append((positive[y == 0].mean(), positive[y == 1].mean()))
    return np.asarray(rows)

y = [1, 0, 1, 0]
score = [0.9, 0.6, 0.4, 0.1]
print(roc_curve_points(y, score))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml16)

### C · Lần theo mã

1. Hai mẫu bằng điểm có đi vào dự đoán dương ở cùng một ngưỡng không?
2. Theo dõi bước hạ ngưỡng qua điểm 0,6. Tại sao chỉ một tọa độ thay đổi ở bước ấy?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay score rồi giải lại đề lõi.  
**D1** · `y = [1,0,1,0]  score = [0.8,0.6,0.6,0.2]`

Thay y rồi giải lại đề lõi.  
**D2** · `y = [0,1,1,0]  score = [0.9,0.6,0.4,0.1]`

Thay score rồi giải lại đề lõi.  
**D3** · `y = [1,0,1,0]  score = [0.4,0.7,0.9,0.2]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `y = [0,1,1]  score = [0.8,0.6,0.2]`  
Kết quả tự nộp ____________________

**E2** · `y = [1,0,1,0]  score = [0.8,0.8,0.5,0.1]`  
Kết quả tự nộp ____________________

**E3** · `y = [0,0,1]  score = [1,3,2]`  
Kết quả tự nộp ____________________

**E4** · `y = [1,0]  score = [0.2,0.2]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `roc_curve_points(y, score)`. Nhận vectơ nhãn 0/1 có cả hai lớp và vectơ score hữu hạn cùng kích thước. Trả ma trận hai cột FPR và TPR cho threshold +∞ rồi các score phân biệt theo thứ tự giảm. Báo ValueError nếu miền hoặc kích thước sai. [Tệp điền mã](../../thuc-hanh/ML16.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `y = [1,1,0]  score = [0.5,0.9,0.7]`  
Kết quả tự nộp ____________________

**R2** · `y = [0,1,0,1]  score = [0.7,0.7,0.2,0.1]`  
Kết quả tự nộp ____________________

**R3** · `y = [1,0,0]  score = [2,0,1]`  
Kết quả tự nộp ____________________

**R4** · `y = [0,1,1]  score = [4,4,2]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Dùng các điểm ROC [[0,0],[0,0.5],[0.5,1],[1,1]] để tính diện tích dưới đường cong (AUC) bằng quy tắc hình thang. Ghi diện tích từng dải.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML16](#kiem-lai-ml16)

Ôn cùng thao tác · [ML16-practice-2](#ml16-practice-2) · [ML16-practice-3](#ml16-practice-3)


<a id="ml17"></a>

## ML17 · Chọn bậc mô hình bằng sai số xác thực

Nhận các bậc cùng sai số huấn luyện và xác thực (validation loss). Chọn bậc có sai số xác thực nhỏ nhất, nếu hòa thì chọn bậc nhỏ hơn. Nộp [bậc, sai số xác thực trừ sai số huấn luyện] ở đúng bậc đã chọn.

Tiên quyết · ML08, ML13

### A · Dự đoán

1. Bậc nào có sai số xác thực nhỏ nhất? Hãy đánh dấu cùng vị trí trên cả ba dãy.
2. Nộp cặp [bậc,độ chênh] cho lựa chọn của bạn. Kiểm tra dấu của phép trừ.

### B · Chạy mẫu

```python
import numpy as np

def pick_degree(degrees, train_loss, val_loss):
    degrees = np.asarray(degrees)
    train, valid = (np.asarray(train_loss, dtype=float), np.asarray(val_loss, dtype=float))
    i = np.lexsort((degrees, valid))[0]
    return (int(degrees[i]), float(valid[i] - train[i]))

degrees = [1, 2, 4]
train_loss = [4, 2, 0]
val_loss = [5, 3, 6]
print(pick_degree(degrees, train_loss, val_loss))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml17)

### C · Lần theo mã

1. Nếu đảo thứ tự các bậc cùng các giá trị tương ứng, kết quả có đổi không? Vì sao?
2. Nếu chỉ nhìn dãy sai số huấn luyện, bạn sẽ chọn bậc nào? So với tiêu chí được chấm.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay val_loss rồi giải lại đề lõi.  
**D1** · `degrees = [1,2,4]  train_loss = [4,2,0]  val_loss = [4,4,7]`

Thay train_loss rồi giải lại đề lõi.  
**D2** · `degrees = [1,2,4]  train_loss = [3,1,0]  val_loss = [5,3,6]`

Thay degrees rồi giải lại đề lõi.  
**D3** · `degrees = [2,1,4]  train_loss = [4,2,0]  val_loss = [5,3,6]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `degrees = [1,3,5]  train_loss = [5,2,0]  val_loss = [6,3,7]`  
Kết quả tự nộp ____________________

**E2** · `degrees = [4,1,3]  train_loss = [0,3,1]  val_loss = [4,4,5]`  
Kết quả tự nộp ____________________

**E3** · `degrees = [0,2]  train_loss = [3,2]  val_loss = [2,5]`  
Kết quả tự nộp ____________________

**E4** · `degrees = [3]  train_loss = [2]  val_loss = [1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `pick_degree(degrees, train_loss, val_loss)`. Nhận ba vectơ cùng độ dài dương. Bậc nguyên không âm và phân biệt. Loss hữu hạn không âm. Trả (bậc có val_loss nhỏ nhất, val_loss−train_loss của bậc đó), nếu hòa thì lấy bậc nhỏ. Báo ValueError cho đầu vào sai. [Tệp điền mã](../../thuc-hanh/ML17.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `degrees = [0,1,2]  train_loss = [4,3,2]  val_loss = [5,2,4]`  
Kết quả tự nộp ____________________

**R2** · `degrees = [5,2,1]  train_loss = [0,2,3]  val_loss = [3,3,5]`  
Kết quả tự nộp ____________________

**R3** · `degrees = [1,4]  train_loss = [2,0]  val_loss = [1,6]`  
Kết quả tự nộp ____________________

**R4** · `degrees = [2]  train_loss = [4]  val_loss = [2]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một người chọn bậc 4 vì sai số huấn luyện bằng 0. Với bậc [1,2,4], sai số huấn luyện [4,2,0] và sai số xác thực [5,3,8], chẩn đoán và đề xuất lựa chọn.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML17](#kiem-lai-ml17)

Ôn cùng thao tác · [ML17-practice-2](#ml17-practice-2) · [ML17-practice-3](#ml17-practice-3)


<a id="ml18"></a>

## ML18 · Khớp hồi quy có phạt L2

Hồi quy Ridge (ridge regression) tối thiểu hóa tổng bình phương phần dư cộng lam nhân tổng bình phương các trọng số. Bỏ hệ số tự do khỏi phần phạt. Nộp [hệ số tự do, các trọng số]. Khi lam bằng 0, dùng bình phương tối thiểu.

Tiên quyết · ML17, ML05

### A · Dự đoán

1. Cột nào của ma trận thiết kế đi cùng hệ số tự do? Ô nào trên đường chéo ma trận phạt phải bằng 0?
2. Ghi hệ số tự do và trọng số sau điều chuẩn. Với X có trung bình 0, hãy đoán hệ số nào dễ tìm trước.

### B · Chạy mẫu

```python
import numpy as np

def ridge_fit(X, y, lam):
    X, y = (np.asarray(X, dtype=float), np.asarray(y, dtype=float))
    A = np.column_stack([np.ones(len(X)), X])
    if lam == 0:
        return np.linalg.lstsq(A, y, rcond=None)[0]
    penalty = np.eye(A.shape[1])
    penalty[0, 0] = 0
    return np.linalg.solve(A.T @ A + lam * penalty, A.T @ y)

X = [[-1], [0], [1]]
y = [0, 2, 4]
lam = 2
print(ridge_fit(X, y, lam))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml18)

### C · Lần theo mã

1. Thêm cùng một hằng số vào mọi y sẽ tác động thế nào đến hệ số tự do nếu X đã có trung bình 0?
2. Tính riêng tổng x² rồi quan sát tác dụng của lam ở mẫu số của trọng số trên bộ dữ liệu này.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay lam rồi giải lại đề lõi.  
**D1** · `X = [[-1],[0],[1]]  y = [0,2,4]  lam = 4`

Thay y rồi giải lại đề lõi.  
**D2** · `X = [[-1],[0],[1]]  y = [1,3,5]  lam = 2`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[-2],[0],[2]]  y = [0,2,4]  lam = 2`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[-2],[0],[2]]  y = [0,3,6]  lam = 4`  
Kết quả tự nộp ____________________

**E2** · `X = [[-1],[0],[1]]  y = [3,5,7]  lam = 2`  
Kết quả tự nộp ____________________

**E3** · `X = [[0],[1],[2]]  y = [1,4,7]  lam = 0`  
Kết quả tự nộp ____________________

**E4** · `X = [[-1,0],[0,1],[1,0]]  y = [0,4,2]  lam = 1`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `ridge_fit(X, y, lam)`. X 2D có ít nhất một hàng và một cột, y là vectơ cùng số hàng, λ hữu hạn không âm. Trả vectơ [hệ số tự do, các hệ số] tối thiểu hóa SSE + λ·Σwⱼ², bỏ phạt hệ số tự do. λ=0 dùng nghiệm `lstsq`. Báo ValueError nếu kích thước hoặc λ sai. [Tệp điền mã](../../thuc-hanh/ML18.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[-3],[0],[3]]  y = [0,2,4]  lam = 6`  
Kết quả tự nộp ____________________

**R2** · `X = [[-2],[0],[2]]  y = [2,6,10]  lam = 8`  
Kết quả tự nộp ____________________

**R3** · `X = [[1],[2],[3]]  y = [0,3,6]  lam = 0`  
Kết quả tự nộp ____________________

**R4** · `X = [[-2,0],[0,1],[2,0]]  y = [-1,5,3]  lam = 2`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Một bản sửa phạt cả hệ số tự do. Với X = [[0],[0]], y = [2,6] và lam = 2, tính b ở hai phiên bản. Giải thích sự khác biệt.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML18](#kiem-lai-ml18)

Ôn cùng thao tác · [ML18-practice-1](#ml18-practice-1) · [ML18-practice-4](#ml18-practice-4)


<a id="ml19"></a>

## ML19 · Gán nhãn bằng perceptron

Với bộ phân loại perceptron, tính điểm z = Xw + b cho từng hàng. Nộp vectơ nhãn theo quy tắc z ≥ 0 cho nhãn 1, các điểm còn lại cho nhãn 0.

Tiên quyết · ML09

### A · Dự đoán

1. Hàng nào cho điểm bằng 0? Nhãn của các hàng ấy là gì?
2. Tính ba điểm z rồi viết vectơ nhãn cuối cùng theo thứ tự hàng.

### B · Chạy mẫu

```python
import numpy as np

def perceptron(X, w, b):
    X, w = (np.asarray(X), np.asarray(w))
    return (X @ w + b >= 0).astype(int)

X = [[0, 0], [1, 0], [1, 1]]
w = [1, -1]
b = 0
print(perceptron(X, w, b))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml19)

### C · Lần theo mã

1. Tìm dòng mà việc đổi dấu ≥ thành > sẽ ảnh hưởng đến đầu ra.
2. Tìm tất cả hàng nằm đúng đường biên và giải thích vì sao chúng có cùng nhãn.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay b rồi giải lại đề lõi.  
**D1** · `X = [[0,0],[1,0],[1,1]]  w = [1,-1]  b = -1`

Thay w rồi giải lại đề lõi.  
**D2** · `X = [[0,0],[1,0],[1,1]]  w = [2,-1]  b = 0`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[-1,2],[1,1],[2,1]]  w = [1,-1]  b = 0`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[1,0],[0,1]]  w = [2,-1]  b = -1`  
Kết quả tự nộp ____________________

**E2** · `X = [[-1],[0],[2]]  w = [2]  b = 0`  
Kết quả tự nộp ____________________

**E3** · `X = [[1,2],[2,1],[0,1]]  w = [-1,2]  b = -1`  
Kết quả tự nộp ____________________

**E4** · `X = [[-1],[2]]  w = [0]  b = -2`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `perceptron(X, w, b)`. Nhận ma trận 2D có ít nhất một cột và vectơ w có đúng số cột. Trả vectơ nhị phân theo z≥0. Báo ValueError nếu kích thước sai. [Tệp điền mã](../../thuc-hanh/ML19.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[2,0],[0,1]]  w = [1,-2]  b = -3`  
Kết quả tự nộp ____________________

**R2** · `X = [[2],[-1],[0]]  w = [1]  b = 1`  
Kết quả tự nộp ____________________

**R3** · `X = [[2,1],[0,1],[1,0]]  w = [-2,1]  b = 1`  
Kết quả tự nộp ____________________

**R4** · `X = [[3],[1]]  w = [0]  b = 1`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Thiết kế cổng AND cho bốn điểm [[0,0],[0,1],[1,0],[1,1]]. Chọn w, b và chứng minh bằng bốn nhãn.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML19](#kiem-lai-ml19)

Ôn cùng thao tác · [ML19-practice-2](#ml19-practice-2) · [ML19-practice-4](#ml19-practice-4)


<a id="ml20"></a>

## ML20 · Tính ReLU và đạo hàm

Hàm kích hoạt tuyến tính chỉnh lưu (rectified linear unit, ReLU) cho max(0,z). Với kind bằng 'relu', nộp [giá trị hàm, đạo hàm] cho từng vị trí của z. Dùng đạo hàm quy ước bằng 0 tại z = 0.

Tiên quyết · ML19

### A · Dự đoán

1. Phần tử 0 sẽ cho cặp giá trị và đạo hàm nào? Giá trị nào của z được giữ lại?
2. Ghi hai mảng riêng cho giá trị ReLU và đạo hàm. Kiểm tra vị trí ứng với z = 0.

### B · Chạy mẫu

```python
import numpy as np

def activation_and_derivative(z, kind):
    z = np.asarray(z, dtype=float)
    return np.maximum(0, z), (z > 0).astype(float)

z = [-1, 0, 2]
kind = 'relu'
print(activation_and_derivative(z, kind))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml20)

### C · Lần theo mã

1. Tại một đầu vào dương, phân biệt giá trị của hàm với độ dốc của đồ thị.
2. So đạo hàm ở z = −1 với ở z = 2 bằng cách xem đồ thị thay đổi thế nào quanh mỗi điểm.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay z rồi giải lại đề lõi.  
**D1** · `z = [-2,1,3]  kind = "relu"`

Thay z rồi giải lại đề lõi.  
**D2** · `z = [0,-3,4]  kind = "relu"`

Thay z rồi giải lại đề lõi.  
**D3** · `z = [1,2,-1,0]  kind = "relu"`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `z = [-3,2]  kind = "relu"`  
Kết quả tự nộp ____________________

**E2** · `z = [0,-2,5]  kind = "relu"`  
Kết quả tự nộp ____________________

**E3** · `z = [2,4,0]  kind = "relu"`  
Kết quả tự nộp ____________________

**E4** · `z = [-1,-4]  kind = "relu"`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `activation_and_derivative(z, kind)`. Dùng kind = 'relu' trong đề lõi. Hàm trả hai mảng cùng kích thước z. Ghi đạo hàm 0 tại gốc. Bài F thêm hai hàm kích hoạt khác. Tên hàm kích hoạt ngoài các tên được hỗ trợ phải báo ValueError. [Tệp điền mã](../../thuc-hanh/ML20.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `z = [1,-5]  kind = "relu"`  
Kết quả tự nộp ____________________

**R2** · `z = [-1,4,0]  kind = "relu"`  
Kết quả tự nộp ____________________

**R3** · `z = [7,0,1]  kind = "relu"`  
Kết quả tự nộp ____________________

**R4** · `z = [-2,-6,-1]  kind = "relu"`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Thêm sigmoid và tanh vào hàm kích hoạt. Tại z = 0, so giá trị và đạo hàm của hai hàm mới với ReLU. Thử thêm sigmoid ở −1000 và 1000.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML20](#kiem-lai-ml20)

Ôn cùng thao tác · [ML20-practice-1](#ml20-practice-1) · [ML20-practice-5](#ml20-practice-5)


<a id="ml21"></a>

## ML21 · Lan truyền tiến qua hai tầng

Lan truyền tiến (forward propagation) theo thứ tự XW₁ + b₁, ReLU, rồi HW₂ + b₂ với H là đầu ra tầng ẩn. Tầng cuối là tuyến tính. Nộp ma trận có một hàng cho mỗi mẫu và một cột cho mỗi đầu ra.

Tiên quyết · ML20

Đến ML22, cùng đi qua hai tầng nhưng đổi sang sigmoid ở cả hai tầng để tính tổn thất phân loại. Thử mạng mẫu của ML22 với x = [0,2], tham số [0,0,2,−1].

### A · Dự đoán

1. Mẫu nào cho giá trị âm trước ReLU? Tầng cuối nhận giá trị nào từ mẫu ấy?
2. Từ hai giá trị tầng ẩn, tính hai hàng của ma trận đầu ra. Giữ nguyên chiều có độ dài 1.

### B · Chạy mẫu

```python
import numpy as np

def forward(X, W1, b1, W2, b2):
    X, W1, b1, W2, b2 = (np.asarray(v, dtype=float) for v in (X, W1, b1, W2, b2))
    return np.maximum(0, X @ W1 + b1) @ W2 + b2

X = [[-1], [2]]
W1 = [[2]]
b1 = [0]
W2 = [[3]]
b2 = [1]
print(forward(X, W1, b1, W2, b2))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml21)

### C · Lần theo mã

1. Nếu trọng số ở tầng cuối là số âm, có cần áp dụng ReLU ở đầu ra không? Đối chiếu với công thức.
2. Ở hàng đầu, giá trị tầng ẩn bằng 0. Xác định tham số nào còn quyết định đầu ra của hàng ấy.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay b1 rồi giải lại đề lõi.  
**D1** · `X = [[-1],[2]]  W1 = [[2]]  b1 = [1]  W2 = [[3]]  b2 = [1]`

Thay b2 rồi giải lại đề lõi.  
**D2** · `X = [[-1],[2]]  W1 = [[2]]  b1 = [0]  W2 = [[3]]  b2 = [-1]`

Thay X rồi giải lại đề lõi.  
**D3** · `X = [[-2],[0],[3]]  W1 = [[2]]  b1 = [0]  W2 = [[3]]  b2 = [1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[-2],[1]]  W1 = [[1]]  b1 = [0]  W2 = [[2]]  b2 = [1]`  
Kết quả tự nộp ____________________

**E2** · `X = [[-3],[1]]  W1 = [[2]]  b1 = [1]  W2 = [[-2]]  b2 = [4]`  
Kết quả tự nộp ____________________

**E3** · `X = [[0],[2]]  W1 = [[-1]]  b1 = [1]  W2 = [[3]]  b2 = [-2]`  
Kết quả tự nộp ____________________

**E4** · `X = [[1],[-1],[3]]  W1 = [[1]]  b1 = [-1]  W2 = [[2]]  b2 = [0]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `forward(X, W1, b1, W2, b2)`. Thực hiện X @ W1 + b1, ReLU, rồi H @ W2 + b2. Trả ma trận 2D kể cả khi chỉ có 1 mẫu hay 1 neuron đầu ra. Các bias là vectơ 1D đúng độ dài. Báo ValueError khi kích thước không tương thích. [Tệp điền mã](../../thuc-hanh/ML21.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[-3],[2]]  W1 = [[1]]  b1 = [0]  W2 = [[3]]  b2 = [1]`  
Kết quả tự nộp ____________________

**R2** · `X = [[-2],[2]]  W1 = [[2]]  b1 = [-1]  W2 = [[-3]]  b2 = [5]`  
Kết quả tự nộp ____________________

**R3** · `X = [[0],[-2]]  W1 = [[1]]  b1 = [1]  W2 = [[2]]  b2 = [-1]`  
Kết quả tự nộp ____________________

**R4** · `X = [[-1],[0],[4]]  W1 = [[1]]  b1 = [-2]  W2 = [[2]]  b2 = [1]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Đổi hàm kích hoạt ẩn và hàm đầu ra sang sigmoid để chuẩn bị cho ML22. Với x = [0,2] và [w₁,b₁,w₂,b₂] = [0,0,2,−1], tính cả h và p.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML21](#kiem-lai-ml21)

Ôn cùng thao tác · [ML21-practice-2](#ml21-practice-2) · [ML21-practice-4](#ml21-practice-4)


<a id="ml22"></a>

## ML22 · Lan truyền ngược trên cả lô

Lan truyền ngược (backpropagation) cho mạng có một nơron sigmoid ở mỗi tầng và BCE trung bình. Tính h và p cho tất cả các mẫu trước. Nộp bốn gradient trung bình theo thứ tự [w₁,b₁,w₂,b₂].

Tiên quyết · ML21

Bắt đầu bằng một lượt lan truyền tiến cho chính mạng sigmoid của bài này. Dùng x = [0,2], w₁ = b₁ = 0, w₂ = 2 và b₂ = −1. Giữ h và p của cả hai hàng để đi ngược từ tầng ra.

### A · Dự đoán

1. Ở trạng thái mẫu, h và p của mỗi hàng bằng bao nhiêu? Sai số p − y có cùng dấu trên hai hàng không?
2. Ghi bốn gradient theo thứ tự tham số. Hãy đánh dấu chỗ bạn dự đoán các đóng góp sẽ triệt tiêu.

### B · Chạy mẫu

```python
import numpy as np

def backprop_1d(x, y, params):
    x, y, params = (np.asarray(v, dtype=float) for v in (x, y, params))
    w1, b1, w2, b2 = params
    h = np.exp(-np.logaddexp(0, -(w1 * x + b1)))
    p = np.exp(-np.logaddexp(0, -(w2 * h + b2)))
    d2 = p - y
    d1 = d2 * w2 * h * (1 - h)
    return np.array([(d1 * x).mean(), d1.mean(), (d2 * h).mean(), d2.mean()])

x = [0, 2]
y = [0, 1]
params = [0, 0, 2, -1]
print(backprop_1d(x, y, params))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml22)

### C · Lần theo mã

1. So hai phép lấy trung bình tạo gradient theo w₁ và b₁. Phép nào cần nhân thêm x?
2. Viết riêng đóng góp vào gradient w₁ của mẫu x = 0 và của mẫu x = 2. Vì sao trung bình của chúng khác 0?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay x rồi giải lại đề lõi.  
**D1** · `x = [-1,3]  y = [0,1]  params = [0,0,2,-1]`

Thay y rồi giải lại đề lõi.  
**D2** · `x = [0,2]  y = [1,1]  params = [0,0,2,-1]`

Thay params rồi giải lại đề lõi.  
**D3** · `x = [0,2]  y = [0,1]  params = [0,0,-2,1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [1,3]  y = [0,1]  params = [0,0,2,-1]`  
Kết quả tự nộp ____________________

**E2** · `x = [-1,2]  y = [1,0]  params = [0,0,2,-1]`  
Kết quả tự nộp ____________________

**E3** · `x = [0,1,2]  y = [1,1,0]  params = [0,0,0,0]`  
Kết quả tự nộp ____________________

**E4** · `x = [-1,1]  y = [0,1]  params = [1,0,1,0]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `backprop_1d(x, y, params)`. x,y là hai vectơ cùng độ dài dương, y nhị phân, params có đúng bốn số (w1,b1,w2,b2). Với một neuron sigmoid mỗi tầng và BCE trung bình, trả mảng bốn gradient tương ứng. Báo ValueError nếu kích thước hoặc y sai. [Tệp điền mã](../../thuc-hanh/ML22.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [0,4]  y = [1,0]  params = [0,0,2,-1]`  
Kết quả tự nộp ____________________

**R2** · `x = [-2,3]  y = [0,1]  params = [0,0,-2,1]`  
Kết quả tự nộp ____________________

**R3** · `x = [0,2,4]  y = [0,1,0]  params = [0,0,0,0]`  
Kết quả tự nộp ____________________

**R4** · `x = [-2,1]  y = [1,0]  params = [1,0,1,0]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Kiểm gradient theo w₁ bằng cách tăng và giảm riêng w₁ một lượng 10⁻⁵. Dùng đúng bộ B, BCE trung bình và các tham số còn lại giữ cố định.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML22](#kiem-lai-ml22)

Ôn cùng thao tác · [ML22-practice-1](#ml22-practice-1) · [ML22-practice-6](#ml22-practice-6)


<a id="ml23"></a>

## ML23 · Một vòng phân cụm Lloyd

Thực hiện một vòng của phân cụm K-means (K-means clustering) bằng thuật toán Lloyd. Gán mẫu vào tâm Euclid gần nhất, hòa chọn chỉ số nhỏ. Tính lại tâm từ các nhãn vừa gán, giữ tâm cũ nếu cụm rỗng. Nộp [nhãn, tâm mới, tổng bình phương khoảng cách đến tâm mới (SSE)].

Tiên quyết · ML01

Mang nhãn của lượt B sang ML24. Bốn vị trí giữ nguyên thứ tự khi đối chiếu với một phân hoạch tham chiếu.

### A · Dự đoán

1. Hai hàng đầu gần tâm nào hơn? Sau khi gán các điểm đó, tâm đầu chuyển về đâu?
2. Dự đoán nhãn, hai tâm mới và SSE. Dùng một hàng cho mỗi tâm.

### B · Chạy mẫu

```python
import numpy as np

def lloyd_step(X, centers):
    X, centers = (np.asarray(X, dtype=float), np.asarray(centers, dtype=float))
    d2 = ((X[:, None, :] - centers[None, :, :]) ** 2).sum(axis=2)
    labels = d2.argmin(axis=1)
    updated = centers.copy()
    for i in range(len(centers)):
        members = X[labels == i]
        if len(members):
            updated[i] = members.mean(axis=0)
    return (labels, updated, float(((X - updated[labels]) ** 2).sum()))

X = [[0], [2], [7], [9]]
centers = [[0], [7]]
print(lloyd_step(X, centers))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml23)

### C · Lần theo mã

1. Khi tính SSE cuối vòng, dùng nhãn và tâm của thời điểm nào?
2. Chọn điểm 2 và so bình phương khoảng cách của nó trước và sau khi tâm di chuyển.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay centers rồi giải lại đề lõi.  
**D1** · `X = [[0],[2],[7],[9]]  centers = [[1],[8]]`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [[0],[4],[6],[10]]  centers = [[0],[7]]`

Thay centers rồi giải lại đề lõi.  
**D3** · `X = [[0],[2],[7],[9]]  centers = [[2],[5]]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[1],[3],[8],[10]]  centers = [[1],[9]]`  
Kết quả tự nộp ____________________

**E2** · `X = [[0],[2],[4],[7]]  centers = [[0],[4]]`  
Kết quả tự nộp ____________________

**E3** · `X = [[-3],[-1],[4],[6]]  centers = [[-3],[4]]`  
Kết quả tự nộp ____________________

**E4** · `X = [[0],[1],[8]]  centers = [[0],[8],[30]]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `lloyd_step(X, centers)`. Nhận X và centers là hai ma trận 2D hữu hạn, không rỗng, cùng số cột dương. Trả (labels, centers_mới, SSE sau cập nhật với labels vừa gán). Hòa khoảng cách chọn chỉ số cụm nhỏ. Cụm rỗng giữ tâm cũ. Báo ValueError khi kích thước hoặc giá trị sai. [Tệp điền mã](../../thuc-hanh/ML23.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[0],[3],[6],[9]]  centers = [[0],[9]]`  
Kết quả tự nộp ____________________

**R2** · `X = [[1],[3],[5],[8]]  centers = [[1],[5]]`  
Kết quả tự nộp ____________________

**R3** · `X = [[-4],[0],[5],[7]]  centers = [[-4],[6]]`  
Kết quả tự nộp ____________________

**R4** · `X = [[1],[2],[7]]  centers = [[1],[7],[20]]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Chạy vòng Lloyd thứ hai trên X = [[0],[3],[4],[10]] với tâm ban đầu [[0],[4]]. So nhãn, tâm và SSE qua hai vòng.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML23](#kiem-lai-ml23)

Ôn cùng thao tác · [ML23-practice-5](#ml23-practice-5) · [ML23-practice-6](#ml23-practice-6)


<a id="ml24"></a>

## ML24 · So sánh hai phân hoạch theo cặp

Dùng chỉ số Rand (Rand index) và Jaccard để so hai cách chia cụm. Xét từng cặp chỉ số i < j một lần. Rand tính tỷ lệ hai phân hoạch đưa ra cùng quyết định. Jaccard lấy số cặp cùng cụm ở cả hai chia cho số cặp cùng cụm ở ít nhất một. Nếu mẫu số bằng 0, lấy Jaccard = 1. Nộp [Rand,Jaccard].

Tiên quyết · ML23

Phân hoạch a = [0,0,1,1] lấy từ lượt B của ML23. So với b = [2,2,2,3] theo từng cặp mẫu.

### A · Dự đoán

1. Với bốn mẫu có bao nhiêu cặp? Hai mẫu đầu cùng cụm trong những phân hoạch nào?
2. Lập bảng sáu cặp rồi nộp [Rand,Jaccard]. Bạn dự đoán hai chỉ số có bằng nhau không?

### B · Chạy mẫu

```python
import numpy as np

def pair_scores(a, b):
    a, b = (np.asarray(a), np.asarray(b))
    i, j = np.triu_indices(a.size, k=1)
    left, right = (a[i] == a[j], b[i] == b[j])
    union = np.count_nonzero(left | right)
    match = np.count_nonzero(left & right)
    return (float((left == right).mean()), match / union if union else 1.0)

a = [0, 0, 1, 1]
b = [2, 2, 2, 3]
print(pair_scores(a, b))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml24)

### C · Lần theo mã

1. Nếu đổi toàn bộ tên cụm, quyết định “cùng cụm” của một cặp có đổi không?
2. Tìm một cặp khác cụm ở cả hai phân hoạch. Cặp đó được tính thế nào trong từng chỉ số?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay b rồi giải lại đề lõi.  
**D1** · `a = [0,0,1,1]  b = [2,2,3,3]`

Thay a rồi giải lại đề lõi.  
**D2** · `a = [0,1,1,1]  b = [2,2,2,3]`

Thay b rồi giải lại đề lõi.  
**D3** · `a = [0,0,1,1]  b = [0,1,0,1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `a = [0,0,1]  b = [3,4,4]`  
Kết quả tự nộp ____________________

**E2** · `a = [0,0,1,2]  b = [7,7,8,9]`  
Kết quả tự nộp ____________________

**E3** · `a = [0,1,2]  b = [4,5,6]`  
Kết quả tự nộp ____________________

**E4** · `a = [1,1,1,0]  b = [2,2,3,3]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `pair_scores(a, b)`. Hai vectơ nhãn nguyên 1D cùng độ dài, tối thiểu hai phần tử. Trả (Rand, Jaccard). Dùng Jaccard=1 nếu cả hai không có cặp cùng cụm. Báo ValueError nếu đầu vào sai kích thước. [Tệp điền mã](../../thuc-hanh/ML24.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `a = [0,1,1,0,2]  b = [4,4,5,5,6]`  
Kết quả tự nộp ____________________

**R2** · `a = [2,1,2,0]  b = [4,7,4,7]`  
Kết quả tự nộp ____________________

**R3** · `a = [3,2,1,0]  b = [8,7,6,6]`  
Kết quả tự nộp ____________________

**R4** · `a = [1,0,0]  b = [1,1,1]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Hai phân hoạch [0,0,1,1] và [7,7,3,3] đặt tên cụm khác nhau. Thử so nhãn theo từng hàng rồi dùng Rand và Jaccard. Giải thích kết quả.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML24](#kiem-lai-ml24)

Ôn cùng thao tác · [ML24-practice-3](#ml24-practice-3) · [ML24-practice-4](#ml24-practice-4)


<a id="ml25"></a>

## ML25 · Khớp các trục chính của PCA

Phân tích thành phần chính (principal component analysis, PCA) bắt đầu bằng trừ trung bình từng cột. Sắp các trục theo trị riêng giảm dần. Nộp [trung bình cột, ma trận có k trục theo cột, tỷ lệ phương sai của mỗi trục]. Mỗi tỷ lệ dùng tổng phương sai của tất cả các trục. Hai hướng ngược nhau trên cùng một trục đều hợp lệ.

Tiên quyết · ML02

### A · Dự đoán

1. Bộ mẫu trải rộng hơn theo tọa độ nào? Trục đầu tiên có mấy phần tử?
2. Ghi trung bình, một vectơ đơn vị cho trục đầu và tỷ lệ phương sai tương ứng.

### B · Chạy mẫu

```python
import numpy as np

def pca_fit(X, k):
    X = np.asarray(X, dtype=float)
    mu = X.mean(axis=0)
    C = X - mu
    eig, U = np.linalg.eigh(C.T @ C / (len(X) - 1))
    eig = eig[::-1].clip(min=0)
    ratios = eig[:k] / eig.sum() if eig.sum() else np.zeros(k)
    return (mu, U[:, ::-1][:, :k], ratios)

X = [[-2, 0], [2, 0], [0, -1], [0, 1]]
k = 1
print(pca_fit(X, k))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml25)

### C · Lần theo mã

1. Đổi dấu một vectơ riêng có thay đổi đường thẳng mà nó biểu diễn không? Hãy kiểm tra độ dài của vectơ.
2. So tổng độ lệch bình phương theo hai trục với hai trị riêng. Vì sao hệ số chia n − 1 triệt tiêu trong tỷ lệ?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay X rồi giải lại đề lõi.  
**D1** · `X = [[-1,0],[1,0],[0,-2],[0,2]]  k = 1`

Thay X rồi giải lại đề lõi.  
**D2** · `X = [[1,1],[5,1],[3,0],[3,2]]  k = 1`

Thay k rồi giải lại đề lõi.  
**D3** · `X = [[-2,0],[2,0],[0,-1],[0,1]]  k = 2`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X = [[-3,0],[3,0],[0,-1],[0,1]]  k = 1`  
Kết quả tự nộp ____________________

**E2** · `X = [[1,0],[3,2],[5,4]]  k = 1`  
Kết quả tự nộp ____________________

**E3** · `X = [[1,-1],[3,-1],[2,-4],[2,2]]  k = 1`  
Kết quả tự nộp ____________________

**E4** · `X = [[-2,1],[4,1],[1,-1],[1,3]]  k = 2`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `pca_fit(X, k)`. Nhận train 2D hữu hạn, ít nhất hai hàng và một cột, k nguyên trong [1,d]. Trả (mu, U_top, ratios), các cột U_top sắp theo eigenvalue giảm dần. Ratios dùng tổng phương sai của mọi thành phần. Nếu tổng bằng 0, trả các ratio bằng 0. Kiểm theo projector để chấp nhận cả hai dấu hợp lệ. [Tệp điền mã](../../thuc-hanh/ML25.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X = [[-4,0],[4,0],[0,-1],[0,1]]  k = 1`  
Kết quả tự nộp ____________________

**R2** · `X = [[-1,3],[1,1],[3,-1]]  k = 1`  
Kết quả tự nộp ____________________

**R3** · `X = [[2,2],[4,2],[3,-2],[3,6]]  k = 1`  
Kết quả tự nộp ____________________

**R4** · `X = [[0,-1],[4,-1],[2,-2],[2,0]]  k = 2`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Sau khi khớp PCA với X = [[−2,0],[2,0],[0,1],[0,−1]], hãy dùng một trục đầu để chiếu rồi dựng lại điểm [1,3]. Nộp điểm dựng lại.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML25](#kiem-lai-ml25)

Ôn cùng thao tác · [ML25-practice-1](#ml25-practice-1) · [ML25-practice-2](#ml25-practice-2)


<a id="ml26"></a>

## ML26 · Tìm điểm chia Gini tốt nhất

Với một đặc trưng x và nhãn nhị phân y, thử trung điểm của từng cặp giá trị x phân biệt liền nhau. Đưa x ≤ ngưỡng sang trái. Tính mức giảm độ hỗn tạp Gini (Gini impurity) có tính trọng số hai nhánh. Nộp [ngưỡng, mức giảm]. Hòa trong 10⁻¹² thì lấy ngưỡng nhỏ. Ghi null nếu mức giảm lớn nhất không vượt 10⁻¹².

Tiên quyết · ML01

### A · Dự đoán

1. Có bao nhiêu trung điểm cần thử? Ngưỡng nào tách hai lớp của mẫu thành hai nhánh thuần?
2. Nộp [ngưỡng,mức giảm] của lượt B. Tính Gini nút cha trước khi so các nhánh.

### B · Chạy mẫu

```python
import numpy as np

def best_gini_split(x, y):
    x, y = (np.asarray(x, dtype=float), np.asarray(y))

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
        gain = parent - (left.sum() * gini(y[left]) + (~left).sum() * gini(y[~left])) / len(y)
        if gain > 1e-12 and (best is None or gain > best[1] + 1e-12):
            best = (float(t), float(gain))
    return best

x = [0, 1, 2, 3]
y = [0, 0, 1, 1]
print(best_gini_split(x, y))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml26)

### C · Lần theo mã

1. Vì sao cần nhân độ hỗn tạp mỗi nhánh với tỷ lệ số mẫu của nhánh đó?
2. Tính mức giảm của ngưỡng nhỏ nhất rồi so nó với ngưỡng bạn đã chọn.

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay x rồi giải lại đề lõi.  
**D1** · `x = [0,2,4,6]  y = [0,0,1,1]`

Thay y rồi giải lại đề lõi.  
**D2** · `x = [0,1,2,3]  y = [1,0,0,1]`

Thay y rồi giải lại đề lõi.  
**D3** · `x = [0,1,2,3]  y = [0,1,1,1]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `x = [1,2,4,7]  y = [0,1,1,1]`  
Kết quả tự nộp ____________________

**E2** · `x = [0,2,4]  y = [0,1,0]`  
Kết quả tự nộp ____________________

**E3** · `x = [1,1,3,5]  y = [0,0,1,1]`  
Kết quả tự nộp ____________________

**E4** · `x = [2,4,8]  y = [1,1,1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `best_gini_split(x, y)`. Nhận vectơ x hữu hạn và vectơ y nhị phân cùng độ dài dương. Thử các điểm giữa hai giá trị x phân biệt liền nhau. Trả (ngưỡng, mức giảm) dương lớn nhất, hòa lấy ngưỡng nhỏ. Dùng dung sai 10⁻¹² khi so các gain. Nếu không có gain vượt dung sai, trả None. Báo ValueError nếu đầu vào sai. [Tệp điền mã](../../thuc-hanh/ML26.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `x = [-2,0,3,6]  y = [1,1,0,0]`  
Kết quả tự nộp ____________________

**R2** · `x = [1,3,5]  y = [1,0,1]`  
Kết quả tự nộp ____________________

**R3** · `x = [0,2,2,7]  y = [0,1,1,1]`  
Kết quả tự nộp ____________________

**R4** · `x = [3,6,9]  y = [0,1,1]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Đổi tiêu chí từ Gini sang entropy cơ số 2. Trên x = [0,1,2,3], y = [0,0,1,1], tính ngưỡng và mức giảm theo cả hai cách.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML26](#kiem-lai-ml26)

Ôn cùng thao tác · [ML26-practice-4](#ml26-practice-4) · [ML26-practice-9](#ml26-practice-9)


<a id="ml27"></a>

## ML27 · Gộp phiếu từ các cây chưa thấy mẫu

Với mỗi hàng i, tìm các cây đã bỏ hàng ấy ra ngoài khi lấy mẫu có hoàn lại (out-of-bag, OOB). Đọc cột i của votes và chỉ đếm phiếu của những cây vừa tìm được. Nộp vectơ nhãn theo thứ tự hàng. Nếu hòa phiếu, lấy 0. Nếu mọi cây đều đã thấy hàng i, ghi −1.

Tiên quyết · ML26

### A · Dự đoán

1. Hàng 0 vắng mặt trong mẫu của cây nào? Cột nào trong votes chứa phiếu cho hàng 0?
2. Tự lập vectơ ba nhãn. Đánh dấu riêng các hàng chưa có cây nào đủ điều kiện.

### B · Chạy mẫu

```python
import numpy as np

def oob_vote(bags, votes, n):
    bags, votes = (np.asarray(bags), np.asarray(votes))
    oob = np.ones(bags.shape, dtype=bool)
    oob[np.arange(len(bags))[:, None], bags] = False
    count = oob.sum(axis=0)
    ones = (oob * votes).sum(axis=0)
    return np.where(count == 0, -1, (2 * ones > count).astype(int))

bags = [[0, 0, 2], [1, 1, 2], [0, 1, 2]]
votes = [[1, 1, 1], [1, 1, 0], [0, 0, 0]]
n = 3
print(oob_vote(bags, votes, n))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml27)

### C · Lần theo mã

1. Ghi hai trường hợp có thể làm số phiếu 1 bằng 0. Khi nào nhãn là −1?
2. Ở hàng 2, thử đếm tất cả cây. Vì sao phép tính ấy trả được một nhãn dù phiếu OOB phải ghi −1?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay bags rồi giải lại đề lõi.  
**D1** · `bags = [[0,2,2],[0,0,1],[1,2,2]]  votes = [[1,1,1],[1,1,0],[0,0,0]]  n = 3`

Thay votes rồi giải lại đề lõi.  
**D2** · `bags = [[0,0,2],[1,1,2],[0,1,2]]  votes = [[0,0,1],[1,0,1],[1,1,0]]  n = 3`

Thay votes rồi giải lại đề lõi.  
**D3** · `bags = [[0,0,2],[1,1,2],[0,1,2]]  votes = [[1,1,0],[0,0,1],[1,0,1]]  n = 3`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `bags = [[0,0],[1,1]]  votes = [[1,0],[1,0]]  n = 2`  
Kết quả tự nộp ____________________

**E2** · `bags = [[0,0],[0,0],[0,1]]  votes = [[1,1],[1,0],[1,1]]  n = 2`  
Kết quả tự nộp ____________________

**E3** · `bags = [[1,2,2],[0,2,2]]  votes = [[0,1,1],[1,1,0]]  n = 3`  
Kết quả tự nộp ____________________

**E4** · `bags = [[0,1,2],[0,1,2]]  votes = [[1,1,0],[0,1,0]]  n = 3`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `oob_vote(bags, votes, n)`. bags là ma trận B×n các chỉ số bootstrap 0..n−1. votes là ma trận B×n nhãn dự đoán 0/1 của mỗi cây trên n hàng train. Với mỗi hàng, chỉ gộp phiếu từ cây mà hàng là OOB, hòa lấy 0. Trả vectơ nhãn, dùng −1 nếu chưa có cây OOB. Báo ValueError nếu miền hoặc kích thước sai. [Tệp điền mã](../../thuc-hanh/ML27.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `bags = [[1,1],[0,0]]  votes = [[0,1],[0,1]]  n = 2`  
Kết quả tự nộp ____________________

**R2** · `bags = [[1,1],[1,1],[0,1]]  votes = [[1,1],[0,1],[1,1]]  n = 2`  
Kết quả tự nộp ____________________

**R3** · `bags = [[0,0,1],[1,2,2]]  votes = [[1,0,1],[0,1,0]]  n = 3`  
Kết quả tự nộp ____________________

**R4** · `bags = [[0,1],[1,0]]  votes = [[1,0],[1,1]]  n = 2`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Trên bộ B, gộp phiếu của mọi cây rồi so với kết quả OOB. Giải thích riêng hàng 2 và chỉ ra vì sao một hàng có thể thiếu nhãn OOB.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML27](#kiem-lai-ml27)

Ôn cùng thao tác · [ML27-practice-4](#ml27-practice-4) · [ML27-practice-7](#ml27-practice-7)


<a id="ml28"></a>

## ML28 · Chuẩn hóa, dự đoán và đo MAE

Trong chuỗi xử lý hồi quy (regression pipeline), tính trung bình và độ lệch chuẩn tổng thể trên tập huấn luyện. Với cột hằng, dùng mẫu số 1. Dùng các thống kê ấy cho cả hai tập, khớp bình phương tối thiểu có hệ số tự do trên tập huấn luyện rồi nộp [vectơ dự đoán tập kiểm tra, MAE trên tập kiểm tra].

Tiên quyết · ML03, ML07, ML09, ML13, ML15

### A · Dự đoán

1. Ba điểm huấn luyện nằm trên đường thẳng nào? Giá trị đầu tiên trong tập kiểm tra sẽ có dự đoán gì?
2. Nộp hai dự đoán và MAE của chúng. Tách riêng giá trị mô hình dự đoán với nhãn dùng để chấm.

### B · Chạy mẫu

```python
import numpy as np

def regression_pipeline(X_train, y_train, X_test, y_test):
    X_train, y_train, X_test, y_test = (np.asarray(v, dtype=float) for v in (X_train, y_train, X_test, y_test))
    mu = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    scale = np.where(std == 0, 1, std)
    train = np.column_stack([np.ones(len(X_train)), (X_train - mu) / scale])
    test = np.column_stack([np.ones(len(X_test)), (X_test - mu) / scale])
    pred = test @ np.linalg.lstsq(train, y_train, rcond=None)[0]
    return (pred, float(np.abs(pred - y_test).mean()))

X_train = [[0], [2], [4]]
y_train = [1, 5, 9]
X_test = [[6], [8]]
y_test = [13, 16]
print(regression_pipeline(X_train, y_train, X_test, y_test))
```

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-ml28)

### C · Lần theo mã

1. Những dòng nào chỉ được đọc tập huấn luyện? Đến bước nào mới cần nhãn của tập kiểm tra?
2. Giữ nguyên X_test và thay một nhãn y_test. Thành phần nào của đầu ra có thể đổi?

### D · Thử ba thay đổi

Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.

Thay y_train rồi giải lại đề lõi.  
**D1** · `X_train = [[0],[2],[4]]  y_train = [0,2,4]  X_test = [[6],[8]]  y_test = [13,16]`

Thay y_test rồi giải lại đề lõi.  
**D2** · `X_train = [[0],[2],[4]]  y_train = [1,5,9]  X_test = [[6],[8]]  y_test = [14,15]`

Thay X_test rồi giải lại đề lõi.  
**D3** · `X_train = [[0],[2],[4]]  y_train = [1,5,9]  X_test = [[5],[9]]  y_test = [13,16]`

### E · Tự giải và viết hàm

Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu. Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối 10⁻⁶.

**E1** · `X_train = [[1],[2],[3]]  y_train = [3,5,7]  X_test = [[4],[5]]  y_test = [8,12]`  
Kết quả tự nộp ____________________

**E2** · `X_train = [[0],[2],[4]]  y_train = [1,3,5]  X_test = [[8],[10]]  y_test = [8,12]`  
Kết quả tự nộp ____________________

**E3** · `X_train = [[-1],[0],[1]]  y_train = [-1,2,5]  X_test = [[2],[3]]  y_test = [9,10]`  
Kết quả tự nộp ____________________

**E4** · `X_train = [[2],[2]]  y_train = [1,5]  X_test = [[4],[8]]  y_test = [4,1]`  
Kết quả tự nộp ____________________

**Viết mã.** Viết hàm `regression_pipeline(X_train, y_train, X_test, y_test)`. Nhận hai ma trận 2D hữu hạn không rỗng cùng số cột dương và hai vectơ đích hữu hạn tương ứng. Fit Z-score tổng thể trên train (std=0 đổi thành 1), rồi fit least squares có hệ số tự do. Trả (dự đoán test, MAE test). Báo ValueError với đầu vào không hợp lệ. [Tệp điền mã](../../thuc-hanh/ML28.py).

Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.

#### Bộ số để làm lại

**R1** · `X_train = [[0],[1],[2]]  y_train = [3,6,9]  X_test = [[3],[4]]  y_test = [12,16]`  
Kết quả tự nộp ____________________

**R2** · `X_train = [[1],[3],[5]]  y_train = [2,4,6]  X_test = [[9],[11]]  y_test = [9,14]`  
Kết quả tự nộp ____________________

**R3** · `X_train = [[-2],[0],[2]]  y_train = [-2,2,6]  X_test = [[4],[6]]  y_test = [9,15]`  
Kết quả tự nộp ____________________

**R4** · `X_train = [[4],[4]]  y_train = [2,6]  X_test = [[0],[5]]  y_test = [4,3]`  
Kết quả tự nộp ____________________

### F · Vận dụng sau mốc đạt

Chuyển sang phân loại. Cho xác suất [0.1,0.8,0.5], nhãn thực [0,1,0], ngưỡng 0,5 và quy tắc bằng ngưỡng lấy 1. Nộp dự đoán và tỷ lệ đúng, rồi nêu bước tiền xử lý nào vẫn chỉ học từ train.

### Buổi sau · Kiểm lại

Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.

[Mở bộ S của ML28](#kiem-lai-ml28)

Ôn cùng thao tác · [ML28-practice-1](#ml28-practice-1) · [ML28-practice-5](#ml28-practice-5)


<a id="mlp01"></a>

## MLP01 · Mã hóa một thuộc tính phân loại

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp01)

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

**Viết mã.** Viết hàm `encode_categories(train, values)`. Nhận hai list chuỗi, train không rỗng. Trả (list mức phân biệt xếp tăng, ma trận one-hot của values). Mức lạ thành hàng 0, values có thể rỗng. Báo ValueError nếu train rỗng hoặc đầu vào sai chiều. [Tệp điền mã](../../thuc-hanh/MLP01.py).

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

[Mở bộ S của MLP01](#kiem-lai-mlp01)


<a id="mlp02"></a>

## MLP02 · Lọc cột theo phương sai

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp02)

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

**Viết mã.** Viết hàm `variance_filter(train, X, cutoff)`. Với train 2D hữu hạn không rỗng và X 2D hữu hạn cùng số cột, giữ cột có phương sai tổng thể > cutoff hữu hạn ≥ 0. Trả (chỉ số cột, X đã chọn), cho phép 0 cột được giữ. Báo ValueError nếu kích thước hoặc cutoff sai. [Tệp điền mã](../../thuc-hanh/MLP02.py).

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

[Mở bộ S của MLP02](#kiem-lai-mlp02)


<a id="mlp03"></a>

## MLP03 · Gộp cụm theo khoảng cách gần nhất

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp03)

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

**Viết mã.** Viết hàm `linkage_history(X, linkage)`. Trong đề lõi, dùng linkage = 'single'. X là vectơ hữu hạn có ít nhất một mẫu. Trả lịch sử theo quy tắc ở đầu phiếu. Báo ValueError cho dữ liệu hoặc phương pháp không hợp lệ. Bài F bổ sung liên kết đầy đủ. [Tệp điền mã](../../thuc-hanh/MLP03.py).

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

[Mở bộ S của MLP03](#kiem-lai-mlp03)


<a id="mlp04"></a>

## MLP04 · Gán nhãn cụm mật độ trong một chiều

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp04)

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

**Viết mã.** Viết hàm `dbscan_1d(x, eps, min_samples)`. Nhận vectơ 1D hữu hạn, eps hữu hạn không âm, min_samples nguyên dương. Duyệt core theo chỉ số tăng. Với mỗi core chưa nhãn, mở rộng qua các core kề, gán lân cận chưa nhãn vào cụm hiện tại. Nhãn cụm bắt đầu từ 0, nhiễu −1. Trả vectơ nhãn và báo ValueError nếu miền sai. [Tệp điền mã](../../thuc-hanh/MLP04.py).

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

[Mở bộ S của MLP04](#kiem-lai-mlp04)


<a id="mlp05"></a>

## MLP05 · Tính tổn thất bản lề và mục tiêu SVM

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp05)

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

**Viết mã.** Viết hàm `svm_objective(X, y, w, b, C)`. Với ma trận n×d, n,d dương, y thuộc {−1,1}, vectơ w đúng d, C hữu hạn dương, trả (hinge từng mẫu, 0.5·||w||²+C·tổng hinge). Báo ValueError nếu kích thước, nhãn hoặc C sai. [Tệp điền mã](../../thuc-hanh/MLP05.py).

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

[Mở bộ S của MLP05](#kiem-lai-mlp05)


<a id="mlp06"></a>

## MLP06 · Dựng lại dữ liệu bằng SVD

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp06)

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

**Viết mã.** Viết hàm `svd_reconstruct(X, k)`. Nhận ma trận 2D hữu hạn có n,d dương, k nguyên trong [0,min(n,d)]. Trả (ma trận dựng lại hạng k sau khi trừ tâm và cộng lại trung bình, SSE). Với k=0, dựng lại từng hàng bằng mean. Báo ValueError nếu miền sai. [Tệp điền mã](../../thuc-hanh/MLP06.py).

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

[Mở bộ S của MLP06](#kiem-lai-mlp06)


<a id="mlp07"></a>

## MLP07 · Cập nhật một bước của bản đồ tự tổ chức

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp07)

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

**Viết mã.** Viết hàm `som_step(weights, x, lr, radius)`. weights là ma trận (số node, số đặc trưng) hữu hạn không rỗng, x là vectơ tương ứng. Các node nằm trên lưới 1D theo chỉ số. Chọn winner bằng Euclid, hòa lấy chỉ số nhỏ. Cập nhật node cách winner ≤ radius nguyên không âm với lr trong [0,1]. Trả (winner, weights mới), báo ValueError nếu miền sai. [Tệp điền mã](../../thuc-hanh/MLP07.py).

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

[Mở bộ S của MLP07](#kiem-lai-mlp07)


<a id="mlp08"></a>

## MLP08 · Đo độ tách cụm bằng Davies–Bouldin

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

Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B](#dap-an-mlp08)

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

**Viết mã.** Viết hàm `davies_bouldin_1d(x, labels)`. Với x 1D hữu hạn, labels nguyên cùng kích thước, có 2..n−1 cụm và mọi tâm phân biệt, trả một giá trị DB dùng khoảng cách tuyệt đối. Độ phân tán là trung bình khoảng cách tới tâm. Báo ValueError khi kích thước, số cụm hoặc tâm sai điều kiện. [Tệp điền mã](../../thuc-hanh/MLP08.py).

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

[Mở bộ S của MLP08](#kiem-lai-mlp08)


<a id="on-ml01"></a>

## Ôn tập ML01

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml01-mcq-1"></a>

### ML01-mcq-1

Ma trận X = [[40,2],[55,3],[70,4]] có kích thước (shape) nào?

- A · (2, 3)
- B · (3, 2)
- C · (6,)

<a id="ml01-mcq-2"></a>

### ML01-mcq-2

Chọn biểu thức lấy cột số 1 của X trên tất cả các hàng. Chỉ số đầu là 0.

- A · X[1, :]
- B · X[:, 1]
- C · X[0, 1]

<a id="ml01-mcq-3"></a>

### ML01-mcq-3

Nếu X có kích thước (n,d), thêm một cột hệ số tự do sẽ cho kích thước nào?

- A · (n+1,d)
- B · (n,d+1)
- C · (d,n)

<a id="ml01-mcq-4"></a>

### ML01-mcq-4

Một mẫu được mô tả bằng bốn số thực. Vectơ của mẫu thuộc không gian nào?

- A · R⁴
- B · Rᴺ với N là số mẫu
- C · R¹ vì chỉ có một mẫu

<a id="ml01-mcq-5"></a>

### ML01-mcq-5

X có kích thước (6,2), mỗi hàng là một mẫu. X[2] lấy phần nào của bảng?

- A · Đặc trưng thứ ba của mọi mẫu
- B · Vectơ hai thuộc tính của mẫu thứ ba
- C · Hai mẫu đầu tiên

<a id="ml01-mcq-6"></a>

### ML01-mcq-6

Dùng phép cắt nào để lấy cột đầu của X mà vẫn giữ kích thước (6,1)?

- A · X[:,0]
- B · X[0,:]
- C · X[:,0:1]

<a id="ml01-mcq-7"></a>

### ML01-mcq-7

Sáu mẫu, mỗi mẫu có hai đặc trưng, đang được lưu trong ma trận (2,6). Phép nào đưa mỗi mẫu về một hàng?

- A · X.T
- B · X.flatten()
- C · Giữ nguyên vì đều có 12 số

<a id="ml01-mcq-8"></a>

### ML01-mcq-8

Điều gì xảy ra nếu đổi chỗ hai cột x₁ và x₂ nhưng giữ tên cột ở vị trí cũ?

- A · Số mẫu tự tăng
- B · Giá trị được hiểu thành sai thuộc tính
- C · Không có vấn đề vì kích thước không đổi

<a id="ml01-mcq-9"></a>

### ML01-mcq-9

Để ghép một cột toàn 1 vào X có kích thước (6,2) bằng np.hstack, bạn cần tạo mảng số 1 có kích thước nào?

- A · (6,)
- B · (1,6)
- C · (6,1)

<a id="ml01-mcq-10"></a>

### ML01-mcq-10

Từ kích thước (0,2), bạn còn biết được điều gì về cấu trúc của bảng X?

- A · Định nghĩa hai cột đặc trưng nhưng không có hàng quan sát
- B · Có hai mẫu
- C · Không có số chiều

<a id="ml01-practice-1"></a>

### ML01-practice-1

X có tám mẫu và ba đặc trưng cho mỗi mẫu. Hãy ghi kích thước và giải thích ý nghĩa hai trục.

<a id="ml01-practice-2"></a>

### ML01-practice-2

Với X = [[40,2],[55,3],[70,4]], viết lệnh lấy mẫu thứ hai. Hai số thu được đến từ hàng nào?

<a id="ml01-practice-3"></a>

### ML01-practice-3

Lấy cột đầu của X = [[40,2],[55,3],[70,4]]. Ghi các giá trị và kích thước của vectơ.

<a id="ml01-practice-4"></a>

### ML01-practice-4

X có ba hàng và hai cột. Vì sao X[:,0] và X[:,0:1] chứa cùng giá trị nhưng khác kích thước?

<a id="ml01-practice-5"></a>

### ML01-practice-5

Thêm một cột toàn 1 bên trái X = [[40,2],[55,3]]. In cả bảng lẫn kích thước mới.

<a id="ml01-practice-6"></a>

### ML01-practice-6

Hai điểm (30,6) và (25,3) cách nhau bao xa theo Euclid? Làm tròn đến bốn chữ số thập phân.

<a id="ml01-practice-7"></a>

### ML01-practice-7

Với (30,6) và (25,3), tính phần đóng góp của tọa độ đầu vào bình phương khoảng cách. Liên hệ kết quả với đơn vị đo.

<a id="ml01-practice-8"></a>

### ML01-practice-8

So sánh kích thước np.array([40,2]) và np.array([[40,2]]). Mảng nào giữ một hàng mẫu rõ ràng?

<a id="ml01-practice-9"></a>

### ML01-practice-9

Chuyển vị ma trận (4,3) rồi ghi kích thước và số phần tử. Số mẫu quan sát ban đầu có tăng không?

<a id="ml01-practice-10"></a>

### ML01-practice-10

Cho ví dụ về hai bảng cùng kích thước (6,2) nhưng ý nghĩa của các cột khác nhau.

<a id="ml01-practice-11"></a>

### ML01-practice-11

Viết phép cắt lấy hai hàng cuối của X = [[40,2],[55,3],[70,4]] với đủ hai cột. Kết quả có kích thước nào?

<a id="ml01-practice-12"></a>

### ML01-practice-12

Một bạn thêm cột hệ số tự do vào X có kích thước (5,2) nhưng thu được (6,2). Bạn ấy đã ghép theo trục nào?


<a id="on-ml02"></a>

## Ôn tập ML02

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml02-mcq-1"></a>

### ML02-mcq-1

Ô C[j,j] trên đường chéo của ma trận hiệp phương sai cho biết đại lượng nào của cột j?

- A · Trung bình cột j
- B · Phương sai mẫu của cột j
- C · Số mẫu n

<a id="ml02-mcq-2"></a>

### ML02-mcq-2

Khi đã ước lượng trung bình từ n mẫu, vì sao hiệp phương sai mẫu chia cho n − 1?

- A · Để đổi đơn vị dữ liệu
- B · Lấy trung bình từ chính n mẫu làm mất một bậc tự do
- C · Để mọi hiệp phương sai nằm trong [-1,1]

<a id="ml02-mcq-3"></a>

### ML02-mcq-3

Tính chất nào luôn đúng với một ma trận hiệp phương sai mẫu hợp lệ?

- A · Đối xứng và PSD
- B · Mọi phần tử đều dương
- C · Định thức luôn bằng 1

<a id="ml02-mcq-4"></a>

### ML02-mcq-4

Bảng có năm mẫu và ba thuộc tính. Ma trận hiệp phương sai giữa các thuộc tính có kích thước nào?

- A · (5,5)
- B · (3,3)
- C · (5,3)

<a id="ml02-mcq-5"></a>

### ML02-mcq-5

Với hai giá trị 1 và 3, phương sai mẫu bằng bao nhiêu?

- A · 1
- B · 4
- C · 2

<a id="ml02-mcq-6"></a>

### ML02-mcq-6

Một dãy tăng [1,2,3] đi cùng dãy giảm [3,2,1]. Hiệp phương sai mẫu mang dấu nào?

- A · Âm
- B · Dương
- C · Luôn bằng 0 vì trung bình bằng nhau

<a id="ml02-mcq-7"></a>

### ML02-mcq-7

Nếu cộng 100 vào mọi phần tử của một cột, hiệp phương sai mẫu có thay đổi không?

- A · Có, tăng 100
- B · Không, nếu các cột và mẫu còn lại giữ nguyên
- C · Hiệp phương sai luôn thành 0

<a id="ml02-mcq-8"></a>

### ML02-mcq-8

Một cột chỉ chứa giá trị 7. Phương sai của nó và hiệp phương sai với cột khác bằng bao nhiêu?

- A · Phương sai 7 và hiệp phương sai 7
- B · Không xác định dù có ít nhất hai mẫu
- C · Đều bằng 0

<a id="ml02-mcq-9"></a>

### ML02-mcq-9

Sau khi trừ trung bình riêng của từng cột, tổng các phần tử trong mỗi cột bằng bao nhiêu?

- A · 0
- B · Số mẫu n
- C · Trung bình ban đầu

<a id="ml02-mcq-10"></a>

### ML02-mcq-10

Có ba mẫu. Bạn chia tổng tích các độ lệch cho số nào để lấy hiệp phương sai mẫu?

- A · 2
- B · 3
- C · Số đặc trưng bất kỳ

<a id="ml02-practice-1"></a>

### ML02-practice-1

Tính vectơ trung bình cột của X = [[1,4],[3,8]].

<a id="ml02-practice-2"></a>

### ML02-practice-2

Từ X = [[1,4],[3,8]], trừ trung bình từng cột và ghi ma trận kết quả.

<a id="ml02-practice-3"></a>

### ML02-practice-3

Lấy [1,3] làm hai quan sát. Tính phương sai với mẫu số n − 1.

<a id="ml02-practice-4"></a>

### ML02-practice-4

Tính hiệp phương sai mẫu của hai cột x = [1,3] và y = [4,8].

<a id="ml02-practice-5"></a>

### ML02-practice-5

Lập toàn bộ ma trận hiệp phương sai mẫu của X = [[1,4],[3,8]].

<a id="ml02-practice-6"></a>

### ML02-practice-6

Tính hiệp phương sai mẫu cho x = [1,2,3] và y = [3,2,1].

<a id="ml02-practice-7"></a>

### ML02-practice-7

Dùng công thức tổng tích độ lệch để giải thích vì sao C[i,j] bằng C[j,i].

<a id="ml02-practice-8"></a>

### ML02-practice-8

Điều gì xảy ra với mẫu số n − 1 khi bảng chỉ có một hàng?

<a id="ml02-practice-9"></a>

### ML02-practice-9

Tính phương sai mẫu của cột x = [7,7,7].

<a id="ml02-practice-10"></a>

### ML02-practice-10

Cộng cùng c vào mọi phần tử của một cột. Hãy dùng độ lệch so với trung bình mới để chứng minh hiệp phương sai giữ nguyên.

<a id="ml02-practice-11"></a>

### ML02-practice-11

Nhân một cột với 2 và giữ nguyên cột kia. Phương sai của cột thứ nhất và hiệp phương sai giữa hai cột thay đổi bao nhiêu lần?

<a id="ml02-practice-12"></a>

### ML02-practice-12

C = [[2,−1],[−1,2]] có hai ô âm. Chỉ dấu của các ô đó đã đủ để bác bỏ tính nửa xác định dương chưa?


<a id="on-ml03"></a>

## Ôn tập ML03

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml03-mcq-1"></a>

### ML03-mcq-1

Khi chuẩn hóa cực tiểu–cực đại, bạn học min và max từ phần dữ liệu nào?

- A · Toàn bộ tập huấn luyện và tập kiểm tra
- B · Chỉ tập huấn luyện
- C · Chỉ tập kiểm tra

<a id="ml03-mcq-2"></a>

### ML03-mcq-2

Tập huấn luyện có trung bình 50 và độ lệch chuẩn 10. Điểm chuẩn hóa Z của giá trị kiểm tra 70 là bao nhiêu?

- A · 2
- B · 0.2
- C · 70

<a id="ml03-mcq-3"></a>

### ML03-mcq-3

Trong trường hợp nào chuẩn hóa theo tập huấn luyện có thể đưa giá trị kiểm tra ra ngoài [0,1]?

- A · Khi tập kiểm tra nằm ngoài khoảng tập huấn luyện
- B · Không bao giờ
- C · Chỉ khi dùng Z-điểm

<a id="ml03-mcq-4"></a>

### ML03-mcq-4

Dùng tập huấn luyện [10,20] để chuẩn hóa cực tiểu–cực đại cho giá trị 5. Kết quả bằng bao nhiêu?

- A · −0.5
- B · 0
- C · 0.5

<a id="ml03-mcq-5"></a>

### ML03-mcq-5

Với z = (x − mean)/std, mean = 8 và std = 2, giá trị x = 8 được biến đổi thành gì?

- A · 1
- B · 0
- C · 8

<a id="ml03-mcq-6"></a>

### ML03-mcq-6

Vì sao phải có quy ước riêng cho cột huấn luyện chỉ chứa một giá trị khi chuẩn hóa cực tiểu–cực đại?

- A · Vì có quá nhiều mẫu
- B · Vì max luôn âm
- C · Vì max−min bằng 0

<a id="ml03-mcq-7"></a>

### ML03-mcq-7

Khi chuẩn hóa độc lập từng cột, các thống kê của một đặc trưng được tính ở đâu?

- A · Mỗi thuộc tính dùng thống kê của chính cột tập huấn luyện đó
- B · Mỗi hàng dùng min và max riêng
- C · Mọi cột luôn dùng chung một khoảng

<a id="ml03-mcq-8"></a>

### ML03-mcq-8

So sánh công thức (x − mean)/max dùng trong bài với công thức chuẩn hóa cực tiểu–cực đại. Chúng khác nhau ở đâu?

- A · Hai công thức luôn giống nhau
- B · Dùng trung bình ở tử và max ở mẫu, thay vì min và max−min
- C · Chỉ khác tên biến

<a id="ml03-mcq-9"></a>

### ML03-mcq-9

Lô kiểm tra mới có trung bình khác tập huấn luyện. Bạn dùng bộ trung bình và độ lệch chuẩn nào để biến đổi lô ấy?

- A · Tính lại trung bình/std từ lô tập kiểm tra
- B · Ghép tập huấn luyện và tập kiểm tra rồi tính lại
- C · Giữ trung bình/std tập huấn luyện để biến đổi lô tập kiểm tra

<a id="ml03-mcq-10"></a>

### ML03-mcq-10

Tập huấn luyện là [10,20] và tập kiểm tra chỉ có [30]. Nếu tính min và max riêng trên tập kiểm tra, mẫu số sẽ ra sao?

- A · Khoảng tập kiểm tra bằng 0 và còn sai quy trình khớp mô hình bộ chuẩn hóa
- B · Kết quả đúng bắt buộc là 2
- C · Bảo đảm không có rò rỉ dữ liệu

<a id="ml03-practice-1"></a>

### ML03-practice-1

Lấy min và max từ [10,20], rồi biến đổi lần lượt 15 và 30.

<a id="ml03-practice-2"></a>

### ML03-practice-2

Dùng khoảng huấn luyện [−10,10] để chuẩn hóa ba giá trị [−20,0,20].

<a id="ml03-practice-3"></a>

### ML03-practice-3

Với trung bình 50 và độ lệch chuẩn 10 trên tập huấn luyện, tính điểm Z cho [40,50,70].

<a id="ml03-practice-4"></a>

### ML03-practice-4

Dùng từng cột của train = [[0,10],[10,30]] để chuẩn hóa cực tiểu–cực đại cho [[5,20]].

<a id="ml03-practice-5"></a>

### ML03-practice-5

Một giá trị kiểm tra vượt cực đại huấn luyện. Giải thích vì sao kết quả chuẩn hóa lớn hơn 1 vẫn có thể đúng.

<a id="ml03-practice-6"></a>

### ML03-practice-6

Một người tính min và max trên toàn bộ bảng rồi mới chia tập. Dữ liệu kiểm tra đã ảnh hưởng đến bước nào?

<a id="ml03-practice-7"></a>

### ML03-practice-7

Áp dụng đúng công thức (x − mean)/max cho hai giá trị huấn luyện [10,20]. Ghi cả hai kết quả.

<a id="ml03-practice-8"></a>

### ML03-practice-8

Trên cùng [10,20], hãy tính và so sánh hai kết quả của công thức cực tiểu–cực đại và công thức (x − mean)/max.

<a id="ml03-practice-9"></a>

### ML03-practice-9

Hãy thay min và max của [4,4,4] vào công thức để chỉ ra chỗ phép chia mất nghĩa.

<a id="ml03-practice-10"></a>

### ML03-practice-10

Điều gì xảy ra khi tính điểm Z cho một cột có độ lệch chuẩn huấn luyện bằng 0?

<a id="ml03-practice-11"></a>

### ML03-practice-11

Tập huấn luyện có hai đặc trưng nhưng mẫu mới có ba. Vì sao cần kiểm tra số cột trước khi cho NumPy tự mở rộng kích thước?

<a id="ml03-practice-12"></a>

### ML03-practice-12

Từ tập huấn luyện [0,4], chuẩn hóa độc lập hai lô [2] và [6] bằng cùng các thống kê. Ghi kết quả mỗi lô.


<a id="on-ml04"></a>

## Ôn tập ML04

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml04-mcq-1"></a>

### ML04-mcq-1

Với a = 0.08, b = 0, x = [20,40] và y = [1.6,3.2], tổn thất E bằng bao nhiêu?

- A · 0
- B · 0.5
- C · 3.2

<a id="ml04-mcq-2"></a>

### ML04-mcq-2

Hệ số 1/2 trong tổn thất bình phương giúp phép tính đạo hàm đơn giản ở đâu?

- A · Đổi đơn vị
- B · Triệt tiêu hệ số 2 khi đạo hàm
- C · Đảm bảo E âm

<a id="ml04-mcq-3"></a>

### ML04-mcq-3

Khi ma trận thiết kế thiếu hạng, các bộ hệ số tối ưu có thể có tính chất nào?

- A · Nhiều theta cùng tối ưu
- B · MSE luôn âm
- C · Mọi dự đoán đều khác nhau

<a id="ml04-mcq-4"></a>

### ML04-mcq-4

Với dự đoán 0.08x, x = 20 và y = 2, phần dư dự đoán trừ thực tế bằng bao nhiêu?

- A · −0.4
- B · 0.4
- C · 1.6

<a id="ml04-mcq-5"></a>

### ML04-mcq-5

Có một mẫu với phần dư −2. Tính E = Σe²/(2m).

- A · −2
- B · 2
- C · 4

<a id="ml04-mcq-6"></a>

### ML04-mcq-6

Nếu mọi phần dư cùng bằng 0, điều gì chắc chắn đúng trên các mẫu đã xét?

- A · E âm
- B · E không xác định
- C · Mô hình khớp các mẫu đang xét và E=0

<a id="ml04-mcq-7"></a>

### ML04-mcq-7

Đảo dấu toàn bộ phần dư. Giá trị tổn thất bình phương E sẽ thay đổi thế nào?

- A · Không
- B · Có, E đổi dấu
- C · E luôn tăng gấp đôi

<a id="ml04-mcq-8"></a>

### ML04-mcq-8

Trên cùng bộ mẫu, E = Σe²/(2m) bằng bao nhiêu lần MSE = Σe²/m?

- A · Gấp đôi MSE
- B · Bằng một nửa MSE
- C · Bằng MSE trong mọi trường hợp

<a id="ml04-mcq-9"></a>

### ML04-mcq-9

Mô hình đạt E = 0 trên tập huấn luyện. Kết quả nào về dữ liệu mới vẫn còn bỏ ngỏ?

- A · Phần dư tập huấn luyện bằng 0
- B · Training MSE bằng 0
- C · Sai số trên tập kiểm tra cũng bằng 0

<a id="ml04-mcq-10"></a>

### ML04-mcq-10

Hai phần dư [−1,1] có trung bình 0. Tổn thất bình phương của chúng có bằng 0 không?

- A · Không, tổn thất theo 2m bằng 0.5
- B · Có vì sai số triệt tiêu
- C · Không xác định vì có số âm

<a id="ml04-practice-1"></a>

### ML04-practice-1

Với x = 20, y = 2, a = 0.08 và b = 0, lần lượt tính dự đoán và phần dư dự đoán trừ thực tế.

<a id="ml04-practice-2"></a>

### ML04-practice-2

Từ hai phần dư [1,−1], tính E bằng công thức có mẫu số 2m.

<a id="ml04-practice-3"></a>

### ML04-practice-3

Tính E khi x = [20,40], y = [1.6,3.2] và cả a lẫn b đều bằng 0.

<a id="ml04-practice-4"></a>

### ML04-practice-4

Giữ x = [20,40] và y = [1.6,3.2]. Đặt a = 0.08, b = 0 rồi tính E.

<a id="ml04-practice-5"></a>

### ML04-practice-5

Tính E cho mẫu x = 1.5, y = 2.5 trên đường thẳng có a = 1 và b = 1.

<a id="ml04-practice-6"></a>

### ML04-practice-6

Giải thích điều gì xảy ra với bình phương phần dư và với công thức đạo hàm khi đổi quy ước dấu của phần dư.

<a id="ml04-practice-7"></a>

### ML04-practice-7

Tính E của [0,2] và của [1,1]. Hai bộ phần dư cùng trung bình cho kết quả thế nào?

<a id="ml04-practice-8"></a>

### ML04-practice-8

Giữ nguyên hệ số và nhân đôi tập dữ liệu bằng cách lặp mỗi mẫu hai lần. E thay đổi thế nào?

<a id="ml04-practice-9"></a>

### ML04-practice-9

Ba mẫu có tổng bình phương phần dư bằng 12. Tính cả E và MSE.

<a id="ml04-practice-10"></a>

### ML04-practice-10

Chỉ ra bước tính E không xác định trên tập có 0 mẫu.

<a id="ml04-practice-11"></a>

### ML04-practice-11

x có hai phần tử còn y chỉ có một. Vì sao phép tự mở rộng kích thước của NumPy có thể che mất lỗi dữ liệu?

<a id="ml04-practice-12"></a>

### ML04-practice-12

Hàm tổn thất lồi theo a và b. Bạn còn cần biết điều gì về ma trận thiết kế để kết luận nghiệm tối ưu là duy nhất?


<a id="on-ml05"></a>

## Ôn tập ML05

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml05-mcq-1"></a>

### ML05-mcq-1

Một bước hạ gradient trên cả lô dùng bao nhiêu mẫu huấn luyện để tính gradient?

- A · Mẫu đầu
- B · Toàn bộ lô
- C · Không mẫu

<a id="ml05-mcq-2"></a>

### ML05-mcq-2

Tốc độ học quá lớn có thể làm dãy tham số thay đổi thế nào sau nhiều bước?

- A · Phân kỳ
- B · Luôn chính xác hơn
- C · Đổi nhãn

<a id="ml05-mcq-3"></a>

### ML05-mcq-3

Trong một lần cập nhật đồng thời, các gradient phải được tính tại bộ tham số nào?

- A · Mọi theta dùng gradient cũ
- B · Theta0 cập nhật rồi mới tính theta1
- C · Chỉ cập nhật hệ số tự do

<a id="ml05-mcq-4"></a>

### ML05-mcq-4

Với x = [20,40], y = [1.6,3.2], a = b = 0 và E = Σe²/(2m), gradient theo a bằng bao nhiêu?

- A · −80
- B · −2.4
- C · 80

<a id="ml05-mcq-5"></a>

### ML05-mcq-5

Với x = [20,40], y = [1.6,3.2], a = b = 0 và tốc độ học 0.001, b bằng bao nhiêu sau một bước?

- A · −0.0024
- B · 0.0024
- C · 0.08

<a id="ml05-mcq-6"></a>

### ML05-mcq-6

Để cập nhật đồng thời a và b, khi nào bạn được thay giá trị cũ của chúng?

- A · Cập nhật a trước rồi dùng a mới tính d_b
- B · Luôn giữ b bằng 0
- C · Tính cả hai gradient từ cùng tham số cũ

<a id="ml05-mcq-7"></a>

### ML05-mcq-7

Khi toàn bộ gradient bằng 0, một bước với tốc độ học hữu hạn sẽ đưa tham số đến đâu?

- A · Giữ nguyên tham số
- B · Tự giảm tổn thất xuống âm
- C · Đổi ngẫu nhiên trọng số

<a id="ml05-mcq-8"></a>

### ML05-mcq-8

Điều gì có thể xảy ra với tổn thất nếu tốc độ học làm tham số nhảy qua vùng cực tiểu?

- A · Luôn hội tụ nhanh hơn
- B · Vượt quá vùng cải thiện và có thể phân kỳ
- C · Tự biến thành phương trình chuẩn

<a id="ml05-mcq-9"></a>

### ML05-mcq-9

Trong hạ gradient trên cả lô, những quan sát nào góp vào gradient của mỗi bước?

- A · Một mẫu bất kỳ duy nhất
- B · Chỉ mẫu có phần dư lớn nhất
- C · Toàn bộ tập tập huấn luyện đang dùng

<a id="ml05-mcq-10"></a>

### ML05-mcq-10

Mã tính a mới rồi dùng nó để tính gradient theo b. Cách làm ấy có đáp ứng quy tắc cập nhật đồng thời không?

- A · Không
- B · Có vì cả hai được cập nhật
- C · Có nếu alpha nhỏ

<a id="ml05-practice-1"></a>

### ML05-practice-1

Từ x = [20,40], y = [1.6,3.2] và a = b = 0, hãy tính gradient theo từng tham số.

<a id="ml05-practice-2"></a>

### ML05-practice-2

Dùng gradient của x = [20,40], y = [1.6,3.2] tại a = b = 0 và tốc độ học 0.001. Nộp cặp tham số sau một bước.

<a id="ml05-practice-3"></a>

### ML05-practice-3

Từ a = b = 0, thực hiện một bước với x = [20,40], y = [1.6,3.2], tốc độ học 0.001. So hai dự đoán mới với y.

<a id="ml05-practice-4"></a>

### ML05-practice-4

Với x = [1,2], y = [2,3], a = b = 0 và tốc độ học 0.1, tính rồi nộp [a_mới,b_mới].

<a id="ml05-practice-5"></a>

### ML05-practice-5

Với x = [1,2], y = [2,3], a = b = 0 và tốc độ học 0.1, thử tính gradient b bằng a_mới = 0.4. So b thu được với b của phép cập nhật đồng thời.

<a id="ml05-practice-6"></a>

### ML05-practice-6

Cho x = [1,2], y = [2,4], a = 2 và b = 0. Tính gradient và bộ tham số sau một bước.

<a id="ml05-practice-7"></a>

### ML05-practice-7

Tính một bước cho mẫu x = 2, y = 5 với a = 1, b = 1 và tốc độ học 0.1. Nộp [a_mới,b_mới].

<a id="ml05-practice-8"></a>

### ML05-practice-8

Nếu lặp mỗi quan sát hai lần, tổng và trung bình phần dư thay đổi ra sao? Liên hệ với độ dài bước cập nhật.

<a id="ml05-practice-9"></a>

### ML05-practice-9

Giữ gradient [−4,−2.5]. So độ lớn cập nhật khi dùng tốc độ học 0.1 và 0.01.

<a id="ml05-practice-10"></a>

### ML05-practice-10

Sau một lần cập nhật, tổn thất giảm. Bằng chứng đó đã đủ để kết luận hội tụ chưa?

<a id="ml05-practice-11"></a>

### ML05-practice-11

Làm tròn tham số ngay sau mỗi bước khác gì với chỉ làm tròn khi in kết quả?

<a id="ml05-practice-12"></a>

### ML05-practice-12

Từ X = [[1,1],[1,2]], theta = [0,0], y = [2,3] và tốc độ học 0.1, tính theta mới. Ghi rõ vị trí hệ số tự do và hệ số góc.


<a id="on-ml06"></a>

## Ôn tập ML06

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml06-mcq-1"></a>

### ML06-mcq-1

Muốn chia order = [2,0,1] thành các lô tối đa hai phần tử và giữ phần dư, bạn thu được gì?

- A · [[2,0]]
- B · [[2,0],[1]]
- C · [[0,1],[2]]

<a id="ml06-mcq-2"></a>

### ML06-mcq-2

Trường hợp nào khiến việc cắt lô theo size không thể thực hiện đúng quy ước?

- A · size = 1
- B · size = 0
- C · Size lớn hơn số mẫu

<a id="ml06-mcq-3"></a>

### ML06-mcq-3

Bạn cần kiểm tra điều gì ở order trước khi dùng nó làm hoán vị các hàng?

- A · Mọi chỉ số từ 0 đến n − 1 xuất hiện đúng một lần
- B · Các chỉ số đã được sắp tăng
- C · Giá trị đầu tiên bằng 0

<a id="ml06-mcq-4"></a>

### ML06-mcq-4

Mười mẫu, tối đa bốn mẫu mỗi lô và giữ phần dư. Một lượt qua toàn bộ dữ liệu có mấy lô?

- A · 2
- B · 3
- C · 4

<a id="ml06-mcq-5"></a>

### ML06-mcq-5

Để mỗi hàng vẫn đi cùng nhãn của nó, bạn xáo thứ tự X và y như thế nào?

- A · Dùng cùng một permutation chỉ số
- B · Xáo độc lập từng mảng
- C · Chỉ xáo y

<a id="ml06-mcq-6"></a>

### ML06-mcq-6

Tám mẫu được xử lý từng mẫu một với size = 1. Cách lấy gradient này tương ứng với phương pháp nào?

- A · Toàn bộ tám mẫu mỗi bước
- B · Hai mẫu mỗi bước
- C · Một mẫu mỗi bước như SGD

<a id="ml06-mcq-7"></a>

### ML06-mcq-7

Kích thước lô bằng đúng số mẫu. Có mấy lần cập nhật trong một lượt qua tập huấn luyện?

- A · Một
- B · Bằng số mẫu
- C · Không có cập nhật

<a id="ml06-mcq-8"></a>

### ML06-mcq-8

Cố định hạt giống ngẫu nhiên khi tạo hoán vị giúp bạn lặp lại điều gì?

- A · Bảo đảm mô hình tốt hơn
- B · Giúp tái lập thứ tự với cùng môi trường và chuỗi lời gọi
- C · Bảo đảm mỗi lần gọi generator đang tồn tại đều trả cùng permutation

<a id="ml06-mcq-9"></a>

### ML06-mcq-9

Lô cuối chỉ có hai mẫu trong khi các lô trước có bốn. Chia tổng gradient của lô cuối cho số nào?

- A · 4 như cấu hình ban đầu
- B · Tổng số mẫu toàn khóa
- C · 2 là số mẫu thực tế trong lô

<a id="ml06-mcq-10"></a>

### ML06-mcq-10

Với chín mẫu, size = 4 và bỏ lô cuối chưa đủ cỡ, một lượt dùng bao nhiêu mẫu?

- A · 8
- B · 9
- C · 4

<a id="ml06-practice-1"></a>

### ML06-practice-1

Chia 11 mẫu thành các lô tối đa bốn phần tử và giữ phần dư. Liệt kê kích thước từng lô và số lần cập nhật.

<a id="ml06-practice-2"></a>

### ML06-practice-2

Chỉ có năm mẫu trong khi size = 8. Nếu giữ lô cuối, những mẫu nào được dùng?

<a id="ml06-practice-3"></a>

### ML06-practice-3

Lấy idx = [2,0,1], X = [10,20,30] và y = [1,2,3]. Viết hai dãy sau khi cùng lấy theo idx.

<a id="ml06-practice-4"></a>

### ML06-practice-4

Vì sao xáo riêng X và y có thể cho một giá trị tổn thất hợp lệ về kích thước nhưng sai quan hệ mẫu–nhãn?

<a id="ml06-practice-5"></a>

### ML06-practice-5

Cắt idx = [4,1,3,0,2] thành các lô dài tối đa 2. Nộp tất cả các lô theo đúng thứ tự.

<a id="ml06-practice-6"></a>

### ML06-practice-6

Với 12 mẫu, tính số bước trong một lượt khi kích thước lô lần lượt là 12, 3 và 1.

<a id="ml06-practice-7"></a>

### ML06-practice-7

Hai bộ sinh ngẫu nhiên mới dùng cùng hạt giống và cùng gọi permutation(6) lần đầu. So sánh hai kết quả.

<a id="ml06-practice-8"></a>

### ML06-practice-8

Một lô ngắn có hai gradient [2,6]. Tính gradient trung bình rồi cập nhật theta = 1 với tốc độ học 0.1.

<a id="ml06-practice-9"></a>

### ML06-practice-9

Vì sao hàm nên báo lỗi ngay khi size bằng 0?

<a id="ml06-practice-10"></a>

### ML06-practice-10

Phân biệt một lần cập nhật (step) với một lượt duyệt hết dữ liệu (epoch).

<a id="ml06-practice-11"></a>

### ML06-practice-11

Nếu tạo lô bằng hoán vị, bạn sẽ đối chiếu các chỉ số thế nào để phát hiện mẫu bị lặp hoặc bị bỏ?

<a id="ml06-practice-12"></a>

### ML06-practice-12

Vì sao gradient của các lô nhỏ có thể dao động quanh gradient của toàn tập?


<a id="on-ml07"></a>

## Ôn tập ML07

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml07-mcq-1"></a>

### ML07-mcq-1

Trong ma trận thiết kế dùng cho hồi quy có hệ số tự do, bạn đặt cột toàn 1 ở đâu theo quy ước của bài?

- A · Sau hàng cuối của X
- B · Bên trái các cột đặc trưng
- C · Thay cho cột đặc trưng cuối

<a id="ml07-mcq-2"></a>

### ML07-mcq-2

Hai cột của X giống hệt nhau. Cách nào vẫn tìm được nghiệm bình phương tối thiểu có chuẩn nhỏ nhất?

- A · Lấy nghịch đảo trực tiếp của ma trận Gram
- B · Bỏ nhãn của một mẫu
- C · Dùng np.linalg.lstsq trên ma trận thiết kế

<a id="ml07-mcq-3"></a>

### ML07-mcq-3

Trước khi khớp mô hình với X và y, số hàng của X phải khớp với đại lượng nào?

- A · Số cột của X
- B · Số phần tử của y
- C · Số hệ số kể cả hệ số tự do

<a id="ml07-mcq-4"></a>

### ML07-mcq-4

X có kích thước (10,3). Tích X.T @ X có kích thước nào?

- A · (10,10)
- B · (3,3)
- C · (10,3)

<a id="ml07-mcq-5"></a>

### ML07-mcq-5

Điều kiện nào trên các cột của X bảo đảm phương trình chuẩn có nghiệm duy nhất?

- A · X đủ hạng cột
- B · Chỉ cần có nhiều số trong X
- C · Mọi nhãn phải khác nhau

<a id="ml07-mcq-6"></a>

### ML07-mcq-6

Nếu hai cột của X giống hệt nhau, vì sao công thức dùng nghịch đảo của X.T @ X gặp vấn đề?

- A · Luôn có nghịch đảo
- B · Đổi y sẽ làm X.T@X khả nghịch
- C · X không đủ hạng cột, Gram ma trận suy biến

<a id="ml07-mcq-7"></a>

### ML07-mcq-7

Khi cột toàn 1 nằm bên trái ma trận thiết kế, theta[0] ứng với thành phần nào?

- A · Hệ số chặn
- B · Số mẫu
- C · Gradient đầu tiên

<a id="ml07-mcq-8"></a>

### ML07-mcq-8

Khi A khả nghịch, vì sao nên giải hệ bằng solve(A,b) thay vì tạo inv(A) rồi nhân với b?

- A · Để mọi hệ suy biến tự có nghiệm duy nhất
- B · Giải trực tiếp hệ mà không cần tạo nghịch đảo tường minh
- C · Để bỏ qua kiểm tra kích thước

<a id="ml07-mcq-9"></a>

### ML07-mcq-9

Ma trận Gram suy biến. Điều đó cho phép kết luận gì về sự tồn tại của nghiệm bình phương tối thiểu?

- A · Có, mọi trường hợp đều vô nghiệm
- B · Có, vì y luôn không hữu hạn
- C · Không. Vấn đề là tính duy nhất và công thức nghịch đảo

<a id="ml07-mcq-10"></a>

### ML07-mcq-10

X đủ hạng cột có bảo đảm việc giải phương trình chuẩn hoàn toàn ổn định về số không?

- A · Không
- B · Có, mọi phép tính máy là chính xác
- C · Có nếu dùng inv thay solve

<a id="ml07-practice-1"></a>

### ML07-practice-1

X có kích thước (7,3) và y có kích thước (7,). Ghi kích thước của X.T @ y và theta.

<a id="ml07-practice-2"></a>

### ML07-practice-2

Với X = [[1,1],[1,2]], tính ma trận X.T @ X.

<a id="ml07-practice-3"></a>

### ML07-practice-3

Từ X = [[1,1],[1,2]] và y = [2,4], tính vectơ X.T @ y.

<a id="ml07-practice-4"></a>

### ML07-practice-4

Giải phương trình chuẩn của X = [[1,1],[1,2]] và y = [2,4] để tìm hai hệ số.

<a id="ml07-practice-5"></a>

### ML07-practice-5

Khớp hồi quy qua gốc tọa độ cho X = [[2],[4]] và y = [3,6]. Tính hệ số duy nhất.

<a id="ml07-practice-6"></a>

### ML07-practice-6

Xét hạng của X = [[1,2],[2,4]]. Hạng ấy giải thích thế nào cho việc không thể lấy nghịch đảo chuẩn?

<a id="ml07-practice-7"></a>

### ML07-practice-7

Một ma trận hai hàng, ba cột có thể đủ hạng cột không? Giải thích bằng hạng tối đa.

<a id="ml07-practice-8"></a>

### ML07-practice-8

Vì sao so toàn bộ X.shape với y.shape sẽ báo sai dù số mẫu thực sự khớp nhau?

<a id="ml07-practice-9"></a>

### ML07-practice-9

Chỉ ra lỗi trong điều kiện np.linalg.matrix_rank(A) < A.shape. Bạn cần so với kích thước nào?

<a id="ml07-practice-10"></a>

### ML07-practice-10

Thêm cột toàn 1 vào x = [20,40] rồi khớp y = [1.6,3.2]. Ghi hệ số tự do trước hệ số góc.

<a id="ml07-practice-11"></a>

### ML07-practice-11

Nếu đổi chỗ các cột của X nhưng giữ theta theo thứ tự cũ, dự đoán có được bảo toàn không?

<a id="ml07-practice-12"></a>

### ML07-practice-12

Dùng lstsq với một ma trận có hai cột trùng nhau. Giải thích vì sao vẫn tính được dự đoán hữu hạn khi ma trận Gram không khả nghịch.


<a id="on-ml08"></a>

## Ôn tập ML08

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml08-mcq-1"></a>

### ML08-mcq-1

Với một đặc trưng x, hàng nào biểu diễn đầy đủ đa thức bậc hai có hệ số tự do?

- A · [x,x²]
- B · [1,x,x²]
- C · [1,x,2x]

<a id="ml08-mcq-2"></a>

### ML08-mcq-2

Nếu degree bằng 0, bạn cần tạo một hàng như thế nào cho mỗi mẫu?

- A · [1]
- B · [0]
- C · Một hàng rỗng

<a id="ml08-mcq-3"></a>

### ML08-mcq-3

Khi biến đổi dữ liệu kiểm tra, thứ tự các cột lũy thừa phải khớp với bảng nào?

- A · Thứ tự xuất hiện của giá trị trong tập kiểm tra
- B · Thứ tự các cột đã dùng khi huấn luyện
- C · Thứ tự giảm dần theo phương sai

<a id="ml08-mcq-4"></a>

### ML08-mcq-4

Với n mẫu và cơ sở [1,x,x²], ma trận thiết kế có kích thước nào?

- A · (n,3)
- B · (3,n)
- C · (n,2)

<a id="ml08-mcq-5"></a>

### ML08-mcq-5

Trong theta₀ + theta₁·x + theta₂·x², các hệ số theta xuất hiện tuyến tính hay phi tuyến?

- A · Không vì có x²
- B · Có vì mỗi theta chỉ xuất hiện bậc nhất
- C · Chỉ khi theta2=0

<a id="ml08-mcq-6"></a>

### ML08-mcq-6

Chỉ tăng bậc đa thức có bảo đảm sai số kiểm tra giảm không?

- A · Luôn giảm
- B · Luôn bằng 0
- C · Không bảo đảm giảm

<a id="ml08-mcq-7"></a>

### ML08-mcq-7

Từ x = 2, tạo hàng gồm hệ số tự do và các lũy thừa đến bậc ba.

- A · [1,2,4,8]
- B · [2,4,6]
- C · [1,2,3,4]

<a id="ml08-mcq-8"></a>

### ML08-mcq-8

Vì sao tập huấn luyện và tập kiểm tra cần dùng cùng cách tạo cột đa thức?

- A · Để tập kiểm tra có cùng số hàng với tập huấn luyện
- B · Để mỗi hệ số gắn đúng cùng đặc trưng khi dự đoán
- C · Để mọi giá trị tập kiểm tra bằng tập huấn luyện

<a id="ml08-mcq-9"></a>

### ML08-mcq-9

Thêm hai cột toàn 1 vào cùng ma trận thiết kế ảnh hưởng thế nào đến hạng?

- A · Tăng gấp đôi số mẫu
- B · Tự giảm quá khớp
- C · Tạo cột phụ thuộc tuyến tính

<a id="ml08-mcq-10"></a>

### ML08-mcq-10

Có tập giá trị x nào khiến hai cột x và x² phụ thuộc tuyến tính không?

- A · Không
- B · Có vì ký hiệu khác nhau
- C · Chỉ cần số mẫu chẵn

<a id="ml08-practice-1"></a>

### ML08-practice-1

Viết ma trận có các cột [1,x,x²] cho ba đầu vào [0,1,2].

<a id="ml08-practice-2"></a>

### ML08-practice-2

Dùng theta = [1,2,3] nhân với hàng [1,x,x²] tại x = 2. Dự đoán bằng bao nhiêu?

<a id="ml08-practice-3"></a>

### ML08-practice-3

Tại x = −2, ghi đủ bốn phần tử của hàng đặc trưng bậc ba, bắt đầu bằng 1.

<a id="ml08-practice-4"></a>

### ML08-practice-4

Năm mẫu, một đặc trưng và đa thức bậc 4 có hệ số tự do. Tìm kích thước ma trận và số hệ số cần khớp.

<a id="ml08-practice-5"></a>

### ML08-practice-5

Trên x = [1,2,3], tính riêng x**2 và 2*x rồi đối chiếu từng vị trí.

<a id="ml08-practice-6"></a>

### ML08-practice-6

Tính các dự đoán của X_poly = [[1,0,0],[1,1,1],[1,2,4]] với theta = [1,2,1].

<a id="ml08-practice-7"></a>

### ML08-practice-7

Vì sao có thể dùng phép nhân X_poly @ theta để dự đoán trong hồi quy đa thức?

<a id="ml08-practice-8"></a>

### ML08-practice-8

Hai mô hình bậc 1 và 6 có sai số huấn luyện tương ứng 2 và 0. Bạn còn cần bằng chứng nào để chọn bậc?

<a id="ml08-practice-9"></a>

### ML08-practice-9

Tập huấn luyện dùng [1,x,x²] nhưng tập kiểm tra chỉ dùng [x,x²]. Hãy chỉ ra lỗi khi áp dụng theta.

<a id="ml08-practice-10"></a>

### ML08-practice-10

Tại x = 10, so giá trị x với x⁴. Kết quả gợi ý điều gì về thang đo của các cột?

<a id="ml08-practice-11"></a>

### ML08-practice-11

Nếu x = [1,1,1], ba cột [1,x,x²] có đủ hạng cột không? Vì sao?

<a id="ml08-practice-12"></a>

### ML08-practice-12

Khi chỉ giữ bậc 0 cho cả n mẫu, mô hình có thể đưa ra những dự đoán nào?


<a id="on-ml09"></a>

## Ôn tập ML09

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml09-mcq-1"></a>

### ML09-mcq-1

Điểm z có thể nhận những giá trị nào trước khi đi qua sigmoid?

- A · Toàn bộ số thực
- B · Chỉ [0,1]
- C · Chỉ số nguyên

<a id="ml09-mcq-2"></a>

### ML09-mcq-2

Thay z = ln(3) vào sigmoid. Xác suất thu được bằng bao nhiêu?

- A · 3
- B · 0.75
- C · 0.25

<a id="ml09-mcq-3"></a>

### ML09-mcq-3

Xác suất hiện tại là p. Nếu đảo dấu cả w và b, xác suất mới viết theo p như thế nào?

- A · p+1
- B · −p
- C · 1−p

<a id="ml09-mcq-4"></a>

### ML09-mcq-4

Khi đầu vào z bằng 0, sigmoid trả giá trị nào?

- A · 0
- B · 0.5
- C · 1

<a id="ml09-mcq-5"></a>

### ML09-mcq-5

Ngưỡng gán nhãn 1 là p ≥ 0.5. Một mẫu có z = −2 nhận nhãn nào?

- A · 0
- B · 1
- C · Không thể xác định vì không có y thật

<a id="ml09-mcq-6"></a>

### ML09-mcq-6

Mô hình gán p = 0.8 cho một mẫu. Phát biểu nào diễn giải đúng con số này?

- A · Chắc chắn nhãn thật bằng 1
- B · Mô hình đúng 80% trên toàn bộ tập kiểm tra
- C · Đây là xác suất lớp 1 do mô hình ước lượng cho mẫu này

<a id="ml09-mcq-7"></a>

### ML09-mcq-7

Với z = b + w₁x₁ + w₂x₂, phương trình nào biểu diễn ranh giới p = 0.5?

- A · z=0
- B · z=0.5
- C · z=1

<a id="ml09-mcq-8"></a>

### ML09-mcq-8

Giữ mọi xác suất và nâng ngưỡng từ 0.5 lên 0.8. Tập mẫu được gán nhãn 1 sẽ thay đổi thế nào?

- A · Mọi mẫu tự có p cao hơn
- B · Tập mẫu dự đoán 1 không thể tăng
- C · Số dự đoán 1 bắt buộc giảm đúng một nửa

<a id="ml09-mcq-9"></a>

### ML09-mcq-9

Nếu z chứa x², ranh giới theo biến x ban đầu có thể phi tuyến không?

- A · Không bao giờ
- B · Chỉ khi sigmoid bị bỏ đi
- C · Có

<a id="ml09-mcq-10"></a>

### ML09-mcq-10

Trên cùng một mẫu, z tăng từ 0 lên 1. Xác suất sigmoid tăng hay giảm?

- A · Tăng từ 0.5 lên khoảng 0.7311
- B · Giảm từ 0.5 xuống 0
- C · Giữ nguyên vì nhãn chưa đổi

<a id="ml09-practice-1"></a>

### ML09-practice-1

Tự tính sigmoid(0) từ định nghĩa của hàm.

<a id="ml09-practice-2"></a>

### ML09-practice-2

Tính sigmoid lần lượt tại −2, 0, 2. Chỉ làm tròn đến bốn chữ số khi ghi kết quả.

<a id="ml09-practice-3"></a>

### ML09-practice-3

Gán nhãn cho p = [0.2,0.5,0.9] bằng quy tắc p ≥ 0.5.

<a id="ml09-practice-4"></a>

### ML09-practice-4

Tìm x trên ranh giới p = 0.5 khi b = −3 và w = 2.

<a id="ml09-practice-5"></a>

### ML09-practice-5

Với x = 2, b = −3 và w = 2, tính logit z rồi tính xác suất đến bốn chữ số thập phân.

<a id="ml09-practice-6"></a>

### ML09-practice-6

Cho p = [0.4,0.6,0.8]. Ghi hai vectơ nhãn ở ngưỡng 0.5 và 0.8, dùng dấu ≥ trong cả hai lượt.

<a id="ml09-practice-7"></a>

### ML09-practice-7

Vì sao điểm z của hồi quy logistic chưa thể dùng trực tiếp như xác suất?

<a id="ml09-practice-8"></a>

### ML09-practice-8

Tính sigmoid(2) và dùng quan hệ sigmoid(−z) = 1 − sigmoid(z) để kiểm tra sigmoid(−2).

<a id="ml09-practice-9"></a>

### ML09-practice-9

Với z = x₁ + x₂ − 3, tìm hai điểm khác nhau cùng có p = 0.5.

<a id="ml09-practice-10"></a>

### ML09-practice-10

Tìm tất cả các giá trị x thỏa p = 0.5 khi z = x² − 1.

<a id="ml09-practice-11"></a>

### ML09-practice-11

Một mẫu có p = 0.7 nhưng nhãn thực là 0. Riêng quan sát đó có chứng minh hàm sigmoid được viết sai không?

<a id="ml09-practice-12"></a>

### ML09-practice-12

Tính logit của X = [[1,0],[1,2]] với theta = [−1,1], rồi gán nhãn ở ngưỡng xác suất 0.5.


<a id="on-ml10"></a>

## Ôn tập ML10

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml10-mcq-1"></a>

### ML10-mcq-1

Với nhãn thực y = 0, tổn thất BCE của một mẫu được viết theo xác suất p như thế nào?

- A · −ln(1−p)
- B · −ln(p)
- C · p−y

<a id="ml10-mcq-2"></a>

### ML10-mcq-2

Nhãn thực là 1. Nếu p tăng từ 0.4 lên 0.6, tổn thất BCE tăng hay giảm?

- A · Bắt buộc không đổi vì vẫn cùng dữ liệu
- B · Giảm
- C · Tăng

<a id="ml10-mcq-3"></a>

### ML10-mcq-3

X có kích thước (8,3) còn p − y có kích thước (8,). Gradient của BCE trung bình có kích thước nào?

- A · (8,)
- B · (8,3)
- C · (3,)

<a id="ml10-mcq-4"></a>

### ML10-mcq-4

Với nhãn thực bằng 1, biểu thức nào tính BCE cho một mẫu?

- A · −log(p)
- B · −log(1−p)
- C · log(p)

<a id="ml10-mcq-5"></a>

### ML10-mcq-5

Với y = 0, trong hai dự đoán p = 0.1 và p = 0.9, dự đoán nào có tổn thất nhỏ hơn?

- A · p=0.9
- B · p=0.1
- C · Hai giá trị luôn bằng nhau

<a id="ml10-mcq-6"></a>

### ML10-mcq-6

Nếu p = sigmoid(X @ theta), biểu thức nào cho gradient của BCE trung bình theo theta?

- A · X.T@(y−p)/m
- B · P−y không cần X
- C · X.T@(p−y)/m

<a id="ml10-mcq-7"></a>

### ML10-mcq-7

Vì sao người ta có thể giới hạn p trước khi lấy logarit trong phép tính BCE?

- A · Tránh log(0) khi xác suất máy biểu diễn chạm 0 hoặc 1
- B · Bảo đảm mô hình luôn đúng nhãn
- C · Tự sửa data rò rỉ dữ liệu

<a id="ml10-mcq-8"></a>

### ML10-mcq-8

Nếu p và y đều là vectơ một chiều dài m, hiệu p − y có kích thước nào?

- A · (d,) với d là số hệ số
- B · (m,)
- C · (m, m) trong mọi trường hợp

<a id="ml10-mcq-9"></a>

### ML10-mcq-9

Hai dự đoán đều sai nhãn. Dự đoán sai với xác suất tự tin hơn có thể bị BCE phạt nặng hơn không?

- A · Không vì đều sai một nhãn
- B · Không vì BCE luôn trong [0,1]
- C · Có

<a id="ml10-mcq-10"></a>

### ML10-mcq-10

Khi y = 1 nhưng p tiến dần về 0, BCE tiến đến đâu?

- A · Tăng không bị chặn trong công thức lý tưởng
- B · Tiến về 0
- C · Luôn bằng 1

<a id="ml10-practice-1"></a>

### ML10-practice-1

Tính BCE với y = 1, p = 0.8 bằng logarit tự nhiên. Ghi kết quả đến sáu chữ số thập phân.

<a id="ml10-practice-2"></a>

### ML10-practice-2

Tính BCE với y = 0, p = 0.2 rồi đối chiếu với trường hợp y = 1, p = 0.8.

<a id="ml10-practice-3"></a>

### ML10-practice-3

Hai mẫu có y = [1,0] và p = [0.8,0.3]. Tính BCE trung bình.

<a id="ml10-practice-4"></a>

### ML10-practice-4

Với nhãn thực 1, hãy tính và so BCE ở p = 0.9 và p = 0.1.

<a id="ml10-practice-5"></a>

### ML10-practice-5

Tính p và gradient cho X = [[1,0],[1,1]], theta = [0,0] và y = [0,1].

<a id="ml10-practice-6"></a>

### ML10-practice-6

Cập nhật theta = [0,0] bằng gradient [0,−0.25] với tốc độ học 0.1.

<a id="ml10-practice-7"></a>

### ML10-practice-7

Khi y có kích thước (m,1) còn p có kích thước (m,), phép trừ của NumPy có thể tạo ra hình dạng nào ngoài ý muốn?

<a id="ml10-practice-8"></a>

### ML10-practice-8

Giới hạn p = [0,1] vào [eps,1−eps] với eps = 1e−6. Kiểm tra các số hạng logarit trong BCE còn hữu hạn.

<a id="ml10-practice-9"></a>

### ML10-practice-9

Nếu đổi từ logarit tự nhiên sang logarit cơ số 10 trong tổn thất, hệ số trong gradient phải thay đổi ra sao?

<a id="ml10-practice-10"></a>

### ML10-practice-10

Giữ nguyên tham số rồi lặp mọi mẫu hai lần. BCE trung bình có thay đổi không? Giải thích.

<a id="ml10-practice-11"></a>

### ML10-practice-11

Khi p luôn bằng 0.5, hãy tính BCE của một mẫu cho cả hai nhãn 0 và 1.

<a id="ml10-practice-12"></a>

### ML10-practice-12

Nhãn thực là 1. Xác suất tăng từ 0.6 lên 0.9 trong khi nhãn dự đoán ở ngưỡng 0.5 vẫn giữ nguyên. BCE đổi thế nào?


<a id="on-ml11"></a>

## Ôn tập ML11

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml11-mcq-1"></a>

### ML11-mcq-1

Với f(t) = t²/2, một bước Newton từ t = 2 đưa bạn đến giá trị nào?

- A · 0
- B · 1
- C · 4

<a id="ml11-mcq-2"></a>

### ML11-mcq-2

Hessian có kích thước 3 × 3 nhưng gradient chỉ có hai phần tử. Cần làm gì trước khi giải hệ?

- A · Bỏ hàng cuối H
- B · Báo sai kích thước trước giải
- C · Tự thêm số 0 vào g

<a id="ml11-mcq-3"></a>

### ML11-mcq-3

Trong H = X.T @ W @ X / m, ma trận W phải có kích thước nào cho m mẫu?

- A · (d,d)
- B · (m,d)
- C · (m,m)

<a id="ml11-mcq-4"></a>

### ML11-mcq-4

Với Hessian H khả nghịch và gradient g, công thức nào cập nhật theta theo Newton?

- A · theta−solve(H,g)
- B · theta−H@g
- C · theta+g

<a id="ml11-mcq-5"></a>

### ML11-mcq-5

Nếu theta có d thành phần, Hessian theo theta gồm bao nhiêu hàng và cột?

- A · (m,d)
- B · (d,d)
- C · (m,)

<a id="ml11-mcq-6"></a>

### ML11-mcq-6

Trong hồi quy logistic, phần tử Wᵢᵢ của ma trận trọng số Hessian được tính từ xác suất nào và theo công thức nào?

- A · y_i
- B · p_i−y_i
- C · p_i(1−p_i)

<a id="ml11-mcq-7"></a>

### ML11-mcq-7

Nếu H suy biến, phép lấy nghịch đảo có còn cho bước Newton chuẩn không?

- A · Không. Cần xử lý suy biến theo phương pháp đã quy định
- B · Có, nghịch đảo luôn trả nghiệm chính xác
- C · Chỉ cần đổi tên biến H

<a id="ml11-mcq-8"></a>

### ML11-mcq-8

Tổn thất và gradient đã lấy trung bình trên m mẫu. Hessian phải dùng quy ước nào để nhất quán?

- A · X.T@W@X không chia m
- B · X.T@W@X/m
- C · W@X.T/m

<a id="ml11-mcq-9"></a>

### ML11-mcq-9

Hội tụ bậc hai của Newton có được bảo đảm cho mọi hàm và mọi điểm khởi tạo không?

- A · Có, không cần giả định
- B · Có, kể cả Hessian không tồn tại
- C · Không. Cần điều kiện gần nghiệm và tính trơn/khả nghịch phù hợp

<a id="ml11-mcq-10"></a>

### ML11-mcq-10

Nếu g = 0 và H khả nghịch, nghiệm delta của H·delta = g bằng bao nhiêu?

- A · Vector 0
- B · Vectơ toàn 1
- C · Không thể giải dù H khả nghịch

<a id="ml11-practice-1"></a>

### ML11-practice-1

Giải H·delta = g cho H = [[2,0],[0,4]] và g = [2,8].

<a id="ml11-practice-2"></a>

### ML11-practice-2

Từ theta = [3,5] và bước hiệu chỉnh delta = [1,2], tính theta mới.

<a id="ml11-practice-3"></a>

### ML11-practice-3

Với f(t) = (t − 3)²/2 và t = 0, tính gradient, Hessian rồi thực hiện một bước Newton.

<a id="ml11-practice-4"></a>

### ML11-practice-4

Tính hai trọng số p(1 − p) ứng với p = [0.5,0.8].

<a id="ml11-practice-5"></a>

### ML11-practice-5

Với X = [[1,0],[1,1]] và p = [0.5,0.5], dựng Hessian của BCE trung bình.

<a id="ml11-practice-6"></a>

### ML11-practice-6

Dùng X = [[1,0],[1,1]], p = [0.5,0.5], y = [0,1] và theta = [0,0] để tính trọn một bước Newton.

<a id="ml11-practice-7"></a>

### ML11-practice-7

Giải thích vì sao lấy H @ g cho bước hiệu chỉnh khác với giải hệ H·delta = g.

<a id="ml11-practice-8"></a>

### ML11-practice-8

Theta có ba phần tử nhưng H chỉ có kích thước (2,2). Hãy nêu cách xử lý và lý do.

<a id="ml11-practice-9"></a>

### ML11-practice-9

Xác định hạng của H = [[1,1],[1,1]] rồi kết luận về khả năng lấy nghịch đảo.

<a id="ml11-practice-10"></a>

### ML11-practice-10

Ở p = 0.5, trọng số Hessian là 0.25. Mô tả giới hạn của trọng số khi p tiến về hai đầu 0 và 1.

<a id="ml11-practice-11"></a>

### ML11-practice-11

Vì sao dùng tổng để tính gradient nhưng trung bình để tính Hessian sẽ làm sai độ dài bước?

<a id="ml11-practice-12"></a>

### ML11-practice-12

Giải H·delta = g với H = [[2,1],[1,3]] và g = [1,2]. Nhân lại để tự kiểm.


<a id="on-ml12"></a>

## Ôn tập ML12

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml12-mcq-1"></a>

### ML12-mcq-1

Đặc điểm nào khiến k-NN được gọi là học lười (lazy learning)?

- A · Phần lớn tính khoảng cách được thực hiện lúc truy vấn
- B · Không cần dữ liệu tập huấn luyện
- C · Không cần kiểm tra đầu vào

<a id="ml12-mcq-2"></a>

### ML12-mcq-2

Với k = 1, truy vấn đúng một điểm huấn luyện và không có điểm trùng mang nhãn khác. Dự đoán là gì?

- A · Trung bình mọi nhãn tập huấn luyện
- B · Nhãn của điểm đó
- C · Luôn lớp 0

<a id="ml12-mcq-3"></a>

### ML12-mcq-3

Khoảng cách Manhattan (Manhattan distance) giữa hai vectơ d chiều được tính bằng tổng nào?

- A · Căn tổng sai lệch bình phương
- B · Tổng sai lệch có dấu
- C · Tổng trị tuyệt đối sai lệch tọa độ

<a id="ml12-mcq-4"></a>

### ML12-mcq-4

Tính khoảng cách Euclid từ (0,0) đến (3,4).

- A · 7
- B · 5
- C · 25

<a id="ml12-mcq-5"></a>

### ML12-mcq-5

Ba láng giềng mang nhãn [1,0,1]. Lớp nào thắng khi bỏ phiếu đa số?

- A · 1
- B · 0
- C · Không thể xác định

<a id="ml12-mcq-6"></a>

### ML12-mcq-6

Nếu hai đặc trưng chênh nhau nhiều về thang đo, đặc trưng nào có thể chi phối khoảng cách?

- A · Tự động không đổi theo đơn vị
- B · Luôn bằng 0
- C · Bị đặc trưng thang đo lớn chi phối

<a id="ml12-mcq-7"></a>

### ML12-mcq-7

Hàm yêu cầu 1 ≤ k ≤ n. Khi k lớn hơn số mẫu huấn luyện, hãy chọn cách xử lý phù hợp.

- A · Báo đầu vào không hợp lệ
- B · Nhân bản mẫu tập huấn luyện để đủ k
- C · Dùng nhãn tập kiểm tra để đủ k

<a id="ml12-mcq-8"></a>

### ML12-mcq-8

Để phân lớp một mẫu mới bằng k-NN, cần giữ lại những thông tin nào từ tập huấn luyện?

- A · Chỉ nhãn thật của mẫu mới
- B · Đặc trưng và nhãn của tập huấn luyện, cùng đặc trưng mẫu mới
- C · Chỉ chỉ số thứ tự của mẫu mới

<a id="ml12-mcq-9"></a>

### ML12-mcq-9

Với k = 4, hai lớp hòa phiếu. Cần chốt điều gì để lần chạy sau cho cùng kết quả?

- A · Giấu tình huống này khỏi tập kiểm tra
- B · Luôn trả lớp của tập kiểm tra
- C · Quy tắc phá hòa được công bố

<a id="ml12-mcq-10"></a>

### ML12-mcq-10

Hai vectơ giống nhau có khoảng cách Euclid bằng bao nhiêu?

- A · 0
- B · 1
- C · Không xác định

<a id="ml12-practice-1"></a>

### ML12-practice-1

Dùng chuẩn Euclid để tính khoảng cách giữa (1,2) và (4,6).

<a id="ml12-practice-2"></a>

### ML12-practice-2

Vẫn với (1,2) và (4,6), khoảng cách Manhattan bằng bao nhiêu?

<a id="ml12-practice-3"></a>

### ML12-practice-3

Trên các điểm [0,3,8], tính khoảng cách tới 2. Ghi chỉ số của điểm gần nhất, bắt đầu từ 0.

<a id="ml12-practice-4"></a>

### ML12-practice-4

Với X = [0,3,8], y = [0,1,0], q = 2 và k = 1, hãy nộp nhãn dự đoán.

<a id="ml12-practice-5"></a>

### ML12-practice-5

Đếm phiếu của từng lớp trong [0,1,1] rồi ghi lớp thắng.

<a id="ml12-practice-6"></a>

### ML12-practice-6

Các khoảng cách theo chỉ số là [0.4,0.1,0.7,0.2]. Liệt kê hai chỉ số gần nhất theo thứ tự khoảng cách.

<a id="ml12-practice-7"></a>

### ML12-practice-7

Vì sao mẫu truy vấn phải dùng các cột theo cùng thứ tự với mẫu huấn luyện?

<a id="ml12-practice-8"></a>

### ML12-practice-8

Một điểm huấn luyện bị gán nhãn nhiễu có thể ảnh hưởng thế nào đến kết quả khi k = 1?

<a id="ml12-practice-9"></a>

### ML12-practice-9

Cho bốn nhãn [0,1,0,1]. Dùng quy tắc hòa lấy lớp có số nhỏ hơn và ghi dự đoán.

<a id="ml12-practice-10"></a>

### ML12-practice-10

Hai điểm huấn luyện cách đều truy vấn nhưng chỉ còn một vị trí trong nhóm gần nhất. Vì sao cần quy tắc chọn trước?

<a id="ml12-practice-11"></a>

### ML12-practice-11

Giải thích vì sao dùng nhãn thật của mẫu đang dự đoán để chọn Euclid hay Manhattan làm sai quy trình đánh giá.

<a id="ml12-practice-12"></a>

### ML12-practice-12

Từ q = [0,0], tính khoảng cách Euclid đến từng hàng của [[1,0],[0,2],[3,4]].


<a id="on-ml13"></a>

## Ôn tập ML13

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml13-mcq-1"></a>

### ML13-mcq-1

Chia 25 mẫu thành 5 phần đều nhau. Sau đủ năm lượt, mỗi mẫu xuất hiện trong tập xác thực mấy lần?

- A · Một
- B · Năm
- C · Không lần nào

<a id="ml13-mcq-2"></a>

### ML13-mcq-2

Các quan sát của cùng một người xuất hiện ở cả hai tập. Điều đó có thể ảnh hưởng thế nào đến ước tính cho người mới?

- A · Tự tăng số đặc trưng
- B · Đánh giá lạc quan nếu mục tiêu là tổng quát sang người mới
- C · Bảo đảm dữ liệu độc lập

<a id="ml13-mcq-3"></a>

### ML13-mcq-3

Sau khi chọn cấu hình bằng kiểm định chéo, có thể khớp lại trên toàn bộ tập huấn luyện ban đầu trước khi dùng tập kiểm tra riêng không?

- A · Không, chỉ được giữ mô hình phần cuối
- B · Có và dùng thêm nhãn tập kiểm tra để khớp mô hình
- C · Có, theo quy trình đã chốt

<a id="ml13-mcq-4"></a>

### ML13-mcq-4

Tập kiểm tra được giữ riêng để trả lời câu hỏi đánh giá nào?

- A · Chọn mọi hyperparameter bằng cách thử lặp lại
- B · Ước lượng hiệu năng sau khi đã chốt lựa chọn mô hình
- C · Thay tập tập huấn luyện để tính gradient

<a id="ml13-mcq-5"></a>

### ML13-mcq-5

Khi chuyển sang phần xác thực kế tiếp, mô hình dùng để đánh giá cần được khởi tạo và huấn luyện ra sao?

- A · Huấn luyện độc lập từ dữ liệu tập huấn luyện của phần đó
- B · Kế thừa trọng số đã học trên toàn bộ dữ liệu
- C · Chỉ dự đoán từ mô hình phần đầu

<a id="ml13-mcq-6"></a>

### ML13-mcq-6

Chia 12 mẫu đều vào ba phần. Trong mỗi lượt có bao nhiêu mẫu huấn luyện và bao nhiêu mẫu xác thực?

- A · 4 train,8 validation
- B · 12 train,4 validation
- C · 8 train,4 validation

<a id="ml13-mcq-7"></a>

### ML13-mcq-7

Trong từng lượt, bộ chuẩn hóa phải học các tham số từ phần dữ liệu nào?

- A · Chỉ tập huấn luyện của phần
- B · Toàn bộ dữ liệu trước khi chia phần
- C · Tập xác thực của phần

<a id="ml13-mcq-8"></a>

### ML13-mcq-8

Kiểm định bỏ-một-mẫu (leave-one-out cross-validation, LOOCV) trên n mẫu cần khớp mô hình bao nhiêu lần?

- A · 1
- B · n
- C · n−1

<a id="ml13-mcq-9"></a>

### ML13-mcq-9

Đã chạy K phần bên trong tập huấn luyện. Bạn còn cần giữ độc lập tập kiểm tra riêng không?

- A · Có, có thể dùng tập kiểm tra để chọn phần tốt nhất
- B · Có, gộp mọi nhãn tập kiểm tra vào tập huấn luyện ngay khi chọn K
- C · Không

<a id="ml13-mcq-10"></a>

### ML13-mcq-10

Có 10 mẫu và K = 3. Kích thước ba phần có nhất thiết bằng nhau không?

- A · Không, kích thước phải nguyên và có thể lệch một mẫu
- B · Có, dùng số mẫu lẻ
- C · Không thể dùng K-phần khi n không chia hết K

<a id="ml13-practice-1"></a>

### ML13-practice-1

Giữ riêng 5 trong tổng số 20 mẫu để kiểm tra cuối. Còn bao nhiêu mẫu cho huấn luyện và chọn mô hình?

<a id="ml13-practice-2"></a>

### ML13-practice-2

Với chỉ số 0 đến 11 theo thứ tự và K = 3, ghi ba tập xác thực liên tiếp.

<a id="ml13-practice-3"></a>

### ML13-practice-3

Các chỉ số là [0,1,2,3,4,5]. Nếu xác thực dùng [0,1], các chỉ số huấn luyện còn lại là gì?

<a id="ml13-practice-4"></a>

### ML13-practice-4

Ba phần xác thực cùng kích thước có MSE lần lượt là 1, 2 và 3. Tính MSE trung bình.

<a id="ml13-practice-5"></a>

### ML13-practice-5

Với LOOCV trên năm mẫu, mỗi lần khớp dùng bao nhiêu mẫu và tổng cộng khớp mấy lần?

<a id="ml13-practice-6"></a>

### ML13-practice-6

Một chương trình khớp trên tất cả mẫu rồi mới chia K phần để đánh giá. Hãy chỉ ra mẫu xác thực đã ảnh hưởng đến mô hình từ lúc nào.

<a id="ml13-practice-7"></a>

### ML13-practice-7

Tập huấn luyện của một lượt là [10,20], tập xác thực là [30]. Tính giá trị chuẩn hóa cực tiểu–cực đại của 30.

<a id="ml13-practice-8"></a>

### ML13-practice-8

Nếu dùng tiếp trọng số đã học ở lượt trước, dữ liệu xác thực ở lượt mới có thể lọt vào quá trình học ra sao?

<a id="ml13-practice-9"></a>

### ML13-practice-9

Một trong năm phần có mẫu xuất hiện lặp, trong khi một mẫu khác vắng mặt. Các phần có tạo thành phân hoạch hợp lệ không?

<a id="ml13-practice-10"></a>

### ML13-practice-10

Kiểm tra [[0,1],[2,3],[4,5]] có phủ đủ các chỉ số 0 đến 5 và có phần nào chồng lặp không.

<a id="ml13-practice-11"></a>

### ML13-practice-11

Chọn mô hình chỉ vì đạt điểm cao nhất trên một phần xác thực có thể bỏ qua thông tin nào?

<a id="ml13-practice-12"></a>

### ML13-practice-12

K = 1 làm tập huấn luyện của lượt duy nhất rỗng. Hàm chia phần cần xử lý đầu vào này thế nào?


<a id="on-ml14"></a>

## Ôn tập ML14

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml14-mcq-1"></a>

### ML14-mcq-1

Hai phần dư đều bằng 0 và nhãn thực có biến thiên. RMSE bằng bao nhiêu?

- A · 0
- B · 1
- C · Không xác định dù có hai mẫu

<a id="ml14-mcq-2"></a>

### ML14-mcq-2

Trên cùng các phần dư, theo công thức chuẩn, RMSE có thể nhỏ hơn MAE không?

- A · Không thể so vì khác đơn vị
- B · Không, trừ sai số số học
- C · Luôn nhỏ hơn

<a id="ml14-mcq-3"></a>

### ML14-mcq-3

MSE bằng 9 có đủ để khẳng định mọi phần dư đều bằng 3 không?

- A · Có vì căn MSE=3
- B · Chỉ khi số mẫu chẵn
- C · Không

<a id="ml14-mcq-4"></a>

### ML14-mcq-4

Tính MAE của hai phần dư [−2,2].

- A · 0
- B · 2
- C · 4

<a id="ml14-mcq-5"></a>

### ML14-mcq-5

Hai phần dư [−2,2] cho MSE và RMSE lần lượt bằng bao nhiêu?

- A · MSE=4,RMSE=2
- B · MSE=2,RMSE=4
- C · Cả hai bằng 0

<a id="ml14-mcq-6"></a>

### ML14-mcq-6

Nếu y dùng đơn vị u, RMSE biểu diễn theo đơn vị nào?

- A · u²
- B · Không có đơn vị
- C · u

<a id="ml14-mcq-7"></a>

### ML14-mcq-7

Với SST > 0, điều kiện nào giữa SSE và SST khiến R² âm trên tập đánh giá?

- A · SSE của mô hình lớn hơn SST của dự đoán hằng trung bình y
- B · Không bao giờ vì R² là bình phương
- C · Chỉ khi số mẫu âm

<a id="ml14-mcq-8"></a>

### ML14-mcq-8

Khi mọi nhãn thực bằng nhau, thành phần nào trong R² = 1 − SSE/SST khiến phép tính mất nghĩa?

- A · Luôn trả 1
- B · SST=0 nên cần quy định hành vi
- C · Luôn trả 0

<a id="ml14-mcq-9"></a>

### ML14-mcq-9

Vì sao một phần dư lớn tác động mạnh lên MSE hơn lên MAE?

- A · Vì bỏ mọi phần dư nhỏ
- B · Vì chỉ đếm dấu phần dư
- C · Vì bình phương làm đóng góp tăng nhanh theo độ lớn

<a id="ml14-mcq-10"></a>

### ML14-mcq-10

Nếu mọi phần dư đều bằng 2, hãy chọn đúng bộ [MAE,MSE,RMSE].

- A · 2,4,2
- B · 2,2,2
- C · 0,4,2

<a id="ml14-practice-1"></a>

### ML14-practice-1

Từ y = [1,3] và dự đoán [2,1], tính vectơ phần dư theo thứ tự dự đoán trừ thực tế.

<a id="ml14-practice-2"></a>

### ML14-practice-2

Lấy trung bình các giá trị tuyệt đối của [1,−2] để tìm MAE.

<a id="ml14-practice-3"></a>

### ML14-practice-3

Tính MSE và RMSE của [1,−2]. Ghi RMSE đến sáu chữ số thập phân.

<a id="ml14-practice-4"></a>

### ML14-practice-4

Tính đủ [MAE,MSE,RMSE,R²] khi y và dự đoán cùng là [1,2,3].

<a id="ml14-practice-5"></a>

### ML14-practice-5

Với y = [1,2,3], tính R² cho mô hình luôn dự đoán 2.

<a id="ml14-practice-6"></a>

### ML14-practice-6

Với y = [1,2,3], tính R² cho mô hình luôn dự đoán 0.

<a id="ml14-practice-7"></a>

### ML14-practice-7

Đối chiếu E = Σe²/(2m) với định nghĩa MSE. Hai con số liên hệ thế nào?

<a id="ml14-practice-8"></a>

### ML14-practice-8

Hai vectơ phần dư [0,4] và [2,2] cho MAE và MSE bằng bao nhiêu? So sánh kết quả.

<a id="ml14-practice-9"></a>

### ML14-practice-9

Khi y = [5,5] và dự đoán cũng đúng cả hai, vì sao cần quy ước riêng cho R²?

<a id="ml14-practice-10"></a>

### ML14-practice-10

Nhân cả nhãn thực và dự đoán với 1000. Tìm hệ số thay đổi của MAE, RMSE, MSE và R², giả sử SST ban đầu dương.

<a id="ml14-practice-11"></a>

### ML14-practice-11

Một báo cáo gọi MSE tính trên chính dữ liệu dùng để khớp là MSE kiểm tra. Hãy sửa cách diễn giải ấy.

<a id="ml14-practice-12"></a>

### ML14-practice-12

Khi m = 0, việc điền 0 thay cho sai số trung bình có phù hợp với công thức không? Giải thích.


<a id="on-ml15"></a>

## Ôn tập ML15

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml15-mcq-1"></a>

### ML15-mcq-1

Nhãn thực bằng 1 và dự đoán bằng 0. Mẫu này tăng bộ đếm nào?

- A · FN
- B · FP
- C · TN

<a id="ml15-mcq-2"></a>

### ML15-mcq-2

Một mẫu thật sự âm và cũng được dự đoán âm thuộc ô nào của ma trận nhầm lẫn?

- A · FN
- B · TN
- C · TP

<a id="ml15-mcq-3"></a>

### ML15-mcq-3

Độ chuẩn xác bằng 1 có bảo đảm mô hình tìm được mọi mẫu dương không?

- A · Có vì mọi dự đoán dương đúng
- B · Có nếu có FP
- C · Không

<a id="ml15-mcq-4"></a>

### ML15-mcq-4

Nếu 1 là lớp dương, mẫu có y = 0 nhưng được dự đoán 1 được gọi là gì?

- A · FN
- B · FP
- C · TP

<a id="ml15-mcq-5"></a>

### ML15-mcq-5

Mẫu số nào đi với TP trong công thức tính độ chuẩn xác?

- A · TP/(TP+FP)
- B · TP/(TP+FN)
- C · (TP+TN)/N

<a id="ml15-mcq-6"></a>

### ML15-mcq-6

Độ bao phủ cho biết điều gì về các mẫu thực sự dương?

- A · Tỷ lệ dự đoán dương là đúng
- B · Tỷ lệ toàn bộ mẫu được dự đoán đúng
- C · Tỷ lệ mẫu dương thật được tìm thấy

<a id="ml15-mcq-7"></a>

### ML15-mcq-7

Với TP = 3, FP = 1 và FN = 2, tính F1 trực tiếp từ ba bộ đếm.

- A · 2/3
- B · 3/4
- C · 3/5

<a id="ml15-mcq-8"></a>

### ML15-mcq-8

Mô hình luôn dự đoán âm trên tập có 99 âm và 1 dương. Tỷ lệ đúng 99% che mất điều gì?

- A · Recall dương là 100%
- B · Recall dương là 0%
- C · Đã chứng minh mô hình hữu ích cho tìm ca dương

<a id="ml15-mcq-9"></a>

### ML15-mcq-9

Nếu mô hình chưa dự đoán dương lần nào, mẫu số của độ chuẩn xác bằng bao nhiêu?

- A · Luôn bằng 1
- B · Luôn bằng recall
- C · TP+FP=0, cần quy định hành vi

<a id="ml15-mcq-10"></a>

### ML15-mcq-10

Tăng riêng TN và giữ nguyên TP, FP, FN. Độ chuẩn xác và độ bao phủ có đổi không?

- A · Cả hai giữ nguyên
- B · Cả hai bắt buộc tăng
- C · Precision tăng còn recall giảm

<a id="ml15-practice-1"></a>

### ML15-practice-1

Từ y = [1,1,0,0] và dự đoán [1,0,1,0], ghi bốn số đếm theo thứ tự TP, FP, FN, TN.

<a id="ml15-practice-2"></a>

### ML15-practice-2

Tính tỷ lệ đúng khi TP = 3, FP = 1, FN = 2 và TN = 4.

<a id="ml15-practice-3"></a>

### ML15-practice-3

Cho TP = 3, FP = 1, FN = 2, TN = 4. Tính riêng độ chuẩn xác và độ bao phủ.

<a id="ml15-practice-4"></a>

### ML15-practice-4

Tính F1 từ TP = 3, FP = 1, FN = 2, TN = 4. Làm tròn đến sáu chữ số thập phân.

<a id="ml15-practice-5"></a>

### ML15-practice-5

Dựng ma trận nhầm lẫn cho TP = 3, FP = 1, FN = 2 và TN = 4. Hàng là nhãn thực [0,1], cột là nhãn dự đoán [0,1].

<a id="ml15-practice-6"></a>

### ML15-practice-6

Trong 10 mẫu thực sự dương, mô hình tìm đúng 6 mẫu. Độ bao phủ bằng bao nhiêu?

<a id="ml15-practice-7"></a>

### ML15-practice-7

Trong 8 mẫu được dự đoán dương có 2 mẫu sai. Tính độ chuẩn xác.

<a id="ml15-practice-8"></a>

### ML15-practice-8

F1 kết hợp độ chuẩn xác và độ bao phủ bằng cách nào? Vì sao trung bình cộng cho đại lượng khác?

<a id="ml15-practice-9"></a>

### ML15-practice-9

Khi tập đánh giá không có mẫu dương thực sự, phân biệt kết quả của công thức recall trực tiếp với quy ước dùng trong phiếu.

<a id="ml15-practice-10"></a>

### ML15-practice-10

Tính F1 theo bộ đếm khi TP = 0, FP = 2 và FN = 3.

<a id="ml15-practice-11"></a>

### ML15-practice-11

Bỏ sót một mẫu dương gây chi phí cao. Chỉ số nào đo trực tiếp tỷ lệ tìm được trong các mẫu dương thực?

<a id="ml15-practice-12"></a>

### ML15-practice-12

Nếu đổi lớp dương từ 1 sang 0, hai chỉ số precision và recall có buộc giữ nguyên không? Giải thích.


<a id="on-ml16"></a>

## Ôn tập ML16

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml16-mcq-1"></a>

### ML16-mcq-1

Điểm ROC có tọa độ (0,1) nói gì về dự đoán trên hai lớp?

- A · Không dương giả và tìm hết positive
- B · Không dương đúng
- C · Mọi mẫu dự đoán dương

<a id="ml16-mcq-2"></a>

### ML16-mcq-2

AUC bằng 1 có đủ để khẳng định nhóm được dự đoán xác suất 0.9 có đúng 90% mẫu dương không?

- A · Chỉ khi có hai lớp
- B · Không
- C · Có vì ranking hoàn hảo

<a id="ml16-mcq-3"></a>

### ML16-mcq-3

Không có điểm hòa. Khi đảo dấu tất cả điểm dự đoán và giữ nhãn thực, AUC mới liên hệ thế nào với AUC cũ?

- A · AUC cũ+1
- B · Luôn 0.5
- C · 1−AUC cũ

<a id="ml16-mcq-4"></a>

### ML16-mcq-4

Trong cặp tọa độ trên đường ROC, trục ngang và trục dọc biểu diễn gì?

- A · FPR và TPR
- B · Precision và Recall
- C · TP và FP chưa chuẩn hóa

<a id="ml16-mcq-5"></a>

### ML16-mcq-5

Tính tỷ lệ dương giả từ FP và những mẫu âm thực bằng công thức nào?

- A · FP/(TP+FP)
- B · FP/(FP+TN)
- C · FN/(TP+FN)

<a id="ml16-mcq-6"></a>

### ML16-mcq-6

Giữ điểm dự đoán, giảm ngưỡng và giả sử có đủ hai lớp. TPR và FPR có thể thay đổi theo hướng nào?

- A · Cả hai bắt buộc giảm
- B · TPR tăng nhưng FPR bắt buộc giảm
- C · Cả hai không giảm, nhưng có thể giữ nguyên

<a id="ml16-mcq-7"></a>

### ML16-mcq-7

So với tỷ lệ đúng ở một ngưỡng cố định, AUC phản ánh trực tiếp khả năng nào?

- A · Khả năng xếp hạng điểm giữa lớp dương và âm
- B · Số lần chạy gradient
- C · Độ chính xác tại ngưỡng 0.5 duy nhất

<a id="ml16-mcq-8"></a>

### ML16-mcq-8

Tập đánh giá chỉ có nhãn dương. Thành phần nào khiến bạn không thể dựng đầy đủ ROC?

- A · Có vì mọi TPR bằng 1
- B · Không. Không có mẫu âm để xác định FPR
- C · Có và AUC bắt buộc bằng 1

<a id="ml16-mcq-9"></a>

### ML16-mcq-9

Một mẫu dương và một mẫu âm bằng điểm. Theo quy ước chấm cặp hòa bằng 0.5, cặp này góp bao nhiêu vào tổng?

- A · 1
- B · 0
- C · 0.5

<a id="ml16-mcq-10"></a>

### ML16-mcq-10

Nếu mọi mẫu dương đều đứng dưới mọi mẫu âm, AUC theo cặp bằng bao nhiêu?

- A · 0
- B · 1
- C · 0.5

<a id="ml16-practice-1"></a>

### ML16-practice-1

Từ TP = 8, FN = 2, FP = 3 và TN = 7, tính TPR và FPR.

<a id="ml16-practice-2"></a>

### ML16-practice-2

Với y = [1,0,1,0], điểm [0.9,0.8,0.4,0.1] và ngưỡng 0.5, tính TPR và FPR. Điểm bằng ngưỡng được dự đoán dương.

<a id="ml16-practice-3"></a>

### ML16-practice-3

Với y = [1,0,1,0] và điểm [0.9,0.8,0.4,0.1], hạ ngưỡng xuống 0.3 rồi tính lại TPR và FPR.

<a id="ml16-practice-4"></a>

### ML16-practice-4

Khi đủ hai lớp và ngưỡng cao hơn mọi điểm dự đoán, hãy ghi tọa độ ROC.

<a id="ml16-practice-5"></a>

### ML16-practice-5

Khi đủ hai lớp và ngưỡng thấp hơn mọi điểm dự đoán, hãy ghi tọa độ ROC.

<a id="ml16-practice-6"></a>

### ML16-practice-6

Ghép từng điểm dương trong [0.9,0.4] với từng điểm âm trong [0.8,0.1]. Tính AUC, tính nửa điểm cho mỗi cặp hòa.

<a id="ml16-practice-7"></a>

### ML16-practice-7

Có một điểm dương 0.5 và một điểm âm 0.5. AUC bằng bao nhiêu nếu cặp hòa tính nửa điểm?

<a id="ml16-practice-8"></a>

### ML16-practice-8

Khi tất cả mẫu dương được xếp trên tất cả mẫu âm, mỗi cặp được bao nhiêu điểm và AUC bằng bao nhiêu?

<a id="ml16-practice-9"></a>

### ML16-practice-9

Cộng cùng một hằng số vào mọi điểm. Giải thích kết quả đối với thứ hạng và AUC.

<a id="ml16-practice-10"></a>

### ML16-practice-10

Vì sao vẫn cần chọn ngưỡng phù hợp với chi phí lỗi dù mô hình có AUC cao?

<a id="ml16-practice-11"></a>

### ML16-practice-11

Nếu tập kiểm tra chỉ chứa một lớp, nên báo cáo AUC thế nào và vì sao?

<a id="ml16-practice-12"></a>

### ML16-practice-12

Trong các chỉ số của ML15, tên nào khác dùng cho TPR?


<a id="on-ml17"></a>

## Ôn tập ML17

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml17-mcq-1"></a>

### ML17-mcq-1

Vì sao mô hình luôn dự đoán một hằng số có thể thiếu khớp khi quan hệ cần học phức tạp?

- A · Khả năng biểu diễn bị hạn chế
- B · Vì luôn có training loss=0
- C · Vì mọi mô hình hằng quá khớp

<a id="ml17-mcq-2"></a>

### ML17-mcq-2

Mô hình phức tạp hơn làm giảm sai số huấn luyện nhưng không cải thiện sai số xác thực. Có đủ lý do để chọn nó theo tiêu chí xác thực không?

- A · Có nếu bỏ tập kiểm tra khỏi báo cáo
- B · Không theo tiêu chí tập xác thực đang dùng
- C · Có, mọi tập huấn luyện tốt hơn đều tổng quát tốt hơn

<a id="ml17-mcq-3"></a>

### ML17-mcq-3

Hai tập huấn luyện và xác thực có phân bố khác nhau. Điều này có thể tạo độ chênh sai số lớn không?

- A · Không, gap chỉ do quá khớp
- B · Chỉ khi label là chuỗi
- C · Có

<a id="ml17-mcq-4"></a>

### ML17-mcq-4

Khi cả sai số huấn luyện lẫn sai số xác thực đều cao, dấu hiệu đầu tiên cần xem xét là gì?

- A · thiếu khớp là một khả năng cần kiểm tra
- B · Chắc chắn quá khớp
- C · Chắc chắn tập kiểm tra bị lộ

<a id="ml17-mcq-5"></a>

### ML17-mcq-5

Sai số huấn luyện rất thấp trong khi sai số xác thực cao gợi ý rủi ro nào?

- A · Mô hình chắc chắn hoàn hảo
- B · quá khớp hoặc khác biệt dữ liệu cần chẩn đoán
- C · Không cần thêm đánh giá

<a id="ml17-mcq-6"></a>

### ML17-mcq-6

Nên xem kết quả trên tập nào để chọn mức phức tạp của mô hình?

- A · Tập kiểm tra lặp lại cho đến khi tốt
- B · Chỉ training tổn thất nhỏ nhất
- C · Tập xác thực hoặc CV trong phần tập huấn luyện

<a id="ml17-mcq-7"></a>

### ML17-mcq-7

Thêm một đặc trưng bất kỳ có bảo đảm cải thiện dự đoán trên dữ liệu mới không?

- A · Không
- B · Có vì có nhiều thông tin hơn
- C · Có nếu số cột là số chẵn

<a id="ml17-mcq-8"></a>

### ML17-mcq-8

Độ chệch trong phân tích độ chệch–phương sai có cùng nghĩa với cột toàn 1 trong ma trận thiết kế không?

- A · Giống hoàn toàn
- B · Không, đây là các khái niệm khác nhau
- C · Phương sai là số hàng X

<a id="ml17-mcq-9"></a>

### ML17-mcq-9

Mô hình thắng trên một lần chia xác thực có chắc sẽ thắng trên mọi dữ liệu tương lai không?

- A · Có
- B · Có nếu tập huấn luyện loss=0
- C · Không

<a id="ml17-mcq-10"></a>

### ML17-mcq-10

Hai tập có những bản sao của cùng một mẫu. Chênh lệch tổn thất nhỏ lúc này nói được gì về khả năng khái quát?

- A · Không, cần kiểm rò rỉ dữ liệu giữa hai tập
- B · Có vì điểm hai tập giống nhau
- C · Có nếu mô hình nhiều tham số

<a id="ml17-practice-1"></a>

### ML17-practice-1

A có MSE huấn luyện 1 và xác thực 8. B có hai giá trị tương ứng 2 và 3. Nếu cách chia hợp lệ, nên chọn mô hình nào theo MSE xác thực?

<a id="ml17-practice-2"></a>

### ML17-practice-2

Với cặp [sai số huấn luyện,sai số xác thực] của A là [1,8] và B là [2,3], tính độ chênh xác thực trừ huấn luyện.

<a id="ml17-practice-3"></a>

### ML17-practice-3

Ba bậc [1,3,8] cho MSE xác thực [5,2,7]. Hãy chọn bậc bằng tập xác thực.

<a id="ml17-practice-4"></a>

### ML17-practice-4

Sai số trên cả hai tập đều cao. Nêu hai điều cần kiểm tra trước khi quyết định tăng bậc mô hình.

<a id="ml17-practice-5"></a>

### ML17-practice-5

Nếu sửa siêu tham số mỗi lần nhìn điểm kiểm tra, vai trò của tập kiểm tra thay đổi thế nào?

<a id="ml17-practice-6"></a>

### ML17-practice-6

Một đặc trưng chỉ xuất hiện sau thời điểm dự đoán. Vì sao điểm huấn luyện và xác thực tốt vẫn chưa đáng tin?

<a id="ml17-practice-7"></a>

### ML17-practice-7

Thêm một đặc trưng ngẫu nhiên khiến sai số huấn luyện giảm và sai số xác thực tăng. Bạn có thể kết luận gì từ hai số đo ấy?

<a id="ml17-practice-8"></a>

### ML17-practice-8

MSE huấn luyện bằng 0 cho biết gì, và cần đo thêm gì trên dữ liệu chưa gặp?

<a id="ml17-practice-9"></a>

### ML17-practice-9

Ba lần chia cho MSE xác thực [1,5,3]. Ghi trung bình cùng giá trị nhỏ nhất và lớn nhất.

<a id="ml17-practice-10"></a>

### ML17-practice-10

Mô hình hằng dự đoán cùng một số cho một quan hệ cong rõ rệt. Chẩn đoán loại sai lệch mô hình có thể gặp.

<a id="ml17-practice-11"></a>

### ML17-practice-11

Vì sao số tham số lớn hơn có thể cải thiện độ khớp trên tập huấn luyện nhưng làm giảm chất lượng trên dữ liệu mới?

<a id="ml17-practice-12"></a>

### ML17-practice-12

Hai mô hình cùng có MSE xác thực bằng 2 và MSE huấn luyện lần lượt 0.1, 1.8. Có đủ chứng cứ để xếp hạng chúng trên mọi dữ liệu tương lai không?


<a id="on-ml18"></a>

## Ôn tập ML18

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml18-mcq-1"></a>

### ML18-mcq-1

Với w = [0,0] và lambda hữu hạn, số hạng phạt L2 bằng bao nhiêu?

- A · 0
- B · lambda
- C · Không xác định

<a id="ml18-mcq-2"></a>

### ML18-mcq-2

Phạt L2 trong Ridge có buộc các hệ số bị co phải trở thành đúng bằng 0 không?

- A · Chỉ hệ số tự do bị xóa
- B · Không
- C · Có, đó là định nghĩa L2

<a id="ml18-mcq-3"></a>

### ML18-mcq-3

Dùng tổng tổn thất dữ liệu và giữ nguyên phần phạt. Khi tăng số mẫu, tỷ trọng của phần phạt có thể thay đổi không?

- A · Không trong mọi trường hợp
- B · Mọi tham số tự bằng 0
- C · Có thể đổi

<a id="ml18-mcq-4"></a>

### ML18-mcq-4

Với E = mean(e²)/2 + lambda·sum(w²)/2, gradient do riêng phần phạt tạo ra là gì?

- A · lambda*w
- B · 2*lambda*w
- C · lambda

<a id="ml18-mcq-5"></a>

### ML18-mcq-5

Theo quy ước Ridge của phiếu, hệ số tự do b có chịu phạt L2 không?

- A · Chỉ phạt hệ số tự do
- B · Không
- C · Có, mọi tham số bắt buộc bị phạt

<a id="ml18-mcq-6"></a>

### ML18-mcq-6

Khi lambda = 0, hàm mục tiêu còn lại phần nào?

- A · Mọi hệ số bằng 0
- B · Không thể huấn luyện
- C · Trở về tổn thất không phạt

<a id="ml18-mcq-7"></a>

### ML18-mcq-7

Hệ số phạt lambda rất lớn có thể gây ảnh hưởng nào đến khả năng khớp dữ liệu?

- A · thiếu khớp do hệ số bị co quá mạnh
- B · Luôn cải thiện tập kiểm tra
- C · Tự thêm đặc trưng

<a id="ml18-mcq-8"></a>

### ML18-mcq-8

Vì sao thang đo của các đặc trưng ảnh hưởng đến ý nghĩa của phạt L2?

- A · Vì hệ số tự do phải là số nguyên
- B · Penalty tác động lên hệ số vốn phụ thuộc đơn vị đặc trưng
- C · L2 tự bỏ mọi khác biệt đơn vị

<a id="ml18-mcq-9"></a>

### ML18-mcq-9

Dùng đi dùng lại điểm kiểm tra cuối để chọn lambda có phù hợp không?

- A · Có, tập kiểm tra là nơi tối ưu
- B · Chỉ chọn lambda lớn nhất
- C · Không, dùng tập xác thực/CV

<a id="ml18-practice-1"></a>

### ML18-practice-1

Với w = [3,4] và lambda = 0.2, tính lambda·sum(w²)/2.

<a id="ml18-practice-2"></a>

### ML18-practice-2

Tính gradient của lambda·sum(w²)/2 tại w = [3,4], lambda = 0.2.

<a id="ml18-practice-3"></a>

### ML18-practice-3

Tổn thất dữ liệu bằng 1.5 và phần phạt bằng 2.5. Giá trị mục tiêu cần tối thiểu hóa bằng bao nhiêu?

<a id="ml18-practice-4"></a>

### ML18-practice-4

Cộng gradient dữ liệu [1,−1] với gradient phạt tại w = [2,3], lambda = 0.1. Dùng phần phạt lambda·sum(w²)/2.

<a id="ml18-practice-5"></a>

### ML18-practice-5

Cho w = 2, gradient dữ liệu bằng 0, lambda = 0.5 và tốc độ học 0.1. Cập nhật w với gradient phạt lambda·w.

<a id="ml18-practice-6"></a>

### ML18-practice-6

Tính phần phạt khi b = 10, w = 0 và hệ số tự do được miễn phạt.

<a id="ml18-practice-7"></a>

### ML18-practice-7

Thêm L2 khiến riêng tổn thất dữ liệu trên tập huấn luyện tăng. Bạn còn cần so đại lượng nào trước khi đánh giá hiệu quả điều chuẩn?

<a id="ml18-practice-8"></a>

### ML18-practice-8

Phân biệt vai trò của hệ số phạt lambda với tốc độ học alpha trong một bước tối ưu.

<a id="ml18-practice-9"></a>

### ML18-practice-9

Nếu chọn phần phạt lambda·sum(w²)/(2m), gradient phạt theo w có thêm hệ số nào?

<a id="ml18-practice-10"></a>

### ML18-practice-10

Khi theta[0] chứa hệ số tự do, cần xây dựng ma trận phạt thế nào để giữ đúng mục tiêu?

<a id="ml18-practice-11"></a>

### ML18-practice-11

Một mô hình đang thiếu khớp. Tăng phạt có chắc cải thiện kết quả không? Giải thích.

<a id="ml18-practice-12"></a>

### ML18-practice-12

Các giá trị lambda [0,0.1,1] cho MSE xác thực [4,2,3]. Chọn lambda và nêu căn cứ.


<a id="on-ml19"></a>

## Ôn tập ML19

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml19-mcq-1"></a>

### ML19-mcq-1

Với w = 0 và b = −1, mọi đầu vào hữu hạn nhận nhãn nào nếu gán 1 khi z ≥ 0?

- A · 0
- B · 1
- C · Phụ thuộc x

<a id="ml19-mcq-2"></a>

### ML19-mcq-2

Tại (0,0), tính điểm đầu vào của perceptron có w = [1,1] và b = −0.5.

- A · 0.5
- B · −0.5
- C · 0

<a id="ml19-mcq-3"></a>

### ML19-mcq-3

Perceptron có hai đầu vào và một đầu ra. Tính cả hệ số tự do, có bao nhiêu tham số vô hướng?

- A · 2
- B · 4
- C · 3

<a id="ml19-mcq-4"></a>

### ML19-mcq-4

Trong z = w @ x + b, hệ số tự do b giúp thay đổi ranh giới phân loại ra sao?

- A · Dịch ngưỡng quyết định
- B · Thêm mẫu dữ liệu
- C · Bảo đảm mọi bài toán phân tách tuyến tính

<a id="ml19-mcq-5"></a>

### ML19-mcq-5

Theo quy tắc gán 1 khi z ≥ 0, một mẫu nằm đúng trên ranh giới nhận nhãn nào?

- A · Không xác định
- B · 1
- C · 0

<a id="ml19-mcq-6"></a>

### ML19-mcq-6

Với hai đầu vào nhị phân, w = [1,1] và b = −1.5 thực hiện cổng logic nào?

- A · OR
- B · XOR
- C · AND

<a id="ml19-mcq-7"></a>

### ML19-mcq-7

Một perceptron tuyến tính duy nhất có thể khớp đủ bốn dòng của cổng XOR không?

- A · Không
- B · Có chỉ cần b=0
- C · Có nếu đổi tên nhãn

<a id="ml19-mcq-8"></a>

### ML19-mcq-8

Cho x = [2,3], w = [1,−1] và b = 2. Điểm z bằng bao nhiêu?

- A · 7
- B · 1
- C · −1

<a id="ml19-mcq-9"></a>

### ML19-mcq-9

Nhân mọi trọng số và b với cùng một số dương. Dấu của điểm hữu hạn và nhãn có đổi không?

- A · Luôn đổi tất cả
- B · Chỉ đổi số mẫu
- C · Không

<a id="ml19-practice-1"></a>

### ML19-practice-1

Viết từng số hạng của w @ x + b rồi tính với x = [2,3], w = [1,−1] và b = 2.

<a id="ml19-practice-2"></a>

### ML19-practice-2

Lập bốn hàng của bảng AND cho w = [1,1], b = −1.5, ngưỡng gán 1 là z ≥ 0.

<a id="ml19-practice-3"></a>

### ML19-practice-3

Lập bảng OR bằng w = [1,1] và b = −0.5. Ghi điểm rồi ghi nhãn ở mỗi hàng.

<a id="ml19-practice-4"></a>

### ML19-practice-4

Dùng ngưỡng z ≥ 0 để biến [−0.1,0,0.1] thành một vectơ nhãn.

<a id="ml19-practice-5"></a>

### ML19-practice-5

Nếu bỏ b khỏi perceptron AND có w = [1,1], điểm (0,0) sẽ nhận nhãn nào với quy tắc z ≥ 0?

<a id="ml19-practice-6"></a>

### ML19-practice-6

Viết phương trình đường biên của perceptron có w = [2,−1] và b = 1.

<a id="ml19-practice-7"></a>

### ML19-practice-7

Thay x = (1,3) vào 2x₁ − x₂ + 1 để xác định vị trí của điểm so với đường biên.

<a id="ml19-practice-8"></a>

### ML19-practice-8

Vì sao cần nói rõ một điểm có z đúng bằng 0 thuộc lớp nào?

<a id="ml19-practice-9"></a>

### ML19-practice-9

Phân biệt giá trị đầu vào có trọng số z và nhãn mà perceptron trả về.

<a id="ml19-practice-10"></a>

### ML19-practice-10

Vectơ w dài 3 còn một mẫu x dài 2. Hàm nên xử lý trường hợp này thế nào?

<a id="ml19-practice-11"></a>

### ML19-practice-11

Vì sao việc đưa nhãn XOR mong muốn vào bộ kiểm tra chưa chứng minh perceptron đã học được XOR?

<a id="ml19-practice-12"></a>

### ML19-practice-12

Nhân đôi w = [1,1] và b = −1.5. Hãy tính lại cả bảng AND để kiểm tra nhãn.


<a id="on-ml20"></a>

## Ôn tập ML20

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml20-mcq-1"></a>

### ML20-mcq-1

Hàm tang hyperbol (hyperbolic tangent, tanh) có đầu ra t = 0. Đạo hàm tại điểm đó bằng bao nhiêu?

- A · 1
- B · 0
- C · 0.25

<a id="ml20-mcq-2"></a>

### ML20-mcq-2

Hàm ReLU trả về giá trị nào tại z = −3?

- A · 3
- B · 0
- C · −3

<a id="ml20-mcq-3"></a>

### ML20-mcq-3

Khi z tăng đến dương vô cùng, sigmoid tiến đến giá trị nào?

- A · 0
- B · Vô cực
- C · 1

<a id="ml20-mcq-4"></a>

### ML20-mcq-4

Biểu thức nào cho đúng định nghĩa của ReLU(z)?

- A · max(0,z)
- B · min(0,z)
- C · 1/(1+exp(−z))

<a id="ml20-mcq-5"></a>

### ML20-mcq-5

Giá trị tanh(0) bằng bao nhiêu?

- A · 1
- B · 0
- C · 0.5

<a id="ml20-mcq-6"></a>

### ML20-mcq-6

Nếu s là đầu ra sigmoid, đạo hàm sigmoid được viết theo s như thế nào?

- A · 1−s²
- B · s²
- C · s(1−s)

<a id="ml20-mcq-7"></a>

### ML20-mcq-7

Tại z = 0, hai đạo hàm một phía của ReLU có cho một đạo hàm cổ điển duy nhất không?

- A · Không
- B · Có và luôn bằng 1
- C · Có và mọi framework bắt buộc dùng 0.5

<a id="ml20-mcq-8"></a>

### ML20-mcq-8

Nếu mọi tầng chỉ thực hiện biến đổi affine, toàn bộ mạng có thể rút thành phép biến đổi nào?

- A · Một bộ K-Means
- B · Một phép affine
- C · Mọi hàm phi tuyến

<a id="ml20-mcq-9"></a>

### ML20-mcq-9

Đầu ra sigmoid sát 0 hoặc 1 ảnh hưởng thế nào đến độ lớn đạo hàm?

- A · Đạo hàm luôn lớn hơn 1
- B · Tự làm dữ liệu hết NaN
- C · Đạo hàm nhỏ, có thể góp phần vanishing gradient

<a id="ml20-practice-1"></a>

### ML20-practice-1

Áp dụng ReLU cho từng vị trí của [−2,0,3], giữ nguyên thứ tự.

<a id="ml20-practice-2"></a>

### ML20-practice-2

Tại z = 0, tính và so sánh ba giá trị sigmoid, tanh và ReLU.

<a id="ml20-practice-3"></a>

### ML20-practice-3

Khi sigmoid trả s = 0.5, hãy tính s(1 − s).

<a id="ml20-practice-4"></a>

### ML20-practice-4

Khi tanh trả t = 0.6, hãy tính đạo hàm của nó.

<a id="ml20-practice-5"></a>

### ML20-practice-5

Với quy ước đạo hàm ReLU bằng 0 tại gốc, ghi các đạo hàm cho [−2,0,3].

<a id="ml20-practice-6"></a>

### ML20-practice-6

So sánh độ dốc sigmoid tại hai đầu ra 0.5 và 0.99.

<a id="ml20-practice-7"></a>

### ML20-practice-7

Cho ví dụ về đầu vào khiến giá trị ReLU nằm ngoài khoảng xác suất [0,1].

<a id="ml20-practice-8"></a>

### ML20-practice-8

Với đầu vào thực hữu hạn, hãy ghi khoảng giá trị toán học của sigmoid và tanh.

<a id="ml20-practice-9"></a>

### ML20-practice-9

Thế h = 2x + 1 vào o = 3h − 4 rồi rút gọn hai tầng thành một biểu thức theo x.

<a id="ml20-practice-10"></a>

### ML20-practice-10

Theo quy tắc chuỗi, tích của năm đạo hàm cùng bằng 0.1 có độ lớn bao nhiêu?

<a id="ml20-practice-11"></a>

### ML20-practice-11

Vì sao việc chọn giữa ReLU và sigmoid còn phụ thuộc vai trò của tầng?

<a id="ml20-practice-12"></a>

### ML20-practice-12

Một nơron ReLU có z âm cho mọi mẫu. Đạo hàm của đầu ra theo z ở các mẫu này bằng bao nhiêu?


<a id="on-ml21"></a>

## Ôn tập ML21

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml21-mcq-1"></a>

### ML21-mcq-1

Tầng kết nối đầy đủ từ 4 đầu vào đến 2 nơron có bao nhiêu trọng số nếu bỏ qua hệ số tự do?

- A · 8
- B · 6
- C · 2

<a id="ml21-mcq-2"></a>

### ML21-mcq-2

Hai mẫu giống nhau đi qua cùng mạng xác định và cùng trọng số. Hai kết quả lan truyền tiến có quan hệ gì?

- A · Một đầu ra bị bỏ
- B · Hai đầu ra giống nhau
- C · Bắt buộc khác vì vị trí hàng

<a id="ml21-mcq-3"></a>

### ML21-mcq-3

Một mạng phân loại nhị phân dùng sigmoid ở đầu ra. Bạn áp dụng ngưỡng quyết định lên đại lượng nào?

- A · Trọng số W1 bất kỳ
- B · Số neuron ẩn
- C · Xác suất sau sigmoid

<a id="ml21-mcq-4"></a>

### ML21-mcq-4

Với X có kích thước (n,d) và W₁ có kích thước (d,h), tích X @ W₁ có kích thước nào?

- A · (n,h)
- B · (d,n)
- C · (h,h)

<a id="ml21-mcq-5"></a>

### ML21-mcq-5

Vectơ hệ số tự do gồm h phần tử được cộng vào từng hàng của tầng ẩn như thế nào?

- A · Chỉ cộng vào hàng đầu
- B · Cùng hệ số tự do h chiều cho mỗi hàng mẫu
- C · Mỗi mẫu tự sinh số neuron khác nhau

<a id="ml21-mcq-6"></a>

### ML21-mcq-6

Với H có kích thước (n,h) và W₂ có kích thước (h,1), ma trận điểm đầu ra có kích thước nào?

- A · (1,n)
- B · (h,1)
- C · (n,1)

<a id="ml21-mcq-7"></a>

### ML21-mcq-7

Thêm hàm phi tuyến ở tầng ẩn mở rộng khả năng biểu diễn so với việc chỉ ghép các tầng affine ra sao?

- A · Cho phép phép hợp biểu diễn quan hệ phi tuyến
- B · Tự thay y thật
- C · Bảo đảm accuracy 100%

<a id="ml21-mcq-8"></a>

### ML21-mcq-8

Trong pha lan truyền tiến chỉ để dự đoán, có bước nào cập nhật trọng số không?

- A · Chỉ cập nhật hệ số tự do
- B · Không, pha này tính activations/đầu ra với trọng số hiện tại
- C · Có, sửa luôn W theo y

<a id="ml21-mcq-9"></a>

### ML21-mcq-9

W₁ có ba cột trong khi W₂ có bốn hàng. Hai tầng có ghép trực tiếp được không?

- A · Có vì đều là ma trận
- B · Có nếu thêm một nhãn
- C · Không, số neuron ẩn phải khớp

<a id="ml21-practice-1"></a>

### ML21-practice-1

X có 5 mẫu với 2 đặc trưng, tầng ẩn có 3 nơron và tầng ra có 1. Ghi kích thước W₁, b₁, W₂, b₂ khi mỗi hàng là một mẫu.

<a id="ml21-practice-2"></a>

### ML21-practice-2

Tính z₁ cho x = [[1,2]], W₁ = [[1,0],[0,1]] và b₁ = [−2,1].

<a id="ml21-practice-3"></a>

### ML21-practice-3

Áp dụng ReLU lên từng phần tử của z₁ = [[−1,3]]. Giữ đúng kích thước đầu ra.

<a id="ml21-practice-4"></a>

### ML21-practice-4

Từ h = [[0,3]], W₂ = [[2],[1]] và b₂ = [−1], tính điểm trước kích hoạt ở tầng ra.

<a id="ml21-practice-5"></a>

### ML21-practice-5

Cho điểm đầu ra là 2. Tính xác suất sigmoid và làm tròn đến bốn chữ số thập phân.

<a id="ml21-practice-6"></a>

### ML21-practice-6

Tính biến đổi affine cho [[0,2],[3,4]] với ma trận trọng số đơn vị và b = [1,−1].

<a id="ml21-practice-7"></a>

### ML21-practice-7

Khi chuẩn bị lan truyền ngược, việc lưu z trước hàm kích hoạt giúp tính đại lượng nào?

<a id="ml21-practice-8"></a>

### ML21-practice-8

Hai biểu diễn của một mẫu có kích thước (2,) và (1,2). NumPy có nhất thiết trả đầu ra cùng kích thước không?

<a id="ml21-practice-9"></a>

### ML21-practice-9

Đổi thứ tự các hàng trong lô và giữ nguyên mạng. Theo dõi đầu ra của từng mẫu sau phép đổi.

<a id="ml21-practice-10"></a>

### ML21-practice-10

Đếm tất cả trọng số và hệ số tự do của mạng có 2 đầu vào, 3 nơron ẩn, 1 đầu ra.

<a id="ml21-practice-11"></a>

### ML21-practice-11

Nếu bỏ phi tuyến giữa hai tầng affine, mạng có còn biểu diễn chính xác cổng XOR hai bit được không?

<a id="ml21-practice-12"></a>

### ML21-practice-12

Phép nhân báo sai kích thước. Trước khi thay W₁ bằng chuyển vị, cần đối chiếu quy ước trục nào?


<a id="on-ml22"></a>

## Ôn tập ML22

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml22-mcq-1"></a>

### ML22-mcq-1

Trong công thức cập nhật W − alpha·g, tham số thay đổi thế nào nếu alpha bằng 0?

- A · Không đổi
- B · Thành 0
- C · Đổi dấu

<a id="ml22-mcq-2"></a>

### ML22-mcq-2

Gradient truyền tới một hàm kích hoạt là u và đạo hàm cục bộ là 0.25. Delta bằng bao nhiêu?

- A · u+0.25
- B · 0.25u
- C · u/0.25

<a id="ml22-mcq-3"></a>

### ML22-mcq-3

Nếu tổn thất hiện tại hoàn toàn độc lập với một trọng số, gradient theo trọng số ấy bằng bao nhiêu?

- A · 1
- B · Bằng trọng số
- C · 0

<a id="ml22-mcq-4"></a>

### ML22-mcq-4

Delta tầng ra có kích thước (n,o) và W₂ có kích thước (h,o). Gradient truyền về các kích hoạt ẩn có kích thước nào?

- A · (n,h) qua delta2@W2.T
- B · (h,n) qua W2@delta2
- C · (n, o) không cần trọng số

<a id="ml22-mcq-5"></a>

### ML22-mcq-5

Để tính delta ẩn của cùng một lượt, cần dùng W₂ tại thời điểm nào?

- A · Trọng số ngẫu nhiên mới
- B · Trọng số của forward hiện tại
- C · Trọng số vừa update trước khi tính delta ẩn

<a id="ml22-mcq-6"></a>

### ML22-mcq-6

Với tổn thất trung bình trên lô và delta tính riêng từng mẫu, phép gộp nào cho gradient của hệ số tự do?

- A · Sum theo trục neuron
- B · Luôn bằng 0
- C · Trung bình delta theo trục mẫu

<a id="ml22-mcq-7"></a>

### ML22-mcq-7

Nếu nơron sigmoid trả giá trị s, biểu thức nào cho đạo hàm của kích hoạt?

- A · s*(1−s)
- B · 1−s
- C · s

<a id="ml22-mcq-8"></a>

### ML22-mcq-8

W₁ có kích thước (d,h). Gradient theo W₁ phải có kích thước nào?

- A · (n,h)
- B · (d,h)
- C · (h, d) trong mọi quy ước

<a id="ml22-mcq-9"></a>

### ML22-mcq-9

Delta đã được chia cho n để biểu diễn tổn thất trung bình. Khi lập gradient, có cần chia tiếp cho n không?

- A · Có, bất kỳ công thức nào cũng chia hai lần
- B · Chỉ chia hai lần cho hệ số tự do
- C · Không

<a id="ml22-practice-1"></a>

### ML22-practice-1

Tính H.T @ delta₂ / 2 với H = [[1,2],[3,4]] và delta₂ = [[1],[−1]].

<a id="ml22-practice-2"></a>

### ML22-practice-2

Với delta = [[1,3],[3,5]], lấy trung bình theo trục mẫu để tìm gradient của vectơ hệ số tự do.

<a id="ml22-practice-3"></a>

### ML22-practice-3

Một sigmoid cho đầu ra 0.5 và nhận gradient truyền về bằng 2. Tính gradient theo điểm trước kích hoạt.

<a id="ml22-practice-4"></a>

### ML22-practice-4

Với delta tầng ra [[2]] và W₂ = [[1],[−3]], tính gradient truyền về hai kích hoạt ẩn trước khi nhân đạo hàm cục bộ.

<a id="ml22-practice-5"></a>

### ML22-practice-5

Hai kích hoạt sigmoid ẩn cùng bằng 0.5, gradient truyền về là [2,−6]. Tính hai delta ẩn.

<a id="ml22-practice-6"></a>

### ML22-practice-6

Cho X = [[1,2]] và delta₁ = [[0.5,−1.5]]. Tính ma trận gradient W₁ của mẫu này.

<a id="ml22-practice-7"></a>

### ML22-practice-7

Giải thích vì sao không nên thay W₂ bằng giá trị mới giữa lúc tính gradient của hai tầng.

<a id="ml22-practice-8"></a>

### ML22-practice-8

Với delta chứa đạo hàm từng mẫu, gradient của tổn thất trung bình là X.T @ delta / n. Viết công thức cho tổng tổn thất.

<a id="ml22-practice-9"></a>

### ML22-practice-9

Phân biệt các giá trị lưu từ lượt lan truyền tiến với nhãn thực y khi tính gradient.

<a id="ml22-practice-10"></a>

### ML22-practice-10

Thực hiện một bước từ W = 2 với gradient −3 và tốc độ học 0.1.

<a id="ml22-practice-11"></a>

### ML22-practice-11

Điểm trước ReLU âm và gradient truyền về khác 0. Delta tại điểm trước kích hoạt bằng bao nhiêu?

<a id="ml22-practice-12"></a>

### ML22-practice-12

Trong phép tính delta, nêu vai trò khác nhau của phép nhân từng phần tử và phép nhân ma trận.


<a id="on-ml23"></a>

## Ôn tập ML23

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml23-mcq-1"></a>

### ML23-mcq-1

Một cụm chỉ chứa vectơ [2,5]. Tâm sau khi lấy trung bình bằng gì?

- A · [2,5]
- B · [0,0]
- C · [5,2]

<a id="ml23-mcq-2"></a>

### ML23-mcq-2

Nếu đổi tên cụm 0 và 1 cùng với hai tâm tương ứng, SSE sẽ thay đổi thế nào?

- A · Chỉ khi cụm cân bằng
- B · Không
- C · Có vì tên số khác

<a id="ml23-mcq-3"></a>

### ML23-mcq-3

Kết quả SSE là một số âm lớn. Bạn nên kiểm tra điều gì trong phép tính khoảng cách?

- A · Đã tìm cực tiểu tốt hơn 0
- B · Thuật toán luôn cho SSE âm
- C · Lỗi tính toán hoặc triển khai

<a id="ml23-mcq-4"></a>

### ML23-mcq-4

Trong bước gán của K-means, mỗi mẫu được đưa vào cụm theo điều kiện nào?

- A · Gán mỗi mẫu cho tâm cụm gần nhất
- B · Cập nhật nhãn thật
- C · Chọn ngẫu nhiên mọi tâm cụm sau mỗi bước

<a id="ml23-mcq-5"></a>

### ML23-mcq-5

Với khoảng cách Euclid bình phương, tâm mới của một cụm có thành viên được tính thế nào?

- A · Tổng nhãn các mẫu
- B · Trung bình vectơ các mẫu trong cụm
- C · Mẫu đầu tiên bất kỳ

<a id="ml23-mcq-6"></a>

### ML23-mcq-6

Khi tính SSE nội cụm, bạn cộng bình phương những khoảng cách nào?

- A · Khoảng cách giữa mọi cặp tâm cụm
- B · Số mẫu có nhãn dự đoán sai
- C · Bình phương khoảng cách mẫu đến tâm cụm được gán

<a id="ml23-mcq-7"></a>

### ML23-mcq-7

Nếu sau khi gán có một cụm rỗng, thuật toán cần có quy tắc nào cho tâm đó?

- A · Theo quy tắc được công bố
- B · Lấy trung bình rỗng rồi chấp nhận NaN
- C · Tự xóa mẫu tập kiểm tra

<a id="ml23-mcq-8"></a>

### ML23-mcq-8

Chạy K-means có bảo đảm đạt nghiệm tối ưu toàn cục ở mọi lần khởi tạo không?

- A · Có nếu có hai đặc trưng
- B · Không
- C · Có nếu dùng đúng NumPy

<a id="ml23-mcq-9"></a>

### ML23-mcq-9

Vì sao nên xem lại thang đo các đặc trưng trước khi dùng khoảng cách trong K-means?

- A · Để số mẫu bằng K
- B · Để tự biết nhãn đúng
- C · Khoảng cách có thể bị thuộc tính thang đo lớn chi phối

<a id="ml23-practice-1"></a>

### ML23-practice-1

Điểm một chiều 3 gần tâm nào hơn trong hai tâm [0,10]? Ghi chỉ số cụm từ 0.

<a id="ml23-practice-2"></a>

### ML23-practice-2

Tìm tâm mới cho cụm một chiều gồm các giá trị [1,3,5].

<a id="ml23-practice-3"></a>

### ML23-practice-3

Hai điểm [0,2] và [2,4] thuộc cùng một cụm. Tính từng tọa độ của tâm.

<a id="ml23-practice-4"></a>

### ML23-practice-4

Với các điểm [1,3,5] và tâm 3, tính tổng bình phương khoảng cách trong cụm.

<a id="ml23-practice-5"></a>

### ML23-practice-5

Cho các điểm [0,2,8,10] và tâm cũ [0,10]. Nộp các nhãn rồi tính hai tâm mới sau một vòng.

<a id="ml23-practice-6"></a>

### ML23-practice-6

Với [0,2,8,10] và tâm cũ [0,10], giữ các nhãn vừa gán và tính SSE trước lẫn sau khi thay tâm.

<a id="ml23-practice-7"></a>

### ML23-practice-7

Để cập nhật tâm, cần lấy trung bình tọa độ hay mã cụm? Giải thích bằng ý nghĩa của mỗi đại lượng.

<a id="ml23-practice-8"></a>

### ML23-practice-8

Một điểm cách đều hai tâm. Nêu quy tắc cần chốt để lượt gán có kết quả xác định.

<a id="ml23-practice-9"></a>

### ML23-practice-9

Nêu hai điều kiện có thể dùng để dừng Lloyd và giới hạn của mỗi điều kiện.

<a id="ml23-practice-10"></a>

### ML23-practice-10

Để so hai lần chạy K-means, vì sao cần giữ cùng dữ liệu và ghi lại cách khởi tạo hay hạt giống ngẫu nhiên?

<a id="ml23-practice-11"></a>

### ML23-practice-11

Nếu chỉ có một cụm cho [0,2,4], tâm tối ưu và SSE tương ứng bằng bao nhiêu?

<a id="ml23-practice-12"></a>

### ML23-practice-12

SSE huấn luyện thấp nói gì về khoảng cách nội cụm? Cần thêm bằng chứng nào để diễn giải ý nghĩa của cụm?


<a id="on-ml24"></a>

## Ôn tập ML24

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml24-mcq-1"></a>

### ML24-mcq-1

Một cặp được tách ở cả hai phân hoạch có được tính là đồng thuận trong tử số Rand không?

- A · Có
- B · Không, Jaccard và Rand giống nhau
- C · Chỉ khi mã cụm giống tên

<a id="ml24-mcq-2"></a>

### ML24-mcq-2

Với đúng hai mẫu, lập được bao nhiêu cặp không thứ tự gồm hai mẫu khác nhau?

- A · 0
- B · 1
- C · 2

<a id="ml24-mcq-3"></a>

### ML24-mcq-3

Hai dãy nhãn [0,0,1] và [0,1,1] có biểu diễn cùng cách nhóm mẫu không?

- A · Có vì đều hai cụm
- B · Có vì cùng số mẫu
- C · Không

<a id="ml24-mcq-4"></a>

### ML24-mcq-4

Đánh giá cụm bằng tiêu chí bên ngoài thường cần thêm nguồn thông tin nào?

- A · Nhãn tham chiếu
- B · Chỉ màu tâm cụm
- C · Luôn cần tập kiểm tra classification accuracy

<a id="ml24-mcq-5"></a>

### ML24-mcq-5

Đơn vị so sánh cơ bản khi tính Rand là từng nhãn hay từng cặp mẫu?

- A · Số chiều đặc trưng
- B · Cặp mẫu
- C · Chỉ từng tâm cụm

<a id="ml24-mcq-6"></a>

### ML24-mcq-6

Bốn mẫu tạo ra bao nhiêu cặp chỉ số i < j?

- A · 12
- B · 4
- C · 6

<a id="ml24-mcq-7"></a>

### ML24-mcq-7

Nếu hai kết quả chỉ khác tên cụm, chỉ số so sánh theo cặp có phân biệt chúng không?

- A · Không
- B · Có vì nhãn số thay đổi
- C · Chỉ nếu có đúng hai cụm

<a id="ml24-mcq-8"></a>

### ML24-mcq-8

Trong Jaccard theo cặp cùng cụm, loại cặp nào bị loại khỏi cả tử lẫn mẫu?

- A · Mọi cặp bất đồng
- B · Các cặp khác cụm trong cả hai phân hoạch
- C · Cặp cùng cụm trong cả hai

<a id="ml24-mcq-9"></a>

### ML24-mcq-9

Nếu chỉ có một mẫu, số cặp quan sát được gây khó khăn gì cho chỉ số theo cặp?

- A · Luôn bằng 100%
- B · Luôn bằng −1
- C · Không có cặp, cần quy định hành vi

<a id="ml24-practice-1"></a>

### ML24-practice-1

Tính số cặp không thứ tự có thể lấy từ năm mẫu khác nhau.

<a id="ml24-practice-2"></a>

### ML24-practice-2

So [0,0,1] với [5,5,7] theo từng cặp. Hai cách đặt tên có làm thay đổi phân hoạch không?

<a id="ml24-practice-3"></a>

### ML24-practice-3

Cho tham chiếu [0,0,1] và dự đoán [0,1,1]. Liệt kê cả ba cặp, ghi rõ cặp nào đồng thuận.

<a id="ml24-practice-4"></a>

### ML24-practice-4

Tính Rand bằng cách đếm cặp cho tham chiếu [0,0,1] và dự đoán [0,1,1].

<a id="ml24-practice-5"></a>

### ML24-practice-5

Có a = 2 cặp cùng cụm ở cả hai, b = 1 chỉ cùng ở tham chiếu, c = 1 chỉ cùng ở dự đoán, d = 2 khác ở cả hai. Tính Rand.

<a id="ml24-practice-6"></a>

### ML24-practice-6

Cho a = 2 cặp cùng ở cả hai, b = 1 chỉ cùng ở tham chiếu, c = 1 chỉ cùng ở dự đoán, d = 2 khác ở cả hai. Tính Jaccard theo cặp.

<a id="ml24-practice-7"></a>

### ML24-practice-7

Vì sao so tên cụm dự đoán với tên cụm tham chiếu bằng phép == trên từng hàng có thể đánh giá sai?

<a id="ml24-practice-8"></a>

### ML24-practice-8

Điểm so với phân hoạch tham chiếu cao có đủ để kết luận các cụm gọn trong không gian đặc trưng không?

<a id="ml24-practice-9"></a>

### ML24-practice-9

Một chỉ số đánh giá nội bộ có bắt buộc phải biết nhãn tham chiếu không? Giải thích.

<a id="ml24-practice-10"></a>

### ML24-practice-10

Nếu mỗi mẫu đứng riêng trong cả hai phân hoạch, công thức a/(a+b+c) gặp trường hợp nào và phiếu dùng quy ước gì?

<a id="ml24-practice-11"></a>

### ML24-practice-11

Nếu thiếu một nhãn, vì sao phải xử lý mẫu đó nhất quán ở cả hai phân hoạch trước khi so?

<a id="ml24-practice-12"></a>

### ML24-practice-12

Một cặp cùng cụm ở tham chiếu nhưng khác cụm ở dự đoán góp vào tử và mẫu của Rand, Jaccard ra sao?


<a id="on-ml25"></a>

## Ôn tập ML25

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml25-mcq-1"></a>

### ML25-mcq-1

Nếu giữ đủ d trục trực chuẩn cùng vectơ trung bình, có thể dựng lại chính xác dữ liệu trong số học chính xác không?

- A · Có
- B · Không vì luôn mất ít nhất một chiều
- C · Chỉ khi không có mẫu

<a id="ml25-mcq-2"></a>

### ML25-mcq-2

Trị riêng bằng 0 của ma trận hiệp phương sai nói gì về độ biến thiên theo trục tương ứng?

- A · Mọi đặc trưng gốc đều hằng
- B · Không có phương sai dữ liệu tâm hóa theo hướng đó
- C · Tâm cụm bằng 0

<a id="ml25-mcq-3"></a>

### ML25-mcq-3

PCA chuẩn có dùng nhãn y để chọn hướng dự đoán y tốt nhất không?

- A · Có vì mọi ML cần y
- B · Có nếu y là số
- C · Không

<a id="ml25-mcq-4"></a>

### ML25-mcq-4

Trước khi lập ma trận hiệp phương sai cho PCA, cần biến đổi từng cột của X thế nào?

- A · Trừ trung bình theo cột tập huấn luyện
- B · Trừ trung bình riêng của từng hàng
- C · Đổi nhãn thành số cụm

<a id="ml25-mcq-5"></a>

### ML25-mcq-5

Muốn giữ hướng có phương sai lớn nhất, bạn chọn vectơ riêng ứng với trị riêng nào?

- A · Âm nhất
- B · Lớn nhất
- C · Nhỏ nhất

<a id="ml25-mcq-6"></a>

### ML25-mcq-6

Với Xc có kích thước (n,d) và V_k có kích thước (d,k), tọa độ chiếu có kích thước nào?

- A · (d,n)
- B · (k,k)
- C · (n,k)

<a id="ml25-mcq-7"></a>

### ML25-mcq-7

Khi tổng phương sai dương, tỷ lệ phương sai của tất cả các thành phần cộng lại bằng bao nhiêu?

- A · 1
- B · Số mẫu n
- C · 0

<a id="ml25-mcq-8"></a>

### ML25-mcq-8

Đổi dấu của một vectơ riêng có làm thay đổi phương sai được giải thích bởi trục đó không?

- A · Chỉ với một mẫu
- B · Có
- C · Không vì trị riêng đổi dấu

<a id="ml25-mcq-9"></a>

### ML25-mcq-9

Khi chiếu tập kiểm tra bằng PCA đã khớp, cần trừ vectơ trung bình lấy từ tập nào?

- A · Trung bình riêng tập kiểm tra
- B · Trung bình từ tập kiểm tra label
- C · Trung bình tập huấn luyện đã khớp mô hình

<a id="ml25-practice-1"></a>

### ML25-practice-1

Với X = [[1,2],[3,4]], hãy ghi trung bình từng cột rồi ghi ma trận sau khi trừ trung bình.

<a id="ml25-practice-2"></a>

### ML25-practice-2

Từ hai trị riêng [4,1], tính tỷ lệ phương sai của từng thành phần.

<a id="ml25-practice-3"></a>

### ML25-practice-3

Các trị riêng giảm dần là [6,3,1]. Số thành phần ít nhất để giữ 90% phương sai là bao nhiêu?

<a id="ml25-practice-4"></a>

### ML25-practice-4

Tính Xc @ V_k với Xc = [[1,2],[3,4]] và V_k = [[1],[0]].

<a id="ml25-practice-5"></a>

### ML25-practice-5

Tính chất nào của ma trận hiệp phương sai thực khiến np.linalg.eigh là lựa chọn phù hợp?

<a id="ml25-practice-6"></a>

### ML25-practice-6

eigh trả trị riêng tăng dần. Nếu lấy ngay cột đầu tiên để giữ phương sai lớn nhất, bạn đã bỏ sót bước nào?

<a id="ml25-practice-7"></a>

### ML25-practice-7

Khi mọi cột đều hằng, công thức lambda/sum(lambda) gặp điều gì và phiếu ghi tỷ lệ là bao nhiêu?

<a id="ml25-practice-8"></a>

### ML25-practice-8

Nếu thay v bằng −v và đổi dấu tọa độ chiếu tương ứng, điểm dựng lại có thay đổi không?

<a id="ml25-practice-9"></a>

### ML25-practice-9

Một bảng (10,4) được chiếu lên hai trục. Đếm số tọa độ trước và sau phép chiếu cho toàn bảng.

<a id="ml25-practice-10"></a>

### ML25-practice-10

Vì sao việc khớp PCA riêng trên tập kiểm tra có thể làm các tọa độ không tương thích với mô hình đã học?

<a id="ml25-practice-11"></a>

### ML25-practice-11

Một cột có đơn vị đo lớn nên có phương sai lớn. PCA dựa trên hiệp phương sai có tự triệt ảnh hưởng thang đo không?

<a id="ml25-practice-12"></a>

### ML25-practice-12

Khi hai trị riêng bằng nhau, vì sao hai thư viện có thể trả các vectơ riêng khác nhau nhưng đều đúng?


<a id="on-ml26"></a>

## Ôn tập ML26

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml26-mcq-1"></a>

### ML26-mcq-1

Một nút có số mẫu từng lớp là [0,5]. Độ hỗn tạp Gini của nút bằng bao nhiêu?

- A · 0
- B · 0.5
- C · 5

<a id="ml26-mcq-2"></a>

### ML26-mcq-2

Đổi cơ số logarit từ 2 sang e cho mọi phép tính entropy. Thứ tự ưu tiên các điểm chia theo mức tăng thông tin có đổi không?

- A · Không thể tính entropy với ln
- B · Không nếu tính nhất quán
- C · Có, luôn đảo thứ tự

<a id="ml26-mcq-3"></a>

### ML26-mcq-3

Bốn mẫu được chia thành hai nhánh đều thuần lớp. Gini có trọng số của hai nhánh bằng bao nhiêu?

- A · 1
- B · Phụ thuộc tên lớp
- C · 0

<a id="ml26-mcq-4"></a>

### ML26-mcq-4

Viết công thức Gini của một nút theo các tỷ lệ lớp pⱼ.

- A · 1−sum(p_j²)
- B · sum(p_j)
- C · −sum(log(p_j))

<a id="ml26-mcq-5"></a>

### ML26-mcq-5

Hai lớp có cùng số mẫu trong một nút. Gini bằng bao nhiêu?

- A · 1
- B · 0.5
- C · 0

<a id="ml26-mcq-6"></a>

### ML26-mcq-6

Khi hai nhánh có số mẫu khác nhau, cần kết hợp độ hỗn tạp của chúng theo trọng số nào?

- A · Luôn cộng hai impurity rồi chia 2
- B · Chỉ dùng nhánh lớn
- C · Trung bình có trọng số theo số mẫu

<a id="ml26-mcq-7"></a>

### ML26-mcq-7

Mức tăng thông tin bằng hiệu giữa hai đại lượng nào?

- A · Entropy cha trừ entropy con có trọng số
- B · Entropy con trừ cha
- C · Tổng nhãn lớp

<a id="ml26-mcq-8"></a>

### ML26-mcq-8

Nếu điểm chia tạo một nhánh rỗng, có thể tính tỷ lệ lớp ở nhánh đó bằng phép chia thông thường không?

- A · Gán toàn nhánh lớp 1
- B · Không, cần xử lý/ngăn điểm chia rỗng
- C · Có nếu để NaN tự truyền

<a id="ml26-mcq-9"></a>

### ML26-mcq-9

Cho cây tiếp tục chia đến độ sâu rất lớn có thể gây rủi ro nào trên dữ liệu mới?

- A · Bảo đảm tốt nhất tập kiểm tra
- B · Mọi nút tự thành linear regression
- C · Overfitting

<a id="ml26-practice-1"></a>

### ML26-practice-1

Ở một nút chỉ chứa một lớp, Gini và entropy lần lượt bằng bao nhiêu?

<a id="ml26-practice-2"></a>

### ML26-practice-2

Áp dụng công thức Gini cho hai tỷ lệ [0.5,0.5].

<a id="ml26-practice-3"></a>

### ML26-practice-3

Tính Gini khi tỷ lệ hai lớp là [0.75,0.25].

<a id="ml26-practice-4"></a>

### ML26-practice-4

Nhánh trái có 6 mẫu thuần lớp, nhánh phải có 2 mẫu thuộc hai lớp khác nhau. Với Gini hai nhánh là 0 và 0.5, tính Gini có trọng số sau khi chia.

<a id="ml26-practice-5"></a>

### ML26-practice-5

Nút cha có Gini 0.5 và Gini có trọng số của các con là 0.125. Tính mức giảm.

<a id="ml26-practice-6"></a>

### ML26-practice-6

Hai lớp cân bằng có entropy bao nhiêu bit khi dùng logarit cơ số 2?

<a id="ml26-practice-7"></a>

### ML26-practice-7

Hai cách chia cùng một nút cho Gini có trọng số là 0.2 ở A và 0.3 ở B. Chọn cách giảm Gini nhiều hơn.

<a id="ml26-practice-8"></a>

### ML26-practice-8

Với x = [1,2,3,4] và ngưỡng 2.5, ghi chỉ số bắt đầu từ 0 của nhánh trái (≤) và nhánh phải (>).

<a id="ml26-practice-9"></a>

### ML26-practice-9

Dùng công thức Gini để giải thích vì sao hoán đổi tên hai lớp 0 và 1 không đổi kết quả.

<a id="ml26-practice-10"></a>

### ML26-practice-10

Nếu cả hai nhánh giữ nguyên tỷ lệ lớp như nút cha, mức giảm độ hỗn tạp bằng bao nhiêu?

<a id="ml26-practice-11"></a>

### ML26-practice-11

Giải thích vì sao dùng nhãn của tập kiểm tra để chọn ngưỡng chia sẽ làm sai quy trình đánh giá.

<a id="ml26-practice-12"></a>

### ML26-practice-12

Một nút có số mẫu từng lớp [1,3]. Ghi hai tỷ lệ rồi tính Gini.


<a id="on-ml27"></a>

## Ôn tập ML27

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml27-mcq-1"></a>

### ML27-mcq-1

Một mẫu huấn luyện có thể hoàn toàn vắng mặt sau n lần lấy mẫu có hoàn lại không?

- A · Có
- B · Không vì luôn dùng mọi mẫu phân biệt
- C · Chỉ nếu không có hạt giống ngẫu nhiên

<a id="ml27-mcq-2"></a>

### ML27-mcq-2

Ba dự đoán hồi quy là [1,1,7]. Trung bình của chúng bằng bao nhiêu?

- A · 7
- B · 3
- C · 1

<a id="ml27-mcq-3"></a>

### ML27-mcq-3

Có thể học các bước tạo mẫu và bỏ phiếu của rừng ngẫu nhiên bằng Python và NumPy mà chưa gọi bộ phân loại dựng sẵn không?

- A · Chỉ làm được bằng cách gọi một lớp RandomForest dựng sẵn
- B · Có. Có thể viết từng bước bằng Python và NumPy
- C · Chỉ được dùng phép lấy trung bình cho mọi loại nhãn

<a id="ml27-mcq-4"></a>

### ML27-mcq-4

Khi tạo một mẫu bootstrap, mỗi lượt chọn có đưa mẫu vừa lấy trở lại tập để chọn tiếp không?

- A · Có hoàn lại
- B · Không bao giờ lặp mẫu
- C · Chỉ lấy tập kiểm tra

<a id="ml27-mcq-5"></a>

### ML27-mcq-5

Trong bagging cho hồi quy, phép gộp thông dụng cho các dự đoán số là gì?

- A · Chỉ chọn mô hình cuối
- B · Trung bình các dự đoán
- C · Tổng nhãn tập kiểm tra

<a id="ml27-mcq-6"></a>

### ML27-mcq-6

Ngoài lấy mẫu có hoàn lại, rừng ngẫu nhiên tạo thêm khác biệt giữa các cây ở bước chọn đặc trưng như thế nào?

- A · Đổi nhãn thật ngẫu nhiên để khớp mô hình
- B · Bắt mọi cây cùng đúng một điểm chia
- C · Lấy tập con đặc trưng ứng viên khi chia nút

<a id="ml27-mcq-7"></a>

### ML27-mcq-7

Nếu các mô hình mắc đúng cùng một sai số trên một mẫu, lấy trung bình có triệt được sai số chung không?

- A · Không
- B · Có, luôn hết lỗi
- C · Chỉ cần tăng số mô hình vô hạn

<a id="ml27-mcq-8"></a>

### ML27-mcq-8

Sau n lượt rút bootstrap, có bắt buộc thu được n chỉ số phân biệt không?

- A · Có nếu hạt giống ngẫu nhiên cố định
- B · Không
- C · Có theo định nghĩa

<a id="ml27-mcq-9"></a>

### ML27-mcq-9

Ba cây cho nhãn [1,0,1]. Biểu quyết đa số cho kết quả nào?

- A · 0
- B · Trung bình nhãn 2/3 là nhãn mới
- C · 1

<a id="ml27-practice-1"></a>

### ML27-practice-1

Gộp ba dự đoán hồi quy [2,4,6] bằng trung bình và ghi kết quả.

<a id="ml27-practice-2"></a>

### ML27-practice-2

Hai mô hình dự đoán trên hai mẫu lần lượt [1,3] và [3,5]. Gộp theo từng mẫu để thu vectơ nào?

<a id="ml27-practice-3"></a>

### ML27-practice-3

Lấy các chỉ số [1,1,3,0] từ X = [10,20,30,40]. Ghi dãy thu được và số chỉ số khác nhau.

<a id="ml27-practice-4"></a>

### ML27-practice-4

Với n = 4 và mẫu bootstrap [1,1,3,0], tìm chỉ số ngoài mẫu của cây.

<a id="ml27-practice-5"></a>

### ML27-practice-5

Vì sao X và y phải cùng được lấy theo một dãy chỉ số bootstrap?

<a id="ml27-practice-6"></a>

### ML27-practice-6

Một trăm mô hình đều dự đoán 5 trên cùng một mẫu. Trung bình tập hợp bằng bao nhiêu?

<a id="ml27-practice-7"></a>

### ML27-practice-7

Đếm phiếu trong [0,1,1] rồi nộp nhãn đa số.

<a id="ml27-practice-8"></a>

### ML27-practice-8

Vì sao tự ý sửa nhãn đúng của tập huấn luyện là cách không phù hợp để tạo khác biệt giữa các cây?

<a id="ml27-practice-9"></a>

### ML27-practice-9

Giả sử có 10 đặc trưng và mỗi lần tìm điểm chia chỉ xét 3. Điều này có buộc mọi nút trong cây dùng đúng cùng ba đặc trưng không?

<a id="ml27-practice-10"></a>

### ML27-practice-10

Để người khác tái lập một lần mô phỏng tổ hợp cây, bạn cần lưu những dữ liệu, tham số và thông tin ngẫu nhiên nào?

<a id="ml27-practice-11"></a>

### ML27-practice-11

Chọn một cây tốt nhất bằng nhãn kiểm tra khác với bagging ở đâu?


<a id="on-ml28"></a>

## Ôn tập ML28

Ghi câu trả lời trước khi [mở phần giải](#loi-giai-ngan-hang).

<a id="ml28-mcq-1"></a>

### ML28-mcq-1

Khi báo cáo hồi quy, cần nêu đơn vị của y ở phần nào để người đọc diễn giải được sai số?

- A · Trong mô tả dữ liệu và diễn giải chỉ số
- B · Bỏ qua vì mọi kết quả hồi quy cùng đơn vị
- C · Chỉ ghi hạt giống ngẫu nhiên

<a id="ml28-mcq-2"></a>

### ML28-mcq-2

Kết quả chương trình khác đáp án dự kiến. Trước khi sửa đáp án, cần kiểm lại những gì?

- A · Có nếu còn thiếu số câu
- B · Không, phải kiểm công thức và nguồn của cả hai
- C · Có, máy luôn đúng thuật toán

<a id="ml28-mcq-3"></a>

### ML28-mcq-3

Kết quả trên dữ liệu mô phỏng cho phép kết luận trong phạm vi nào?

- A · Chứng minh hiệu năng trên mọi tập dữ liệu mới
- B · Chứng minh luôn đạt cùng chỉ số ở mọi hạt giống ngẫu nhiên
- C · Chỉ chứng minh hành vi trên dữ liệu/quy trình mô phỏng đã nêu

<a id="ml28-mcq-4"></a>

### ML28-mcq-4

Trong bài tổng hợp, tập nào dùng để học các thống kê chuẩn hóa?

- A · Tập huấn luyện, hoặc tập huấn luyện của từng phần
- B · Tập huấn luyện và tập kiểm tra gộp lại
- C · Tập kiểm tra riêng

<a id="ml28-mcq-5"></a>

### ML28-mcq-5

Một bảng số do chương trình tự sinh để minh họa chuỗi xử lý nên được giới thiệu với người đọc ra sao?

- A · Giấu hạt giống ngẫu nhiên để trông tự nhiên
- B · Ghi rõ là dữ liệu mô phỏng
- C · Gọi là dữ liệu quan sát

<a id="ml28-mcq-6"></a>

### ML28-mcq-6

Ở thời điểm nào cần chốt quy tắc chuyển giá trị thành nhãn phân loại?

- A · Sau khi xem tập kiểm tra để cho điểm tốt
- B · Luôn lấy giá trị dự đoán hồi quy làm tròn
- C · Định nghĩa rõ theo bài toán trước đánh giá

<a id="ml28-mcq-7"></a>

### ML28-mcq-7

Khi kiểm định chéo cho bài tổng hợp, vì sao mỗi phần cần một lần huấn luyện mô hình riêng?

- A · Có
- B · Không, khớp mô hình toàn dữ liệu một lần
- C · Chỉ thay tên phần

<a id="ml28-mcq-8"></a>

### ML28-mcq-8

Có thể ghi một chỉ số tính trên tập huấn luyện là chỉ số kiểm tra không?

- A · Có nếu mô hình hội tụ
- B · Không
- C · Có nếu số đẹp

<a id="ml28-mcq-9"></a>

### ML28-mcq-9

Nếu tập kiểm tra chỉ chứa một lớp, nên xử lý việc báo cáo ROC và AUC như thế nào?

- A · Tự gán AUC=1
- B · Dùng training AUC rồi đổi tên
- C · Báo không xác định theo quy tắc đã ghi

<a id="ml28-practice-1"></a>

### ML28-practice-1

Sắp xếp bốn bước chia tập, học bộ chuẩn hóa, huấn luyện mô hình và kiểm tra để dữ liệu kiểm tra chỉ được dùng đúng vai trò.

<a id="ml28-practice-2"></a>

### ML28-practice-2

X có kích thước (40,3) nhưng y chỉ có 39 phần tử. Hãy nêu việc cần làm trước khi huấn luyện.

<a id="ml28-practice-3"></a>

### ML28-practice-3

Nếu điền giá trị thiếu trong một cột bằng trung bình, bạn phải lấy trung bình từ những hàng nào?

<a id="ml28-practice-4"></a>

### ML28-practice-4

Lớp 1 được định nghĩa bằng y ≥ 3. Với y = [2,3,4], hãy ghi vectơ nhãn theo thứ tự.

<a id="ml28-practice-5"></a>

### ML28-practice-5

Tập kiểm tra có y = [2,4] và dự đoán [3,3]. Tính MAE và MSE.

<a id="ml28-practice-6"></a>

### ML28-practice-6

Với y = [1,0,1] và nhãn dự đoán [1,1,0], đếm TP, FP và FN.

<a id="ml28-practice-7"></a>

### ML28-practice-7

Một phần xác thực thiếu mẫu dương. Có thể điền F1 = 1 để bỏ qua trường hợp này không? Giải thích.

<a id="ml28-practice-8"></a>

### ML28-practice-8

Ba mô hình dự đoán 2.8, 3.0 và 3.2 cho cùng một mẫu. Gộp bằng trung bình và ghi dự đoán cuối.

<a id="ml28-practice-9"></a>

### ML28-practice-9

Tập dữ liệu chỉ có sáu mẫu. Vì sao một điểm kiểm tra cao chưa cho biết chắc mô hình sẽ hoạt động tốt trên mẫu mới?

<a id="ml28-practice-10"></a>

### ML28-practice-10

Cần lưu gì về nguồn số liệu, cách chia, mã và cách chấm để người khác tái lập bài tổng hợp dùng dữ liệu mô phỏng?

<a id="ml28-practice-11"></a>

### ML28-practice-11

Nếu chọn cấu hình tốt nhất sau nhiều lượt xem điểm kiểm tra, điểm đó còn là đánh giá độc lập không? Giải thích.


<a id="kiem-lai"></a>

# Kiểm lại ở buổi sau

Mở đúng mã bài vào buổi học tiếp theo. Ghi ngày, tự tính khi đã đóng mẫu rồi mới đối chiếu ở phụ lục đáp án.

<a id="kiem-lai-ml01"></a>

### ML01 · Chấm điểm từng hàng

Mỗi hàng của X là một mẫu, mỗi cột là một đặc trưng (feature). Nhân từng hàng với vectơ trọng số w bằng tích vô hướng (dot product), rồi cộng hệ số tự do (bias) b. Nộp một vectơ điểm theo thứ tự hàng.

**S** · `X = [[-2,1],[0,3]]  w = [3,2]  b = -1`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml02"></a>

### ML02 · Hiệp phương sai mẫu

Từ bảng X có ít nhất hai hàng, tính ma trận hiệp phương sai mẫu (sample covariance). Trừ đi trung bình của từng cột ngay trong cột đó. Với n hàng, chia tổng tích độ lệch cho n − 1. Nộp ma trận vuông theo thứ tự cột của X.

**S** · `X = [[1,5],[3,3],[5,1]]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml03"></a>

### ML03 · Chuẩn hóa từ tập huấn luyện

Với phép chuẩn hóa cực tiểu–cực đại (min–max scaling), tìm min và max của mỗi cột trên tập huấn luyện (training set) rồi áp dụng cho X. Nộp ma trận có cùng kích thước với X. Giá trị ngoài khoảng huấn luyện có thể nhỏ hơn 0 hoặc lớn hơn 1.

**S** · `train = [[1,-3],[5,5]]  X = [[7,1],[0,-5]]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml04"></a>

### ML04 · Tính tổn thất của một đường thẳng

Từ x, y, w và b, tính phần dư (residual) theo thứ tự dự đoán trừ giá trị thực. Nộp một số J bằng một nửa trung bình bình phương các phần dư. Mỗi mẫu có cùng trọng số.

**S** · `x = [0,1,3]  y = [-1,2,4]  w = 1  b = 0`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml05"></a>

### ML05 · Cập nhật trọng số trong một bước

Dùng hạ gradient trên cả lô (batch gradient descent) để cập nhật đường thẳng w·x + b. Trước hết, tính sai số của từng mẫu từ w và b ban đầu. Giữ nguyên các sai số ấy khi tính hai gradient, rồi mới cập nhật hai tham số bằng tốc độ học lr. Nộp [w_mới, b_mới] sau đúng một bước.

**S** · `x = [-1,3]  y = [0,6]  w = 1  b = 1  lr = 0.1`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml06"></a>

### ML06 · Chia một dãy chỉ số thành các lô

Chia hoán vị order thành các lô nhỏ (mini-batch) liên tiếp, mỗi lô tối đa size phần tử. Nộp danh sách các lô theo thứ tự đã cho, kể cả lô cuối ngắn hơn size.

**S** · `order = [2,5,0,1,3,4]  size = 4`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml07"></a>

### ML07 · Khớp đường hồi quy có hệ số tự do

Khớp bình phương tối thiểu (least squares) từ X và y. Thêm cột toàn 1 ở bên trái và gọi cùng bộ giải lstsq cho mọi lượt. Nộp vectơ hệ số với hệ số tự do đứng đầu. Khi có nhiều nghiệm, lấy nghiệm có chuẩn Euclid nhỏ nhất.

**S** · `X = [[0,0],[1,2],[2,4]]  y = [1,6,11]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml08"></a>

### ML08 · Tạo ma trận đặc trưng đa thức

Với mỗi giá trị x, tạo một hàng gồm các lũy thừa từ bậc 0 đến degree. Nộp ma trận đặc trưng đa thức (polynomial features), cột đầu là 1 và cột cuối là x mũ degree.

**S** · `x = [-2,1,0]  degree = 3`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml09"></a>

### ML09 · Từ điểm logit đến nhãn nhị phân

Nhận điểm logit, đổi từng điểm thành xác suất qua hàm sigmoid, rồi so với ngưỡng (threshold). Gán nhãn 1 nếu xác suất bằng hoặc vượt ngưỡng. Nộp vectơ nhãn 0/1 theo thứ tự đầu vào.

**S** · `logits = [0,-4,4]  threshold = 0.5`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml10"></a>

### ML10 · Tổn thất và gradient của hồi quy logistic

Với ma trận thiết kế A, nhãn y và hệ số w, tính tổn thất entropy chéo nhị phân (binary cross-entropy, BCE) trung bình và gradient theo w. Nộp [giá trị tổn thất, vectơ gradient] theo thứ tự cột của A.

**S** · `A = [[1,-1],[1,3]]  y = [0,1]  w = [1,-1]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml11"></a>

### ML11 · Một bước Newton cho hồi quy logistic

Tính gradient g và ma trận đạo hàm bậc hai (Hessian) H của BCE trung bình tại w. Giải hệ (H + damping·I)s = g rồi nộp vectơ w − s. Trong các lượt luyện, damping bằng 0 và hệ có nghiệm duy nhất.

**S** · `A = [[1,0],[1,3]]  y = [1,0]  w = [0,0]  damping = 0`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml12"></a>

### ML12 · Bỏ phiếu bằng các láng giềng gần nhất

Phân lớp theo k láng giềng gần nhất (k-nearest neighbors). Xếp các hàng của X theo khoảng cách Euclid đến q. Nếu bằng khoảng cách, giữ hàng xuất hiện trước. Nộp một nhãn 0 hoặc 1 sau khi bỏ phiếu. Hai bên bằng phiếu thì chọn 0.

**S** · `X = [[1],[5],[7]]  y = [0,1,0]  q = [6]  k = 2`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml13"></a>

### ML13 · Chia tập theo K phần

Kiểm định chéo K phần (K-fold cross-validation) dùng lần lượt mỗi đoạn của order làm tập xác thực. Nếu chia có dư, các đoạn đầu nhận thêm một hàng. Nộp danh sách các cặp [chỉ số huấn luyện, chỉ số xác thực], cùng thứ tự như order.

**S** · `order = [2,5,0,1,3,4]  k = 4`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml14"></a>

### ML14 · Đo sai số hồi quy

Từ y và dự đoán yhat, nộp bốn đại lượng theo thứ tự [sai số tuyệt đối trung bình (MAE), sai số bình phương trung bình (MSE), căn MSE (RMSE), hệ số xác định (R²)]. Nếu y hằng, ghi null cho R².

**S** · `y = [1,2,6]  yhat = [2,2,4]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml15"></a>

### ML15 · Đo chất lượng phân loại nhị phân

Lấy 1 làm lớp dương. Bạn có hai vectơ, y ghi nhãn thực và p ghi nhãn dự đoán. Từ đó, nộp bốn số theo thứ tự [tỷ lệ đúng (accuracy), độ chuẩn xác (precision), độ bao phủ (recall), điểm F1]. Nếu mẫu số của đại lượng nào bằng 0, ghi 0 ở đúng vị trí ấy. TP và TN là số dương đúng và âm đúng. FP và FN là số dương giả và âm giả.

**S** · `y = [1,0,1,0,1]  p = [1,1,0,0,0]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml16"></a>

### ML16 · Dựng các điểm trên đường ROC

Dựng đường đặc trưng hoạt động (ROC) từ nhãn nhị phân và điểm dự đoán. Bắt đầu ở [0,0], rồi hạ ngưỡng qua các điểm phân biệt từ cao xuống thấp. Nộp các cặp [tỷ lệ dương giả (FPR), tỷ lệ dương đúng (TPR)]. Nhận mọi điểm bằng ngưỡng.

**S** · `y = [0,1,1,0]  score = [0.3,0.6,0.6,0.8]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml17"></a>

### ML17 · Chọn bậc mô hình bằng sai số xác thực

Nhận các bậc cùng sai số huấn luyện và xác thực (validation loss). Chọn bậc có sai số xác thực nhỏ nhất, nếu hòa thì chọn bậc nhỏ hơn. Nộp [bậc, sai số xác thực trừ sai số huấn luyện] ở đúng bậc đã chọn.

**S** · `degrees = [3,1,2]  train_loss = [0,3,1]  val_loss = [4,4,6]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml18"></a>

### ML18 · Khớp hồi quy có phạt L2

Hồi quy Ridge (ridge regression) tối thiểu hóa tổng bình phương phần dư cộng lam nhân tổng bình phương các trọng số. Bỏ hệ số tự do khỏi phần phạt. Nộp [hệ số tự do, các trọng số]. Khi lam bằng 0, dùng bình phương tối thiểu.

**S** · `X = [[-1],[0],[1]]  y = [4,6,8]  lam = 6`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml19"></a>

### ML19 · Gán nhãn bằng perceptron

Với bộ phân loại perceptron, tính điểm z = Xw + b cho từng hàng. Nộp vectơ nhãn theo quy tắc z ≥ 0 cho nhãn 1, các điểm còn lại cho nhãn 0.

**S** · `X = [[2,-1],[0,1],[-1,0]]  w = [1,2]  b = 0`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml20"></a>

### ML20 · Tính ReLU và đạo hàm

Hàm kích hoạt tuyến tính chỉnh lưu (rectified linear unit, ReLU) cho max(0,z). Với kind bằng 'relu', nộp [giá trị hàm, đạo hàm] cho từng vị trí của z. Dùng đạo hàm quy ước bằng 0 tại z = 0.

**S** · `z = [0,3,-4,2]  kind = "relu"`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml21"></a>

### ML21 · Lan truyền tiến qua hai tầng

Lan truyền tiến (forward propagation) theo thứ tự XW₁ + b₁, ReLU, rồi HW₂ + b₂ với H là đầu ra tầng ẩn. Tầng cuối là tuyến tính. Nộp ma trận có một hàng cho mỗi mẫu và một cột cho mỗi đầu ra.

**S** · `X = [[-1],[2]]  W1 = [[2]]  b1 = [-1]  W2 = [[-1]]  b2 = [3]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml22"></a>

### ML22 · Lan truyền ngược trên cả lô

Lan truyền ngược (backpropagation) cho mạng có một nơron sigmoid ở mỗi tầng và BCE trung bình. Tính h và p cho tất cả các mẫu trước. Nộp bốn gradient trung bình theo thứ tự [w₁,b₁,w₂,b₂].

**S** · `x = [1,2,4]  y = [0,1,1]  params = [0,0,2,-1]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml23"></a>

### ML23 · Một vòng phân cụm Lloyd

Thực hiện một vòng của phân cụm K-means (K-means clustering) bằng thuật toán Lloyd. Gán mẫu vào tâm Euclid gần nhất, hòa chọn chỉ số nhỏ. Tính lại tâm từ các nhãn vừa gán, giữ tâm cũ nếu cụm rỗng. Nộp [nhãn, tâm mới, tổng bình phương khoảng cách đến tâm mới (SSE)].

**S** · `X = [[-2],[0],[2],[6]]  centers = [[-2],[2]]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml24"></a>

### ML24 · So sánh hai phân hoạch theo cặp

Dùng chỉ số Rand (Rand index) và Jaccard để so hai cách chia cụm. Xét từng cặp chỉ số i < j một lần. Rand tính tỷ lệ hai phân hoạch đưa ra cùng quyết định. Jaccard lấy số cặp cùng cụm ở cả hai chia cho số cặp cùng cụm ở ít nhất một. Nếu mẫu số bằng 0, lấy Jaccard = 1. Nộp [Rand,Jaccard].

**S** · `a = [0,0,1,1,2]  b = [3,4,4,4,5]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml25"></a>

### ML25 · Khớp các trục chính của PCA

Phân tích thành phần chính (principal component analysis, PCA) bắt đầu bằng trừ trung bình từng cột. Sắp các trục theo trị riêng giảm dần. Nộp [trung bình cột, ma trận có k trục theo cột, tỷ lệ phương sai của mỗi trục]. Mỗi tỷ lệ dùng tổng phương sai của tất cả các trục. Hai hướng ngược nhau trên cùng một trục đều hợp lệ.

**S** · `X = [[0,1],[2,3],[4,5]]  k = 1`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml26"></a>

### ML26 · Tìm điểm chia Gini tốt nhất

Với một đặc trưng x và nhãn nhị phân y, thử trung điểm của từng cặp giá trị x phân biệt liền nhau. Đưa x ≤ ngưỡng sang trái. Tính mức giảm độ hỗn tạp Gini (Gini impurity) có tính trọng số hai nhánh. Nộp [ngưỡng, mức giảm]. Hòa trong 10⁻¹² thì lấy ngưỡng nhỏ. Ghi null nếu mức giảm lớn nhất không vượt 10⁻¹².

**S** · `x = [0,1,3,4]  y = [0,1,1,0]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml27"></a>

### ML27 · Gộp phiếu từ các cây chưa thấy mẫu

Với mỗi hàng i, tìm các cây đã bỏ hàng ấy ra ngoài khi lấy mẫu có hoàn lại (out-of-bag, OOB). Đọc cột i của votes và chỉ đếm phiếu của những cây vừa tìm được. Nộp vectơ nhãn theo thứ tự hàng. Nếu hòa phiếu, lấy 0. Nếu mọi cây đều đã thấy hàng i, ghi −1.

**S** · `bags = [[0,0,0],[1,1,1],[1,2,2]]  votes = [[0,1,1],[1,0,0],[0,1,1]]  n = 3`  
Kết quả tự nộp ____________________

<a id="kiem-lai-ml28"></a>

### ML28 · Chuẩn hóa, dự đoán và đo MAE

Trong chuỗi xử lý hồi quy (regression pipeline), tính trung bình và độ lệch chuẩn tổng thể trên tập huấn luyện. Với cột hằng, dùng mẫu số 1. Dùng các thống kê ấy cho cả hai tập, khớp bình phương tối thiểu có hệ số tự do trên tập huấn luyện rồi nộp [vectơ dự đoán tập kiểm tra, MAE trên tập kiểm tra].

**S** · `X_train = [[-1],[1],[3]]  y_train = [0,4,8]  X_test = [[5],[7]]  y_test = [11,18]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp01"></a>

### MLP01 · Mã hóa một thuộc tính phân loại

Mã hóa một-nóng (one-hot encoding) dùng một cột cho mỗi mức học được từ train. Sắp các mức theo thứ tự từ điển. Với mức mới ở values, ghi một hàng toàn 0. Nộp [danh sách mức, ma trận mã hóa] theo thứ tự values.

**S** · `train = ["t","a","t"]  values = ["q","t","a"]`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp02"></a>

### MLP02 · Lọc cột theo phương sai

Bộ lọc phương sai (variance filter) giữ các cột có phương sai tổng thể trên train lớn hơn cutoff. Chọn lại các cột đó trong X theo thứ tự cũ. Nộp [danh sách chỉ số cột, ma trận X sau lọc]. Chỉ số đầu là 0.

**S** · `train = [[0,0,4],[4,2,4]]  X = [[8,2,7]]  cutoff = 1`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp03"></a>

### MLP03 · Gộp cụm theo khoảng cách gần nhất

Phân cụm phân cấp kết tụ (agglomerative clustering) bắt đầu với mỗi điểm là một cụm. Ở đề lõi, dùng liên kết đơn (single linkage), khoảng cách giữa hai cụm là khoảng cách nhỏ nhất giữa hai thành viên. Mỗi lần gộp i < j, giữ vị trí i và bỏ vị trí j. Hòa khoảng cách chọn cặp vị trí (i,j) nhỏ nhất. Nộp lịch sử [độ cao, danh sách chỉ số mẫu đã sắp tăng] cho đến khi còn một cụm.

**S** · `X = [5,1,3,9]  linkage = "single"`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp04"></a>

### MLP04 · Gán nhãn cụm mật độ trong một chiều

Khi phân cụm theo mật độ có nhiễu (DBSCAN, density-based spatial clustering of applications with noise), lân cận gồm mọi điểm cách không quá eps, kể cả chính nó. Điểm lõi (core) có ít nhất min_samples điểm trong lân cận. Duyệt lõi theo chỉ số tăng, nối các lõi kề nhau và gán các điểm biên (border) chưa nhãn. Nộp vectơ nhãn, cụm đầu mang số 0, nhiễu mang số −1.

**S** · `x = [0,2,4,6,15]  eps = 2  min_samples = 3`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp05"></a>

### MLP05 · Tính tổn thất bản lề và mục tiêu SVM

Với máy vectơ hỗ trợ (support vector machine, SVM), lấy nhãn −1 hoặc +1. Tổn thất bản lề (hinge loss) của một mẫu là max(0,1 − y·(Xw + b)). Nộp [vectơ tổn thất, 0,5 nhân bình phương độ dài w cộng C nhân tổng tổn thất].

**S** · `X = [[-1],[1],[2]]  y = [-1,-1,1]  w = [1]  b = 0  C = 2`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp06"></a>

### MLP06 · Dựng lại dữ liệu bằng SVD

Dùng phân rã giá trị kỳ dị (singular value decomposition, SVD) cho X sau khi trừ trung bình cột. Giữ k thành phần đầu, nhân lại rồi cộng trung bình từng cột. Nộp [ma trận dựng lại, tổng bình phương sai số dựng lại (SSE)].

**S** · `X = [[-2,-1],[4,-1],[1,-3],[1,1]]  k = 1`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp07"></a>

### MLP07 · Cập nhật một bước của bản đồ tự tổ chức

Trong bản đồ tự tổ chức (self-organizing map, SOM), chọn nút có vectơ trọng số gần x nhất theo Euclid, hòa lấy chỉ số nhỏ. Cập nhật nút thắng và mọi nút có khoảng cách chỉ số đến nó không quá radius bằng W + lr·(x − W). Nộp [chỉ số nút thắng, ma trận trọng số mới].

**S** · `weights = [[0],[6],[12]]  x = [9]  lr = 0.5  radius = 0`  
Kết quả tự nộp ____________________

<a id="kiem-lai-mlp08"></a>

### MLP08 · Đo độ tách cụm bằng Davies–Bouldin

Chỉ số Davies–Bouldin (Davies–Bouldin index, DB) dùng độ phân tán từng cụm là khoảng cách tuyệt đối trung bình đến tâm. Với mỗi cụm i, tính tỷ số (Sᵢ + Sⱼ)/khoảng cách hai tâm cho mọi j khác i, giữ tỷ số lớn nhất. Nộp trung bình của các giá trị lớn nhất ấy. Dùng ít nhất hai cụm có tâm phân biệt.

**S** · `x = [0,4,8,12,24,26]  labels = [0,0,1,1,2,2]`  
Kết quả tự nộp ____________________

<a id="dap-an-phieu"></a>

# Đáp án các phiếu

## Tự kiểm đầu vào

1. Hàm trả 4. Có thể dùng sum(xs) / len(xs).

2. Kích thước là (3,2), cột số 1 là [4,8,2].

3. Tính 2×3 − 1×4 + 1 = 3.

4. Đạo hàm là w − 1, tại w = 2 bằng 1.

<a id="dap-an-ml01"></a>

## ML01 · Đối chiếu

**B** · `[-2,0,10]`

**D1** · `[-5,-3,7]`

**D2** · `[24,32,16]`

**D3** · `[-1,-5]`

**E1** · `[2,3]`

**E2** · `[10,-4]`

**E3** · `[3,-3,7]`

**E4** · `[2,-2]`

**R1** · `[6,9]`

**R2** · `[-4,3]`

**R3** · `[14,2,-1]`

**R4** · `[1,-1]`

**S** · `[-5,5]`

Hàng đầu cho 2 × 2 + 7 × (−1) + 1 = −2. Làm tương tự với mỗi hàng còn lại.

Nếu mọi điểm cùng lệch một lượng, hãy kiểm tra b. Nếu số điểm bằng số cột, xem lại trục chứa mẫu.

**F.** Điểm là [1,1,2], chỉ số 2. Với hai hàng giống nhau cùng đứng đầu, chỉ số là 0.

### Hàm tham khảo

```python
import numpy as np

def score_rows(X, w, b):
    X, w = np.asarray(X), np.asarray(w)
    if X.ndim != 2 or min(X.shape) == 0 or w.shape != (X.shape[1],) or np.asarray(b).ndim != 0:
        raise ValueError("Shape không hợp lệ")
    return X @ w + b
```

### Ca kiểm hàm

```python
same(score_rows([[2, 1], [-1, 3]], [2, -1], 5), [8, 0])
```

```python
same(score_rows([[4]], [0.5], -2), [0])
```

```python
rejects(score_rows, [1, 2], [1, 2], 0)
```

```python
rejects(score_rows, [[1, 2]], [1], 0)
```

<a id="dap-an-ml02"></a>

## ML02 · Đối chiếu

**B** · `[[4,2],[2,4]]`

**D1** · `[[1,-2],[-2,4]]`

**D2** · `[[2,4],[4,8]]`

**D3** · `[[9]]`

**E1** · `[[4,4],[4,4]]`

**E2** · `[[2,-4],[-4,8]]`

**E3** · `[[0,0],[0,4]]`

**E4** · `[[9]]`

**R1** · `[[1,3],[3,9]]`

**R2** · `[[8,-8],[-8,8]]`

**R3** · `[[0,0],[0,25]]`

**R4** · `[[6.333333333333]]`

**S** · `[[4,-4],[-4,4]]`

Hai cột của mẫu có trung bình là 3 và 2. Tổng tích độ lệch giữa hai cột là 4, nên hai ô ngoài đường chéo cùng bằng 2.

Nếu ma trận chỉ còn một nửa giá trị mong đợi trên bộ hai hàng, kiểm tra mẫu số. Hãy lấy trung bình theo cột.

**F.** Ma trận tổng thể là [[1,−1],[−1,1]]. Với n = 2, ma trận mẫu có mọi phần tử gấp đôi.

### Hàm tham khảo

```python
import numpy as np

def sample_cov(X):
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or X.shape[0] < 2 or X.shape[1] == 0:
        raise ValueError("Cần ít nhất hai mẫu và một đặc trưng")
    centered = X - X.mean(axis=0)
    return centered.T @ centered / (len(X) - 1)
```

### Ca kiểm hàm

```python
same(sample_cov([[1, 2], [3, 0]]), [[2, -2], [-2, 2]])
```

```python
same(sample_cov([[2], [4], [6]]), [[4]])
```

```python
same(sample_cov([[2, 1], [2, 3]]), [[0, 0], [0, 2]])
```

```python
rejects(sample_cov, [[1, 2]])
```

<a id="dap-an-ml03"></a>

## ML03 · Đối chiếu

**B** · `[[0.5,0.25],[1,1.5]]`

**D1** · `[[0.25,0.75],[0.75,1.75]]`

**D2** · `[[1,0.375],[1.5,1]]`

**D3** · `[[-0.5,2]]`

**E1** · `[[0.25],[0.75]]`

**E2** · `[[-0.5,2],[0.5,-0.5]]`

**E3** · `[[0.5,0.5],[0.75,0.25]]`

**E4** · `[[1,0]]`

**R1** · `[[0.3333333333333],[0.5]]`

**R2** · `[[-0.5,2],[0.25,-0.25]]`

**R3** · `[[0.25,0.75]]`

**R4** · `[[0,1]]`

**S** · `[[1.5,0.5],[-0.25,-0.25]]`

Cột thứ hai của train trải từ 2 đến 6. Giá trị 8 trong X trở thành (8 − 2) / (6 − 2) = 1,5.

Nếu mọi kết quả đều nằm trong [0,1], kiểm tra xem bạn có dùng min và max của X hoặc cắt giá trị ở hai đầu không.

**F.** Dùng thống kê huấn luyện cho [1,2]. Tính lại trên lô kiểm tra cho [0,1] và làm mất thông tin rằng 20 vượt miền huấn luyện.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(scale_from_train([[1, 10], [3, 20]], [[0, 25]]), [[-0.5, 1.5]])
```

```python
same(scale_from_train([[0], [4]], [[2], [4]]), [[0.5], [1]])
```

```python
same(scale_from_train([[0], [4]], np.empty((0, 1))), np.empty((0, 1)))
```

```python
rejects(scale_from_train, [[1, 1], [1, 2]], [[2, 3]])
```

<a id="dap-an-ml04"></a>

## ML04 · Đối chiếu

**B** · `6.5`

**D1** · `2.5`

**D2** · `2.5`

**D3** · `2.5`

**E1** · `0`

**E2** · `1`

**E3** · `0.3333333333333`

**E4** · `0`

**R1** · `0.25`

**R2** · `1.25`

**R3** · `0.8333333333333`

**R4** · `0.25`

**S** · `0.5`

Hai phần dư là −1 và −5. Bình phương rồi cộng cho 26. Chia cho hai mẫu và chia đôi cho J = 6,5.

Nếu kết quả lớn gấp đôi, xem lại hệ số 1/2. Bình phương từng phần dư trước khi lấy trung bình.

**F.** J lần lượt là 1 và 0,5. Sai số tuyệt đối trung bình cùng bằng 1. Bình phương làm phần dư lớn đóng góp mạnh hơn.

### Hàm tham khảo

```python
import numpy as np

def half_mse(x, y, w, b):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or x.size == 0 or x.shape != y.shape:
        raise ValueError("Cần hai vector cùng độ dài dương")
    return float(np.mean((w * x + b - y) ** 2) / 2)
```

### Ca kiểm hàm

```python
same(half_mse([0, 2], [0, 4], 2, 0), 0)
```

```python
same(half_mse([0, 2], [1, 1], 1, 0), 0.5)
```

```python
same(half_mse([2], [1], -1, 1), 2)
```

```python
rejects(half_mse, [], [], 0, 0)
```

<a id="dap-an-ml05"></a>

## ML05 · Đối chiếu

**B** · `[0.5,0.3]`

**D1** · `[1,0.6]`

**D2** · `[1.25,0.65]`

**D3** · `[0.3,0.1]`

**E1** · `[1.2,0.5]`

**E2** · `[1.4,1.2]`

**E3** · `[2,-1]`

**E4** · `[-0.4,0]`

**R1** · `[2.4,1]`

**R2** · `[1.625,0.125]`

**R3** · `[2,1]`

**R4** · `[-0.6,0]`

**S** · `[1.3,1.1]`

Với hai sai số −1 và −5, gradient theo w là −5 và theo b là −3. Tốc độ học 0,1 cho w = 0,5 và b = 0,3.

Nếu w đúng mà b sai, kiểm tra xem hai gradient có cùng đọc sai số cũ không. Nhân sai số với x chỉ khi tính gradient theo w.

**F.** Cặp sai là [1.4,1.16], cặp đúng là [1.4,1.2]. Tính cả hai gradient trước dòng thay đổi w. Kiểm tra lại bằng một bộ số có trung bình x khác 0.

### Hàm tham khảo

```python
import numpy as np

def gd_step(x, y, w, b, lr):
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    if x.ndim != 1 or x.size == 0 or x.shape != y.shape or not np.isfinite(lr) or lr < 0:
        raise ValueError("Đầu vào không hợp lệ")
    error = w * x + b - y
    return float(w - lr * np.mean(error * x)), float(b - lr * error.mean())
```

### Ca kiểm hàm

```python
same(gd_step([1, 3], [2, 4], 0, 0, 0.1), [0.7, 0.3])
```

```python
same(gd_step([1, 2], [3, 5], 2, 1, 0.5), [2, 1])
```

```python
same(gd_step([1], [2], 3, 4, 0), [3, 4])
```

```python
rejects(gd_step, [1], [1], 0, 0, -1)
```

<a id="dap-an-ml06"></a>

## ML06 · Đối chiếu

**B** · `[[3,0],[4,1],[2]]`

**D1** · `[[3,0,4],[1,2]]`

**D2** · `[[4,2],[0,3],[1]]`

**D3** · `[[3],[0],[4],[1],[2]]`

**E1** · `[[2,0],[1,3]]`

**E2** · `[[3,1,4],[0,2]]`

**E3** · `[[4,0],[2,1],[3]]`

**E4** · `[[1,0]]`

**R1** · `[[1,3],[0,2]]`

**R2** · `[[0,3],[1,4],[2]]`

**R3** · `[[3,2,0],[1]]`

**R4** · `[[2,0,1]]`

**S** · `[[2,5,0,1],[3,4]]`

Cắt [3,0,4,1,2] sau phần tử thứ hai và thứ tư. Chỉ số 2 còn lại tạo thành lô cuối.

Nếu thiếu một chỉ số, kiểm tra lát cắt cuối. Duyệt theo vị trí trong order, giữ nguyên giá trị chỉ số ở từng vị trí.

**F.** Hai lô là [1,0] và [2]. Gradient lô tương ứng là 5 và 5. Lô cuối chia cho 1.

### Hàm tham khảo

```python
import numpy as np

def split_batches(order, size):
    if not isinstance(size, (int, np.integer)) or size < 1 or sorted(order) != list(range(len(order))):
        raise ValueError("Size hoặc hoán vị không hợp lệ")
    return [order[start:start + size] for start in range(0, len(order), size)]
```

### Ca kiểm hàm

```python
assert split_batches([2, 0, 1], 2) == [[2, 0], [1]]
```

```python
assert split_batches([], 1) == []
```

```python
assert split_batches([1, 0], 9) == [[1, 0]]
```

```python
rejects(split_batches, [0, 0], 2)
```

```python
rejects(split_batches, [0], 0)
```

<a id="dap-an-ml07"></a>

## ML07 · Đối chiếu

**B** · `[2,3,-1]`

**D1** · `[1,2,3]`

**D2** · `[2,1.5,-1]`

**D3** · `[-2,4,3]`

**E1** · `[3,2]`

**E2** · `[2,2,2]`

**E3** · `[1,-1,3]`

**E4** · `[2,0.5]`

**R1** · `[-1,3]`

**R2** · `[1,1,1]`

**R3** · `[3,-1,2]`

**R4** · `[2,1.25]`

**S** · `[1,1,2]`

Ba hàng mẫu cho b = 2, b + w₁ = 5 và b + w₂ = 1. Vectơ trả về là [2,3,−1].

Nếu hai cột giống nhau, tổng hai hệ số có thể đúng dù từng hệ số sai. Hai cột trùng nhau nhận phần bằng nhau trong nghiệm chuẩn nhỏ nhất.

**F.** [1,2,0] và [1,0,2] đều khớp. Nghiệm chuẩn nhỏ nhất là [1,1,1]. Hai cột trùng nhau khiến A.T @ A suy biến.

### Hàm tham khảo

```python
import numpy as np

def fit_linear(X, y):
    X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),) or not np.isfinite(X).all() or not np.isfinite(y).all():
        raise ValueError("Shape không hợp lệ")
    A = np.column_stack([np.ones(len(X)), X])
    return np.linalg.lstsq(A, y, rcond=None)[0]
```

### Ca kiểm hàm

```python
same(fit_linear([[0], [1], [2]], [2, 5, 8]), [2, 3])
```

```python
same(fit_linear([[0, 0], [1, 1], [2, 2]], [1, 3, 5]), [1, 1, 1])
```

```python
same(fit_linear([[0, 0], [1, 0], [0, 1]], [1, 3, -2]), [1, 2, -3])
```

```python
rejects(fit_linear, [[1], [2]], [1])
```

<a id="dap-an-ml08"></a>

## ML08 · Đối chiếu

**B** · `[[1,-2,4],[1,0,0],[1,2,4]]`

**D1** · `[[1,-2,4,-8],[1,0,0,0],[1,2,4,8]]`

**D2** · `[[1,-1,1],[1,1,1],[1,3,9]]`

**D3** · `[[1],[1],[1]]`

**E1** · `[[1,-1,1,-1],[1,2,4,8]]`

**E2** · `[[1,0,0],[1,-2,4],[1,3,9]]`

**E3** · `[[1],[1]]`

**E4** · `[[1,-3],[1,1]]`

**R1** · `[[1,1,1,1],[1,-3,9,-27]]`

**R2** · `[[1,-1,1],[1,0,0],[1,4,16]]`

**R3** · `[[1],[1],[1]]`

**R4** · `[[1,2],[1,0],[1,-1]]`

**S** · `[[1,-2,4,-8],[1,1,1,1],[1,0,0,0]]`

Hàng ứng với −2 là [1,−2,4]. Hàng ứng với 0 là [1,0,0].

Nếu thiếu một cột, đếm cả bậc 0. Giữ dấu âm ở lũy thừa lẻ và giữ nguyên thứ tự mẫu.

**F.** Hai dự đoán là −2 và 1. Mỗi hệ số phải đi cùng đúng lũy thừa của nó.

### Hàm tham khảo

```python
import numpy as np

def poly_features(x, degree):
    x = np.asarray(x, dtype=float)
    if x.ndim != 1 or not isinstance(degree, (int, np.integer)) or degree < 0:
        raise ValueError("Đầu vào không hợp lệ")
    return np.vander(x, degree + 1, increasing=True)
```

### Ca kiểm hàm

```python
same(poly_features([-2, 0, 2], 3), [[1,-2,4,-8],[1,0,0,0],[1,2,4,8]])
```

```python
same(poly_features([4, -1], 0), [[1], [1]])
```

```python
same(poly_features([], 2), np.empty((0, 3)))
```

```python
rejects(poly_features, [[2]], 2)
```

<a id="dap-an-ml09"></a>

## ML09 · Đối chiếu

**B** · `[0,1,1]`

**D1** · `[0,0,1]`

**D2** · `[0,1,1]`

**D3** · `[1,1,1]`

**E1** · `[0,1,1]`

**E2** · `[0,1,1,1]`

**E3** · `[1,0,0]`

**E4** · `[1,1,0]`

**R1** · `[0,0,1]`

**R2** · `[1,1,0,1]`

**R3** · `[0,0,1]`

**R4** · `[1,0,1]`

**S** · `[1,0,1]`

Ba điểm −1, 0 và 2 cho xác suất xấp xỉ 0,269, 0,5 và 0,881. Ở ngưỡng 0,5, nhãn là [0,1,1].

Nếu chỉ sai ở logit 0, kiểm tra dấu lớn hơn hoặc bằng. Nếu các điểm khác sai, kiểm tra xem đã đổi logit thành xác suất chưa.

**F.** Điểm biên là −1 và 1. Ba nhãn lần lượt là [1,0,1].

### Hàm tham khảo

```python
import numpy as np

def logistic_labels(logits, threshold):
    logits = np.asarray(logits, dtype=float)
    if logits.ndim != 1 or not np.all(np.isfinite(logits)) or not 0 < threshold < 1:
        raise ValueError("Logit hoặc threshold không hợp lệ")
    p = np.exp(-np.logaddexp(0, -logits))
    return (p >= threshold).astype(int)
```

### Ca kiểm hàm

```python
same(logistic_labels([-1000, 0, 1000], 0.5), [0, 1, 1])
```

```python
same(logistic_labels([-1, 0, 1, 2], 0.8), [0, 0, 0, 1])
```

```python
same(logistic_labels([0], 0.1), [1])
```

```python
rejects(logistic_labels, [0], 1)
```

<a id="dap-an-ml10"></a>

## ML10 · Đối chiếu

**B** · `[0.377778959707,[-0.1167538335507,-0.1691157551381]]`

**D1** · `[0.7111122930404,[-0.1167538335507,0.1642175781953]]`

**D2** · `[0.6931471805599,[-0.1666666666667,-0.5]]`

**D3** · `[0.1629256833783,[-0.06572145750848,-0.2165416283156]]`

**E1** · `[0.6931471805599,[0,-1]]`

**E2** · `[0.6931471805599,[0.1666666666667,1]]`

**E3** · `[1.313261687518,[0,0.73105857863]]`

**E4** · `[1.313261687518,[0.73105857863,1.46211715726]]`

**R1** · `[0.6931471805599,[0,1.5]]`

**R2** · `[0.6931471805599,[-0.1666666666667,-1.166666666667]]`

**R3** · `[0.2200948492806,[0.07486924967394,0.2536736327071]]`

**R4** · `[1.313261687518,[-0.73105857863,-1.46211715726]]`

**S** · `[2.126928011043,[0,-1.761594155956]]`

Các logit của mẫu là −1, 0 và 2. Ở hàng giữa, p − y bằng −0,5. Hàng này góp vào gradient hệ số tự do và góp 0 vào gradient hệ số còn lại.

Nếu cả gradient hoặc tổn thất lớn gấp số hàng, kiểm tra phép lấy trung bình. Gradient dùng p − y.

**F.** Gradient là sigmoid(1) − 0,5, xấp xỉ 0,23105858. Tính [L(w+h) − L(w−h)]/(2h) và đối chiếu.

### Hàm tham khảo

```python
import numpy as np

def bce_and_gradient(A, y, w):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    if A.ndim != 2 or min(A.shape) == 0 or y.shape != (len(A),) or w.shape != (A.shape[1],) or not np.isin(y, [0, 1]).all():
        raise ValueError("Shape hoặc nhãn không hợp lệ")
    z = A @ w
    p = np.exp(-np.logaddexp(0, -z))
    loss = np.logaddexp(0, (1 - 2 * y) * z).mean()
    return float(loss), A.T @ (p - y) / len(y)
```

### Ca kiểm hàm

```python
loss, g = bce_and_gradient([[1, 1], [1, 3]], [0, 1], [0, 0])
same(loss, np.log(2))
same(g, [0, -0.5])
```

```python
loss, g = bce_and_gradient([[1], [-1]], [1, 0], [-1000])
same(loss, 1000)
same(g, [-1])
```

```python
rejects(bce_and_gradient, [[1]], [2], [0])
```

<a id="dap-an-ml11"></a>

## ML11 · Đối chiếu

**B** · `[0.6153572590407,1.809483986655]`

**D1** · `[0.6547038893793,0.1867974116699]`

**D2** · `[0.2857142857143,1.142857142857]`

**D3** · `[1.175497850645,1.566450479498]`

**E1** · `[0,1]`

**E2** · `[-2,2]`

**E3** · `[0,-2.718281828459]`

**E4** · `[0.2857142857143,0.2857142857143]`

**R1** · `[0,-0.6666666666667]`

**R2** · `[-4,2]`

**R3** · `[0.6724923512946,-1.695387089877]`

**R4** · `[-0.6666666666667,0]`

**S** · `[2,-1.333333333333]`

Dùng cùng xác suất như ở ML10. Hàng có logit 0 có trọng số p(1−p) = 0,25 trong H. Giải hệ để tìm bước hiệu chỉnh cho cả hai hệ số.

Nếu chỉ đổi độ lớn gradient, hãy kiểm tra bước giải hệ. H chứa cả các tích giữa hai cột của A.

**F.** Thêm 0,5 vào hai ô đường chéo. Gradient là [−0.5,−0.5], nghiệm hiệu chỉnh là [−0.5,−0.5], tham số mới là [0.5,0.5].

### Hàm tham khảo

```python
import numpy as np

def newton_step(A, y, w, damping=0.0):
    A, y, w = (np.asarray(v, dtype=float) for v in (A, y, w))
    if A.ndim != 2 or min(A.shape) == 0 or y.shape != (len(A),) or w.shape != (A.shape[1],) or not np.isin(y, [0, 1]).all() or not np.isfinite(damping) or damping < 0:
        raise ValueError("Đầu vào không hợp lệ")
    p = np.exp(-np.logaddexp(0, -(A @ w)))
    g = A.T @ (p - y) / len(y)
    H = A.T @ ((p * (1 - p))[:, None] * A) / len(y)
    return w - np.linalg.solve(H + damping * np.eye(len(w)), g)
```

### Ca kiểm hàm

```python
same(newton_step([[1, -2], [1, 2]], [0, 1], [0, 0]), [0, 1])
```

```python
same(newton_step([[1, 1], [1, 1]], [1, 1], [0, 0], 0.5), [0.5, 0.5])
```

```python
rejects(newton_step, [[1]], [1], [0], -0.1)
```

```python
with np.testing.assert_raises(np.linalg.LinAlgError):
    newton_step([[1, 1], [1, 1]], [0, 1], [0, 0])
```

<a id="dap-an-ml12"></a>

## ML12 · Đối chiếu

**B** · `1`

**D1** · `0`

**D2** · `0`

**D3** · `0`

**E1** · `0`

**E2** · `1`

**E3** · `0`

**E4** · `1`

**R1** · `1`

**R2** · `0`

**R3** · `1`

**R4** · `0`

**S** · `0`

Với q = 3, bình phương khoảng cách là 9, 1, 4 và 25. Ba hàng gần nhất mang nhãn 0, 1 và 1.

Nếu sai ở lượt E2, hãy ghi cả chỉ số lẫn khoảng cách trước khi chọn k hàng. Hòa khoảng cách và hòa phiếu là hai bước khác nhau.

**F.** Euclid chọn [2,2] vì √8 < 3 nên nhãn 1. Manhattan chọn [3,0] vì 3 < 4 nên nhãn 0.

### Hàm tham khảo

```python
import numpy as np

def knn_one(X, y, q, k):
    X, q, y = np.asarray(X, dtype=float), np.asarray(q, dtype=float), np.asarray(y)
    if X.ndim != 2 or X.shape[1] == 0 or q.shape != (X.shape[1],) or y.shape != (len(X),) or not np.isin(y, [0, 1]).all() or not isinstance(k, (int, np.integer)) or not 1 <= k <= len(X):
        raise ValueError("Đầu vào không hợp lệ")
    d2 = ((X - q) ** 2).sum(axis=1)
    near = np.argsort(d2, kind="stable")[:k]
    return int(2 * y[near].sum() > k)
```

### Ca kiểm hàm

```python
same(knn_one([[0], [1], [9]], [0, 1, 1], [0.9], 1), 1)
```

```python
same(knn_one([[1], [-1]], [1, 0], [0], 1), 1)
```

```python
same(knn_one([[1], [-1]], [1, 0], [0], 2), 0)
```

```python
rejects(knn_one, [[1]], [0], [1], 2)
```

<a id="dap-an-ml13"></a>

## ML13 · Đối chiếu

**B** · `[[[4,1,2],[3,0]],[[3,0,2],[4,1]],[[3,0,4,1],[2]]]`

**D1** · `[[[1,2],[3,0,4]],[[3,0,4],[1,2]]]`

**D2** · `[[[0,3,1],[4,2]],[[4,2,1],[0,3]],[[4,2,0,3],[1]]]`

**D3** · `[[[0,4,1,2],[3]],[[3,4,1,2],[0]],[[3,0,1,2],[4]],[[3,0,4,2],[1]],[[3,0,4,1],[2]]]`

**E1** · `[[[1,3],[2,0]],[[2,0],[1,3]]]`

**E2** · `[[[0,2],[3,1,4]],[[3,1,4],[0,2]]]`

**E3** · `[[[2,1,3],[4,0]],[[4,0,3],[2,1]],[[4,0,2,1],[3]]]`

**E4** · `[[[0,2],[1]],[[1,2],[0]],[[1,0],[2]]]`

**R1** · `[[[0,2],[1,3]],[[1,3],[0,2]]]`

**R2** · `[[[1,4,2],[0,3]],[[0,3,2],[1,4]],[[0,3,1,4],[2]]]`

**R3** · `[[[0,1],[3,2]],[[3,2,1],[0]],[[3,2,0],[1]]]`

**R4** · `[[[0,1],[2]],[[2,1],[0]],[[2,0],[1]]]`

**S** · `[[[0,1,3,4],[2,5]],[[2,5,3,4],[0,1]],[[2,5,0,1,4],[3]],[[2,5,0,1,3],[4]]]`

Ba tập xác thực của mẫu lần lượt là [3,0], [4,1] và [2]. Ở lượt đầu, các chỉ số huấn luyện là [4,1,2].

Nếu đặt phần dư ở cuối, kích thước các phần đầu sẽ sai. Giữ nguyên thứ tự của order khi ghép các phần huấn luyện.

**F.** MSE trên mọi mẫu là (2×1 + 2×4 + 1×9)/5 = 3,8. Trung bình ba phần là 14/3.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
assert kfold_indices([2, 0, 1], 2) == [([1], [2, 0]), ([2, 0], [1])]
```

```python
assert kfold_indices([1, 0], 2) == [([0], [1]), ([1], [0])]
```

```python
rejects(kfold_indices, [0, 0], 2)
```

```python
rejects(kfold_indices, [0, 1], 3)
```

<a id="dap-an-ml14"></a>

## ML14 · Đối chiếu

**B** · `[1,1.666666666667,1.290994448736,0.375]`

**D1** · `[1,1.666666666667,1.290994448736,0.375]`

**D2** · `[2,4.666666666667,2.160246899469,0.25]`

**D3** · `[0,0,0,1]`

**E1** · `[1.5,2.5,1.581138830084,-1.5]`

**E2** · `[0.6666666666667,0.6666666666667,0.8164965809277,null]`

**E3** · `[1,1,1,0.8333333333333]`

**E4** · `[2,4,2,-3]`

**R1** · `[1,2,1.414213562373,0.1111111111111]`

**R2** · `[1.5,2.5,1.581138830084,null]`

**R3** · `[1.333333333333,2,1.414213562373,0.6666666666667]`

**R4** · `[4,16,4,-3]`

**S** · `[1,1.666666666667,1.290994448736,0.6428571428571]`

Ba phần dư là 1, 0 và −2. Giá trị tuyệt đối có tổng 3, còn bình phương có tổng 5. Lấy căn sau khi đã tính MSE.

Nếu R² chưa xác định vì y hằng, vẫn tính ba đại lượng đầu. RMSE là căn của trung bình các bình phương.

**F.** Ba đại lượng đầu lần lượt nhân 10, 100, 10. R² giữ giá trị −1 do cả tử và mẫu trong SSE/SST cùng nhân 100.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(regression_metrics([1, 3], [1, 5]), [1, 2, np.sqrt(2), -1])
```

```python
assert regression_metrics([2, 2], [2, 2]) == (0, 0, 0, None)
```

```python
same(regression_metrics([0, 2], [1, 1]), [1, 1, 1, 0])
```

```python
rejects(regression_metrics, [], [])
```

<a id="dap-an-ml15"></a>

## ML15 · Đối chiếu

**B** · `[0.6,0.5,0.5,0.5]`

**D1** · `[0.8,0.6666666666667,1,0.8]`

**D2** · `[1,1,1,1]`

**D3** · `[0.6,0,0,0]`

**E1** · `[0.5,0.6666666666667,0.6666666666667,0.6666666666667]`

**E2** · `[0.5,1,0.3333333333333,0.5]`

**E3** · `[0.6666666666667,0,0,0]`

**E4** · `[0.6,0.5,1,0.6666666666667]`

**R1** · `[1,1,1,1]`

**R2** · `[0.6,1,0.5,0.6666666666667]`

**R3** · `[0.75,0,0,0]`

**R4** · `[0.5,0.3333333333333,1,0.5]`

**S** · `[0.4,0.5,0.3333333333333,0.4]`

Ở mẫu chạy thử có 1 dương đúng, 1 dương giả, 1 âm giả và 2 âm đúng. Tỷ lệ đúng là 3/5. Ba điểm còn lại cùng bằng 1/2.

Nếu precision và recall bị đảo, viết riêng số dương dự đoán và số dương thực tế. F1 có thể tính bằng 2TP/(2TP + FP + FN).

**F.** Chi phí A là 9, B là 11. Chọn A theo quy tắc chi phí đã cho.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(binary_metrics([1,1,0,0], [1,0,1,0]), [0.5,0.5,0.5,0.5])
```

```python
same(binary_metrics([1,0,0,0], [0,0,0,0]), [0.75,0,0,0])
```

```python
same(binary_metrics([1,1,0], [1,0,0]), [2/3,1,0.5,2/3])
```

```python
same(binary_metrics([0], [0]), [1,0,0,0])
```

```python
rejects(binary_metrics, [1], [2])
```

<a id="dap-an-ml16"></a>

## ML16 · Đối chiếu

**B** · `[[0,0],[0,0.5],[0.5,0.5],[0.5,1],[1,1]]`

**D1** · `[[0,0],[0,0.5],[0.5,1],[1,1]]`

**D2** · `[[0,0],[0.5,0],[0.5,0.5],[0.5,1],[1,1]]`

**D3** · `[[0,0],[0,0.5],[0.5,0.5],[0.5,1],[1,1]]`

**E1** · `[[0,0],[1,0],[1,0.5],[1,1]]`

**E2** · `[[0,0],[0.5,0.5],[0.5,1],[1,1]]`

**E3** · `[[0,0],[0.5,0],[0.5,1],[1,1]]`

**E4** · `[[0,0],[1,1]]`

**R1** · `[[0,0],[0,0.5],[1,0.5],[1,1]]`

**R2** · `[[0,0],[0.5,0.5],[1,0.5],[1,1]]`

**R3** · `[[0,0],[0,1],[0.5,1],[1,1]]`

**R4** · `[[0,0],[1,0.5],[1,1]]`

**S** · `[[0,0],[0.5,0],[0.5,1],[1,1]]`

Ở ngưỡng 0,9 chỉ mẫu đầu được chọn. Hai âm thực đều còn ở phía âm và một trong hai dương thực đã được nhận, nên điểm kế là [0,0.5].

Nếu có quá nhiều hàng, nhóm các điểm bằng nhau trước khi hạ ngưỡng. FPR chia cho số âm thực, TPR chia cho số dương thực.

**F.** Ba dải cho 0, 0,375 và 0,5. AUC bằng 0,875.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(roc_curve_points([1, 0, 1, 0], [0.9, 0.8, 0.8, 0.1]), [[0,0],[0,0.5],[0.5,1],[1,1]])
```

```python
same(roc_curve_points([0, 1], [4, 4]), [[0,0],[1,1]])
```

```python
same(roc_curve_points([0, 1], [2, 1]), [[0,0],[1,0],[1,1]])
```

```python
rejects(roc_curve_points, [1, 1], [0.4, 0.8])
```

<a id="dap-an-ml17"></a>

## ML17 · Đối chiếu

**B** · `[2,1]`

**D1** · `[1,0]`

**D2** · `[2,2]`

**D3** · `[1,1]`

**E1** · `[3,1]`

**E2** · `[1,1]`

**E3** · `[0,-1]`

**E4** · `[3,-1]`

**R1** · `[1,-1]`

**R2** · `[2,1]`

**R3** · `[1,-1]`

**R4** · `[2,-2]`

**S** · `[1,1]`

Sai số xác thực nhỏ nhất là 3 ở bậc 2. Sai số huấn luyện tại đó là 2, nên độ chênh bằng 1.

Khi hòa, so giá trị của bậc. Sau khi chọn, lấy cả hai sai số tại cùng một vị trí.

**F.** Chọn bậc 2. Ở bậc 4, sai số huấn luyện giảm nhưng sai số xác thực tăng từ 3 lên 8, dấu hiệu của quá khớp.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(pick_degree([3,0,2,1], [0,9,1,4], [8,10,2,5]), [2,1])
```

```python
same(pick_degree([4,1], [0,2], [3,3]), [1,1])
```

```python
same(pick_degree([2], [2], [1]), [2,-1])
```

```python
rejects(pick_degree, [1,1], [1,2], [2,1])
```

<a id="dap-an-ml18"></a>

## ML18 · Đối chiếu

**B** · `[2,1]`

**D1** · `[2,0.6666666666667]`

**D2** · `[3,1]`

**D3** · `[2,0.8]`

**E1** · `[3,1]`

**E2** · `[5,1]`

**E3** · `[1,3]`

**E4** · `[1.6,0.6666666666667,1.2]`

**R1** · `[2,0.5]`

**R2** · `[6,1]`

**R3** · `[-3,3]`

**R4** · `[2,0.8,1]`

**S** · `[6,0.5]`

Trong mẫu, X có trung bình 0 nên b bằng trung bình y, tức 2. Trọng số còn lại là 4/(2+2) = 1.

Nếu hệ số tự do cũng co về 0, kiểm tra ô đầu của ma trận phạt. Dùng tổng bình phương phần dư theo đúng quy ước của bài.

**F.** Bản đúng cho b = 4. Phạt cả b cho nghiệm b = 8/(2+2) = 2. Trọng số bằng 0 ở cả hai.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(ridge_fit([[-2], [0], [2]], [0, 4, 8], 8), [4,1])
```

```python
same(ridge_fit([[0],[0]], [1,5], 100), [3,0])
```

```python
same(ridge_fit([[0,0],[1,1],[2,2]], [1,3,5], 0), [1,1,1])
```

```python
rejects(ridge_fit, [[1]], [2], -1)
```

<a id="dap-an-ml19"></a>

## ML19 · Đối chiếu

**B** · `[1,1,1]`

**D1** · `[0,1,0]`

**D2** · `[1,1,1]`

**D3** · `[0,1,1]`

**E1** · `[1,0]`

**E2** · `[0,1,1]`

**E3** · `[1,0,1]`

**E4** · `[0,0]`

**R1** · `[0,0]`

**R2** · `[1,1,1]`

**R3** · `[0,1,0]`

**R4** · `[1,1]`

**S** · `[1,1,0]`

Các hàng mẫu cho điểm 0, 1, 0. Cả ba đều thuộc phía dương khi dùng quy tắc đã cho.

Nếu sai ở điểm trên ranh giới, thử riêng z = 0. Cộng b trước khi so dấu.

**F.** Chẳng hạn w = [1,1], b = −1,5 cho điểm [−1.5,−0.5,−0.5,0.5] và nhãn [0,0,0,1].

### Hàm tham khảo

```python
import numpy as np

def perceptron(X, w, b):
    X, w = np.asarray(X), np.asarray(w)
    if X.ndim != 2 or X.shape[1] == 0 or w.shape != (X.shape[1],):
        raise ValueError("Shape không hợp lệ")
    return (X @ w + b >= 0).astype(int)
```

### Ca kiểm hàm

```python
same(perceptron([[0,0],[1,0],[1,1]], [2,-1], -1), [0,1,1])
```

```python
same(perceptron([[-1],[0],[2]], [1], 0), [0,1,1])
```

```python
same(perceptron([[2],[3]], [0], -1), [0,0])
```

```python
rejects(perceptron, [[1,2]], [1], 0)
```

<a id="dap-an-ml20"></a>

## ML20 · Đối chiếu

**B** · `[[0,0,2],[0,0,1]]`

**D1** · `[[0,1,3],[0,1,1]]`

**D2** · `[[0,0,4],[0,0,1]]`

**D3** · `[[1,2,0,0],[1,1,0,0]]`

**E1** · `[[0,2],[0,1]]`

**E2** · `[[0,0,5],[0,0,1]]`

**E3** · `[[2,4,0],[1,1,0]]`

**E4** · `[[0,0],[0,0]]`

**R1** · `[[1,0],[1,0]]`

**R2** · `[[0,4,0],[0,1,0]]`

**R3** · `[[7,0,1],[1,0,1]]`

**R4** · `[[0,0,0],[0,0,0]]`

**S** · `[[0,3,0,2],[0,1,0,1]]`

Với z = [−1,0,2], giá trị là [0,0,2] và đạo hàm là [0,0,1].

Nếu đạo hàm ở 0 bằng 1, kiểm tra điều kiện z > 0. Trả hai mảng theo thứ tự giá trị rồi đạo hàm.

**F.** Các cặp [giá trị,đạo hàm] tại 0 là [0.5,0.25] cho sigmoid, [0,1] cho tanh và [0,0] cho ReLU theo quy ước. Sigmoid ở hai đầu phải hữu hạn.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(activation_and_derivative([-1,0,2], 'relu'), [[0,0,2],[0,0,1]])
```

```python
same(activation_and_derivative([2,-3], 'relu'), [[2,0],[1,0]])
```

```python
a, g = activation_and_derivative([[0,-2]], 'relu')
same(a, [[0,0]])
same(g, [[0,0]])
```

```python
rejects(activation_and_derivative, [1], 'linear')
```

<a id="dap-an-ml21"></a>

## ML21 · Đối chiếu

**B** · `[[1],[13]]`

**D1** · `[[1],[16]]`

**D2** · `[[-1],[11]]`

**D3** · `[[1],[1],[19]]`

**E1** · `[[1],[3]]`

**E2** · `[[4],[-2]]`

**E3** · `[[1],[-2]]`

**E4** · `[[0],[0],[4]]`

**R1** · `[[1],[7]]`

**R2** · `[[5],[-4]]`

**R3** · `[[1],[-1]]`

**R4** · `[[1],[1],[5]]`

**S** · `[[3],[0]]`

Hai đầu vào −1 và 2 cho giá trị tầng ẩn 0 và 4. Sau bước 3H + 1, hai hàng đầu ra lần lượt là [1] và [13].

Nếu cả hai hàng bị chặn ở 0, kiểm tra vị trí đặt ReLU. Hãy giữ cột đầu ra ngay cả khi chỉ có một nơron.

**F.** Hai mẫu cùng có h = 0,5. Logit tầng ra bằng 2×0,5−1 = 0 nên p = [0.5,0.5].

### Hàm tham khảo

```python
import numpy as np

def forward(X, W1, b1, W2, b2):
    X, W1, b1, W2, b2 = (np.asarray(v, dtype=float) for v in (X, W1, b1, W2, b2))
    if any(m.ndim != 2 for m in (X, W1, W2)):
        raise ValueError("Cần ma trận 2D")
    if X.shape[1] != W1.shape[0] or b1.shape != (W1.shape[1],) or W1.shape[1] != W2.shape[0] or b2.shape != (W2.shape[1],):
        raise ValueError("Shape không tương thích")
    return np.maximum(0, X @ W1 + b1) @ W2 + b2
```

### Ca kiểm hàm

```python
same(forward([[1,-1],[2,1]], [[1,2],[1,-1]], [0,-1], [[2],[-1]], [1]), [[-1],[5]])
```

```python
same(forward([[-3],[2]], [[1]], [1], [[2,3]], [4,5]), [[4,5],[10,14]])
```

```python
same(forward([[3]], [[1]], [-3], [[2]], [1]), [[1]])
```

```python
rejects(forward, [[1]], [[2]], 0, [[3]], [4])
```

<a id="dap-an-ml22"></a>

## ML22 · Đối chiếu

**B** · `[-0.25,0,0,0]`

**D1** · `[-0.5,0,0,0]`

**D2** · `[-0.25,-0.25,-0.25,-0.5]`

**D3** · `[0.25,0,0,0]`

**E1** · `[-0.25,0,0,0]`

**E2** · `[0.375,0,0,0]`

**E3** · `[0,0,-0.08333333333333,-0.1666666666667]`

**E4** · `[-0.08766881665439,0.02377731668101,-0.04256086437822,0.1209352671987]`

**R1** · `[0.5,0,0,0]`

**R2** · `[0.625,0,0,0]`

**R3** · `[0,0,0.08333333333333,0.1666666666667]`

**R4** · `[0.1157318234845,0.04167441320885,0.2187193240193,0.1024015102836]`

**S** · `[-0.4166666666667,-0.08333333333333,-0.08333333333333,-0.1666666666667]`

Ở lượt mẫu, cả h và p đều bằng 0,5. Hai sai số tầng ra triệt tiêu khi lấy trung bình, nhưng khi nhân sai số tầng ẩn với x, gradient w₁ vẫn bằng −0,25.

Nếu mọi gradient đều lớn gấp kích thước lô, kiểm tra phép lấy trung bình. Dùng từng giá trị x trước khi cộng gradient trọng số.

**F.** Lấy hiệu hai tổn thất chia 2×10⁻⁵. Đạo hàm số xấp xỉ −0,25, khớp thành phần đầu của gradient giải tích.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(backprop_1d([2], [1], [0,0,2,-1]), [-0.5,-0.25,-0.25,-0.5])
```

```python
same(backprop_1d([0,2], [0,1], [0,0,2,-1]), [-0.25,0,0,0])
```

```python
same(backprop_1d([2], [0], [0,0,0,0]), [0,0,0.25,0.5])
```

```python
rejects(backprop_1d, [1], [3], [0,0,1,0])
```

<a id="dap-an-ml23"></a>

## ML23 · Đối chiếu

**B** · `[[0,0,1,1],[[1],[8]],4]`

**D1** · `[[0,0,1,1],[[1],[8]],4]`

**D2** · `[[0,1,1,1],[[0],[6.666666666667]],18.66666666667]`

**D3** · `[[0,0,1,1],[[1],[8]],4]`

**E1** · `[[0,0,1,1],[[2],[9]],4]`

**E2** · `[[0,0,1,1],[[1],[5.5]],6.5]`

**E3** · `[[0,0,1,1],[[-2],[5]],4]`

**E4** · `[[0,0,1],[[0.5],[8],[30]],0.5]`

**R1** · `[[0,0,1,1],[[1.5],[7.5]],9]`

**R2** · `[[0,0,1,1],[[2],[6.5]],6.5]`

**R3** · `[[0,0,1,1],[[-2],[6]],10]`

**R4** · `[[0,0,1],[[1.5],[7],[20]],0.5]`

**S** · `[[0,0,1,1],[[-1],[4]],10]`

Nhãn là [0,0,1,1]. Hai tâm mới là 1 và 8. Mỗi điểm cách tâm mới một đơn vị nên SSE bằng 4.

Nếu điểm giữa hai tâm vào cụm sau, kiểm tra quy tắc hòa. Tính SSE bằng tâm mới và nhãn của lượt gán vừa rồi.

**F.** Lượt một cho nhãn [0,1,1,1], tâm [0,17/3], SSE = 86/3. Lượt hai giữ các nhãn đó nên tâm và SSE cũng giữ nguyên.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
labels, centers, sse = lloyd_step([[0],[2],[7],[9]], [[0],[7]])
same(labels, [0,0,1,1])
same(centers, [[1],[8]])
same(sse, 4)
```

```python
labels, centers, sse = lloyd_step([[0],[1],[2]], [[0],[2]])
same(labels, [0,0,1])
same(centers, [[0.5],[2]])
same(sse, 0.5)
```

```python
labels, centers, sse = lloyd_step([[0],[4]], [[0],[0]])
same(centers, [[2],[0]])
same(sse, 8)
```

```python
rejects(lloyd_step, [[0]], [[0,1]])
```

<a id="dap-an-ml24"></a>

## ML24 · Đối chiếu

**B** · `[0.5,0.25]`

**D1** · `[1,1]`

**D2** · `[0.3333333333333,0.2]`

**D3** · `[0.3333333333333,0]`

**E1** · `[0.3333333333333,0]`

**E2** · `[1,1]`

**E3** · `[1,1]`

**E4** · `[0.5,0.25]`

**R1** · `[0.6,0]`

**R2** · `[0.8333333333333,0.5]`

**R3** · `[0.8333333333333,0]`

**R4** · `[0.3333333333333,0.3333333333333]`

**S** · `[0.7,0.25]`

Trong sáu cặp có ba quyết định giống nhau. Chỉ một trong bốn cặp thuộc hợp là cùng cụm ở cả hai, nên kết quả là [0.5,0.25].

Nếu đổi tên nhãn làm điểm giảm, bạn đang so nhãn từng hàng. Hãy so quan hệ giữa hai hàng trong từng phân hoạch.

**F.** So trực tiếp từng nhãn cho 0 hàng bằng nhau. Cả hai chỉ số theo cặp bằng 1 vì mọi cặp đều có cùng quan hệ.

### Hàm tham khảo

```python
import numpy as np

def pair_scores(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.ndim != 1 or a.shape != b.shape or a.size < 2 or a.dtype.kind not in "iu" or b.dtype.kind not in "iu":
        raise ValueError("Cần hai phân hoạch cùng độ dài ≥ 2")
    i, j = np.triu_indices(a.size, k=1)
    left, right = a[i] == a[j], b[i] == b[j]
    union = np.count_nonzero(left | right)
    match = np.count_nonzero(left & right)
    return float((left == right).mean()), match / union if union else 1.0
```

### Ca kiểm hàm

```python
same(pair_scores([0,0,1,1], [2,2,2,3]), [0.5,0.25])
```

```python
same(pair_scores([0,1,2], [8,3,4]), [1,1])
```

```python
same(pair_scores([0,0,0], [8,8,2]), [1/3,1/3])
```

```python
rejects(pair_scores, [0], [0])
```

<a id="dap-an-ml25"></a>

## ML25 · Đối chiếu

**B** · `[[0,0],[[1],[0]],[0.8]]`

**D1** · `[[0,0],[[0],[1]],[0.8]]`

**D2** · `[[3,1],[[1],[0]],[0.8]]`

**D3** · `[[0,0],[[1,0],[0,1]],[0.8,0.2]]`

**E1** · `[[0,0],[[1],[0]],[0.9]]`

**E2** · `[[3,2],[[0.7071067811865],[0.7071067811865]],[1]]`

**E3** · `[[2,-1],[[0],[1]],[0.9]]`

**E4** · `[[1,1],[[1,0],[0,1]],[0.6923076923077,0.3076923076923]]`

**R1** · `[[0,0],[[1],[0]],[0.9411764705882]]`

**R2** · `[[1,1],[[-0.7071067811865],[0.7071067811865]],[1]]`

**R3** · `[[3,2],[[0],[1]],[0.9411764705882]]`

**R4** · `[[2,-1],[[1,0],[0,1]],[0.8,0.2]]`

**S** · `[[2,3],[[0.7071067811865],[0.7071067811865]],[1]]`

Bốn điểm có trung bình [0,0]. Tổng bình phương theo hai trục là 8 và 2, nên trục ngang giải thích 8/10 phương sai.

Khi mẫu nằm dọc đường chéo, trục đầu phải có độ dài 1. Chấp nhận đổi dấu cả cột cùng lúc. Kiểm tra tỷ lệ trên tổng mọi trị riêng.

**F.** Dữ liệu có trung bình [0,0], trục đầu nằm ngang. Điểm dựng lại là [1,0] với cả hai cách chọn dấu trục.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
mu, U, ratio = pca_fit([[-2,0],[0,1],[0,-1],[2,0]], 1)
same(mu, [0,0])
same(U @ U.T, [[1,0],[0,0]])
same(ratio, [0.8])
```

```python
mu, U, ratio = pca_fit([[1,1],[3,3]], 1)
same(mu, [2,2])
same(U @ U.T, [[0.5,0.5],[0.5,0.5]])
same(ratio, [1])
```

```python
mu, U, ratios = pca_fit([[2,2],[2,2]], 2)
same(mu, [2,2])
same(U @ U.T, np.eye(2))
same(ratios, [0,0])
```

```python
rejects(pca_fit, [[0,1]], 1)
```

<a id="dap-an-ml26"></a>

## ML26 · Đối chiếu

**B** · `[1.5,0.5]`

**D1** · `[3,0.5]`

**D2** · `[0.5,0.1666666666667]`

**D3** · `[0.5,0.375]`

**E1** · `[1.5,0.375]`

**E2** · `[1,0.1111111111111]`

**E3** · `[2,0.5]`

**E4** · `null`

**R1** · `[1.5,0.5]`

**R2** · `[2,0.1111111111111]`

**R3** · `[1,0.375]`

**R4** · `[4.5,0.4444444444444]`

**S** · `[0.5,0.1666666666667]`

Ở ngưỡng 1,5, nhánh trái chỉ có nhãn 0 và nhánh phải chỉ có nhãn 1. Gini của nút cha là 0,5 và của cả hai nhánh là 0.

Nếu hai ngưỡng cho mức giảm bằng nhau, giữ ngưỡng nhỏ. Khi không có mức giảm dương đủ lớn, kết quả là null.

**F.** Cùng chọn ngưỡng 1,5. Nút cha có hai lớp cân bằng. Mức giảm Gini là 0,5 và mức giảm entropy là 1 bit.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(best_gini_split([0,1,2,3], [0,0,1,1]), [1.5,0.5])
```

```python
same(best_gini_split([0,1,2], [0,1,0]), [0.5,1/9])
```

```python
same(best_gini_split([2,0,0,2], [1,0,0,1]), [1,0.5])
```

```python
assert best_gini_split([1,1], [0,1]) is None
```

```python
assert best_gini_split([0,1], [1,1]) is None
```

```python
rejects(best_gini_split, [0,1], [0,2])
```

<a id="dap-an-ml27"></a>

## ML27 · Đối chiếu

**B** · `[1,1,-1]`

**D1** · `[0,1,0]`

**D2** · `[1,0,-1]`

**D3** · `[0,1,-1]`

**E1** · `[1,0]`

**E2** · `[-1,0]`

**E3** · `[0,1,-1]`

**E4** · `[-1,-1,-1]`

**R1** · `[0,1]`

**R2** · `[0,-1]`

**R3** · `[0,-1,1]`

**R4** · `[-1,-1]`

**S** · `[0,1,0]`

Ở hàng 0 chỉ cây thứ hai được bỏ phiếu, và nó bỏ phiếu 1. Hàng 2 có mặt trong cả ba mẫu nên nhận −1.

Đánh dấu các cây đủ điều kiện trước khi đếm nhãn. Phân biệt không có cây OOB với có cây OOB nhưng số phiếu hòa.

**F.** Gộp mọi cây cho [1,1,0]. OOB cho [1,1,−1]. Hàng 2 có mặt trong mẫu của mọi cây nên không có cây đủ điều kiện.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
same(oob_vote([[0,0,2],[1,1,2],[0,1,2]], [[1,1,1],[1,1,0],[0,0,0]], 3), [1,1,-1])
```

```python
same(oob_vote([[0,0],[0,0]], [[1,1],[1,0]], 2), [-1,0])
```

```python
same(oob_vote([[0]], [[1]], 1), [-1])
```

```python
rejects(oob_vote, [[0,2]], [[0,1]], 2)
```

<a id="dap-an-ml28"></a>

## ML28 · Đối chiếu

**B** · `[[13,17],0.5]`

**D1** · `[[6,8],7.5]`

**D2** · `[[13,17],1.5]`

**D3** · `[[11,19],2.5]`

**E1** · `[[9,11],1]`

**E2** · `[[9,11],1]`

**E3** · `[[8,11],1]`

**E4** · `[[3,3],1.5]`

**R1** · `[[12,15],0.5]`

**R2** · `[[10,12],1.5]`

**R3** · `[[10,14],1]`

**R4** · `[[4,4],0.5]`

**S** · `[[12,16],1.5]`

Đường thẳng y = 2x + 1 cho dự đoán [13,17]. So với [13,16], hai sai số tuyệt đối là 0 và 1, nên MAE bằng 0,5.

Nếu dãy dự đoán bị kéo về giữa tập kiểm tra, hãy tìm chỗ tính lại trung bình trên dữ liệu kiểm tra. MAE dùng các nhãn kiểm tra theo đúng thứ tự.

**F.** Nhãn là [0,1,1], tỷ lệ đúng 2/3. Trung bình và độ lệch chuẩn phải lấy từ tập huấn luyện.

### Hàm tham khảo

```python
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
```

### Ca kiểm hàm

```python
p,m = regression_pipeline([[0,7],[2,7],[4,7]], [1,5,9], [[8,7],[10,7]], [18,20])
same(p, [17,21])
same(m, 1)
```

```python
p,m = regression_pipeline([[2],[2]], [1,5], [[3]], [4])
same(p, [3])
same(m, 1)
```

```python
p,m = regression_pipeline([[0],[2]], [0,2], [[4]], [12])
same(p, [4])
same(m, 8)
```

```python
rejects(regression_pipeline, [[0]], [0], [[1,2]], [0])
```

```python
rejects(regression_pipeline, [[float('nan')]], [0], [[1]], [0])
```

<a id="dap-an-mlp01"></a>

## MLP01 · Đối chiếu

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

**F.** Trung vị là 4, cột danh mục lần lượt là a, b. Hai hàng ghép là [[4,0,0],[8,1,0]].

### Hàm tham khảo

```python
import numpy as np

def encode_categories(train, values):
    train, values = np.asarray(train, dtype=str), np.asarray(values, dtype=str)
    if train.ndim != 1 or not train.size or values.ndim != 1:
        raise ValueError("Đầu vào không hợp lệ")
    levels = np.unique(train)
    return levels.tolist(), (values[:, None] == levels[None, :]).astype(int)
```

### Ca kiểm hàm

```python
levels, rows = encode_categories(['b','x','b'], ['x','a','b'])
assert levels == ['b','x']
same(rows, [[0,1],[0,0],[1,0]])
```

```python
levels, rows = encode_categories(['c','a'], ['a','z'])
assert levels == ['a','c']
same(rows, [[1,0],[0,0]])
same(encode_categories(['a'],[])[1], np.empty((0,1)))
```

```python
rejects(encode_categories, [], ['a'])
```

```python
rejects(encode_categories, [['m']], ['m'])
```

<a id="dap-an-mlp02"></a>

## MLP02 · Đối chiếu

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

**F.** Cột 0 cho đường y = 2x và MSE bằng 0. Cột 1 dự đoán [1,5] và có MSE bằng 37.

### Hàm tham khảo

```python
import numpy as np

def variance_filter(train, X, cutoff):
    train, X = np.asarray(train, dtype=float), np.asarray(X, dtype=float)
    if train.ndim != 2 or min(train.shape) == 0 or X.ndim != 2 or X.shape[1] != train.shape[1] or not np.isfinite(cutoff) or cutoff < 0 or not np.isfinite(train).all() or not np.isfinite(X).all():
        raise ValueError("Đầu vào không hợp lệ")
    keep = np.flatnonzero(train.var(axis=0) > cutoff)
    return keep, X[:, keep]
```

### Ca kiểm hàm

```python
idx, out = variance_filter([[1,0,0],[1,2,1]], [[8,4,2]], 0.25)
same(idx,[1])
same(out,[[4]])
```

```python
idx, out = variance_filter([[2,2],[2,2]], [[9,9]], 0)
same(idx,[])
same(out,np.empty((1,0)))
```

```python
same(variance_filter([[0],[2]], [[100]], 0)[1], [[100]])
```

```python
rejects(variance_filter, [[1,2]], [[2]], 0)
```

<a id="dap-an-mlp03"></a>

## MLP03 · Đối chiếu

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

**F.** Liên kết đơn cho một cụm. Liên kết đầy đủ cho hai cụm chỉ số [0,1] và [2,3], chỉ gộp cả hai ở độ cao 6.

### Hàm tham khảo

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

### Ca kiểm hàm

```python
assert linkage_history([0,2,5,6], 'single') == [(1,[2,3]),(2,[0,1]),(3,[0,1,2,3])]
```

```python
assert linkage_history([1,3,8], 'single') == [(2,[0,1]),(5,[0,1,2])]
```

```python
assert linkage_history([0,1,2], 'single')[0] == (1,[0,1])
```

```python
assert linkage_history([5], 'single') == []
```

```python
rejects(linkage_history, [0,1], 'unknown')
```

<a id="dap-an-mlp04"></a>

## MLP04 · Đối chiếu

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

**F.** Nhãn [0,0,0,−1]. Điểm [0,1] có đủ ba thành viên trong lân cận, hai điểm còn lại của cụm là điểm biên.

### Hàm tham khảo

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

### Ca kiểm hàm

```python
same(dbscan_1d([0,0.5,1,4,4.5,5,8], 0.5, 3), [0,0,0,1,1,1,-1])
```

```python
same(dbscan_1d([0,0.5,1,1.5,2], 0.5, 3), [0,0,0,0,0])
```

```python
same(dbscan_1d([0,3,3], 0, 2), [-1,0,0])
```

```python
same(dbscan_1d([], 1, 1), [])
```

```python
rejects(dbscan_1d, [1], -1, 2)
```

<a id="dap-an-mlp05"></a>

## MLP05 · Đối chiếu

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

**F.** Nhân đa thức phân đúng 4/4 ở dữ liệu này. Một đường thẳng không thể phân đúng cả bốn nhãn xen kẽ.

### Hàm tham khảo

```python
import numpy as np

def svm_objective(X, y, w, b, C):
    X, y, w = (np.asarray(v, dtype=float) for v in (X, y, w))
    if X.ndim != 2 or min(X.shape) == 0 or y.shape != (len(X),) or w.shape != (X.shape[1],) or not np.isin(y, [-1,1]).all() or not np.isfinite(C) or C <= 0:
        raise ValueError("Đầu vào không hợp lệ")
    hinge = np.maximum(0, 1 - y * (X @ w + b))
    return hinge, float(0.5 * (w @ w) + C * hinge.sum())
```

### Ca kiểm hàm

```python
h,obj = svm_objective([[-1],[1]], [-1,1], [1], 0, 3)
same(h,[0,0])
same(obj,0.5)
```

```python
h,obj = svm_objective([[0],[2]], [-1,1], [0], 1, 2)
same(h,[2,0])
same(obj,4)
```

```python
h,obj = svm_objective([[-0.25],[1]], [-1,1], [1], 0, 1)
same(h,[0.75,0])
same(obj,1.25)
```

```python
rejects(svm_objective, [[0]], [0], [1], 0, 1)
```

<a id="dap-an-mlp06"></a>

## MLP06 · Đối chiếu

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

**F.** Một thành phần giữ 16/21, hai thành phần giữ 20/21. Chọn k = 2.

### Hàm tham khảo

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

### Ca kiểm hàm

```python
R,sse = svd_reconstruct([[-2,0],[2,0],[0,1],[0,-1]], 1)
same(R,[[-2,0],[2,0],[0,0],[0,0]])
same(sse,2)
```

```python
R,sse = svd_reconstruct([[1,3],[3,7]], 0)
same(R,[[2,5],[2,5]])
same(sse,10)
```

```python
same(svd_reconstruct([[2,5,7]], 1)[0], [[2,5,7]])
```

```python
rejects(svd_reconstruct, [[1,2]], 2)
```

<a id="dap-an-mlp07"></a>

## MLP07 · Đối chiếu

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

**F.** Theo thứ tự ban đầu, trọng số cuối là [[0.5],[2.5],[7.5]]. Khi đảo thứ tự, kết quả là [[0.5],[5.5],[7.5]].

### Hàm tham khảo

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

### Ca kiểm hàm

```python
i,W = som_step([[0],[4],[8],[12]],[5],0.5,1)
assert i == 1
same(W,[[2.5],[4.5],[6.5],[12]])
```

```python
i,W = som_step([[0,0],[2,0],[4,0]],[1,0],1,0)
assert i == 0
same(W,[[1,0],[2,0],[4,0]])
```

```python
same(som_step([[0],[4]], [1], 0, 2)[1], [[0],[4]])
```

```python
rejects(som_step, [[0]], [0], 1.1, 0)
```

<a id="dap-an-mlp08"></a>

## MLP08 · Đối chiếu

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

**F.** NMI(a,b) bằng 1 vì phân hoạch chỉ đổi tên. NMI(a,c) bằng 0 vì bảng chéo có bốn ô cùng tần số.

### Hàm tham khảo

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

### Ca kiểm hàm

```python
same(davies_bouldin_1d([0,2,8,10],[9,9,2,2]), 0.25)
```

```python
same(davies_bouldin_1d([0,2,8,10,20,22],[0,0,1,1,2,2]), 2/9)
```

```python
same(davies_bouldin_1d([0,0,5],[1,1,2]), 0)
```

```python
rejects(davies_bouldin_1d, [0,1,2], [0,1,0])
```

```python
rejects(davies_bouldin_1d, [0,1], [0,1])
```

<a id="loi-giai-ngan-hang"></a>

# Đáp án ngân hàng

## Ôn tập ML01 · Lời giải

### ML01-mcq-1 · Đối chiếu

**Chọn B.** Hàng là mẫu, cột là thuộc tính.

- A · Đảo số mẫu và số thuộc tính.
- B · Ba hàng, hai cột.
- C · Đó là dạng flatten, không phải kích thước ma trận ban đầu.

### ML01-mcq-2 · Đối chiếu

**Chọn B.** Dấu : ở chiều hàng giữ toàn bộ mẫu.

- A · Chỉ lấy mẫu thứ hai.
- B · Lấy tất cả hàng ở cột 1.
- C · Chỉ lấy một giá trị.

### ML01-mcq-3 · Đối chiếu

**Chọn B.** Cột toàn 1 đứng cạnh d cột đặc trưng. Bảng vẫn có n hàng và nay có d + 1 cột.

- A · Thêm hàng, không phải cột.
- B · Mỗi mẫu có thêm một giá trị hệ số tự do.
- C · Đảo trục không liên quan.

### ML01-mcq-4 · Đối chiếu

**Chọn A.** Số chiều vectơ mẫu bằng số thuộc tính d.

- A · Mỗi thuộc tính là một tọa độ: có bốn tọa độ.
- B · N đếm mẫu, không xác định số chiều của từng mẫu.
- C · Một mẫu vẫn có thể có nhiều thuộc tính.

### ML01-mcq-5 · Đối chiếu

**Chọn B.** X[i] lấy vectơ thuộc tính của mẫu i.

- A · Chỉ số đầu tiên chọn hàng. X chỉ có hai cột.
- B · Chỉ số bắt đầu từ 0, nên hàng 2 là mẫu thứ ba.
- C · Chọn một hàng không lấy hai mẫu.

### ML01-mcq-6 · Đối chiếu

**Chọn C.** Giữ một chiều bằng lát cắt khác với chọn một chỉ số.

- A · Chỉ số cột đơn làm kết quả thành vectơ kích thước (6,).
- B · Đây là hàng đầu, kích thước (2,).
- C · Lát cắt cột giữ trục thứ hai, kích thước (6,1).

### ML01-mcq-7 · Đối chiếu

**Chọn A.** Phải kiểm cả kích thước lẫn ý nghĩa từng trục.

- A · Chuyển vị đổi hai trục thành (6,2).
- B · Flatten tạo vectơ 1D, mất cách tổ chức mẫu và thuộc tính.
- C · Cùng số phần tử không có nghĩa cùng semantics.

### ML01-mcq-8 · Đối chiếu

**Chọn B.** Thứ tự và ý nghĩa đặc trưng là một phần của hợp đồng dữ liệu.

- A · Đổi cột không tạo thêm hàng.
- B · Giá trị x₁ bị gắn với tên x₂ và ngược lại.
- C · Kích thước chỉ mô tả kích thước, không xác nhận tên cột.

### ML01-mcq-9 · Đối chiếu

**Chọn C.** Các khối ghép ngang phải cùng số hàng và số chiều.

- A · Vectơ 1D không cùng số chiều với X trong hstack này.
- B · Đây là một hàng có sáu cột.
- C · Một giá trị hệ số tự do cho mỗi hàng: sáu hàng, một cột.

### ML01-mcq-10 · Đối chiếu

**Chọn A.** Dữ liệu rỗng vẫn có thể giữ schema hai cột, khác mảng rỗng 1D.

- A · Dữ liệu rỗng vẫn có thể giữ schema hai cột, khác mảng rỗng 1D.
- B · Nhầm cột với hàng.
- C · Kích thước vẫn có hai trục.

### ML01-practice-1 · Đối chiếu

Kích thước là (8,3). Trục đầu có tám hàng, mỗi hàng là một mẫu. Trục còn lại có ba cột cho ba đặc trưng.

### ML01-practice-2 · Đối chiếu

Chỉ số đầu tiên là 0 nên X[1] lấy hàng thứ hai, [55,3].

```python
import numpy as np
X = np.array([[40,2],[55,3],[70,4]])
print(X[1].tolist())
```
Kết quả [55, 3]

### ML01-practice-3 · Đối chiếu

X[:,0] trả vectơ [40,55,70], kích thước (3,).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
a=X[:,0]
print(a.tolist())
print(a.shape)
```
Kết quả [40, 55, 70]
(3,)

### ML01-practice-4 · Đối chiếu

Chọn chỉ số cột tạo (3,). Lát cắt cột giữ ma trận (3,1).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
print(X[:,0].shape)
print(X[:,0:1].shape)
```
Kết quả (3,)
(3, 1)

### ML01-practice-5 · Đối chiếu

Cột hệ số tự do có một số 1 cho mỗi mẫu. Ma trận mới có kích thước (2,3).

```python
import numpy as np
X=np.array([[40,2],[55,3]])
B=np.column_stack([np.ones(len(X),dtype=int),X])
print(B.tolist())
print(B.shape)
```
Kết quả [[1, 40, 2], [1, 55, 3]]
(2, 3)

### ML01-practice-6 · Đối chiếu

Khoảng cách sqrt((30−25)²+(6−3)²)=sqrt(34)≈5.8310.

```python
import numpy as np
a=np.array([30.,6.]); b=np.array([25.,3.])
print(f"{np.sqrt(np.sum((a-b)**2)):.4f}")
```
Kết quả 5.8310

### ML01-practice-7 · Đối chiếu

Tọa độ đầu góp 25 trong tổng 34, tức khoảng 73.53%. Đặc trưng có thang đo lớn có thể chi phối khoảng cách. Chuẩn hóa được học ở ML03.

### ML01-practice-8 · Đối chiếu

Mảng đầu là vectơ kích thước (2,). Mảng sau là ma trận dữ liệu có một hàng, kích thước (1,2).

```python
import numpy as np
print(np.array([40,2]).shape)
print(np.array([[40,2]]).shape)
```
Kết quả (2,)
(1, 2)

### ML01-practice-9 · Đối chiếu

Kích thước mới (3,4), vẫn 12 phần tử. Chuyển vị đổi cách bố trí trục, không thu thập thêm mẫu quan sát.

```python
import numpy as np
X=np.arange(12).reshape(4,3)
print(X.T.shape)
print(X.T.size)
```
Kết quả (3, 4)
12

### ML01-practice-10 · Đối chiếu

Không. Một ma trận có cột x₁, x₂. Ma trận kia có cột x₂, x₁. Kích thước giống nhau nhưng thứ tự và ý nghĩa đặc trưng khác nhau.

### ML01-practice-11 · Đối chiếu

X[1:,:] giữ hàng 1 và 2, kích thước (2,2).

```python
import numpy as np
X=np.array([[40,2],[55,3],[70,4]])
Y=X[1:,:]
print(Y.tolist())
print(Y.shape)
```
Kết quả [[55, 3], [70, 4]]
(2, 2)

### ML01-practice-12 · Đối chiếu

Đã tăng số hàng như thêm một mẫu. Hệ số tự do là thêm một thuộc tính cho từng mẫu nên kích thước đúng là (5,3), cột hệ số tự do gồm năm số 1.

## Ôn tập ML02 · Lời giải

### ML02-mcq-1 · Đối chiếu

**Chọn B.** Hiệp phương sai của một biến với chính nó là phương sai.

- A · Trung bình không phải hiệp phương sai.
- B · Đúng.
- C · N không phải đại lượng trong đường chéo.

### ML02-mcq-2 · Đối chiếu

**Chọn B.** Sau khi ước lượng trung bình, chỉ còn n − 1 độ lệch độc lập. Mẫu số này cho ước lượng không chệch khi các quan sát độc lập, cùng phân phối và có phương sai hữu hạn.

- A · Mẫu số không đổi đơn vị.
- B · Các độ lệch trong mỗi cột có tổng bằng 0.
- C · Đó là tính chất tương quan, không phải hiệp phương sai.

### ML02-mcq-3 · Đối chiếu

**Chọn A.** C = XcᵀXc/(n-1) nên đối xứng và PSD.

- A · Đúng về mặt toán học.
- B · Hiệp phương sai có thể âm.
- C · Không có tính chất này.

### ML02-mcq-4 · Đối chiếu

**Chọn B.** Mỗi cặp trong ba thuộc tính cho một phần tử, nên C là 3×3.

- A · Đó là kích thước theo mẫu, không theo thuộc tính.
- B · Mỗi cặp trong ba thuộc tính cho một phần tử, nên C là 3×3.
- C · Đây là kích thước dữ liệu ban đầu.

### ML02-mcq-5 · Đối chiếu

**Chọn C.** Trung bình bằng 2, tổng bình phương sai lệch=2. Chia n−1=1 được 2.

- A · Đây là kết quả chia cho n thay vì n−1.
- B · 4 là khoảng cách giữa hai giá trị khi bình phương, không phải tổng quanh trung bình.
- C · Trung bình bằng 2, tổng bình phương sai lệch=2. Chia n−1=1 được 2.

### ML02-mcq-6 · Đối chiếu

**Chọn A.** Sai lệch hai biến ngược dấu, tổng tích âm.

- A · Sai lệch hai biến ngược dấu, tổng tích âm.
- B · Hai cột biến thiên ngược chiều.
- C · Trung bình bằng nhau không quyết định hiệp phương sai.

### ML02-mcq-7 · Đối chiếu

**Chọn B.** Tâm hóa loại bỏ hằng số cộng, nên hiệp phương sai không đổi.

- A · Độ lệch so với trung bình không tăng 100 vì trung bình cũng tăng 100.
- B · Tâm hóa loại bỏ hằng số cộng, nên hiệp phương sai không đổi.
- C · Dịch chuyển không làm mất biến thiên.

### ML02-mcq-8 · Đối chiếu

**Chọn C.** Mọi sai lệch của cột hằng bằng 0.

- A · Giá trị trung bình không phải phương sai.
- B · Công thức hiệp phương sai vẫn xác định nếu n≥2.
- C · Mọi sai lệch của cột hằng bằng 0.

### ML02-mcq-9 · Đối chiếu

**Chọn A.** Tổng (xᵢ−trung bình)=0. Số thực máy có thể có sai số nhỏ.

- A · Tổng (xᵢ−trung bình)=0. Số thực máy có thể có sai số nhỏ.
- B · Tâm hóa không tạo cột toàn 1.
- C · Trung bình ban đầu đã bị trừ đi.

### ML02-mcq-10 · Đối chiếu

**Chọn A.** Theo công thức mẫu đang học, dùng n−1.

- A · Theo công thức mẫu đang học, dùng n−1.
- B · Đó là mẫu số n của quy ước khác.
- C · Mẫu số dựa số mẫu.

### ML02-practice-1 · Đối chiếu

Hai trung bình lần lượt là 2 và 6.

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
print(X.mean(axis=0).tolist())
```
Kết quả [2.0, 6.0]

### ML02-practice-2 · Đối chiếu

Trừ vectơ trung bình [2,6] ở mỗi hàng, được [[−1,−2],[1,2]].

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
print((X-X.mean(axis=0)).tolist())
```
Kết quả [[-1.0, -2.0], [1.0, 2.0]]

### ML02-practice-3 · Đối chiếu

Trung bình bằng 2. Tổng bình phương sai lệch=2. Chia 1 được 2.

```python
import numpy as np
x=np.array([1.,3.])
print(float(np.var(x,ddof=1)))
```
Kết quả 2.0

### ML02-practice-4 · Đối chiếu

Sai lệch x=[−1,1], y=[−2,2]. Tổng tích=4. Chia 1 được 4.

```python
import numpy as np
x=np.array([1.,3.]);y=np.array([4.,8.])
print(float(np.sum((x-x.mean())*(y-y.mean()))/(len(x)-1)))
```
Kết quả 4.0

### ML02-practice-5 · Đối chiếu

Hai phương sai là 2 và 8. Hiệp phương sai là 4, nên C=[[2,4],[4,8]].

```python
import numpy as np
X=np.array([[1.,4.],[3.,8.]])
Z=X-X.mean(axis=0)
print((Z.T@Z/(len(X)-1)).tolist())
```
Kết quả [[2.0, 4.0], [4.0, 8.0]]

### ML02-practice-6 · Đối chiếu

Trung bình hai cột đều 2. Tổng tích sai lệch=−2, chia 2 được −1.

```python
import numpy as np
print(float(np.cov([1.,2.,3.],[3.,2.,1.],ddof=1)[0,1]))
```
Kết quả -1.0

### ML02-practice-7 · Đối chiếu

Mỗi tích (xᵢj−mean_j)(xᵢk−mean_k) không đổi khi đổi j, k, nên C_jk=C_kj.

### ML02-practice-8 · Đối chiếu

Không theo công thức đang dùng: n−1=0. Cần ít nhất hai mẫu. Phải báo giới hạn thay vì coi kết quả là 0.

### ML02-practice-9 · Đối chiếu

Trung bình bằng 7, mọi sai lệch bằng 0 nên phương sai bằng 0.

```python
import numpy as np
print(float(np.var([7.,7.,7.],ddof=1)))
```
Kết quả 0.0

### ML02-practice-10 · Đối chiếu

Khi thay x bằng x + c, trung bình cũng tăng c. Mỗi độ lệch (xᵢ + c) − (x̄ + c) bằng xᵢ − x̄, nên tổng tích độ lệch và hiệp phương sai giữ nguyên.

### ML02-practice-11 · Đối chiếu

Sai lệch cột được nhân 2. Phương sai nhân 4. Hiệp phương sai với cột còn lại nhân 2.

### ML02-practice-12 · Đối chiếu

Không. PSD nói vᵀCv≥0 với mọi v, không đòi mọi phần tử C không âm. Với v=[1,1], vᵀCv=2.

```python
import numpy as np
C=np.array([[2.,-1.],[-1.,2.]])
v=np.array([1.,1.])
print(float(v@C@v))
```
Kết quả 2.0

## Ôn tập ML03 · Lời giải

### ML03-mcq-1 · Đối chiếu

**Chọn B.** Tập kiểm tra phải được giữ chưa thấy khi học tham số.

- A · Làm rò thông tin tập kiểm tra.
- B · Đúng. Sau đó áp dụng cho dữ liệu khác.
- C · Không thể đánh giá khách quan.

### ML03-mcq-2 · Đối chiếu

**Chọn A.** Z-điểm đo số độ lệch chuẩn so với trung bình tập huấn luyện.

- A · (70-50)/10.
- B · Đảo tử số và mẫu số.
- C · Chưa chuẩn hóa.

### ML03-mcq-3 · Đối chiếu

**Chọn A.** Không kẹp tập kiểm tra tùy tiện vì sẽ làm mất thông tin.

- A · Đúng và đó là tín hiệu cần giữ nguyên.
- B · Sai nếu dữ liệu mới vượt miền tập huấn luyện.
- C · Không liên quan.

### ML03-mcq-4 · Đối chiếu

**Chọn A.** (5−10)/(20−10)=−0.5.

- A · (5−10)/(20−10)=−0.5.
- B · Không tự kẹp giá trị tập kiểm tra về 0.
- C · Sai dấu vì tập kiểm tra nằm dưới min tập huấn luyện.

### ML03-mcq-5 · Đối chiếu

**Chọn B.** Tại trung bình, tử số bằng 0.

- A · 1 ứng với một độ lệch chuẩn phía trên trung bình.
- B · Tại trung bình, tử số bằng 0.
- C · Chưa thực hiện phép biến đổi.

### ML03-mcq-6 · Đối chiếu

**Chọn C.** Công thức trực tiếp chia cho 0. Bài này quy định báo lỗi.

- A · Số mẫu không gây vấn đề này.
- B · Cột hằng có thể âm hoặc dương.
- C · Công thức trực tiếp chia cho 0. Bài này quy định báo lỗi.

### ML03-mcq-7 · Đối chiếu

**Chọn A.** Mỗi đặc trưng có thang đo và thống kê riêng.

- A · Mỗi đặc trưng có thang đo và thống kê riêng.
- B · Đây là thao tác theo mẫu, khác mục tiêu chuẩn hóa từng đặc trưng.
- C · Dùng chung một khoảng có thể giữ sự chênh thang đo giữa các cột.

### ML03-mcq-8 · Đối chiếu

**Chọn B.** Đây là hai phép biến đổi khác nhau. Phải ghi rõ quy ước đang dùng.

- A · Ví dụ tập huấn luyện [10,20] cho các kết quả khác nhau.
- B · Đây là hai phép biến đổi khác nhau. Phải ghi rõ quy ước đang dùng.
- C · Thay đại lượng trong công thức làm đổi phép biến đổi.

### ML03-mcq-9 · Đối chiếu

**Chọn C.** Dùng cùng tham số để giữ hợp đồng biến đổi giữa tập huấn luyện và dữ liệu mới.

- A · Tính lại làm thay hệ tọa độ so với lúc học.
- B · Dùng tập kiểm tra để học thống kê gây rò rỉ dữ liệu trong đánh giá.
- C · Dùng cùng tham số để giữ hợp đồng biến đổi giữa tập huấn luyện và dữ liệu mới.

### ML03-mcq-10 · Đối chiếu

**Chọn A.** Cần dùng tập huấn luyện min=10, max=20 để được 2.

- A · Cần dùng tập huấn luyện min=10, max=20 để được 2.
- B · 2 dùng thống kê tập huấn luyện, chứ không từ tập kiểm tra một phần tử.
- C · khớp mô hình trên tập kiểm tra không đúng quy trình.

### ML03-practice-1 · Đối chiếu

Min=10, max=20. Kết quả [0.5,2.0].

```python
import numpy as np
train=np.array([10.,20.]);test=np.array([15.,30.])
print(((test-train.min())/(train.max()-train.min())).tolist())
```
Kết quả [0.5, 2.0]

### ML03-practice-2 · Đối chiếu

Khoảng bằng 20. Kết quả [−0.5,0.5,1.5].

```python
import numpy as np
train=np.array([-10.,10.]);test=np.array([-20.,0.,20.])
print(((test-train.min())/(train.max()-train.min())).tolist())
```
Kết quả [-0.5, 0.5, 1.5]

### ML03-practice-3 · Đối chiếu

Các kết quả là [−1,0,2].

```python
import numpy as np
print(((np.array([40.,50.,70.])-50)/10).tolist())
```
Kết quả [-1.0, 0.0, 2.0]

### ML03-practice-4 · Đối chiếu

Min=[0,10], max=[10,30]. Mẫu mới biến đổi thành [[0.5,0.5]].

```python
import numpy as np
T=np.array([[0.,10.],[10.,30.]])
X=np.array([[5.,20.]])
print(((X-T.min(axis=0))/(T.max(axis=0)-T.min(axis=0))).tolist())
```
Kết quả [[0.5, 0.5]]

### ML03-practice-5 · Đối chiếu

Thống kê lấy từ tập huấn luyện nên tập kiểm tra có thể nằm ngoài khoảng đã thấy. Giá trị lớn hơn 1 đúng theo công thức. Không tự kẹp trừ khi có quy ước riêng.

### ML03-practice-6 · Đối chiếu

Thông tin từ tập kiểm tra đã tham gia thống kê chuẩn hóa. Cần chia trước, học thống kê trên tập huấn luyện, rồi dùng nguyên thống kê đó cho các phần còn lại.

### ML03-practice-7 · Đối chiếu

Trung bình bằng 15, max=20. Kết quả [−0.25,0.25]. Đây không phải Min–Max.

```python
import numpy as np
x=np.array([10.,20.])
print(((x-x.mean())/x.max()).tolist())
```
Kết quả [-0.25, 0.25]

### ML03-practice-8 · Đối chiếu

Min–Max cho [0,1]. Quy ước (x−trung bình)/max cho [−0.25,0.25]. Không thay công thức này bằng công thức kia mà không đổi mô tả.

### ML03-practice-9 · Đối chiếu

max=min=4, mẫu số 0. Theo hợp đồng bài tập cần ValueError. Thực tế có thể chọn quy tắc xử lý đặc trưng hằng khác nhưng phải ghi rõ.

### ML03-practice-10 · Đối chiếu

Chia cho 0. Cần quy định cách xử lý cột hằng. Không âm thầm xem NaN hay Inf là dữ liệu chuẩn hóa hợp lệ.

### ML03-practice-11 · Đối chiếu

Không. Dữ liệu mới phải có cùng số cột, ý nghĩa và thứ tự đặc trưng để dùng thống kê tập huấn luyện. Kích thước không khớp là lỗi hợp đồng cần xử lý.

### ML03-practice-12 · Đối chiếu

Dùng cùng min=0, max=4, hai kết quả là [0.5] và [1.5]. Không khớp mô hình lại từng lô tập kiểm tra.

```python
import numpy as np
lo,hi=0.,4.
for test in [[2.],[6.]]:
    print(((np.array(test)-lo)/(hi-lo)).tolist())
```
Kết quả [0.5]
[1.5]

## Ôn tập ML04 · Lời giải

### ML04-mcq-1 · Đối chiếu

**Chọn A.** Hai phần dư đều bằng 0.

- A · Đúng vì dự đoán khớp cả hai điểm.
- B · Không phải tổng phần dư bình phương.
- C · Đó là một giá trị y.

### ML04-mcq-2 · Đối chiếu

**Chọn B.** Đạo hàm của bình phương sinh hệ số 2.

- A · Không.
- B · Đúng.
- C · E vẫn không âm.

### ML04-mcq-3 · Đối chiếu

**Chọn A.** Tham số không nhất thiết duy nhất.

- A · Đúng.
- B · MSE không âm.
- C · Có thể cùng dự đoán.

### ML04-mcq-4 · Đối chiếu

**Chọn A.** 1.6−2=−0.4.

- A · 1.6−2=−0.4.
- B · Đây là y−y_hat, ngược quy ước.
- C · Đây là dự đoán, chưa trừ y.

### ML04-mcq-5 · Đối chiếu

**Chọn B.** 4/(2×1)=2.

- A · Bình phương phần dư không âm.
- B · 4/(2×1)=2.
- C · 4 là bình phương phần dư, chưa chia 2m.

### ML04-mcq-6 · Đối chiếu

**Chọn C.** Mọi số hạng bằng 0. Không suy ra dự đoán tốt trên dữ liệu mới.

- A · Tổng bình phương không âm.
- B · Với m>0 công thức xác định.
- C · Mọi số hạng bằng 0. Không suy ra dự đoán tốt trên dữ liệu mới.

### ML04-mcq-7 · Đối chiếu

**Chọn A.** Bình phương loại bỏ dấu của từng residual.

- A · Bình phương loại bỏ dấu của từng residual.
- B · Hàm mất mát không có dấu residual.
- C · Không có hệ số 2 mới nào xuất hiện.

### ML04-mcq-8 · Đối chiếu

**Chọn B.** E=MSE/2. Hệ số dương không đổi vị trí cực tiểu.

- A · Hệ số mẫu số lớn gấp đôi làm giá trị nhỏ đi.
- B · E=MSE/2. Hệ số dương không đổi vị trí cực tiểu.
- C · Chỉ bằng nhau khi cả hai bằng 0.

### ML04-mcq-9 · Đối chiếu

**Chọn C.** Chưa có bằng chứng về dữ liệu chưa dùng để học.

- A · Tổng bình phương bằng 0 buộc mọi phần dư bằng 0.
- B · MSE=2E nên cũng bằng 0.
- C · Chưa có bằng chứng về dữ liệu chưa dùng để học.

### ML04-mcq-10 · Đối chiếu

**Chọn A.** Phân biệt trung bình phần dư với trung bình squared residual.

- A · Phân biệt trung bình phần dư với trung bình squared residual.
- B · Bình phương trước khi cộng nên không triệt tiêu.
- C · Bình phương số âm hoàn toàn xác định.

### ML04-practice-1 · Đối chiếu

Dự đoán 1.6. Phần dư y_hat−y=−0.4.

```python
x,y,a,b=20.,2.,.08,0.
print(round(a*x+b,4))
print(round(a*x+b-y,4))
```
Kết quả 1.6
-0.4

### ML04-practice-2 · Đối chiếu

Tổng bình phương=2, m=2 nên E=0.5.

```python
import numpy as np
e=np.array([1.,-1.])
print(float(np.sum(e**2)/(2*len(e))))
```
Kết quả 0.5

### ML04-practice-3 · Đối chiếu

Dự đoán bằng 0. E=(2.56+10.24)/4=3.2.

```python
import numpy as np
y=np.array([1.6,3.2])
print(round(float(np.sum(y**2)/(2*len(y))),4))
```
Kết quả 3.2

### ML04-practice-4 · Đối chiếu

Hai dự đoán khớp nhãn. E=0.

```python
import numpy as np
x=np.array([20.,40.]);y=np.array([1.6,3.2])
print(float(np.mean((.08*x-y)**2)/2))
```
Kết quả 0.0

### ML04-practice-5 · Đối chiếu

Dự đoán 2.5 nên residual=0, E=0.

```python
x,y,a,b=1.5,2.5,1.,1.
print((a*x+b-y)**2/2)
```
Kết quả 0.0

### ML04-practice-6 · Đối chiếu

E và −e có cùng bình phương. Khi đạo hàm phải tính cả đạo hàm của phần dư theo tham số. Đổi dấu phần dư mà giữ công thức gradient cũ có thể làm cập nhật sai chiều.

### ML04-practice-7 · Đối chiếu

E lần lượt 1 và 0.5. Cùng tổng phần dư là 2 không có nghĩa cùng tổng bình phương.

```python
import numpy as np
for e in [[0.,2.],[1.,1.]]:
    print(float(np.mean(np.array(e)**2)/2))
```
Kết quả 1.0
0.5

### ML04-practice-8 · Đối chiếu

Không. Tổng bình phương và số mẫu cùng nhân 2 nên tỷ số không đổi.

### ML04-practice-9 · Đối chiếu

E=12/6=2. MSE=12/3=4.

```python
m,sse=3,12.
print(sse/(2*m))
print(sse/m)
```
Kết quả 2.0
4.0

### ML04-practice-10 · Đối chiếu

m=0 làm mẫu số bằng 0. Không coi NaN hay giá trị tự gán là một tổn thất hợp lệ.

### ML04-practice-11 · Đối chiếu

Mỗi x cần đúng nhãn y tương ứng. Broadcasting có thể chạy nhưng sẽ so cả hai dự đoán với cùng nhãn ngoài ý định, che lỗi dữ liệu.

### ML04-practice-12 · Đối chiếu

Không. Tính duy nhất cần ma trận thiết kế [x,1] đủ hạng cột. Nếu mọi x bằng nhau thì nhiều cặp a, b có thể tạo cùng dự đoán.

## Ôn tập ML05 · Lời giải

### ML05-mcq-1 · Đối chiếu

**Chọn B.** Tất cả mẫu huấn luyện đều đóng góp vào gradient của bước này.

- A · Đó là SGD.
- B · Đúng.
- C · Không thể tính gradient.

### ML05-mcq-2 · Đối chiếu

**Chọn A.** Bước nhảy vượt qua vùng giảm.

- A · Đúng.
- B · Không.
- C · Alpha không đổi nhãn.

### ML05-mcq-3 · Đối chiếu

**Chọn A.** Vectơ update dùng cùng gradient.

- A · Đúng.
- B · Sai thứ tự.
- C · Không.

### ML05-mcq-4 · Đối chiếu

**Chọn A.** ((-1.6)×20+(-3.2)×40)/2=−80.

- A · ((-1.6)×20+(-3.2)×40)/2=−80.
- B · −2.4 là gradient theo b.
- C · Sai dấu vì phần dư ban đầu âm.

### ML05-mcq-5 · Đối chiếu

**Chọn B.** d_b=−2.4 nên b_new=0−0.001×(−2.4).

- A · Cập nhật phải trừ gradient âm.
- B · d_b=−2.4 nên b_new=0−0.001×(−2.4).
- C · 0.08 là a mới, không phải b.

### ML05-mcq-6 · Đối chiếu

**Chọn C.** Hai thành phần gradient thuộc cùng một điểm tham số.

- A · Đó là cập nhật nối tiếp, khác một bước lô GD đã định nghĩa.
- B · Hệ số tự do vẫn phải được cập nhật khi bài có hệ số tự do.
- C · Hai thành phần gradient thuộc cùng một điểm tham số.

### ML05-mcq-7 · Đối chiếu

**Chọn A.** theta_new=theta−alpha×0=theta.

- A · theta_new=theta−alpha×0=theta.
- B · Tổn thất bình phương không âm.
- C · GD không tự thêm cập nhật ngẫu nhiên trong công thức này.

### ML05-mcq-8 · Đối chiếu

**Chọn B.** Bước nhảy lớn có thể làm tổn thất tăng. Cần theo dõi diễn biến.

- A · Không có bảo đảm này.
- B · Bước nhảy lớn có thể làm tổn thất tăng. Cần theo dõi diễn biến.
- C · Đây là hai phương pháp khác nhau.

### ML05-mcq-9 · Đối chiếu

**Chọn C.** Gradient lô tổng hợp mọi mẫu rồi chia m.

- A · Đó gần với SGD chứ không phải lô đầy đủ.
- B · Công thức không loại các mẫu phần dư nhỏ.
- C · Gradient lô tổng hợp mọi mẫu rồi chia m.

### ML05-mcq-10 · Đối chiếu

**Chọn A.** Gradient hai thành phần phải từ cùng tham số cũ.

- A · Gradient hai thành phần phải từ cùng tham số cũ.
- B · Thứ tự dùng tham số thay đổi điểm tính gradient.
- C · Nhỏ không biến hai thuật toán thành giống hệt.

### ML05-practice-1 · Đối chiếu

d_a=−80, d_b=−2.4.

```python
import numpy as np
x=np.array([20.,40.]);y=np.array([1.6,3.2]);e=-y
print(round(float(np.mean(e*x)),4))
print(round(float(e.mean()),4))
```
Kết quả -80.0
-2.4

### ML05-practice-2 · Đối chiếu

a_new=0.08, b_new=0.0024.

```python
a,b,da,db,alpha=0.,0.,-80.,-2.4,.001
print(a-alpha*da)
print(b-alpha*db)
```
Kết quả 0.08
0.0024

### ML05-practice-3 · Đối chiếu

Không. Có hệ số tự do mới 0.0024 nên dự đoán [1.6024,3.2024]. A=0.08 riêng lẻ không chứng minh cả mô hình khớp.

```python
import numpy as np
x=np.array([20.,40.])
print(np.round(.08*x+.0024,4).tolist())
```
Kết quả [1.6024, 3.2024]

### ML05-practice-4 · Đối chiếu

d_a=−4, d_b=−2.5 nên a_new=0.4, b_new=0.25.

```python
import numpy as np
x=np.array([1.,2.]);y=np.array([2.,3.]);e=-y
print(round(float(-.1*np.mean(e*x)),4))
print(round(float(-.1*e.mean()),4))
```
Kết quả 0.4
0.25

### ML05-practice-5 · Đối chiếu

Dùng a mới cho phần dư [−1.6,−2.2], mean=−1.9 nên b_new=0.19, khác đáp án đồng thời 0.25.

```python
import numpy as np
x=np.array([1.,2.]);y=np.array([2.,3.])
print(round(float(-.1*np.mean(.4*x-y)),4))
```
Kết quả 0.19

### ML05-practice-6 · Đối chiếu

Residual=0 nên cả hai gradient bằng 0, tham số vẫn là a=2, b=0.

### ML05-practice-7 · Đối chiếu

Dự đoán=3, residual=−2, d_a=−4, d_b=−2. A_new=1.4, b_new=1.2.

```python
x,y,a,b,alpha=2.,5.,1.,1.,.1
e=a*x+b-y
print(a-alpha*e*x)
print(b-alpha*e)
```
Kết quả 1.4
1.2

### ML05-practice-8 · Đối chiếu

Trung bình chia cho m. Nếu lặp đôi toàn bộ dữ liệu, sum tăng gấp đôi nhưng trung bình không đổi. Gradient của hàm E dùng mẫu số m.

### ML05-practice-9 · Đối chiếu

Bước lần lượt [0.4,0.25] và [0.04,0.025]. Giảm alpha mười lần làm bước nhỏ mười lần tại cùng gradient.

### ML05-practice-10 · Đối chiếu

Không. Cần theo dõi qua các bước và điều kiện dừng cụ thể. Một lần giảm không chứng minh đã tới cực tiểu.

### ML05-practice-11 · Đối chiếu

Làm tròn thay đổi trạng thái thuật toán và có thể làm bước nhỏ biến mất. Giữ độ chính xác tính toán, chỉ định dạng khi hiển thị.

### ML05-practice-12 · Đối chiếu

Gradient=[−2.5,−4] nên theta_new=[0.25,0.4]. Cột đầu là hệ số tự do, cột sau là đặc trưng. Không đổi chỗ hai hệ số.

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]])
theta=np.zeros(2);y=np.array([2.,3.])
print(np.round(theta-.1*(X.T@(X@theta-y)/len(y)),4).tolist())
```
Kết quả [0.25, 0.4]

## Ôn tập ML06 · Lời giải

### ML06-mcq-1 · Đối chiếu

**Chọn B.** Cắt theo thứ tự đã cho và giữ lô cuối.

- A · Cách cắt này bỏ chỉ số còn dư.
- B · Cắt theo thứ tự đã cho và giữ lô cuối.
- C · Thứ tự này xuất phát từ dãy đã sắp lại.

### ML06-mcq-2 · Đối chiếu

**Chọn B.** Kích thước lô phải là số nguyên dương.

- A · Mỗi mẫu tạo một lô.
- B · Kích thước lô phải là số nguyên dương.
- C · Toàn bộ dãy vẫn tạo được một lô.

### ML06-mcq-3 · Đối chiếu

**Chọn A.** Hoán vị phủ đủ các hàng và mỗi hàng chỉ xuất hiện một lần.

- A · Hoán vị phủ đủ các hàng và mỗi hàng chỉ xuất hiện một lần.
- B · Hoán vị có thể có thứ tự bất kỳ.
- C · Chỉ số đầu của dãy có thể khác 0.

### ML06-mcq-4 · Đối chiếu

**Chọn B.** Các kích thước là 4,4,2.

- A · Hai lô chỉ dùng tám mẫu.
- B · Các kích thước là 4,4,2.
- C · Lô size không phải số lô.

### ML06-mcq-5 · Đối chiếu

**Chọn A.** Cùng chỉ số giữ đúng nhãn của mỗi hàng.

- A · Cùng chỉ số giữ đúng nhãn của mỗi hàng.
- B · Hai permutation khác nhau có thể gắn nhầm nhãn.
- C · Đổi riêng nhãn phá cặp dữ liệu.

### ML06-mcq-6 · Đối chiếu

**Chọn C.** Mỗi bước dùng gradient từ một mẫu.

- A · Đó là lô đầy đủ.
- B · Lô size đã cho là 1.
- C · Mỗi bước dùng gradient từ một mẫu.

### ML06-mcq-7 · Đối chiếu

**Chọn A.** Toàn tập nằm trong một lô.

- A · Toàn tập nằm trong một lô.
- B · Nhầm một bước trên mỗi mẫu với lô đầy đủ.
- C · Có một lô hợp lệ.

### ML06-mcq-8 · Đối chiếu

**Chọn B.** Hạt giống ngẫu nhiên giúp lặp lại thí nghiệm khi trạng thái và lời gọi được giữ.

- A · Hạt giống ngẫu nhiên không bảo đảm chất lượng mô hình.
- B · Hạt giống ngẫu nhiên giúp lặp lại thí nghiệm khi trạng thái và lời gọi được giữ.
- C · Generator tiến trạng thái qua các lần gọi.

### ML06-mcq-9 · Đối chiếu

**Chọn C.** Dùng số mẫu thực tế của lô.

- A · Chia 4 làm sai gradient trung bình của lô ngắn.
- B · Đó không phải trung bình lô hiện tại.
- C · Dùng số mẫu thực tế của lô.

### ML06-mcq-10 · Đối chiếu

**Chọn A.** Quy tắc drop-last làm mất mẫu phần dư trong lượt qua dữ liệu đó. Phải công bố.

- A · Quy tắc drop-last làm mất mẫu phần dư trong lượt qua dữ liệu đó. Phải công bố.
- B · Đã bỏ một mẫu phần dư.
- C · Có hai lô đầy đủ.

### ML06-practice-1 · Đối chiếu

Các lô có 4,4,3 mẫu. Có 3 bước cập nhật.

```python
n,b=11,4
print([min(b,n-i) for i in range(0,n,b)])
```
Kết quả [4, 4, 3]

### ML06-practice-2 · Đối chiếu

Có. Một lô chứa cả 5 mẫu. Lô size là giới hạn chia, không buộc mọi lô đủ 8.

### ML06-practice-3 · Đối chiếu

Kết quả [30,10,20] và [3,1,2]. Mỗi nhãn đi cùng mẫu tương ứng.

```python
import numpy as np
idx=np.array([2,0,1]);X=np.array([10,20,30]);y=np.array([1,2,3])
print(X[idx].tolist())
print(y[idx].tolist())
```
Kết quả [30, 10, 20]
[3, 1, 2]

### ML06-practice-4 · Đối chiếu

Kích thước vẫn khớp nên phép toán chạy, nhưng nhãn không còn thuộc đúng mẫu. Tính hợp lệ kích thước không bảo đảm cặp dữ liệu đúng.

### ML06-practice-5 · Đối chiếu

Các nhóm chỉ số là [4,1],[3,0],[2].

```python
idx=[4,1,3,0,2]
print([idx[i:i+2] for i in range(0,len(idx),2)])
```
Kết quả [[4, 1], [3, 0], [2]]

### ML06-practice-6 · Đối chiếu

Lần lượt 1,4,12 bước. Không có nghĩa các phương pháp đạt cùng tham số sau một lượt qua dữ liệu vì tham số cập nhật giữa các lô.

```python
n=12
for b in [12,3,1]:
    print(len(range(0,n,b)))
```
Kết quả 1
4
12

### ML06-practice-7 · Đối chiếu

Có trong cùng môi trường NumPy và cùng chuỗi lời gọi. Không cần hard-mã permutation để kiểm tính tái lập.

```python
import numpy as np
a=np.random.default_rng(7).permutation(6)
b=np.random.default_rng(7).permutation(6)
print(bool(np.array_equal(a,b)))
```
Kết quả True

### ML06-practice-8 · Đối chiếu

Gradient=4. Theta_new=1−0.1×4=0.6.

```python
g=sum([2.,6.])/2
print(g)
print(round(1.-.1*g,4))
```
Kết quả 4.0
0.6

### ML06-practice-9 · Đối chiếu

Kích thước lô phải là số nguyên dương. Bước range bằng 0 không hợp lệ và không định nghĩa được cách tiến qua dữ liệu.

### ML06-practice-10 · Đối chiếu

Step là một lần cập nhật từ lô hiện tại. Lượt qua dữ liệu là một lượt đi qua tập tập huấn luyện theo quy tắc duyệt. Có thể gồm nhiều step.

### ML06-practice-11 · Đối chiếu

Ghép tất cả chỉ số lô phải chứa mỗi chỉ số từ 0 đến n−1 đúng một lần nếu không sampling có hoàn lại hoặc bỏ lô cuối.

```python
idx=[4,1,3,0,2];batches=[idx[i:i+2] for i in range(0,len(idx),2)]
flat=[j for batch in batches for j in batch]
print(sorted(flat)==list(range(5)))
```
Kết quả True

### ML06-practice-12 · Đối chiếu

Mỗi lô chỉ chứa một phần dữ liệu, có phân bố và phần dư khác nhau. Gradient ước lượng có biến thiên giữa lô. Không từ đó kết luận mọi bước đều giảm tổn thất toàn tập.

## Ôn tập ML07 · Lời giải

### ML07-mcq-1 · Đối chiếu

**Chọn B.** Cột đầu đi cùng hệ số tự do đứng đầu vectơ kết quả.

- A · Thêm một hàng sẽ làm thay đổi số mẫu.
- B · Cột đầu đi cùng hệ số tự do đứng đầu vectơ kết quả.
- C · Các cột đặc trưng vẫn cần có mặt.

### ML07-mcq-2 · Đối chiếu

**Chọn C.** lstsq trả nghiệm bình phương tối thiểu có chuẩn nhỏ nhất khi có nhiều nghiệm.

- A · Hai cột trùng nhau khiến ma trận Gram suy biến.
- B · Bỏ một nhãn làm mất sự tương ứng giữa hàng và nhãn.
- C · lstsq trả nghiệm bình phương tối thiểu có chuẩn nhỏ nhất khi có nhiều nghiệm.

### ML07-mcq-3 · Đối chiếu

**Chọn B.** Mỗi hàng cần một giá trị đích tương ứng.

- A · Số cột biểu diễn số đặc trưng.
- B · Mỗi hàng cần một giá trị đích tương ứng.
- C · Số tham số được xác định theo số cột.

### ML07-mcq-4 · Đối chiếu

**Chọn B.** (3,10) nhân (10,3) cho (3,3).

- A · Đó là kích thước của X@X.T.
- B · (3,10) nhân (10,3) cho (3,3).
- C · Đây là kích thước X, không phải Gram ma trận.

### ML07-mcq-5 · Đối chiếu

**Chọn A.** Khi đó X.T@X khả nghịch trong số học chính xác.

- A · Khi đó X.T@X khả nghịch trong số học chính xác.
- B · Số phần tử không xác định tính độc lập cột.
- C · Nhãn trùng không tự gây suy biến ma trận thiết kế.

### ML07-mcq-6 · Đối chiếu

**Chọn C.** Công thức nghịch đảo không áp dụng. bình phương tối thiểu vẫn có thể có nhiều nghiệm.

- A · Hai cột trùng tạo phụ thuộc tuyến tính.
- B · Gram ma trận chỉ phụ thuộc X.
- C · Công thức nghịch đảo không áp dụng. bình phương tối thiểu vẫn có thể có nhiều nghiệm.

### ML07-mcq-7 · Đối chiếu

**Chọn A.** Cột toàn 1 nhân theta[0] tạo thành phần chặn.

- A · Cột toàn 1 nhân theta[0] tạo thành phần chặn.
- B · Theta chứa hệ số mô hình, không chứa số mẫu.
- C · Theta là tham số, không phải gradient.

### ML07-mcq-8 · Đối chiếu

**Chọn B.** Đây thường là lựa chọn tốt hơn về thực thi và số học. Phương trình chuẩn vẫn có hạn chế điều kiện số.

- A · Solve vẫn cần hệ hợp lệ và có thể thất bại khi suy biến.
- B · Đây thường là lựa chọn tốt hơn về thực thi và số học. Phương trình chuẩn vẫn có hạn chế điều kiện số.
- C · Kích thước vẫn phải khớp.

### ML07-mcq-9 · Đối chiếu

**Chọn C.** Có thể dùng lstsq/pseudoinverse để chọn nghiệm. Không dùng nghịch đảo chuẩn.

- A · bình phương tối thiểu tuyến tính vẫn có nghiệm tối ưu.
- B · Tính hữu hạn y là vấn đề khác.
- C · Có thể dùng lstsq/pseudoinverse để chọn nghiệm. Không dùng nghịch đảo chuẩn.

### ML07-mcq-10 · Đối chiếu

**Chọn A.** Điều kiện khả nghịch toán học khác độ điều kiện số và sai số tính toán.

- A · Điều kiện khả nghịch toán học khác độ điều kiện số và sai số tính toán.
- B · Số thực máy có sai số.
- C · Tạo nghịch đảo không bảo đảm ổn định hơn.

### ML07-practice-1 · Đối chiếu

X.T@y là vectơ (3,). Theta là vectơ (3,). Nếu X đã chứa hệ số tự do thì ba thành phần đã gồm hệ số tự do.

### ML07-practice-2 · Đối chiếu

Kết quả [[2,3],[3,5]].

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]])
print((X.T@X).tolist())
```
Kết quả [[2.0, 3.0], [3.0, 5.0]]

### ML07-practice-3 · Đối chiếu

Kết quả [6,10].

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]]);y=np.array([2.,4.])
print((X.T@y).tolist())
```
Kết quả [6.0, 10.0]

### ML07-practice-4 · Đối chiếu

Theta=[0,2], nên dự đoán là 0+2x.

```python
import numpy as np
X=np.array([[1.,1.],[1.,2.]]);y=np.array([2.,4.])
t=np.linalg.solve(X.T@X,X.T@y)
print(np.round(t,6).tolist())
```
Kết quả [0.0, 2.0]

### ML07-practice-5 · Đối chiếu

Theta=(4+16)⁻¹(6+24)=1.5.

```python
import numpy as np
X=np.array([[2.],[4.]]);y=np.array([3.,6.])
print(np.linalg.solve(X.T@X,X.T@y).tolist())
```
Kết quả [1.5]

### ML07-practice-6 · Đối chiếu

Rank=1<2 vì cột hai gấp đôi cột một. Gram ma trận suy biến.

```python
import numpy as np
X=np.array([[1.,2.],[2.,4.]])
print(int(np.linalg.matrix_rank(X)))
```
Kết quả 1

### ML07-practice-7 · Đối chiếu

Không. Rank không vượt min(2,3)=2 nên không thể bằng 3. Không áp dụng công thức nghịch đảo của Gram ma trận.

### ML07-practice-8 · Đối chiếu

X là 2D nên kích thước là (m, d), y là 1D nên kích thước là (m,). Hai tuple vốn khác nhau. Phải kiểm ndim rồi so X.shape[0] với y.shape[0].

### ML07-practice-9 · Đối chiếu

A.shape là tuple kích thước, không phải số cột. Với A vuông, so rank với A.shape[0] sau khi kiểm A là ma trận vuông.

### ML07-practice-10 · Đối chiếu

Theta xấp xỉ [0,0.08]. Không làm tròn bên trong solver chỉ để trông giống đáp án.

```python
import numpy as np
x=np.array([20.,40.]);X=np.column_stack([np.ones(2),x]);y=np.array([1.6,3.2])
t=np.linalg.solve(X.T@X,X.T@y)
print(bool(np.allclose(t,[0.,.08],rtol=1e-9,atol=1e-12)))
```
Kết quả True

### ML07-practice-11 · Đối chiếu

Không nói chung. Cần hoán vị theta tương ứng với hoán vị cột. Các hệ số phải gắn đúng đặc trưng.

### ML07-practice-12 · Đối chiếu

Hai cột giống nhau chỉ xác định được tổng hai hệ số. Hàm lstsq chọn nghiệm có chuẩn Euclid nhỏ nhất và vẫn cho dự đoán hữu hạn.

```python
import numpy as np
X=np.array([[1.,1.],[2.,2.],[3.,3.]]);y=np.array([2.,4.,6.])
t=np.linalg.lstsq(X,y,rcond=None)[0]
print(bool(np.allclose(X@t,y)))
```
Kết quả True

## Ôn tập ML08 · Lời giải

### ML08-mcq-1 · Đối chiếu

**Chọn B.** Các số mũ tăng từ 0 đến 2.

- A · Hàng này thiếu cột cho hệ số tự do.
- B · Các số mũ tăng từ 0 đến 2.
- C · 2x chỉ là bội của x.

### ML08-mcq-2 · Đối chiếu

**Chọn A.** Bậc 0 tạo một cột toàn 1.

- A · Bậc 0 tạo một cột toàn 1.
- B · Giá trị cơ sở hằng được chọn bằng 1.
- C · Vẫn cần một cột cho hằng số.

### ML08-mcq-3 · Đối chiếu

**Chọn B.** Mỗi trọng số phải nhân với cùng một lũy thừa ở hai tập.

- A · Thứ tự các mẫu không xác định ý nghĩa hệ số.
- B · Mỗi trọng số phải nhân với cùng một lũy thừa ở hai tập.
- C · Đổi thứ tự này sẽ ghép hệ số với sai lũy thừa.

### ML08-mcq-4 · Đối chiếu

**Chọn A.** Ba cột gồm hệ số tự do và hai lũy thừa.

- A · Ba cột gồm hệ số tự do và hai lũy thừa.
- B · Đảo hai trục mẫu/đặc trưng.
- C · Đã bỏ qua cột hệ số tự do.

### ML08-mcq-5 · Đối chiếu

**Chọn B.** Các cột 1, x, x² cố định. Dự đoán là tích ma trận với theta.

- A · Phi tuyến theo x khác phi tuyến theo theta.
- B · Các cột 1, x, x² cố định. Dự đoán là tích ma trận với theta.
- C · Không cần ép hệ số bậc hai bằng 0.

### ML08-mcq-6 · Đối chiếu

**Chọn C.** Cần đánh giá trên dữ liệu chưa dùng huấn luyện.

- A · Mô hình phức tạp có thể quá khớp.
- B · Khớp tập huấn luyện không bảo đảm khớp tập kiểm tra.
- C · Cần đánh giá trên dữ liệu chưa dùng huấn luyện.

### ML08-mcq-7 · Đối chiếu

**Chọn A.** Lần lượt x⁰, x¹, x², x³.

- A · Lần lượt x⁰, x¹, x², x³.
- B · Nhân x với số mũ không phải lấy lũy thừa.
- C · Đây không phải các lũy thừa của 2.

### ML08-mcq-8 · Đối chiếu

**Chọn B.** Thứ tự và định nghĩa cột tạo hợp đồng với theta.

- A · Số mẫu hai tập có thể khác nhau.
- B · Thứ tự và định nghĩa cột tạo hợp đồng với theta.
- C · Không cần và không nên ép dữ liệu hai tập giống nhau.

### ML08-mcq-9 · Đối chiếu

**Chọn C.** Hai cột giống nhau làm mất đủ hạng cột. nghịch đảo chuẩn có thể không dùng được.

- A · Thêm cột không thêm hàng.
- B · Không có bảo đảm giảm quá khớp.
- C · Hai cột giống nhau làm mất đủ hạng cột. nghịch đảo chuẩn có thể không dùng được.

### ML08-mcq-10 · Đối chiếu

**Chọn A.** Cần kiểm dữ liệu thực tế, chẳng hạn toàn x=1 tạo hai cột giống nhau.

- A · Cần kiểm dữ liệu thực tế, chẳng hạn toàn x=1 tạo hai cột giống nhau.
- B · Trên dữ liệu đặc biệt như x toàn 1 chúng trùng nhau.
- C · Chẵn lẻ không quyết định rank.

### ML08-practice-1 · Đối chiếu

Các hàng là [1,0,0],[1,1,1],[1,2,4].

```python
import numpy as np
x=np.array([0.,1.,2.])
print(np.column_stack([np.ones(len(x)),x,x**2]).tolist())
```
Kết quả [[1.0, 0.0, 0.0], [1.0, 1.0, 1.0], [1.0, 2.0, 4.0]]

### ML08-practice-2 · Đối chiếu

1+2×2+3×4=17.

```python
import numpy as np
print(float(np.array([1.,2.,4.])@np.array([1.,2.,3.])))
```
Kết quả 17.0

### ML08-practice-3 · Đối chiếu

[1,−2,4,−8]. Số mũ lẻ giữ dấu âm.

```python
x=-2
print([x**i for i in range(4)])
```
Kết quả [1, -2, 4, -8]

### ML08-practice-4 · Đối chiếu

Ma trận (5,5). Có 5 hệ số. Điều này chưa tự chứng minh ma trận đủ hạng.

### ML08-practice-5 · Đối chiếu

Bình phương [1,4,9] khác nhân đôi [2,4,6].

```python
import numpy as np
x=np.array([1,2,3])
print((x**2).tolist())
print((2*x).tolist())
```
Kết quả [1, 4, 9]
[2, 4, 6]

### ML08-practice-6 · Đối chiếu

Các dự đoán là [1,4,9].

```python
import numpy as np
X=np.array([[1.,0.,0.],[1.,1.,1.],[1.,2.,4.]])
print((X@np.array([1.,2.,1.])).tolist())
```
Kết quả [1.0, 4.0, 9.0]

### ML08-practice-7 · Đối chiếu

Các phép lũy thừa được tính thành cột dữ liệu trước. Mô hình sau đó cộng tuyến tính các cột với trọng số theta. Phi tuyến nằm ở ánh xạ x sang đặc trưng.

### ML08-practice-8 · Đối chiếu

Không. Chỉ biết bậc 6 khớp tập huấn luyện hơn, chưa có bằng chứng về tổng quát hóa. Cần đánh giá theo quy trình dữ liệu riêng sẽ học ở ML13.

### ML08-practice-9 · Đối chiếu

Thiếu hệ số tự do làm số cột không khớp theta ba phần tử. Cần áp dụng cùng phép tạo đặc trưng ở hai nơi.

### ML08-practice-10 · Đối chiếu

x=10, x⁴=10000. Các cột có độ lớn chênh lệch có thể gây vấn đề tối ưu/số học. Cần dùng đúng quy trình chuẩn hóa đã học.

### ML08-practice-11 · Đối chiếu

Không, ba cột đều giống nhau, rank chỉ 1.

```python
import numpy as np
x=np.ones(3);X=np.column_stack([np.ones(3),x,x**2])
print(int(np.linalg.matrix_rank(X)))
```
Kết quả 1

### ML08-practice-12 · Đối chiếu

Chỉ có cột toàn 1 nên mô hình dự đoán hằng theta0 cho mọi mẫu. Không phụ thuộc x.

## Ôn tập ML09 · Lời giải

### ML09-mcq-1 · Đối chiếu

**Chọn A.** Tổ hợp tuyến tính có thể âm, dương hoặc 0.

- A · Tổ hợp tuyến tính có thể âm, dương hoặc 0.
- B · Đó là miền xác suất, không phải logit.
- C · Z có thể liên tục.

### ML09-mcq-2 · Đối chiếu

**Chọn B.** exp(−ln3)=1/3 nên 1/(1+1/3)=3/4.

- A · Chưa ánh xạ qua sigmoid.
- B · exp(−ln3)=1/3 nên 1/(1+1/3)=3/4.
- C · Đó là sigmoid(−ln3).

### ML09-mcq-3 · Đối chiếu

**Chọn C.** Sigmoid(−z)=1−sigmoid(z).

- A · Có thể vượt 1.
- B · Xác suất không âm.
- C · Sigmoid(−z)=1−sigmoid(z).

### ML09-mcq-4 · Đối chiếu

**Chọn B.** 1/(1+exp(0))=1/2.

- A · Sigmoid hữu hạn luôn dương.
- B · 1/(1+exp(0))=1/2.
- C · Sigmoid tại 0 không phải 1.

### ML09-mcq-5 · Đối chiếu

**Chọn A.** Sigmoid tăng và z<0 cho p<0.5.

- A · Sigmoid tăng và z<0 cho p<0.5.
- B · Sai dấu so với ngưỡng.
- C · Dự đoán không cần biết nhãn thật.

### ML09-mcq-6 · Đối chiếu

**Chọn C.** Đó là ý nghĩa đầu ra mô hình, không phải bằng chứng hiệu chuẩn xác suất.

- A · Xác suất không phải bảo đảm sự kiện.
- B · Một dự đoán không xác định accuracy toàn tập.
- C · Đó là ý nghĩa đầu ra mô hình, không phải bằng chứng hiệu chuẩn xác suất.

### ML09-mcq-7 · Đối chiếu

**Chọn A.** Sigmoid(0)=0.5.

- A · Sigmoid(0)=0.5.
- B · Nhầm xác suất với đầu vào sigmoid.
- C · Sigmoid(1) lớn hơn 0.5.

### ML09-mcq-8 · Đối chiếu

**Chọn B.** Điều kiện chặt hơn nên chỉ giữ nguyên hoặc giảm số dự đoán 1.

- A · Ngưỡng không thay đổi xác suất mô hình.
- B · Điều kiện chặt hơn nên chỉ giữ nguyên hoặc giảm số dự đoán 1.
- C · Mức thay đổi phụ thuộc phân bố p.

### ML09-mcq-9 · Đối chiếu

**Chọn C.** Z tuyến tính theo đặc trưng mở rộng có thể phi tuyến theo tọa độ gốc.

- A · Phi tuyến theo x có thể xuất hiện qua ánh xạ đặc trưng.
- B · Sigmoid vẫn ánh xạ z sang xác suất.
- C · Z tuyến tính theo đặc trưng mở rộng có thể phi tuyến theo tọa độ gốc.

### ML09-mcq-10 · Đối chiếu

**Chọn A.** Sigmoid là hàm tăng.

- A · Sigmoid là hàm tăng.
- B · Sigmoid tăng theo z.
- C · Xác suất có thể đổi dù nhãn ngưỡng giữ nguyên.

### ML09-practice-1 · Đối chiếu

Kết quả 0.5.

```python
import numpy as np
print(float(1/(1+np.exp(0.))))
```
Kết quả 0.5

### ML09-practice-2 · Đối chiếu

Xấp xỉ [0.1192,0.5,0.8808].

```python
import numpy as np
z=np.array([-2.,0.,2.])
print(np.round(1/(1+np.exp(-z)),4).tolist())
```
Kết quả [0.1192, 0.5, 0.8808]

### ML09-practice-3 · Đối chiếu

Kết quả [0,1,1]. P đúng ngưỡng thuộc lớp 1 theo quy ước đề.

```python
import numpy as np
p=np.array([.2,.5,.9])
print((p>=.5).astype(int).tolist())
```
Kết quả [0, 1, 1]

### ML09-practice-4 · Đối chiếu

−3+2x=0 nên x=1.5. Phía x lớn hơn có z>0 và p>0.5.

### ML09-practice-5 · Đối chiếu

z=1, p≈0.7311.

```python
import numpy as np
z=-3.+2.*2.
print(z)
print(round(float(1/(1+np.exp(-z))),4))
```
Kết quả 1.0
0.7311

### ML09-practice-6 · Đối chiếu

Hai bộ nhãn là [0,1,1] và [0,0,1].

```python
import numpy as np
p=np.array([.4,.6,.8])
for threshold in [.5,.8]:
    print((p>=threshold).astype(int).tolist())
```
Kết quả [0, 1, 1]
[0, 0, 1]

### ML09-practice-7 · Đối chiếu

Z có thể là bất kỳ số thực nào, kể cả âm hoặc lớn hơn 1. Sigmoid ánh xạ z sang khoảng (0,1).

### ML09-practice-8 · Đối chiếu

Hai phía bằng nhau trong dung sai số học. Không so chuỗi thập phân.

```python
import numpy as np
s=lambda z:1/(1+np.exp(-z))
print(bool(np.isclose(s(-2.),1-s(2.))))
```
Kết quả True

### ML09-practice-9 · Đối chiếu

Ví dụ (1,2),(2,1), vì tổng hai tọa độ bằng 3. Đây là đường thẳng theo hai thuộc tính gốc.

### ML09-practice-10 · Đối chiếu

z=0 cho x=−1 và x=1. Lớp 1 ở |x|≥1 theo quy tắc ≥, lớp 0 khi |x|<1.

### ML09-practice-11 · Đối chiếu

Không. Xác suất mô hình không bảo đảm nhãn từng mẫu. Cần tách lỗi tính toán khỏi dự đoán sai của mô hình.

### ML09-practice-12 · Đối chiếu

z=[−1,1]. Dự đoán [0,1]. Cột đầu là hệ số tự do.

```python
import numpy as np
X=np.array([[1.,0.],[1.,2.]]);theta=np.array([-1.,1.])
z=X@theta
print(z.tolist())
print((1/(1+np.exp(-z))>=.5).astype(int).tolist())
```
Kết quả [-1.0, 1.0]
[0, 1]

## Ôn tập ML10 · Lời giải

### ML10-mcq-1 · Đối chiếu

**Chọn A.** Thay y=0 vào công thức BCE.

- A · Thay y=0 vào công thức BCE.
- B · Đây là nhánh y=1.
- C · Đó là phần dư xác suất.

### ML10-mcq-2 · Đối chiếu

**Chọn B.** −ln(p) giảm khi p tăng.

- A · Tổn thất phụ thuộc p.
- B · −ln(p) giảm khi p tăng.
- C · Xác suất dành cho nhãn thật tăng nên tổn thất giảm.

### ML10-mcq-3 · Đối chiếu

**Chọn C.** X.T@(p−y)/8 trả một gradient cho mỗi hệ số.

- A · Đó là phần dư theo mẫu.
- B · Đó là kích thước X.
- C · X.T@(p−y)/8 trả một gradient cho mỗi hệ số.

### ML10-mcq-4 · Đối chiếu

**Chọn A.** Thay y=1 vào −y log(p)−(1−y)log(1−p).

- A · Thay y=1 vào −y log(p)−(1−y)log(1−p).
- B · Đây là tổn thất khi y=0.
- C · Sai dấu, log(p) âm với p trong (0,1).

### ML10-mcq-5 · Đối chiếu

**Chọn B.** −log(0.9) nhỏ hơn −log(0.1).

- A · Độ tin cậy cao vào lớp sai bị phạt mạnh.
- B · −log(0.9) nhỏ hơn −log(0.1).
- C · Tổn thất phụ thuộc xác suất gán cho nhãn đúng.

### ML10-mcq-6 · Đối chiếu

**Chọn C.** Đây là gradient của trung bình BCE logistic không có regularization.

- A · Đảo dấu gradient. Trừ nó sẽ đi sai hướng.
- B · Chưa ánh xạ phần dư mẫu về không gian tham số.
- C · Đây là gradient của trung bình BCE logistic không có regularization.

### ML10-mcq-7 · Đối chiếu

**Chọn A.** Đây là biện pháp ổn định tính toán. Epsilon cần rõ ràng.

- A · Đây là biện pháp ổn định tính toán. Epsilon cần rõ ràng.
- B · Clipping không cải thiện nhãn thật hay bảo đảm chất lượng.
- C · Rò rỉ dữ liệu thuộc quy trình dữ liệu.

### ML10-mcq-8 · Đối chiếu

**Chọn B.** Mỗi mẫu đóng góp một phần dư xác suất.

- A · Đó là kích thước gradient sau nhân X.T, không phải residual.
- B · Mỗi mẫu đóng góp một phần dư xác suất.
- C · Chỉ có thể vô tình thành ma trận khi kích thước bị broadcast sai.

### ML10-mcq-9 · Đối chiếu

**Chọn C.** Xác suất gán cho nhãn đúng càng gần 0, −log càng lớn.

- A · BCE xét độ tin cậy chứ không chỉ nhãn sau ngưỡng.
- B · BCE không bị chặn trên bởi 1.
- C · Xác suất gán cho nhãn đúng càng gần 0, −log càng lớn.

### ML10-mcq-10 · Đối chiếu

**Chọn A.** −log(p) tăng khi p tiến về 0 từ bên phải.

- A · −log(p) tăng khi p tiến về 0 từ bên phải.
- B · Dự đoán đang sai ngày càng tự tin.
- C · BCE không giới hạn ở 1.

### ML10-practice-1 · Đối chiếu

−log(0.8)≈0.223144.

```python
import numpy as np
print(f"{-np.log(.8):.6f}")
```
Kết quả 0.223144

### ML10-practice-2 · Đối chiếu

−log(1−0.2)=−log(0.8), bằng nhau.

```python
import numpy as np
print(f"{-np.log(1-.2):.6f}")
```
Kết quả 0.223144

### ML10-practice-3 · Đối chiếu

Trung bình của −log(0.8) và −log(0.7), xấp xỉ 0.289909.

```python
import numpy as np
y=np.array([1.,0.]);p=np.array([.8,.3])
print(f"{-np.mean(y*np.log(p)+(1-y)*np.log(1-p)):.6f}")
```
Kết quả 0.289909

### ML10-practice-4 · Đối chiếu

Lần lượt khoảng 0.105361 và 2.302585. Dự đoán sai tự tin bị phạt mạnh.

```python
import numpy as np
for p in [.9,.1]:
    print(f"{-np.log(p):.6f}")
```
Kết quả 0.105361
2.302585

### ML10-practice-5 · Đối chiếu

p=[0.5,0.5]. Residual=[0.5,−0.5]. Gradient=[0,−0.25].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);y=np.array([0.,1.]);p=np.full(2,.5)
print(p.tolist())
print((X.T@(p-y)/len(y)).tolist())
```
Kết quả [0.5, 0.5]
[0.0, -0.25]

### ML10-practice-6 · Đối chiếu

Theta mới [0,0.025].

```python
import numpy as np
theta=np.zeros(2);g=np.array([0.,-.25])
print((theta-.1*g).tolist())
```
Kết quả [0.0, 0.025]

### ML10-practice-7 · Đối chiếu

Broadcasting có thể tạo ma trận (m, m), không còn một phần dư trên mỗi mẫu. Phải chuẩn hóa và kiểm kích thước trước khi tính.

### ML10-practice-8 · Đối chiếu

Sau clipping không có log(0). Tổn thất hữu hạn, nhưng giá trị vẫn phụ thuộc eps.

```python
import numpy as np
p=np.clip(np.array([0.,1.]),1e-6,1-1e-6);y=np.array([1.,0.])
loss=-np.mean(y*np.log(p)+(1-y)*np.log(1-p))
print(bool(np.isfinite(loss)))
```
Kết quả True

### ML10-practice-9 · Đối chiếu

Đổi cơ số nhân tổn thất với hằng số 1/ln(10), gradient cũng phải nhân cùng hằng số. Giữ công thức cũ sẽ không còn là đạo hàm của tổn thất vừa định nghĩa.

### ML10-practice-10 · Đối chiếu

Không. Tổng tổn thất và m cùng nhân đôi. Trung bình giữ nguyên.

### ML10-practice-11 · Đối chiếu

Đều bằng −ln(0.5)=ln(2)≈0.693147.

```python
import numpy as np
print(f"{-np.log(.5):.6f}")
```
Kết quả 0.693147

### ML10-practice-12 · Đối chiếu

BCE giảm từ −ln(0.6) xuống −ln(0.9), dù nhãn dự đoán không đổi. Accuracy một mẫu không mô tả hết thay đổi của xác suất.

## Ôn tập ML11 · Lời giải

### ML11-mcq-1 · Đối chiếu

**Chọn A.** g=2, H=1, t_new=2−2=0.

- A · g=2, H=1, t_new=2−2=0.
- B · Đó có thể là GD với alpha khác, không phải bước Newton ở đây.
- C · Đi sai chiều.

### ML11-mcq-2 · Đối chiếu

**Chọn B.** Gradient và Hessian phải thuộc cùng vectơ tham số.

- A · Tự bỏ tham số.
- B · Gradient và Hessian phải thuộc cùng vectơ tham số.
- C · Thay bài toán không có căn cứ.

### ML11-mcq-3 · Đối chiếu

**Chọn C.** Mỗi phần tử đường chéo tương ứng một mẫu.

- A · W chứa trọng số theo mẫu, không theo tham số.
- B · Không phải đường chéo theo mẫu.
- C · Mỗi phần tử đường chéo tương ứng một mẫu.

### ML11-mcq-4 · Đối chiếu

**Chọn A.** Giải H delta=g, rồi trừ delta khỏi theta.

- A · Giải H delta=g, rồi trừ delta khỏi theta.
- B · Nhân H không phải áp dụng nghịch đảo Hessian.
- C · Đó không phải công thức Newton.

### ML11-mcq-5 · Đối chiếu

**Chọn B.** Mỗi cặp tham số có một đạo hàm bậc hai.

- A · Đây thường là kích thước dữ liệu X.
- B · Mỗi cặp tham số có một đạo hàm bậc hai.
- C · Đây là kích thước theo mẫu, không phải theo cặp tham số.

### ML11-mcq-6 · Đối chiếu

**Chọn C.** Đạo hàm sigmoid là p(1−p).

- A · Nhãn không phải đạo hàm sigmoid.
- B · Đây là phần dư dùng trong gradient.
- C · Đạo hàm sigmoid là p(1−p).

### ML11-mcq-7 · Đối chiếu

**Chọn A.** Công thức chuẩn cần hệ giải được. Không che lỗi bằng kết quả giả.

- A · Công thức chuẩn cần hệ giải được. Không che lỗi bằng kết quả giả.
- B · nghịch đảo không tồn tại khi suy biến.
- C · Tên biến không thay tính chất toán học.

### ML11-mcq-8 · Đối chiếu

**Chọn B.** Cả gradient và Hessian đều thuộc cùng trung bình tổn thất.

- A · Thiếu hệ số so với trung bình gradient.
- B · Cả gradient và Hessian đều thuộc cùng trung bình tổn thất.
- C · Thường sai kích thước và công thức.

### ML11-mcq-9 · Đối chiếu

**Chọn C.** Hành vi cục bộ khác bảo đảm toàn cục.

- A · Đó là kết luận quá mức.
- B · Phương pháp cần đạo hàm bậc hai phù hợp.
- C · Hành vi cục bộ khác bảo đảm toàn cục.

### ML11-mcq-10 · Đối chiếu

**Chọn A.** Solve(H,0)=0, tham số không đổi.

- A · Solve(H,0)=0, tham số không đổi.
- B · H delta=0 có nghiệm duy nhất 0.
- C · Giả định đã bảo đảm giải được.

### ML11-practice-1 · Đối chiếu

Delta=[1,2].

```python
import numpy as np
H=np.diag([2.,4.]);g=np.array([2.,8.])
print(np.linalg.solve(H,g).tolist())
```
Kết quả [1.0, 2.0]

### ML11-practice-2 · Đối chiếu

Theta mới=[2,3].

```python
import numpy as np
print((np.array([3.,5.])-np.array([1.,2.])).tolist())
```
Kết quả [2.0, 3.0]

### ML11-practice-3 · Đối chiếu

g=−3, H=1, t_new=0−(−3)/1=3.

```python
t=0.
g=t-3;H=1.
print(g)
print(H)
print(t-g/H)
```
Kết quả -3.0
1.0
3.0

### ML11-practice-4 · Đối chiếu

Các trọng số là [0.25,0.16].

```python
import numpy as np
p=np.array([.5,.8])
print(np.round(p*(1-p),4).tolist())
```
Kết quả [0.25, 0.16]

### ML11-practice-5 · Đối chiếu

H=[[0.25,0.125],[0.125,0.125]].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);p=np.full(2,.5)
H=X.T@np.diag(p*(1-p))@X/len(p)
print(H.tolist())
```
Kết quả [[0.25, 0.125], [0.125, 0.125]]

### ML11-practice-6 · Đối chiếu

g=[0,−0.25]. Delta=[2,−4]. Theta mới=[−2,4].

```python
import numpy as np
X=np.array([[1.,0.],[1.,1.]]);p=np.full(2,.5);y=np.array([0.,1.])
g=X.T@(p-y)/2;H=X.T@np.diag(p*(1-p))@X/2
print((-np.linalg.solve(H,g)).tolist())
```
Kết quả [-2.0, 4.0]

### ML11-practice-7 · Đối chiếu

Solve tìm delta sao cho H delta=g. Nhân H tạo vectơ H g khác phép nghịch đảo tác động lên g, trừ những trường hợp đặc biệt.

### ML11-practice-8 · Đối chiếu

Báo lỗi kích thước và kiểm lại design ma trận/tham số. Không cắt theta hoặc thêm số để phép tính chạy.

### ML11-practice-9 · Đối chiếu

Rank=1<2 nên suy biến. Bước Newton chuẩn không xác định duy nhất bằng nghịch đảo.

```python
import numpy as np
print(int(np.linalg.matrix_rank([[1.,1.],[1.,1.]])))
```
Kết quả 1

### ML11-practice-10 · Đối chiếu

Tiến gần 0. Điều này có thể làm độ cong nhỏ và hệ Newton khó giải hơn. Không mặc định H luôn ổn định.

### ML11-practice-11 · Đối chiếu

Chúng phải là đạo hàm của cùng một tổn thất. Chia m cho chỉ một trong hai làm tỷ lệ bước Newton sai.

### ML11-practice-12 · Đối chiếu

Dùng allclose kiểm phần dư thay vì so chuỗi số thực.

```python
import numpy as np
H=np.array([[2.,1.],[1.,3.]]);g=np.array([1.,2.])
delta=np.linalg.solve(H,g)
print(bool(np.allclose(H@delta,g)))
```
Kết quả True

## Ôn tập ML12 · Lời giải

### ML12-mcq-1 · Đối chiếu

**Chọn A.** Không khớp mô hình một bộ hệ số cố định như hồi quy tuyến tính chuẩn.

- A · Không khớp mô hình một bộ hệ số cố định như hồi quy tuyến tính chuẩn.
- B · Cần đặc trưng và nhãn tập huấn luyện.
- C · Vẫn cần kích thước, k và miền dữ liệu hợp lệ.

### ML12-mcq-2 · Đối chiếu

**Chọn B.** Khoảng cách tới chính điểm đó bằng 0.

- A · Đó không phải 1-NN.
- B · Khoảng cách tới chính điểm đó bằng 0.
- C · Không phụ thuộc quy tắc này.

### ML12-mcq-3 · Đối chiếu

**Chọn C.** L1 cộng |x_j−z_j|.

- A · Đó là Euclid.
- B · Có thể triệt tiêu dù hai vectơ khác nhau.
- C · L1 cộng |x_j−z_j|.

### ML12-mcq-4 · Đối chiếu

**Chọn B.** sqrt(9+16)=5.

- A · 7 là khoảng cách Manhattan.
- B · sqrt(9+16)=5.
- C · 25 là bình phương khoảng cách.

### ML12-mcq-5 · Đối chiếu

**Chọn A.** Lớp 1 có hai phiếu, lớp 0 có một phiếu.

- A · Lớp 1 có hai phiếu, lớp 0 có một phiếu.
- B · Lớp 0 không chiếm đa số.
- C · Không có hòa phiếu ở ví dụ nhị phân này.

### ML12-mcq-6 · Đối chiếu

**Chọn C.** chuẩn hóa có thể cần thiết. Thống kê chuẩn hóa phải học từ tập huấn luyện.

- A · Đổi đơn vị có thể thay thứ tự láng giềng.
- B · Thang đo không khiến mọi điểm trùng nhau.
- C · chuẩn hóa có thể cần thiết. Thống kê chuẩn hóa phải học từ tập huấn luyện.

### ML12-mcq-7 · Đối chiếu

**Chọn A.** Đó là vi phạm hợp đồng. Không âm thầm sửa dữ liệu.

- A · Đó là vi phạm hợp đồng. Không âm thầm sửa dữ liệu.
- B · Nhân bản thay đổi biểu quyết.
- C · Dùng nhãn tập kiểm tra gây leakage.

### ML12-mcq-8 · Đối chiếu

**Chọn B.** Tính khoảng cách rồi biểu quyết nhãn các láng giềng tập huấn luyện.

- A · Nhãn thật mẫu mới chưa biết và không được dùng để dự đoán.
- B · Tính khoảng cách rồi biểu quyết nhãn các láng giềng tập huấn luyện.
- C · Chỉ số không thay thế dữ liệu thuộc tính.

### ML12-mcq-9 · Đối chiếu

**Chọn C.** Có thể chọn lớp theo quy tắc cố định. Phải ghi rõ và kiểm thử.

- A · Tập kiểm tra phải kiểm hành vi đã định nghĩa.
- B · Dùng nhãn tập kiểm tra là sai quy trình.
- C · Có thể chọn lớp theo quy tắc cố định. Phải ghi rõ và kiểm thử.

### ML12-mcq-10 · Đối chiếu

**Chọn A.** Tổng bình phương mọi sai lệch bằng 0.

- A · Tổng bình phương mọi sai lệch bằng 0.
- B · Không có sai lệch tọa độ.
- C · Công thức xác định trên dữ liệu hữu hạn.

### ML12-practice-1 · Đối chiếu

sqrt((4−1)²+(6−2)²)=5.

```python
import numpy as np
x=np.array([1.,2.]);z=np.array([4.,6.])
print(float(np.sqrt(np.sum((x-z)**2))))
```
Kết quả 5.0

### ML12-practice-2 · Đối chiếu

|4−1|+|6−2|=7.

```python
import numpy as np
print(float(np.abs(np.array([1.,2.])-np.array([4.,6.])).sum()))
```
Kết quả 7.0

### ML12-practice-3 · Đối chiếu

Khoảng cách [2,1,6]. Chỉ số 1 gần nhất.

```python
import numpy as np
X=np.array([0.,3.,8.]);d=np.abs(X-2.)
print(d.tolist())
print(int(np.argmin(d)))
```
Kết quả [2.0, 1.0, 6.0]
1

### ML12-practice-4 · Đối chiếu

Điểm 3 gần nhất, nhãn 1. Dự đoán 1.

### ML12-practice-5 · Đối chiếu

Lớp 0: một phiếu, lớp 1: hai phiếu, dự đoán 1.

```python
labels=[0,1,1]
print(labels.count(0))
print(labels.count(1))
```
Kết quả 1
2

### ML12-practice-6 · Đối chiếu

Chỉ số [1,3], tương ứng 0.1 và 0.2.

```python
import numpy as np
d=np.array([.4,.1,.7,.2])
print(np.argsort(d)[:2].tolist())
```
Kết quả [1, 3]

### ML12-practice-7 · Đối chiếu

Khoảng cách phải trừ các thuộc tính tương ứng. Đảo cột có thể so x₁ của tập huấn luyện với x₂ của query dù kích thước vẫn hợp lệ.

### ML12-practice-8 · Đối chiếu

Một nhãn nhiễu gần query có thể quyết định hoàn toàn dự đoán. Không kết luận k lớn hơn luôn tốt. Cần quy trình chọn k và đánh giá phù hợp.

### ML12-practice-9 · Đối chiếu

Hai phiếu mỗi lớp. Theo quy tắc đã cho, dự đoán 0. Đây là quy ước bài tập chứ không phải mọi k-NN đều dùng như vậy.

### ML12-practice-10 · Đối chiếu

Nếu cắt top-k tại khoảng cách hòa thì lựa chọn có thể phụ thuộc thứ tự sort. Cần quy tắc xác định, chẳng hạn khoảng cách rồi chỉ số tập huấn luyện.

### ML12-practice-11 · Đối chiếu

Nhãn thật của dữ liệu đánh giá không được tham gia lựa chọn cách dự đoán. Nếu chọn theo tập kiểm tra label thì đánh giá bị leakage.

### ML12-practice-12 · Đối chiếu

Các khoảng cách [1,2,5].

```python
import numpy as np
X=np.array([[1.,0.],[0.,2.],[3.,4.]])
print(np.sqrt(np.sum(X**2,axis=1)).tolist())
```
Kết quả [1.0, 2.0, 5.0]

## Ôn tập ML13 · Lời giải

### ML13-mcq-1 · Đối chiếu

**Chọn A.** Các phần tập xác thực phân hoạch tập dữ liệu.

- A · Các phần tập xác thực phân hoạch tập dữ liệu.
- B · Năm là số phần toàn lượt, không phải số lần mỗi mẫu giữ lại.
- C · Mỗi mẫu phải có lượt được đánh giá ngoài tập huấn luyện fold.

### ML13-mcq-2 · Đối chiếu

**Chọn B.** Cách chia cần phù hợp đơn vị tổng quát hóa.

- A · Không liên quan số cột.
- B · Cách chia cần phù hợp đơn vị tổng quát hóa.
- C · Cùng thực thể có thể chia sẻ thông tin.

### ML13-mcq-3 · Đối chiếu

**Chọn C.** CV chọn cấu hình. khớp mô hình cuối dùng phần dữ liệu huấn luyện được phép.

- A · Mô hình phần cuối không bắt buộc là mô hình cuối.
- B · Tập kiểm tra vẫn phải giữ riêng.
- C · CV chọn cấu hình. khớp mô hình cuối dùng phần dữ liệu huấn luyện được phép.

### ML13-mcq-4 · Đối chiếu

**Chọn B.** Tập kiểm tra được giữ riêng để đánh giá cuối theo quy trình đã định.

- A · Thử chọn trên tập kiểm tra làm tập kiểm tra tham gia tối ưu.
- B · Tập kiểm tra được giữ riêng để đánh giá cuối theo quy trình đã định.
- C · Gradient học từ tập huấn luyện, không từ tập kiểm tra.

### ML13-mcq-5 · Đối chiếu

**Chọn A.** Không mang thông tin phần tập xác thực sang lần huấn luyện khác.

- A · Không mang thông tin phần tập xác thực sang lần huấn luyện khác.
- B · Đã học dữ liệu tập xác thực của phần sẽ gây leakage.
- C · Mỗi phần có tập huấn luyện khác nhau, phải khớp mô hình lại.

### ML13-mcq-6 · Đối chiếu

**Chọn C.** Một phần ba giữ lại, hai phần ba dùng tập huấn luyện.

- A · Đảo vai trò phần giữ lại và phần gộp.
- B · Tập xác thực không đồng thời nằm trong tập huấn luyện của cùng fold.
- C · Một phần ba giữ lại, hai phần ba dùng tập huấn luyện.

### ML13-mcq-7 · Đối chiếu

**Chọn A.** Sau đó dùng thống kê ấy biến đổi tập huấn luyện và tập xác thực.

- A · Sau đó dùng thống kê ấy biến đổi tập huấn luyện và tập xác thực.
- B · Thông tin tập xác thực tham gia thống kê.
- C · Không học bước tiền xử lý từ tập xác thực.

### ML13-mcq-8 · Đối chiếu

**Chọn B.** Mỗi lượt giữ một mẫu, tổng cộng n lượt.

- A · Một lần khớp mô hình không đủ n lượt giữ một mẫu.
- B · Mỗi lượt giữ một mẫu, tổng cộng n lượt.
- C · N−1 là số mẫu tập huấn luyện mỗi lượt.

### ML13-mcq-9 · Đối chiếu

**Chọn C.** Cross-tập xác thực dùng để chọn mô hình trong vùng tập huấn luyện. Tập kiểm tra riêng vẫn giữ vai trò cuối.

- A · Chọn theo tập kiểm tra vẫn gây leakage.
- B · Chưa hoàn tất đánh giá mà dùng tập kiểm tra để học làm sai vai trò.
- C · Cross-tập xác thực dùng để chọn mô hình trong vùng tập huấn luyện. Tập kiểm tra riêng vẫn giữ vai trò cuối.

### ML13-mcq-10 · Đối chiếu

**Chọn A.** Ví dụ các kích thước 4,3,3 giữ đủ dữ liệu.

- A · Ví dụ các kích thước 4,3,3 giữ đủ dữ liệu.
- B · Không thể có một phần mẫu.
- C · Có thể chia phần gần đều.

### ML13-practice-1 · Đối chiếu

Còn 15 mẫu. 5 mẫu tập kiểm tra không tham gia bước lựa chọn.

```python
print(20-5)
```
Kết quả 15

### ML13-practice-2 · Đối chiếu

[0,1,2,3],[4,5,6,7],[8,9,10,11]. Đây chỉ là ví dụ minh họa cách chia, chưa phải khuyến nghị bỏ shuffle cho mọi dữ liệu.

```python
indices=list(range(12))
print([indices[i:i+4] for i in range(0,12,4)])
```
Kết quả [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]

### ML13-practice-3 · Đối chiếu

Train=[2,3,4,5], không có giao với tập xác thực.

```python
all_idx=list(range(6));val={0,1}
print([i for i in all_idx if i not in val])
```
Kết quả [2, 3, 4, 5]

### ML13-practice-4 · Đối chiếu

Trung bình bằng 2. Không gọi đây là tập kiểm tra MSE của một tập kiểm tra set riêng.

```python
scores=[1.,2.,3.]
print(sum(scores)/len(scores))
```
Kết quả 2.0

### ML13-practice-5 · Đối chiếu

Mỗi lượt tập huấn luyện 4 mẫu và tập xác thực 1 mẫu. Tổng cộng 5 lần khớp mô hình.

### ML13-practice-6 · Đối chiếu

Mô hình đã thấy các mẫu gọi là tập xác thực. Đổi chỉ số khi dự đoán không xóa thông tin đã học. Phải khớp mô hình độc lập theo tập huấn luyện từng fold.

### ML13-practice-7 · Đối chiếu

Dùng lo=10, hi=20 từ tập huấn luyện phần. Kết quả 2.0.

```python
train=[10.,20.];value=30.
print((value-min(train))/(max(train)-min(train)))
```
Kết quả 2.0

### ML13-practice-8 · Đối chiếu

Tập xác thực phần sau có thể từng nằm trong tập huấn luyện phần trước. Trọng số đã mang thông tin đó, nên phần sau không còn đánh giá từ một lần khớp mô hình độc lập.

### ML13-practice-9 · Đối chiếu

Không. Mỗi mẫu phải thuộc tập xác thực đúng một lần trong một lượt K-phần. Cần kiểm trùng và thiếu chỉ số.

### ML13-practice-10 · Đối chiếu

Ghép lại có đủ sáu chỉ số và không trùng.

```python
folds=[[0,1],[2,3],[4,5]]
flat=[i for f in folds for i in f]
print(sorted(flat)==list(range(6)) and len(flat)==len(set(flat)))
```
Kết quả True

### ML13-practice-11 · Đối chiếu

Điểm một phần có thể phụ thuộc cách chia. Cần tổng hợp theo quy trình CV thay vì chọn lần chia may mắn. Sau lựa chọn thường khớp mô hình lại trên phần tập huấn luyện cho phép và đánh giá tập kiểm tra riêng.

### ML13-practice-12 · Đối chiếu

K-phần thông thường cần ít nhất 2 phần và đủ dữ liệu. Phải từ chối K không hợp lệ trước khi khớp mô hình, không biến lỗi môi trường này thành điểm đánh giá.

## Ôn tập ML14 · Lời giải

### ML14-mcq-1 · Đối chiếu

**Chọn A.** Trung bình bình phương 0 rồi căn bằng 0.

- A · Trung bình bình phương 0 rồi căn bằng 0.
- B · Không có sai lệch.
- C · RMSE vẫn xác định.

### ML14-mcq-2 · Đối chiếu

**Chọn B.** Bất đẳng thức RMS≥AM áp dụng trên |phần dư|.

- A · Cả hai cùng đơn vị y.
- B · Bất đẳng thức RMS≥AM áp dụng trên |phần dư|.
- C · RMS không nhỏ hơn trung bình trị tuyệt đối.

### ML14-mcq-3 · Đối chiếu

**Chọn C.** Nhiều phân bố phần dư khác nhau có cùng trung bình bình phương.

- A · RMSE là đại lượng tổng hợp, không phải từng residual.
- B · Chẵn lẻ không quyết định.
- C · Nhiều phân bố phần dư khác nhau có cùng trung bình bình phương.

### ML14-mcq-4 · Đối chiếu

**Chọn B.** Mean(|e|)=(2+2)/2=2.

- A · Hai dấu không được triệt tiêu trong trị tuyệt đối.
- B · Mean(|e|)=(2+2)/2=2.
- C · 4 là MSE của ví dụ.

### ML14-mcq-5 · Đối chiếu

**Chọn A.** Trung bình bình phương=4, căn bậc hai=2.

- A · Trung bình bình phương=4, căn bậc hai=2.
- B · Đã đảo và tính sai công thức.
- C · Phần dư trái dấu không triệt tiêu sau bình phương.

### ML14-mcq-6 · Đối chiếu

**Chọn C.** Lấy căn MSE đưa đơn vị về cùng y.

- A · Đó là đơn vị MSE.
- B · RMSE vẫn mang đơn vị của nhãn.
- C · Lấy căn MSE đưa đơn vị về cùng y.

### ML14-mcq-7 · Đối chiếu

**Chọn A.** R²=1−SSE/SST nên có thể âm.

- A · R²=1−SSE/SST nên có thể âm.
- B · Tên R² không bảo đảm không âm trong đánh giá dự đoán.
- C · Số mẫu không âm và không liên quan lập luận này.

### ML14-mcq-8 · Đối chiếu

**Chọn B.** Phải nêu quy ước hoặc báo không xác định.

- A · Trường hợp 0/0 chưa tự xác định là 1.
- B · Phải nêu quy ước hoặc báo không xác định.
- C · Không được tự gán 0 nếu chưa định nghĩa.

### ML14-mcq-9 · Đối chiếu

**Chọn C.** Sai lệch gấp đôi góp bình phương gấp bốn.

- A · MSE vẫn dùng mọi residual.
- B · MSE không giữ dấu sau bình phương.
- C · Sai lệch gấp đôi góp bình phương gấp bốn.

### ML14-mcq-10 · Đối chiếu

**Chọn A.** Các trung bình của giá trị hằng giữ đúng công thức.

- A · Các trung bình của giá trị hằng giữ đúng công thức.
- B · MSE bình phương nên bằng 4.
- C · Trị tuyệt đối phần dư không bằng 0.

### ML14-practice-1 · Đối chiếu

Residual=[1,−2].

```python
import numpy as np
y=np.array([1.,3.]);pred=np.array([2.,1.])
print((pred-y).tolist())
```
Kết quả [1.0, -2.0]

### ML14-practice-2 · Đối chiếu

(1+2)/2=1.5.

```python
import numpy as np
print(float(np.mean(np.abs([1.,-2.]))))
```
Kết quả 1.5

### ML14-practice-3 · Đối chiếu

MSE=2.5. RMSE=sqrt(2.5)≈1.581139.

```python
import numpy as np
mse=np.mean(np.array([1.,-2.])**2)
print(float(mse))
print(f"{np.sqrt(mse):.6f}")
```
Kết quả 2.5
1.581139

### ML14-practice-4 · Đối chiếu

Ba sai số bằng 0. SST>0 nên R²=1.

```python
import numpy as np
y=np.array([1.,2.,3.]);e=np.zeros(3)
print(float(np.mean(np.abs(e))))
print(float(np.mean(e**2)))
print(float(np.sqrt(np.mean(e**2))))
print(float(1-np.sum(e**2)/np.sum((y-y.mean())**2)))
```
Kết quả 0.0
0.0
0.0
1.0

### ML14-practice-5 · Đối chiếu

Dự đoán bằng trung bình y, SSE=SST=2 nên R²=0.

```python
import numpy as np
y=np.array([1.,2.,3.]);pred=np.full(3,2.)
print(float(1-np.sum((pred-y)**2)/np.sum((y-y.mean())**2)))
```
Kết quả 0.0

### ML14-practice-6 · Đối chiếu

SSE=14, SST=2 nên R²=1−7=−6.

```python
import numpy as np
y=np.array([1.,2.,3.])
print(float(1-np.sum(y**2)/np.sum((y-y.mean())**2)))
```
Kết quả -6.0

### ML14-practice-7 · Đối chiếu

MSE=Σe²/m=2E. Chúng có cùng vị trí cực tiểu khi dữ liệu cố định nhưng giá trị khác nhau.

### ML14-practice-8 · Đối chiếu

MAE đều 2. MSE lần lượt 8 và 4, phản ánh ảnh hưởng của phần dư lớn.

```python
import numpy as np
for e in [[0.,4.],[2.,2.]]:
    a=np.array(e)
    print((float(np.abs(a).mean()),float((a*a).mean())))
```
Kết quả (2.0, 8.0)
(2.0, 4.0)

### ML14-practice-9 · Đối chiếu

Trung bình bằng 5 và SST=0. Khi SSE=0, công thức có 0/0. Cần ghi không xác định hoặc quy ước rõ ràng thay vì dùng phép chia trực tiếp.

### ML14-practice-10 · Đối chiếu

MAE và RMSE nhân 1000. MSE nhân 1000000. R² giữ nguyên nếu SST>0 vì cả SSE và SST nhân cùng hệ số bình phương.

### ML14-practice-11 · Đối chiếu

Sai tên tập đánh giá. Đây là training MSE. Phải giữ dữ liệu đánh giá riêng và ghi đúng tập dùng để tính.

### ML14-practice-12 · Đối chiếu

Không. Chưa có quan sát để lấy trung bình. Phải từ chối hoặc báo không có dữ liệu theo hợp đồng đã định.

## Ôn tập ML15 · Lời giải

### ML15-mcq-1 · Đối chiếu

**Chọn A.** Âm dự đoán sai trên mẫu dương thật.

- A · Âm dự đoán sai trên mẫu dương thật.
- B · FP là true=0, pred=1.
- C · TN cần true=pred=0.

### ML15-mcq-2 · Đối chiếu

**Chọn B.** Cả nhãn thật và dự đoán đều âm.

- A · FN cần true=1.
- B · Cả nhãn thật và dự đoán đều âm.
- C · TP cần lớp dương.

### ML15-mcq-3 · Đối chiếu

**Chọn C.** Ví dụ TP=1, FP=0, FN=9 cho precision=1, recall=0.1.

- A · Vẫn có thể bỏ sót nhiều mẫu dương.
- B · Precision=1 với mẫu số dương đòi FP=0.
- C · Ví dụ TP=1, FP=0, FN=9 cho precision=1, recall=0.1.

### ML15-mcq-4 · Đối chiếu

**Chọn B.** Dự đoán dương sai: dương giả.

- A · FN là thật 1 nhưng dự đoán 0.
- B · Dự đoán dương sai: dương giả.
- C · TP cần thật và dự đoán đều dương.

### ML15-mcq-5 · Đối chiếu

**Chọn A.** Mẫu số là toàn bộ dự đoán dương.

- A · Mẫu số là toàn bộ dự đoán dương.
- B · Đây là recall.
- C · Đây là accuracy.

### ML15-mcq-6 · Đối chiếu

**Chọn C.** Recall=TP/(TP+FN).

- A · Đó là precision.
- B · Đó là accuracy.
- C · Recall=TP/(TP+FN).

### ML15-mcq-7 · Đối chiếu

**Chọn A.** 2TP/(2TP+FP+FN)=6/9=2/3.

- A · 2TP/(2TP+FP+FN)=6/9=2/3.
- B · Đây là precision.
- C · Đây là recall.

### ML15-mcq-8 · Đối chiếu

**Chọn B.** TP=0, FN=1 nên recall=0.

- A · Không tìm được mẫu dương nào.
- B · TP=0, FN=1 nên recall=0.
- C · Accuracy cao do mất cân bằng, chưa đáp ứng mục tiêu tìm dương.

### ML15-mcq-9 · Đối chiếu

**Chọn C.** Có thể báo không xác định hoặc quy ước zero_division rõ ràng.

- A · Không tự gán 1.
- B · Hai chỉ số có mẫu số khác nhau.
- C · Có thể báo không xác định hoặc quy ước zero_division rõ ràng.

### ML15-mcq-10 · Đối chiếu

**Chọn A.** Precision và recall chỉ dùng TP/FP hoặc TP/FN.

- A · Precision và recall chỉ dùng TP/FP hoặc TP/FN.
- B · TN không nằm trong hai mẫu số đó.
- C · Không có thay đổi TP, FP, FN.

### ML15-practice-1 · Đối chiếu

Mỗi loại có đúng một mẫu.

```python
y=[1,1,0,0];pred=[1,0,1,0]
print([sum(a==t and b==p for a,b in zip(y,pred)) for t,p in [(1,1),(0,1),(1,0),(0,0)]])
```
Kết quả [1, 1, 1, 1]

### ML15-practice-2 · Đối chiếu

(3+4)/(3+1+2+4)=0.7.

```python
tp,fp,fn,tn=3,1,2,4
print((tp+tn)/(tp+fp+fn+tn))
```
Kết quả 0.7

### ML15-practice-3 · Đối chiếu

Precision=3/4=0.75. Recall=3/5=0.6.

```python
tp,fp,fn=3,1,2
print(tp/(tp+fp))
print(tp/(tp+fn))
```
Kết quả 0.75
0.6

### ML15-practice-4 · Đối chiếu

F1=6/9≈0.666667.

```python
tp,fp,fn=3,1,2
print(f"{2*tp/(2*tp+fp+fn):.6f}")
```
Kết quả 0.666667

### ML15-practice-5 · Đối chiếu

[[TN, FP],[FN, TP]]=[[4,1],[2,3]]. Phải ghi quy ước trục.

```python
tn,fp,fn,tp=4,1,2,3
print([[tn,fp],[fn,tp]])
```
Kết quả [[4, 1], [2, 3]]

### ML15-practice-6 · Đối chiếu

TP=6, FN=4. Recall=6/10=0.6.

```python
print(6/10)
```
Kết quả 0.6

### ML15-practice-7 · Đối chiếu

TP=6, FP=2. Precision=6/8=0.75.

```python
print((8-2)/8)
```
Kết quả 0.75

### ML15-practice-8 · Đối chiếu

F1 là trung bình điều hòa 2PR/(P+R), không phải (P+R)/2. Cần giữ đúng định nghĩa. Hai cách khác nhau khi P khác R.

### ML15-practice-9 · Đối chiếu

Recall = TP/(TP+FN). Khi không có mẫu dương thực, mẫu số bằng 0. Phiếu này quy ước ghi 0 và vẫn báo số mẫu dương khi diễn giải.

### ML15-practice-10 · Đối chiếu

Mẫu số=5>0, tử số=0 nên F1=0 dù không có TP.

```python
tp,fp,fn=0,2,3
print(2*tp/(2*tp+fp+fn))
```
Kết quả 0.0

### ML15-practice-11 · Đối chiếu

Recall và số FN giúp theo dõi bỏ sót. Vẫn cần xem FP/precision và chi phí thực tế. Không kết luận tối ưu chỉ từ một chỉ số.

### ML15-practice-12 · Đối chiếu

Không nói chung. Counts dương/âm đổi vai trò. Phải nêu rõ lớp dương trước khi tính và diễn giải chỉ số.

## Ôn tập ML16 · Lời giải

### ML16-mcq-1 · Đối chiếu

**Chọn A.** Trục x=FPR=0, trục y=TPR=1.

- A · Trục x=FPR=0, trục y=TPR=1.
- B · TPR=1 nghĩa tìm đủ positive.
- C · Khi đó FPR thường bằng 1 nếu có negative.

### ML16-mcq-2 · Đối chiếu

**Chọn B.** AUC đo thứ hạng, không trực tiếp đo hiệu chuẩn.

- A · Có hai lớp cần để tính ROC nhưng không bảo đảm calibration.
- B · AUC đo thứ hạng, không trực tiếp đo hiệu chuẩn.
- C · Ranking và calibration là khác nhau.

### ML16-mcq-3 · Đối chiếu

**Chọn C.** Mỗi cặp thắng thành thua và ngược lại.

- A · Có thể vượt miền [0,1].
- B · Thứ tự bị đảo hoàn toàn, chưa chắc ngẫu nhiên.
- C · Mỗi cặp thắng thành thua và ngược lại.

### ML16-mcq-4 · Đối chiếu

**Chọn A.** ROC vẽ TPR theo FPR khi đổi ngưỡng.

- A · ROC vẽ TPR theo FPR khi đổi ngưỡng.
- B · Đó là một hệ trục khác, không phải ROC.
- C · ROC dùng tỷ lệ, không chỉ counts.

### ML16-mcq-5 · Đối chiếu

**Chọn B.** Mẫu số là toàn bộ mẫu âm thật.

- A · Đây là tỷ lệ sai trong dự đoán dương, không phải FPR.
- B · Mẫu số là toàn bộ mẫu âm thật.
- C · Đây là tỷ lệ bỏ sót dương.

### ML16-mcq-6 · Đối chiếu

**Chọn C.** Tập dự đoán dương mở rộng. Các count TP, FP không giảm.

- A · Ngưỡng thấp hơn không loại dự đoán dương cũ.
- B · Thêm dự đoán dương cũng có thể thêm FP.
- C · Tập dự đoán dương mở rộng. Các count TP, FP không giảm.

### ML16-mcq-7 · Đối chiếu

**Chọn A.** AUC tổng hợp sự phân tách theo thứ hạng qua các ngưỡng.

- A · AUC tổng hợp sự phân tách theo thứ hạng qua các ngưỡng.
- B · Đây không phải chỉ số tối ưu hóa theo số bước.
- C · Accuracy ở một ngưỡng khác AUC.

### ML16-mcq-8 · Đối chiếu

**Chọn B.** FP+TN=0 nên FPR không xác định.

- A · TPR còn phụ thuộc ngưỡng. Thiếu mẫu âm vẫn là vấn đề.
- B · FP+TN=0 nên FPR không xác định.
- C · Không tự gán AUC hoàn hảo.

### ML16-mcq-9 · Đối chiếu

**Chọn C.** Hai điểm hòa được tính nửa điểm theo quy ước đã nêu.

- A · Đó là đóng góp khi dương có điểm cao hơn âm.
- B · Đó là khi dương xếp thấp hơn âm.
- C · Hai điểm hòa được tính nửa điểm theo quy ước đã nêu.

### ML16-mcq-10 · Đối chiếu

**Chọn A.** Mọi cặp dương–âm nhận 0 điểm.

- A · Mọi cặp dương–âm nhận 0 điểm.
- B · Thứ tự hoàn toàn ngược.
- C · Không có cặp hòa hay thắng.

### ML16-practice-1 · Đối chiếu

TPR=8/10=0.8. FPR=3/10=0.3.

```python
tp,fn,fp,tn=8,2,3,7
print(tp/(tp+fn))
print(fp/(fp+tn))
```
Kết quả 0.8
0.3

### ML16-practice-2 · Đối chiếu

Dự đoán [1,1,0,0]. TP=1, FP=1, FN=1, TN=1 nên cả hai tỷ lệ 0.5.

```python
y=[1,0,1,0];score=[.9,.8,.4,.1];pred=[int(s>=.5) for s in score]
tp=sum(t==1 and p==1 for t,p in zip(y,pred));fp=sum(t==0 and p==1 for t,p in zip(y,pred))
print(pred)
print((tp/2,fp/2))
```
Kết quả [1, 1, 0, 0]
(0.5, 0.5)

### ML16-practice-3 · Đối chiếu

Dự đoán [1,1,1,0]. TPR=1, FPR=0.5.

```python
y=[1,0,1,0];score=[.9,.8,.4,.1];pred=[int(s>=.3) for s in score]
print(pred)
print((sum(t==1 and p==1 for t,p in zip(y,pred))/2,sum(t==0 and p==1 for t,p in zip(y,pred))/2))
```
Kết quả [1, 1, 1, 0]
(1.0, 0.5)

### ML16-practice-4 · Đối chiếu

Không mẫu nào dự đoán dương: FP=TP=0 nên (FPR, TPR)=(0,0).

### ML16-practice-5 · Đối chiếu

Mọi mẫu đều dự đoán dương nên (FPR, TPR)=(1,1).

### ML16-practice-6 · Đối chiếu

Bốn cặp: 0.9 thắng hai lần,0.4 thắng một lần. AUC=3/4=0.75.

```python
positive=[.9,.4];negative=[.8,.1]
credit=sum(1. if u>v else .5 if u==v else 0. for u in positive for v in negative)
print(credit/(len(positive)*len(negative)))
```
Kết quả 0.75

### ML16-practice-7 · Đối chiếu

Một cặp hòa, AUC=0.5.

```python
u,v=.5,.5
print(1. if u>v else .5 if u==v else 0.)
```
Kết quả 0.5

### ML16-practice-8 · Đối chiếu

AUC=1 vì mọi cặp dương–âm đều có điểm dương cao hơn. Điều này không tự quyết định ngưỡng vận hành.

### ML16-practice-9 · Đối chiếu

Không nếu phép cộng không tạo lỗi số học. Thứ tự và quan hệ hòa giữ nguyên. Ngưỡng số cụ thể có thể cần đổi tương ứng.

### ML16-practice-10 · Đối chiếu

Một ngưỡng vẫn có thể tạo quá nhiều FP hoặc FN. Cần chọn theo chi phí lỗi và dữ liệu tập xác thực, giữ tập kiểm tra độc lập.

### ML16-practice-11 · Đối chiếu

Báo không xác định hoặc lỗi đầu vào theo hợp đồng. Không gán 0.5 hay 1 rồi trình bày như đo được ROC hợp lệ.

### ML16-practice-12 · Đối chiếu

TPR=TP/(TP+FN), chính là recall/sensitivity của lớp dương theo cùng quy ước nhãn.

## Ôn tập ML17 · Lời giải

### ML17-mcq-1 · Đối chiếu

**Chọn A.** Không thể phản ánh nhiều dạng thay đổi theo đặc trưng.

- A · Không thể phản ánh nhiều dạng thay đổi theo đặc trưng.
- B · Không đúng nói chung.
- C · Không phải kết luận mặc định.

### ML17-mcq-2 · Đối chiếu

**Chọn B.** Lựa chọn cần theo tiêu chí đánh giá đã quy định.

- A · Không giải quyết chất lượng mô hình.
- B · Lựa chọn cần theo tiêu chí đánh giá đã quy định.
- C · Đó là suy luận sai từ khớp mô hình tập huấn luyện.

### ML17-mcq-3 · Đối chiếu

**Chọn C.** Cần kiểm dữ liệu ngoài giả thuyết độ phức tạp.

- A · Gap có nhiều nguyên nhân.
- B · Không liên quan kiểu biểu diễn nhãn.
- C · Cần kiểm dữ liệu ngoài giả thuyết độ phức tạp.

### ML17-mcq-4 · Đối chiếu

**Chọn A.** Có thể mô hình chưa đủ khả năng hoặc chưa được tối ưu tốt. Không chỉ dựa hai số để kết luận tuyệt đối.

- A · Có thể mô hình chưa đủ khả năng hoặc chưa được tối ưu tốt. Không chỉ dựa hai số để kết luận tuyệt đối.
- B · quá khớp thường có khoảng cách tập huấn luyện thấp, tập xác thực cao.
- C · Hai số này không chứng minh leakage.

### ML17-mcq-5 · Đối chiếu

**Chọn B.** Khoảng cách lớn cần xem độ phức tạp, quy trình và phân bố dữ liệu.

- A · Khớp tập huấn luyện không bảo đảm tổng quát hóa.
- B · Khoảng cách lớn cần xem độ phức tạp, quy trình và phân bố dữ liệu.
- C · Tập xác thực đang đưa tín hiệu vấn đề.

### ML17-mcq-6 · Đối chiếu

**Chọn C.** Đây là vai trò dữ liệu dùng lựa chọn mô hình.

- A · Tập kiểm tra sẽ tham gia lựa chọn, gây đánh giá lạc quan.
- B · Chỉ tập huấn luyện có thể ưu tiên mô hình quá phức tạp.
- C · Đây là vai trò dữ liệu dùng lựa chọn mô hình.

### ML17-mcq-7 · Đối chiếu

**Chọn A.** Đặc trưng nhiễu hoặc không phù hợp có thể làm tổng quát hóa kém.

- A · Đặc trưng nhiễu hoặc không phù hợp có thể làm tổng quát hóa kém.
- B · Nhiều cột không đồng nghĩa nhiều tín hiệu hữu ích.
- C · Tính chẵn lẻ không quyết định chất lượng.

### ML17-mcq-8 · Đối chiếu

**Chọn B.** Hệ số tự do mô hình trong phân tích lỗi không phải hệ số chặn của design ma trận.

- A · Tên hệ số tự do dùng trong hai ngữ cảnh khác nhau.
- B · Hệ số tự do mô hình trong phân tích lỗi không phải hệ số chặn của design ma trận.
- C · Phương sai không phải kích thước dữ liệu.

### ML17-mcq-9 · Đối chiếu

**Chọn C.** Cần xem biến thiên do cách chia và phạm vi dữ liệu.

- A · Một phép đo hữu hạn không bảo đảm mọi tương lai.
- B · Tập huấn luyện khớp tuyệt đối vẫn có thể quá khớp.
- C · Cần xem biến thiên do cách chia và phạm vi dữ liệu.

### ML17-mcq-10 · Đối chiếu

**Chọn A.** Phải kiểm đơn vị mẫu và cách chia để đánh giá dữ liệu mới.

- A · Phải kiểm đơn vị mẫu và cách chia để đánh giá dữ liệu mới.
- B · Sự trùng mẫu có thể làm đánh giá lạc quan.
- C · Không giải quyết độc lập dữ liệu.

### ML17-practice-1 · Đối chiếu

Ưu tiên B theo tiêu chí đã cho, dù tập huấn luyện MSE cao hơn. Chưa dùng tập kiểm tra để thay đổi lựa chọn.

### ML17-practice-2 · Đối chiếu

A có gap=7. B gap=1. Gap hỗ trợ chẩn đoán nhưng vẫn cần mức sai số tuyệt đối và ngữ cảnh.

```python
for train,val in [(1.,8.),(2.,3.)]:
    print(val-train)
```
Kết quả 7.0
1.0

### ML17-practice-3 · Đối chiếu

Chọn bậc 3. Không chọn bậc 8 chỉ vì linh hoạt hơn.

```python
degrees=[1,3,8];scores=[5.,2.,7.]
print(degrees[min(range(len(scores)),key=lambda i:scores[i])])
```
Kết quả 3

### ML17-practice-4 · Đối chiếu

Kiểm tối ưu đã hội tụ chưa, đặc trưng/nhãn/kích thước có đúng không. Sau đó xét mô hình có đủ khả năng biểu diễn quan hệ không. Dữ liệu hoặc mã sai cũng có thể tạo lỗi cao.

### ML17-practice-5 · Đối chiếu

Khi quyết định phụ thuộc tập kiểm tra thì tập kiểm tra trở thành dữ liệu lựa chọn. Cần tập xác thực/CV để chọn, giữ tập kiểm tra cho đánh giá cuối.

### ML17-practice-6 · Đối chiếu

Không. Có nguy cơ rò rỉ dữ liệu vì thông tin chưa tồn tại lúc dự đoán thực tế. Cần kiểm thời điểm và nguồn từng đặc trưng.

### ML17-practice-7 · Đối chiếu

Mô hình tận dụng thêm độ linh hoạt để khớp tập huấn luyện nhưng chưa có bằng chứng đặc trưng giúp tổng quát hóa. Cần cân nhắc bỏ hoặc đánh giá theo quy trình ổn định.

### ML17-practice-8 · Đối chiếu

Mục tiêu là dự đoán dữ liệu chưa dùng để học. Ghi nhớ tập huấn luyện có thể đạt 0 nhưng sai ngoài tập huấn luyện, đặc biệt khi mô hình quá phức tạp.

### ML17-practice-9 · Đối chiếu

Trung bình bằng 3, min=1, max=5. Các kết quả dao động nên không chỉ chọn lần tốt nhất để báo cáo.

```python
scores=[1.,5.,3.]
print(sum(scores)/len(scores))
print((min(scores),max(scores)))
```
Kết quả 3.0
(1.0, 5.0)

### ML17-practice-10 · Đối chiếu

Có thể thiếu khớp do không biểu diễn được sự thay đổi theo x. Cần đánh giá và kiểm dữ liệu. Không chỉ dùng tên mô hình để kết luận mọi bài toán.

### ML17-practice-11 · Đối chiếu

Nhiều tham số tăng khả năng khớp cả tín hiệu và nhiễu. Chất lượng cần được đo ngoài dữ liệu huấn luyện và cân nhắc độ phức tạp phù hợp.

### ML17-practice-12 · Đối chiếu

Không. Tập xác thực điểm đang ngang nhau theo tiêu chí cho trước. Có thể xét độ ổn định, độ phức tạp và chi phí theo quy trình. Không tự suy từ tập huấn luyện gap ra bảo đảm tuyệt đối.

## Ôn tập ML18 · Lời giải

### ML18-mcq-1 · Đối chiếu

**Chọn A.** Tổng w_j²=0.

- A · Tổng w_j²=0.
- B · Không có thành phần hệ số khác 0.
- C · Tổng bình phương xác định.

### ML18-mcq-2 · Đối chiếu

**Chọn B.** Shrinkage không đồng nghĩa tự động chọn đặc trưng bằng đặt 0.

- A · Hệ số tự do trong bài không bị phạt.
- B · Shrinkage không đồng nghĩa tự động chọn đặc trưng bằng đặt 0.
- C · L2 thường co hệ số, không tạo sparsity như quy tắc ngưỡng bắt buộc.

### ML18-mcq-3 · Đối chiếu

**Chọn C.** Cần công bố normalization để lambda có ý nghĩa nhất quán.

- A · Data term tổng phụ thuộc số mẫu.
- B · Không suy ra.
- C · Cần công bố normalization để lambda có ý nghĩa nhất quán.

### ML18-mcq-4 · Đối chiếu

**Chọn A.** Đạo hàm lambda*w²/2 là lambda*w theo quy ước đã nêu.

- A · Đạo hàm lambda*w²/2 là lambda*w theo quy ước đã nêu.
- B · Hệ số 1/2 đã triệt tiêu 2.
- C · Đạo hàm phụ thuộc giá trị w.

### ML18-mcq-5 · Đối chiếu

**Chọn B.** Penalty chỉ tổng trên các hệ số đặc trưng.

- A · Ngược quy ước đang dùng.
- B · Penalty chỉ tổng trên các hệ số đặc trưng.
- C · Quy ước bài loại hệ số tự do khỏi penalty.

### ML18-mcq-6 · Đối chiếu

**Chọn C.** Term L2 bằng 0.

- A · Không có penalty không buộc hệ số bằng 0.
- B · Tổn thất gốc vẫn xác định.
- C · Term L2 bằng 0.

### ML18-mcq-7 · Đối chiếu

**Chọn A.** Phạt mạnh có thể hạn chế mô hình quá mức.

- A · Phạt mạnh có thể hạn chế mô hình quá mức.
- B · Không có bảo đảm này.
- C · Lambda không sinh cột dữ liệu.

### ML18-mcq-8 · Đối chiếu

**Chọn B.** Cùng dự đoán có thể cần hệ số rất khác khi đổi đơn vị.

- A · Không có điều kiện đó.
- B · Cùng dự đoán có thể cần hệ số rất khác khi đổi đơn vị.
- C · Không tự động.

### ML18-mcq-9 · Đối chiếu

**Chọn C.** Giữ tập kiểm tra riêng cho đánh giá cuối.

- A · Làm tập kiểm tra tham gia lựa chọn.
- B · Không có cơ sở luôn tốt.
- C · Giữ tập kiểm tra riêng cho đánh giá cuối.

### ML18-practice-1 · Đối chiếu

0.2×25/2=2.5.

```python
import numpy as np
w=np.array([3.,4.]);print(float(.2*np.sum(w*w)/2))
```
Kết quả 2.5

### ML18-practice-2 · Đối chiếu

Lambda*w=[0.6,0.8].

```python
import numpy as np
print(np.round(.2*np.array([3.,4.]),4).tolist())
```
Kết quả [0.6, 0.8]

### ML18-practice-3 · Đối chiếu

4.0. Khi báo chỉ số dữ liệu cần phân biệt data tổn thất với tổn thất có penalty.

```python
print(1.5+2.5)
```
Kết quả 4.0

### ML18-practice-4 · Đối chiếu

[1.2,−0.7].

```python
import numpy as np
print((np.array([1.,-1.])+.1*np.array([2.,3.])).tolist())
```
Kết quả [1.2, -0.7]

### ML18-practice-5 · Đối chiếu

2−0.1×0.5×2=1.9.

```python
w=2.;print(w-.1*.5*w)
```
Kết quả 1.9

### ML18-practice-6 · Đối chiếu

Bằng 0 dù b lớn. Không tính b² vào tổng penalty.

### ML18-practice-7 · Đối chiếu

Không. L2 có thể đánh đổi khớp mô hình tập huấn luyện để cải thiện tập xác thực. Cần đo ngoài tập huấn luyện và nêu tổn thất nào đang báo.

### ML18-practice-8 · Đối chiếu

Lambda thay mục tiêu qua penalty. Alpha điều khiển bước tối ưu. Đổi alpha không tương đương đổi regularization.

### ML18-practice-9 · Đối chiếu

Lambda*w/m. Khác quy ước không chia m. Phải giữ công thức tổn thất và gradient khớp nhau.

### ML18-practice-10 · Đối chiếu

Cần thực hiện đúng hợp đồng bài: theta[0] là hệ số tự do phải loại khỏi penalty. Vị trí mảng không thay định nghĩa toán học.

### ML18-practice-11 · Đối chiếu

Không. Penalty mạnh hơn có thể hạn chế thêm khả năng khớp mô hình. Cần kiểm tra dữ liệu, tối ưu và độ phức tạp.

### ML18-practice-12 · Đối chiếu

Chọn 0.1. Chưa dùng tập kiểm tra để đổi lựa chọn.

```python
lam=[0,.1,1];score=[4,2,3]
print(lam[min(range(3),key=lambda i:score[i])])
```
Kết quả 0.1

## Ôn tập ML19 · Lời giải

### ML19-mcq-1 · Đối chiếu

**Chọn A.** Net=−1 nên step trả 0.

- A · Net=−1 nên step trả 0.
- B · Net luôn âm.
- C · w=0 loại mọi ảnh hưởng x.

### ML19-mcq-2 · Đối chiếu

**Chọn B.** Tổng trọng số bằng 0 rồi cộng −0.5.

- A · Sai dấu hệ số tự do.
- B · Tổng trọng số bằng 0 rồi cộng −0.5.
- C · Đã bỏ hệ số tự do.

### ML19-mcq-3 · Đối chiếu

**Chọn C.** Hai trọng số và một hệ số tự do.

- A · Thiếu hệ số tự do.
- B · Không có bốn tham số ở cấu hình này.
- C · Hai trọng số và một hệ số tự do.

### ML19-mcq-4 · Đối chiếu

**Chọn A.** Hệ số tự do cho phép biên không phải đi qua gốc.

- A · Hệ số tự do cho phép biên không phải đi qua gốc.
- B · Hệ số tự do không tạo mẫu.
- C · Không có bảo đảm đó.

### ML19-mcq-5 · Đối chiếu

**Chọn B.** Dấu bằng thuộc lớp 1.

- A · Điểm biên đã được quy định.
- B · Dấu bằng thuộc lớp 1.
- C · Sai với quy tắc >= đã cho.

### ML19-mcq-6 · Đối chiếu

**Chọn C.** Chỉ (1,1) có net dương.

- A · OR cần nhận cả (1,0).
- B · Một perceptron tuyến tính không tách XOR.
- C · Chỉ (1,1) có net dương.

### ML19-mcq-7 · Đối chiếu

**Chọn A.** XOR không phân tách tuyến tính trong hai đầu vào gốc.

- A · XOR không phân tách tuyến tính trong hai đầu vào gốc.
- B · Không có đường thẳng tách đúng bốn điểm XOR.
- C · Đổi tên không thay cấu trúc phân tách.

### ML19-mcq-8 · Đối chiếu

**Chọn B.** 2−3+2=1.

- A · Đã mất dấu trọng số thứ hai.
- B · 2−3+2=1.
- C · Đã bỏ hoặc sai hệ số tự do.

### ML19-mcq-9 · Đối chiếu

**Chọn C.** Cùng nhân dương giữ dấu và quy tắc biên.

- A · Dấu net giữ nguyên.
- B · Phép nhân không tạo mẫu.
- C · Cùng nhân dương giữ dấu và quy tắc biên.

### ML19-practice-1 · Đối chiếu

Net=1.

```python
import numpy as np
print(float(np.array([1.,-1.])@np.array([2.,3.])+2))
```
Kết quả 1.0

### ML19-practice-2 · Đối chiếu

Đầu ra theo (0,0),(0,1),(1,0),(1,1) là [0,0,0,1].

```python
inputs=[(0,0),(0,1),(1,0),(1,1)]
print([int(x+y-1.5>=0) for x,y in inputs])
```
Kết quả [0, 0, 0, 1]

### ML19-practice-3 · Đối chiếu

Đầu ra [0,1,1,1].

```python
inputs=[(0,0),(0,1),(1,0),(1,1)]
print([int(x+y-.5>=0) for x,y in inputs])
```
Kết quả [0, 1, 1, 1]

### ML19-practice-4 · Đối chiếu

[0,1,1].

```python
print([int(z>=0) for z in [-.1,0.,.1]])
```
Kết quả [0, 1, 1]

### ML19-practice-5 · Đối chiếu

Net=0 nên ra 1 theo >=0, không đúng bảng AND.

```python
print(int(0+0>=0))
```
Kết quả 1

### ML19-practice-6 · Đối chiếu

2x1−x2+1=0, hay x2=2x1+1.

### ML19-practice-7 · Đối chiếu

Net=0, thuộc lớp 1 nếu step>=0.

```python
z=2*1-3+1
print(z)
print(int(z>=0))
```
Kết quả 0
1

### ML19-practice-8 · Đối chiếu

Hai implementation dùng >0 và >=0 cho nhãn khác nhau tại biên. Tập kiểm tra cần khớp quy ước.

### ML19-practice-9 · Đối chiếu

Net là tổng có trọng số cộng hệ số tự do, có thể là số thực bất kỳ. Đầu ra step là nhãn theo ngưỡng.

### ML19-practice-10 · Đối chiếu

Báo lỗi kích thước. Không tự bỏ trọng số hay thêm thuộc tính giả.

### ML19-practice-11 · Đối chiếu

Phải có một bộ tham số và quy tắc dự đoán tạo đúng đầu ra. Hard-mã nhãn theo tập kiểm tra không chứng minh mô hình tuyến tính biểu diễn được XOR.

### ML19-practice-12 · Đối chiếu

Bộ mới [2,2], b=−3 vẫn cho [0,0,0,1].

```python
print([int(2*x+2*y-3>=0) for x,y in [(0,0),(0,1),(1,0),(1,1)]])
```
Kết quả [0, 0, 0, 1]

## Ôn tập ML20 · Lời giải

### ML20-mcq-1 · Đối chiếu

**Chọn A.** Đạo hàm tanh là 1−t².

- A · Đạo hàm tanh là 1−t².
- B · 1−0²=1.
- C · Đó là sigmoid derivative tại đầu ra 0.5.

### ML20-mcq-2 · Đối chiếu

**Chọn B.** max(0,−3)=0.

- A · ReLU không phải trị tuyệt đối.
- B · max(0,−3)=0.
- C · Phần âm bị chặn thành 0.

### ML20-mcq-3 · Đối chiếu

**Chọn C.** Giới hạn khi z tiến +vô cực là 1.

- A · Đó là phía z rất âm.
- B · Sigmoid bị chặn trên.
- C · Giới hạn khi z tiến +vô cực là 1.

### ML20-mcq-4 · Đối chiếu

**Chọn A.** ReLU bằng 0 khi z âm và bằng z khi z dương.

- A · ReLU bằng 0 khi z âm và bằng z khi z dương.
- B · Sai nửa trục giữ lại.
- C · Đó là sigmoid.

### ML20-mcq-5 · Đối chiếu

**Chọn B.** Tanh đối xứng lẻ qua gốc.

- A · Tanh(0) không bão hòa dương.
- B · Tanh đối xứng lẻ qua gốc.
- C · Đó là sigmoid(0).

### ML20-mcq-6 · Đối chiếu

**Chọn C.** Áp dụng đạo hàm sigmoid.

- A · Đó là đạo hàm tanh theo đầu ra.
- B · Thiếu thành phần 1−s.
- C · Áp dụng đạo hàm sigmoid.

### ML20-mcq-7 · Đối chiếu

**Chọn A.** Cần nêu quy ước dùng khi triển khai tại điểm gãy.

- A · Cần nêu quy ước dùng khi triển khai tại điểm gãy.
- B · Hai đạo hàm một phía khác nhau.
- C · Không có quy tắc bắt buộc đó.

### ML20-mcq-8 · Đối chiếu

**Chọn B.** Phép hợp các affine có thể rút gọn thành một affine.

- A · Không liên quan.
- B · Phép hợp các affine có thể rút gọn thành một affine.
- C · Ghép affine vẫn affine.

### ML20-mcq-9 · Đối chiếu

**Chọn C.** Tích nhiều đạo hàm nhỏ có thể làm gradient giảm mạnh.

- A · s(1−s) không lớn hơn 0.25.
- B · Activation không sửa mọi đầu vào không hợp lệ.
- C · Tích nhiều đạo hàm nhỏ có thể làm gradient giảm mạnh.

### ML20-practice-1 · Đối chiếu

[0,0,3].

```python
import numpy as np
print(np.maximum(0,np.array([-2.,0.,3.])).tolist())
```
Kết quả [0.0, 0.0, 3.0]

### ML20-practice-2 · Đối chiếu

Lần lượt 0.5,0,0.

```python
import numpy as np
print(float(1/(1+np.exp(0.))))
print(float(np.tanh(0.)))
print(float(np.maximum(0,0.)))
```
Kết quả 0.5
0.0
0.0

### ML20-practice-3 · Đối chiếu

s(1−s)=0.25.

```python
s=.5
print(s*(1-s))
```
Kết quả 0.25

### ML20-practice-4 · Đối chiếu

1−t²=0.64.

```python
t=.6
print(round(1-t*t,4))
```
Kết quả 0.64

### ML20-practice-5 · Đối chiếu

[0,0,1].

```python
import numpy as np
z=np.array([-2.,0.,3.])
print((z>0).astype(int).tolist())
```
Kết quả [0, 0, 1]

### ML20-practice-6 · Đối chiếu

0.25 và 0.0099. Đầu ra gần bão hòa có đạo hàm nhỏ hơn.

```python
for s in [.5,.99]:
    print(round(s*(1-s),4))
```
Kết quả 0.25
0.0099

### ML20-practice-7 · Đối chiếu

Đầu ra có thể lớn hơn 1. ReLU không tự chuẩn hóa thành xác suất.

### ML20-practice-8 · Đối chiếu

Sigmoid trong (0,1), tanh trong (−1,1). Số học máy có thể làm tròn tới biên.

### ML20-practice-9 · Đối chiếu

o=6x−1 vẫn affine.

```python
x=2.
h=2*x+1
print(3*h-4)
print(6*x-1)
```
Kết quả 11.0
11.0

### ML20-practice-10 · Đối chiếu

10⁻5. Đây là minh họa nhân nhiều hệ số nhỏ, chưa phải đo gradient của một mạng cụ thể.

```python
print(f"{.1**5:.5f}")
```
Kết quả 0.00001

### ML20-practice-11 · Đối chiếu

Lựa chọn phụ thuộc vai trò tầng và bài toán. Đầu ra nhị phân cần diễn giải xác suất có thể dùng sigmoid, ReLU có điểm gãy và vùng gradient 0.

### ML20-practice-12 · Đối chiếu

Bằng 0 trong vùng âm. Nó có thể không nhận cập nhật từ đường truyền này. Không coi đây là mọi neuron của mạng đều ngừng học.

## Ôn tập ML21 · Lời giải

### ML21-mcq-1 · Đối chiếu

**Chọn A.** Ma trận 4×2 chứa tám phần tử.

- A · Ma trận 4×2 chứa tám phần tử.
- B · Đó là tổng d+h, không phải số liên kết đầy đủ.
- C · Đó là số neuron đầu ra tầng.

### ML21-mcq-2 · Đối chiếu

**Chọn B.** Cùng đầu vào và cùng phép biến đổi xác định cho cùng đầu ra.

- A · Không có quy tắc bỏ hàng.
- B · Cùng đầu vào và cùng phép biến đổi xác định cho cùng đầu ra.
- C · Affine/activation này không dựa chỉ số hàng.

### ML21-mcq-3 · Đối chiếu

**Chọn C.** Quy tắc ngưỡng áp dụng đầu ra xác suất.

- A · W1 không phải xác suất dự đoán của mẫu.
- B · Không phải điểm của mẫu.
- C · Quy tắc ngưỡng áp dụng đầu ra xác suất.

### ML21-mcq-4 · Đối chiếu

**Chọn A.** Mỗi mẫu tạo h net đầu vào tầng ẩn.

- A · Mỗi mẫu tạo h net đầu vào tầng ẩn.
- B · Không khớp phép nhân.
- C · Sai số hàng.

### ML21-mcq-5 · Đối chiếu

**Chọn B.** Broadcasting đúng theo trục mẫu là chủ ý của hợp đồng này.

- A · Hệ số tự do áp dụng cho mọi mẫu.
- B · Broadcasting đúng theo trục mẫu là chủ ý của hợp đồng này.
- C · Kiến trúc h cố định.

### ML21-mcq-6 · Đối chiếu

**Chọn C.** Từng hàng mẫu cho một đầu ra.

- A · Đã đảo trục.
- B · Đó là kích thước W2.
- C · Từng hàng mẫu cho một đầu ra.

### ML21-mcq-7 · Đối chiếu

**Chọn A.** Nếu bỏ mọi phi tuyến, các affine rút gọn thành một affine.

- A · Nếu bỏ mọi phi tuyến, các affine rút gọn thành một affine.
- B · Không được đổi nhãn.
- C · Không có bảo đảm này.

### ML21-mcq-8 · Đối chiếu

**Chọn B.** Forward tách khỏi backward và update.

- A · Không đúng định nghĩa pha forward.
- B · Forward tách khỏi backward và update.
- C · Đó thuộc bước tính gradient/tối ưu.

### ML21-mcq-9 · Đối chiếu

**Chọn C.** Đầu ra width tầng trước phải bằng đầu vào width tầng sau.

- A · Số chiều bên trong phải bằng nhau.
- B · Nhãn không sửa kích thước trọng số.
- C · Đầu ra width tầng trước phải bằng đầu vào width tầng sau.

### ML21-practice-1 · Đối chiếu

W1=(2,3), b1=(3,), W2=(3,1), b2=(1,).

### ML21-practice-2 · Đối chiếu

z1=[[-1,3]].

```python
import numpy as np
X=np.array([[1.,2.]]);W=np.eye(2);b=np.array([-2.,1.])
print((X@W+b).tolist())
```
Kết quả [[-1.0, 3.0]]

### ML21-practice-3 · Đối chiếu

h=[[0,3]].

```python
import numpy as np
print(np.maximum(0,np.array([[-1.,3.]])).tolist())
```
Kết quả [[0.0, 3.0]]

### ML21-practice-4 · Đối chiếu

z2=[[2]].

```python
import numpy as np
h=np.array([[0.,3.]])
print((h@np.array([[2.],[1.]])+np.array([-1.])).tolist())
```
Kết quả [[2.0]]

### ML21-practice-5 · Đối chiếu

Xấp xỉ 0.8808.

```python
import numpy as np
print(round(float(1/(1+np.exp(-2.))),4))
```
Kết quả 0.8808

### ML21-practice-6 · Đối chiếu

Kết quả [[1,1],[4,3]].

```python
import numpy as np
X=np.array([[0.,2.],[3.,4.]])
print((X@np.eye(2)+np.array([1.,-1.])).tolist())
```
Kết quả [[1.0, 1.0], [4.0, 3.0]]

### ML21-practice-7 · Đối chiếu

Đạo hàm activation có thể cần z hoặc đầu ra activation. Lưu cache giúp tính backward đúng theo cùng forward.

### ML21-practice-8 · Đối chiếu

Không. Vectơ 1D có thể làm mất trục lô trong kết quả. Cần quy định rõ API nhận lô 2D hay một mẫu 1D.

### ML21-practice-9 · Đối chiếu

Với các affine và activation độc lập theo hàng, đầu ra hoán vị theo cùng thứ tự mẫu. Không tự hoán vị nhãn riêng.

### ML21-practice-10 · Đối chiếu

W1 có6, b1 có3, W2 có3, b2 có1, tổng13.

```python
d,h,o=2,3,1
print(d*h+h+h*o+o)
```
Kết quả 13

### ML21-practice-11 · Đối chiếu

Không. Hợp affine vẫn affine nên không tạo khả năng biểu diễn XOR trong không gian đầu vào gốc bằng một ngưỡng tuyến tính.

### ML21-practice-12 · Đối chiếu

Đối chiếu quy ước hàng/cột và số đầu vào/đầu ra neuron. Transpose tùy tiện có thể chạy nhưng đổi ý nghĩa kiến trúc.

## Ôn tập ML22 · Lời giải

### ML22-mcq-1 · Đối chiếu

**Chọn A.** W_new=W−0×g=W. API có thể từ chối alpha=0 nếu hợp đồng đòi dương.

- A · W_new=W−0×g=W. API có thể từ chối alpha=0 nếu hợp đồng đòi dương.
- B · Nhân gradient với 0 chứ không nhân tham số với 0.
- C · Không có phép đổi dấu đó.

### ML22-mcq-2 · Đối chiếu

**Chọn B.** Nhân gradient truyền về với đạo hàm activation.

- A · Không cộng hai đạo hàm.
- B · Nhân gradient truyền về với đạo hàm activation.
- C · Quy tắc chuỗi nhân, không chia.

### ML22-mcq-3 · Đối chiếu

**Chọn C.** Đạo hàm bằng 0 nếu tổn thất không phụ thuộc trọng số đó.

- A · Không có đóng góp thay đổi tổn thất.
- B · Không có quy tắc này.
- C · Đạo hàm bằng 0 nếu tổn thất không phụ thuộc trọng số đó.

### ML22-mcq-4 · Đối chiếu

**Chọn A.** Nhân với chuyển vị trọng số đưa gradient về h neuron ẩn.

- A · Nhân với chuyển vị trọng số đưa gradient về h neuron ẩn.
- B · Thường sai phép nhân hoặc quy ước lô.
- C · Chưa truyền qua ánh xạ đầu ra.

### ML22-mcq-5 · Đối chiếu

**Chọn B.** Tính toàn bộ gradient trước khi update tham số.

- A · Không còn đạo hàm mạng đã chạy.
- B · Tính toàn bộ gradient trước khi update tham số.
- C · Làm gradient không còn thuộc cùng điểm tham số.

### ML22-mcq-6 · Đối chiếu

**Chọn C.** Tổng đóng góp các mẫu rồi chia n theo quy ước trung bình.

- A · Không cho vectơ hệ số tự do đúng chiều.
- B · Hệ số tự do vẫn ảnh hưởng đầu ra.
- C · Tổng đóng góp các mẫu rồi chia n theo quy ước trung bình.

### ML22-mcq-7 · Đối chiếu

**Chọn A.** Đạo hàm cần nhân theo quy tắc chuỗi.

- A · Đạo hàm cần nhân theo quy tắc chuỗi.
- B · Thiếu thừa số s.
- C · Không phải đạo hàm sigmoid.

### ML22-mcq-8 · Đối chiếu

**Chọn B.** Cập nhật từng trọng số cần gradient tương ứng.

- A · Đó là kích thước theo lô, không phải tham số.
- B · Cập nhật từng trọng số cần gradient tương ứng.
- C · Theo quy ước W1 này, gradient phải cùng kích thước W1.

### ML22-mcq-9 · Đối chiếu

**Chọn C.** Phải theo dõi normalization nằm ở đâu, chỉ áp dụng đúng một lần.

- A · Làm gradient nhỏ sai hệ số n.
- B · Cả hai gradient phải cùng quy ước.
- C · Phải theo dõi normalization nằm ở đâu, chỉ áp dụng đúng một lần.

### ML22-practice-1 · Đối chiếu

Gradient W2=[[-1],[-1]].

```python
import numpy as np
H=np.array([[1.,2.],[3.,4.]]);delta=np.array([[1.],[-1.]])
print((H.T@delta/2).tolist())
```
Kết quả [[-1.0], [-1.0]]

### ML22-practice-2 · Đối chiếu

[2,4].

```python
import numpy as np
print(np.array([[1.,3.],[3.,5.]]).mean(axis=0).tolist())
```
Kết quả [2.0, 4.0]

### ML22-practice-3 · Đối chiếu

2×0.5×0.5=0.5.

```python
s=.5;upstream=2.
print(upstream*s*(1-s))
```
Kết quả 0.5

### ML22-practice-4 · Đối chiếu

[[2,−6]].

```python
import numpy as np
print((np.array([[2.]])@np.array([[1.],[-3.]]).T).tolist())
```
Kết quả [[2.0, -6.0]]

### ML22-practice-5 · Đối chiếu

[0.5,−1.5].

```python
import numpy as np
s=np.array([.5,.5]);g=np.array([2.,-6.])
print((g*s*(1-s)).tolist())
```
Kết quả [0.5, -1.5]

### ML22-practice-6 · Đối chiếu

[[0.5,−1.5],[1,−3]].

```python
import numpy as np
print((np.array([[1.,2.]]).T@np.array([[.5,-1.5]])).tolist())
```
Kết quả [[0.5, -1.5], [1.0, -3.0]]

### ML22-practice-7 · Đối chiếu

Gradient W1 phải thuộc cùng mạng và tham số đã dùng forward. Dùng W2 mới làm trộn hai điểm tham số.

### ML22-practice-8 · Đối chiếu

Gradient sum không chia n. Cả tổn thất, delta và gradient phải nhất quán để tránh nhân/chia n sai.

### ML22-practice-9 · Đối chiếu

Cache chứa đầu vào/net/activation của lượt forward. Y xác định sai số theo tổn thất. Không thay activation bằng nhãn khi nhân đạo hàm.

### ML22-practice-10 · Đối chiếu

W_new=2.3.

```python
print(2.-.1*(-3.))
```
Kết quả 2.3

### ML22-practice-11 · Đối chiếu

Bằng 0 ở điểm đó do nhân đạo hàm activation. Không được bỏ thừa số activation chỉ vì gradient truyền về khác 0.

### ML22-practice-12 · Đối chiếu

Delta thường nhân đạo hàm từng neuron cùng vị trí. @ trộn/tổng theo chiều ma trận, có thể sai kích thước hoặc nghĩa dù đôi lúc chạy được.

## Ôn tập ML23 · Lời giải

### ML23-mcq-1 · Đối chiếu

**Chọn A.** Trung bình một vectơ là chính vectơ đó.

- A · Trung bình một vectơ là chính vectơ đó.
- B · Không có bước trừ mẫu để về 0.
- C · Không đổi thứ tự đặc trưng.

### ML23-mcq-2 · Đối chiếu

**Chọn B.** Hoán vị tên không đổi phân hoạch hay khoảng cách.

- A · Không cần cân bằng.
- B · Hoán vị tên không đổi phân hoạch hay khoảng cách.
- C · SSE dùng khoảng cách tới tâm tương ứng.

### ML23-mcq-3 · Đối chiếu

**Chọn C.** Kiểm dtype, công thức và dữ liệu trước khi báo kết quả.

- A · Tổng bình phương không âm.
- B · Sai định nghĩa.
- C · Kiểm dtype, công thức và dữ liệu trước khi báo kết quả.

### ML23-mcq-4 · Đối chiếu

**Chọn A.** Giữ tâm cụm hiện tại và so khoảng cách.

- A · Giữ tâm cụm hiện tại và so khoảng cách.
- B · K-Means không cần nhãn thật để khớp mô hình.
- C · Không phải assignment chuẩn.

### ML23-mcq-5 · Đối chiếu

**Chọn B.** Trung bình tối thiểu tổng khoảng cách bình phương trong cụm cố định.

- A · Không dùng nhãn thật.
- B · Trung bình tối thiểu tổng khoảng cách bình phương trong cụm cố định.
- C · Không tối thiểu SSE nói chung.

### ML23-mcq-6 · Đối chiếu

**Chọn C.** SSE đo độ phân tán quanh tâm cụm.

- A · Đó không phải SSE mục tiêu này.
- B · Clustering không có nhãn dự đoán đúng/sai như classifier.
- C · SSE đo độ phân tán quanh tâm cụm.

### ML23-mcq-7 · Đối chiếu

**Chọn A.** Có thể giữ tâm cũ hoặc khởi tạo lại theo quy tắc cụ thể.

- A · Có thể giữ tâm cũ hoặc khởi tạo lại theo quy tắc cụ thể.
- B · NaN không phải tâm cụm hợp lệ.
- C · Không liên quan và thay dữ liệu.

### ML23-mcq-8 · Đối chiếu

**Chọn B.** Kết quả có thể phụ thuộc khởi tạo và cực tiểu địa phương.

- A · Số chiều hai không bảo đảm.
- B · Kết quả có thể phụ thuộc khởi tạo và cực tiểu địa phương.
- C · Thư viện không thay bảo đảm thuật toán.

### ML23-mcq-9 · Đối chiếu

**Chọn C.** K-Means dùng khoảng cách giữa các vector.

- A · chuẩn hóa không đổi số mẫu.
- B · chuẩn hóa không cung cấp nhãn.
- C · K-Means dùng khoảng cách giữa các vector.

### ML23-practice-1 · Đối chiếu

Tâm 0 vì khoảng cách 3<7.

```python
centers=[0.,10.];x=3.
print(min(range(2),key=lambda j:abs(x-centers[j])))
```
Kết quả 0

### ML23-practice-2 · Đối chiếu

Trung bình bằng 3.

```python
print(sum([1.,3.,5.])/3)
```
Kết quả 3.0

### ML23-practice-3 · Đối chiếu

[1,3].

```python
import numpy as np
print(np.array([[0.,2.],[2.,4.]]).mean(axis=0).tolist())
```
Kết quả [1.0, 3.0]

### ML23-practice-4 · Đối chiếu

4+0+4=8.

```python
import numpy as np
x=np.array([1.,3.,5.]);print(float(np.sum((x-3)**2)))
```
Kết quả 8.0

### ML23-practice-5 · Đối chiếu

Hai cụm [0,2],[8,10]. Tâm mới [1,9].

```python
import numpy as np
x=np.array([0.,2.,8.,10.]);c=np.array([0.,10.])
labels=np.argmin((x[:,None]-c[None,:])**2,axis=1)
print(labels.tolist())
print([float(x[labels==i].mean()) for i in range(2)])
```
Kết quả [0, 0, 1, 1]
[1.0, 9.0]

### ML23-practice-6 · Đối chiếu

SSE trước=8, sau=4.

```python
import numpy as np
x=np.array([0.,2.,8.,10.])
for c in [[0.,10.],[1.,9.]]:
    d=(x[:,None]-np.array(c)[None,:])**2
    print(float(d.min(axis=1).sum()))
```
Kết quả 8.0
4.0

### ML23-practice-7 · Đối chiếu

Nhãn cụm là mã gán, chỉ số không mang tọa độ. Tâm cụm phải lấy trung bình vectơ đặc trưng của các mẫu được gán.

### ML23-practice-8 · Đối chiếu

Cách phá hòa, chẳng hạn chọn chỉ số tâm nhỏ hơn. Quy tắc giúp tái lập và kiểm thử assignment.

### ML23-practice-9 · Đối chiếu

Giới hạn số vòng và độ dịch tâm dưới tolerance. Cũng có thể kiểm nhãn không đổi. Phải nêu tolerance và xử lý cụm rỗng. Dừng không chứng minh cực tiểu toàn cục.

### ML23-practice-10 · Đối chiếu

Khởi tạo ảnh hưởng kết quả. Giữ dữ liệu/hạt giống ngẫu nhiên giúp tách ảnh hưởng thuật toán khỏi thay đổi thí nghiệm.

### ML23-practice-11 · Đối chiếu

Tâm=2, SSE=8.

```python
import numpy as np
x=np.array([0.,2.,4.]);c=x.mean()
print(float(c))
print(float(np.sum((x-c)**2)))
```
Kết quả 2.0
8.0

### ML23-practice-12 · Đối chiếu

Không. SSE chỉ phản ánh mục tiêu khoảng cách trên dữ liệu/thang đo đã chọn. Cần diễn giải cụm và đánh giá phù hợp.

## Ôn tập ML24 · Lời giải

### ML24-mcq-1 · Đối chiếu

**Chọn A.** Đồng thuận gồm cả cùng-cùng và khác-khác.

- A · Đồng thuận gồm cả cùng-cùng và khác-khác.
- B · Rand có phần d mà Jaccard cùng cụm loại bỏ.
- C · Tên cụm không quan trọng.

### ML24-mcq-2 · Đối chiếu

**Chọn B.** Chỉ một cặp (0,1).

- A · Có cặp giữa hai mẫu khác nhau.
- B · Chỉ một cặp (0,1).
- C · Đã đếm cả hai hướng.

### ML24-mcq-3 · Đối chiếu

**Chọn C.** Quan hệ của cặp (0,1) và (1,2) đã đổi.

- A · Số cụm bằng nhau không đủ.
- B · Số mẫu bằng nhau không đủ.
- C · Quan hệ của cặp (0,1) và (1,2) đã đổi.

### ML24-mcq-4 · Đối chiếu

**Chọn A.** External so cấu trúc phân cụm với nhãn tham chiếu.

- A · External so cấu trúc phân cụm với nhãn tham chiếu.
- B · Màu hiển thị không phải nhãn tham chiếu.
- C · Chỉ số phân cụm khác accuracy classifier.

### ML24-mcq-5 · Đối chiếu

**Chọn B.** Xét cùng/khác cụm ở hai phân hoạch.

- A · Không đo sự đồng thuận phân cụm.
- B · Xét cùng/khác cụm ở hai phân hoạch.
- C · Không phải định nghĩa pair counting.

### ML24-mcq-6 · Đối chiếu

**Chọn C.** n(n−1)/2=6.

- A · 12 đếm cả hai hướng.
- B · Đó là số mẫu.
- C · n(n−1)/2=6.

### ML24-mcq-7 · Đối chiếu

**Chọn A.** Quan hệ cùng/khác cụm của mọi cặp vẫn giữ nguyên.

- A · Quan hệ cùng/khác cụm của mọi cặp vẫn giữ nguyên.
- B · Tên cụm chỉ là mã.
- C · Lập luận không phụ thuộc số cụm.

### ML24-mcq-8 · Đối chiếu

**Chọn B.** Jaccard cùng cụm dùng a/(a+b+c), không tính d.

- A · Bất đồng vẫn thuộc hợp.
- B · Jaccard cùng cụm dùng a/(a+b+c), không tính d.
- C · Đó là phần giao cần giữ.

### ML24-mcq-9 · Đối chiếu

**Chọn C.** Không báo phép chia 0 như chỉ số thực đo.

- A · Không tự suy ra từ mẫu số 0.
- B · Không đúng định nghĩa.
- C · Không báo phép chia 0 như chỉ số thực đo.

### ML24-practice-1 · Đối chiếu

5×4/2=10.

```python
n=5
print(n*(n-1)//2)
```
Kết quả 10

### ML24-practice-2 · Đối chiếu

Có, cặp (0,1) cùng cụm. Hai cặp còn lại khác cụm trong cả hai.

### ML24-practice-3 · Đối chiếu

(0,1) bất đồng,(0,2) đồng thuận khác cụm,(1,2) bất đồng. Rand=1/3.

### ML24-practice-4 · Đối chiếu

Một trong ba cặp đồng thuận.

```python
from itertools import combinations
t=[0,0,1];p=[0,1,1];pairs=list(combinations(range(3),2))
print(f"{sum((t[i]==t[j])==(p[i]==p[j]) for i,j in pairs)/len(pairs):.6f}")
```
Kết quả 0.333333

### ML24-practice-5 · Đối chiếu

(a+d)/(a+b+c+d)=4/6.

```python
a,b,c,d=2,1,1,2
print(f"{(a+d)/(a+b+c+d):.6f}")
```
Kết quả 0.666667

### ML24-practice-6 · Đối chiếu

A/(a+b+c)=2/4=0.5.

```python
a,b,c=2,1,1
print(a/(a+b+c))
```
Kết quả 0.5

### ML24-practice-7 · Đối chiếu

Mã cụm có thể hoán vị tùy ý mà vẫn cùng phân hoạch. So tên số đánh đồng vấn đề nhận dạng tên với cấu trúc nhóm.

### ML24-practice-8 · Đối chiếu

Không. External so với nhãn tham chiếu. Độ gọn/khoảng cách nội tại là khía cạnh khác.

### ML24-practice-9 · Đối chiếu

Không theo nghĩa internal. Dùng dữ liệu và cấu trúc cụm. Cần nêu chỉ số cụ thể, không tự tạo nhãn chuẩn từ chính đầu ra rồi coi external điểm cao là bằng chứng.

### ML24-practice-10 · Đối chiếu

Không có cặp nào nằm trong hợp nên công thức trực tiếp cho 0/0. Theo quy ước của phiếu, hai phân hoạch đều tách riêng mọi mẫu nên Jaccard bằng 1.

### ML24-practice-11 · Đối chiếu

Không. Hai mảng phải tham chiếu cùng tập mẫu theo cùng thứ tự. Lọc cần áp dụng đồng bộ và ghi phạm vi đánh giá.

### ML24-practice-12 · Đối chiếu

Là bất đồng:không vào tử Rand. Vào mẫu số Jaccard nhưng không vào tử. Đây là cặp bị tách so với tham chiếu.

## Ôn tập ML25 · Lời giải

### ML25-mcq-1 · Đối chiếu

**Chọn A.** Phép chiếu trên cơ sở trực chuẩn đầy đủ giữ mọi tọa độ.

- A · Phép chiếu trên cơ sở trực chuẩn đầy đủ giữ mọi tọa độ.
- B · Không giảm chiều khi giữ đủ cơ sở.
- C · Không cần trường hợp đó.

### ML25-mcq-2 · Đối chiếu

**Chọn B.** Phương sai phép chiếu bằng trị riêng tương ứng.

- A · Chỉ một hướng không đủ kết luận mọi cột hằng.
- B · Phương sai phép chiếu bằng trị riêng tương ứng.
- C · Không phải tâm cụm.

### ML25-mcq-3 · Đối chiếu

**Chọn C.** PCA tối đa phương sai X, không tối ưu trực tiếp tổn thất dự đoán y.

- A · PCA là phép biến đổi không giám sát này.
- B · Kiểu số không thay thuật toán.
- C · PCA tối đa phương sai X, không tối ưu trực tiếp tổn thất dự đoán y.

### ML25-mcq-4 · Đối chiếu

**Chọn A.** Tâm hóa mỗi đặc trưng trước khi tính hiệp phương sai.

- A · Tâm hóa mỗi đặc trưng trước khi tính hiệp phương sai.
- B · Đó không phải tâm hóa đặc trưng đang dùng.
- C · PCA không cần nhãn này.

### ML25-mcq-5 · Đối chiếu

**Chọn B.** Trị riêng biểu diễn phương sai theo hướng tương ứng.

- A · Hiệp phương sai lý tưởng là PSD.
- B · Trị riêng biểu diễn phương sai theo hướng tương ứng.
- C · Giữ phương sai ít nhất.

### ML25-mcq-6 · Đối chiếu

**Chọn C.** Xc@V_k giữ n mẫu và k tọa độ mới.

- A · Sai thứ tự trục.
- B · Sai số hàng.
- C · Xc@V_k giữ n mẫu và k tọa độ mới.

### ML25-mcq-7 · Đối chiếu

**Chọn A.** Tổng lambda_i/sum(lambda)=1.

- A · Tổng lambda_i/sum(lambda)=1.
- B · Tỷ lệ được chuẩn hóa bởi tổng eigenvalue.
- C · Không nếu tổng phương sai dương.

### ML25-mcq-8 · Đối chiếu

**Chọn B.** Tọa độ phép chiếu đổi dấu tương ứng nhưng cùng hướng trục.

- A · Không phụ thuộc điều kiện đó.
- B · Tọa độ phép chiếu đổi dấu tương ứng nhưng cùng hướng trục.
- C · Đổi dấu vectơ không đổi eigenvalue.

### ML25-mcq-9 · Đối chiếu

**Chọn C.** Giữ cùng trung bình và các vectơ hướng tập huấn luyện.

- A · Đổi tâm khác hệ tọa độ đã học.
- B · PCA này không dùng nhãn tập kiểm tra.
- C · Giữ cùng trung bình và các vectơ hướng tập huấn luyện.

### ML25-practice-1 · Đối chiếu

Trung bình bằng [2,3], Xc=[[-1,−1],[1,1]].

```python
import numpy as np
X=np.array([[1.,2.],[3.,4.]])
print(X.mean(axis=0).tolist())
print((X-X.mean(axis=0)).tolist())
```
Kết quả [2.0, 3.0]
[[-1.0, -1.0], [1.0, 1.0]]

### ML25-practice-2 · Đối chiếu

[0.8,0.2].

```python
import numpy as np
v=np.array([4.,1.]);print((v/v.sum()).tolist())
```
Kết quả [0.8, 0.2]

### ML25-practice-3 · Đối chiếu

Hai thành phần vì (6+3)/10=0.9.

```python
import numpy as np
v=np.array([6.,3.,1.]);c=np.cumsum(v)/v.sum()
print(int(np.searchsorted(c,.9)+1))
```
Kết quả 2

### ML25-practice-4 · Đối chiếu

[[1],[3]], kích thước (2,1).

```python
import numpy as np
print((np.array([[1.,2.],[3.,4.]])@np.array([[1.],[0.]])).tolist())
```
Kết quả [[1.0], [3.0]]

### ML25-practice-5 · Đối chiếu

Hàm dành cho ma trận Hermitian/đối xứng, trả hệ trị riêng/vectơ riêng phù hợp cấu trúc. Vẫn cần sắp thứ tự theo mục tiêu PCA.

### ML25-practice-6 · Đối chiếu

Đã chọn hướng phương sai nhỏ nhất. Cần sắp giảm dần và hoán vị cột vectơ riêng tương ứng.

### ML25-practice-7 · Đối chiếu

Mọi trị riêng cùng bằng 0, nên công thức tỷ lệ cho 0/0. Hàm của phiếu trả 0 cho từng thành phần được giữ.

### ML25-practice-8 · Đối chiếu

Có, zvᵀ=(-z)(−v)ᵀ. Không ép vectơ riêng cùng dấu với một đầu ra mẫu rồi báo sai toán học.

### ML25-practice-9 · Đối chiếu

Ban đầu 40, sau 20, không tính trung bình và các vectơ hướng cần lưu.

```python
n,d,k=10,4,2
print(n*d)
print(n*k)
```
Kết quả 40
20

### ML25-practice-10 · Đối chiếu

Không. Các hướng và trung bình có thể khác nhau. Mô hình cần cùng phép biến đổi đã khớp mô hình trên tập huấn luyện.

### ML25-practice-11 · Đối chiếu

Không. thang đo ảnh hưởng hiệp phương sai và hướng PCA. Quy trình chuẩn hóa trước PCA phải nêu rõ và học từ tập huấn luyện.

### ML25-practice-12 · Đối chiếu

Không. Có thể có nhiều cơ sở trực chuẩn trong cùng không gian con. Kiểm không gian/phương sai hoặc tái tạo phù hợp hơn so vectơ từng phần tử.

## Ôn tập ML26 · Lời giải

### ML26-mcq-1 · Đối chiếu

**Chọn A.** Nút thuần lớp.

- A · Nút thuần lớp.
- B · Đó là hai lớp cân bằng.
- C · Count không phải impurity.

### ML26-mcq-2 · Đối chiếu

**Chọn B.** Mọi entropy/gain nhân cùng hệ số dương.

- A · Có thể, đơn vị khác.
- B · Mọi entropy/gain nhân cùng hệ số dương.
- C · Đổi cơ số chỉ nhân hằng số dương.

### ML26-mcq-3 · Đối chiếu

**Chọn C.** Tổng có trọng số của hai số 0 bằng 0.

- A · Mỗi nhánh impurity 0.
- B · Không phụ thuộc mã tên.
- C · Tổng có trọng số của hai số 0 bằng 0.

### ML26-mcq-4 · Đối chiếu

**Chọn A.** Gini bằng 0 ở nút thuần lớp.

- A · Gini bằng 0 ở nút thuần lớp.
- B · Tổng tỷ lệ bằng 1, không đo impurity.
- C · Thiếu trọng số p và không phải Gini.

### ML26-mcq-5 · Đối chiếu

**Chọn B.** Thay p0=p1=0.5.

- A · Hai lớp cân bằng cho 1−0.25−0.25.
- B · Thay p0=p1=0.5.
- C · Chỉ nút thuần lớp có Gini 0.

### ML26-mcq-6 · Đối chiếu

**Chọn C.** Mỗi nhánh đóng góp theo tỷ lệ mẫu.

- A · Sai khi nhánh khác cỡ.
- B · Bỏ ảnh hưởng nhánh nhỏ.
- C · Mỗi nhánh đóng góp theo tỷ lệ mẫu.

### ML26-mcq-7 · Đối chiếu

**Chọn A.** Cùng định nghĩa entropy và cơ số log.

- A · Cùng định nghĩa entropy và cơ số log.
- B · Đảo dấu.
- C · Không đo giảm impurity.

### ML26-mcq-8 · Đối chiếu

**Chọn B.** Quy tắc điểm chia phải có ca biên rõ.

- A · Bịa dữ liệu nhánh.
- B · Quy tắc điểm chia phải có ca biên rõ.
- C · Không phải đánh giá hợp lệ.

### ML26-mcq-9 · Đối chiếu

**Chọn C.** Có thể ghi nhớ các nhóm rất nhỏ/nhiễu.

- A · Không có bảo đảm.
- B · Khác mô hình.
- C · Có thể ghi nhớ các nhóm rất nhỏ/nhiễu.

### ML26-practice-1 · Đối chiếu

Cả hai bằng 0. Hạng 0 log0 lấy giới hạn bằng 0.

### ML26-practice-2 · Đối chiếu

0.5.

```python
p=[.5,.5]
print(1-sum(x*x for x in p))
```
Kết quả 0.5

### ML26-practice-3 · Đối chiếu

1−0.5625−0.0625=0.375.

```python
p=[.75,.25]
print(1-sum(x*x for x in p))
```
Kết quả 0.375

### ML26-practice-4 · Đối chiếu

Gini có trọng số là (6×0 + 2×0,5)/8 = 0,125. Nhánh phải có một mẫu của mỗi lớp nên Gini ở đó bằng 0,5.

### ML26-practice-5 · Đối chiếu

0.375.

```python
print(.5-.125)
```
Kết quả 0.375

### ML26-practice-6 · Đối chiếu

1 bit.

```python
import math
print(-sum(p*math.log2(p) for p in [.5,.5]))
```
Kết quả 1.0

### ML26-practice-7 · Đối chiếu

Chọn A vì impurity con thấp hơn, cùng impurity cha nên gain cao hơn.

### ML26-practice-8 · Đối chiếu

Trái [0,1], phải [2,3].

```python
x=[1,2,3,4]
print([i for i,v in enumerate(x) if v<=2.5])
print([i for i,v in enumerate(x) if v>2.5])
```
Kết quả [0, 1]
[2, 3]

### ML26-practice-9 · Đối chiếu

Gini dùng bình phương tỷ lệ lớp. Hoán vị các tỷ lệ không đổi tổng.

### ML26-practice-10 · Đối chiếu

Bằng 0 vì weighted impurity con bằng impurity cha.

### ML26-practice-11 · Đối chiếu

Ngưỡng là phần mô hình đã học. Tập kiểm tra phải giữ ngoài fitting và lựa chọn để đánh giá độc lập.

### ML26-practice-12 · Đối chiếu

Tỷ lệ [0.25,0.75], Gini=0.375.

```python
c=[1,3];p=[x/sum(c) for x in c]
print(p)
print(1-sum(x*x for x in p))
```
Kết quả [0.25, 0.75]
0.375

## Ôn tập ML27 · Lời giải

### ML27-mcq-1 · Đối chiếu

**Chọn A.** N lượt lấy có hoàn lại không bảo đảm phủ đủ n mẫu gốc.

- A · N lượt lấy có hoàn lại không bảo đảm phủ đủ n mẫu gốc.
- B · Có hoàn lại tạo mẫu lặp và mẫu vắng.
- C · Hạt giống ngẫu nhiên không ngăn vắng mẫu.

### ML27-mcq-2 · Đối chiếu

**Chọn B.** (1+1+7)/3=3.

- A · Đó là giá trị lớn nhất.
- B · (1+1+7)/3=3.
- C · Đó là median, không phải trung bình.

### ML27-mcq-3 · Đối chiếu

**Chọn B.** Sinh chỉ số bootstrap, lấy phiếu của từng cây và gộp kết quả là các phép thao tác trên mảng.

- A · Các bước lấy mẫu và bỏ phiếu đều có thể viết riêng.
- B · Sinh chỉ số bootstrap, lấy phiếu của từng cây và gộp kết quả là các phép thao tác trên mảng.
- C · Phân loại thường dùng biểu quyết. Trung bình phù hợp với các dự đoán hồi quy.

### ML27-mcq-4 · Đối chiếu

**Chọn A.** Mỗi lần chọn có thể chọn lại một mẫu.

- A · Mỗi lần chọn có thể chọn lại một mẫu.
- B · Bootstrap cho phép lặp.
- C · Không được dùng tập kiểm tra để khớp mô hình.

### ML27-mcq-5 · Đối chiếu

**Chọn B.** Trung bình giảm biến thiên khi các sai số không hoàn toàn tương quan.

- A · Không phải phép gộp bagging thông thường.
- B · Trung bình giảm biến thiên khi các sai số không hoàn toàn tương quan.
- C · Không dùng tập kiểm tra label.

### ML27-mcq-6 · Đối chiếu

**Chọn C.** Đặc trưng subsampling giúp giảm tương quan giữa cây.

- A · Không phải cơ chế đúng.
- B · Làm các cây giống nhau.
- C · Đặc trưng subsampling giúp giảm tương quan giữa cây.

### ML27-mcq-7 · Đối chiếu

**Chọn A.** Đa dạng và mức tương quan ảnh hưởng lợi ích tổ hợp mô hình.

- A · Đa dạng và mức tương quan ảnh hưởng lợi ích tổ hợp mô hình.
- B · Lỗi chung giữ lại qua trung bình.
- C · Nếu dự đoán giống hệt thì trung bình vẫn thế.

### ML27-mcq-8 · Đối chiếu

**Chọn B.** Lượt chọn khác số mẫu duy nhất.

- A · Hạt giống ngẫu nhiên không loại trùng.
- B · Lượt chọn khác số mẫu duy nhất.
- C · Có hoàn lại cho phép trùng.

### ML27-mcq-9 · Đối chiếu

**Chọn C.** Lớp 1 chiếm đa số.

- A · Lớp 1 có hai phiếu.
- B · Cần phân biệt điểm tổng hợp và nhãn biểu quyết.
- C · Lớp 1 chiếm đa số.

### ML27-practice-1 · Đối chiếu

4.

```python
print(sum([2.,4.,6.])/3)
```
Kết quả 4.0

### ML27-practice-2 · Đối chiếu

Trung bình bằng [2,4].

```python
import numpy as np
print(np.array([[1.,3.],[3.,5.]]).mean(axis=0).tolist())
```
Kết quả [2.0, 4.0]

### ML27-practice-3 · Đối chiếu

[20,20,40,10]. 3 mẫu duy nhất.

```python
X=[10,20,30,40];idx=[1,1,3,0]
print([X[i] for i in idx])
print(len(set(idx)))
```
Kết quả [20, 20, 40, 10]
3

### ML27-practice-4 · Đối chiếu

Chỉ số 2.

```python
idx=[1,1,3,0]
print(sorted(set(range(4))-set(idx)))
```
Kết quả [2]

### ML27-practice-5 · Đối chiếu

Giữ đúng cặp mẫu–nhãn. Resample riêng hai mảng sẽ làm mô hình học nhãn sai.

### ML27-practice-6 · Đối chiếu

Vẫn 5. Tăng số mô hình giống hệt không thay đầu ra.

```python
print(sum([5.]*100)/100)
```
Kết quả 5.0

### ML27-practice-7 · Đối chiếu

1.

```python
labels=[0,1,1]
print(max(set(labels),key=labels.count))
```
Kết quả 1

### ML27-practice-8 · Đối chiếu

Làm sai mục tiêu học. Đa dạng bagging đến từ sampling và giới hạn đặc trưng theo thuật toán, không bịa nhãn.

### ML27-practice-9 · Đối chiếu

Không theo Random Forest thường dùng. Tập ứng viên có thể được lấy lại ở mỗi điểm chia. Phải đọc cấu hình và thuật toán cụ thể.

### ML27-practice-10 · Đối chiếu

Dữ liệu/thứ tự mẫu, hạt giống ngẫu nhiên, số mô hình, cách resample, đặc trưng sampling và quy tắc tổng hợp/phá hòa.

### ML27-practice-11 · Đối chiếu

Không. Vừa dùng tập kiểm tra để lựa chọn, vừa thay phép gộp tổ hợp mô hình bằng chọn mô hình. Không đúng quy trình đã định.

## Ôn tập ML28 · Lời giải

### ML28-mcq-1 · Đối chiếu

**Chọn A.** Dự đoán và MAE/RMSE dùng cùng đơn vị với y.

- A · Ghi đơn vị trong mô tả dữ liệu và khi diễn giải chỉ số.
- B · Đơn vị của y phụ thuộc dữ liệu và ảnh hưởng cách đọc kết quả.
- C · Hạt giống ngẫu nhiên không thay metadata đơn vị.

### ML28-mcq-2 · Đối chiếu

**Chọn B.** Expected là oracle phải có căn cứ, không lấy actual làm chuẩn tự động.

- A · Số lượng không thay bằng chứng.
- B · Expected là oracle phải có căn cứ, không lấy actual làm chuẩn tự động.
- C · Mã chạy vẫn có thể sai.

### ML28-mcq-3 · Đối chiếu

**Chọn C.** Không biến mô phỏng thành bằng chứng thực nghiệm ngoài phạm vi.

- A · Suy rộng cần dữ liệu đánh giá đại diện cho miền quan tâm.
- B · Hạt giống ngẫu nhiên khác có thể đổi dữ liệu và kết quả.
- C · Không biến mô phỏng thành bằng chứng thực nghiệm ngoài phạm vi.

### ML28-mcq-4 · Đối chiếu

**Chọn A.** Giữ tập kiểm tra để đánh giá sau cùng.

- A · Giữ tập kiểm tra để đánh giá sau cùng.
- B · Gây rò rỉ dữ liệu trong đánh giá.
- C · Không học tiền xử lý từ tập kiểm tra.

### ML28-mcq-5 · Đối chiếu

**Chọn B.** Không biến mô phỏng thành kết quả thực nghiệm thực tế.

- A · Cản tái lập và dễ gây hiểu nhầm.
- B · Không biến mô phỏng thành kết quả thực nghiệm thực tế.
- C · Không có bằng chứng dữ liệu thực.

### ML28-mcq-6 · Đối chiếu

**Chọn C.** Ngưỡng/quy tắc tạo nhãn phải minh bạch và không tối ưu bằng tập kiểm tra.

- A · Làm chỉ số bị lựa chọn theo kết quả.
- B · Không có định nghĩa nhãn thực phù hợp.
- C · Ngưỡng/quy tắc tạo nhãn phải minh bạch và không tối ưu bằng tập kiểm tra.

### ML28-mcq-7 · Đối chiếu

**Chọn A.** Cả preprocessing và mô hình khớp mô hình theo tập huấn luyện fold.

- A · Cả preprocessing và mô hình khớp mô hình theo tập huấn luyện fold.
- B · Mô hình đã thấy tập xác thực.
- C · Không tạo đánh giá độc lập.

### ML28-mcq-8 · Đối chiếu

**Chọn B.** Ghi chính xác nguồn dự đoán và nhãn.

- A · Hội tụ không thay tập đánh giá.
- B · Ghi chính xác nguồn dự đoán và nhãn.
- C · Tên tập không phụ thuộc kết quả.

### ML28-mcq-9 · Đối chiếu

**Chọn C.** Cần cả hai lớp để ROC thông thường xác định đầy đủ.

- A · Thiếu lớp không chứng minh ranking hoàn hảo.
- B · Sai phạm vi đánh giá.
- C · Cần cả hai lớp để ROC thông thường xác định đầy đủ.

### ML28-practice-1 · Đối chiếu

Chia tập huấn luyện/tập kiểm tra trước. khớp mô hình bộ chuẩn hóa trên tập huấn luyện. Biến đổi hai tập bằng bộ chuẩn hóa tập huấn luyện. khớp mô hình mô hình trên tập huấn luyện. Đánh giá tập kiểm tra riêng.

### ML28-practice-2 · Đối chiếu

Từ chối kích thước không khớp và tìm lỗi ghép dữ liệu. Không cắt bỏ mẫu tùy tiện để qua tập kiểm tra.

### ML28-practice-3 · Đối chiếu

Chỉ tập huấn luyện của điểm chia/phần. Áp dụng cùng giá trị đã học cho tập xác thực/tập kiểm tra. Cần nêu quy tắc cho cột tập huấn luyện toàn NaN.

### ML28-practice-4 · Đối chiếu

[0,1,1]. Quy tắc y ≥ 3 đưa trường hợp đúng bằng ngưỡng vào lớp 1.

```python
y=[2.,3.,4.]
print([int(v>=3.) for v in y])
```
Kết quả [0, 1, 1]

### ML28-practice-5 · Đối chiếu

Phần dư [1,−1], MAE=1, MSE=1.

```python
import numpy as np
y=np.array([2.,4.]);pred=np.array([3.,3.]);e=pred-y
print(float(np.abs(e).mean()))
print(float((e*e).mean()))
```
Kết quả 1.0
1.0

### ML28-practice-6 · Đối chiếu

Mỗi count bằng 1. Precision=recall=F1=0.5.

```python
y=[1,0,1];pred=[1,1,0]
print([sum(t==a and p==b for t,p in zip(y,pred)) for a,b in [(1,1),(0,1),(1,0)]])
```
Kết quả [1, 1, 1]

### ML28-practice-7 · Đối chiếu

Không. Báo counts và áp dụng quy tắc mẫu số rõ ràng. Không biến giới hạn dữ liệu thành thành tích tốt.

### ML28-practice-8 · Đối chiếu

3.0, cùng đơn vị với y.

```python
print(round(sum([2.8,3.,3.2])/3,6))
```
Kết quả 3.0

### ML28-practice-9 · Đối chiếu

Số mẫu nhỏ khiến chỉ số nhạy với cách chia. Cần thêm dữ liệu độc lập và phù hợp với tập dữ liệu mà mô hình sẽ gặp.

### ML28-practice-10 · Đối chiếu

Mã sinh dữ liệu/hạt giống ngẫu nhiên, schema/đơn vị, quy tắc nhãn, các chỉ số điểm chia, tham số bộ chuẩn hóa/mô hình, quy tắc chỉ số và kết quả thật.

### ML28-practice-11 · Đối chiếu

Không. Tập kiểm tra đã tham gia lựa chọn. Phải ghi rõ giới hạn và cần dữ liệu đánh giá độc lập mới nếu muốn kết luận tổng quát hóa.

<a id="doi-chieu"></a>

# Đối chiếu tài liệu USTH

Bản đối chiếu sau ghi nhận phạm vi của nguồn trước lần biên tập này.

# Đối chiếu giáo trình Machine Learning PE với Drive

## Kết luận

**Commit `dd6cfd7` khớp bộ giáo trình 603 câu trên Drive. Phạm vi slide USTH rộng hơn bộ 28 bài.** Bản đồ 28 hàng trong CSV khớp mã, tên bài, module và danh sách khái niệm của `source/course.json`. Tệp `ML_603_lessons_final.json` trên Drive trùng từng byte với `reference/studio-lessons.json` trong commit. SHA-256 của cả hai là `6448f5b248903ef0d8ff3e61bc2e589a5940083d62b90d6084d6463742fb9784`. [Commit gốc](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/commit/dd6cfd7652f0f5ba39179cdc9293a7016dc2bf99) · [JSON 603 câu](https://drive.google.com/file/d/1Fj2sOc134m_uvpMIhvTJcT8Qmzm2mFWe/view) · [CSV 28 bài](https://drive.google.com/file/d/1_UP5P5Mbu81srvNQYy1L8O3L3BS4Ce8_/view) · [Thư mục Drive](https://drive.google.com/drive/folders/1fwg-IDH1LrU0ekEIzx9e873vrnZH8Yhc)

**Phần thực hành của commit thiếu triển khai ở 20 bài.** Từ ML09 đến ML28, `referenceSolution` của bài S4 chỉ chuyển đầu vào thành mảng, kiểm tra rỗng rồi trả lại mảng nguyên. Ví dụ, ML09 chưa tính sigmoid, ML23 chưa gán hoặc cập nhật centroid và ML28 chưa fit mô hình hay đánh giá. Ví dụ Run của ba bài ML06–ML08 chỉ in một câu, còn 20 bài ML09–ML28 chỉ in shape (1, 2). Bản PRIMM có mã thực hiện mục tiêu từng bài và ca kiểm kết quả số, kích thước hoặc điều kiện biên. [Dữ liệu bài gốc](../../source/practice.json) · [PRIMM ML09](../../bai-hoc/ML09.md) · [PRIMM ML23](../../bai-hoc/ML23.md) · [PRIMM ML28](../../bai-hoc/ML28.md)

## Đối chiếu ML01–ML28 theo nội dung

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

## Kiến thức bổ sung theo slide

| Phần có trong Drive | Bài luyện bổ sung |
|---|---|
| Biểu diễn danh mục, dữ liệu thiếu và rời rạc hóa. [Data Preparation, slide 3–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) | [MLP01](../../bai-hoc/MLP01.md) |
| Chọn đặc trưng bằng filter, wrapper, embedded. [Feature Selection, slide 13–31](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) | [MLP02](../../bai-hoc/MLP02.md) |
| Phân cụm tích tụ và linkage. [Clustering, tr. 12–22](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP03](../../bai-hoc/MLP03.md) |
| DBSCAN và core/border/noise. [Clustering, tr. 23–26](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP04](../../bai-hoc/MLP04.md) |
| SVM, margin, soft margin và kernel. [Classification, tr. 30–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) | [MLP05](../../bai-hoc/MLP05.md) |
| SVD và dựng lại ma trận. [Statistics and PCA, tr. 36–38](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) | [MLP06](../../bai-hoc/MLP06.md) |
| Self-Organizing Map. [Clustering, tr. 35–43](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP07](../../bai-hoc/MLP07.md) |
| Davies–Bouldin và NMI. [Clustering, tr. 44–52](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP08](../../bai-hoc/MLP08.md) |

## Các điểm cần giữ rõ khi dạy

- **Quy ước và cách diễn giải.** Hiệp phương sai bằng 0 chưa đủ kết luận hai biến độc lập. Dùng đúng mẫu số cho phương sai mẫu/tổng thể, ghi hệ số 1/2 trong loss ML04 và quy ước λ trong Ridge. Với R², dự đoán tệ hơn mốc dự đoán bằng mean có thể cho R² âm. [Statistics and PCA, tr. 9–16](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) · [Model Evaluation, tr. 8](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view)
- **Lựa chọn mô hình và độ tổng quát.** Chọn siêu tham số và tập đặc trưng bằng validation hoặc CV. Slide wrapper gọi tập chấm trong vòng chọn là “test”; vai trò của nó là validation. Tập test cuối cần độc lập. Random Forest vẫn có thể overfit, đặc biệt khi dữ liệu hoặc quy trình đánh giá có vấn đề. [Feature Selection, slide 22–24](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) · [Ensemble Models, tr. 28](https://drive.google.com/file/d/13RwLiEQo8sAYKu-cjVoyz9986Z4zWAQt/view)
- **Phạm vi bổ sung.** Hai slide nhập môn có tổng quan ngành, phân biệt học có/không/bán giám sát và quy trình khai phá dữ liệu. Trong Drive còn có biến đổi dữ liệu ảnh/văn bản, ví dụ kernel dual đầy đủ và chi tiết thuật toán SOM. Gói thực hành mới tập trung vào phép tính lõi và các điểm thiếu lớn được nêu ở bảng trên. [Introduction, tr. 10–22](https://drive.google.com/file/d/1BK1s7InGNzpFWBHOx-2snV_U8-skGBl4/view) · [Data Mining Introduction, slide 16–26](https://docs.google.com/presentation/d/1J0TSOBcRdXKbvNK3AY45H-mYmDUv43eD/edit) · [Data Preparation, slide 10–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) · [Classification, tr. 40–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view)

## Bằng chứng kiểm tra

- Kiểm cấu trúc nguồn của commit đạt đủ 28 mã, 6 module, 603 câu và 168 test gốc. Chạy lại 181 đoạn lời giải có mã của ngân hàng câu hỏi và 168 ca S4 bằng CPython. Tất cả khớp kết quả gốc, kể cả các ca S4 chỉ thử hành vi kiểm đầu vào. Bảng đối chiếu rà khái niệm và các vấn đề thực hành chính. Từng đáp án lý thuyết trong 603 câu chưa được thẩm định riêng.
- Bản PRIMM có 36 bài. Chạy 36 mã mẫu và 151 ca Make 1 trên lời giải tham khảo. Kiểm thêm một số ca Modify và Make 2, gồm pipeline phân loại ML28 và so sánh kernel SVM. 603 câu ôn giữ mã và đáp án lựa chọn. Các câu có ngữ cảnh lĩnh vực được biên tập sang dữ liệu vô danh. Make 2 dùng ca kiểm ghi trong đề để người học tự đối chiếu.
- Hai tệp `4.ModelEvaluation.pdf` và `4. ModelEvaluation.pdf` có cùng SHA-256. Hai bản Regularization và hai bản Neural Network có số trang khác nhau; đã dùng các phần tương ứng theo số trang mỗi tệp.
