# Decorator Chaining
def decorator_one(func):
    def wrapper():
        print("Decorator One: Before the function call.")
        func()
        print("Decorator One: After the function call.")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two: Before the function call.")
        func()
        print("Decorator Two: After the function call.")
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()
# Output:
# Decorator One: Before the function call.
# Decorator Two: Before the function call.
# Hello!
# Decorator Two: After the function call.
# Decorator One: After the function call. 

# Chaining more decorators
def decorator_three(func):
    def wrapper():
        print("Decorator Three: Before the function call.")
        func()
        print("Decorator Three: After the function call.")
    return wrapper
@decorator_one
@decorator_two
@decorator_three
def greet():
    print("Hello!")

greet()         

# Output:
# Decorator One: Before the function call.
# Decorator Two: Before the function call.
# Decorator Three: Before the function call.
# Hello!
# Decorator Three: After the function call.
# Decorator Two: After the function call.
# Decorator One: After the function call.
# Note: The order of execution is from the innermost decorator to the outermost.
# This means decorator_three is applied first, then decorator_two, and finally decorator_one.
# This is because the decorators are applied from the bottom up.
# You can chain as many decorators as you want in this manner.
# You can also use decorators with arguments
def decorator_with_args(arg1, arg2):
    def decorator(func):
        def wrapper():
            print(f"Decorator with args: {arg1}, {arg2} - Before the function call.")
            func()
            print(f"Decorator with args: {arg1}, {arg2} - After the function call.")
        return wrapper
    return decorator

@decorator_with_args("Hello", "World")
def greet():
    print("Greetings!")

greet()     
# Output:
# Decorator with args: Hello, World - Before the function call.
# Greetings!
# Decorator with args: Hello, World - After the function call.      
# You can combine decorators with and without arguments
@decorator_one
@decorator_with_args("Python", "Rocks")
def greet():
    print("Greetings!")

greet()
# Output:
# Decorator One: Before the function call.
# Decorator with args: Python, Rocks - Before the function call.
# Greetings!
# Decorator with args: Python, Rocks - After the function call.
# Decorator One: After the function call.   
# This shows the flexibility and power of decorators in Python.
# You can also use functools.wraps to preserve the original function's metadata
import functools    
def decorator_with_wraps(func):
    @functools.wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper
@decorator_with_wraps
def greet():
    """This is the greet function."""
    print("Hello!") 
greet()
print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: This is the greet function.
# Without functools.wraps, the name and docstring would be of the wrapper function
# This is important for debugging and introspection 
# You can also create class-based decorators
class DecoratorClass:   
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print("Before the function call.")
        self.func()
        print("After the function call.")   
@DecoratorClass
def greet():
    print("Hello from class-based decorator!")  
greet()
# Output:
# Before the function call.
# Hello from class-based decorator!
# After the function call.  
# Class-based decorators can also take arguments