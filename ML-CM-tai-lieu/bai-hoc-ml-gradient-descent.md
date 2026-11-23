# Hồi quy tuyến tính đơn biến và Bước cập nhật Gradient Descent [NGOÀI NGUỒN]

## S1 Ngữ cảnh
Một nhóm nghiên cứu cần dự đoán giá thuê nhà dựa trên diện tích sử dụng. Với mô hình hồi quy tuyến tính đơn biến $y_{pred} = w \cdot x + b$, việc tìm trọng số $w$ và hệ số chệch $b$ tối ưu được bắt đầu bằng việc tính hàm mất mát sai số toàn phương trung bình (Mean Squared Error - MSE) từ các tham số khởi tạo ban đầu [NGOÀI NGUỒN].

```python
import numpy as np

# Tập dữ liệu mẫu: x (diện tích), y (giá thuê)
x = np.array([1.0, 2.0])
y = np.array([2.0, 4.0])

# Khởi tạo trọng số w = 0.0, hệ số chệch b = 0.0
w, b = 0.0, 0.0
y_pred = w * x + b
error = y_pred - y
loss = np.mean(error ** 2)
```

### Dự đoán
Giá trị của biến `loss` (hàm mất mát MSE) sau khi thực thi đoạn mã trên là bao nhiêu?
- [ ] A. 0.0 — Mô hình chưa qua huấn luyện nên chưa phát sinh sai số
- [x] B. 10.0 — Bình phương sai số gồm (-2.0)^2 = 4.0 và (-4.0)^2 = 16.0, trung bình là (4.0 + 16.0) / 2 = 10.0
- [ ] C. 20.0 — Tổng bình phương sai số 4.0 + 16.0 = 20.0 chưa chia trung bình cho số lượng mẫu N = 2
- [ ] D. -3.0 — Lấy trung bình cộng sai số tuyến tính (-2.0 + -4.0) / 2 thay vì bình phương

### Giải thích
1. **Dòng 5–6**: Mảng `x` và `y` chứa 2 điểm dữ liệu thực nghiệm: (1.0, 2.0) và (2.0, 4.0).
2. **Dòng 9–10**: Với `w = 0.0` và `b = 0.0`, dự đoán `y_pred = 0.0 * x + 0.0` trả về mảng `[0.0, 0.0]`.
3. **Dòng 11**: Hiệu số sai số `error = y_pred - y` có giá trị là `[0.0 - 2.0, 0.0 - 4.0] = [-2.0, -4.0]`.
4. **Dòng 12**: Bình phương sai số `error ** 2` tạo ra mảng `[4.0, 16.0]`, hàm `np.mean` tính trung bình cộng `(4.0 + 16.0) / 2 = 10.0`.

### Ngộ nhận
**"Hàm mất mát MSE có thể nhận giá trị âm nếu giá trị mô hình dự đoán nhỏ hơn thực tế."**
Bình phương của mọi số thực luôn không âm $((y_{pred} - y)^2 \ge 0)$, do đó trung bình cộng MSE luôn luôn lớn hơn hoặc bằng 0; dấu âm của hiệu số bị triệt tiêu khi lũy thừa bậc hai [NGOÀI NGUỒN].

## S2 Trắc nghiệm
Trong giải thuật Gradient Descent với hàm mất mát MSE, quy tắc cập nhật đúng cho trọng số $w$ với tốc độ học $\alpha$ (learning rate) là gì?
- [ ] A. $w = w + \alpha \cdot \frac{\partial L}{\partial w}$ — Sai dấu vì cập nhật cùng chiều gradient sẽ làm tăng hàm mất mát (Gradient Ascent)
- [x] B. $w = w - \alpha \cdot \frac{\partial L}{\partial w}$ — Đi ngược chiều đạo hàm giúp di chuyển dần về phía cực tiểu của hàm mất mát [NGOÀI NGUỒN]
- [ ] C. $w = \alpha \cdot \frac{\partial L}{\partial w} - w$ — Đảo lộn vị trí giữa tham số hiện tại và độ dốc gradient
- [ ] D. $w = w - \frac{\alpha}{\frac{\partial L}{\partial w}}$ — Đặt gradient dưới mẫu số gây nguy cơ chia cho 0 khi đạo hàm tiệm cận 0

### Phân loại
Phân loại các biến số và thành phần trong bài toán tối ưu Hồi quy tuyến tính:
- params | Tham số mô hình | Cần tối ưu | Các giá trị được giải thuật cập nhật tự động sau mỗi bước lặp :: `w (trọng số góc)`, `b (hệ số chệch)`
- hyperparams | Siêu tham số | Thiết lập trước | Các hằng số điều khiển do người lập trình ấn định trước khi huấn luyện :: `learning_rate (tốc độ học)`, `epochs (số vòng lặp)`

### Tự giải thích
Tại sao trong công thức cập nhật Gradient Descent bắt buộc phải nhân đạo hàm riêng (gradient) với tốc độ học (learning rate)?
- điều chỉnh bước nhảy :: độ lớn bước nhảy, phân kỳ, dao động, bước nhảy quá nhỏ
- định hướng hội tụ :: điểm cực tiểu, giảm hàm mất mát, ổn định nghiệm

## S3 Lắp ghép
Hoàn thành hàm `compute_gradients` tính đạo hàm riêng của MSE theo `w` và `b` cho bài toán hồi quy tuyến tính đơn biến $y_{pred} = w \cdot x + b$. Công thức đạo hàm giải tích: $\frac{\partial L}{\partial w} = \frac{2}{N} \sum (y_{pred} - y) x$ và $\frac{\partial L}{\partial b} = \frac{2}{N} \sum (y_{pred} - y)$ [NGOÀI NGUỒN].

