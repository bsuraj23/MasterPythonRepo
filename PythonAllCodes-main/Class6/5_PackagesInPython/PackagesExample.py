#code to demo packages in python
# Creating a package named 'mypackage' with the following structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py        
# __init__.py can be empty or can contain initialization code for the package
# module1.py
def func1():
    return "Function 1 from module 1"
# module2.py
def func2():
    return "Function 2 from module 2"
# Using the package and its modules
# Importing the entire package
import mypackage.module1 as m1
import mypackage.module2 as m2
print(m1.func1())  # Output: Function 1 from module 1
print(m2.func2())  # Output: Function 2 from module 2
# Importing specific functions from the modules
from mypackage.module1 import func1
from mypackage.module2 import func2
print(func1())  # Output: Function 1 from module 1
print(func2())  # Output: Function 2 from module 2
# You can also use from...import * to import all functions from a module
from mypackage.module1 import *
from mypackage.module2 import *
print(func1())  # Output: Function 1 from module 1
print(func2())  # Output: Function 2 from module 2
# End of the package demonstration code
# You can run this file directly to test the functions from the package
# or you can import this package in another Python script to use the functions  
# Example of using the package in another script
import mypackage.module1 as m1
import mypackage.module2 as m2
print(m1.func1())  # Output: Function 1 from module 1
print(m2.func2())  # Output: Function 2 from module 2
