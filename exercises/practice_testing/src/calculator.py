class Calculator:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def is_even(self, num):
        return num % 2 == 0

# calc = Calculator()
# print(calc.add(2,3))