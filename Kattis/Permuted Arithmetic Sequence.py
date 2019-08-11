for i in range(int(input())):
    seq = list(map(int, input().split()[1:]))
    d = seq[1] - seq[0]

    for j in seq:
        if not j == seq[0] + seq.index(j) * d:
            break
    else:
        print('arithmetic')
        continue

    seq.sort()
    d = seq[1] - seq[0]
    for j in seq:
        if not j == seq[0] + seq.index(j) * d:
            break
    else:
        print('permuted arithmetic')
        continue

    print('non-arithmetic')
