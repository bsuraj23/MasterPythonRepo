# Position Argument
def greet(name):
    print("Hello,", name)

greet("Alice")
greet("Bob")
greet("Charlie")
# Default Arguments
def greet(name="Guest"):
    print("Hello,", name)
greet()
greet("Alice")
# Keyword Arguments
def greet(name, message="Welcome"):
    print(f"{message}, {name}!")
greet(name="Alice", message="Hi")
greet(message="Greetings", name="Bob")  
greet("Charlie")  # Uses default message
# Variable-length Arguments
def greet(*names):
    for name in names:
        print("Hello,", name)
greet("Alice", "Bob", "Charlie")
# Example with both *args and **kwargs
def greet(*names, **messages):
    for name in names:
        message = messages.get(name, "Hello")
        print(f"{message}, {name}!")
greet("Alice", "Bob", Alice="Hi", Bob="Welcome")
# More examples of functions with different types of arguments
def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even_odd(10)
check_even_odd(15)




def check_even_odd(number=4):
   
    a=90
    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even_odd()







