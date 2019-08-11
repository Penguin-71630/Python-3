for i in range(int(input())):
    odd = []
    int(input())
    for number in input().split():
        if number not in odd:
            odd.append(number)
        else:
            odd.remove(number)
    print('Case #{}: {}'.format(i + 1, int(odd[0])))
