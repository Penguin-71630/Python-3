def triplet():
    a=0
    b=0
    c=0
    ans=0

    for a in range(1,999):
        for b in range(1,999):
            c=1000-a-b
            if a ** 2 + b ** 2 == c ** 2:
                ans = a * b * c
                return ans
                break
            elif a ** 2 + c ** 2 == b ** 2:
                ans = a * b * c
                return ans
                break
            elif b ** 2 + c ** 2 == a ** 2:
                ans = a * b * c
                return ans
                break
        if ans != 0:
            break


if __name__=='__main__':
    print(triplet())