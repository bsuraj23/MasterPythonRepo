# recursive  Function
def square(x):
    if x == 1:
        return 1
    else:
        return x * square(x-1)
print(square(4))

# Function inside function
def outer_function():   
    print("I am outer function")
    def inner_function():
        print("I am inner function")
    inner_function()        
outer_function()    
# inner_function()  #error

#TODO
#more examples of recursion
#factorial ,fibonacci,tail recursion etc


