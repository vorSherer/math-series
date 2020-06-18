import pytest
from math_series.series import (
    fibonacci,
    lucas,
    sum_series,
)


def test_fib_exists():
    assert fibonacci


def test_lucas_exists():
    assert lucas


def test_sum_series_exists():
    assert sum_series


# *************  Fibonacci series tests  ************

def test_fib_0():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected


def test_fib_false_pos():
    expected = 0
    actual = fibonacci(1)
    assert actual != expected


def test_fib_less_than_0():
    expected = "n must be an integer greater than or equal to 0."
    actual = fibonacci(-1)
    assert actual == expected


# @pytest.mark.skip
def test_fib_str_0():
    with pytest.raises(TypeError):
        assert fibonacci("0") is TypeError


def test_fib_int1():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected


def test_fib_int2():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected


def test_fib_int5():
    expected = 2 + 3
    actual = fibonacci(5)
    assert actual == expected


# *************  Lucas series tests  ************

def test_luc_0_pass():
    expected = 2
    actual = lucas(0)
    assert actual == expected


def test_luc_0_false_pos():
    expected = 2
    actual = lucas(1)
    assert actual != expected


def test_luc_less_than_0():
    expected = "n must be an integer greater than or equal to 0."
    actual = lucas(-1)
    assert actual == expected


def test_luc_4():
    expected = 3 + 4
    actual = lucas(4)
    assert actual == expected


# *************  Sum series tests  ************

def test_sum_series_fib_0():
    expected = 0
    actual = sum_series(0, 0, 1)
    assert actual == expected


def test_sum_series_lucas_0():
    expected = 2
    actual = sum_series(0, 2, 1)
    assert actual == expected


def test_sum_series_less_than_zero():
    expected = "n must be an integer greater than or equal to 0."
    actual = sum_series(-1)
    assert actual == expected


def test_sum_series_not_fib_luc():
    expected = "Sorry, that combination has not yet been defined."
    actual = sum_series(4, 1, 2)
    assert actual == expected


