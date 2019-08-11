for case in range(int(input())):
    people, length = map(int, input().split())
    opinion = [0 for i in range(length)]

    for i in range(people):
        index = 0
        for letter in input():
            opinion[index] += int(letter)
            index += 1

    for i in opinion:
        print(0, end='') if i < people / 2 else print(1, end='')
    print()
