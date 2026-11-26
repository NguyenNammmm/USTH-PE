"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def encode_categories(train, values):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    levels, rows = encode_categories(['b','x','b'], ['x','a','b'])
    assert levels == ['b','x']
    same(rows, [[0,1],[0,0],[1,0]])


def case_02():
    levels, rows = encode_categories(['c','a'], ['a','z'])
    assert levels == ['a','c']
    same(rows, [[1,0],[0,0]])
    same(encode_categories(['a'],[])[1], np.empty((0,1)))


def case_03():
    rejects(encode_categories, [], ['a'])


def case_04():
    rejects(encode_categories, [['m']], ['m'])


CASES = [case_01, case_02, case_03, case_04]


if __name__ == "__main__":
    failed = 0
    for i, case in enumerate(CASES, 1):
        try:
            case()
        except NotImplementedError as error:
            sys.exit(str(error))
        except Exception as error:
            failed += 1
            print(f"Ca {i} chưa đạt · {type(error).__name__} · {error}")
        else:
            print(f"Ca {i} đạt")
    print(f"Đạt {len(CASES) - failed}/{len(CASES)} ca.")
    sys.exit(int(failed > 0))
