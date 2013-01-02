from nose.tools import assert_equal

from memoizer import memoize


@memoize
def fib(x):
    if x < 2:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


@memoize
def fib_default(x=0, y=0):
    if x < 2:
        return 1
    else:
        return fib_default(x - 1) + fib_default(x - 2)


def test_fib():
    assert_equal(fib(0), 1)
    assert_equal(fib(1), 1)
    assert_equal(fib(10), 89)


def test_memoize():
    assert_equal(fib(50), 20365011074)


def test_memoize_default():
    assert_equal(fib_default(), 1)
    assert_equal(fib_default(50), 20365011074)
