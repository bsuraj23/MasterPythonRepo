class Animal:
    def add(self,a):
        print("add with no paarmeter Constructor")
    def add(self,a,b):
        print("add with two para",a)
class Dog(Animal):
    pass  # No own constructor

# d = Dog()

ani = Animal()
ani.add(23)
