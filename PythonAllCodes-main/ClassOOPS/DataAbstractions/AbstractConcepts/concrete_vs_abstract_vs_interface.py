# Concreate Class vs Abstract Class vs Interface
from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def show(self): pass

class ConcreteClass(AbstractClass):
    def show(self):
        print("Concrete implementation")

class Interface(ABC):
    @abstractmethod
    def method(self): pass
