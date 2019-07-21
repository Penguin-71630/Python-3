pattern = []
for i in range(3):
    line = [int(j) for j in input().split()]
    pattern += [line]


def find_index(number):
    global pattern
    for k in range(3):
        if number in pattern[k]:
            return [k, pattern[k].index(number)]


def find_distance(current):
    global last_index
    return ((abs(last_index[0] - current[0]) ** 2) +
            (abs(last_index[1] - current[1]) ** 2)) ** 0.5


last_index = find_index(1)
distance = 0

for i in range(2, 10):
    distance += find_distance(find_index(i))
    last_index = find_index(i)

print(distance)
