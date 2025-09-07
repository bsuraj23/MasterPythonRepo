# Example 1: Simple list copy using slicing
list1 = [1, 2, 3]
list2 = list1[:]
print(list2)

# Example 2: Copy using list() function
list3 = list(list1)
print(list3)

# Example 3: Copy using copy module
import copy
list4 = copy.copy(list1)
print(list4)

# Example 4: Copy using append in a loop
list5 = []
for item in list1:
    list5.append(item)
print(list5)

# Example 5: Copy using list comprehension
list6 = [x for x in list1]
print(list6)

# Example 6: Copy using extend()
list7 = []
list7.extend(list1)
print(list7)
