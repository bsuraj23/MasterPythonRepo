#code for method overriding polymorphism concept
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")

child = Child()
child.show()  # Calls the overridden method in Child class  
# Output: Child class method
# Here, the show method is overridden in the Child class, demonstrating method overriding polymorphism.
# In this case, the method that gets called is determined at runtime based on the object type (Child), not the reference type (Parent).
# This is a runtime polymorphism example.
#more examples for method Overriding and edge cases
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")  
class Cat(Animal):
    def speak(self):
        print("Cat meows")

obj_animal = Animal()
obj_dog = Dog() 
obj_cat = Cat()

obj_animal.speak() #Animal speaks
obj_dog.speak()    #Dog barks
obj_cat.speak()    #Cat meows


