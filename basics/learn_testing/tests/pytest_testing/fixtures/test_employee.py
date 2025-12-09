import pytest

from fixtures.employee1 import Employee

@pytest.fixture
def corey_employee():
    return Employee('Corey', 'Schafer', 50000)


@pytest.fixture
def john_employee():
    return Employee('John', 'Doe', 60000)


def test_fullname(corey_employee):
    assert corey_employee.fullname == "Corey Schafer"


def test_email(corey_employee):
    assert corey_employee.email == "Corey.Schafer@email.com"


def test_apply_raise(corey_employee):
    corey_employee.apply_raise()
    assert corey_employee.pay == 52500


def test_another_employee_email(john_employee):
    assert john_employee.email == "John.Doe@email.com"
