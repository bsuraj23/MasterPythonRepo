# Constructor Concept
class Student:
    a=90
    def __init__(self, name):
        self.name = name
        print("i am getting executed")
        b=78
    def add():
        pass



print(Student.a)
Student.a=67
Alice = Student("Alice")
print(Alice.a)
Alice.b=34
print(Alice.b)
print(Alice.add())

Ajayobj = Student("Ajay")


print(Ajayobj.a)
print(Ajay.add())



class Person:
    name = "name"
    age = 14
    def sleep():
        print("sleeping executed ")

personObj1 = Person()
personObj1.name ="ajay"
personObj1.age = 24
print(personObj1.age)
# print(personObj1.sleep())

personObj2 = Person()
personObj2.name = "vijay"
personObj2.age = 34
print(personObj2.age)
# print(personObj2.sleep())

# print(personObj2.age)
# print(personObj2.sleep())


