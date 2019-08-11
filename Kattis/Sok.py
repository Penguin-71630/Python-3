def ipt(): return list(map(int, input().split()))


fruit, recipe, smallest = ipt(), ipt(), 10 ** 3
for i in range(len(fruit)):
    porp = fruit[i] / recipe[i]
    smallest = porp if porp < smallest else smallest

for i in range(len(fruit)):
    print(fruit[i] - smallest * recipe[i], end=' ')
