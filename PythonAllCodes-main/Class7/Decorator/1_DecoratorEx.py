#code for decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function 

@decorator_function
def display():
    print("Display function executed")

# display()




#output
#Wrapper executed this before display
#Display function executed

#more examples
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed")

@decorator_function
def show():
    print("Show function executed")
    display()

display()
show()

    

