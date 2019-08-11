int(input())
print(len(list(filter(lambda x: True if x < 0 else False,
                      list(map(int, input().split()))))))
