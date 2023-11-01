# if the sum of the digits can perfectly divide the number or not.
num=tmp=int(input("Enter a number: "))
sum=0
while num>0:
    rem=num%10
    sum+=rem
    num//=10
if tmp%sum==0:
    print(tmp,"is Harshad number!")
else:
    print(tmp,"is NOT Harshad number!")