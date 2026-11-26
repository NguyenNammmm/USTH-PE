# Bàn giao thiết kế và chấm bài học Machine Learning PRIMM

Ngày bàn giao 27/11/2026 · Phiên bản giáo trình được chấm `acce7f7` trên nhánh `test-ML-nam`.

## Kết luận bàn giao

Bộ 36 phiếu đạt trung bình **63,1/100** theo mục tiêu học viên tự giải lại cùng một dạng bài với dữ liệu mới. Ca kiểm Make 1 là phần đã có sẵn. Việc cần làm trước là thống nhất **đầu vào, quy tắc giải và đầu ra chính** giữa Run, Modify và Make 1. Sau đó thêm các lượt tự giải riêng và một lần kiểm lại ở buổi sau. [Bản giáo trình đã chấm](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/blob/acce7f7669ebebb55bd958ef53373bc6cb2e01f9/PE_Machine_Learning/docs/PRIMM/Machine-Learning-PE-PRIMM.md)

## Hai cuốn sách dùng để làm gì

### Understanding by Design — Grant Wiggins và Jay McTighe

Thiết kế ngược theo thứ tự **đầu ra mong muốn → bằng chứng đánh giá → hoạt động học**. Viết đề cuối và cách chấm trước khi chọn ví dụ hoặc sửa phiếu. Tách bằng chứng thực hiện đúng thao tác khỏi bằng chứng vận dụng được trong một tình huống mới. [Khung UbD của hai tác giả](https://jaymctighe.com/wp-content/uploads/2020/06/UbD-White-Paper.pdf)

| Chương | Việc áp dụng khi soạn bài |
|---|---|
| **1. Backward Design** | Viết đầu ra quan sát được. Ví dụ, học viên tự tính đúng một bước Batch Gradient Descent trên bộ dữ liệu chưa gặp và nộp cặp tham số mới. |
| **7. Thinking Like an Assessor** | Chọn bằng chứng cho từng mục tiêu. Đổi số để kiểm thao tác. Cho học viên nhận diện và giải thích một lỗi trong mã mới để kiểm vận dụng. |
| **8. Criteria and Validity** | Chốt điều kiện đúng và dung sai trước. Tạo ca phân biệt lời giải đúng với lỗi phổ biến. Với ML05, cần một ca mà dùng trọng số mới để tính gradient của bias sẽ làm kết quả sai. |
| **9. Planning for Learning** | Sắp từ đọc mẫu có hướng dẫn đến tự làm, nhận phản hồi và làm lại. Đối chiếu từng hoạt động với yêu cầu của đề cuối. |

Tên và số chương theo [*Understanding by Design*, Expanded 2nd Edition](https://www.pearson.com/en-us/subject-catalog/p/understanding-by-design-expanded-edition/P200000002022/9780131950849).

### Make It Stick — Peter C. Brown, Henry L. Roediger III và Mark A. McDaniel

Ba cách áp dụng cho bài luyện là **tự nhớ lại và vận dụng**, **luyện cách quãng**, và **xen kẽ những dạng bài cần phân biệt**. Dùng vài biến thể đổi số để học viên làm quen thao tác. Bố trí một đề chưa gặp ở buổi sau để đo khả năng tự làm lại. Khi đã dạy các dạng liên quan, giao một đề buộc học viên tự chọn cách giải. [Hướng dẫn của nhóm tác giả](https://www.makeitstick.com/learning-strategies)

| Chương | Việc áp dụng khi soạn bài |
|---|---|
| **2. To Learn, Retrieve** | Đóng mã mẫu trước lượt tự giải. Cho học viên nộp kết quả hoặc viết lại quy trình. Mở đáp án và giải thích sau lần thử. |
| **3. Mix Up Your Practice** | Đặt một bài cùng dạng ở buổi sau. Khi mục tiêu là phân biệt cách giải, xen kẽ những dạng đã học và để học viên tự chọn quy tắc. |
| **4. Embrace Difficulties** | Giảm hỗ trợ đúng ở thao tác cần học. Chẳng hạn, bỏ gợi ý tính gradient bias rồi phản hồi ở bước tính sai. |
| **5. Avoid Illusions of Knowing** | So kết quả khi còn nhìn mẫu với kết quả trên một đề độc lập. Dùng lượt buổi sau để kiểm tra lại mức độ nhớ và vận dụng. |

Tên và số chương theo [*Make It Stick*, Harvard University Press](https://www.degruyterbrill.com/document/doi/10.4159/9780674419377/html).

**Thứ tự đọc nếu cần sửa bài ngay:** UbD **1 → 7 → 8**, rồi *Make It Stick* **2 → 3**. Dùng UbD chương 9 để sắp lại phiếu và *Make It Stick* chương 4–5 để rà gợi ý, phản hồi và lượt kiểm lại.

## Mẫu thiết kế cho một topic

1. **Khóa đề lõi.** Ghi đầu vào, quy tắc, dạng kết quả phải nộp và ca phân biệt lỗi cần bắt.
2. **A–C · Đọc, chạy và giải thích mẫu.** Dùng một đề mẫu có cùng đầu ra với Make 1. Cho học viên chỉ ra bước quyết định kết quả.
3. **D · Ba lượt luyện cùng đề.** Đổi giá trị, nhãn hoặc tham số đã có. Giữ thao tác và đầu ra chính. Thay kích thước dữ liệu được tính nếu quy trình hiện tại xử lý được.
4. **E · Tự giải trên dữ liệu mới.** Giao ít nhất ba đề độc lập. Cho nộp trước khi xem đáp án, có phản hồi theo từng lỗi. Ghi mốc đạt bằng số ca hoặc ca bắt lỗi bắt buộc.
5. **Buổi sau · Kiểm lại.** Đưa một bộ dữ liệu chưa gặp, với mã mẫu đóng. Ghi kết quả riêng để phân biệt làm được ngay và làm lại được sau khoảng nghỉ.
6. **F · Chuyển giao.** Sau mốc tự kiểm, giao tình huống cần nhận ra hoặc giải thích quy tắc. Ví dụ, đổi từ tính một bước sang tìm lỗi cập nhật tuần tự trong mã.

Ví dụ, đổi `k` trong k-NN vẫn là một lượt luyện nếu giữ Euclid và quy tắc xử lý hòa. Chuyển sang Manhattan là bài mở rộng. Giữ **một yêu cầu chính** cho các lượt lặp giúp người học luyện đủ thao tác trước khi phải chọn phương pháp.

## Thang điểm đã dùng để tự chấm

| Tiêu chí | Tối đa | Cách cho điểm | Trung bình |
|---|---:|---|---:|
| **Đề lõi xuyên suốt** | 25 | 25 nếu Run và Make 1 dùng cùng thao tác chính, quy ước và đầu ra chính. 15 nếu một bước chỉ luyện một phần hoặc đổi hợp đồng đầu vào/đầu ra. 5 nếu cùng chủ đề nhưng Make 1 cần thuật toán chính khác. 0 nếu thiếu đề lõi. | 19,4 |
| **Lặp có hướng dẫn** | 30 | Mỗi lượt Modify được 10 nếu đổi dữ liệu hoặc tham số đã có và vẫn giải được cùng việc bằng quy trình ở Run. Tối đa một lần cho mỗi mục Modify. | 16,4 |
| **Tự giải cùng đề trên dữ liệu mới** | 20 | 20 nếu có ít nhất 3 bộ dữ liệu độc lập dùng cùng đề và học viên tự nộp trước khi mở kết quả. 10 nếu Make 1 tự làm đúng đề lõi nhưng chưa có chuỗi đó. 5 nếu Make 1 chỉ lặp một phần. 0 nếu Make 1 đổi thao tác chính. | 7,2 |
| **Tự kiểm kết quả** | 15 | 15 nếu Make 1 có ít nhất 2 ca có đầu ra đối chiếu và 1 ca biên hoặc đầu vào sai. 10 nếu có 2 ca có đầu ra. 5 nếu có 1 ca. 0 nếu thiếu. | 15,0 |
| **Thời điểm chuyển giao** | 10 | 10 nếu Make 2 có nhãn riêng và đứng sau mốc tự kiểm cụ thể. 5 nếu Make 2 có nhãn riêng. 0 nếu thiếu điểm chuyển. | 5,0 |

**Cách tính.** Mỗi phiếu có trọng số như nhau. Mỗi mục Modify được tối đa 10 điểm, kể cả mục có nhiều thao tác thử. Ca test Make 1 kiểm cùng một hàm đã viết. Chỉ tính vào lượt tự giải nếu phiếu giao một đề riêng buộc học viên nộp kết quả cho ca đó trước khi được xem đáp án.

**Phạm vi.** Rà cả 36 phiếu, 108 mục Modify và cấu trúc của 151 ca kiểm Make 1. Ngân hàng 603 câu được xem theo mẫu để tìm câu có thể ghép vào chuỗi luyện. Điểm phản ánh thiết kế phiếu trước khi thử với học viên. [Bản chấm gốc](https://chatgpt.com/space/page_2f6d98d25bf88191a7e66d83785aa5f4)

## Kết quả và thứ tự sửa

- **63,1/100 chung**, gồm trung bình **63,2** ở 28 bài chính và **62,5** ở 8 bài bổ sung.
- **59/108 lượt Modify** giữ nguyên dạng bài. Phân bố số lượt đạt trên mỗi phiếu là 2 phiếu đạt 0 lượt, 12 đạt 1, 19 đạt 2 và 3 đạt đủ 3. Ba phiếu đạt đủ là ML02, ML22 và MLP07. ML22 giữ dạng trong phạm vi một mẫu, trong khi Make 1 còn yêu cầu tính trung bình qua batch.
- **18/36 phiếu** giữ nguyên thao tác và đầu ra chính từ Run đến Make 1. Có 16 phiếu nối một phần và hai phiếu đổi thao tác chính. ML27 chuyển từ gộp phiếu tất cả cây sang chỉ gộp phiếu OOB. MLP04 chuyển từ nhận diện core và border sang nối cụm và gán nhãn.
- **0/36 phiếu** giao ít nhất ba đề tự giải độc lập cùng dạng ngay trong luồng phiếu. Cả 36 đạt tiêu chí ca kiểm Make 1 và có Make 2 được đặt tên riêng.

**Sửa trước ML07, ML15, ML27 và MLP04.** Chốt thao tác và đầu ra ở E, rồi sửa B để minh họa đúng đề đó. Sau đó lấy ML05 làm mẫu cho ba lượt D và các đề E độc lập. Có thể tái sử dụng ML05-practice-4 và ML05-practice-7 nếu chuẩn hóa cùng dạng đầu ra và quy ước chấm.

### Các mối nối cần giữ

| Tuyến tiên quyết | Điều đã nối được | Cách làm mối nối rõ hơn |
|---|---|---|
| **ML04 → ML05** | ML04 tính residual và J. ML05 dùng residual để tính một bước cập nhật. | Dùng lại đúng một bộ x, y, w, b ở bài sau. Giữ kiểm J như bài chuyển giao sau khi làm thạo cập nhật. |
| **ML09 → ML10 → ML11** | Logit và xác suất đi vào loss/gradient, rồi gradient đi vào Newton. | Giữ chung ma trận thiết kế A, y và w. Chuyển đầu ra của bài trước thành dữ liệu đã biết của bài sau. |
| **ML21 → ML22** | Mạng hai tầng đi từ forward sang backprop. Ví dụ đổi cấu hình ReLU + đầu ra tuyến tính sang sigmoid + BCE. | Mở ML22 bằng một lượt forward cho chính mạng sigmoid + BCE sẽ dùng để tính gradient. |
| **ML23 → ML24** | Nhãn từ Lloyd có thể làm đầu vào cho Rand/Jaccard. Phiếu hiện dùng nhãn cho sẵn. | Thêm một ca lấy nhãn từ ML23, rồi đối chiếu với một phân hoạch tham chiếu. Giữ đề Rand/Jaccard độc lập cho vòng luyện số. |

## Mẫu áp dụng và đáp án ML05

**Đề cố định.** Tính đúng một bước Batch Gradient Descent cho hồi quy tuyến tính một biến. Nhận hai vector `x` và `y` cùng độ dài dương, `w` và `b` cũ cùng tốc độ học `η` không âm. Nộp `(w_mới, b_mới)`. Tính cả hai gradient từ cùng một residual cũ.

1. Tính `r = w*x + b − y`.
2. Tính `g_w = mean(r*x)` và `g_b = mean(r)`.
3. Tính `w_mới = w − η*g_w` và `b_mới = b − η*g_b` bằng hai gradient vừa có.

| Lượt | x | y | w cũ | b cũ | η |
|---|---|---|---:|---:|---:|
| Run mẫu | [0, 2] | [1, 5] | 0 | 0 | 0,1 |
| D1 · Đổi η | [0, 2] | [1, 5] | 0 | 0 | 0,2 |
| D2 · Đổi tham số cũ | [0, 2] | [1, 5] | 1 | 0,5 | 0,1 |
| D3 · Đổi nhãn đích | [0, 2] | [−1, 3] | 0 | 0 | 0,1 |
| E1 · Tự làm | [1, 3] | [3, 7] | 0 | 0 | 0,1 |
| E2 · Tự làm | [−1, 2] | [0, 5] | 1 | 1 | 0,2 |
| E3 · Tự làm | [−2, 1] | [−5, 1] | 2 | −1 | 0,3 |
| E4 · Tự làm | [−2, 2] | [1, −1] | 0 | 0 | 0,2 |

**Chấm lượt học viên.** Mỗi thành phần đúng được 1 điểm. Một ca đạt khi cả hai thành phần đúng trong dung sai tuyệt đối 10⁻⁹. Mốc mẫu là đạt ít nhất 3/4 ca E, trong đó E2 bắt buộc đạt. Khi chưa đạt, cho học viên xem lỗi ở residual hoặc gradient và thử lại với bộ số mới. Ở buổi sau, giao một bộ số khác để kiểm lại. Có thể dùng một đoạn mã có lỗi cập nhật tuần tự cho bài chuyển giao.

### Đáp án bàn giao cho người soạn

| Lượt | Gradient w | Gradient b | w mới | b mới |
|---|---:|---:|---:|---:|
| Run mẫu | −5 | −3 | 0,5 | 0,3 |
| D1 | −5 | −3 | 1,0 | 0,6 |
| D2 | −2,5 | −1,5 | 1,25 | 0,65 |
| D3 | −3 | −1 | 0,3 | 0,1 |
| E1 | −12 | −5 | 1,2 | 0,5 |
| E2 | −2 | −1 | 1,4 | 1,2 |
| E3 | 0 | 0 | 2,0 | −1,0 |
| E4 | 2 | 0 | −0,4 | 0,0 |

Tám kết quả đã được đối chiếu giữa phép tính bằng phân số và hàm `gd_step` của giáo trình. Dùng `w_mới` để tính gradient của `b` ở E2 sẽ cho `b = 1.16` thay vì `1.20`. E4 có gradient bias bằng 0 và gradient của `w` bằng 2. Phiếu ML05 hiện tại được chấm **65/100**. Bộ số trên là mẫu biên tập để áp dụng trong lượt sửa tiếp. [Phiếu ML05 đã chấm](https://github.com/ProgrammingEdu-USTH/Giao_Trinh_PE/blob/acce7f7669ebebb55bd958ef53373bc6cb2e01f9/PE_Machine_Learning/docs/PRIMM/Machine-Learning-PE-PRIMM.md#L2385)

## Điểm của 36 phiếu

Cột **Lượt giữ đề** ghi số thứ tự của mục Modify được tính, mỗi lượt tương ứng 10 điểm. Mỗi phiếu dưới đây có thêm 15 điểm tự kiểm và 5 điểm cho phần chuyển giao. Tổng điểm theo hàng bằng **đề lõi + 10 × số lượt giữ đề + điểm tự làm + 20**.

### 28 bài chính

| Bài | Đề lõi /25 | Lượt giữ đề | Tự làm /20 | Tổng /100 | Căn cứ |
|---|---:|:---:|---:|---:|---|
| ML01 | 15 | 1 | 5 | **50** | Run trộn đọc shape/trục với tích vô hướng. Make thêm bias. |
| ML02 | 25 | 1, 2, 3 | 10 | **85** | Cả ba lượt giữ nguyên công thức hiệp phương sai mẫu. |
| ML03 | 25 | 1 | 10 | **65** | Lượt 2 bổ sung nhánh lỗi. Lượt 3 đổi sang công thức scaling khác. |
| ML04 | 25 | 1, 2 | 10 | **75** | Hai lượt giữ J. Lượt 3 thêm đầu ra MAE. |
| ML05 | 25 | 1 | 10 | **65** | Lượt 2 chuyển sang đánh giá J. Lượt 3 chạy 5 bước thay vì 1. |
| ML06 | 15 | 1, 2 | 5 | **60** | Run in cả batch và mean gradient, Make chỉ chia chỉ số. Lượt 3 kiểm tái lập seed. |
| ML07 | 15 | — | 5 | **40** | Bỏ intercept, kiểm hạng và đổi bộ giải đều đổi nhiệm vụ so với mẫu. |
| ML08 | 15 | 1, 2 | 5 | **60** | Run fit và dự đoán, Make chỉ tạo cột đa thức. Lượt 3 thêm MSE validation. |
| ML09 | 15 | 1, 2 | 5 | **60** | Run đi từ X đến p và nhãn, Make nhận logit. Lượt 3 thêm đặc trưng bình phương. |
| ML10 | 25 | 1, 2 | 10 | **75** | Hai lượt giữ cặp loss–gradient. Lượt 3 cấp logit trực tiếp và chỉ kiểm loss. |
| ML11 | 15 | 1 | 5 | **50** | Một lượt lặp Newton gốc. Hai lượt sau xử lý Hessian suy biến hoặc thêm damping. |
| ML12 | 25 | 1, 3 | 10 | **75** | Đổi k hoặc giá trị tọa độ vẫn dùng Euclid. Lượt 2 đổi metric. |
| ML13 | 25 | 1, 2 | 10 | **75** | Hai lượt đổi K, giữ cách chia. Lượt 3 chuyển sang tổng hợp điểm. |
| ML14 | 25 | 1, 2 | 10 | **75** | Hai lượt giữ bộ metric. Lượt 3 thêm quy ước R² khi y hằng. |
| ML15 | 15 | — | 5 | **40** | Make thêm F1. Các lượt Modify thêm metric hoặc quy ước chia cho 0. |
| ML16 | 15 | 1 | 5 | **50** | Run dùng danh sách ngưỡng sẵn. Make dựng danh sách ngưỡng. Lượt 2–3 thêm AUC. |
| ML17 | 25 | 1 | 10 | **65** | Lượt 2 thêm quy tắc hòa khi đảo thứ tự. Lượt 3 so với baseline. |
| ML18 | 25 | 1 | 10 | **65** | Lượt 2 đổi penalty. Lượt 3 đổi số hệ số và cần đổi kích thước ma trận phạt. |
| ML19 | 25 | 1, 2 | 10 | **75** | Hai lượt đổi w hoặc b. Lượt 3 đổi từ ≥ sang >. |
| ML20 | 15 | 1 | 5 | **50** | Run in ba hàm một lần, Make chọn từng hàm. Lượt 2–3 thêm hàm hoặc đổi biểu thức. |
| ML21 | 25 | 1, 3 | 10 | **75** | Đổi bias hoặc số đầu ra vẫn giữ cùng phép lan truyền. Lượt 2 bỏ ReLU. |
| ML22 | 15 | 1, 2, 3 | 5 | **70** | Ba lượt đổi số cho một mẫu. Make còn yêu cầu lấy trung bình qua batch. |
| ML23 | 25 | 1, 3 | 10 | **75** | Lượt 1 và 3 giữ một vòng Lloyd. Lượt 2 cần xử lý cụm rỗng. |
| ML24 | 25 | 1, 2 | 10 | **75** | Hai lượt đổi phân hoạch. Lượt 3 bổ sung quy ước Jaccard cho mẫu số 0. |
| ML25 | 15 | 1, 2 | 5 | **60** | Run in tọa độ chiếu, Make trả trục PCA. Lượt 3 dựng lại dữ liệu. |
| ML26 | 15 | 1 | 5 | **50** | Run chấm các điểm chia có sẵn, Make tìm điểm chia tốt nhất. Lượt 2–3 thêm quy tắc hoặc đổi impurity. |
| ML27 | 5 | 1, 2 | 0 | **45** | Run gộp phiếu mọi cây. Make chỉ gộp phiếu từ các cây mà mẫu là OOB. |
| ML28 | 25 | 1 | 10 | **65** | Lượt 2 thêm xử lý cột hằng. Lượt 3 chọn mô hình qua validation. |

### 8 bài bổ sung

| Bài | Đề lõi /25 | Lượt giữ đề | Tự làm /20 | Tổng /100 | Căn cứ |
|---|---:|:---:|---:|---:|---|
| MLP01 | 15 | 1 | 5 | **50** | Run gồm one-hot và rời rạc hóa. Make chỉ làm one-hot. |
| MLP02 | 25 | 1 | 10 | **65** | Một lượt đổi dữ liệu cho variance filter. Hai lượt còn lại đổi tiêu chí chọn cột. |
| MLP03 | 15 | 1, 2 | 5 | **60** | Hai lượt đổi điểm dừng hoặc số liệu. Lượt 3 đổi sang complete linkage. |
| MLP04 | 5 | 1, 2 | 0 | **45** | Run nhận diện lân cận, core và border. Make thêm bước nối cụm và gán nhãn. |
| MLP05 | 25 | 1, 2 | 10 | **75** | Hai lượt giữ hinge loss và mục tiêu. Lượt 3 chuyển sang kernel. |
| MLP06 | 15 | 1, 2 | 5 | **60** | Run báo SSE trên dữ liệu đã trừ tâm, Make trả ma trận dựng lại sau cộng trung bình. |
| MLP07 | 25 | 1, 2, 3 | 10 | **85** | Ba lượt đổi radius, x hoặc lr, giữ cùng quy tắc SOM. |
| MLP08 | 15 | 1, 2 | 5 | **60** | Mẫu 2 cụm dùng một tỷ số. Thêm cụm thứ ba mới đòi hỏi tính max cho từng cụm. |

## Nguồn cần mở khi tiếp quản

| Việc | Tệp hoặc tài liệu |
|---|---|
| Sửa đề lõi, mã Run, Modify, Make 1 và ca kiểm | [Nguồn PRIMM](../source/primm.json) |
| Tìm câu cùng dạng để đưa vào các lượt luyện | [Ngân hàng câu hỏi](../source/questions.json) |
| Tra tiên quyết giữa các bài chính | [Khung khóa học](../source/course.json) |
| Dựng lại bài Markdown theo từng mã và kiểm mã mẫu cùng ca Make 1 | [Công cụ dựng PRIMM](../tools/dung_primm.py) |
| Đối chiếu phạm vi nội dung với tài liệu giảng dạy | [Đối chiếu Drive](DOI-CHIEU-DRIVE.md) |

Sau khi sửa nguồn, chạy trình dựng từ thư mục `PE_Machine_Learning_PRIMM`. Lệnh `--check` đối chiếu bản dựng và chạy ca kiểm. Bước này kiểm nội dung kỹ thuật. Khi chấm lại, ghi rõ đề lõi, các lượt D đủ điều kiện và đề E độc lập đã giao. Dùng kết quả buổi sau để đánh giá khả năng tự làm lại.

```powershell
python tools/dung_primm.py
python tools/dung_primm.py --check
```
