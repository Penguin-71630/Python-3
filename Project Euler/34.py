# Q34-Digit factorials
# unsolved


def factorial(a):
    fac = 1
    for i in range(a, 0, -1):
        fac *= i
    return fac


def take_number_apart(a):
    fac_sum = 0
    for j in str(a):
        fac_sum += factorial(int(j))
    return fac_sum


# find the limit
k = 9
summation = 0
while k < take_number_apart(k):
    k = k * 10 + 9

for n in range(3, k+1, 1):
    summation += n if n == take_number_apart(n) else False
print(summation)
