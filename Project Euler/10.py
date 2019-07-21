# Q10-Summation of primes
sum = 0
result = 0
'''
0=not prime
1=prime
'''

import math as m


def find(n):
    result = 1
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            result = 0
            return result
            break
    if result == 1:
        return result


for j in range(2, 2000000):
    result = find(j)
    if result == 1:
        sum += j
print(sum)
