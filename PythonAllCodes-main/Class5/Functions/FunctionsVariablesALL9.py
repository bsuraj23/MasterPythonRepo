# # Variables, Local Variables, Global Variables - 6 Examples

# # Example 1 - Variables
# message = "Hello World"
# print(message)

# # Example 2 - Local Variables
# def example_func():
#     x = 10
#     print("", x)

# example_func()

# # Example 3 - locals()
# def show_locals():
#     a = 5
#     b = 10
#     print(locals())

# show_locals()

# Example 4 - Global Variables
count = 0

def increment():
    global count
    # count += 1
    
    

increment()
print(count)

# Example 5 - globals()
def show_globals():
    print(globals().keys())

show_globals()

outside =""
# Example 6 - Calling Local Variables Globally
def define_var():
    global outside
    outside = "I am global now"

define_var()
print(outside)
