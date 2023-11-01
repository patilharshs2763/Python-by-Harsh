# Python Sets
# A set is a collection of unique data. That is, elements of a set cannot be duplicate. For example,
# Suppose we want to store information about student IDs. Since student IDs cannot be duplicate, we can use a set.
# In Python, we create sets by placing all the elements inside curly braces {}, separated by comma.

student_rno={11,12,13,14,15,"Hii",11}
print(type(student_rno))
print(student_rno)

# Create an Empty Set in Python
# Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.
# To make a set without any elements, we use the set() function without any argument. For example,
# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

# Add and Update Set Items in Python
# Sets are mutable. However, since they are unordered, indexing has no meaning.

# We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

# Add Items to a Set in Python
# In Python we use the add() method to add an item to a set. For example,
numbers = {21, 34, 54, 12}

print('Initial Set:',numbers)

# using add() method
numbers.add(32)

print('Updated Set:', numbers) 
numbers.insert(40)