# Đặc tả nội dung Machine Learning PE

Tài liệu này áp dụng cấu trúc có thật của khóa Python. ML không tạo schema mới:
mỗi bài dùng `studio-lesson/v2`, type và renderer hiện có của StudioLesson.

## 1. Phân biệt ba lớp quy tắc

### Bắt buộc bởi validator hiện tại

- `content_json` phải là object, có `title` không rỗng và ít nhất một trong
  `step_1`–`step_4` có nội dung.
- Nếu có `step_1.predict`: cần ít nhất hai lựa chọn và phải đánh dấu đáp án đúng.
- Nếu có `step_2.mcq`: mỗi câu cần `question`, ít nhất hai lựa chọn và đáp án
  đúng bằng `correct` dạng chỉ số hoặc `option.correct: true`.
- Nếu có scaffold: `template` phải chứa `{{slotN}}`; mỗi slot có `n` và
  `answer`; danh sách slot không rỗng.
- Nếu có `step_4.tests`: mảng không rỗng. ML ưu tiên hợp đồng `call`/`expect`
  vì đây là dạng validator hiện kiểm trực tiếp.
- Nếu có `starterCode`, bài phải có tests để có thể nộp và chấm.
- `files` chỉ dùng tên file trơn và `content` dạng chuỗi.
- Nếu có theory: mỗi block có `title` và có `body` hoặc `bullets`.
- Figure phải là SVG cùng origin, có `src`, `caption` và `alt`.
- Nếu có `play`: `games` không rỗng, ID không trùng và type thuộc danh sách hệ
  thống. `fill` cần scaffold; `parsons` và `debug` cần tests;
  `selfExplain` cần `step_2.selfExplain`.

Validator không bắt buộc `schema`, subtitle, source, duration, XP hoặc đủ bốn
step. Khóa ML vẫn coi chúng là quy ước authoring bắt buộc dưới đây.

### Quy ước bắt buộc của khóa ML

- Record ngoài có `lesson_code`, `sort_order`, `module`, `title`, `subtitle`,
  `estimated_minutes`, `xp_reward`, `content_json`.
- `content_json.schema` luôn là `studio-lesson/v2`.
- Mã bài là `ML01`–`ML28`; thứ tự và module phải khớp `course.json`.
- Mỗi bài có đủ S1–S4. Ngoại lệ capstone/procedure phải được ghi rõ trong bài
  và test nội dung.
- `source` ghi nguồn bài giảng, trang/slide hoặc dataset; không ghi nguồn giả.
- Python 3.12; package chỉ khai khi sandbox thực sự cần tải.
- Thư viện ngoài Python chuẩn được phép trong nội dung là NumPy và pandas.
  Không dùng scikit-learn, TensorFlow hoặc PyTorch.
- Code, solution và test phải xác định; phép toán ngẫu nhiên phải có seed hoặc
  được kiểm bằng invariant ổn định.

### Khuyến nghị sư phạm, không phải yêu cầu schema

- Mở bài bằng một vấn đề dữ liệu hoặc lỗi kỹ thuật có thật.
- Yêu cầu dự đoán trước khi chạy code.
- Giải thích shape, đơn vị, quy ước làm tròn và dòng chảy dữ liệu.
- Dùng phương án nhiễu từ lỗi ML thật: leakage, sai axis/shape, sai metric,
  overfitting hoặc cập nhật gradient sai.
- Với dataset thật, ghi nguồn, giấy phép, đơn vị và giới hạn suy luận.
- Bài nâng cao giảm scaffold và tăng yêu cầu debug/tự giải thích.

## 2. Record bài học

```json
{
  "lesson_code": "ML01",
  "sort_order": 1,
  "module": "M1 · Cơ sở toán học, dữ liệu và tiền xử lý",
  "title": "ML01 · Biểu diễn dữ liệu dạng bảng và không gian vector",
  "subtitle": "Cơ bản · M1 · 30 phút",
  "estimated_minutes": 30,
  "xp_reward": 15,
  "content_json": {
    "schema": "studio-lesson/v2",
    "title": "ML01 · Biểu diễn dữ liệu dạng bảng và không gian vector",
    "subtitle": "Cơ bản · M1 · 30 phút",
    "source": {
      "kind": "pe-ml",
      "filename": "Giao_Trinh_Machine_Learning_PE.docx#ML01",
      "parser": "pe-ml-codex"
    },
    "step_1": {},
    "step_2": {},
    "step_3": {},
    "step_4": {},
    "play": {}
  }
}
```

Đây là khung cấu trúc, không phải nội dung hoàn chỉnh của ML01.

## 3. S1 — học khái niệm và dự đoán

Theo Python v4, S1 có thể gồm:

- `theory`: các khối `{title, body?, bullets?, figure?}`.
- `brief`: nhiệm vụ và ví dụ vào/ra.
- `context`: mức độ, kiến thức học trước và file cấp sẵn.
- `code`: ví dụ minh họa, không phải lời giải bài sandbox.
- `predict`: câu dự đoán có các option và đúng một đáp án.
- `misconception`: ngộ nhận phổ biến và lý do sai.
- `explain`: giải thích tuần tự kết quả hoặc bước chạy.
- `figure`: hình SVG có caption và alt.

Với cách trình bày dữ liệu/NumPy dài theo `pe-da`, có thể dùng `read` đã chia
thành nhiều màn. Không trộn `read` và theory chỉ để lặp lại cùng một nội dung.

## 4. S2 — đánh giá tư duy

