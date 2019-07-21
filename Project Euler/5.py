# Q5-Smallest multiple


def find_smallest_multiple():
    x = 1
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    for i in prime:
        i_read = i
        while i_read <= 20:
            i_read *= i
        x *= int(i_read / i)
    return x


if __name__ == '__main__':
    print(find_smallest_multiple())
