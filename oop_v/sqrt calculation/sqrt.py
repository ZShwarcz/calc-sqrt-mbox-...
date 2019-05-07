# sqrt calculation

import sys


class Sqrt:
    def __init__(self, a, e):
        """initiate val"""
        self.a = a
        self.e = e
        self.i = 0
        self.temp = 0

    def calc_sqrt(self):
        """sqrt calculation"""
        while self.i < 10000:
            self.e = 0.5*(self.e + self.a / self.e)
            if self.e == self.temp:
                break
            self.i += 1
            self.temp = self.e
            print(self.temp)
        print("sqrt from " + str(self.a) + " = " + str(self.e))


try:
    a = float(input("enter a: "))
    if a < 0:
        print("NINE")
        exit("a < 0")
    e = float(input("enter e: "))

except Exception:
    print(sys.exc_info()[1])

else:
    test = Sqrt(a, e)
    test.calc_sqrt()
