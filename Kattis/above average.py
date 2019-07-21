for i in range(int(input())):
    a = input().split()
    x = [int(i) for i in a]
    del a

    average = (sum(i for i in x) - x[0]) / x[0]
    x.pop(0)

    higher = 0
    for j in x:
        higher += 1 if j > average else 0

    ratio = '%.3f' % (100 * higher / len(x)), '%'
    a = ''
    print(a.join(ratio))
