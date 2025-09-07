# Example 1: Method Overriding
class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirping")

# Example 2: Function with different objects
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
    animal.speak()

# Example 3: Operator Overloading
class Demo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

# Example 4: Polymorphism via Duck Typing
class File:
    def execute(self):
        print("Executing file")

class Program:
    def execute(self):
        print("Running program")

def run_code(entity):
    entity.execute()

# Example 5: Built-in polymorphism
print(len("Python"))
print(len([10, 20, 30]))
