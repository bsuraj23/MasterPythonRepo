# Control Flow in try-except-finally
try:
    print("Try")
    x = 1 / 0
except ZeroDivisionError:
    print("Except")
finally:
    print("Finally")
print("After all")
