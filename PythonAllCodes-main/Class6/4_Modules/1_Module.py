#generate code to demo modules in python
# Custom Module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b
# You can add more functions as needed
# Save this file as my_math_module.py
# This module can be imported and used in other Python scripts


# Example usage:  Next file will demonstrate usage as below 
import my_math_module as mm
print(mm.add(5, 3))  # Output: 8
print(mm.subtract(5, 3))  # Output: 2
print(mm.multiply(5, 3))  # Output: 15
print(mm.divide(5, 0))  # Output: Division by zero is not allowed
print(mm.power(2, 3))  # Output: 8
print(mm.modulus(5, 3))  # Output: 2


# You can also use from...import statement
from my_math_module import add, subtract
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
#   Using import...as statement
import my_math_module as mm
print(mm.multiply(5, 3))  # Output: 15
print(mm.divide(5, 0))  # Output: Division by zero is not allowed


# Using dir() function to list all functions in the module
# import my_math_module as mm
# print(dir(mm))
# Output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'divide', 'modulus', 'multiply', 'power', 'subtract']
# Using __name__ variable to check if the module is being run directly 
# or imported
if __name__ == "__main__":
    print("This module is being run directly")
    # You can add code here to test the functions in the module
    print("Testing add function: ", add(5, 3))  # Output: 8
    print("Testing subtract function: ", subtract(5, 3))  # Output: 2
    print("Testing multiply function: ", multiply(5, 3))  # Output: 15
    print("Testing divide function: ", divide(5, 0))  # Output: Division by zero is not allowed
    print("Testing power function: ", power(2, 3))  # Output: 8
    print("Testing modulus function: ", modulus(5, 3))  # Output: 2
else:
    print("This module is being imported")


# You can also take input from user to test the functions
if __name__ == "__main__":
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    print("Addition: ", add(n, m))
    print("Subtraction: ", subtract(n, m))
    print("Multiplication: ", multiply(n, m))
    print("Division: ", divide(n, m))
    print("Power: ", power(n, m))
    print("Modulus: ", modulus(n, m))
# Save this file as my_math_module.py
# You can run this file directly to test the functions
#generate code to demo dir() function in python
#generate code to demo __name__ variable in python
#generate code to demo __main__ in python
#generate code to demo creating and using a custom module in python
#generate code to demo creating and using a custom module in python with if __name__ == "__main__"
#generate code to demo creating and using a custom module in python with if __name__ == "__main__" and taking input from user
#generate code to demo creating and using a custom module in python with if __name__ == "__main__" and taking input from user and using functions from the module
# Class6/4_Modules/1_Module.py
# Custom Module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"    
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b
# You can add more functions as needed
# Save this file as my_math_module.py   
# This module can be imported and used in other Python scripts
# Example usage:
import my_math_module as mm
print(mm.add(5, 3))  # Output: 8
print(mm.subtract(5, 3))  # Output: 2
print(mm.multiply(5, 3))  # Output: 15
print(mm.divide(5, 0))  # Output: Division by zero is not allowed
print(mm.power(2, 3))  # Output: 8
print(mm.modulus(5, 3))  # Output: 2
# You can also use from...import statement
# from my_math_module import add, subtract
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2


