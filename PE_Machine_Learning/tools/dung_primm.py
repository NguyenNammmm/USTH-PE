#!/usr/bin/env python3
"""Dựng bài Markdown và tệp Make. Dùng --check để kiểm đầu ra và chạy ca kiểm."""

import argparse
import contextlib
import io
import json
from pathlib import Path
from collections import defaultdict

import ban_doc as book
from lo_trinh import roadmap_md


ROOT = Path(__file__).resolve().parents[1]
CORE_IDS = [f"ML{i:02}" for i in range(1, 29)]
EXTRA_IDS = [f"MLP{i:02}" for i in range(1, 9)]


CHECK_HELPERS = '''def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)
'''


def read_json(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def bullets(tasks, code):
    return "\n".join(f"{i}. **{code}{i}** · {task}" for i, task in enumerate(tasks, 1))


def capture(code, lesson_id):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        exec(compile(code, f"{lesson_id} — Run", "exec"), {})
    return out.getvalue().strip()


def check_body(checks):
    functions = []
    for i, case in enumerate(checks, 1):
        body = "\n".join(f"    {line}" for line in case.splitlines())
        functions.append(f"def case_{i:02}():\n{body}")
    calls = ", ".join(f"case_{i:02}" for i in range(1, len(checks) + 1))
    functions.append(f"CASES = [{calls}]")
    return "\n\n\n".join(functions)


def starter_script(make):
    return f'''"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def {make["signature"]}:
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


{CHECK_HELPERS}

{check_body(make["checks"])}


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {{i}} chưa đạt · {{type(error).__name__}} · {{error}}")
        else:
            print(f"Ca {{i}} đạt")
    print(f"Đạt {{len(CASES) - failed}}/{{len(CASES)}} ca.")
    sys.exit(int(failed > 0))
'''


def verify_solution(lesson, script):
    make = lesson["make"]
    placeholder = (f'def {make["signature"]}:\n'
                   '    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")')
    source = script.replace(placeholder, make["solution"], 1)
    assert source != script, lesson["id"]
    env = {"__name__": "reference"}
    exec(compile(source, f'{lesson["id"]} — Make', "exec"), env)
    for i, case in enumerate(env["CASES"], 1):
        try:
            case()
        except Exception as err:
            raise AssertionError(f'{lesson["id"]} · Ca Make {i}') from err



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Đối chiếu tài liệu và chạy ca kiểm")
    checking=parser.parse_args().check
    course=read_json("source/course.json")
    core={x["id"]:x for x in course["lessons"]}
    rows=read_json("source/primm.json")["lessons"]
    assert [r["id"] for r in rows]==CORE_IDS+EXTRA_IDS
    questions=read_json("source/questions.json")["questions"]
    assert len(questions)==len({q["question_id"] for q in questions})==603
    assert sum(q["type"]=="mcq" for q in questions)==269
    bank=defaultdict(list)
    for q in questions:
        assert q["prompt"].strip()
        if q["type"]=="mcq":
            assert q["correctOption"] in {o["id"] for o in q["options"]}
        else:
            assert q["answer"].strip()
        bank[q["lesson_id"]].append(q)
    assert list(bank)==CORE_IDS
    examples=read_json("source/worked-examples.json")
    assert set(examples)=={r["id"] for r in rows}
    keys={}; starters={}; artifacts={}; index=0
    for module,count in book.MODULES:
        for r in rows[index:index+count]:
            r["module"]=module
        index+=count
    assert index==len(rows)
    for row in rows:
        c=row["id"];m=row["make"]
        row["beforeText"]=", ".join(core[c]["before"]) if c in core else row["after"]
        if not row["beforeText"]:row["beforeText"]="Tự kiểm đầu vào"
        row["prerequisites"]=core[c]["before"] if c in core else [row["after"]]
        keys[c]=book.key_for(row)
        row["workedExamples"]=book.worked_examples(row, examples[c])
        starters[c]=starter_script(m)
        verify_solution(row,starters[c])
        assert capture(row["code"],c)
        assert all(q in {x["question_id"] for x in bank.get(c,[])} for q in row["reviewIds"])
        assert all(len(row[stage])==count for stage,count in [("predict",2),("investigate",2),("modify",3)])
        artifacts["bai-hoc/"+c+".md"]=book.lesson_md(row,keys[c],local=True)
        artifacts["thuc-hanh/"+c+".py"]=starters[c]
        if c in bank:
            artifacts["on-tap/"+c+".md"]=book.bank_md(c,bank[c],local=True)
    directory="docs/PRIMM/"
    stem=directory+book.STEM
    artifacts[stem+".md"]=book.combined_md(rows,bank,keys)
    artifacts[stem+".html"]=book.page_html(rows,bank,keys,starters)
    artifacts[directory+"Lo-trinh-hoc.md"]="\n\n".join(roadmap_md(rows, standalone=True))+"\n"
    artifacts[directory+"README.md"]=book.reader_readme(rows)
    for path,contents in artifacts.items():
        dest=ROOT/path
        if checking:
            assert dest.read_text(encoding="utf-8")==contents, "Cần dựng lại "+path
        else:
            dest.parent.mkdir(exist_ok=True,parents=True)
            dest.write_text(contents,encoding="utf-8",newline="\n")
    total_checks=sum(len(r["make"]["checks"]) for r in rows)
    print(f"PRIMM_PASS · {len(rows)} phiếu · {len(questions)} câu ôn · {len(rows)*len(book.PANELS)} bộ dữ liệu · {sum(len(r['workedExamples']) for r in rows)} ví dụ mới · {total_checks} ca hàm")
if __name__=="__main__":
    main()
