# Q1-Multiples of 3 and 5
# Sol1 : 窮舉法

import time as t  # 計時用
start = t.time()

a = 1000
print(sum(i for i in range(a) if i % 3 == 0 or i % 5 == 0))

end = t.time()
print(end - start)

# Sol2 : 排容原理 (速度足足快了3.5倍)
start = t.time()


def sum_to(lim, factor):
    return factor * sum(i for i in range(1, int(lim / factor) + 1))


print(sum_to(a - 1, 3) + sum_to(a - 1, 5) - sum_to(a - 1, 15))

end = t.time()
print(end - start)
