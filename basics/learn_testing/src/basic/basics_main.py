def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def times(a,b):
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError ("Cant divide by 0")
    return a/b
