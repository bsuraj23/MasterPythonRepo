from abc import ABC, abstractmethod

class Shape(ABC):
    
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height 
rect = Rectangle(5, 10)
print(rect.area())  # Output: 50        
# If we comment the area method in Rectangle class then it will give error as we cannot create object of abstract class
# TypeError: Can't instantiate abstract class Rectangle with abstract method area





#from abc import ABC   why this 
# The `ABC` module stands for "Abstract Base Classes". It provides a way to define abstract classes in Python. An abstract class is a class that cannot be instantiated and is meant to be subclassed. By inheriting from `ABC`, we can create an abstract class that can contain abstract methods, which are methods that must be implemented by any subclass. This allows us to enforce a certain interface or contract for the subclasses, ensuring that they implement specific functionality.