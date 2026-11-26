"""Điền hàm ở đầu tệp. Chạy tệp để tự kiểm bài Make 1."""

import sys

import numpy as np


def pca_fit(X, k):
    raise NotImplementedError("Điền phần thân hàm rồi chạy lại")


def same(actual, expected):
    actual, expected = np.asarray(actual), np.asarray(expected)
    assert actual.shape == expected.shape, (actual.shape, expected.shape)
    np.testing.assert_allclose(actual, expected, rtol=1e-7, atol=1e-9)


def rejects(fn, *args):
    with np.testing.assert_raises(ValueError):
        fn(*args)


def case_01():
    mu, U, ratio = pca_fit([[-2,0],[0,1],[0,-1],[2,0]], 1)
    same(mu, [0,0])
    same(U @ U.T, [[1,0],[0,0]])
    same(ratio, [0.8])


def case_02():
    mu, U, ratio = pca_fit([[1,1],[3,3]], 1)
    same(mu, [2,2])
    same(U @ U.T, [[0.5,0.5],[0.5,0.5]])
    same(ratio, [1])


def case_03():
    mu, U, ratios = pca_fit([[2,2],[2,2]], 2)
    same(mu, [2,2])
    same(U @ U.T, np.eye(2))
    same(ratios, [0,0])


def case_04():
    rejects(pca_fit, [[0,1]], 1)


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
