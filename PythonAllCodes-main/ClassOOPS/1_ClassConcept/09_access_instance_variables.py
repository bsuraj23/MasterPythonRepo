# How to Access Instance Variables
class Student:
    a=78
    def __init__(self, name):
        self.name = name
s = Student("Bob")
print(s.name)
