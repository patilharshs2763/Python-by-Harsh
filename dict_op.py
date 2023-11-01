# Python dictionary is an ordered collection of items. It stores elements in key-value pairs.
# Here, keys are unique identifiers that are associated with each value.
# We create dictionaries by placing key:value pairs inside curly brackets {}, separated by commas. 

student={10:"Harsh",20:"Rohit",30:"Rohan","Y":3}
print(student)

# Access Dictionary Items
# We can access the value of a dictionary item by placing the key inside square brackets.
print(student[20])

# Change Dictionary Items
# Python dictionaries are mutable (changeable). We can change the value of a dictionary element by referring to its key.
student[20]="Ram"
print(student)

# Add Items to a Dictionary
# We can add an item to the dictionary by assigning a value to a new key (that does not exist in the dictionary). 

student[40]="Sham"
print(student)

# Remove Dictionary Items
# We use the del statement to remove an element from the dictionary.

del student[40]
print(student)

# If we need to remove all items from the dictionary at once, we can use the clear() method.
# student.clear()
# print(student)

# get() method returns a default value if the key is missing.
# However, if the key is not found when you use dict[key], KeyError exception is raised.

name=student.get(10)
print(name)
print(student["Y"])

print(student.get(50))  #Using get() results in None
# print(student[50])      #Using [] results in KeyError

# The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order.

# Returns the latest inserted element (key,value) pair from the dictionary.
# Removes the returned element pair from the dictionary.

rem=student.popitem()
print("Removed item:",rem)
print(student)