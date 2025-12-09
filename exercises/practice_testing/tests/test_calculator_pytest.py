import pytest
import calculator

def test_add():
    assert calculator.Calculator().add(10,2)==12
