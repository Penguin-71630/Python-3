# Q2-Even Fibonacci numbers

total, x, y = 0, 1, 2
while x <= 4000000:
    total += x if x % 2 == 0 else 0
    x, y = y, x + y
print(total)
