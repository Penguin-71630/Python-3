def compute():
    sum = 0
    for i in range(2, 1000000):
        if i == five_power_digit_sum(i):
            sum += i
    return sum


def five_power_digit_sum(n):
    five_power = sum(int(str(n)[i]) ** 5
                     for i in range(0, len(str(n))))
    return five_power


if __name__ == '__main__':
    print(compute())
