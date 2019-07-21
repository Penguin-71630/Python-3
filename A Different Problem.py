import sys

for i in sys.stdin:
    x, y = map(int, i.split())
    print(abs(x - y))
