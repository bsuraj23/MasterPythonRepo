# yield is used to make a generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

for val in simple_generator():
    print(val)
