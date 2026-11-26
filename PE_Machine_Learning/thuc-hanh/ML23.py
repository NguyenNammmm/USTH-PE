"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def lloyd_step(X, centers):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    labels, centers, sse = lloyd_step([[0],[2],[7],[9]], [[0],[7]])
    same(labels, [0,0,1,1])
    same(centers, [[1],[8]])
    same(sse, 4)


def case_02():
    labels, centers, sse = lloyd_step([[0],[1],[2]], [[0],[2]])
    same(labels, [0,0,1])
    same(centers, [[0.5],[2]])
    same(sse, 0.5)


def case_03():
    labels, centers, sse = lloyd_step([[0],[4]], [[0],[0]])
    same(centers, [[2],[0]])
    same(sse, 8)


def case_04():
    rejects(lloyd_step, [[0]], [[0,1]])


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
