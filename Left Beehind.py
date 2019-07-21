while True:
    sweet, sour = map(int, input().split())
    if sweet + sour == 0:
        break
    else:
        print('Never speak again.') if sour + sweet == 13 \
            else print('Undecided.') if sour == sweet \
            else print('To the convention.') if sour < sweet \
            else print('Left beehind.')
