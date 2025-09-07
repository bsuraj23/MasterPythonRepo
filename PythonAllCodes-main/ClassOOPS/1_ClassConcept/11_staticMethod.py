#static Methods in classes in Python
#A static method is a method that does not receive an implicit first argument (neither self nor cls).
# It behaves like a regular function but belongs to the class's namespace.

class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b    
# Call static methods using the class name
print(MathOperations.add(5, 3))       # Output: 8   
print(MathOperations.multiply(5, 3))  # Output: 15
# Static methods can be called on the class itself without creating an instance.
# They are often used for utility functions that don't need access to instance or class data.
# Static methods do not modify class or instance state.
# They are just grouped within the class for organizational purposes.
#Example of static method in Car class
class Car:  
    def __init__(self, color):
        self.color = color  # This car’s color

    # Static method to describe the car
    @staticmethod
    def describe():
        return "This is a car."
my_car = Car("red")
print(my_car.color)  # Only my_car is red!  
print(Car.describe())  # Call static method using class name
print(my_car.describe())  # Call static method using instance (not common but possible)
#Both ways of calling static method are valid, but using the class name is more common.

#rarely used methods in real world scenarios. 