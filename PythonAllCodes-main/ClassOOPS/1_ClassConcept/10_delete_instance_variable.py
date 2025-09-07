# How to delete Instance Variable from the Object
class Student:
    def __init__(self):
        self.name = "Tom"
s = Student("suraj")
del s.name
2 = Student("aman")