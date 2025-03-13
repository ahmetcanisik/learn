import pytest
from calculator import square

def test_square():
    nums = [-1, -5, 0, 2, 5, 8, 21]
    
    for num in nums:
        assert square(num) == (num * num)
        
def test_positive():
    assert square(4) == 16
    assert square(8) == 64
    
def test_negative():
    assert square(-1) == 1
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cats")