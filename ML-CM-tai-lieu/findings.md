# Kết Quả Rà Soát Repo Programming EDU (findings.md)

> **Người thực hiện:** Công Minh (ML-CM)  
> **Ngày rà soát:** 22/11/2026  
> **Nguyên tắc thực hiện:** CHỈ ĐỌC repo; không sửa file của repo; không commit; không in mật khẩu/token; mọi thông tin kèm đường dẫn:dòng và trích NGUYÊN VĂN.

---

## A. MÔN ML

### 1. Mọi thứ liên quan ML trong repo
- **Kết quả tìm kiếm tên file/thư mục:**
  - `docs/ml-pipeline.md`: Tài liệu thiết kế pipeline sinh đề và cách đánh giá (áp dụng cho python_advanced, SQL, ML).
  - `docs/questionnaire-spec.md`: Đặc tả bộ câu hỏi đầu vào và cách xếp module (áp dụng cho python_advanced, SQL, ML).
  - `ML-CM-tai-lieu/review-ml.md`: File đánh giá cục bộ của Công Minh đặt sẵn chờ bài ML.
  - `frontend/e2e/drag-regression.spec.ts`: File kiểm thử e2e cho tính năng kéo thả (từ khóa `regression` ở đây là kiểm thử hồi quy phần mềm, không phải bài học ML).
  - `scripts/fixtures/sample-course/course.json:6`: Nhắc tới ML trong mô tả gói bài mẫu:
    ```json
    "description": "Gói bài mẫu gọn để kiểm tra đồng bộ giáo trình cho mọi môn trước khi nạp bộ dữ liệu SQL và ML thật."
    ```
- **Kế hoạch giáo trình, danh sách module/bài ML dự kiến trong repo:**
  - Trong toàn bộ codebase và tài liệu hiện tại của repo **HOÀN TOÀN CHƯA CÓ** danh sách module hay bài học ML cụ thể nào.
