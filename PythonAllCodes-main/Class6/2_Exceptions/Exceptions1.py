try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero error do not give zero ")

   
def add():
    try:
        a = int(input("Enter first number"))
        b = int(input("Enter second number"))
        print("div is ", a / b)    
    
    except Exception as e:
            print("you got error please check it ", e)
add()