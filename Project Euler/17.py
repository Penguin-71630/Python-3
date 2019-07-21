n1_19 = ['', 'one', 'two', 'three', 'four', 'five'
    , 'six', 'seven', 'eight', 'nine', 'ten'
    , 'eleven', 'twelve', 'thirteen', 'fourteen'
    , 'fifteen', 'sixteen', 'seventeen'
    , 'eighteen', 'nineteen']
n20_90 = {20: 'twenty', 30: 'thirty', 40: 'forty',
          50: 'fifty', 60: 'sixty', 70: 'seventy',
          80: 'eighty', 90: 'ninety'}
t = 'thousand'
h = 'hundred'

if __name__ == '__main__':
    e = 0
    letter_sum = 0
    num = int(input('number:  (1 to 1000)'))
    if len(str(num)) == 4:
        letter_sum += len(n1_19[int(str(num)[0])]) + len(t)
        print(letter_sum)  # testing
    elif len(str(num)) == 3:
        letter_sum += len(n1_19[int(str(num)[0])]) + len(h)
        print(letter_sum)  # testing
