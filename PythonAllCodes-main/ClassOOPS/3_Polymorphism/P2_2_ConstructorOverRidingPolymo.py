#code for constructor over riding  polymorphism concept

#not possible as python does not support constructor overloading last defined constructor will be considered
#thus we can not achieve constructor overloading in python like other languages  Java or C++


class Animal:
    def __init__(self, name):
        self.name = name
         print("Animal constructor called")  
    def __init__(self, name):
        self.name = name
         print("Animal constructor called")  
    def __init__(self, name, age):
        self.name = name
         print("Animal constructor called")  
    def __init__(self, name, age, species):
        self.name = name
         print("Animal constructor called")  
   