"""Lộ trình học và các ví dụ bổ sung trong từng phiếu PRIMM."""
from html import escape

LANES = (
    ("Nền tảng dữ liệu", "ML01 ML02 ML03 MLP01"),
    ("Hồi quy và tối ưu", "ML01 ML04 ML05 ML06"),
    ("Hồi quy đa biến", "ML04 ML05 ML07 ML08"),
    ("Logistic và Newton", "ML04 ML09 ML10 ML11"),
    ("Phân loại theo khoảng cách", "ML01 ML12"),
    ("Đánh giá hồi quy", "ML04 ML14"),
    ("Đánh giá phân loại", "ML09 ML15 ML16"),
    ("Chọn và điều chuẩn mô hình", "ML13 ML17 ML18"),
    ("Lọc đặc trưng", "ML17 MLP02"),
    ("Mạng nơron", "ML09 ML19 ML20 ML21 ML22"),
    ("Biên phân loại", "ML19 MLP05"),
    ("Phân cụm và đánh giá", "ML01 ML23 ML24 MLP08"),
    ("Phân cụm mở rộng", "ML23 MLP03", "ML23 MLP04", "ML23 MLP07"),
    ("Giảm chiều", "ML02 ML25 MLP06"),
    ("Cây và tổ hợp", "ML01 ML26 ML27"),
    ("Bài tổng hợp", "ML28"),
)
SHORT = (
    "Dữ liệu theo hàng", "Hiệp phương sai", "Chuẩn hóa", "Tổn thất hồi quy", "Hạ gradient",
    "Chia lô", "Hồi quy đa biến", "Đặc trưng đa thức", "Sigmoid và nhãn", "BCE và gradient",
    "Bước Newton", "k láng giềng", "Kiểm định K phần", "Chỉ số hồi quy", "Chỉ số phân loại",
    "Đường ROC", "Chọn bậc", "Ridge", "Perceptron", "ReLU", "Lan truyền tiến",
    "Lan truyền ngược", "K-means", "Rand và Jaccard", "PCA", "Chia theo Gini",
    "Bỏ phiếu OOB", "Chuỗi hồi quy", "Mã hóa một-nóng", "Lọc phương sai",
    "Phân cụm phân cấp", "DBSCAN", "SVM", "SVD", "SOM", "Davies–Bouldin",
)
GUIDE = "Bắt đầu bằng bài tự kiểm đầu vào và ML01, rồi chọn tuyến theo mục tiêu học. Mũi tên chỉ thứ tự trong từng tuyến. Mỗi ô ghi đủ các mã cần học trước, kể cả bài ở tuyến khác. Mã MLP là bài bổ sung."


def course_routes(rows):
    names = {row["id"]: name for row, name in zip(rows, SHORT, strict=True)}
    by_id = {row["id"]: row for row in rows}
    assert {code for _, *paths in LANES for path in paths for code in path.split()} == set(names)
    return names, by_id


def roadmap_md(rows, standalone=False):
    names, by_id = course_routes(rows)
    heading = "# Sơ đồ lộ trình học" if standalone else "## Sơ đồ lộ trình học"
    graph = ["```mermaid", "flowchart LR", '    START["Tự kiểm đầu vào"]']
    for row in rows:
        code = row["id"]
        graph.append(f'    {code}["{code} · {names[code]}"]')
    for row in rows:
        code = row["id"]
        for need in row["prerequisites"] or ["START"]:
            graph.append(f"    {need} --> {code}")
    graph.extend(["    classDef elective fill:#f4ead4,stroke:#9d783a,color:#392a13",
                  "    class " + ",".join(r["id"] for r in rows if r["id"].startswith("MLP")) + " elective",
                  "```"])
    lines = [heading, "Mỗi mũi tên trong sơ đồ nối một bài tiên quyết với bài sử dụng kiến thức đó. Các ô màu vàng là bài bổ sung.", "\n".join(graph), "### Các tuyến học"]
    for label, *paths in LANES:
        links = []
        for sequence in paths:
            nodes = []
            for code in sequence.split():
                dest = f"../../bai-hoc/{code}.md" if standalone else f"#{code.lower()}"
                nodes.append(f"[{code} {names[code]}]({dest})")
            links.append(" → ".join(nodes))
        lines.append(f"- **{label}** · " + " / ".join(links))
    lines.append("Để vào ML28, hoàn thành ML03, ML07, ML09, ML13 và ML15.")
    return lines


def roadmap_html(rows):
    names, by_id = course_routes(rows)
    out = ['<article id="lo-trinh" class="panel roadmap"><header class="title"><h2>Sơ đồ lộ trình học</h2></header>',
           '<p>'+GUIDE+'</p><p class="road-start"><a href="#start">Tự kiểm đầu vào</a> → <a href="#ML01">ML01 · Dữ liệu theo hàng</a></p>']
    for label, *paths in LANES:
        out.append(f'<section class="road-lane"><h3>{escape(label)}</h3>')
        for path in paths:
            out.append('<ol class="road-nodes">')
            for code in path.split():
                previous = ", ".join(by_id[code]["prerequisites"]) or "Tự kiểm đầu vào"
                kind = " elective" if code.startswith("MLP") else ""
                out.append(f'<li class="road-node{kind}"><a href="#{code}"><b>{code}</b> {escape(names[code])}</a>'
                           f'<small>Sau {escape(previous)}</small></li>')
            out.append('</ol>')
        out.append('</section>')
    return ''.join(out)+'</article>'
