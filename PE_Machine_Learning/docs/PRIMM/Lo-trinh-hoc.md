# Sơ đồ lộ trình học

Mỗi mũi tên trong sơ đồ nối một bài tiên quyết với bài sử dụng kiến thức đó. Các ô màu vàng là bài bổ sung.

```mermaid
flowchart LR
    START["Tự kiểm đầu vào"]
    ML01["ML01 · Dữ liệu theo hàng"]
    ML02["ML02 · Hiệp phương sai"]
    ML03["ML03 · Chuẩn hóa"]
    ML04["ML04 · Tổn thất hồi quy"]
    ML05["ML05 · Hạ gradient"]
    ML06["ML06 · Chia lô"]
    ML07["ML07 · Hồi quy đa biến"]
    ML08["ML08 · Đặc trưng đa thức"]
    ML09["ML09 · Sigmoid và nhãn"]
    ML10["ML10 · BCE và gradient"]
    ML11["ML11 · Bước Newton"]
    ML12["ML12 · k láng giềng"]
    ML13["ML13 · Kiểm định K phần"]
    ML14["ML14 · Chỉ số hồi quy"]
    ML15["ML15 · Chỉ số phân loại"]
    ML16["ML16 · Đường ROC"]
    ML17["ML17 · Chọn bậc"]
    ML18["ML18 · Ridge"]
    ML19["ML19 · Perceptron"]
    ML20["ML20 · ReLU"]
    ML21["ML21 · Lan truyền tiến"]
    ML22["ML22 · Lan truyền ngược"]
    ML23["ML23 · K-means"]
    ML24["ML24 · Rand và Jaccard"]
    ML25["ML25 · PCA"]
    ML26["ML26 · Chia theo Gini"]
    ML27["ML27 · Bỏ phiếu OOB"]
    ML28["ML28 · Chuỗi hồi quy"]
    MLP01["MLP01 · Mã hóa một-nóng"]
    MLP02["MLP02 · Lọc phương sai"]
    MLP03["MLP03 · Phân cụm phân cấp"]
    MLP04["MLP04 · DBSCAN"]
    MLP05["MLP05 · SVM"]
    MLP06["MLP06 · SVD"]
    MLP07["MLP07 · SOM"]
    MLP08["MLP08 · Davies–Bouldin"]
    START --> ML01
    ML01 --> ML02
    ML01 --> ML03
    ML02 --> ML03
    ML01 --> ML04
    ML04 --> ML05
    ML05 --> ML06
    ML04 --> ML07
    ML05 --> ML07
    ML07 --> ML08
    ML04 --> ML09
    ML09 --> ML10
    ML10 --> ML11
    ML01 --> ML12
    ML04 --> ML13
    ML04 --> ML14
    ML09 --> ML15
    ML15 --> ML16
    ML08 --> ML17
    ML13 --> ML17
    ML17 --> ML18
    ML05 --> ML18
    ML09 --> ML19
    ML19 --> ML20
    ML20 --> ML21
    ML21 --> ML22
    ML01 --> ML23
    ML23 --> ML24
    ML02 --> ML25
    ML01 --> ML26
    ML26 --> ML27
    ML03 --> ML28
    ML07 --> ML28
    ML09 --> ML28
    ML13 --> ML28
    ML15 --> ML28
    ML03 --> MLP01
    ML17 --> MLP02
    ML23 --> MLP03
    ML23 --> MLP04
    ML19 --> MLP05
    ML25 --> MLP06
    ML23 --> MLP07
    ML24 --> MLP08
    classDef elective fill:#f4ead4,stroke:#9d783a,color:#392a13
    class MLP01,MLP02,MLP03,MLP04,MLP05,MLP06,MLP07,MLP08 elective
```

### Các tuyến học

- **Nền tảng dữ liệu** · [ML01 Dữ liệu theo hàng](../../bai-hoc/ML01.md) → [ML02 Hiệp phương sai](../../bai-hoc/ML02.md) → [ML03 Chuẩn hóa](../../bai-hoc/ML03.md) → [MLP01 Mã hóa một-nóng](../../bai-hoc/MLP01.md)

