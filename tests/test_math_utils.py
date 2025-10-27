from src.math_utils import multiply, add, subtract, divide
import pytest


def test_multiply_one():
    assert multiply(3, 4) == 12


def test_multiply_two():
    assert multiply(4, 5) == 20


def test_add_one():
    assert add(2, 3) == 5


def test_subtract_one():
    assert subtract(2, 3) == -1


def test_divide_one():
    with pytest.raises(ZeroDivisionError):
        divide(3, 0)


def test_divide_two():
    assert divide(4, 1) == 4
