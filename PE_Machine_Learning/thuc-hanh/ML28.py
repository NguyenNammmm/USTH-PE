"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def regression_pipeline(X_train, y_train, X_test, y_test):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    p,m = regression_pipeline([[0,7],[2,7],[4,7]], [1,5,9], [[8,7],[10,7]], [18,20])
    same(p, [17,21])
    same(m, 1)


def case_02():
    p,m = regression_pipeline([[2],[2]], [1,5], [[3]], [4])
    same(p, [3])
    same(m, 1)


def case_03():
    p,m = regression_pipeline([[0],[2]], [0,2], [[4]], [12])
    same(p, [4])
    same(m, 8)


def case_04():
    rejects(regression_pipeline, [[0]], [0], [[1,2]], [0])


def case_05():
    rejects(regression_pipeline, [[float('nan')]], [0], [[1]], [0])


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
