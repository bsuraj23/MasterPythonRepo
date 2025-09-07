#TODO: Decorators
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