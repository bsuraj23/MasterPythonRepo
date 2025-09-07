# Example 1: Direct assignment (no actual copy)
a = [1, 2, 3]
b = a  # Both point to same list
b.append(4)
print(a)  # Output will change because a and b share the same list

# Example 2: Changing b affects a
b[0] = 99
print(a)

# Example 3: Check memory IDs
print(id(a))
print(id(b))

# Example 4: Compare if a and b are same object
print(a is b)

# Example 5: Reference copying in dictionary
dict1 = {'x': 1}
dict2 = dict1
dict2['y'] = 2
print(dict1)

# Example 6: Reference sharing with lists inside a list
list1 = [[1, 2], [3, 4]]
list2 = list1
list2[0][0] = 999
print(list1)
