lights, time = map(int, input().split())
wait = 0

for i in range(lights):
    d, r, g = map(int, input().split())
    wait += (r - (wait + d) % (r + g)) * int(r - (wait + d) % (r + g) >= 0)

print(time + wait)
