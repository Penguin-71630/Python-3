# Q7-10001st prime
count = 0
num = 2
result = 0

import math as m


def find_prime(n):
    result = 'true'
    for i in range(2, int(m.sqrt(n)) + 1):
        if n % i == 0:
            result = 'false'
            return result
            break
    if result == 'true':
        return result


while count < 10001:
    result = find_prime(num)
    if result == 'true':
        count += 1
    if count == 10001:
        break
    num += 1
print(num)
