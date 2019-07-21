# Q29-Distinct Powers
x = []
for a in range(2, 101):
    for b in range(2, 101):
        x.append(a**b) if a**b not in x else False
print(len(x))
