# Find max element in list using recursion
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], find_max(lst[1:]))
print(find_max([4, 7, 1, 9, 2]))
