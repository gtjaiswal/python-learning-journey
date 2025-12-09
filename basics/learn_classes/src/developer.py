from typing import List, Any

from employee import Employee


class Developer(Employee):

    def __init__(self,first="devFirst", last="devLast",language=None):
        print("calling Dev constructor")
        super().__init__(first, last)
        self.language = language

    raise_amount = 0.5

class Manager (Employee):

    def __init__(self, first="mgrFirst",last="mgrLast", reportees=None):
        print("calling Manager constructor")
        super().__init__(first,last)
        self.reportees = reportees if reportees is not None else []

    def add_reportee(self, reportee):
        if reportee not in self.reportees:
            self.reportees.append(reportee)

    def remove_reportee(self, reportee):
        if reportee in self.reportees:
            self.reportees.remove(reportee)

    def  list_reportees(self):
        return (rep.fullname() for rep in self.reportees)

if __name__ == "__main__":

    dev1 = Developer()
    print("dev1 = " , dev1.fullname(), dev1.language)

    # dev1.raise_amount = 3.50
    print(Employee.raise_amount)
    print(dev1.salary, dev1.raise_salary())

    manager1 = Manager()
    manager1.add_reportee(dev1)

    print(list(manager1.list_reportees()))
    print(*manager1.list_reportees())
