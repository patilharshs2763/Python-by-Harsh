#The addition of factors of that given number is greater than itself it is called abundant number
num=int(input("Enter a number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum>num:
  print(num,'is Abundant Number')

else:
  print(num,'is not Abundant Number')