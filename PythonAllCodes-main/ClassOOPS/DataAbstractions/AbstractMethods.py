from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def add(self, other):
       pass

#ADD more example code below
#explain 
# In this code, we define an abstract base class `Shape` using the `ABC` module from the Python standard library. The `Shape` class has two abstract methods: `perimeter` and `add`.
# Any subclass of `Shape` must implement these methods. This ensures a consistent interface for all shapes, allowing polymorphic behavior.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def add(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        raise ValueError("Can only add another Circle")