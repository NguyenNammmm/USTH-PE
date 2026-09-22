# P24 - Capstone: Sổ học tập USTH

Dành cho giảng viên/dev; không gửi trước vào client challenge.

```python
from copy import deepcopy

def apply_action(state, action):
    new_state = deepcopy(state)
    kind = action.get("type")
    if kind in ("add_student", "add_course"):
        key = "students" if kind == "add_student" else "courses"
        ident, name = action.get("id"), action.get("name")
        if not isinstance(ident, str) or not ident.strip():
            raise ValueError("invalid id")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("invalid name")
        if ident in new_state[key]:
            raise ValueError("duplicate id")
        new_state[key][ident] = name
    elif kind == "set_mark":
        sid, cid = action.get("student_id"), action.get("course_id")
        score = action.get("score")
        if not isinstance(sid, str) or not isinstance(cid, str):
            raise ValueError("invalid reference")
        if sid not in new_state["students"] or cid not in new_state["courses"]:
            raise ValueError("unknown reference")
        if type(score) not in (int, float) or not (0 <= score <= 10):
            raise ValueError("invalid score")
        new_state["marks"].setdefault(sid, {})[cid] = score
    else:
        raise ValueError("unknown action")
    return new_state```

## Đáp án kiểm tra hiểu

1. Nhập điểm cho S99 chưa có nên làm gì?

Đáp án: Từ chối, giữ nguyên state

- Tự tạo sinh viên vô danh: Đề yêu cầu sinh viên tồn tại trước.
- Từ chối, giữ nguyên state: Đúng: không tạo bản ghi mồ côi.
- Ghi điểm rồi báo lỗi: Báo lỗi sau khi ghi vẫn làm dữ liệu sai.

2. Mã môn PY tồn tại, nhập điểm mới cho cùng sinh viên/PY thì sao?

Đáp án: Cập nhật điểm cũ

- Tạo một môn thứ hai: Không tạo bản ghi trùng cặp.
- Cấm mọi thay đổi: Bài có chức năng sửa điểm.
- Cập nhật điểm cũ: Đúng: cùng cặp định danh thì cập nhật theo hợp đồng.

