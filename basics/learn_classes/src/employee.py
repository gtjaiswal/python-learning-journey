import datetime

class Employee:

    # class variable - same for all the instances
    num_of_emps = 0
    raise_amount = 1.05

    # Constructors:
    def __init__(self, first="defFirst", last="defLast", salary=100000 ):
        print("calling Emp constructor")
        # instance variables - different fpr each instance
        self.first = first
        self.last=last
        self.salary=salary
        # self.email=first+"."+last+"@email.com"
        # class variable initialized at instance creation
        Employee.num_of_emps+=1

    # class method as constructor
    @classmethod
    def from_string (cls,emp_str):
        first, last, salary = emp_str.split("-")
        return cls(first, last, salary)

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, fullname):
        self.first, self.last = fullname.split(" ")

    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None

    def raise_salary(self):
        # we can call class variable either with Class name or instance
        # raised_sal = self.salary * Employee.raise_amount
        raised_sal = self.salary * self.raise_amount
        return raised_sal

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_work_day(day):
        return not(day.weekday() == 5 or day.weekday() ==6)

    def __repr__(self):
        return "Employee('{}','{}',{}')".format(self.first, self.last, self.email)

    # print() internally call str dunder and str internally call repr if str is not overloaded
    def __str__(self):
        return f"{self.first} {self.last} - {self.email}"

if __name__ == "__main__":
    emp1 = Employee("abc")
    emp2 = Employee()

    print(emp1.email, emp1.salary)
    print(emp2.email,emp2.salary)
    # call on instance
    print(emp1.fullname)
    # call on class
    print(Employee.fullname)
    print(Employee.num_of_emps)

    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)

    Employee.set_raise_amount(2.0)
    emp1.set_raise_amount(2.5)

    print(Employee.raise_amount)
    print(emp1.raise_amount)
    print(emp2.raise_amount)

    emp3=Employee.from_string("Garima-Jaiswal-1000000")
    print(emp3.salary)

    print(Employee.is_work_day(datetime.date(2016, 7, 10)))
    print(emp1)
    print(repr(emp1))
    print(str(emp1))
    str(emp1)
    repr(emp1)

    print("emp1 email before : ", emp1.email)
    emp1.first="newFirst"
    print("emp1 first after : ",emp1.first)
    print("emp1 email after : ", emp1.email)

    print("emp1 fullname before :", emp1.fullname)
    emp1.fullname="Newfirst123 newlast123"
    print("emp1 fullname after :", emp1.fullname)
    print("emp1 first after : ", emp1.first)

    del emp1.fullname

    print(emp1.fullname)