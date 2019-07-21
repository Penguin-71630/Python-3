# Q21-Amicable numbers
x = 0
xf = 0
y = 0
yf = 0
ans = 0
for x in range(1, 10000):
    xf = 0
    yf = 0
    for i in range(1, x):
        if x % i == 0:
            xf += i
    y = xf
    for j in range(1, y):
        if y % j == 0:
            yf += j
    if x == yf and x != y:
        print(x, ',', y)
        ans += x
        ans += y
ans /= 2
print(int(ans))
