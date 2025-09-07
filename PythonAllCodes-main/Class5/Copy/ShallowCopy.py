import copy

# Example 1: Using copy.copy()
list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)
list2[0][0] = 999
print(list1)  # Inner elements affected

# Example 2: Using slicing
list3 = list1[:]
list3[1][1] = 888
print(list1)  # Inner list changed

# Example 3: Shallow copy of dictionary
dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = copy.copy(dict1)
dict2['a'][0] = 100
print(dict1)  # Changes reflect

# Example 4: list() creates shallow copy
list4 = list(list1)
list4[0][1] = 555
print(list1)

# Example 5: extend() creates shallow copy
list5 = []
list5.extend(list1)
list5[1][0] = 444
print(list1)

# Example 6: copy.copy() of list of lists
nested_list = [[10, 20], [30, 40]]
shallow_copied = copy.copy(nested_list)
shallow_copied[0][1] = 200
print(nested_list)
