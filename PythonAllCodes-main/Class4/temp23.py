import os

folder = "Class4/Function2"
os.makedirs(folder, exist_ok=True)

files_content = {
    "functions.py": '''# FUNCTIONS
def greet():
    print("Hello from a function!")
greet()
''',

    "built_in_functions.py": '''# Built in Functions
numbers = [1, 2, 3, 4]
print(sum(numbers))
print(len(numbers))
''',

    "user_defined_functions.py": '''# User Defined Functions
def add(a, b):
    return a + b
print(add(2, 3))
''',

    "parameters.py": '''# Parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
''',

    "return_statement.py": '''# Return Statement
def square(x):
    return x * x
print(square(5))
''',

    "returning_multiple_values.py": '''# Returning Multiple Values from a Function
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
print(stats([1, 2, 3]))
''',

    "types_of_arguments.py": '''# Types of Arguments
def func(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
func(1, 2, 3, 4, x=5)
''',

    "case_study.py": '''# Case Study
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print(factorial(5))
''',

    "types_of_variables.py": '''# Types of Variables
x = 10  # global variable
def show():
    y = 5  # local variable
    print(x, y)
show()
''',

    "global_keyword.py": '''# global Keyword
x = 5
def change():
    global x
    x = 10
change()
print(x)
''',

    "recursive_functions.py": '''# Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))
''',

    "anonymous_functions.py": '''# Anonymous Functions
add = lambda a, b: a + b
print(add(2, 3))
''',

    "normal_function.py": '''# Normal Function
def square(x):
    return x * x
print(square(4))
''',

    "lambda_function.py": '''# Lambda Function
square = lambda x: x * x
print(square(4))
''',

    "filter_function.py": '''# filter() Function
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)
''',

    "map_function.py": '''# map() Function
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))
print(squares)
''',

    "reduce_function.py": '''# reduce() Function
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)
''',

    "everything_is_object.py": '''# Everything is an Object
print(type(10))
print(type("hello"))
print(type(lambda x: x))
''',

    "function_aliasing.py": '''# Function Aliasing
def greet():
    print("Hello!")
hello = greet
hello()
''',

    "nested_functions.py": '''# Nested Functions
def outer():
    def inner():
        print("Inside inner function")
    inner()
outer()
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)