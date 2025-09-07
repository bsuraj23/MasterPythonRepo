import os

folder = "AbstractConcepts"
os.makedirs(folder, exist_ok=True)

files_content = {
    "abstract_method.py": '''# Abstract Method
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
''',

    "abstract_class.py": '''# Abstract class
from abc import ABC
class Vehicle(ABC):
    pass
''',

    "interface.py": '''# Interface
from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print_data(self):
        pass
''',

    "concrete_vs_abstract_vs_interface.py": '''# Concreate Class vs Abstract Class vs Interface
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
''',

    "access_modifiers.py": '''# Public, Private and Protected Members
class Demo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
    def show(self):
        print(self.public, self._protected, self.__private)
d = Demo()
d.show()
print(d.public)
print(d._protected)
# print(d.__private) # Error
print(d._Demo__private) # Access private
''',

    "str_method.py": '''# __str__() Method
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"
p = Person("Alice")
print(p)
''',

    "str_vs_repr.py": '''# Difference between str() and repr() Functions
class Demo:
    def __str__(self):
        return "str called"
    def __repr__(self):
        return "repr called"
d = Demo()
print(str(d))
print(repr(d))
''',

    "banking_app.py": '''# Small Banking Application
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
    def __str__(self):
        return f"Account({self.owner}, Balance: {self.balance})"

acc = Account("Suraj", 1000)
acc.deposit(500)
print(acc)
acc.withdraw(300)
print(acc)
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)