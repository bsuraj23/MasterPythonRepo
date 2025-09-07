# globals() - 6 Examples

# Example 1
x = 100
print("first line ",globals())

# Example 2
y = "Python"
print("y found in globals:", 'y' in globals())

# Example 3
def show_globals():
    print(globals())

show_globals()

# Example 4
z = [1, 2, 3]
print("Globals keys:", list(globals().keys()))

# Example 5
def modify_global():
    globals()['new_var'] = "Created Globally"

modify_global()
print(new_var)

# Example 6
PI = 3.1415
def print_globals_example():
    print(globals()['PI'])

print_globals_example()
