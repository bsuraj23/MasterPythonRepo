# reduce() Function
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)
# Output: 24 (1*2*3*4)

def multiply(x, y):
    return x * y
result = reduce(multiply, [1, 2, 3, 4])
print(result)  # Output: 24 (1*2*3*4)


#same code without lambda function
numbers = [1, 2, 3, 4]
product = reduce(multiply, numbers)
print(product)  # Output: 24 (1*2*3*4)