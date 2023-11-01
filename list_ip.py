list=[]
print(type(list))
size=int(input("Enter size of list:"))
for i in range(1,size+1):
    element=input("Enter element in list:")
    # list.insert(1,num)
    list.append(element)
print(list)
print("------------------------------")
tuple=(10,45,"g",4,45.5)
print(type(tuple))
s1=slice(2)
s1=slice(1,3)
print(tuple[s1])
print(tuple[-1:-4:-1])


