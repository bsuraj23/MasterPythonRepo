# Overview of Function - 6 Examples

#function which return two vars 
def add(a,b):
    sum = a+b
    minus = a-b
    return sum,minus
x,y=add(1,2)
print(x,y)










# Example 2
def double(num):
    return num * 2

print(double(5))

# Example 3
def greet_user(name):
    print("Welcome", name)

greet_user("Alice")

# Example 4
def subtract(x, y):
    return x - y

print(subtract(9, 4))

# Example 5
def cube(num):
    return num ** 3

print(cube(3))

# Example 6
def multiply_numbers(a, b, c):
    return a * b * c

print(multiply_numbers(2, 3, 4))
