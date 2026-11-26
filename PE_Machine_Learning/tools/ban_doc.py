"""Dựng cùng nội dung cho bản đọc Markdown, HTML và bản in từ HTML."""
import html
import json
import numbers
import re
from pathlib import Path

import numpy as np
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
STEM = "Machine-Learning-PE-PRIMM"
PANELS = ("B", "D1", "D2", "D3", "E1", "E2", "E3", "E4", "R1", "R2", "R3", "R4", "S")
MODULES = [
    ("Dữ liệu và tiền xử lý", 3), ("Hồi quy và tối ưu hóa", 5),
    ("Phân loại", 4), ("Đánh giá và điều chuẩn", 6),
    ("Mạng nơron", 4), ("Phân cụm, giảm chiều và tổ hợp mô hình", 6),
    ("Bài bổ sung", 8),
]
PROFILE = "Khóa này phù hợp với người đã học một học phần lập trình nhập môn, thường vào cuối năm nhất hoặc năm hai các ngành máy tính, dữ liệu và kỹ thuật. Đây là ước tính từ các thao tác trong bài. Để vào ML01, bạn nên tự viết được một hàm Python nhỏ, dùng danh sách, vòng lặp, điều kiện và đọc một thông báo lỗi. Với NumPy, hãy biết tạo mảng và lấy một hàng hay cột. Bạn sẽ học các thuật toán học máy (machine learning) qua từng phiếu."
LATER = "Trước ML05, hãy ôn đạo hàm của hàm bậc hai. Trước ML10–ML11 và ML22, cần đọc được phép nhân ma trận, đạo hàm sigmoid và quy tắc chuỗi. Trước ML25, ôn vectơ riêng và trị riêng. Các kỹ năng này có thể học dần theo lộ trình."
DIAG = [
    ("Viết hàm Python tính trung bình một danh sách số khác rỗng. Thử với [2,4,6].", "Hàm trả 4. Có thể dùng sum(xs) / len(xs)."),
    ("Với X = np.array([[1,4],[3,8],[5,2]]), ghi X.shape và X[:,1].tolist().", "Kích thước là (3,2), cột số 1 là [4,8,2]."),
    ("Tính tích vô hướng của [2,−1] và [3,4], rồi cộng 1.", "Tính 2×3 − 1×4 + 1 = 3."),
    ("Tại w = 2, đạo hàm của (w − 1)²/2 bằng bao nhiêu?", "Đạo hàm là w − 1, tại w = 2 bằng 1."),
]
WORKFLOW = "Ghi dự đoán ở A, chạy và sửa mã ở B, giải thích một phép tính ở C. Ba lượt D dùng lại cùng phương pháp. Đóng mẫu trước bốn đề E và nộp riêng từng kết quả. Bạn cũng tự viết một hàm để chạy các ca kiểm. Mở F khi đạt ít nhất 3/4 vị trí E, trong đó E2 bắt buộc đúng. Nếu đã xem đáp án, dùng bộ R cùng số để chứng minh lại. Đầu buổi sau, làm S từ đầu và ghi kết quả riêng."
INPUT_NOTE = "Khi nhập kết quả, dùng dấu chấm thập phân, ngoặc vuông cho vectơ, ma trận và các kết quả ghép. Dùng dấu ngoặc kép cho chuỗi và null cho giá trị không xác định. Với số thập phân dài, giữ ít nhất 7 chữ số sau dấu chấm. Riêng ML05, giữ đến 10 chữ số nếu cần."
GROUP_TEXT = "Dữ liệu mới nằm ngay trong mỗi đề. Nếu đề trả nhiều đại lượng, hãy nhập chúng theo đúng thứ tự trong yêu cầu."
GLOSS = [
("Mẫu (sample)","Một hàng dữ liệu."),("Đặc trưng (feature)","Một đại lượng dùng để mô tả mỗi mẫu."),
("Kích thước (shape)","Dãy độ dài các trục của mảng."),("Trục (axis)","Chiều được chọn khi lấy tổng hoặc trung bình."),
("Tập huấn luyện, xác thực, kiểm tra (train, validation, test)","Dùng lần lượt để học tham số, chọn cấu hình và đánh giá cuối."),
("Hệ số tự do (bias, intercept)","Số hạng được cộng vào điểm có trọng số."),("Gradient","Vectơ đạo hàm riêng của một đại lượng vô hướng."),
("Lô (batch)","Nhóm mẫu dùng trong một phép tính hay một lần cập nhật."),("Ngưỡng (threshold)","Mốc dùng để đưa ra quyết định."),
("Tổn thất (loss)","Đại lượng lượng hóa sai khác giữa dự đoán và mục tiêu."),("Tham số (parameter)","Đại lượng của mô hình có thể được ước lượng từ dữ liệu."),
("Siêu tham số (hyperparameter)","Cấu hình như tốc độ học, số láng giềng hoặc mức phạt."),
]
MD = MarkdownIt("commonmark", {"html": False, "linkify": False}).enable("table")
esc = html.escape

