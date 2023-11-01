#Factorial using while loop
num=int(input("Enter a number:"))
t=num
fact=1
while num > 0:
    fact=fact*num
    num-=1
print("Factorial of",t,"=",fact)

#Factorial using for loop
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factoril of",num,"=",fact)