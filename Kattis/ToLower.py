p, t = map(int, input().split())
question = 0

for i in range(p):
    string = ''
    for j in range(t):
        string += input()[1:]
    question += bool(string.islower())

print(question)
