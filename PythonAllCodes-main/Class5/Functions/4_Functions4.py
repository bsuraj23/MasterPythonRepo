a=90
#code is sqauring the number 
def square(n):
    """ This function suare the input and  returns the same square """
    
    return n * n

# print("Square of 5 is", square(5))
# print("Square of 9 is", square(9))
print(square.__doc__)




#keyword Argument 
def greet(name="Guest"):
    """ This function greets to the person passed in as a parameter """
    print("Hello,", name)

#fibonacci seriers example
def fibonacci(n):
    """ This function returns the fibonacci series upto n terms """
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series
print(fibonacci(10))
print(fibonacci.__doc__)
# Decorators in Python
# A decorator is a function that takes another function and extends the behavior of the latter function without
# explicitly modifying it.
# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.
#code for MethodOverloading polymorphism concept
#python considers only the last defined method with the same name in a class
#thus we can not achieve method overloading in python like other languages  Java or C++










