class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person: {self.name}")
    def add(self,a=0,b):
        result=a+b
        print("value of a is",a)
        print("value of b is ",b)
        print(result)

# class Student(Person):
#     def __init__(self, name=suraj, course,address):
#         super().__init__(name)      # calling parent constructor
#         self.course = course
#         print(f"Student enrolled in {self.course}")

# sobj = Student("Amit", "Python Bootcamp")
# mobj = Student("sunil", "Python Bootcamp")
# otherobj = Student("","CSE")

# print(sobj.name)

Pobj =Person("anil")
Pobj.add(12)
