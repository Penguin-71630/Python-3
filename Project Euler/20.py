#Q20-Factorial digit sum
x=1
sum=0
for i in range(1,101):
    x *= i
x=str(x)
for j in range(0,len(x)):
    sum += int(x[j])
print(sum)
