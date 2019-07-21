def longest():
    term = 0
    ans = [0,0]
    'ans = [terms,value]'
    i2 = 0

    for i in range(1,1000001):
        i2 = i
        term = 1

        while i2 != 1:
            if i2 % 2 == 0:
                i2 /= 2
                term += 1
            else:
                i2 = i2 * 3 + 1
                term += 1

        if term > ans[0]:
            ans = [term,i]

    return ans[1]


if __name__=='__main__':
    print(longest())
