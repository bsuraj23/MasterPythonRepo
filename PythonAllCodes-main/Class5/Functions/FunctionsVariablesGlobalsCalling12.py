# Calling Local Variables Globally - 6 Examples

# Example 1
def make_global():
    global a
    a = "Now I am global"

make_global()
print(a)

# Example 2
def define_var():
    global message
    message = "Access me outside"

define_var()
print(message)

# Example 3
def create_global_variable():
    global num
    num = 42

create_global_variable()
print(num)

# Example 4
def declare_globally():
    global temp
    temp = "Global from inside function"

declare_globally()
print(temp)

# Example 5
def inside():
    global result
    result = "Declared inside but accessible globally"

inside()
print(result)

# Example 6
def outer():
    global outside_var
    outside_var = 999

outer()
print(outside_var)
