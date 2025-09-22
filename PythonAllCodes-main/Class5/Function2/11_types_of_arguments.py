# Types of Arguments
def func(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
func(1, 2, 3, 4, x=5)


def add()   :
    return "No arguments"
print(add())  # Output: No arguments

def add(a=0, b=0):
    return a + b
print(add(5, 10))  # Output: 15
print(add(b=10, a=5))  # Output: 15
print(add())  # Output: 0
print(add(5))  # Output: 5