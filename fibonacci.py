#0 1 1 2 3 5 8 13 21 34.....

n=int(input("Enter a number: "))
n1,n2=0,1
print(n1,"\t",n2,"\t",end="")
for i in range(2,n):
    n3=n1+n2
    print(n3,"\t",end="")
    n1=n2
    n2=n3

#another loop
n=int(input("\nEnter a number: "))
n1,n2=0,1
print(n1,"\t",n2,"\t",end="")
i=3
while i<=n:
    n3=n1+n2
    print(n3,"\t",end="")
    n1=n2
    n2=n3
    i+=1