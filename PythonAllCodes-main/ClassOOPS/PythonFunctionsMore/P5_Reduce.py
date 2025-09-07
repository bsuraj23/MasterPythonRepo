from functools import reduce

# reduce applies a rolling computation (like a fold)
numbers = [1, 2, 3, 4,5]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24
