for i in range(int(input())):
    n = int(input())
    print(n, 'is', end=' ')
    print('odd') if n % 2 == 1 else print('even')
