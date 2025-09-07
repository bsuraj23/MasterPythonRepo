# Control Flow in try-except
try:
    print("Try block")
    x = 1 / 0
    print("After error")
except ZeroDivisionError:
    print("Except block")
print("After try-except")
