# Q22-Names Score


def find_names_score():
    file = open('Q22-names.txt')
    name_list = file.read().split(',')
    x = 0
    for i in name_list:
        name_list.insert(x, i.strip('"'))
        name_list.pop(x + 1)
        x += 1
    x = 0
    name_list.sort()
    dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                  'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                  'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    summation = 0
    for string in name_list:
        for i in string:
            x += dictionary[i]
        summation += x * (name_list.index(string) + 1)
        x = 0
    print(summation)


if __name__ == '__main__':
    find_names_score()
