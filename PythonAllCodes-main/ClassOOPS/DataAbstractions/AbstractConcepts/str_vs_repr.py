# Difference between str() and repr() Functions
# In Python, both str() and repr() are built-in functions that return string representations of objects, but they serve different purposes and are used in different contexts.
# str() is intended to produce a "pretty" or user-friendly string representation of an object
# repr() is intended to produce a string representation that is more suitable for debugging and development, often including more detail about the object
# The goal of repr() is to be unambiguous and, if possible, to produce a string that could be used to recreate the object using eval()
# The goal of str() is to be readable and user-friendly
class Demo:
    def __str__(self):
        return "str called"
    def __repr__(self):
        return "repr called"
d = Demo()
print(str(d))
print(repr(d))


#Add more exmpale where str and repr differ
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(str(p))  # Output: Alice, 30 years old (user-friendly)
print(repr(p))  # Output: Person(name='Alice', age=30) (developer-friendly)