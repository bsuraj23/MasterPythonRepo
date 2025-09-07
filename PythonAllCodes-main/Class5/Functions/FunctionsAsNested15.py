# Nested Functions - 6 Examples

# Example 1
def outer():
    def inner():
        print("Inner function called")
    inner()

outer()

# Example 2
def main_function():
    def sub_function():
        return "Nested function working"
    print(sub_function())

main_function()

# Example 3
def calculator(a, b):
    def add():
        return a + b
    return add()

print(calculator(5, 10))

# Example 4
def greet_outer():
    message = "Hello"
    def greet_inner():
        print(message)
    greet_inner()

greet_outer()

# Example 5
def math_operations(x):
    def square():
        return x * x
    return square()

print(math_operations(7))

# Example 6
def wrapper():
    def wrapped():
        print("I am wrapped inside a function.")
    wrapped()

wrapper()
