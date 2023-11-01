print("\n----------Sequenced data type----------")
# '''List is an ordered collection of similar or different types of items separated by commas and enclosed within brackets [ ]'''
# In Python, lists are used to store multiple data at once.
# Suppose we need to record the ages of 5 students. Instead of creating 5 separate variables, we can simply create a list.
# Example:Taking ages for 4 people
list_age=[54,29,65,45]
print(type(list_age))
print(list_age)      #Op:[54, 29, 65, 845]

# In Python, lists are ordered and each item in a list is associated with a number. The number is known as a list index.
# To access items from a list, we use the index number (0, 1, 2 ...).
print("Value in List of age at 0th index:",list_age[0])
print("Value in List of age at 1th index:",list_age[1])
print("Value in List of age at 2th index:",list_age[2])
print("Value in List of age at 3th index:",list_age[3])

# Negative Indexing in Python
# Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.
print("Value at -1 index: ",list_age[-1])
print("Value at -2 index: ",list_age[-2])
print("Value at -3 index: ",list_age[-3])
print("Value at -4 index: ",list_age[-4])

# A list can
# store elements of different types (integer, float, string, etc.)
# store duplicate elements

list=["Harsh",70,'A',77.53]
print(list)
list1=["Harsh",70,"Harsh",70]   #Storing duplicate elements!
print(list1)

# Slicing of a List
# In Python, it is possible to access a portion of a list using the slicing operator :
my_list=[10,50,"Harsh",55.2,"P"]
my_list1=['H','A','R','S','H','V','A','R','D','H','A','N']

print("From index 0 to 5: ",my_list1[0:5])  #items from 0 to index 4 will print
print("From index start (not defined) to 5: ",my_list1[:5])    #Means that it will print from '0' (Start) index
print("From index 5 to 12:",my_list1[5:12]) #items from 5 to  11 will print
print("From index 5 to end:",my_list1[5:])  #items from 5 to end will print
print("From beg to end:",my_list1[:])
print("From beg to 3:",my_list[0:3])

# Add Elements to a List
# Lists are mutable (changeable). Meaning we can add and remove elements from a list.
# Python list provides different methods to add items to a list.
# 1. Using append()
# The append() method adds an item at the end of the list
l1=[10,54,12,18,152]
l2=['H',780,42,"Harsh"]
print("Befor appending:",l1)
l1.append(20)
print("After appending:",l1)
x=21
l2.append(x)
print("After appending in l2:",l2)

# 2. Using extend()
# We use the extend() method to add all the items of an iterable (list, tuple, string, dictionary, etc.) to the end of the list. For example,
l1.extend(l2)
print("After extending list l1:",l1)

# 3. Using insert()
# We use the insert() method to add an element at the specified index => list.insert(index,value)
l2.insert(1,"P")
print("After inserting value at index 1(2nd position):",l2)

#Remove item from list
l2.remove('P')
print(l2)
del l2[1]   #deleting index 1 item
print(l2)
#nested list
ll=[10,54,[45,200],450,10,(10,540)]
print(ll)
ll[0]=11        #Changing elements of index 0
print(ll)
print(ll.count(10))

# The list pop() method removes the item at the specified index. The method also returns the removed item.
#If we not specifies the index value then it will remove last in.i.eLIFO
rem=ll.pop(0)
print("Removed item:",rem)
print(ll)