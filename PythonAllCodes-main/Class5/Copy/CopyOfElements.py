# Example 1: Copy elements using slicing
numbers = [10, 20, 30]
copy_numbers = numbers[:]
print(copy_numbers)

# Example 2: Copy elements using list()
copy_numbers = list(numbers)
print(copy_numbers)

# Example 3: Using loop
copy_numbers = []
for n in numbers:
    copy_numbers.append(n)
print(copy_numbers)

# Example 4: List comprehension
copy_numbers = [x for x in numbers]
print(copy_numbers)

# Example 5: Using extend()
copy_numbers = []
copy_numbers.extend(numbers)
print(copy_numbers)

# Example 6: Using copy module
import copy
copy_numbers = copy.copy(numbers)
print(copy_numbers)
