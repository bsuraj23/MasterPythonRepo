# Lambda Function
xyz = lambda x: x * x
print(xyz(4))

# Lambda function with multiple arguments
add = lambda a, b: a + b
print(add(5, 10))

# Lambda function with no arguments
greet = lambda: "Hello, World!"
print(greet())  



# Lambda function with default argument
power = lambda x, y=2: x ** y
print(power(3))      # Uses default argument y=2, Output: 9
print(power(2, 3))   # Overrides default argument, Output: 8
# Lambda function with variable-length arguments
concat = lambda *args: ''.join(args)
print(concat("Hello", " ", "World"))  # Output: Hello World

def add(*args):
    return sum(args)

result = add(1,2,3) #output:6
print(result)
print(add(10, 20, 30,23,12  ))  # Output: 60

