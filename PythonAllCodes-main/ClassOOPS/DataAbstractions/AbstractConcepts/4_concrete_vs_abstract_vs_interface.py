#code example for  Concrete Class vs Abstract Class vs Interface
# Concrete Class: A concrete class is a regular class that can be instantiated and contains implementations for all its methods.
# Abstract Class: An abstract class is a class that cannot  be instantiated on its own and is meant to be subclassed.
# It can contain abstract methods (methods without implementation) that must be implemented by any subclass.
# Interface: An interface is a contract that defines a set of methods that a class must implement, without providing any implementation details.    
# In Python, interfaces can be represented using abstract base classes (ABCs) from the abc module.
# An interface is similar to an abstract class that contains only abstract methods (methods without implementation).
from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass    
# Interface with only abstract methods  
class MyConcreteClass(MyInterface):
    def my_method(self):
        return "Implemented my_method"
obj = MyConcreteClass()
print(obj.my_method())  # Output: Implemented my_method 
# Concrete class implementing the interface
# If we comment the my_method in MyConcreteClass then it will give error as we cannot create object of abstract class
# TypeError: Can't instantiate abstract class MyConcreteClass with abstract method my_method
# Abstract class with abstract method
class MyAbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
# Abstract class cannot be instantiated
# obj2 = MyAbstractClass()  # This will raise an error because we cannot instantiate an abstract class
# Concrete class extending abstract class and implementing abstract method
class MyConcreteClass2(MyAbstractClass):
    def abstract_method(self):
        return "Implemented abstract_method"        
obj2 = MyConcreteClass2()
print(obj2.abstract_method())  # Output: Implemented abstract_method    
# If we comment the abstract_method in MyConcreteClass2 then it will give error as we cannot create object of abstract class
# TypeError: Can't instantiate abstract class MyConcreteClass2 with abstract method abstract_method 
# Summary:
# Concrete Class: Can be instantiated, contains implementations for all methods.
# Abstract Class: Cannot be instantiated, may contain abstract methods that must be implemented by subclasses.
# Interface: Defines a contract with no implementation, classes must implement all interface methods.   
# In Python, interfaces are typically represented using abstract base classes (ABCs) with only abstract methods.
# Abstract classes can have both abstract and concrete methods, while interfaces usually contain only abstract methods. 
# A concrete class can implement multiple interfaces (abstract base classes) in Python.
# Example of multiple inheritance with interfaces
class InterfaceA(ABC):
    @abstractmethod
    def method_a(self):
        pass
class InterfaceB(ABC):
    @abstractmethod
    def method_b(self):
        pass
class ConcreteClass(InterfaceA, InterfaceB):
    def method_a(self):
        return "Implemented method_a"
    def method_b(self):
        return "Implemented method_b"
obj3 = ConcreteClass()
print(obj3.method_a())  # Output: Implemented method_a
print(obj3.method_b())  # Output: Implemented method_b
# If we comment either method_a or method_b in ConcreteClass then it will give error as we cannot create object of abstract class
# TypeError: Can't instantiate abstract class ConcreteClass with abstract method method_a/method_b  
# This demonstrates that a concrete class can implement multiple interfaces (abstract base classes) in Python.
# Note: Python does not have a built-in interface keyword like some other languages (e.g., Java, C#).
# Instead, interfaces are typically represented using abstract base classes (ABCs) with only abstract methods.
# Abstract classes can have both abstract and concrete methods, while interfaces usually contain only abstract methods.