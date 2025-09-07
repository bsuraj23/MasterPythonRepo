# Control Flow in nested try-except-finally
try:
    try:
        print("Inner try")
        x = 1 / 0
    except ZeroDivisionError:
        print("Inner except")
    finally:
        print("Inner finally")
except:
    print("Outer except")
finally:
    print("Outer finally")
