#>>> def fib(n):    # write Fibonacci series up to n
#...     """Print a Fibonacci series up to n."""
#...     a, b = 0, 1
#...     while a < n:
#...         print(a, end=' ')
#...         a, b = b, a+b
#...     print()
#...
#>>> # Now call the function we just defined:
#... fib(2000)
#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

#!/usr/bin/python

def add(a,b):
    c=a+b
    return c
result = add(12,2)
print("The sum is:", result)


# Function definition is here
def justprint( str ):
   "This prints a passed string into this function"
   print (str);
   return;

# Now you can call printme function
justprint("I'm first String to user defined function!");
justprint("Again second String2 to the same function");



