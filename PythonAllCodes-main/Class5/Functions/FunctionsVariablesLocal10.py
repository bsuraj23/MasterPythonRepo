# locals() - 6 Examples

# Example 1
def show_locals():
    x = 10
    y = 20
    print(locals())

show_locals()

# Example 2
def sum_numbers(a, b):
    result = a + b
    print(locals())

sum_numbers(5, 7)

# Example 3
def inside_func():
    name = "Alice"
    age = 25
    print("Local variables:", locals())

inside_func()

# Example 4
def square_and_log(n):
    square = n * n
    print("priniting Last ",locals())

square_and_log(78)
