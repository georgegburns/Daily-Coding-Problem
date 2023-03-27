# This problem was asked by Alibaba.
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
# A solution will always exist. See Goldbach’s conjecture.
# Example:
# Input: 4
# Output: 2 + 2 = 4
# If there are more than one solution possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
# [a, b] < [c, d]
# If a < c OR a==c AND b < d.

import time

def SieveofEratosthenes(n : int):
    # a list of possible primes
    primes = list(range(2, n+1))
    
    # 2 is the first prime
    i = 2
    
    # the sieve works by removing every number that is a multiple of a prime starting at the first prime 2
    while i * i <= n:        
        for j in range(i * i, n+1, i):
            if (j in primes):
                primes.remove(j)
        i += 1
    return primes


def Goldbachsconjecture(n : int):
    st = time.time()
    # using the sieve to generate the prime numbers up to the required result
    lst = SieveofEratosthenes(n)
    for i in lst: 
        for j in reversed(lst):
            # by working in both directions it garuantees the smallest first number + the smallest second number
            if i + j == n:
                result = (j,i)
    ed = time.time()
    elapse = ed - st
    print(f'Completed in {round(elapse, 2)} seconds')
    return result
            
print(Goldbachsconjecture(5000))