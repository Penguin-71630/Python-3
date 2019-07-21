n = int(input())
x = list(input() for i in range(n))

for i in range(1, len(x) - 1):
    if (x[i - 1] < x[i]) != (x[i] < x[i + 1]):
        print('NEITHER')
        break
else:
    print('INCREASING') if x[0] < x[1] \
        else print('DECREASING')
