for i in range(int(input())):
    sound, animal, temp = input().split(), [], [0]

    while temp[0] != 'what':
        temp = input().split()
        animal += [temp[-1]]

    for j in sound:
        print(j, end=' ') if j not in animal else 0
    print()
