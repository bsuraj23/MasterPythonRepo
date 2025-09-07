# Different Data Types in Python

#Immutable: int, float, str, tuple, frozenset, etc.

#Mutable: list, dict, set, bytearray, etc.
#none is also a Datatype 
array = [1, 2, 3, 4, 5]         
print(type(array))
matrix = [[1, 2, 3], [4, 5, 6]]  
print(type(matrix))
vector = (1, 2, 3)          
print(type(vector))         
data_set = {1, 2, 3, 4}                 

print(type(data_set))
dictionary = {"name": "Alice", "age": 30}           
print(type(dictionary))             
print("")           
#none data type
x = None
print(type(x))
print(x)

# A key difference between bytes and strings 
# is that bytes are immutable and do
# not support most string methods directly. 
# For example, you cannot concatenate a bytes
# object with a string without explicit conversion
b = b"Hello"
print(type(b))


print(b)
print(b.decode("utf-8"))  # Convert bytes to string
print(type(b.decode("utf-8")))
print("")
#bytearray
ba = bytearray([65, 66, 67])
print(type(ba))
print(ba)
print(ba.decode("utf-8"))
print(type(ba.decode("utf-8")))
print("")
#memoryview
mv = memoryview(b"Hello")
print(type(mv))
print(mv)
print(mv.tobytes())
print(mv.tobytes().decode("utf-8"))
print(type(mv.tobytes().decode("utf-8")))
print("")
# Unlike Java, Python does not have a built-in array type for
# general use. 
# The closest built-in structure is the list,
# which is more flexible than Java arrays
# because it can hold elements of different types
# and can change size.

#range is used to generate a sequence of numbers
#range is also a data type in python
r = range(5)
print(type(r))
print(list(r))  # Convert range to list for display
print("")
#frozenset is an immutable version of a set
fs = frozenset([1, 2, 3, 4, 5])
print(type(fs))
print(fs)       
print("")
   