# Python Tuple Data Type
# Tuple is an ordered sequence of items same as a list.A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.Tuples once created cannot be modified.tuples are immutable
# In Python, we use the parentheses () to store items of a tuple.
tpl=(70,"Harsh",77.53,"A")
print(type(tpl))
print(tpl)

# Access Tuple Items
# Similar to lists, we use the index number to access tuple items in Python 
print("Value at index 1:",tpl[1])
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

var1 = ("Hello") # string
var2 = ("Hello",) # tuple       #Comma is required in tuple to indicate it is tuple
print(type(var1),type(var2))

print(tpl[::-1])
tuple=(45,4,"harsh","SDf",45055,45.12)
s1=slice(1,4)
print(tuple[s1])