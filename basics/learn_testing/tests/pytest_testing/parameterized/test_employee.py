import pytest
from parameterized.employee1 import Employee


@pytest.fixture
def employee():
    return Employee('Corey', 'Schafer', 50000)

# --- Parametrized Test for Multiple Scenarios ---

@pytest.mark.parametrize("start_pay, expected_raised_pay", [
    (50000, 52500),      # Scenario 1
    (60000, 63000),      # Scenario 2
    (100000, 105000),    # Scenario 3
    (0, 0)               # Scenario 4: Edge case
])
def test_apply_raise_with_different_salaries(start_pay, expected_raised_pay):
    """
    This single tests function will run four times, once for each pair of values.
    """
    # 1. Create an employee with the specific starting pay for the current scenario
    emp = Employee('Test', 'User', start_pay)

    # 2. Perform the action
    emp.apply_raise()

    # 3. Assert against the expected result for the current scenario
    assert emp.pay == expected_raised_pay

@pytest.mark.parametrize("first_name, last_name, email", [
    ("John", "Jane" ,"John.Jane@email.com"),      # Scenario 1
    ("David", "Atta", "David.Atta@email.com"),      # Scenario 2
    ("Mary", "Lamb", "Mary.Lamb@email.com"),     # Scenario 3
    ("Atika", "Sharma", "Atika.Sharma@email.com")            # Scenario 4
])
def test_email_formation_with_different_names(first_name, last_name, email):
    emp = Employee(first_name, last_name,0)
    assert emp.email==email
    # --- 2. Negative Assertions ---
    incorrect_format_1 = f"{first_name}{last_name}@email.com"
    assert emp.email != incorrect_format_1

    incorrect_format_2 = f"{first_name}_{last_name}@email.com"
    assert emp.email != incorrect_format_2
