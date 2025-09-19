#Instance Methods vs Class Methods vs Static Methods in Python

#In class method we have to pass class variable as a parameter to the class method.
#In static method we don't have to pass any parameter to the static method.



class MyClass:
    # Instance Method
    def instance_method(self):
        return f"Instance method called on {self}"
   
    # Class Method
    @classmethod
    def class_method(cls):
        return f"Class method called on {cls}"

    # Static Method
    @staticmethod
    def static_method():
        return "Static method called"   
# Create an instance of MyClass
obj = MyClass() 
print(obj.instance_method())  # Calls instance method
print(MyClass.class_method())  # Calls class method
print(MyClass.static_method())  # Calls static method   


#Instance methods can access and modify object state,
#  class methods can access and modify class state, 
# and static methods are utility functions that do not access instance or class state.


#we have to pass instance variable as a parameter to the instance method.
#example: self  is the instance variable.   
class Car:
    def __init__(self, color):
        self.color = color  # This car’s color

    #this is instance method because it is using instance variable self.color
    def describe(self):
        return f"This car is {self.color}"
    #getter 
    def get_color(self):
        return self.color   
    #setter 
    def set_color(self, new_color):
        self.color = new_color
        return f"Car color changed to {self.color}"
car = Car("red")
print(car.describe())  # Only car is red!
car.set_color("blue")  # Change color to blue
print(car.describe())  # Now car is blue!
print(car.get_color())  # Get the current color using the getter
car.set_color("green")  # Change color to green
print(car.describe())  # Now car is green!

my_car = Car("red")
print(my_car.describe())  # Only my_car is red!

#more Examples
class Circle:
    pi = 3.14159  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable

    # Instance method
    def area(self):
        return Circle.pi * (self.radius ** 2)
    #getter
    def get_radius(self):
        return self.radius
    #setter
    def set_radius(self, new_radius):
        self.radius = new_radius
        Circle.pi = new_radius  # Just for demonstration, not typical usage
circle = Circle(5)
print(circle.area())  # Area of the circle with radius 5
print(circle.get_radius())  # Get the radius using the getter
circle.set_radius(10)  # Set a new radius using the setter
print(circle.area())  # Area of the circle with radius 10

#more Examples
class Rectangle:

    def __init__(self, width, height):
        self.width = width  # Instance variable
        self.height = height  # Instance variable

    # Instance method
    def area(self):
        return self.width * self.height

   
