import pytest

from employee import Employee


class TestEmployee:

    def test_fullname(self):
        print("test_fullname:")
        emp1 = Employee()
        assert emp1.fullname() == "defFirst defLast"
