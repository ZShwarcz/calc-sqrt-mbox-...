import sys


class Poly:
    def __init__(self, t):
        self.t = t
        self.add = 0
        for line in t:
            self.add += 1 / float(line) * 3
        print(self.add)


def my_help():
    print("          For calculating poly write: python poly.py poly= numbers(0 1 2 3 ... n)\n")


try:
    if len(sys.argv) == 1:
        print("      This program to work with command line arguments")
        print("      For help write: python poly.py -help")
        exit()
    elif sys.argv[1] == '-help':
        my_help()
    elif sys.argv[1] == 'poly=':
        """for string error"""
        for i in sys.argv[2:]:
            float(i)
        test = Poly(sys.argv[2:])
    else:
        print("wrong argument command line")
except Exception:
    print(sys.exc_info()[1])
    exit()



