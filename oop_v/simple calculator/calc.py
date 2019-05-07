# simple calculator

import sys


class Calc:
    def __init__(self, a, b, c):
        """initiate variables"""
        self.a = a
        self.b = b
        self.c = c

    def calculate(self):
        """calculate values"""
        if self.c == '+':
            """addition"""
            print(float(self.a + self.b))
        elif self.c == '-':
            """subtraction"""
            print(self.a - self.b)
        elif self.c == '/' and self.b != 0:
            """division"""
            print(self.a / self.b)
        elif self.c == '*':
            """multiplication"""
            print(float(self.a * self.b))
        else:
            print(" b not can = 0")


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
        test.calculate()



