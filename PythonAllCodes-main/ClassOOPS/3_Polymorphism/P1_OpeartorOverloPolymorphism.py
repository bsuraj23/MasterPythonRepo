#operator overloading code simple without class for polymorphism concept

def add(x, y):
    return x + y

def add_floats(x, y):
    return x + y

def add_strings(x, y):
    return x + y    
# same function name but different data types
print(add(5, 10))            # integer addition 
print(add_floats(5.5, 10.2)) # float addition
print(add_strings("Hello, ", "World!")) # string concatenation  
#code for polymorphism using class

class Adder:
    def add(self, a, b):
        return a + b

adder = Adder()
print(adder.add(5, 10))            # integer addition
print(adder.add(5.5, 10.2))        # float addition
print(adder.add("Hello, ", "World!")) # string concatenation













class Dog:
    def speak(self):
        print("Dog says: Woof!")

class Cat:
    def speak(self):
        print("Cat says: Meow!")

# Polymorphism in action
def animal_sound(animal):
    animal.speak()  # same method name, different behavior

d = Dog()
c = Cat()

animal_sound(d)  # Dog says: Woof!
animal_sound(c)  # Cat says: Meow!
