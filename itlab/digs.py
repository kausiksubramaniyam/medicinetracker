digits=[4,3,2,1]
j=len(digits)-1
k=1
num=0
while j>=0:
    num=digits[j]*k+num
    k=k*10
    j-=1
print(num)