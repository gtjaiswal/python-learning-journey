class Employee:
    def __init__(self, name:str, salary:float):
        self.name = name
        # This will call the setter method below for validation
        self.salary = salary

    @property
    def salary(self):
        """The getter for the employee's salary."""
        return self._salary

    @salary.setter
    def salary(self, salary: float):
        if not (0 <= salary <= 1000000):
            raise ValueError("Salary cannot be less than 0 or greater than 1000000")
        self._salary = salary


    '''
    that's the default behavior! If you define a property with only a getter,
    Python will automatically raise an AttributeError if someone tries to set it.
    '''
    @property
    def annual_bonus(self):
        return self._salary * 0.10


if __name__ == "__main__":
    # Test it:
    emp = Employee("John", 50000)
    print(emp.salary)  # 50000
    print(emp.annual_bonus)  # 5000
    emp.salary = 60000  # Should work
    try:
        emp.salary = -1000  # Should raise ValueError
    except ValueError as e:
        print(e)
    try:
        emp.annual_bonus = 10000  # Should raise AttributeError
    except AttributeError as e:
        print(e)
