while True:
    side = [int(i) for i in input().split()]
    side.sort()
    if sum(i for i in side) == 0:
        break
    else:
        print('right') if side[0] ** 2 + side[1] ** 2 == side[2] ** 2 \
            else print('wrong')