Mỗi bài mặc định có ba MCQ, ba lựa chọn mỗi câu và đúng một đáp án. Mỗi lựa
chọn phải có `detail`; câu hỏi có `explanation` tổng kết.

```json
{
  "mcq": [
    {
      "question": "Câu hỏi kiểm tra một quyết định ML cụ thể?",
      "options": [
        {"text": "Phương án nhiễu", "detail": "Vì sao sai."},
        {"text": "Phương án đúng", "detail": "Vì sao đúng.", "correct": true},
        {"text": "Phương án nhiễu", "detail": "Vì sao sai."}
      ],
      "correct": 1,
      "explanation": "Nguyên tắc cần ghi nhớ."
    }
  ],
  "selfExplain": {
    "prompt": "Giải thích quyết định bằng lời của bạn.",
    "placeholder": "Nêu dữ liệu, phép biến đổi và hệ quả...",
    "rubric": [
      {"label": "Nêu đúng nguyên nhân", "keywords": ["..."]}
    ],
    "sample": "Lời giải thích mẫu chỉ hiện sau khi người học trả lời."
  }
}
```

## 5. S3 — ghép code nhiều slot

```json
{
  "task": {"title": "Hoàn thiện phép biến đổi", "body": "..."},
  "trace": {"steps": [{"label": "1", "text": "..."}]},
  "counter": {
    "question": "Nếu đổi điều kiện thì kết quả nào đúng?",
    "options": ["A", "B", "C"],
    "correct": "B"
  },
  "scaffold": {
    "template": "def transform(X):\n    a = {{slot1}}\n    return {{slot2}}",
    "slots": [
      {"n": 1, "placeholder": "Tính thống kê", "answer": "X.mean(axis=0)"},
      {"n": 2, "placeholder": "Biến đổi", "answer": "X - a"}
    ],
    "bank": [
      {"label": "X.mean(axis=0)", "slot": 1},
      {"label": "X - a", "slot": 2},
      {"label": "X.mean(axis=1)", "slot": 1, "trap": "Sai axis của đặc trưng."}
    ]
  }
}
```

Các slot có thể phụ thuộc nhau. `bank.slot` xác định vị trí đúng; `trap` giải
thích sai lầm, không chỉ báo “sai”. Bài gate không cấp scaffold.

## 6. S4 — sandbox và kiểm thử

```json
{
  "task": {
    "title": "Hiện thực hàm",
    "body": "Mô tả input, output, shape, dtype, làm tròn và edge case.",
    "io": [{"label": "Ví dụ", "value": "..."}]
  },
  "starterCode": "def solve(X):\n    pass\n",
  "solutionCode": "def solve(X):\n    return X\n",
  "hints": [
    {"title": "Gợi ý 1", "body": "Nhắc nguyên lý."},
    {"title": "Gợi ý 2", "body": "Nhắc bước trung gian."},
    {"title": "Gợi ý 3", "body": "Nhắc API hoặc shape, không chép lời giải."}
  ],
  "tests": [
    {"name": "Trường hợp cơ bản", "call": "solve(...) ", "expect": "..."},
    {"name": "Trường hợp biên", "call": "solve(...) ", "expect": "..."}
  ],
  "packages": ["numpy"]
}
```

Quy ước kiểm thử:

- Ưu tiên 6–8 test/bài; bài trọng tâm có thể nhiều hơn.
- Bao phủ shape, dtype, input nhỏ, trùng lặp, hằng số, NaN/rỗng nếu hợp đồng
  bài cho phép.
- Test phải bắt được các biến thể sai dùng trong `spotError`/`debug`.
- `solutionCode` phải qua toàn bộ test; starter và biến thể sai không được qua
  toàn bộ test.
- Ưu tiên `call`/`expect`. Chỉ dùng test dữ liệu `input`/`expected` sau khi
  pipeline validator tương ứng đã được xác nhận.

## 7. Mini-game được phép

Chỉ dùng tám type hệ thống đã hỗ trợ:

- `traceTable`
- `match`
- `trueFalse`
- `fill`
- `parsons`
- `spotError`
- `debug`
- `selfExplain`

Mỗi game có `id`, `type`, `title` và payload đúng type. Không thêm game type
mới trong giáo trình ML.

Luồng khuyến nghị:

- B: `match/traceTable → fill → spotError`.
- I: `match/traceTable → fill → parsons → spotError`.
- N: `match/traceTable → fill → spotError → debug → selfExplain`.
- Boss/capstone: `trueFalse → spotError → sandbox`, `gate: true`, không scaffold.

```json
{
  "level": "I",
  "boss": false,
  "games": [
    {"id": "fill-0", "type": "fill", "title": "Điền mảnh còn thiếu"}
  ],
  "selfExplainMinWords": 8
}
```

## 8. Checklist trước khi đưa vào bundle

1. Mã, module và thứ tự khớp `course.json`.
2. JSON hợp lệ và `schema` đúng v2.
3. Nguồn, công thức, số liệu và đáp án được đối chiếu với DOCX.
4. Mỗi MCQ có đúng một đáp án và phản hồi cho mọi lựa chọn.
5. Template chứa đủ placeholder của slot; bank có đáp án và bẫy hợp lý.
6. Starter, solution, hints, tests và package nhất quán.
7. Solution qua test; biến thể sai bị test bắt.
8. Game chỉ dùng type có sẵn và có dependency cần thiết.
9. Không nhúng đường dẫn tùy ý hoặc secret vào lesson JSON.
10. Chỉ sinh output vào `out/`; không sửa bundle bằng tay.
