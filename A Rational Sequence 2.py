def find_last():
    global p, q, record
    if p > q:
        record += '1'
        p -= q
    else:
        record += '0'
        q -= p


for i in range(int(input())):
    index, rational = input().split()
    p, q = rational.split('/')
    p, q = int(p), int(q)
    del rational

    record = ''
    while p + q != 2:
        find_last()
    record = '1' + record[::-1]

    print(index, int(record, 2))
