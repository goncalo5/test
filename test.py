from time import time
from itertools import *


g = (x for x in range(10))

print(list(filter(lambda x: x % 2, g)))


def calc_primes(n):
    primes = [n for n in range(2, n + 1)]
    i = 0
    while i < len(primes):
        prime = primes[i]
        to_reduce = (n % prime or n == prime for n in primes)
        primes = list(compress(primes, to_reduce))
        i += 1
    return primes


def calc_primes1(n):
    primes = (n for n in range(2, n + 1))
    i = 0
    while True:
        # print primes, i
        try:
            # print(primes, list(primes))
            # print(type(primes))
            prime = next(primes)
            print(prime)

            # prime = primes[i]
        except StopIteration:
            break
        # print(5, prime, primes, list(primes))
        # for n in primes:
        #     print(n % prime or n == prime)
        primes = filter(lambda n: n % prime or n == prime, primes)
        primes, primes2 = tee(primes)
        print(6, list(primes2))
        # print(6, list(primes))
        i += 1
    return primes


def calc_primes2(n):
    primes = [n for n in range(2, n + 1)]
    i = 0
    while i < len(primes):
        prime = primes[i]
        primes = list(filter(lambda n: n % prime or n == prime, primes))
        i += 1
    return primes


def calc_primes3(n):
    primes = [n for n in range(2, n + 1)]
    i = 0
    while i < len(primes):
        prime = primes[i]
        new_primes = []
        for n in primes:
            if n % prime or n == prime:
                new_primes.append(n)
        primes = new_primes
        i += 1
    return primes


n = 10
t0 = time()
p0 = (calc_primes(n))
print (time() - t0)
t0 = time()
p1 = (calc_primes1(n))
print (list(p1))
print (time() - t0)
t0 = time()
p2 = (calc_primes2(n))
print (time() - t0)
t0 = time()
p3 = (calc_primes3(n))
print (time() - t0)
print (p1 == p0)
print (p1 == p2)
print (p1 == p3)
