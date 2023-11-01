# Python language offers some special types of operators like the identity operator and the membership operator. They are described below with examples.

# Identity operators
# In Python, is and is not are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

# Operator	Meaning	                                                                     Example
# is	    True if the operands are identical (refer to the same object)	             x is True
# is not	True if the operands are not identical (do not refer to the same object)     x is not True

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print("Memory location of x1:",id(x1))
print("Memory location of y1:",id(y1))

print(x1 is not y1)  # prints False

print("Memory location of x2:",id(x2))
print("Memory location of y2:",id(y2))
print(x2 is y2)  # prints True

print("Memory location of x3:",id(x3))
print("Memory location of y3:",id(y3))
print(x3 is y3)  # prints False

#  x3 and y3 are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.

x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True

# check if 'hello' is present in x string
print('hello' not in x)  # prints True

# check if '1' key is present in y
print(1 in y)  # prints True

# check if 'a' key is present in y
print('a' in y)  # prints False