import math

#-------------------------------------------------------------------------------

def primerange(top):
    primes = []
    for i in range(3,top,2):
        prime = True
        for j in range(int(i**0.5),int(i/2)):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return (primes)

def primesbelow(top):
    sum = 0
    pbsqrt = primerange(int(math.sqrt(top))+1)
    curprimes = range(3,top,2)
    primes = [2]
    for i in curprimes:
        prime = True
        for j in pbsqrt:
            if (i % j == 0) and i != j:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes
