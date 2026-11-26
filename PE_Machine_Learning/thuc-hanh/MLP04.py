"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def dbscan_1d(x, eps, min_samples):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    same(dbscan_1d([0,0.5,1,4,4.5,5,8], 0.5, 3), [0,0,0,1,1,1,-1])


def case_02():
    same(dbscan_1d([0,0.5,1,1.5,2], 0.5, 3), [0,0,0,0,0])


def case_03():
    same(dbscan_1d([0,3,3], 0, 2), [-1,0,0])


def case_04():
    same(dbscan_1d([], 1, 1), [])


def case_05():
    rejects(dbscan_1d, [1], -1, 2)


CASES = [case_01, case_02, case_03, case_04, case_05]


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
