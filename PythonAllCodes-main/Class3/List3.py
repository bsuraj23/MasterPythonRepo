numbers = [21, 34, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(32)

print("After Append:", numbers)


prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8]
print("List2:", even_numbers)
    
odd_number = [1, 3, 5]
print("List3:", odd_number)

# join two lists
prime_numbers.extend(odd_number)

print("List after append: of even to prime", prime_numbers)
