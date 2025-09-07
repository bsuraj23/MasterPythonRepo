# Abstract Method
# An abstract method is a method that is declared, but contains no implementation.
# Abstract methods are meant to be overridden in derived classes.   
#same as Java abstract method
# In Python, abstract methods are defined using the abc module, which stands for Abstract Base Classes
#@abstractmethod is mandatory to declare a method as abstract method
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
