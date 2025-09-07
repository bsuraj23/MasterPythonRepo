#code to demo random(),randint(),randrange(),uniform(),choice(),shuffle()
import random   
print(random.random())  #gives random float number between 0 and 1
print(random.randint(1,10))  #gives random integer between 1 and
print(random.randrange(1,10,2))  #gives random odd integer between 1 and 10
print(random.uniform(1,10))  #gives random float number between 1 and 10
print(random.choice(['apple','banana','cherry']))  #gives random element from the list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  #shuffles the list randomly
print(my_list)
# End of random module demonstration code
# Class6/4_Modules/4_Module.py  
# Demonstrating various aspects of modules in Python
# Importing built-in modules
import math
import os
import sys
import datetime
import random
# Using functions from the imported modules
print("Square root of 16 is: ", math.sqrt(16))  # Output: 4.0
print("Current working directory is: ", os.getcwd())  # Output: Path to current directory
print("Python version is: ", sys.version)  # Output: Python version
print("Current date and time is: ", datetime.datetime.now())  # Output: Current date and time
# End of built-in module demonstration code
# You can explore more functions from these modules as needed
# For example, using math module to calculate factorial
print("Factorial of 5 is: ", math.factorial(5))  # Output: 120
# Using os module to list files in the current directory
print("Files in current directory: ", os.listdir('.'))  # Output: List of files
# Using datetime module to format date
now = datetime.datetime.now()
print("Formatted date: ", now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: Formatted current date and time