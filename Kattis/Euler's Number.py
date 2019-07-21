total, deno = 1, 1

for i in range(1, int(input()) + 1):
    deno *= i
    total += 1 / deno

print(total)
