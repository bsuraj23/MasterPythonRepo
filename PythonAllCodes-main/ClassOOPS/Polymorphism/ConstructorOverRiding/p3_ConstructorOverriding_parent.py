class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        super().__init__()   # calls parent constructor
        print("Dog Constructor")

d = Dog()
