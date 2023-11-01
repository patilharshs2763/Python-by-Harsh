#Perfect number is a no. of which the sum of diviser excepting that itself  equal to that number 
num=int(input("Enter a number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum=sum+i
if sum==num:
    print(num,"is perfect number")
else:
    print(num,"is not perfect number")