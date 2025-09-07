# any()
# print(any([False, False, True]))
# print(any([0, 0, 1]))
# print(any(['', 'Hello']))
# print(any([]))
# print(any([None, False, 0, "non-empty"]))

# all()
print(all([True, True, True]))
print(all([1, 2, 3]))
print(all(['Hello', 'World']))
print(all([1, 5, 3]))  # False due to 0
print(all([]))  # Returns True (empty iterable)
