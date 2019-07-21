# Q4-Largest palindrome product

import time as t
# Sol1  [ 18 行 (不含註解和空行) ]
start = t.time()

n = 0
digit = 0
opposite = 0
a = 0
ans = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        n = i*j
        a = n
        opposite = 0
        digit = 0
        while a > 0:
            digit = a % 10
            opposite = opposite * 10 + digit
            a = a // 10
        if n == opposite:
            if n > ans:
                ans = n
print(t.time() - start)
print(ans)

del a, n, digit, opposite

# Sol2 (速度約是Sol1的30倍)  [ 7 行 (不含註解和空行) ]
start = t.time()

ans, record = 0, 0
for i in range(999, 99, -1):
    record = i
    for j in range(999, 99, -1):
        ans = i * j if i * j == int(str(i * j)[::-1]) and ans < i * j else ans

    if record * 999 < ans:
        break

print(t.time() - start)
print(ans)


