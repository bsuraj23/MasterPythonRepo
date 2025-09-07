# Return vs Print - 6 Examples

# Example 1
def using_return():
    return "Returned value"

print(using_return())

# Example 2
def using_print():
    print("Printed value")

using_print()

# Example 3
def sum_return(a, b):
    return a + b

# Example 4
def sum_print(a, b):
    print(a + b)

# Example 5
result = sum_return(4, 5)
print(result)

# Example 6
sum_print(4, 5)
