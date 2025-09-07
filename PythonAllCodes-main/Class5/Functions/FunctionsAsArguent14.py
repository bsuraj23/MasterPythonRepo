# *args and **kwargs - 6 Examples

# Example 1: *args - sum all numbers
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))

# Example 2: *args - print all arguments
def print_args(*args):
    print(args)

print_args("apple", "banana", "cherry")

# Example 3: **kwargs - print key-value pairs
def show_kwargs(**kwargs):
    print
