#Q6-Sum square difference

x=0
y=0
for i in range(1,101,1):
    x += i**2
    y += i
print(y**2-x)
