# IS-A vs HAS-A Relationship
# IS-A: Inheritance
class Animal: pass
class Dog(Animal): pass

# HAS-A: Composition
class Engine: pass
class Car:
    def __init__(self):
        self.engine = Engine()
