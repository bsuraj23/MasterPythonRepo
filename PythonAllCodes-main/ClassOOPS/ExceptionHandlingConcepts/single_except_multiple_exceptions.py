# Single except Block that can handle Multiple Exceptions
try:
    x = int("abc")
except (ValueError, TypeError):
    print("ValueError or TypeError")
