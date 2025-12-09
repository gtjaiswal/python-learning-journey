import pytest

import basic.calc as my_calc

def test_add():
    print("came....")
    assert my_calc.add(10,5) == 15
    assert my_calc.add("Garima ", "Jaiswal" )== ("Garima Jaiswal")


def test_subtract():
    assert my_calc.subtract(10,5) == 5

def test_divide():
    assert my_calc.divide(10,5)==2
    with pytest.raises(ValueError):
        my_calc.divide(10,0)