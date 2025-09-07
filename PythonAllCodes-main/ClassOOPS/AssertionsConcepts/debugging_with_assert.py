# Debugging Python Program by using assert Keyword
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b
print(divide(10, 2))
# print(divide(10, 0))  # Will raise AssertionError
