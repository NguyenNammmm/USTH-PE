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
    return new_state