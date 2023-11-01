import array as arr
a=arr.array('i',[10,45,1,55,78,31,44,12,10])
print("Legth of array:",len(a))
print(type(a))
print("First Element:",a[0])
print("Second Element:",a[1])
print("Third Element:",a[2])
print(a)
print("Priinting all elements:")
for i in range(len(a)):
    print("Elemet at index",i,":",a[i])

#Slicing array
print("Index 2 to 5:",a[2:5])
print("Index 5 to end",a[5:])
print("Index 5 to end",a[5:])
print("Beg to 3 index:",a[:-6])
print("Beg to End:",a[:])

#Changing element in array.Arrays are mutable
a[0]=63
print(a[:])
a[2:5]=arr.array('i',[451,412,410])      #changing 3rd to 5th element
print(a)

#adding element in array
a.append(100)
print(a)
