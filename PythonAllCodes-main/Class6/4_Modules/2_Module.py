# Class6/4_Modules/2_Module.py
# Demonstrating import statements in Python 
# Importing the custom module created in 1_Module.py
import my_math_module as mm
# Using functions from the imported module
print("Addition: ", mm.add(10, 5))          # Output: 15
print("Subtraction: ", mm.subtract(10, 5))  # Output: 5
print("Multiplication: ", mm.multiply(10, 5))  # Output: 50
print("Division: ", mm.divide(10, 0))       # Output    : Division by zero is not allowed
print("Power: ", mm.power(2, 3))            # Output: 8
print("Modulus: ", mm.modulus(10, 3))       # Output: 1
# You can also use from...import statement to import specific functions
from my_math_module import add, subtract
print("Addition using from...import: ", add(20, 10))          # Output: 30
print("Subtraction using from...import: ", subtract(20, 10))  # Output: 10
# Using dir() function to list all functions in the module
print("Functions in my_math_module: ", dir(mm))
# Output: ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'divide', 'modulus', 'multiply', 'power', 'subtract']  
# Demonstrating __name__ variable
print("Module name: ", mm.__name__)  # Output: my_math_module
# If you run this script directly, it will show the following message from the module
# "This module is being imported"
# You can also take input from user to test the functions
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
print("Addition: ", mm.add(n, m))
print("Subtraction: ", mm.subtract(n, m))
print("Multiplication: ", mm.multiply(n, m))
print("Division: ", mm.divide(n, m))
print("Power: ", mm.power(n, m))
print("Modulus: ", mm.modulus(n, m))
# Save this file as test_my_math_module.py      
# You can run this file directly to test the functions from the module
# or you can import this module in another Python script to use the functions


# Example of importing and using the module in another script
import my_math_module as mm
print(mm.add(10, 5))  # Output: 15
print(mm.subtract(10, 5))  # Output: 5
print(mm.multiply(10, 5))  # Output: 50
print(mm.divide(10, 0))  # Output: Division by zero is not    allowed
print(mm.power(2, 4))  # Output: 16
print(mm.modulus(10, 3))  # Output: 1     
# You can also create your own modules and import them in your scripts
# This is a simple demonstration of how to create and use modules in Python
# Modules help in organizing code and reusing it across different programs
# Always remember to keep your module files in the same directory as your script or in the Python path
# This makes it easier to import and use them without any issues
# Happy Python coding !
# End of the module demonstration code