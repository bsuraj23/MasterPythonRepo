# finally Block
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Error")
finally:
    print("Finally block always executes")
