while True:
    repeat = int(input())

    if repeat < 0:
        break
    else:
        last_hours, total = 0, 0
        for i in range(repeat):
            speed, hours = map(int, input().split())
            total += speed * (hours - last_hours)
            last_hours = hours

        print(total, 'miles')
