# Function Aliasing
def greet():
    print("Hello!")
hello = greet
hello()

#TODO
#more examples of function aliasing like
#using alias to pass function as argument
def call_function(func):
    func()
call_function(hello)
#using alias to store function in data structures
func_list = [greet, hello]
for f in func_list:
    f() 
#using alias to return function from another function
def get_greet_function():
    return greet    
g = get_greet_function()
g()
greet_alias = g
greet_alias()()