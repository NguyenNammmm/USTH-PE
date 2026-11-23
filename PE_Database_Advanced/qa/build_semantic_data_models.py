"""Freeze the manually reviewed AD13/AD14 section evidence.

This is a witness-integrity helper. The explicit concept/witness mapping below is
the result of reading the source bodies, not an automated semantic classifier.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
COURSE = ROOT / "output/database-advanced"


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def body_hash(lines, first, last):
    return sha("\n".join(lines[first - 1:last]))


lessons = {
    name: (COURSE / f"lessons/{name}.md").read_text(encoding="utf-8-sig").splitlines()
    for name in ["AD13", "AD14"]
}


def witness(lesson, prefix, role="explanation", section=None, code=False):
    lines = lessons[lesson]
    lo, hi = 0, len(lines)
    if section:
        lo = lines.index(section) + 1
        hi = next((i for i in range(lo, len(lines)) if lines[i].startswith("## ")), len(lines))
    hits = [i for i in range(lo, hi) if lines[i].startswith(prefix)]
    assert len(hits) == 1, (lesson, prefix, hits)
    first = last = hits[0]
    if code:
        first = max(i for i in range(first) if lines[i].startswith("```"))
        last = next(i for i in range(last + 1, len(lines)) if lines[i].startswith("```"))
    heading = next((lines[i] for i in range(first, -1, -1) if lines[i].startswith("#")), "")
    text = "\n".join(lines[first:last + 1])
    p = COURSE / f"lessons/{lesson}.md"
    return {
        "lesson": lesson, "path": str(p),
        "lessonSha256": hashlib.sha256(p.read_bytes()).hexdigest(),
        "heading": heading, "lineRange": [first + 1, last + 1], "role": role,
        "paragraphSha256": sha(text), "excerpt": text[:400],
    }


def exercise(lesson, number):
    return {
        "question": witness(lesson, f"{number}. ", "independent exercise", "## Luyện tập"),
        "answer": witness(lesson, f"{number}. ", "answer with rationale", "## Đáp án và lập luận"),
    }


# Section-specific witnesses were selected after reading every assigned own-body.
# Prefixes identify exact paragraphs, rather than claiming coverage from keywords.
REVIEW = {
    "8.1": ("AD13", [
        "Fixed atomic schemas versus evolving user-profile attributes and interests",
        "Semi-structured storage and exchange of business objects between backend and responsive clients",
    ], [("Semi-structured không", "explanation"), ("Nested object đóng", "business-object tradeoff"),
        ("Serialization phục vụ", "client/service exchange example")], [5, 7]),
    "8.1.1": ("AD13", [
        "Overview of extensions for modern application storage and data exchange; child models assessed separately",
    ], [("Flexible schema không", "model distinctions"), ("Nested object đóng", "storage/exchange example")], [5]),
    "8.1.1.1": ("AD13", [
        "Wide-column: independently varying attributes per tuple",
        "Sparse-column: fixed large schema with unused fields null",
    ], [("Flexible schema không", "two-product example with schema-change distinction")], [5]),
    "8.1.1.2": ("AD13", [
        "Set, multiset, array, map and key uniqueness; put/get/delete map operations",
        "NFNF and the workload-sensitive cost of normalized versus nested user interests",
        "Scientific image/sensor arrays, inferred time offsets, tuple overhead and compressed array storage",
        "Specialized array-database storage/operators versus a generic JSON array",
    ], [("Map giữ", "collection counterexample and NFNF"), ("Trace map từ", "put/get/delete state trace and lookup workload"),
        ("Array còn hữu ích", "offset/compression/missing-sample example")], [5, 6]),
    "8.1.1.3": ("AD13", [
        "Composite attributes and nesting of structured and collection values",
        "JSON/XML tree structure and flexible fields/types",
        "Business-object packaging, exchange and document retrieval versus joins",
    ], [("Nested object đóng", "nested profile and retrieval/update tradeoff"),
        ("Hierarchy giữ", "XML hierarchy and business-object exchange"),
        ("SELECT JSON_OBJECT", "nested constructor example", True)], [5, 8]),
    "8.1.1.4": ("AD13", [
        "Knowledge representation of facts/rules at large scale",
        "RDF entities, attributes and binary relationships as a triple set or graph",
    ], [("RDF triple có", "triple/identity explanation"),
        ("Chuyển triple thành", "graph/facts/rules and linked-information example")], [9]),
    "8.1.2": ("AD13", [
        "JSON textual primitives, object/map fields and ordered arrays; flexible nested structures",
        "Application/web-service parameters/results and language-library conversion",
        "Text storage/parsing overhead and binary/compressed storage representation such as BSON",
        "Separate SQL capabilities: JSON typed storage, row construction, multirow aggregation and path extraction; dialect dependence",
    ], [("Nested object đóng", "storage/parse tradeoff"),
        ("CREATE TEMPORARY TABLE docs", "typed storage and extraction example", True),
        ("SELECT JSON_OBJECT", "row JSON construction", True),
        ("CREATE TEMPORARY TABLE export_item", "multirow aggregate query", True),
        ("Order7 cho", "expected aggregate occurrences and order contract"),
        ("Serialization phục vụ", "language/service exchange")], [1, 2, 7]),
    "8.1.3": ("AD13", [
        "Paired XML tags, hierarchical structured purchase-order document and repeated elements",
        "Flexible tag addition and agreement on tag semantics between organizations",
        "XQuery/XPath distinction and SQL/XML storage, row construction, XMLAGG and path extraction capabilities",
    ], [("XML dùng cặp", "XML model explanation"), ("<purchase id=", "original XML business-object fixture", True),
        ("Hierarchy giữ", "tag contract and path result/counterexample"),
        ("Có ba capability SQL/XML", "storage/construction/aggregation/extraction mechanisms")], [8]),
    "8.1.4": ("AD13", [
        "RDF overview grounded in entities and relationships; descendants assessed separately",
    ], [("RDF triple có", "resource/triple explanation"), ("Chuyển triple thành", "triple-to-graph example")], [9]),
    "8.1.4.1": ("AD13", [
        "Subject/predicate/object; resource-valued relationships versus literal-valued attributes",
        "Resource identifiers, type-as-resource, subtype vocabulary and flexible relationship/property addition",
        "Fresh identity for a composite-key entity with component assertions",
    ], [("ex:an   ex:worksFor", "original resource/literal triple fixture", True),
        ("RDF triple có", "term roles and identity"), ("Type của resource", "type and composite-key resource example"),
        ("RDF còn cho", "subclass vocabulary and inference boundaries")], [3, 9]),
    "8.1.4.2": ("AD13", [
        "Directed labeled graph: resources/literals as nodes and predicates as edges",
        "Knowledge graphs combine facts from sources; answer a question by an edge pattern and optional type condition",
    ], [("Chuyển triple thành", "directed graph and information-source explanation"),
        ("Basic graph pattern", "matching/join example and additional PE proof"),
        ("Type của resource", "resource type condition")], [9]),
    "8.1.4.3": ("AD13", [
        "Triple patterns with variables; multi-pattern joins on shared variables",
        "Variable predicate; SELECT results; OPTIONAL, aggregation and subqueries",
    ], [("SELECT ?person ?skill", "OPTIONAL query", True),
        ("Với URI tương ứng", "OPTIONAL/unbound output"),
        ("Basic graph pattern", "matching algorithm and soundness/completeness explanation"),
        ("Bindings dự kiến", "variable-predicate query and output"),
        ("SELECT ?person (COUNT", "SPARQL aggregation query", True),
        ("Expected là", "aggregate expected output and COUNT(*) counterexample"),
        ("SELECT ?person ?n ?labName", "subquery and join", True),
        ("Kết quả là `(an,2", "subquery output/scope")], [4, 10]),
    "8.1.4.4": ("AD13", [
        "Binary-edge limitation for n-ary relationships and temporal qualifiers",
        "Event/artificial entity linking participants and qualifiers; reification idea",
        "Quads/context versus an event node; linked graphs and source identity",
    ], [("RDF còn cho", "event node and qualifier semantics"),
        ("Một fixture sự kiện", "two original supply events"),
        ("SELECT ?event ?day", "event-anchored query", True),
        ("Bindings dự kiến", "correct event output and spurious pairing counterexample"),
        ("Một context có", "quad/context and validity/provenance distinction"),
        ("Chuyển triple thành", "linked sources and identity conditions")], [3, 5, 9]),
    "8.2": ("AD14", [
        "Relational/programming-language type mismatch and declarative access",
        "Three approaches: DB object-relational features, ORM conversion, native object-oriented DB",
        "Language integration, declarative optimization and source's historical pointer-error tradeoff",
    ], [("Object-relational DBMS mở", "three-way comparison"),
        ("Ví dụ cần tìm", "same retrieval problem through declarative query versus pointer traversal")], [6]),
    "8.2.1": ("AD14", [
        "Object-relational approach adds richer types and object features inside a relational DBMS; child mechanisms assessed separately",
    ], [("Object-relational DBMS mở", "DBMS versus mapping distinction"),
        ("Ở mô hình object-relational", "structured/collection/typed-table example")], [6, 7]),
    "8.2.1.1": ("AD14", [
        "Structured user-defined types, references and typed tables; row insertion distinct from value creation",
        "Scalar/structured/row collections and vendor-dependent array/table-type support",
        "Associated methods on structured types",
    ], [("CREATE TYPE NameT", "type/table declaration model", True),
        ("FINAL cấm", "named structured fields and collection-row capability"),
        ("Constructor tạo", "constructor/value versus persistent-row example"),
        ("Methods được", "method/self example"),
        ("Khởi tạo REF", "identity initialization example")], [7]),
    "8.2.1.2": ("AD14", [
        "Student/Teacher subtypes inherit Person attributes and methods",
        "Subtype can redefine a method",
    ], [("StudentT UNDER", "inherited fields and runtime override trace")], [8]),
    "8.2.1.3": ("AD14", [
        "Table inheritance versus type inheritance and relational class-table mapping",
        "Inherited columns, inserting inherited/local values and implicit inclusion in supertable queries",
        "ONLY excludes descendant-origin rows; source dialect variations are not MySQL capabilities",
    ], [("Table inheritance có", "P1/S2/T3 query scopes and mapping contrast"),
        ("Về update/delete", "separate mutation-scope example"),
        ("Ở mô hình object-relational", "typed-row versus application class distinction")], [5, 9]),
    "8.2.1.4": ("AD14", [
        "REF target type and scope; system OID versus stable key-derived reference",
        "Create/find REF target and set a reference; path navigation and DEREF",
        "Reference hides a join; relational join equivalent and NULL/target-lifetime distinctions",
    ], [("REF có target", "Department head reference and dereference example"),
        ("Khởi tạo REF", "system OID lookup/assignment trace"),
        ("Objects gồm", "reference-sharing versus copy counterexample")], [1, 5]),
    "8.2.2": ("AD14", [
        "Mapping SQL tuples to application objects and materializing selection results",
        "Object create/update/delete/save translated to INSERT/UPDATE/DELETE",
        "Object-model query translated to SQL, cache benefits and limited dialect portability",
        "Bulk-update and complex imperative-query inefficiency; direct SQL fallback and cache consistency",
    ], [("Mapping `Asset{id", "ORM create/read/update/delete and commit trace"),
        ("Trace này tách", "mapping scope, cache benefit and portability limits"),
        ("ORM còn cần", "bulk SQL/cache state and fallback"),
        ("ORM thường có", "identity map and loading tradeoffs")], [5, 12]),
    "29.1": ("AD14", [
        "Atomicity depends on considered operations; structured Address supports both whole-value and component access",
        "Nested Book contains ordered authors, structured publisher and keyword collection",
        "Independent normalized Book/Author/Keyword representations retain occurrence/order and parent identity",
        "Nested object interface versus join/constraint costs; duplicated many-to-many enrollment causes redundancy",
    ], [("Atomicity phụ", "address example and E-R complex-type mapping"),
        ("Fixture book7", "nested-to-relational example"),
        ("Với quan hệ takes", "bidirectional enrollment redundancy counterexample"),
        ("Online §29.4.3 còn", "multiple-collection expansion counterexample")], [10]),
    "29.2": ("AD14", [
        "Named structured types, component access, typed tables and unnamed ROW alternatives",
        "FINAL/NOT FINAL subtype capability",
        "Methods declared on type, body defined separately, self/arguments and mutating methods",
        "Explicit constructor, default no-argument constructor, overloads, row-value construction and insert of typed fields",
    ], [("CREATE TYPE NameT", "declaration model", True),
        ("FINAL cấm", "component access and named/unnamed distinction"),
        ("Constructor tạo", "default/overloaded construction and row values"),
        ("Methods được", "self/method invocation/state trace"),
        ("Một value Book đủ", "complete constructed value with structured fields")], [7]),
    "29.3": ("AD14", [
        "Heading-only container for type and table inheritance; no independent prose or algorithm in own-body",
    ], [("Một structured type Address", "type-versus-table inheritance distinction"),
        ("StudentT UNDER", "type example"), ("Table inheritance có", "table example")], [8, 9]),
    "29.3.1": ("AD14", [
        "Inherited attributes/methods, overriding and FINAL/NOT FINAL",
        "Multiple inheritance is a conceptual source example; common inherited fields versus independently conflicting department fields",
        "Exactly one most-specific type, supertypes and limitation for overlapping roles in the source model",
    ], [("StudentT UNDER", "override and FINAL counterexample"),
        ("Online §29.3.1 mô", "two-department conflict and most-specific type example"),
        ("FINAL cấm", "subtyping and declaration explanation")], [7, 8]),
    "29.3.2": ("AD14", [
        "Typed subtables inherit fields and are implicitly included in parent queries",
        "ONLY query/update/delete scope; descendant-origin mutations",
        "Two consistency constraints on corresponding rows and single insert origin",
        "Source model cannot represent overlapping specialization through those subtables; separate role tables with referential integrity workaround",
        "UNDER privilege controls subtype/subtable creation",
    ], [("Table inheritance có", "P1/S2/T3 select scope"),
        ("Về update/delete", "mutation scope trace"),
        ("Online §29.3.2 còn", "consistency, overlap workaround and privilege explanation"),
        ("Ví dụ Student(1", "role overlap mapping example")], [2, 8, 9]),
    "29.4": ("AD14", [
        "Array order versus unordered multiset multiplicity and set uniqueness",
        "Structured Book with bounded author array, publication date, Publisher and keyword multiset",
        "Choose ordered array when E-R multivalued attribute order matters",
    ], [("Một tác giả có", "array/multiset/set distinction"),
        ("Trong model SQL collection", "collection type and bound declaration"),
        ("Một value Book đủ", "complete typed Book fixture")], [3, 10]),
    "29.4.1": ("AD14", [
        "ARRAY/MULTISET value construction and explicitly defined Publisher constructor",
        "Read/update array element by index",
    ], [("Trong model SQL collection", "construct/read/update example"),
        ("Một value Book đủ", "all fields of original Book construction")], [10]),
    "29.4.2": ("AD14", [
        "Collection can occupy a relation position; membership via unnest",
        "Array-index queries and per-parent UNNEST in FROM with outer variable in scope",
        "WITH ORDINALITY preserves array positions; no order assumption for unordered collections",
    ], [("Query “book có", "membership versus row expansion and ordinality outputs"),
        ("Một tác giả có", "order/multiplicity counterexample"),
        ("unnest(author_id", "unnest/nest model algorithm", True),
        ("Với rows (7,1", "round-trip invariant and cost")], [3, 10]),
    "29.4.3": ("AD14", [
        "Unnest multiple independent collections plus structured Publisher into an atomic flat relation",
        "Grouping and COLLECT produce nested multisets; row multiplication can prevent round trip",
        "Correlated SELECT constructions ARRAY with order and MULTISET with multiplicity restore separate branches per parent",
        "SET, multiset intersection/fusion union, SUBMULTISET and whole-value reassignment via EXCEPT ALL",
    ], [("Online §29.4.3 còn", "two-by-three expansion and lost-parent counterexample"),
        ("Nesting có hai", "COLLECT grouping and exact bag output"),
        ("for each b in Book", "correlated construction pseudocode", True),
        ("Với book7, kết", "expected output, correctness and model cost"),
        ("Multiset operators", "count-based operator example and reassignment")], [3, 10, 11]),
}


def make_ledger():
    prior = json.loads((COURSE / "research/semantic-apps-ledger.json").read_text(encoding="utf-8-sig"))
    selected = [u for u in prior["units"] if set(u["assignedLessonIds"]) & {"AD13", "AD14"}]
    assert {u["section"] for u in selected} == set(REVIEW)
    units = []
    for old in selected:
        lesson, concepts, locators, nums = REVIEW[old["section"]]
        source = old["source"].copy()
        p = Path(source["path"])
        src_lines = p.read_text(encoding="utf-8-sig").splitlines()
        source["sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
        first, last = source["ownBodyRange"]
        source["ownBodySha256"] = body_hash(src_lines, first, last)
        source["ownBodyHashEncoding"] = "UTF-8 of LF-joined decoded source lines; no final newline"
        witnesses = [witness(lesson, loc[0], loc[1], code=len(loc) > 2 and loc[2]) for loc in locators]
        unit = {
            "section": old["section"], "title": old["title"],
            "assignedLessonIds": old["assignedLessonIds"], "source": source,
            "status": "complete", "assessmentScope": "own-body; descendants have independent records",
            "readRanges": [[first, last]],
            "readCoverage": "Full own-body read, including non-heading prose and embedded examples; chapter introductions additionally read",
            "sourceConcepts": concepts, "lessonWitnesses": witnesses,
            "exerciseAnswerWitnesses": [exercise(lesson, n) for n in nums],
            "algorithmProofAssessment": {
                "sourceHasFormalTheoremOrProof": False,
                "sourceHasPseudocodeAlgorithm": False,
                "sourceEvidence": "Full own-body presents data-model/interface/query examples, not a formal theorem or pseudocode algorithm.",
                "lessonAdds": "PE invariants/correctness/cost are explicitly identified by their own lesson witnesses where relevant; no inherited proof credit.",
            },
            "gapNotes": [],
        }
        if old["section"] in {"8.1.4.2", "8.1.4.3"}:
            unit["algorithmProofAssessment"]["additionalLessonProofWitnesses"] = [witness("AD13", "Basic graph pattern", "PE matching/join soundness/completeness and cost")]
        if old["section"] in {"29.4.2", "29.4.3"}:
            unit["algorithmProofAssessment"]["additionalLessonProofWitnesses"] = [
                witness("AD14", "unnest(author_id", "PE unnest/nest pseudocode", code=True),
                witness("AD14", "Với rows (7,1", "PE invariant/round-trip/cost"),
                witness("AD14", "Với book7, kết", "PE correlated-construction correctness/cost"),
            ]
        units.append(unit)
    intro_reads = []
    for filename, bounds in [("chapter-8.txt", (1, 11)), ("online-29.txt", (1, 12))]:
        p = ROOT / "tmp/database-source" / filename
        lines = p.read_text(encoding="utf-8-sig").splitlines()
        intro_reads.append({"path": str(p), "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
                            "readRanges": [list(bounds)], "bodySha256": body_hash(lines, *bounds),
                            "role": "chapter introductory context; not an extra numbered unit"})
    return {
        "schemaVersion": 2, "date": "2026-11-05", "scopeLessonIds": ["AD13", "AD14"],
        "sourceUnitCount": len(units),
        "scopeNote": "Only the 29 assigned own-bodies in print 8.1/8.2 and online 29.1–29.4.3. No verdict on the 947-unit inventory or other lessons.",
        "policy": {"completionMethod": "Manual full-body comparison to final lesson paragraphs, examples, independent exercises and answers",
                   "automatedChecks": "Hash/range/reference integrity only; they do not establish semantic completeness",
                   "headingOrKeywordCredit": False, "blanketBaselineCredit": False, "sourceExerciseCopying": False,
                   "sqlRuntimePerformed": False, "engineExecutionCredit": False,
                   "modelNotation": "SQL complex types/collections are source models, separately labeled from MySQL syntax; SPARQL requires a declared engine"},
        "sourceContextReads": intro_reads,
        "visualSourceReviews": [
            {"source": "DSC 7e supplied print PDF", "physicalPages": [398, 400, 402, 403],
             "figures": ["8.1", "8.2", "8.3", "8.4"],
             "observations": "Verified nested object/array, paired hierarchical XML tags, resource-vs-literal triples, and directed labeled entity/value graph. Original PE fixtures teach the mechanisms; source figures are not redistributed."},
            {"source": "tmp/database-source/online-29.pdf", "physicalPages": [2, 3, 14, 15],
             "figures": ["29.1", "29.2", "29.3", "29.4"],
             "observations": "Verified nested Book fields, normalized Author position/Keyword/Book branches, Cartesian flattened rows and partially nested bags. Explicit lesson counterexample checks COLLECT multiplicity rather than assuming the source sketch round-trips."},
        ],
        "primaryDocsChecked": [
            {"url": "https://dev.mysql.com/doc/refman/8.4/en/aggregate-functions.html#function_json-arrayagg", "reason": "MySQL JSON aggregate order and empty-input contract"},
            {"url": "https://www.w3.org/TR/sparql11-query/", "reason": "SPARQL 1.1 aggregation and subquery capability/syntax"},
        ],
        "units": units, "counts": {"complete": len(units), "partial": 0, "missing": 0, "unreviewed": 0},
        "revisionLog": [{"date": "2026-11-05", "action": "Fresh full read of all 29 assigned units; prior statuses not reused. Replaced missing material with original examples and focused exercise/answer pairs, then froze exact final witnesses."}],
    }


if __name__ == "__main__":
    ledger = make_ledger()
    path = COURSE / "research/semantic-data-models.json"
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"path": str(path), "counts": ledger["counts"]}))