def json_value(x):
    if isinstance(x, np.ndarray):
        return json_value(x.tolist())
    if isinstance(x, (list, tuple)):
        return [json_value(v) for v in x]
    if isinstance(x, np.generic):
        return json_value(x.item())
    if isinstance(x, float):
        if not np.isfinite(x):
            raise ValueError(x)
        if abs(x) < 1e-13:
            return 0
        if abs(x - round(x)) < 1e-13:
            return int(round(x))
        return float(format(x, ".13g"))
    return x

def fmt(x):
    return json.dumps(x, ensure_ascii=False, separators=(",", ":"))

def check_equal(a, b):
    if isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
        return len(a) == len(b) and all(check_equal(x, y) for x, y in zip(a, b))
    if isinstance(a, numbers.Real) and isinstance(b, numbers.Real):
        return abs(a-b) < 1e-9
    return a == b

def key_for(row):
    env = {"np": np}
    sample_env = {"np": np}
    name = row["make"]["signature"].split("(")[0]
    exec(row["make"]["solution"], env)
    exec(row["exampleFunction"], sample_env)
    out = {}
    assert tuple(row["sets"]) == PANELS
    assert len({fmt(c) for c in row["sets"].values()}) == len(PANELS)
    for label, args in row["sets"].items():
        a = json_value(env[name](*args))
        b = json_value(sample_env[name](*args))
        assert check_equal(a, b), (row["id"], label, a, b)
        out[label] = a
    return out

def call_args(row, key):
    return "  ".join(f"{k} = {fmt(v)}" for k,v in zip(row["parameters"], row["sets"][key]))

def codeblock(s):
    return "<pre><code>"+esc(s)+"</code></pre>"

def rich(s):
    return MD.render(s)

