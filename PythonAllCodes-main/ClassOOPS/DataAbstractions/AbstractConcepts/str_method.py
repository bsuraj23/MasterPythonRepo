# __str__() Method
# The __str__() method in Python is a special method that is called by the str() built-in function and by the print function to compute the "informal" or nicely printable string representation of an object.
# It is meant to be overridden in user-defined classes to provide a meaningful string representation of the object.
# If __str__() is not defined in a class, the default implementation from the base class (usually object) is used, which typically returns a string that includes the object's memory address.
# Example of __str__() method in a user-defined class
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"
p = Person("Alice")
print(p)
