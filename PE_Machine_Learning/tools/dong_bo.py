#!/usr/bin/env python3
"""Đồng bộ PE_Machine_Learning với cây của nền tảng (repo pe_usth).

VÌ SAO CÓ TỆP NÀY. Nội dung giáo trình được soạn Ở ĐÂY, nhưng bộ dựng, các cổng
kiểm và việc nạp vào DB vẫn nằm ở pe_usth, và chúng đọc nội dung từ cây của pe_usth. Hai bên
phải giữ ĐÚNG TỪNG BYTE như nhau; chép tay thì lệch mà không ai thấy.

    py tools/dong_bo.py --nen-tang /path/to/pe_usth           # KIỂM: in tệp khác/thiếu, thoát 1 nếu có
    py tools/dong_bo.py --nen-tang /path/to/pe_usth --day     # chép từ ĐÂY sang pe_usth
    py tools/dong_bo.py --nen-tang /path/to/pe_usth --lay     # chiều ngược: từ pe_usth về ĐÂY

Quy ước:
  · chỉ thư viện chuẩn; không xoá tệp nào ở bên đích (tệp thừa chỉ được báo);
  · .json/.md so sánh sau khi gộp CRLF thành LF;
  · khi chép, tệp văn bản luôn ghi LF (đúng như đã lưu trong git).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

GOI = Path(__file__).resolve().parent.parent  # thư mục PE_Machine_Learning/

_ANH_XA = json.loads((GOI / 'tools' / 'anh-xa.json').read_text(encoding='utf-8'))
TEP: list[tuple[str, str]] = [tuple(x) for x in _ANH_XA['tep']]  # type: ignore[misc]
THU_MUC: list[tuple[str, str]] = [tuple(x) for x in _ANH_XA['thuMuc']]  # type: ignore[misc]
VAN_BAN = set(_ANH_XA['vanBan'])
BO_QUA = set(_ANH_XA['boQua'])


def chuan(b: bytes, p: Path) -> bytes:
    return b.replace(b'\r\n', b'\n') if p.suffix.lower() in VAN_BAN else b


def doc(p: Path) -> bytes | None:
    return p.read_bytes() if p.is_file() else None


def cac_cap(nen: Path) -> list[tuple[Path, Path, str]]:
    """Mọi cặp (tệp trong gói, tệp trong nền tảng, tên hiển thị)."""
    cap = [(GOI / a, nen / b, a) for a, b in TEP]
    for tg, tn in THU_MUC:
        ten: set[str] = set()
        for goc in (GOI / tg, nen / tn):
            if goc.is_dir():
                ten |= {p.relative_to(goc).as_posix() for p in goc.rglob('*')
                        if p.is_file() and not (set(p.relative_to(goc).parts) & BO_QUA)}
        cap += [(GOI / tg / t, nen / tn / t, f'{tg}/{t}') for t in sorted(ten)]
    return cap


def main() -> int:
    sys.stdout.reconfigure(encoding='utf-8')
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--nen-tang', required=True, help='thư mục gốc của repo pe_usth')
    chieu = ap.add_mutually_exclusive_group()
    chieu.add_argument('--day', action='store_true', help='chép từ gói sang nền tảng')
    chieu.add_argument('--lay', action='store_true', help='chép từ nền tảng về gói')
    args = ap.parse_args()

    nen = Path(args.nen_tang).resolve()
    if not (nen / 'scripts').is_dir() and not (nen / 'package.json').is_file():
        print(f'LỖI: {nen} không giống repo pe_usth (thiếu thư mục scripts hoặc package.json).')
        return 2

    khop = 0
    lech: list[str] = []
    da_chep = 0
    for g, n, ten in cac_cap(nen):
        a, b = doc(g), doc(n)
        if a is not None and b is not None and chuan(a, g) == chuan(b, n):
            khop += 1
            continue
        if a is None:
            lech.append(f'thiếu ở GÓI       {ten}')
        elif b is None:
            lech.append(f'thiếu ở NỀN TẢNG  {ten}')
        else:
            lech.append(f'KHÁC              {ten}')
        if args.day and a is not None:
            n.parent.mkdir(parents=True, exist_ok=True)
            n.write_bytes(chuan(a, g))
            da_chep += 1
        elif args.lay and b is not None:
            g.parent.mkdir(parents=True, exist_ok=True)
            g.write_bytes(chuan(b, n))
            da_chep += 1

    for dong in lech:
        print(dong)
    print(f'{khop} tệp khớp · {len(lech)} lệch' + (f' · đã chép {da_chep}' if (args.day or args.lay) else ''))
    if args.day or args.lay:
        con = sum(1 for g, n, _ in cac_cap(nen)
                  if not (doc(g) is not None and doc(n) is not None and chuan(doc(g), g) == chuan(doc(n), n)))
        print(f'sau khi chép còn {con} lệch' + (' — đó là tệp chỉ có ở một bên (công cụ không xoá).' if con else '.'))
        return 0 if con == 0 else 1
    return 0 if not lech else 1


if __name__ == '__main__':
    raise SystemExit(main())
