mode, string = input().split()
if mode == 'E':
    while True:
        if string == '':
            break

        str_record = string
        string = string.lstrip(str_record[0])

        print('{}{}'.format(str_record[0], len(str_record) - len(string)), end='')
else:
    for i in range(0, len(string), 2):
        for j in range(int(string[i + 1])):
            print(string[i], end='')
