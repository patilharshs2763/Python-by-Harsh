
list_num = tuple(int(x) for x in input("Enter a tuple of numbers separated by spaces: ").split())
odd = []
even= []
for num in list_num:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Odd numbers in the list:", odd)
print("Even numbers in the list:", even)
