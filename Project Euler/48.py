def last_ten_digits():
    total = 0
    for a in range(1, 1001):
        total += a ** a
    total = str(total)
    ans = total[len(total) - 10:]
    return ans


if __name__ == '__main__':
    print(last_ten_digits())
