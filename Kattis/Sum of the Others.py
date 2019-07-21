import sys

for i in sys.stdin:
    print(int(sum(int(y) for y in i.split()) / 2))
