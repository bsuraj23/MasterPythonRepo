# Where we can declare Instance Variables
#inside constructor
#inside instance method 
#outside the class using object reference variable

class Student:
    def __init__(self, name):
        self.name = name
    #getter method
    def get_name(self):
        return self.name
    # instance method example of declaring instance variable
    def set_age(self, age):
        self.age = age

obj = Student("John")
print(obj.get_name())  # Output: John
obj.set_age(20)

Obj2 = Student("mohan")
print(Obj2.get_name())  # Output: mohan
Obj2.set_age(30)



#declaring instance variable outside the class using object reference variable
obj.age=20  
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


print(obj.__dict__)  # Output: {'name': 'John'}
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}

del obj.age  # Deleting instance variable age from obj
del obj2.age  # Deleting instance variable age from obj2
del obj3.age  # Deleting instance variable age from obj3

print(obj.__dict__)  # Output: {'name': 'John'}
print(obj2.__dict__)  # Output: {'name': 'Ajay', 'age': 30}
print(obj3.__dict__)  # Output: {'name': 'Sashi', 'age': 40}