- **Hồi quy và tối ưu** · [ML01 Dữ liệu theo hàng](../../bai-hoc/ML01.md) → [ML04 Tổn thất hồi quy](../../bai-hoc/ML04.md) → [ML05 Hạ gradient](../../bai-hoc/ML05.md) → [ML06 Chia lô](../../bai-hoc/ML06.md)

- **Hồi quy đa biến** · [ML04 Tổn thất hồi quy](../../bai-hoc/ML04.md) → [ML05 Hạ gradient](../../bai-hoc/ML05.md) → [ML07 Hồi quy đa biến](../../bai-hoc/ML07.md) → [ML08 Đặc trưng đa thức](../../bai-hoc/ML08.md)

- **Logistic và Newton** · [ML04 Tổn thất hồi quy](../../bai-hoc/ML04.md) → [ML09 Sigmoid và nhãn](../../bai-hoc/ML09.md) → [ML10 BCE và gradient](../../bai-hoc/ML10.md) → [ML11 Bước Newton](../../bai-hoc/ML11.md)

- **Phân loại theo khoảng cách** · [ML01 Dữ liệu theo hàng](../../bai-hoc/ML01.md) → [ML12 k láng giềng](../../bai-hoc/ML12.md)

- **Đánh giá hồi quy** · [ML04 Tổn thất hồi quy](../../bai-hoc/ML04.md) → [ML14 Chỉ số hồi quy](../../bai-hoc/ML14.md)

- **Đánh giá phân loại** · [ML09 Sigmoid và nhãn](../../bai-hoc/ML09.md) → [ML15 Chỉ số phân loại](../../bai-hoc/ML15.md) → [ML16 Đường ROC](../../bai-hoc/ML16.md)

- **Chọn và điều chuẩn mô hình** · [ML13 Kiểm định K phần](../../bai-hoc/ML13.md) → [ML17 Chọn bậc](../../bai-hoc/ML17.md) → [ML18 Ridge](../../bai-hoc/ML18.md)

- **Lọc đặc trưng** · [ML17 Chọn bậc](../../bai-hoc/ML17.md) → [MLP02 Lọc phương sai](../../bai-hoc/MLP02.md)

- **Mạng nơron** · [ML09 Sigmoid và nhãn](../../bai-hoc/ML09.md) → [ML19 Perceptron](../../bai-hoc/ML19.md) → [ML20 ReLU](../../bai-hoc/ML20.md) → [ML21 Lan truyền tiến](../../bai-hoc/ML21.md) → [ML22 Lan truyền ngược](../../bai-hoc/ML22.md)

- **Biên phân loại** · [ML19 Perceptron](../../bai-hoc/ML19.md) → [MLP05 SVM](../../bai-hoc/MLP05.md)

- **Phân cụm và đánh giá** · [ML01 Dữ liệu theo hàng](../../bai-hoc/ML01.md) → [ML23 K-means](../../bai-hoc/ML23.md) → [ML24 Rand và Jaccard](../../bai-hoc/ML24.md) → [MLP08 Davies–Bouldin](../../bai-hoc/MLP08.md)

- **Phân cụm mở rộng** · [ML23 K-means](../../bai-hoc/ML23.md) → [MLP03 Phân cụm phân cấp](../../bai-hoc/MLP03.md) / [ML23 K-means](../../bai-hoc/ML23.md) → [MLP04 DBSCAN](../../bai-hoc/MLP04.md) / [ML23 K-means](../../bai-hoc/ML23.md) → [MLP07 SOM](../../bai-hoc/MLP07.md)

- **Giảm chiều** · [ML02 Hiệp phương sai](../../bai-hoc/ML02.md) → [ML25 PCA](../../bai-hoc/ML25.md) → [MLP06 SVD](../../bai-hoc/MLP06.md)

- **Cây và tổ hợp** · [ML01 Dữ liệu theo hàng](../../bai-hoc/ML01.md) → [ML26 Chia theo Gini](../../bai-hoc/ML26.md) → [ML27 Bỏ phiếu OOB](../../bai-hoc/ML27.md)

- **Bài tổng hợp** · [ML28 Chuỗi hồi quy](../../bai-hoc/ML28.md)

Để vào ML28, hoàn thành ML03, ML07, ML09, ML13 và ML15.
