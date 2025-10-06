#code for multiple inheritance concept
class A:
    def func1(self):
        print("This is function 1 from class A")
class B:
    def func1(self):
        print("This is function 2 from class B")
class C(A, B):
    def func3(self):
        print("This is function 3 from class C")
obj = C()
obj.func1() #calling class A function
obj.func1() #calling class B function
obj.func3() #calling class C function
obj1 = A()
obj1.func1() #calling class A function
#obj1.func2() #this will give error as class A object cannot access class B function
#obj1.func3() #this will give error as class A object cannot access class C function
obj2 = B()  
# obj2.func2() #calling class B function
#obj2.func1() #this will give error as class B object cannot access class A function
#obj2.func3() #this will give error as class B object cannot access class C function
#obj3 = C()


# Diamond Problem Example
class X:
    def func(self):
        print("Function from class X")

class Y(X):
    def func(self):
        print("Function from class Y")

class Z(X):
    # def func(self):
    #     print("Function from class Z")

class W(Z,Y):
    pass    


# Create object of W and call func 
obj_w = W()
obj_w.func()  # Shows MRO: Y -> Z -> X



# Show MRO
print("MRO for class W: ", W.__mro__)
obj_w.func()  # Output: Function from class Y
# MRO: Method Resolution Order
# In case of multiple inheritance, Python follows the C3 linearization algorithm to determine the method
# resolution order. You can view the MRO of a class using the __mro__ attribute or the mro() method.
# In the diamond problem example, the MRO for class W is W -> Y -> Z



