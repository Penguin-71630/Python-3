total = 0

for i in range(int(input())):
    string = input()
    total += int(string[:-1]) ** int(string[-1])

print(total)
