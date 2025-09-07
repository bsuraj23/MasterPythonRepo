import os

folder = "AssertionsConcepts"
os.makedirs(folder, exist_ok=True)

files_content = {
    "assertions.py": '''# Assertions
x = 5
assert x > 0, "x should be positive"
''',

    "debugging_with_assert.py": '''# Debugging Python Program by using assert Keyword
def divide(a, b):
    assert b != 0, "Division by zero!"
    return a / b
print(divide(10, 2))
# print(divide(10, 0))  # Will raise AssertionError
''',

    "types_of_assert.py": '''# Types of assert Statements
x = 10
assert x == 10
assert x > 0, "x must be positive"
''',

    "exception_vs_assertion.py": '''# Exception Handling vs Assertions
# Exception handling is for expected errors, assertions are for debugging.
try:
    x = int("abc")
except ValueError:
    print("Exception handled")

y = -1
assert y > 0, "Assertion failed: y must be positive"
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)