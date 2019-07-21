#Q28-Number spiral diagonals

sum=0
x=1
d=2
while d<=1000:
    for i in range(1,5,1):
        sum+=x
        x+=d
    d+=2
sum+=x
print(sum)
