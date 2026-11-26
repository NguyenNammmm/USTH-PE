"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def bce_and_gradient(A, y, w):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    loss, g = bce_and_gradient([[1, 1], [1, 3]], [0, 1], [0, 0])
    same(loss, np.log(2))
    same(g, [0, -0.5])


def case_02():
    loss, g = bce_and_gradient([[1], [-1]], [1, 0], [-1000])
    same(loss, 1000)
    same(g, [-1])


def case_03():
    rejects(bce_and_gradient, [[1]], [2], [0])


CASES = [case_01, case_02, case_03]


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
