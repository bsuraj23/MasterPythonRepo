# Exception Handling vs Assertions
# Exception handling is for expected errors, assertions are for debugging.
try:
    x = int("abc")
except ValueError:
    print("Exception handled")

y = -1
assert y > 0, "Assertion failed: y must be positive"
