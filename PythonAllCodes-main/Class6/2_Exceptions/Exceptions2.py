try:
    print(int("t"))
except ValueError:
    print("Invalid number format")
except ZeroDivisionError:
    print("Division by zero error")


def add():
    try:
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        print("Addition is ", a / b)   
    
    except ValueError:
        print("Invalid input, please enter numeric values.")
    except ZeroDivisionError:
        print("Division by zero error")