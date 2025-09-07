import copy

# Example 1: Using copy.deepcopy()
list1 = [[1, 2], [3, 4]]
list2 = copy.deepcopy(list1)
list2[0][0] = 999
print(list1)  # Original stays safe

# Example 2: Deep copy of dictionary
dict1 = {'x': [10, 20]}
dict2 = copy.deepcopy(dict1)
dict2['x'][0] = 100
print(dict1)

# Example 3: Using deepcopy with nested lists
nested = [[[1, 2]], [[3, 4]]]
copy_nested = copy.deepcopy(nested)
copy_nested[0][0][0] = 555
print(nested)

# Example 4: deepcopy in function
def make_safe_copy(data):
    return copy.deepcopy(data)

safe_copy = make_safe_copy(list1)
safe_copy[1][1] = 777
print(list1)

# Example 5: Comparing IDs of sublists
print(id(list1[0]))
print(id(list2[0]))  # IDs differ

# Example 6: Nested dictionaries deepcopy
dict_nested = {'a': {'b': 2}}
dict_copied = copy.deepcopy(dict_nested)
dict_copied['a']['b'] = 999
print(dict_nested)
