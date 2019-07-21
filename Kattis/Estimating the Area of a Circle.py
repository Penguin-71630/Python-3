import math as m

in_put = []
while True:
    in_put = [float(i) for i in input().split()]
    if sum(i for i in in_put) == 0:
        break

    in_put = [in_put[0] ** 2 * m.pi,
              (in_put[0] * 2) ** 2 * (in_put[2] / in_put[1])]

    for i in in_put:
        print(i, end=' ')
    print()
