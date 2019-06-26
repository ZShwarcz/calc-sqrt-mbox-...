import sys


def addition(a, b):
    """addition"""
    return float(a + b)


def subtraction(a, b):
    """subtraction"""
    return float(a - b)


def division(a, b):
    if b != 0:
        """division"""
        return a / b
    else:
        print(" b not can = 0")


def multiplication(a, b):
    """multiplication"""
    return float(a * b)


print("this is calc")
while True:
    try:
        q = input("Continue? (y\\n): ")
        if q == 'n':
            exit()
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = input("Enter C(+-*/): ")

    except Exception:
        print("Ou wrong value!!!")
        print(sys.exc_info()[1])
    else:
        if c == '+':
            print(addition(a, b))
        elif c == '-':
            print(subtraction(a, b))
        elif c == '/':
            print(division(a, b))
        elif c == '*':
            print(multiplication(a, b))
        else:
            print("ALLERT")

