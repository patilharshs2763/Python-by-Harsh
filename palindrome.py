#151
num=int(input("Enter number: "))
tmp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if tmp==rev:
    print(tmp,"is palindrome")
else:
    print(tmp,"is NOT palindrome")

#Palindrome String logic 1
str=temp=input("Enter string:")
str=str.lower()
s=slice(-1,-100,-1)
if str==str[s]:
    print(temp,"is palindrome")
else:
    print(temp,"is NOT palindrome")

#Palindrome String logic 2
str=temp=input("Enter string:")
str=str.casefold()
if str==str[::-1]:
    print(temp,"is palindrome")
else:
    print(temp,"is NOT palindrome")

#Palindrome String logic 3
str=temp=input("Enter string:")
str2=""
for i in str:
    str2=str2+i
if str==str2:
    print(temp,"is palindrome")
else:
    print(temp,"is NOT palindrome")