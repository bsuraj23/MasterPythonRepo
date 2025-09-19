# What is Reference Variable?
class Student:
    name = "name"
    age = 14  




ajay = Student()
aman= ajay  # s2 is a reference variable pointing to the same object as s1


ajay.age

#shallow copy and deep copy
import copy 
ajay = Student()
vijay= copy.copy(ajay)  # shallow copy
ajay.age
vijay.age
vijay.age=34
print(ajay.age)
print((vijay.age)


