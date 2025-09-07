
#Important -- python function can return two vars than any language

# Working with Functions - 6 Examples

# Example 1: Function to print a message
def greet():
    print("Hello from function!")



# greet()

# # Example 2: Function to add two numbers
def add(a, b):
    c= a + b

print(add(5, 3))

# # Example 3: Function to multiply numbers
# def multiply(a, b):
#     return a * b

# print(multiply(2,4))

# # Example 4: Function to check even number and return example 
# def  is_even(num):
#     return num % 2 == 0

# print(is_even(11))

# # Example 5: Function to print a message passed
#demo for dynamic nature and how code inside can make sure datatype constrains 
# def print_message(msg):
#     print(msg)

# print_message(78)

#how code inside can make sure datatype constrains 
import math
# # Example 6: Function to find square
def square(num):
    temp = int(num)
    result = math.sqrt(temp)
    return result 

print(square("we"))
