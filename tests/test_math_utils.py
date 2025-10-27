from src.math_utils import multiply

def test_multiply_one():
    assert multiply(3, 4) == 12

def test_multiply_two():
    assert multiply(4, 5) == 20