import math


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
    print sum(y)


def e4():
    p = 0
    for i in range(100,999):
        for j in range(100,999):
            if str(i*j)==str(i*j)[::-1]:
                if i*j > p: p = i*j
    print p

def primeRange(top):
    primes = []
    for i in range(3,top,2):
        prime = True
        for j in range(int(i**0.5),int(i/2)):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)

def e10():
    sum = 2
    for i in range(3,2000000,2):
        prime = True
        for j in range(int(i**0.5),int(i/2)):
            if i % j == 0:
                prime = False
                break
        if prime:
            sum += i
    print sum


#-------------------------------------------------------------------------------


euler = {1:e1, 2:e2, 4:e4, 10:e10}

def main():
    euler[input("Which Euler? ")]()

if __name__ == "__main__":
    main()
