"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def svm_objective(X, y, w, b, C):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    h,obj = svm_objective([[-1],[1]], [-1,1], [1], 0, 3)
    same(h,[0,0])
    same(obj,0.5)


def case_02():
    h,obj = svm_objective([[0],[2]], [-1,1], [0], 1, 2)
    same(h,[2,0])
    same(obj,4)


def case_03():
    h,obj = svm_objective([[-0.25],[1]], [-1,1], [1], 0, 1)
    same(h,[0.75,0])
    same(obj,1.25)


def case_04():
    rejects(svm_objective, [[0]], [0], [1], 0, 1)


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
