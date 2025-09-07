# filter selects elements for which the function returns True
numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)  # Output: [2, 4, 6]
