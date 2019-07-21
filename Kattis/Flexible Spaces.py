room, partition = map(int, input().split())
width = [int(i) for i in [0] + input().split() + [room]]

possible = []
for i in range(0, len(width)):
    for j in width[i:]:
        if j - width[i] not in possible:
            possible += [j - width[i]]

possible.remove(0)
possible.sort()

for i in possible:
    print(i, end=' ')
