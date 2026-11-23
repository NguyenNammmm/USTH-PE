#!/usr/bin/env python3
"""Xuất nguồn ML theo cách tổ chức course/practice của PE_Python_DA."""
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path('/home/acm/pe-usth/scripts/pe-ml-codex')


def write(path, value):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def paragraph(value):
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return '\n'.join(paragraph(v) for v in value)
    if isinstance(value, dict):
        return '\n'.join(f'{k}: {paragraph(v)}' for k, v in value.items())
    return str(value)


def main():
    raw = (SOURCE / 'out/lessons.json').read_bytes()
    bundle = json.loads(raw)
    rows = bundle['lessons']
    mapping = {}
    for line in (SOURCE / 'docs/MAP_ML.md').read_text().splitlines():
        cells = [s.strip() for s in line.strip('|').split('|')]
        if len(cells) == 6 and re.fullmatch(r'ML\d{2}', cells[0]):
            mapping[cells[0]] = cells
    groups, lessons, practice = [], [], []
    for row in rows:
        code = row['lesson_code']
        _, module, objective, level, concepts, before = mapping[code]
        group = next((g for g in groups if g['id'] == module), None)
        if group is None:
            group = {'id': module, 'title': row['module'], 'ids': []}
            groups.append(group)
        group['ids'].append(code)
        content = row['content_json']
        reading = []
        for key, value in content['step_1'].items():
            if key == 'code' and isinstance(value, dict):
                reading.append({'type': 'code', 'code': value.get('source', value.get('code', '')),
                                'expected': value.get('expected', '')})
            else:
                reading.append({'type': 'paragraph', 'text': paragraph(value)})
        drills = []
        for item in content['step_2'].get('practice', []):
            answer = item.get('answer', '')
            if item.get('answerCode'):
                answer += '\n\n```python\n' + item['answerCode'] + '\n```'
            if 'answerExpected' in item:
                answer += '\nKết quả: ' + str(item['answerExpected'])
            drills.append({'prompt': item['prompt'], 'answer': answer})
        lessons.append({'id': code, 'title': row['title'],
                        'level': {'B': 'Cơ bản', 'I': 'Trung cấp', 'N': 'Nâng cao'}[level],
                        'before': re.findall(r'ML\d{2}', before),
                        'topics': [v.strip() for v in concepts.split(';')],
                        'reading': reading, 'drills': drills, 'reviewExercises': [],
                        'strand': module,
                        'provenance': 'Giáo trình ML hiệu đính; bản Studio trong reference/studio-lessons.json.'})
        mcq = []
        for i, q in enumerate(content['step_2'].get('mcq', []), 1):
            options = [{'id': chr(97 + j), 'text': opt.get('text', opt.get('title', '')),
                        'feedback': opt.get('detail', '')} for j, opt in enumerate(q['options'])]
            mcq.append({'id': f'{code}-mcq-{i}', 'type': 'mcq', 'title': f'Câu hỏi {i}',
                        'prompt': q['question'], 'options': options,
                        'correctOption': options[q['correct']]['id'],
                        'explanation': q.get('explanation', ''), 'hints': []})
        s4 = content['step_4']
        exercise = {'id': f'{code}-sandbox', 'type': 'code',
                    'title': s4['task']['title'], 'prompt': s4['task']['body'],
                    'starter': s4['starterCode'], 'referenceSolution': s4['solutionCode'],
                    'tests': s4['tests'],
                    'hints': [paragraph(h) for h in s4.get('hints', [])]}
        practice.append({'id': code, 'title': row['title'], 'mcq': mcq, 'exercises': [exercise]})
    course = {'groups': groups, 'lessons': lessons}
    write('source/course.json', course)
    digest = hashlib.sha256((ROOT / 'source/course.json').read_bytes()).hexdigest()
    write('source/practice.json', {'schemaVersion': 1, 'sourceCourseSha256': digest, 'lessons': practice})
    target = ROOT / 'reference/studio-lessons.json'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(raw)
    write('reference/course-catalog.json', json.loads((SOURCE / 'course.json').read_text()))
    for name in ['MAP_ML.md', 'FORMAT_ML.md', 'CHECKLIST.md', 'Giao_Trinh_Machine_Learning_PE_Hieu_Dinh.docx']:
        dest = ROOT / 'docs' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SOURCE / 'docs' / name, dest)
    write('reference/provenance.json', {'source': str(SOURCE),
          'bundleSha256': hashlib.sha256(raw).hexdigest(),
          'reference': 'ProgrammingEdu-USTH/Giao_Trinh_PE: PE_Python_DA/source/course.json + practice.json',
          'scope': 'Cách tổ chức nguồn; chưa nghiệm thu bằng pipeline build của repository giáo trình.'})


if __name__ == '__main__':
    main()
