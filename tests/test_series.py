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


