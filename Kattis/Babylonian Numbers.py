for i in range(int(input())):
    number = []
    for k in input().split(','):
        number.insert(0, int(k)) if k.isdigit() else number.insert(0, 0)
    print(sum(number[j] * (60 ** j) for j in range(len(number))))
