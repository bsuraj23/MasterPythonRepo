#code for constructor  overloading polymorphism concept

class MathOperations:
    def __init__(self, a, b):
       self.a = a
       self.b = b
       self.c = 0
       print("Two arguments constructor called")

    
    def __init__(self, a):
       self.a = a
       self.b = 0
       self.c = 0
       print("One argument constructor called")
    def __init__(self):
         self.a = 0
         self.b = 0
         self.c = 0
         print("No arguments constructor called")

    def __init__(self, *args): #variable length arguments
       print("type of args:", type(args))
       print("Variable Length arguments constructor called")


    def add(self,a,b,c):
       return self.a + self.b + self.c
# Creating objects with different number of arguments
math_ops1 = MathOperations(5, 10)        # Two arguments
math_ops2 = MathOperations(5, 10, 15)    # Three arguments  
math_ops3 = MathOperations(5)            # One argument
math_ops4 = MathOperations()              # No arguments
#variable length arguments
math_ops5 = MathOperations(5, 10, 15, 20) #Four arguments
math_ops6 = MathOperations(5, 10, 15, 20, 25) #Five arguments
math_ops7 = MathOperations(5, 10, 15, 20, 25, 30) #Six arguments
math_ops8 = MathOperations(5, 10, 15, 20, 25, 30, 35) #Seven arguments 



print(math_ops1.add(1,2,3))  # two arguments
print(math_ops2.add(1,2,3))  # three arguments
print(math_ops3.add(1,2,3))  # one argument

print(math_ops4.add())  # no arguments
