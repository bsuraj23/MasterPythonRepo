#generate code for generator example 
def simple_generator():
    yield 1
    yield 2454
    yield 33
    yield 40000


lst = simple_generator()
for temp in lst:
    print(temp)
# print(""""---""")
# print(next(lst))  # Output: 1
# print(next(lst))  # Output: 2
# print(""""---""")

for value in simple_generator():
    print(value)

#generator with loop    
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1  
for number in count_up_to(5):
    print(number)



#generator with expression.... 
squares = (x * x for x in range(1, 6))
for square in squares:
    print(square)
#generator with function and loop
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)      
#infinite generator
# def infinite_counter():
#     count = 0
#     while True:
#         yield count
#         count += 1
#more complex example
def prime_generator():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
for prime in prime_generator():
    if prime > 30:  # Limit output for demonstration
        break
    print(prime)

# Example usage of generator with send()
def echo():
    while True:
        received = yield
        print(f"Received: {received}")
e = echo()
next(e)  # Prime the generator  
e.send("Hello")
e.send("World")
e.close()
# Example usage of generator with throw()
def controlled_generator():
    try:
        yield "Start"
        yield "Running"
        yield "Almost Done"
    except Exception as e:
        yield f"Error: {e}"
    finally:
        yield "Cleanup"
import time
from functools import wraps

# Logging decorator for generators
def logging_generator(gen):
    @wraps(gen)
    def wrapper(*args, **kwargs):
        print(f"Calling generator: {gen.__name__}")
        for value in gen(*args, **kwargs):
            print(f"Yielding: {value}")
            yield value
    return wrapper

# Timing decorator for generators
def timing_generator(gen):
    @wraps(gen)
    def wrapper(*args, **kwargs):
        start = time.time()
        for value in gen(*args, **kwargs):
            yield value
        end = time.time()
        print(f"Generator {gen.__name__} took {end - start:.4f} seconds")
    return wrapper
#use this above and show example 
@timing_generator
def timed_gen():
    for i in range(100000):
        yield i
# Access control decorator for generators
def access_control_generator(gen):
    @wraps(gen)
    def wrapper(*args, **kwargs):
        user = kwargs.get('user', None)
        if user != "admin":
            print("Access denied!")
            return
        yield from gen(*args, **kwargs)
    return wrapper

# Memoization decorator for generators (caches yielded values)
def memoize_generator(gen):
    cache = []
    @wraps(gen)
    def wrapper(*args, **kwargs):
        if cache:
            for value in cache:
                yield value
        else:
            for value in gen(*args, **kwargs):
                cache.append(value)
                yield value
    return wrapper

# Usage examples



@timing_generator
def timed_gen():
    for i in range(100000):
        yield i


#TODO Add code for map filter etc 
