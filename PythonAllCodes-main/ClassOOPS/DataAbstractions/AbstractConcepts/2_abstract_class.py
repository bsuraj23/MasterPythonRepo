# Abstract class
# An abstract class is a class that cannot be instantiated on its own and is meant to be subclassed.
# It can contain abstract methods (methods without implementation) that must be implemented by any subclass.    
#same as Java abstract class
# In Python, abstract classes are defined using the abc module, which stands for Abstract Base Classes


#can create abstract class without abstract method
#observe no decorator 
from abc import ABC
class Vehicle(ABC):
    pass




from abc import ABC, abstractmethod
class Vehicle2(ABC):    
    @abstractmethod
    def start_engine(self):
        pass

# obj2 = Vehicle2()  # This will raise an error because we cannot instantiate an abstract class with abstract methods
#as extended to ABC class
#Java we can create abstract class without abstract method
#but in python if we have abstract method in class then we must declare class as abstract class


#if class has one abstract method and extending ABC class then it is abstract class
#thus cannot create object of that class
#thus must implement abstract method in subclass
class Car(Vehicle2):
    pass

class ThirdCar(Vehicle2):
    def start_engine(self):
        return "ThirdCar engine started"
  
car = Car()
print(car.start_engine())  # Output: Car engine started
# If we comment the start_engine method in Car class then it will give error as we cannot create object of abstract class
# TypeError: Can't instantiate abstract class Car with abstract method start_engine