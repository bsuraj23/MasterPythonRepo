#code example for Public, Private and Protected Members

class Demo:
    def __init__(self):
        __a=90
        self.public = "park"
        self._protected = "cake"
        self.__private = "phone"
    def show(self):
        print(self.public, self._protected, self.__private)
        
    def display(self):
        print(self.__private)
d = Demo()
d.show()
# print(d.__a) # Error
print("public var is ",d.public)
print("Protected var is ",d._protected)
# print(d.__private) # Error
print("Private var is ",    d._Demo__private) # Access private
# Name mangling to access private member
# Private members are not accessible directly outside the class but can be accessed using name mangling.
# Protected members are accessible within the class and its subclasses but should be treated as non-public.
# Public members are accessible from anywhere.  
# In Python, these are just conventions and do not enforce access restrictions like in some other languages.
#mangling code example
class Test:
    def __init__(self):
        self.__private_var = 42  # Private variable

    def get_private_var(self):
        return self.__private_var  # Public method to access private variable   
t = Test()
# print(t.__private_var)  # This will raise an AttributeError   
print(t.get_private_var())  # This will work and print 42
print(t._Test__private_var)  # Accessing the private variable using name mangling   
# Name mangling is a mechanism in Python that alters the name of private variables to prevent accidental access and modification from outside the class.
# It is done by prefixing the variable name with _ClassName.

#TODO mangling