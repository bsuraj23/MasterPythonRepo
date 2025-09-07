# Returning Multiple Values from a Function
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
print(stats([1, 2, 3]))
