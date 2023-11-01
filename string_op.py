# In computer programming, a string is a sequence of characters. For example, "hello" is a string containing a sequence of characters 'h', 'e', 'l', 'l', and 'o'.
# We use single quotes or double quotes to represent a string in Python.In Python, strings are immutable. That means the characters of a string cannot be changed.

str="Harsh"
print("Length:",len(str))
print("Name:",str)
# We can access the characters in a string in three ways.
# Indexing: One way is to treat strings as a list and use index values. 
print("1st index element: ",str[1])
print("Element at -1 index:",str[-1])   #Negative Indexing: Similar to a list, Python allows negative indexing for its strings.It is nothing but value at tot length of string-that negative index value
print("From 1 to 4 index(Position 3):",str[1:4]) #Slicing: Access a range of characters in a string by using the slicing operator colon :
str2="Patil"
str3="harsh"
print("Equal string:",str==str3)
#We can iterate through a string using a for loop. 
for letter in str2:
    print(letter)
print("String in Upper case:",str.upper())
print("String in Lower case:",str.lower())
print(str.replace("Harsh","Harsh Patil"))
str1="Harsh Patil"
# We can test if a substring exists within a string or not, using the keyword in.
print(str1.count("Harsh"))
print("Is end with l?:",str1.endswith("l"))
print("l" in str1)
print("rs" not in str1)

String = 'HARSH'
#Syntax:
# slice(stop)
# slice(start, stop, step) where step is nothing bt index inc/dec
# Using slice constructor
s1 = slice(1)
s2 = slice(1, 5, 2)
s3 = slice(-1,-5, -1)
 
print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# Method 2:
# Syntax:
# arr[start:stop]         # items start through stop-1
# arr[start:]             # items start through the rest of the array
# arr[:stop]              # items from the beginning through stop-1
# arr[:]                  # a copy of the whole array
# arr[start:stop:step]    # start through not past stop, by step

# Python program to demonstrate
# string slicing

# String slicing
String = 'HarshvardhanPatil'

# Using indexing sequence
print(String[:3])
print(String[1:5:2])
print(String[-1:-12:-2])
print(String[::-1])