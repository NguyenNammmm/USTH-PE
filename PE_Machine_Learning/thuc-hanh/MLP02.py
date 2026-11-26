"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def variance_filter(train, X, cutoff):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    idx, out = variance_filter([[1,0,0],[1,2,1]], [[8,4,2]], 0.25)
    same(idx,[1])
    same(out,[[4]])


def case_02():
    idx, out = variance_filter([[2,2],[2,2]], [[9,9]], 0)
    same(idx,[])
    same(out,np.empty((1,0)))


def case_03():
    same(variance_filter([[0],[2]], [[100]], 0)[1], [[100]])


def case_04():
    rejects(variance_filter, [[1,2]], [[2]], 0)


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
