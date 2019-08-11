crd = [list(map(int, input().split())), list(map(int, input().split()))]
rest = (int(input()) - (abs(crd[0][0] - crd[1][0]) + abs(crd[0][1] - crd[1][1])))
if rest >= 0 and rest % 2 == 0:
    print('Y')
else:
    print('N')
