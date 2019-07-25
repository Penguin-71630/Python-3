kitten_position = input()
branch = []

while True:
    input_branch = input().split()
    if input_branch[0] == '-1':
        break
    else:
        branch += [input_branch]


def next_step():
    global kitten_position
    print(kitten_position, end=' ')
    end_code = False

    for k in branch:
        if kitten_position in k[1:]:
            kitten_position = k[0]
            end_code = True
            break

    if end_code:
        next_step()


next_step()
