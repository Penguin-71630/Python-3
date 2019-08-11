# dom = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
# n_dom = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
card = 'AKQJT987'
score = [11, 4, 3, 20, 10, 14, 0, 0,
         11, 4, 3, 2, 10, 0, 0, 0]

repeat, dominant = input().split()
summation = 0

for i in range(int(repeat) * 4):
    having = input()
    summation += score[card.index(having[0]) +
                       int(int(having[1] != dominant) * len(score) / 2)]

print(summation)
