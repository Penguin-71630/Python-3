while True:
    repeat = int(input())
    if repeat == 0:
        break

    list_one = [int(input()) for i in range(repeat)] + \
               [0 for i in range(repeat)]

    list_temp = [i for i in list_one[:repeat]]
    list_temp.sort()

    for i, item in enumerate(list_temp):
        list_one[list_one.index(item) + len(list_temp)] = i

    list_two = [int(input()) for i in range(repeat)]
    list_two.sort()

    for i in list_one[repeat:]:
        print(list_two[i])

    print()
