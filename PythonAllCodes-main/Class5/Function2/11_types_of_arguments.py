# Types of Arguments
def func(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)
func(1, 2, 3, 4, x=5)
