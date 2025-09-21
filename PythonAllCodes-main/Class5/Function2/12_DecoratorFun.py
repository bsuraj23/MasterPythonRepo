# Decorators
def decorator_function(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator_function
def greet():
    print("Hello!")

greet()

# Using the decorator without the @ syntax
def another_greet():
    print("Hi there!")

another_greet = decorator_function(another_greet)
another_greet()

# More examples of decorators
def uppercase_decorator(func):  
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase_decorator
def greet():
    return "Hello!"
print(greet())  # Output: "HELLO!"    

#ADD more examples of decorator
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    return "Finished"
print(slow_function())  # Output: "Finished" and time taken
# Decorator with arguments
def repeat_decorator(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat_decorator(3)
def say_hello():
    print("Hello!")
say_hello()  # Output: "Hello!" printed 3 times
# Decorator for logging
def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper