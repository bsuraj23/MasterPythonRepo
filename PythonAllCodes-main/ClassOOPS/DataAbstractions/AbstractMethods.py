from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def add(self, other):
       pass

#ADD more example code below
