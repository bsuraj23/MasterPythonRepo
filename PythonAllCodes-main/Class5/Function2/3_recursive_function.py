# recursive  Function
def square(x):
    if x == 1:
        return 1
    else:
        return x * square(x-1)
print(square(4))

# Function inside function
def outer_function():   
    print("I am outer function")
    def inner_function():
        print("I am inner function")
    inner_function()        
outer_function()    
# inner_function()  #error


#more examples of recursion
#factorial ,fibonacci,tail recursion etc
#more complex example of function inside function
#accessing variable of outer function inside inner function
def outer_function(x):
    def inner_function(y):
        return y + 1
    return inner_function(x)
result = outer_function(5)
print(result)  # Output: 6  
#accessing variable of outer function inside inner function
def outer_function(x):
    def inner_function(y):
        return y + 1
    return inner_function(x)
result = outer_function(5)
print(result)  # Output: 6
#more complex example of recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))  # Output: 8 (0, 1, 1, 2, 3, 5, 8)
#tail recursion example
def tail_recursive_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_recursive_factorial(n-1, n * accumulator)
print(tail_recursive_factorial(5))  # Output: 120
# Function with default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")
greet()
greet()  # Uses default argument
greet("Bob")
greet()  # Uses default argument
# Function with variable-length arguments
def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3)
print_numbers(4, 5, 6, 7, 8)
print_numbers()  # No arguments
print_numbers(10, 20)
print_numbers(100, 200, 300, 400)
# Function with keyword arguments
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info("Alice", 30)
print_info("Bob", 25)
print_info(name="Charlie", age=35)
print_info(age=28, name="Diana")
print_info("Eve", age=22)
print_info(name="Frank", age=40)
print_info("Grace", 29)
print_info(age=33, name="Hank") 
print_info("Ivy", age=27)
# Function with both variable-length and keyword arguments
def print_details(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details("Alice", "Bob", age=30, location="New York")  
print_details("Charlie", age=25)
print_details()  # No arguments
print_details("Diana", "Eve", "Frank", age=28, location="Los Angeles", profession="Engineer")
print_details("Grace", age=33)