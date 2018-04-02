import sys

def fac(n):
    return 1 if n == 1 else n * fac(n - 1)

try:
    print(fac(int(sys.argv[1])))
except:
    print("Please enter a number as an argument")
