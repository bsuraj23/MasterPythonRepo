#code for constructor over riding  polymorphism concept

#not possible as python does not support constructor overloading last defined constructor will be considered
#thus we can not achieve constructor overloading in python like other languages  Java or C++


class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor one para called")  
     
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Animal constructor two para  called")  

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        print("Animal constructor 3 para called")  

# obj1 = Animal("Buddy")         # This will raise an error
obj2 = Animal("Buddy", 3)            # This will raise an error
obj3 = Animal("Buddy", 3, "Dog")     # This will work
print(f"Name: {obj3.name}, Age: {obj3.age}, Species: {obj3.species}")
