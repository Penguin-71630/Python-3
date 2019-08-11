while True:
    repeat = int(input())
    if repeat == 0:
        break

    order = []
    for i in range(repeat):
        order += [input().split()]
    order.sort()

    menu = []
    for i in order:
        for j in i[1:]:
            if j not in menu:
                menu += [j]
    menu.sort()

    for dish in menu:
        print(dish, end=' ')
        for person in order:
            if dish in person:
                print(person[0], end=' ')
        print()
    print()
