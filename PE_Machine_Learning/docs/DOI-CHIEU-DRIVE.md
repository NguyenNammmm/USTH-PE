# Đối chiếu giáo trình Machine Learning PE với Drive

## Kết luận

**Commit `dd6cfd7` khớp bộ giáo trình 603 câu trên Drive. Phạm vi slide USTH rộng hơn bộ 28 bài.** Bản đồ 28 hàng trong CSV khớp mã, tên bài, module và danh sách khái niệm của `source/course.json`. Tệp `ML_603_lessons_final.json` trên Drive trùng từng byte với `reference/studio-lessons.json` trong commit. SHA-256 của cả hai là `6448f5b248903ef0d8ff3e61bc2e589a5940083d62b90d6084d6463742fb9784`. [Commit gốc](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/commit/dd6cfd7652f0f5ba39179cdc9293a7016dc2bf99) · [JSON 603 câu](https://drive.google.com/file/d/1Fj2sOc134m_uvpMIhvTJcT8Qmzm2mFWe/view) · [CSV 28 bài](https://drive.google.com/file/d/1_UP5P5Mbu81srvNQYy1L8O3L3BS4Ce8_/view) · [Thư mục Drive](https://drive.google.com/drive/folders/1fwg-IDH1LrU0ekEIzx9e873vrnZH8Yhc)

**Phần thực hành của commit thiếu triển khai ở 20 bài.** Từ ML09 đến ML28, `referenceSolution` của bài S4 chỉ chuyển đầu vào thành mảng, kiểm tra rỗng rồi trả lại mảng nguyên. Ví dụ, ML09 chưa tính sigmoid, ML23 chưa gán hoặc cập nhật centroid và ML28 chưa fit mô hình hay đánh giá. Ví dụ Run của ba bài ML06–ML08 chỉ in một câu, còn 20 bài ML09–ML28 chỉ in shape (1, 2). Bản PRIMM có mã thực hiện mục tiêu từng bài và ca kiểm kết quả số, kích thước hoặc điều kiện biên. [Dữ liệu bài gốc](../source/practice.json) · [PRIMM ML09](../bai-hoc/ML09.md) · [PRIMM ML23](../bai-hoc/ML23.md) · [PRIMM ML28](../bai-hoc/ML28.md)

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
| Biểu diễn danh mục, dữ liệu thiếu và rời rạc hóa. [Data Preparation, slide 3–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) | [MLP01](../bai-hoc/MLP01.md) |
| Chọn đặc trưng bằng filter, wrapper, embedded. [Feature Selection, slide 13–31](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) | [MLP02](../bai-hoc/MLP02.md) |
| Phân cụm tích tụ và linkage. [Clustering, tr. 12–22](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP03](../bai-hoc/MLP03.md) |
| DBSCAN và core/border/noise. [Clustering, tr. 23–26](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP04](../bai-hoc/MLP04.md) |
| SVM, margin, soft margin và kernel. [Classification, tr. 30–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view) | [MLP05](../bai-hoc/MLP05.md) |
| SVD và dựng lại ma trận. [Statistics and PCA, tr. 36–38](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) | [MLP06](../bai-hoc/MLP06.md) |
| Self-Organizing Map. [Clustering, tr. 35–43](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP07](../bai-hoc/MLP07.md) |
| Davies–Bouldin và NMI. [Clustering, tr. 44–52](https://drive.google.com/file/d/17YDn3QB0YXwkEsUehvKPmS29DW9aA2lc/view) | [MLP08](../bai-hoc/MLP08.md) |

## Các điểm cần giữ rõ khi dạy

- **Quy ước và cách diễn giải.** Hiệp phương sai bằng 0 chưa đủ kết luận hai biến độc lập. Dùng đúng mẫu số cho phương sai mẫu/tổng thể, ghi hệ số 1/2 trong loss ML04 và quy ước λ trong Ridge. Với R², dự đoán tệ hơn mốc dự đoán bằng mean có thể cho R² âm. [Statistics and PCA, tr. 9–16](https://drive.google.com/file/d/1Yd6BlzBXRddQhwIGJVvA9-vVFi4F4ODF/view) · [Model Evaluation, tr. 8](https://drive.google.com/file/d/1yXQO-DDBgN2sT3wS1HLqXtdt9dI7HGNv/view)
- **Lựa chọn mô hình và độ tổng quát.** Chọn siêu tham số và tập đặc trưng bằng validation hoặc CV. Slide wrapper gọi tập chấm trong vòng chọn là “test”; vai trò của nó là validation. Tập test cuối cần độc lập. Random Forest vẫn có thể overfit, đặc biệt khi dữ liệu hoặc quy trình đánh giá có vấn đề. [Feature Selection, slide 22–24](https://docs.google.com/presentation/d/14IPwl3R2iMYVV20WYVdftkXVwHSTIMpa/edit) · [Ensemble Models, tr. 28](https://drive.google.com/file/d/13RwLiEQo8sAYKu-cjVoyz9986Z4zWAQt/view)
- **Phạm vi bổ sung.** Hai slide nhập môn có tổng quan ngành, phân biệt học có/không/bán giám sát và quy trình khai phá dữ liệu. Trong Drive còn có biến đổi dữ liệu ảnh/văn bản, ví dụ kernel dual đầy đủ và chi tiết thuật toán SOM. Gói thực hành mới tập trung vào phép tính lõi và các điểm thiếu lớn được nêu ở bảng trên. [Introduction, tr. 10–22](https://drive.google.com/file/d/1BK1s7InGNzpFWBHOx-2snV_U8-skGBl4/view) · [Data Mining Introduction, slide 16–26](https://docs.google.com/presentation/d/1J0TSOBcRdXKbvNK3AY45H-mYmDUv43eD/edit) · [Data Preparation, slide 10–16](https://docs.google.com/presentation/d/1n6iL0cB_wtuRsWrnAxK8RvfJ5KI1ezvp/edit) · [Classification, tr. 40–52](https://drive.google.com/file/d/1PM37G-DzdItdY9e8fnvqpfbtprnP-FqF/view)

## Bằng chứng kiểm tra

- Kiểm cấu trúc nguồn của commit đạt đủ 28 mã, 6 module, 603 câu và 168 test gốc. Chạy lại 181 đoạn lời giải có mã của ngân hàng câu hỏi và 168 ca S4 bằng CPython. Tất cả khớp kết quả gốc, kể cả các ca S4 chỉ thử hành vi kiểm đầu vào. Bảng đối chiếu rà khái niệm và các vấn đề thực hành chính. Từng đáp án lý thuyết trong 603 câu chưa được thẩm định riêng.
- Bản PRIMM có 36 bài. Chạy 36 mã mẫu và 151 ca Make 1 trên lời giải tham khảo. Kiểm thêm một số ca Modify và Make 2, gồm pipeline phân loại ML28 và so sánh kernel SVM. 603 câu ôn giữ mã và đáp án lựa chọn. Các câu có ngữ cảnh lĩnh vực được biên tập sang dữ liệu vô danh. Make 2 dùng ca kiểm ghi trong đề để người học tự đối chiếu.
- Hai tệp `4.ModelEvaluation.pdf` và `4. ModelEvaluation.pdf` có cùng SHA-256. Hai bản Regularization và hai bản Neural Network có số trang khác nhau; đã dùng các phần tương ứng theo số trang mỗi tệp.