```python
def compute_gradients(x, y, w, b):
    N = len(x)
    y_pred = w * x + b
    error = y_pred - y
    {{slot1}}
    {{slot2}}
    return dw, db
```

- slot1 = `dw = (2 / N) * np.sum(error * x)`
- slot2 = `db = (2 / N) * np.sum(error)`
- bank1 = `dw = np.sum(error * x) / N` (Bẫy quên hệ số 2 khi tính đạo hàm của hàm bậc hai u^2)

### Dự đoán kết quả
Với $x = [1.0, 2.0]$, $y = [2.0, 4.0]$, $w = 0.0$, $b = 0.0$, hàm trả về `(dw, db)` là cặp giá trị nào? [(-5.0, -3.0) | *(-10.0, -6.0) | (10.0, 6.0)]

## S4 Bài tập
Viết hàm `linear_regression_step(x, y, w, b, lr)` thực hiện MỘT bước cập nhật Gradient Descent cho hồi quy tuyến tính đơn biến.

- Đầu vào:
  - `x`: danh sách hoặc mảng 1D chứa các giá trị đặc trưng.
  - `y`: danh sách hoặc mảng 1D chứa các giá trị mục tiêu.
  - `w`: float, trọng số hiện tại.
  - `b`: float, hệ số chệch hiện tại.
  - `lr`: float, tốc độ học (learning rate).
- Yêu cầu xử lý:
  - Kiểm tra ca biên: nếu `len(x) == 0` hoặc `len(y) == 0` hoặc `len(x) != len(y)`, hàm trả về `None`.
  - Chuyển `x` và `y` sang mảng NumPy kiểu `float`.
  - Tính dự đoán: `y_pred = w * x + b`
  - Tính hàm mất mát: $MSE = \frac{1}{N} \sum (y_{pred} - y)^2$
  - Tính gradient: $dw = \frac{2}{N} \sum (y_{pred} - y) x$ và $db = \frac{2}{N} \sum (y_{pred} - y)$
  - Cập nhật tham số mới: $w_{new} = w - lr \cdot dw$ và $b_{new} = b - lr \cdot db$
  - Trả về dictionary với các giá trị được làm tròn 4 chữ số thập phân (`round(float(...), 4)`) theo định dạng:
    `{"loss": ..., "dw": ..., "db": ..., "w_new": ..., "b_new": ...}`

### Code khởi tạo
```python
import numpy as np

def linear_regression_step(x, y, w, b, lr):
    pass
```

### Lời giải
```python
import numpy as np

def linear_regression_step(x, y, w, b, lr):
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        return None
    x_arr = np.array(x, dtype=float)
    y_arr = np.array(y, dtype=float)
    N = len(x_arr)
    
    y_pred = w * x_arr + b
    error = y_pred - y_arr
    
    loss = np.mean(error ** 2)
    dw = (2.0 / N) * np.sum(error * x_arr)
    db = (2.0 / N) * np.sum(error)
    
    w_new = w - lr * dw
    b_new = b - lr * db
    
    return {
        "loss": round(float(loss), 4),
        "dw": round(float(dw), 4),
        "db": round(float(db), 4),
        "w_new": round(float(w_new), 4),
        "b_new": round(float(b_new), 4)
    }
```

### Gợi ý
- Nguyên lý :: Sử dụng công thức sai số toàn phương trung bình MSE để đo độ lệch và đạo hàm riêng tương ứng để xác định hướng giảm dốc nhanh nhất của tham số w và b.
- Cấu trúc :: Kiểm tra điều kiện danh sách rỗng hoặc lệch kích thước trước tiên trả về None; sau đó ép kiểu sang np.array để tính toán vector hóa y_pred, error, loss, dw, db và cập nhật w_new, b_new.
- Lời giải mẫu :: Dùng `np.mean(error ** 2)` để tính loss, `(2.0 / N) * np.sum(error * x_arr)` cho dw, `(2.0 / N) * np.sum(error)` cho db, và nhớ bọc `round(float(...), 4)` cho từng trường của dictionary trả về.

### Test
| call | expect | name |
|------|--------|------|
| `linear_regression_step([1.0, 2.0], [2.0, 4.0], 0.0, 0.0, 0.1)` | `{"loss": 10.0, "dw": -10.0, "db": -6.0, "w_new": 1.0, "b_new": 0.6}` | Ca cơ bản 2 điểm dữ liệu |
| `linear_regression_step([1.0, 2.0], [2.0, 4.0], 2.0, 0.0, 0.1)` | `{"loss": 0.0, "dw": 0.0, "db": 0.0, "w_new": 2.0, "b_new": 0.0}` | Ca hội tụ hoàn hảo sai số 0 |
| `linear_regression_step([2.0, 2.0], [4.0, 4.0], 1.0, 0.0, 0.05)` | `{"loss": 4.0, "dw": -8.0, "db": -4.0, "w_new": 1.4, "b_new": 0.2}` | Ca dữ liệu có giá trị trùng lặp |
| `linear_regression_step([], [], 0.0, 0.0, 0.1)` | `None` | Ca biên danh sách đầu vào rỗng |
| `linear_regression_step([1.0], [2.0, 3.0], 0.0, 0.0, 0.1)` | `None` | Ca biên kích thước x và y không khớp |

### Cấm
- `sklearn`
- `scipy`
- `LinearRegression`
