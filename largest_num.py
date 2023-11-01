#Largest amoung 3 numbers
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
n3=int(input("Enter 3d number:"))

if n1>n2 and n1>n3:
    print(n1,"is greater")
elif n2>n1 and n2>n3:
    print(n2,"is greater")
else:
    print(n3,"is greater")

#largest amoun n numbers using while loop

n=int(input("Enter total numbers:"))
list=[]
for i in range(n):
    num=int(input("Enter number "))
    list.append(num)
print("Largest number is: ",max(list))
print("Smallest number is: ",min(list))