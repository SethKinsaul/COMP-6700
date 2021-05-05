#Seth Kinsaul (smk0036@auburn.edu)
#COMP 6700 Software Process
#Assignment 2
#Primes that will return from start to end
import math
def primesInRange(start, end):
    primes = []
    for n in range(start, end + 1):
        if n >  1:
            if (n == 2):
                primes.append(n)
            for i in range(2, n):
                if (n % i) == 0:
                    break
                else:
                    if (n not in primes and is_prime(n)):
                        primes.append(n)
    return primes

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True