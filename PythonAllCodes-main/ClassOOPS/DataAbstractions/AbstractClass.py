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





