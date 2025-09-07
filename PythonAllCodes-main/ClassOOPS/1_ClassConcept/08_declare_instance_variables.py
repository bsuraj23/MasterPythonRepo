# Where we can declare Instance Variables
class Student:
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age

obj = Student("John")
obj.set_age(20)

print(obj.name)  # Output: John
print(obj.age)   # Output: 20   


obj2 = Student("Ajay")
obj2.set_age(24)

print(obj2.name)  # Output: John
print(obj2.age)   # Output: 24  


obj3 = Student("Sashi")
obj3.set_age(20)

print(obj3.name)  # Output: John
print(obj3.age)   # Output: 20