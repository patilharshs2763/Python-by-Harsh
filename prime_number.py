#Prime number using while loop
num=int(input("Enter a number:"))
i=2
flag=0
while i<num:
    if (num%i)==0:
        flag=1
    i+=1
if flag==1:
    print(num,"is not prime")
else:
    print(num,"is prime") 

#Prime number using for loop
num=int(input("Enter a number:"))
flag=0
for i in range(2,num):
    if (num % i) == 0:
        flag=1
if flag==1:
    print(num,"is not prime")
else:
    print(num,"is prime")