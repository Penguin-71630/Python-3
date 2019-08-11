def switch(code):
    global ball
    if code == 'A':
        ball = ball[:2][::-1] + [ball[-1]]
    elif code == 'B':
        ball = [ball[0]] + ball[1:][::-1]
    elif code == 'C':
        ball = ball[::-1]


ball = [1, 0, 0]
for i in input():
    switch(i)

print(ball.index(1) + 1)
