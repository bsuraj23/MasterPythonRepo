import os

folder = "Polymorphism"
os.makedirs(folder, exist_ok=True)

files_content = {
    "polymorphism.py": '''# Polymorphism
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
a = Animal()
d = Dog()
a.speak()
d.speak()
''',

    "duck_typing.py": '''# Duck Typing Philosophy of Python
class Bird:
    def fly(self):
        print("Bird can fly")
class Airplane:
    def fly(self):
        print("Airplane can fly")
def lets_fly(obj):
    obj.fly()
b = Bird()
a = Airplane()
lets_fly(b)
lets_fly(a)
''',

    "overloading.py": '''# Overloading
# Python does not support method overloading directly
class Demo:
    def show(self, a=None, b=None):
        print(a, b)
d = Demo()
d.show()
d.show(1)
d.show(1, 2)
''',

    "overriding.py": '''# Overriding
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        print("Hello from Child")
c = Child()
c.greet()
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)