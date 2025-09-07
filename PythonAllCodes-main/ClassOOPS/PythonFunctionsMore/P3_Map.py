# map applies a function to every item in an iterable
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, numbers))

print(squares)  # Output: [1, 4, 9, 16]
