def hello():
  print("Hello Python")
hello()

def add(n1,n2):
    return n1+n2
n1=int(input("Enter n1: "))
n2=int(input("Enter n2: "))
res=add(n1,n2)
print("Addition:",res)

#Lambda Function
x = lambda a : a + 10
print(x(5))

a= lambda x : x*x*x
print(a(5))