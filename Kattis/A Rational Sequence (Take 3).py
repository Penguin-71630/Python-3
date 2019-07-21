def find_next(lr):
    global p, q
    if lr == '1':
        p += q
    else:
        q += p


for i in range(int(input())):
    index, rational = input().split()
    rational = bin(int(rational))[3:]

    p, q = 1, 1
    for j in rational:
        find_next(j)

    print(index, p, end='', )
    print('/', end='')
    print(q)
