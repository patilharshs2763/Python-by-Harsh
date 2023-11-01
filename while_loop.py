print("----------1st Example----------")
a=0
n=5
while a<=n:
    print(a,"\t",end="")
    a+=1
print("\n----------2nd Example----------\n")
x=2
y=1
while y<=10:
    print(x,"*",y,"=",x*y)
    y=y+1
print("----------3rd Example----------")

tot=0
num=int(input("Enter number: "))
while num!=0:
    tot+=num
    num=int(input("Enter number: "))
print("Total=",tot)
# print("----------3rd Example----------")
# n=2
# while n<=10:
#     print(n)
#     n