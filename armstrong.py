num=int(input("Enter a number:"))
temp=num
length=len(str(num))
sum=0
for i in range(1,num):
    rem=num%10
    sum=sum+rem**length
    num=num//10
if temp==sum:
    print(temp,"is an armstrong number")
else:
    print(temp,"is not an armstrong number")