# simple calculator

import sys


class Calc:
    def __init__(self, a, b, c):
        """initiate variables"""
        self.a = a
        self.b = b
        self.c = c

    def addition(self, a, b):
        """addition"""
        print(float(self.a + self.b))

    def subtraction(self, a, b):
        """subtraction"""
        print(float(self.a - self.b))

    def division(self, a, b):
        if self.b != 0:
            """division"""
            print(self.a / self.b)
        else:
            print(" b not can = 0")

    def multiplication(self, a, b):
        """multiplication"""
        print(float(self.a * self.b))


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

        test = Calc(a, b, c)
        if c == '+':
            test.addition(a, b)
        elif c == '-':
            test.subtraction(a, b)
        elif c == '/':
            test.division(a, b)
        elif c == '*':
            test.multiplication(a, b)
        else:
            print("ALLERT")



