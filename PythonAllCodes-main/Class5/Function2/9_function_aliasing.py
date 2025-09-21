# Function Aliasing
def greet():
    print("Hello!")
hello = greet
hello()


#more examples of function aliasing like
#using alias to pass function as argument
def call_function(func):
    func()
call_function(hello)
#using alias to store function in data structures
func_list = [greet, hello]
for f in func_list:
    f() 
#using alias to return function from another function
def get_greet_function():
    return greet    
g = get_greet_function()
g()
greet_alias = g
greet_alias()()

#decorators using function aliasing
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