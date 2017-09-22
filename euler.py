import math
import eulerfuncs

#-------------------------------------------------------------------------------


def e1():
    print sum((i for i in range(1000) if i % 3 == 0 or i % 5 == 0))


def e2():
    x = 1
    fibs = [1]
    while x < 4000000:
        fibs.append(x)
        x = fibs[-1] + fibs[-2]
    y = (i for i in fibs if i % 2 == 0)
    return sum(y)

def e3():
    ans = 0
    for i in eulerfuncs.primesbelow(775146):
        if 600851475143 % i == 0:
            ans = i
    return ans

def e4():
    p = 0
    for i in range(100,999):
        for j in range(100,999):
            if str(i*j)==str(i*j)[::-1]:
                if i*j > p: p = i*j
    return p


def e10():
    return sum(eulerfuncs.primesbelow(2000000))


#-------------------------------------------------------------------------------


euler = {1:e1, 2:e2, 3:e3, 4:e4, 10:e10}

def main():
    print euler[input("Which Euler? ")]()

if __name__ == "__main__":
    main()
