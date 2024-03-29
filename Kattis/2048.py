def rotate(lr):  # l = 1, r = -1
    global tile
    new_board = []

    for j in range(3 * int(lr == 1), 4 * int(lr == -1) - int(lr == 1), -1 * lr):
        new_board += [[k[j] for k in tile[::lr]]]

    tile = new_board


def remove_space(to_l_r):
    global tile
    for j in tile:
        if j.count(0) == 0:
            continue
        while 0 in j:
            j.remove(0)
        while len(j) != 4:
            j.insert(len(j) * int(to_l_r == 1), 0)


def move_tile(l_r):  # l = 1, r = -1
    global tile

    # remove space
    remove_space(l_r)

    # same tile collision
    for j in range(4):
        for k in range((len(tile[j]) - 1) * int(l_r == -1),
                       (len(tile[j]) - 1) * int(l_r == 1), l_r):
            if tile[j][k] == tile[j][k + l_r]:
                tile[j][k] *= 2
                tile[j][k + l_r] = 0

    # remove space again
    remove_space(l_r)


if __name__ == '__main__':
    tile = []
    for i in range(4):
        tile += [[int(i) for i in input().split()]]

    position = int(input())
    if position % 2 == 0:
        move_tile(int(position == 0) * 2 - 1)
    else:
        rotate(1)
        move_tile(int(position == 1) * 2 - 1)
        rotate(-1)

    for row in tile:
        for item in row:
            print(item, end=' ')
        print()
