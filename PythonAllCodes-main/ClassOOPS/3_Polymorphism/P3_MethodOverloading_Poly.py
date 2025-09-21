#code for MethodOverloading polymorphism concept
#python considers only the last defined method with the same name in a class
#thus we can not achieve method overloading in python like other languages  Java or C++
#but we can achieve method overloading using default arguments or *args or **kwargs 
class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c, d):
        return a + b + c + d
    def add(self, a, b, c, d, e):
        return a + b + c + d + e

math_ops = MathOperations()
# print(math_ops.add(5, 10))          # Calls the first add method
# print(math_ops.add(5, 10, 15))      # Calls the second add method
print(math_ops.add(5, 10, 15, 20))  # Calls the third add method
# Note: In Python, the last defined method will override the previous ones.
# To achieve method overloading, we can use default arguments or *args

#code for *args method overloading
class MathOperationsVarArgs:
    def add(self, *args):
        return sum(args)    
math_ops_var = MathOperationsVarArgs()
print(math_ops_var.add(5, 10))                # Two arguments   
print(math_ops_var.add(5, 10, 15))            # Three arguments
print(math_ops_var.add(5, 10, 15, 20))        # Four arguments
print(math_ops_var.add(5, 10, 15, 20, 25))    # Five arguments