def safe_json(o):
    return json.dumps(o, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")

def hints(row):
    return row["feedback"]

def prompt_md(r, key):
    text = f'**{key}** · `{call_args(r,key)}`'
    if key[0] in ("E","R","S"):
        return text + "  \nKết quả tự nộp ____________________"
    return text

def answer_md(q):
    if q["type"] == "practice":
        return q["answer"]
    correct = q["correctOption"].upper()
    feedback = "\n".join(f'- {o["id"].upper()} · {o["feedback"]}' for o in q["options"] if o.get("feedback"))
    return f'**Chọn {correct}.** {q["explanation"]}\n\n{feedback}'

def question_md(q):
    text=q["prompt"]
    if q["type"]=="mcq":
        text+="\n\n"+"\n".join(f'- {opt["id"].upper()} · {opt["text"]}' for opt in q["options"])
    return text

def cases_md(row, key):
    return "\n\n".join(f'**{stage}** · `{fmt(key[stage])}`' for stage in PANELS)

def tol(row):
    return "10⁻⁹" if row["id"] == "ML05" else "10⁻⁶"

def links_md(row, local):
    if not row.get("reviewIds"): return ""
    return "Ôn cùng thao tác · " + " · ".join(f'[{x}]('+("../on-tap/"+row["id"]+".md" if local else "")+"#"+x.lower()+")" for x in row["reviewIds"])

def lesson_md(r, keys, local=False):
    c = r["id"]; m=r["make"]; lower=c.lower()
    keylink=("#doi-chieu" if local else "#dap-an-"+lower)
    starter_relative = "../" if local else "../../"
    out=[f'<a id="{lower}"></a>\n\n'+('#' if local else '##')+f' {c} · {r["title"]}',r["goal"],"Tiên quyết · "+r["beforeText"]]
    if r["bridge"]:out.append(r["bridge"])
    out.extend(["### A · Dự đoán","\n".join(f'{i}. {v}' for i,v in enumerate(r["predict"],1)),"### B · Chạy mẫu",
                f'```python\n{r["code"]}\n```',f'Ghi đầu ra dự đoán trước khi chạy. [Đối chiếu lượt B]({keylink})',
                "### C · Lần theo mã","\n".join(f'{i}. {v}' for i,v in enumerate(r["investigate"],1)),
                "### D · Thử ba thay đổi","Mỗi lần bắt đầu lại từ B. Thay dữ liệu như dưới đây, dự đoán kết quả, rồi chạy để so.",
                *[r["modify"][i]+"  \n"+prompt_md(r,f'D{i+1}') for i in range(3)],
                "### E · Tự giải và viết hàm",GROUP_TEXT+" Đóng mã B. Ghi một kết quả cho từng đề trước khi xem đáp án. Dung sai tuyệt đối "+tol(r)+".",
                *[prompt_md(r,'E'+str(i)) for i in range(1,5)],
                f'**Viết mã.** Viết hàm `{m["signature"]}`. {m["task"]} [Tệp điền mã]({starter_relative}thuc-hanh/{c}.py).',
                "Đạt ít nhất 3/4 vị trí, trong đó vị trí 2 bắt buộc đúng. Sau khi đã xem đáp án Ei, dùng Ri để kiểm lại cùng vị trí.",
                "#### Bộ số để làm lại",*[prompt_md(r,'R'+str(i)) for i in range(1,5)],
                "### F · Vận dụng sau mốc đạt",m["extension"],"### Buổi sau · Kiểm lại",
                "Che mẫu và lời giải. Nộp kết quả, ghi ngày và ghi đúng hoặc cần ôn cho lượt này riêng với E.",("[Mở bộ S của "+c+"]("+("../docs/PRIMM/"+STEM+".md" if local else "")+"#kiem-lai-"+lower+")"),links_md(r,local)])
    if local:
        out.insert(1, '[Về mục lục](../README.md)')
        out.extend(['<a id="doi-chieu"></a>\n\n### Đối chiếu sau khi đã nộp',cases_md(r,keys),r["reasoning"],r["feedback"],"**Vận dụng.** "+r["transferKey"],
                    f'```python\nimport numpy as np\n\n{m["solution"]}\n```'])
    return "\n\n".join(x for x in out if x)+"\n"

def bank_md(code,qs,local=False):
    key="#loi-giai" if local else "#loi-giai-ngan-hang"
    sections=[f'<a id="on-{code.lower()}"></a>\n\n## Ôn tập {code}',f'Ghi câu trả lời trước khi [mở phần giải]({key}).']
    for q in qs:
        sections.append(f'<a id="{q["question_id"].lower()}"></a>\n\n### {q["question_id"]}\n\n'+question_md(q))
    if local:
        sections.append('<a id="loi-giai"></a>\n\n## Đáp án')
        for q in qs:sections.append(f'### {q["question_id"]} · Đối chiếu\n\n'+answer_md(q))
    return "\n\n".join(sections)+"\n"

def intro_md():
    return ["# Machine Learning PE · Thực hành PRIMM","36 phiếu · 28 bài chính và 8 bài bổ sung · 603 câu ôn tập",
            "## Trước khi bắt đầu",PROFILE,LATER,"### Tự kiểm đầu vào",
            *[f'{i}. {s}' for i,(s,_) in enumerate(DIAG,1)],
            "Nếu tự làm được ba câu đầu, hãy bắt đầu ML01. Nếu còn vướng Python hoặc mảng, ôn lại kỹ năng tương ứng. Câu 4 giúp bạn chuẩn bị cho ML05.",
            "## Cách học",WORKFLOW,INPUT_NOTE.replace(';','.'),"### Thuật ngữ dùng trong phiếu",
            *[f'- **{t}** · {d}' for t,d in GLOSS]]

def combined_md(rows, bank, keys):
    out=intro_md()+["## Mục lục"]
    out+= [f'- [{r["id"]} · {r["title"]}](#{r["id"].lower()})'+(f' · [Câu ôn](#on-{r["id"].lower()})' if r["id"] in bank else '') for r in rows]
    out.append('[Đề kiểm lại ở buổi sau](#kiem-lai) · [Đối chiếu bài và tài liệu USTH](#doi-chieu)')
    out+=["Ghi câu trả lời trước khi mở [đáp án phiếu](#dap-an-phieu) hoặc [đáp án ngân hàng](#loi-giai-ngan-hang)."]
    out += [lesson_md(r,keys[r["id"]]) for r in rows]
    out += [bank_md(c,qs) for c,qs in bank.items()]
    out += ['<a id="kiem-lai"></a>\n\n# Kiểm lại ở buổi sau', 'Mở đúng mã bài vào buổi học tiếp theo. Ghi ngày, tự tính khi đã đóng mẫu rồi mới đối chiếu ở phụ lục đáp án.']
    for r in rows:
        c=r["id"]
        out.extend([f'<a id="kiem-lai-{c.lower()}"></a>\n\n### {c} · {r["title"]}',r["goal"],prompt_md(r,"S")])
    out += ['<a id="dap-an-phieu"></a>\n\n# Đáp án các phiếu',"## Tự kiểm đầu vào",*[f'{i}. {a}' for i,(_,a) in enumerate(DIAG,1)]]
    for r in rows:
        c=r["id"];m=r["make"]
        out.extend([f'<a id="dap-an-{c.lower()}"></a>\n\n## {c} · Đối chiếu',cases_md(r,keys[c]),r["reasoning"],r["feedback"],"**F.** "+r["transferKey"],"### Hàm tham khảo",f'```python\nimport numpy as np\n\n{m["solution"]}\n```',"### Ca kiểm hàm",*[f'```python\n{v}\n```' for v in m["checks"]]])
    out+=['<a id="loi-giai-ngan-hang"></a>\n\n# Đáp án ngân hàng']
    for c,qs in bank.items():
        out.append("## Ôn tập "+c+" · Lời giải")
        out += [f'### {q["question_id"]} · Đối chiếu\n\n'+answer_md(q) for q in qs]
    out.extend(['<a id="doi-chieu"></a>\n\n# Đối chiếu tài liệu USTH', 'Bản đối chiếu sau ghi nhận phạm vi của nguồn trước lần biên tập này.', (ROOT/'docs/DOI-CHIEU-DRIVE.md').read_text('utf-8').replace('](../', '](../../').rstrip()])
    return "\n\n".join(out)+"\n"


def submission(row, label):
    code=row["id"]
    caption={"E":"Tự giải","R":"Làm lại","S":"Buổi sau"}[label[0]]
    return f'''<div class="exercise" data-set="{label}"><h4>{label} <span>{caption}</span></h4><div class="args">{esc(call_args(row,label))}</div>
    <form class="web setform"><label>Kết quả của bạn<input name="answer" autocomplete="off" spellcheck="false" placeholder="Nhập kết quả theo đề"></label><button type="submit">Nộp kết quả</button></form>
    <div class="web result" aria-live="polite"></div><button type="button" class="plain web reveal" hidden>Xem cách đối chiếu</button>
    <div class="paper write-line">Kết quả __________________________</div></div>'''

def edit_box(row, kind):
    c=row["id"]
    name="Mã chạy mẫu" if kind=="sample" else "Hàm bạn viết"
    return f'''<div class="web editor" data-editor="{kind}"><label>{name}<textarea spellcheck="false" aria-label="{name} của {c}"></textarea></label>
    <div class="buttons"><button type="button" data-action="run">{'Chạy mã' if kind=='sample' else 'Chạy ca kiểm'}</button>
    <button type="button" class="secondary" data-action="save">Tải mã .py</button></div><pre class="console" aria-live="polite" hidden></pre></div>'''

def numbered(items):
    return "<ol>"+"".join("<li>"+esc(item)+"</li>" for item in items)+"</ol>"

def sheet_html(r, keys):
    c=r['id'];m=r['make']; stage=lambda id,label,title: f'<h3 id="{c}-{id}"><span>{label}</span>{title}</h3>'
    s=[f'<article class="panel sheet" id="{c}" data-course="{c}"><header class="title"><p>{c} · {esc(r["module"])}</p><h2>{esc(r["title"])}</h2></header>',
       f'<p class="prereq">Tiên quyết · {esc(r["beforeText"])}</p><p class="contract">{esc(r["goal"])}</p>']
    if r["bridge"]:s.append('<p class="bridge">'+esc(r["bridge"])+'</p>')
    s+=[stage('A','A','Dự đoán'),numbered(r["predict"]),'<label class="web note">Dự đoán của bạn<textarea data-note="predict" rows="2"></textarea></label><p class="web prediction-msg" aria-live="polite"></p>',
        stage('B','B','Chạy mẫu'),'<p>Ghi dự đoán trước. Chạy đoạn mã, rồi so kết quả theo từng vị trí.</p>', '<div class="paper">'+codeblock(r['code'])+'</div>','<details class="web sample-code" open><summary>Mã Python của lượt B</summary>'+edit_box(r,'sample')+'</details>',
        f'<details class="web sample-result"><summary>Đối chiếu mẫu B</summary><p>{esc(r["reasoning"])}</p>{codeblock(fmt(keys["B"]))}</details>',
        stage('C','C','Lần theo mã'),numbered(r["investigate"]),'<label class="web note">Phép tính hoặc dòng mã bạn muốn ghi lại<textarea data-note="trace" rows="2"></textarea></label>',
        stage('D','D','Thử ba thay đổi'),'<p>Bắt đầu lại từ B cho mỗi lượt. Ghi dự đoán rồi thay dữ liệu, chạy và kiểm lại.</p>']
    for i in range(1,4):
        label=f'D{i}';s.append(f'<div class="exercise guided" data-d="{label}"><h4>{label} <span>{esc(r["modify"][i-1])}</span></h4><div class="args">{esc(call_args(r,label))}</div><label class="web note">Dự đoán cho {label}<input data-note="{label}" autocomplete="off"></label><button class="web secondary" type="button" data-load="{label}">Đưa {label} vào ô chạy</button></div>')
    s += [stage('E','E','Tự giải và viết hàm'),f'<p>{GROUP_TEXT} Đóng mẫu trước khi tính. Dung sai tuyệt đối {tol(r)}. <a href="#format" class="web">Cách nhập kết quả</a></p>',
          '<div class="decks">'+''.join(submission(r,'E'+str(i)) for i in range(1,5))+'</div>',
          '<p class="gate" aria-live="polite">Mốc mở F · Đạt ít nhất 3/4 vị trí, gồm vị trí 2. Ei hoặc Ri có thể xác nhận vị trí i.</p>',
          '<details class="repairs"><summary>Bốn bộ làm lại · R1–R4</summary><p>Đã xem đáp án Ei? Thử Ri ở cùng vị trí với dữ liệu mới. Một vị trí được tính tối đa một lần. Ở Ri, bạn có thể sửa kết quả và thử tiếp trước khi mở đáp án.</p><div class="decks">'+''.join(submission(r,'R'+str(i)) for i in range(1,5))+'</div></details>',
          '<h4 class="sub">Viết và sửa mã</h4>',f'<p><code>{esc(m["signature"])}</code></p><p>{esc(m["task"])}</p>',
          f'<p>Tự viết hàm và chạy {len(m["checks"])} ca kiểm. Ghi lỗi đầu tiên tìm được rồi thử lại.</p>',edit_box(r,'make'),
          stage('F','F','Vận dụng sau mốc đạt'),'<div class="web locked-note">Hoàn thành mốc ở E để mở bài vận dụng.</div>',
          '<div class="transfer"><p>'+esc(m["extension"])+'</p><label class="web note">Lời giải vận dụng<textarea data-note="transfer" rows="3"></textarea></label><button type="button" class="web" data-action="finish-f">Nộp bài vận dụng</button><p class="web f-status" aria-live="polite"></p><details class="web f-key" hidden><summary>Đối chiếu sau khi làm F</summary><p>'+esc(r["transferKey"])+'</p></details></div>',
          stage('S','S','Kiểm lại ở buổi sau'),'<p>Làm từ đầu khi đã đóng mẫu. Kết quả được ghi riêng với điểm E.</p>','<div class="paper"><p>Đến phần <a href="#sp-'+c+'">Đề S · '+c+'</a> ở phụ lục dành cho buổi sau.</p></div><details class="web future"><summary>Bắt đầu lượt S vào buổi sau</summary>'+submission(r,'S')+'</details>']
    if r.get("reviewIds"):s.append('<p class="related">Ôn cùng thao tác · '+' · '.join(f'<a href="#{id}">{id}</a>' for id in r["reviewIds"])+'</p>')
    s.append('<p class="web"><a href="#start">Về lộ trình</a></p></article>')
    return ''.join(s)

def bank_html(code, qs, title):
    out=[f'<article class="panel bank" id="on-{code}"><header class="title"><p>Ôn tập · {code}</p><h2>{esc(title)}</h2></header><p>Trả lời từng câu trước khi mở phản hồi. Với câu tự luận, lưu bài làm rồi đối chiếu từng bước.</p>']
    for q in qs:
        id=q["question_id"]
        out.append(f'<section class="bankq" id="{id}" data-q="{id}"><h4>{id}</h4><p>{esc(q["prompt"])}</p><form>')
        if q["type"]=="mcq":
            for o in q["options"]:
                out.append(f'<label class="choice"><input class="web" type="radio" name="{id}" value="{o["id"]}"><span>{o["id"].upper()}.</span> {esc(o["text"])}</label>')
        else:out.append('<label class="web note">Bài làm của bạn<textarea rows="2" name="attempt"></textarea></label>')
        out.append('<button class="web" type="submit">Nộp câu trả lời</button></form><div class="web q-output" aria-live="polite"></div></section>')
    return ''.join(out)+'</article>'

def printable_key(r, keys):
    c=r["id"];m=r["make"]
    result=[f'<article class="paper print-key"><header class="title"><p>Đáp án phiếu · {c}</p><h2>{esc(r["title"])}</h2></header><p>{esc(r["reasoning"])}</p>']
    result.append('<table><thead><tr><th>Lượt</th><th>Kết quả đối chiếu</th></tr></thead><tbody>')
    for label in PANELS:result.append(f'<tr><td>{label}</td><td><code>{esc(fmt(keys[label]))}</code></td></tr>')
    result.extend(['</tbody></table><p>'+esc(r["feedback"])+'</p>','<h4>Vận dụng</h4><p>'+esc(r["transferKey"])+'</p>',
                   '<h4>Hàm tham khảo</h4>',codeblock('import numpy as np\n\n'+m["solution"]),'<h4>Ca kiểm hàm</h4>'])
    for n,case in enumerate(m["checks"],1):
        result.append('<div class="testcase"><b>Ca '+str(n)+'</b>'+codeblock(case)+'</div>')
    return ''.join(result)+'</article>'

def contents(rows):
    items=[];a=0
    for mod,n in MODULES:
        items.append('<section class="group"><h3>'+esc(mod)+'</h3><ul>'+''.join('<li><a href="#'+r["id"]+'"><b>'+r["id"]+'</b> '+esc(r['title'])+'</a></li>' for r in rows[a:a+n])+'</ul></section>')
        a+=n
    return ''.join(items)

def page_html(rows, bank, keys, starters):
    css=(ROOT/'tools/ban_doc.css').read_text('utf-8');js=(ROOT/'tools/ban_doc.js').read_text('utf-8')
    formats=INPUT_NOTE.replace(';','.')
    main=['<article id="start" class="panel intro"><header class="cover"><p>Programming Education · USTH</p><h1>Thực hành<br>Machine Learning</h1><p class="deck">36 phiếu PRIMM · 603 câu ôn tập</p></header><h2>Trước khi bắt đầu</h2><p>'+PROFILE+'</p><p>'+LATER+'</p>',
          '<h3>Tự kiểm đầu vào</h3>'+numbered([q for q,_ in DIAG]),
          '<p>Nếu tự làm được ba câu đầu, hãy bắt đầu ML01. Câu 4 giúp bạn chuẩn bị cho ML05.</p><details class="web"><summary>Đối chiếu đầu vào</summary>'+numbered([a for _,a in DIAG])+'</details>',
          '<h3>Cách học một phiếu</h3><p>'+WORKFLOW+'</p><p class="web">Trình duyệt lưu bài làm trên thiết bị này. Phần nộp kết quả dùng được khi mở tệp cục bộ. Lần đầu chạy Python cần Internet để tải Python và NumPy. Bạn cũng có thể tải mã và chạy trên máy.</p>',
          '<h3 id="format">Cách nhập kết quả</h3><p>'+formats+' Ví dụ một cặp số viết [1.25,0.65].</p>',
          '<details class="terms"><summary>Thuật ngữ dùng trong phiếu</summary><dl>'+''.join('<dt>'+esc(t)+'</dt><dd>'+esc(d)+'</dd>' for t,d in GLOSS)+'</dl></details>',
          '<section class="toc" id="toc"><h2>Lộ trình 36 phiếu</h2><div>'+contents(rows)+'</div></section></article>']
    for r in rows:main.append(sheet_html(r,keys[r["id"]]))
    byid={r['id']:r for r in rows}
    for c,qs in bank.items():main.append(bank_html(c,qs,byid[c]['title']))
    main.append('<article class="paper followups"><header class="title"><p>Luyện cách quãng</p><h2>Đề kiểm lại ở buổi sau</h2></header><p>Phát riêng mã bài đã học. Ghi ngày, làm khi đã đóng mẫu, rồi mới đối chiếu ở phụ lục đáp án.</p>')
    for r in rows:
        c=r["id"]
        main.append(f'<section class="sp-case" id="sp-{c}"><h4>{c} · {esc(r["title"])}</h4><p>{esc(r["goal"])}</p><div class="args">{esc(call_args(r,"S"))}</div><p>Ngày __________　Kết quả __________________________________</p></section>')
    main.append('</article>')
    main.append('<article class="paper print-key"><header class="title"><p>Đối chiếu sau khi nộp</p><h2>Đáp án tự kiểm đầu vào</h2></header>'+numbered([a for _,a in DIAG])+'</article>')
    for r in rows:main.append(printable_key(r,keys[r["id"]]))
    for c,qs in bank.items():
        main.append(f'<article class="paper bank-key"><header class="title"><p>Đáp án ngân hàng · {c}</p><h2>{esc(byid[c]["title"])}</h2></header>')
        for q in qs:main.append(f'<section class="answer"><h4>{q["question_id"]}</h4>'+rich(answer_md(q))+'</section>')
        main.append('</article>')
    crosswalk=(ROOT/'docs/DOI-CHIEU-DRIVE.md').read_text('utf-8').replace('](../', '](../../').rstrip()
    main.append('<article id="doi-chieu" class="panel sources"><header class="title"><p>Học liệu USTH</p><h2>Đối chiếu tài liệu giảng dạy</h2></header><p>Bản đối chiếu ghi nhận phạm vi của nguồn trước lần biên tập này.</p>'+rich(crosswalk)+'</article>')
    data={"lessons":{},"questions":{}}
    for r in rows:
        c=r["id"]
        data["lessons"][c]={"keys":keys[c],"sets":r["sets"],"parameters":r["parameters"],"function":r["exampleFunction"],"sample":r["code"],"starter":starters[c],"name":r["make"]["signature"].split("(")[0],"hint":r["feedback"],"general":r["hintGeneral"]}
    for qs in bank.values():
        for q in qs:
            entry={"type":q["type"],"answer":rich(answer_md(q))}
            if q["type"]=="mcq":entry.update(correct=q["correctOption"],notes={o["id"]:o["feedback"] for o in q["options"]})
            data["questions"][q["question_id"]]=entry
    nav='<option value="start">Bắt đầu và lộ trình</option><option value="doi-chieu">Đối chiếu tài liệu USTH</option>'+''.join('<option value="'+r['id']+'">'+r['id']+' · '+esc(r['title'])+'</option>' for r in rows)+'<optgroup label="Ngân hàng câu hỏi">'+''.join(f'<option value="on-{c}">Ôn tập {c}</option>' for c in bank)+'</optgroup>'
    return '<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Machine Learning PE · Thực hành PRIMM</title><style>'+css+'</style></head><body><header class="toolbar web"><a href="#start">Machine Learning PE</a><label><span class="sr">Chọn bài</span><select id="route">'+nav+'</select></label><button type="button" class="secondary" id="print">In giáo trình</button></header><main>'+''.join(main)+'</main><script type="application/json" id="course-data">'+safe_json(data)+'</script><script>'+js+'</script></body></html>\n'


def reader_readme(rows):
    return f"""# Machine Learning PE · Bộ học liệu PRIMM

Bộ học liệu có 28 bài chính và 8 bài bổ sung. Các phiếu dùng số, ma trận, nhãn và đoạn mã ngắn. Bạn có thể đưa từng câu vào một hoạt động tương tác trong PE.

| Tệp | Cách dùng |
|---|---|
| [Bản HTML]({STEM}.html) | Chọn phiếu, dự đoán, sửa và chạy mã Python, nộp kết quả, xem phản hồi. |
| [Bản PDF]({STEM}.pdf) | In trang đề trước. Bộ S dành cho buổi sau có phụ lục đề riêng. Hai phần đáp án nằm sau phụ lục ấy. |
| [Bản Markdown]({STEM}.md) | Chỉnh nội dung, tìm theo mã câu và tra đáp án trong phụ lục. |

## Trình độ đầu vào ước tính

{PROFILE}

{LATER}

## Một lượt học

{WORKFLOW}

- **A–C** · Ghi dự đoán, chạy đoạn mã mẫu và giải thích một giá trị bằng phép tính.
- **D** · Làm ba lần với đề cố định. Nút đưa D vào ô chạy thay các đối số bằng bộ số của lượt đang chọn.
- **E** · Mỗi đề E1–E4 nhận một kết quả riêng. Viết thêm hàm Python và chạy các ca kiểm. Việc viết hàm có thể thực hiện trong trình duyệt hoặc bằng tệp tải xuống.
- **Làm lại** · Sau khi mở đáp án, thử Ri ở cùng vị trí với Ei. Mỗi vị trí được tính một lần. Phản hồi chỉ ra phép tính, trục hoặc quy ước cần kiểm.
- **F và S** · Khi đủ ba vị trí và đạt vị trí 2, phần vận dụng mở ra. Dành bộ S cho buổi sau và ghi kết quả riêng với E.

{INPUT_NOTE.replace(';','.')}

## Ngân hàng ôn tập

603 câu được gắn mã theo 28 bài chính, gồm 269 câu trắc nghiệm và 334 câu tự luận hoặc viết mã. Tám bài bổ sung có các lượt D, E, R, S, phần viết hàm và bài vận dụng riêng. HTML hiện phản hồi sau lần nộp. Câu tự luận dùng lời giải để người học tự đối chiếu.

## Chạy Python

Thiết kế tham chiếu thao tác ghi dự đoán, xem kết quả và thử mã trong [bài Python của PE](https://www.programmingedu.io.vn/lesson/python_advanced?lesson=1).

Trình duyệt tải Pyodide 0.27.7 và NumPy ở lần chạy đầu. Trình duyệt lưu tiến độ và mã đã sửa trên thiết bị qua localStorage. Khi mở PDF hoặc Markdown, hãy ghi đáp án từng lượt vào phiếu riêng trước khi tra phụ lục. Có thể cài NumPy trên máy và tải tệp Python từ ô viết mã để làm việc ngoại tuyến.

## Quy mô và quy ước

Có 108 lượt D, 144 đề E, 144 đề làm lại R, 36 đề S và {sum(len(r['make']['checks']) for r in rows)} ca kiểm hàm. Emulate AI đã trả về 92 đoạn gợi ý cho lời dẫn của 36 phiếu và phần đề của toàn bộ 603 câu. Bản cuối đã được biên tập tiếng Việt, đối chiếu công thức, dữ liệu và quy ước trả lời. Đáp án số trên mỗi phiếu được tính lại bằng NumPy. Các thống kê này mô tả thiết kế học liệu. Điểm E và kết quả S sau một khoảng nghỉ là hai số đo nên thu riêng khi thử nghiệm với người học.
"""
