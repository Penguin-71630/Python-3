price = list(input().split())
price = [int(i) for i in price]

truck = []
for i in range(3):
    start, end = input().split()
    truck += [i for i in range(int(start), int(end))]
truck.sort()

total = 0

for i in truck:
    total += price[truck.count(i) - 1]
    i += 1

print(total)
