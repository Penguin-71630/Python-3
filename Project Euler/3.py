# Q3-Largest prime factor
# 1 = prime

import math as m
result = 0


def smallest_pf(n):
    global result
    for i in range(2, n+1):
        if n % i == 0:
            result = 1
            for j in range(2, int(m.sqrt(i))+1):
                if i % j == 0:
                    result = 0
                    break
            if result == 1:
                return i


x = 600851475143
divisor = 0

while x != 1:
    divisor = smallest_pf(x)
    x = x // divisor

print(divisor)
