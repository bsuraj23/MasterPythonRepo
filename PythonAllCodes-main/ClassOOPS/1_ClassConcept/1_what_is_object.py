# What is Object?
# An object is an instance of a class.

class Person:
    pass

obj = Person()

class Student:

    pass
Aditya = Student()

class Automobile:
    tires="tires"   #//2 bytes
    def add(a,b):   #// 7 Bytes
        return a+b
        

BMW = Automobile()  # 10 bytes
print(BMW.tires)
print(BMW.add(3,4))
Thar = Automobile()  #bytes
Hummer = Automobile()
Audi = Automobile()
