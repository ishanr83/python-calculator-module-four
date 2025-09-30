import math
import pytest
from app.operation.basic import add, sub, mul, div

@pytest.mark.parametrize("a,b,expected", [(2,3,5),(0,0,0),(-1,1,0),(1.5,2.5,4.0)])
def test_add(a,b,expected):
    assert add(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [(5,3,2),(0,3,-3),(-2.5,-0.5,-2.0)])
def test_sub(a,b,expected):
    assert sub(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [(3,4,12),(-2,3,-6),(1.5,2,3.0)])
def test_mul(a,b,expected):
    assert mul(a,b) == expected

@pytest.mark.parametrize("a,b,expected", [(10,2,5.0),(3,2,1.5),(-9,-3,3.0)])
def test_div(a,b,expected):
    assert math.isclose(div(a,b), expected)

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1,0)
