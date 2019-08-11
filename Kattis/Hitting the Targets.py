shape = []

for i in range(int(input())):
    command = input().split()
    shape += [list(map(lambda x: x if command.index(x) == 0 else int(x), command))]


def check():
    x, y = map(int, input().split())
    hitting = 0

    for j in shape:
        if j[0][0] == 'r':
            if j[1] <= x <= j[3] and j[2] <= y <= j[4]:
                hitting += 1
        elif j[0][0] == 'c':
            if ((x - j[1]) ** 2 + (y - j[2]) ** 2) ** 0.5 <= j[3]:
                hitting += 1

    print(hitting)


for i in range(int(input())):
    check()