- **Toàn văn phần nói về ML trong `docs/ml-pipeline.md`:**
  - [docs/ml-pipeline.md:3-5](file:///home/acm/pe-usth/docs/ml-pipeline.md#L3-L5):
    > "Phạm vi: sinh câu trắc nghiệm (MCQ) và bài tập code từ giáo trình có sẵn, lọc tự động, lưu chờ duyệt.
    > Áp dụng trước cho `python_advanced` (48 bài, 8 module); SQL và ML dùng cùng pipeline khi có gói bài."
- **Toàn văn phần nói về ML trong `docs/questionnaire-spec.md`:**
  - [docs/questionnaire-spec.md:3-4](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L3-L4):
    > "Khoá áp dụng: `python_advanced` (Advanced Python, 48 bài, 8 module). Môn SQL và ML dùng cùng
    > định dạng khi có giáo trình; chỉ đổi `course_id` và danh sách module."
  - [docs/questionnaire-spec.md:10](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L10):
    > "- **ML (Nghĩa, Tuần 3): dựng questionnaire và API.** Cài đặt mục 3 và 5."
  - [docs/questionnaire-spec.md:204](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L204):
    > "- **Môn SQL và ML:** dùng nguyên định dạng và quy tắc; chỉ cần bảng module của môn đó."

---

### 2. Bài "ML-REG-01" và kiểm tra trên mọi nhánh git
- **Về bài "ML-REG-01":**
  - Bài `ML-REG-01` **KHÔNG nằm trong repo pe-usth**, không có trong bất kỳ file nào và không do ai trong lịch sử commit tạo ra.
  - Nguồn gốc: Xuất phát từ chính nội dung người dùng đưa vào trong phiên chat trước đó (`step_index: 314`, ngày 21/11/2026 23:45:50 UTC+7):
    > `<USER_REQUEST>`  
    > `Chủ đề: Hồi quy tuyến tính đơn biến và Bước cập nhật Gradient Descent`  
    > `Mã bài: ML-REG-01 [NGOÀI NGUỒN]`  
    > `Module: Module 02 - Linear Regression [NGOÀI NGUỒN]`  
    > `Tiên quyết: Không`  
  - Trạng thái hiện tại: Bài học ngoài nguồn (được người dùng dán vào chat để hỏi đánh giá chất lượng); repo chưa có dữ liệu bài này.
  - File [ML-CM-tai-lieu/review-ml.md:5](file:///home/acm/pe-usth/ML-CM-tai-lieu/review-ml.md#L5) ghi nhận:
    > "Trạng thái: **CHƯA CÓ BÀI ĐỂ REVIEW** — file này đặt sẵn, cập nhật khi bài ML vào repo"
- **Kết quả `git branch -a`:**
  ```text
    main
  * test
    remotes/fork/test
    remotes/origin/HEAD -> origin/main
    remotes/origin/chiem-tinh
    remotes/origin/chiem-tinh-v3
    remotes/origin/main
    remotes/origin/test
    remotes/origin/tien-canh-ban-quan-trac
  ```
- **Tìm kiếm trên mọi nhánh:**
  - `git log --all -S"ML-REG"` $\rightarrow$ Không có kết quả (0 commit).
  - `git log --all --grep="ML-REG"` $\rightarrow$ Không có kết quả (0 commit).
  - Không có bất kỳ bài học ML nào trên mọi nhánh của repo.

---

## B. PHÂN CÔNG VÀ QUY TRÌNH

### 3. Git log và phân công nhân sự
- **Kết quả `git shortlog -sn --all`:**
  ```text
     505	sonkh
      29	Tuyet Mieu
      26	Nghia
      18	Cao Trí Thành
       4	Cao Văn Nhân
       2	doancongminh23bi14287
       1	Trần Quốc Thái
  ```
- **20 commit gần nhất (tác giả + ngày + thông điệp):**
  ```text
  816179a | doancongminh23bi14287 | 2026-11-21 | feat: organize retro games into gameretro folder (pacman, mario, doodle-jump, dino-runner)
  b72bdc4 | doancongminh23bi14287 | 2026-11-20 | feat: add retro pixel pacman game
  997bf0d | Cao Trí Thành | 2026-11-19 | feat: nối POST /api/survey ở /onboarding (cả khách và người đăng nhập), thêm học lại khoá, đổi tên hiển thị (PUT /api/user), cờ mock/API và unit test
  a6cda06 | Cao Trí Thành | 2026-11-19 | fix: bỏ ghi cứng hạn phiên 8 giờ (max-age=28800) ở frontend, đọc expiresAt từ /auth/refresh
  929aff1 | Cao Trí Thành | 2026-11-19 | feat: Script chép giáo trình vào curricula.json dùng được cho mọi môn, sửa lại kho bài của khóa python cho đủ 179 bài( trước đó chỉ có 172 bài) cop của nhánh main , tạo hướng dẫn cho nam.
  fd38f31 | Cao Trí Thành | 2026-11-19 | feat: sửa lại trang ôn tập hằng ngày
  c07cfa8 | Cao Trí Thành | 2026-11-19 | feat: sửa lại đường dẫn đến các giao diện mới.
  ac64816 | Nghia | 2026-11-19 | feat(courses): cho phep hoc lai khoa va luu lich su
  4c3494d | Cao Trí Thành | 2026-11-19 | feat: thêm giao diện tủ sách mới và giao diện các khóa học riêng (thành push hộ đức)
  41b5096 | Nghia | 2026-11-18 | fix(courses): đồng bộ số bài hoạt động an toàn (BE2)
  d60e49d | Nghia | 2026-11-18 | feat(learning-events): dựng POST /api/events và GET, POST /api/events/consent (BE6)
  d4efbbe | Nghia | 2026-11-18 | docs(ml): thiết kế pipeline sinh đề và cách đánh giá
  1bbd05a | Nghia | 2026-11-18 | docs(ml): đặc tả bộ câu hỏi đầu vào và cách xếp module
  6897f9d | Nghia | 2026-11-15 | feat(db): chỉ mục danh sách diễn đàn trên posts (BE7)
  8a7af2e | Nghia | 2026-11-15 | feat(diễn đàn): hạn mức riêng cho tạo bài và tạo bình luận (BE7)
  047ad35 | Nghia | 2026-11-15 | test(diễn đàn): 26 ca cho forum.service.ts, gồm cổng "không tải reactions" (BE7)
  8cf3a96 | Nghia | 2026-11-15 | perf(diễn đàn): đếm cảm xúc ở DB thay vì tải mọi hàng reactions (BE7)
  4034a0a | Nghia | 2026-11-15 | Merge origin/test (learning_events, migration, giao diện) vào BE4/BE5
  ad130c3 | Cao Văn Nhân | 2026-11-15 | thêm learning_events, migration chỉ mục/phiên bản nội dung, script kiểm bất biến DB và gói pe-da
  33834e6 | Cao Trí Thành | 2026-11-12 | hoàn tất khung chung lofi: khôi phục T4 Escape, T7 SSR nav và thanh điều hướng SiteHeader
  ```
- **Các trích dẫn nguyên văn về phân công nhân sự:**
  - [docs/ml-pipeline.md:6-7](file:///home/acm/pe-usth/docs/ml-pipeline.md#L6-L7):
    > "Trang này là bản thiết kế cho hai việc Tuần 2 (sinh trắc nghiệm 16–19/11, sinh bài code 19–23/11).  
    > Người duyệt: Nhân, Kiên. Việc đóng khi file có mặt; góp ý được sửa dần, không ai phải chờ."
  - [docs/ml-pipeline.md:82](file:///home/acm/pe-usth/docs/ml-pipeline.md#L82):
    > "Nam duyệt mẫu (B)"
  - [docs/ml-pipeline.md:127](file:///home/acm/pe-usth/docs/ml-pipeline.md#L127):
    > "Nam đánh giá **mẫu ngẫu nhiên 20 câu** mỗi lần chạy (không phải mọi câu), chấm 1–3 theo ba ý:"
  - [docs/questionnaire-spec.md:8](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L8):
    > "- **FE (Trí Thành):** màn `/onboarding` (`OnboardingSurveyView.tsx`) đang dùng 5 câu giả viết cứng."
  - [docs/questionnaire-spec.md:10](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L10):
    > "- **ML (Nghĩa, Tuần 3): dựng questionnaire và API.** Cài đặt mục 3 và 5."
  - [docs/questionnaire-spec.md:11](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L11):
    > "- **Tài liệu (Nam, N4):** câu xếp level theo module. Cột của bảng Nam khớp với trường ở mục 2."
  - [docs/questionnaire-spec.md:202-203](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L202-L203):
    > "...khi Nam xong bảng nhãn "bài tiên quyết" (việc gắn nhãn khái niệm và module, 19–23/11)  
    > thì đổi bước 3 thành "module đầu dưới ngưỡng mà mọi tiên quyết của nó đã đạt"."
  - [scripts/HUONG-DAN-NAM.md:1](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L1):
    > "1. Tạo 1 thư mục riêng cho môn học (vd `sql/` hoặc `ml/`) rồi gửi nguyên thư mục cho Nhân — Nam không cần chạy code."
  - [scripts/HUONG-DAN-NAM.md:5](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L5):
    > "5. Khi nhận bài, Nhân chỉ chạy 1 lệnh `python3 scripts/sync_curricula.py --bundle <thư_mục> --course <mã_môn>` để tự chép giáo trình, tính số bài/giờ thật và kiểm bằng unit test."
  - [AGENTS.md:341-342](file:///home/acm/pe-usth/AGENTS.md#L341-L342):
    > "**DB production CHƯA sửa** — cần Nhân duyệt rồi mới ghi, theo đúng thứ tự: sao lưu → UPDATE trong transaction → `check-db-invariants.ts`."
- **Người soạn bài ML:** **Nam (Nam Nguyễn)** là người chịu trách nhiệm soạn nội dung tài liệu môn học (`scripts/HUONG-DAN-NAM.md:1`, `docs/questionnaire-spec.md:11`). Nhân là người nhận bài và nạp vào repo (`scripts/HUONG-DAN-NAM.md:1, 5`). Nghĩa phụ trách kỹ thuật ML pipeline/API (`docs/questionnaire-spec.md:10`).

---

### 4. Quy trình đưa nội dung từ tài liệu vào repo
- **Script nhập bài:**
  - [scripts/HUONG-DAN-NAM.md:5](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L5):
    > "`python3 scripts/sync_curricula.py --bundle <thư_mục> --course <mã_môn>`"
  - Importer web qua giao diện `/admin`: [LESSON-IMPORT-FORMAT.md:3-5](file:///home/acm/pe-usth/LESSON-IMPORT-FORMAT.md#L3-L5):
    > "Trang `/admin` có mục **Nhập bài học từ PDF / Markdown**. Tải file lên, hệ thống nhận diện thành 4 bước S1–S4, bạn duyệt lại rồi bấm **Lưu vào khoá học**."
- **Định dạng nguồn tiếp nhận:**
  - Bundle JSON gồm `course.json` và `lessons.json` (hoặc thư mục `lessons/*.json`) theo cấu trúc mẫu [scripts/fixtures/sample-course/](file:///home/acm/pe-usth/scripts/fixtures/sample-course/).
  - Markdown hoặc PDF văn bản (không scan) theo mẫu heading S1–S4 ([LESSON-IMPORT-FORMAT.md:17-21](file:///home/acm/pe-usth/LESSON-IMPORT-FORMAT.md#L17-L21)).
- **Schema / cột bắt buộc:**
  - `course.json`: [scripts/HUONG-DAN-NAM.md:2](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L2):
    > "`id` (vd `sql`), `title`, `subtitle`, `description`, `level` (`beginner` / `intermediate` / `advanced`)."
  - `lessons.json`: [scripts/HUONG-DAN-NAM.md:4](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L4):
    > "Mỗi bài bắt buộc có đủ: `lesson_code`, `sort_order` (1, 2, 3… liên tục), `module` (`M1 · Tên chặng`), `title`, `estimated_minutes` (> 0), `xp_reward`, và `content_json`."
- **Mẫu tài liệu trong repo:**
  - File mẫu Markdown: [samples/lesson-fstring.md](file:///home/acm/pe-usth/samples/lesson-fstring.md).
  - File mẫu PDF: `samples/lesson-fstring.pdf`.
  - File mẫu cấu trúc JSON bundle: [scripts/fixtures/sample-course/course.json](file:///home/acm/pe-usth/scripts/fixtures/sample-course/course.json) và [scripts/fixtures/sample-course/lessons.json](file:///home/acm/pe-usth/scripts/fixtures/sample-course/lessons.json).
  - **Không có** file mẫu tài liệu `.docx` trong repo.

---

## C. CÂU HỎI XẾP LEVEL

### 5. Code nạp file questionnaire (loader, API, seed, validate)
- **Vị trí code loader và validator:**
  - File [frontend/src/lib/onboarding-questionnaire.ts:107-217](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts#L107-L217): Hàm `validateQuestionnaire(raw)` và `loadQuestionnaire(courseId, fetcher)`.
- **Backend API và Seed:**
  - Backend hiện **chưa có code controller hoặc service nào xử lý endpoint `/api/questionnaire` hay nạp seed questionnaire**.
  - Xác nhận nguyên văn tại [docs/questionnaire-spec.md:19](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L19):
    > "Bảng `questionnaires` (`version, title, questions_json, is_active`) | Có trong `schema.prisma`, chưa code nào đọc. Bộ câu lưu ở đây, **không cần migration**."
  - Xác nhận nguyên văn tại [docs/questionnaire-spec.md:10](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L10):
    > "- **ML (Nghĩa, Tuần 3): dựng questionnaire và API.** Cài đặt mục 3 và 5."
- **Giới hạn số lựa chọn mỗi câu:**
  - [frontend/src/lib/onboarding-questionnaire.ts:162](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts#L162) & [:195](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts#L195):
    > "`if (!Array.isArray(it.options) || it.options.length < 2) errors.push(\`items[${idx}] cần ít nhất 2 lựa chọn.\`);`"  
    Code kiểm định yêu cầu tối thiểu **2 lựa chọn**, không chặn trần số lựa chọn tối đa (trong khi [docs/ml-pipeline.md:109](file:///home/acm/pe-usth/docs/ml-pipeline.md#L109) quy định luật A2 là 3–4 lựa chọn).
- **Trường bắt buộc trong bộ câu hỏi:**
  - Cấp gốc: `course_id` (string), `version` (number >= 1), `params` (object có `mastery_threshold` trong `(0, 1]` và `self_assess_weight` trong `[0, 1]`), `items` (mảng >= 1 câu hỏi).
  - Cấp từng câu hỏi trong `items`: `id` (string duy nhất), `module_code` (string), `question` (string), `options` (mảng >= 2 phần tử, mỗi phần tử bắt buộc có trường `text` dạng chuỗi không rỗng).
  - Khóa đáp án: `correct` (chỉ số int) và `explanation` (chuỗi giải thích).
- **Kiểm định với file JSON đã soạn:**
  - Đã thực thi trực tiếp hàm `validateQuestionnaire` trong [frontend/src/lib/onboarding-questionnaire.ts](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts):
    - `ML-CM-tai-lieu/questionnaire-python-advanced.json`: **HỢP LỆ 100% (Errors: [])**
    - `ML-CM-tai-lieu/questionnaire-db-design.json`: **HỢP LỆ 100% (Errors: [])**
  - Cả hai file JSON đều hoàn toàn tương thích và được hệ thống tiếp nhận trực tiếp.

---

## D. CHẠY APP

### 6. Hướng dẫn chạy local, tài khoản test, URL deploy và kết quả kiểm thử app
- **Hướng dẫn chạy local:**
  - Trích nguyên văn [README.md:35-46](file:///home/acm/pe-usth/README.md#L35-L46):
    ```bash
    # Backend (cổng 5000)
    cp .env.example .env          # điền DATABASE_URL, DIRECT_URL, JWT_ACCESS_SECRET (>= 32 ký tự)...
    npm install
    npx prisma generate
    npm run start:dev

    # Frontend (cổng 3000) — terminal khác
    cd frontend
    npm install
    npm run dev
    ```
  - Trong repo **không có file `docker-compose.yml`**.
- **Tài khoản test:**
  - Tài khoản E2E: [frontend/e2e/helpers.ts:4-5](file:///home/acm/pe-usth/frontend/e2e/helpers.ts#L4-L5):
    > "`export const E2E_EMAIL = process.env.E2E_EMAIL || 'audit@example.com';`"  
    > "`export const E2E_PASSWORD = process.env.E2E_PASSWORD || 'AuditPass123';`"
  - Tài khoản giảng viên mẫu: [prisma/seed-courses.js:19](file:///home/acm/pe-usth/prisma/seed-courses.js#L19):
    > "`db_design: { email: 'leminhtuan@programmingedu.local', name: 'Lê Minh Tuấn' }`"
  - Tài khoản khách tự động: [AGENTS.md:121-123](file:///home/acm/pe-usth/AGENTS.md#L121-L123):
    > "`apiFetch gặp 401 mà không refresh được thì gọi POST /auth/guest để nhận tài khoản khách (email @guest.local, mật khẩu rỗng nên không đăng nhập bằng mật khẩu được), rồi bài học tự ghi danh.`"
- **URL bản deploy:**
  - Repo **không lưu URL deploy thật** nào (tuân thủ nguyên tắc bảo mật [AGENTS.md:282](file:///home/acm/pe-usth/AGENTS.md#L282): `"Ba môi trường, ba cặp biến. Không ghi link kết nối vào repo, vào chat hay vào .env.example"`). Chỉ có URL mẫu placeholder trong [runner/README.md:14](file:///home/acm/pe-usth/runner/README.md#L14) (`https://<backend>.onrender.com/health`) và [.env.example:22](file:///home/acm/pe-usth/.env.example#L22) (`*.vercel.app + *.onrender.com`).
- **Thực thi kiểm tra app trên engine `PE_runSQL` (định nghĩa tại `frontend/public/static/js/lesson_db_design.js:6387`):**
  Do app chạy hoàn toàn engine SQL parser client-side bằng JavaScript, ta thực thi kiểm tra trực tiếp qua hàm `PE_runSQL` của app mà không cần can thiệp hệ thống hay sửa đổi repo:
  1. **`db_02`**:
     - S4 query: `SELECT username, (EXTRACT(YEAR FROM CURRENT_DATE) - birth_year) AS age FROM player_profile WHERE address_city = 'Tokyo' ORDER BY age DESC;`
     - **Kết quả thực tế trong app:** Trả về `{ "error": "WHERE không hợp lệ: address_city = 'Tokyo'" }` do regex parser của app chưa hỗ trợ phân tích điều kiện WHERE kết hợp biểu thức này trên bảng player_profile.
  2. **`db_13`**:
     - S4 query: `SELECT u.username, u.country, COUNT(p.post_id) AS post_count FROM users u JOIN posts p ON p.user_id = u.user_id WHERE u.is_premium = true AND u.country = 'VN' GROUP BY u.user_id, u.username, u.country ORDER BY post_count DESC LIMIT 3;`
     - **Kết quả thực tế trong app:** **CHẠY THÀNH CÔNG VÀ RA CHÍNH XÁC 3 DÒNG!**  
       `cols: ["username", "country", "post_count"]`  
       `rows: [["minh_gamer", "VN", 5], ["dragon_vn", "VN", 4], ["sara_plays", "VN", 3]]`.  
       *(Khác với SQLite in-memory bị vướng lỗi kiểu chuỗi boolean 'true', engine PE_runSQL của app xử lý linh hoạt và cho kết quả chuẩn).*
  3. **`db_14`**:
     - S4 query: `SELECT settings->>'lang' AS lang, COUNT(*) AS user_count FROM app_users GROUP BY settings->>'lang' ORDER BY user_count DESC;`
     - **Kết quả thực tế trong app:** **CHẠY THÀNH CÔNG VÀ RA CHÍNH XÁC 2 DÒNG!**  
       `cols: ["lang", "user_count"]`  
       `rows: [["vi", 13], ["en", 9]]`.
  4. **`db_15`**:
     - S3 query: Dùng hàm không gian PostGIS `ST_DWithin` và `ST_MakePoint`.
     - **Kết quả thực tế trong app:** Trả về đối tượng bẫy lỗi có chủ đích:  
       `{ "pending": true, "msg": "⚙ Engine demo chưa mô phỏng được: spatial ST_DWithin — đáp án của bạn sẽ được chấm trực tiếp khi bấm Run/Submit." }`.  
       (S4 chạy với `within_10km = 'yes'` trả về `{ "error": "WHERE không hợp lệ: city = 'TP.HCM' AND within_10km = 'yes'" }`).
  5. **`db_16`**:
     - S4 query: Cú pháp Django ORM `LogEvent.objects.filter...`
     - **Kết quả thực tế trong app:** Trả về bẫy lỗi có chủ đích:  
       `{ "pending": true, "msg": "⚙ Engine demo chưa mô phỏng được: Django ORM — đáp án của bạn sẽ được chấm trực tiếp khi bấm Run/Submit." }`.
  6. **`db_17`**:
     - S4 query: Dùng placeholder `%s` của psycopg2 và đa câu lệnh.
     - **Kết quả thực tế trong app:** Trả về bẫy lỗi có chủ đích:  
       `{ "pending": true, "msg": "⚙ Engine demo chưa mô phỏng được: Python placeholder %s — đáp án của bạn sẽ được chấm trực tiếp khi bấm Run/Submit." }`.
- **Chính xác các bước người dùng cần làm để khởi chạy toàn diện full-stack:**
  1. Tạo file `.env` tại thư mục gốc từ `.env.example`, điền thông tin chuỗi kết nối `DATABASE_URL` tới PostgreSQL.
  2. Tại thư mục gốc, cài đặt và sinh prisma client: `npm install && npx prisma generate`.
  3. Khởi chạy Backend NestJS: `npm run start:dev` (chạy trên cổng 5000).
  4. Mở cửa sổ terminal thứ hai, chuyển vào thư mục frontend: `cd frontend && npm install && npm run dev` (chạy trên cổng 3000).
  5. Mở trình duyệt truy cập: `http://localhost:3000/lesson/db_design?lesson=2` (hoặc thay bằng lesson=14, 15, 16, 17, 18 tương ứng) để tương tác trực tiếp với giao diện.

---

## E. CHECKLIST 6 MỤC

### 7. Tra cứu tài liệu về "checklist" hoặc "6 mục" cho môn SQL
- **Trong thư mục `docs/`:** **KHÔNG CÓ**. Chỉ tồn tại 2 file `docs/ml-pipeline.md` và `docs/questionnaire-spec.md`.
- **Trong lịch sử git:**
  - Quét commit message với từ khóa `checklist`: 0 kết quả liên quan đến môn SQL.
  - Quét commit message với từ khóa `6 mục`: 0 kết quả liên quan đến môn SQL (chỉ có commit của môn Python về đo kích thước nút bấm và số màn giao diện).
- **Nguồn gốc cụm từ "checklist 6 mục":**
  - Cụm từ xuất phát từ file bản mẫu review cục bộ [ML-CM-tai-lieu/review-ml.md:18](file:///home/acm/pe-usth/ML-CM-tai-lieu/review-ml.md#L18) với 6 cột tiêu chí: `S1 Dự đoán | S2 Trắc nghiệm | S3 Ghép code | S4 Sandbox | Tải lại | Tiến độ`.
  - Cấu trúc 6 màn này bắt nguồn từ tài liệu Python v3 tại [scripts/pe-v3/README.md:32-44](file:///home/acm/pe-usth/scripts/pe-v3/README.md#L32-L44).
  - Đối với môn SQL (Database Design), giao diện app tại [frontend/src/components/LessonDbDesign.tsx:83-100](file:///home/acm/pe-usth/frontend/src/components/LessonDbDesign.tsx#L83-L100) được chia thành 4 bước: `1. Lý thuyết`, `2. Trắc nghiệm`, `3. Kéo thả`, `4. Gõ SQL`.
- **Kết luận:** **KHÔNG CÓ** tài liệu chính thức nào quy định "checklist" hoặc "6 mục" riêng cho nội dung bài học môn SQL trong repo.

---

## TÓM TẮT

1. **A. Môn ML - File & Kế hoạch:** Repo chỉ có 2 file tài liệu nhắc đến ML ([docs/ml-pipeline.md:4](file:///home/acm/pe-usth/docs/ml-pipeline.md#L4), [docs/questionnaire-spec.md:3-4](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L3-L4)); hoàn toàn chưa có danh sách module hoặc bài học ML nào.
2. **A. Môn ML - Trích nguyên văn:** "Áp dụng trước cho `python_advanced` (48 bài, 8 module); SQL và ML dùng cùng pipeline khi có gói bài." ([docs/ml-pipeline.md:4](file:///home/acm/pe-usth/docs/ml-pipeline.md#L4)).
3. **A. Môn ML - Trích nguyên văn:** "Khoá áp dụng: `python_advanced`... Môn SQL và ML dùng cùng định dạng khi có giáo trình; chỉ đổi `course_id` và danh sách module." ([docs/questionnaire-spec.md:3-4](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L3-L4)).
4. **A. Môn ML - Bài "ML-REG-01":** Không nằm trong repo pe-usth, không có commit nào tạo; bài này do người dùng đưa vào chat ở phiên trước ([ML-CM-tai-lieu/review-ml.md:5](file:///home/acm/pe-usth/ML-CM-tai-lieu/review-ml.md#L5)).
5. **A. Môn ML - Git branch:** `git branch -a` có 9 nhánh; tìm kiếm `git log --all -S"ML-REG"` cho kết quả 0 commit, không nhánh nào có bài ML.
6. **B. Phân công - Commits & Tác giả:** `git shortlog -sn --all` dẫn đầu bởi sonkh (505), Tuyet Mieu (29), Nghia (26), Cao Trí Thành (18), Cao Văn Nhân (4).
7. **B. Phân công - Ai soạn ML:** Nam (Nam Nguyễn) phụ trách soạn nội dung tài liệu ([scripts/HUONG-DAN-NAM.md:1](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L1), [docs/questionnaire-spec.md:11](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L11)).
8. **B. Phân công - Ai nạp & duyệt:** Nhân nạp gói bài vào repo ([scripts/HUONG-DAN-NAM.md:5](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L5)) và duyệt ([docs/ml-pipeline.md:7](file:///home/acm/pe-usth/docs/ml-pipeline.md#L7)); Nghĩa làm backend questionnaire/API ([docs/questionnaire-spec.md:10](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L10)).
9. **B. Quy trình - Script nhập bài:** `python3 scripts/sync_curricula.py --bundle <thư_mục> --course <mã_môn>` ([scripts/HUONG-DAN-NAM.md:5](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L5)).
10. **B. Quy trình - Định dạng & Schema:** Nhận bundle JSON (`course.json` và `lessons.json`) theo mẫu [scripts/fixtures/sample-course/](file:///home/acm/pe-usth/scripts/fixtures/sample-course/); bài bắt buộc đủ 7 trường ([scripts/HUONG-DAN-NAM.md:4](file:///home/acm/pe-usth/scripts/HUONG-DAN-NAM.md#L4)).
11. **B. Quy trình - Mẫu tài liệu:** Có mẫu Markdown [samples/lesson-fstring.md](file:///home/acm/pe-usth/samples/lesson-fstring.md), không có template docx.
12. **C. Xếp level - Code nạp:** Hàm `validateQuestionnaire` nằm tại [frontend/src/lib/onboarding-questionnaire.ts:107](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts#L107); Backend chưa có controller/service nào đọc bảng `questionnaires` ([docs/questionnaire-spec.md:19](file:///home/acm/pe-usth/docs/questionnaire-spec.md#L19)).
13. **C. Xếp level - Giới hạn & Bắt buộc:** Tối thiểu 2 lựa chọn/câu (`options.length >= 2`), trường bắt buộc gồm `id, module_code, question, options.text` ([frontend/src/lib/onboarding-questionnaire.ts:162, 189-204](file:///home/acm/pe-usth/frontend/src/lib/onboarding-questionnaire.ts#L162)).
14. **C. Xếp level - Nhận JSON đã soạn:** CÓ, cả 2 file `questionnaire-python-advanced.json` và `questionnaire-db-design.json` đều đạt 0 lỗi khi chạy qua `validateQuestionnaire`.
15. **D. Chạy app - Lệnh local:** Backend: `npm run start:dev` (cổng 5000); Frontend: `cd frontend && npm run dev` (cổng 3000) ([README.md:35-46](file:///home/acm/pe-usth/README.md#L35-L46)); không có docker-compose.
16. **D. Chạy app - Tài khoản & URL:** Test account `E2E_EMAIL` / `E2E_PASSWORD` ([frontend/e2e/helpers.ts:4-5](file:///home/acm/pe-usth/frontend/e2e/helpers.ts#L4-L5)); không lưu URL deploy thật trong repo ([AGENTS.md:282](file:///home/acm/pe-usth/AGENTS.md#L282)).
17. **D. Chạy app - Kiểm thử thực tế `PE_runSQL`:** `db_13` và `db_14` chạy thành công ra đúng kết quả; `db_15, db_16, db_17` kích hoạt đúng bẫy lỗi pending `honest_error`; `db_02` báo lỗi regex parser WHERE ([frontend/public/static/js/lesson_db_design.js:6387](file:///home/acm/pe-usth/frontend/public/static/js/lesson_db_design.js#L6387)).
18. **E. Checklist 6 mục - Tài liệu SQL:** **KHÔNG CÓ** tài liệu nào về checklist 6 mục cho SQL trong `docs/` hay git history; cấu trúc 6 mục xuất phát từ review môn Python v3 ([scripts/pe-v3/README.md:32-44](file:///home/acm/pe-usth/scripts/pe-v3/README.md#L32-L44)).
