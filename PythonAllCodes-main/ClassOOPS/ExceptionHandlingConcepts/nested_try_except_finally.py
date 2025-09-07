# Nested try-except-finally Blocks
try:
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner except")
finally:
    print("Outer finally")
