#!/usr/bin/env python3
"""Kiểm tra gói nguồn, không sửa hoặc chạy nội dung học viên."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(name):
    return json.loads((ROOT / name).read_text())

course = read('source/course.json')
practice = read('source/practice.json')
original = read('reference/studio-lessons.json')['lessons']
ids = [f'ML{i:02}' for i in range(1, 29)]
assert [v['id'] for v in course['lessons']] == ids
assert [v['id'] for v in practice['lessons']] == ids
assert len(course['groups']) == 6
assert [i for g in course['groups'] for i in g['ids']] == ids
assert practice['sourceCourseSha256'] == hashlib.sha256((ROOT/'source/course.json').read_bytes()).hexdigest()
graph = {v['id']: v['before'] for v in course['lessons']}
def visit(code, path):
    assert code not in path, ('cycle', code)
    for prev in graph[code]:
        assert prev in graph
        visit(prev, path + [code])
for code in ids:
    visit(code, [])
mcq_count = drill_count = test_count = 0
for lesson, authored, old in zip(course['lessons'], practice['lessons'], original):
    assert lesson['level'] in ['Cơ bản', 'Trung cấp', 'Nâng cao']
    assert 3 <= len(lesson['topics']) <= 6
    source = old['content_json']
    assert len(lesson['drills']) == len(source['step_2'].get('practice', []))
    assert len(authored['mcq']) == len(source['step_2']['mcq'])
    for q, oldq in zip(authored['mcq'], source['step_2']['mcq']):
        assert q['prompt'] == oldq['question']
        assert q['correctOption'] == q['options'][oldq['correct']]['id']
        assert len({o['id'] for o in q['options']}) == len(q['options'])
    ex = authored['exercises'][0]
    assert ex['referenceSolution'] == source['step_4']['solutionCode']
    assert ex['tests'] == source['step_4']['tests']
    mcq_count += len(authored['mcq'])
    drill_count += len(lesson['drills'])
    test_count += len(ex['tests'])
manifest = read('reference/provenance.json')
assert hashlib.sha256((ROOT/'reference/studio-lessons.json').read_bytes()).hexdigest() == manifest['bundleSha256']
print(f'PACKAGE_PASS: 28 bài, 6 module, {mcq_count} MCQ, {drill_count} tự luận, {test_count} test được bảo toàn.')
print('Build/Pyodide/browser theo pipeline của sếp: NOT_TESTED; S3 giữ nguyên trong reference.')
