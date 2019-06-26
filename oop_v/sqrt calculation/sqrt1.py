import sys

def calc_sqrt(a, e):
    """sqrt calculation"""
    i = 0
    temp = 0
    while i < 10000:
        e = 0.5 * (e + a / e)
        if e == temp:
            break
        i += 1
        temp = e
        print(temp)
    print("sqrt from " + str(a) + " = " + str(e))

try:
    a = float(input("enter a: "))
    if a < 0:
        print("NINE")
        exit("a < 0")
    e = float(input("enter e: "))

except Exception:
    print(sys.exc_info()[1])

else:
    calc_sqrt(a, e)