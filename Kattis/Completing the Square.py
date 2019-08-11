coord = []

for i in range(3):
    coord.append(list(map(int, input().split())))

# find the top of the current "quarter circle"
# c = coordinate
def dis(c1, c2): return (abs(c1[0] - c2[0]) ** 2 + abs(c1[1] - c2[1]) ** 2) ** 0.5


distance = [dis(coord[0], coord[1]) == dis(coord[0], coord[2]),
            dis(coord[0], coord[1]) == dis(coord[1], coord[2]),
            dis(coord[2], coord[1]) == dis(coord[0], coord[2])]

# find the forth top of the original square
differ = [coord[distance.index(False)][0] - coord[distance.index(True)][0],
          coord[distance.index(False)][1] - coord[distance.index(True)][1]]

print(coord[::-1][distance[::-1].index(False)][0] + differ[0],
      coord[::-1][distance[::-1].index(False)][1] + differ[1])
