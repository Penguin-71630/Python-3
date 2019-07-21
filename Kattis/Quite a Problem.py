import sys

for i in sys.stdin:
    print('no') if i.lower().count('problem') == 0 else print('yes')
