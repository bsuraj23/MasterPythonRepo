#code for inheritance concept is a
class A:
    def func1(self):
        print("This is function 1 from class A")    
class B(A):   #inheriting class A
    def func2(self):
        print("This is function 2 from class B")    
class C(B):   #inheriting class B
    def func3(self):
        print("This is function 3 from class C")
obj = C()
obj.func1() #calling class A function   
obj.func2() #calling class B function
obj.func3() #calling class C function
obj1 = B()
obj1.func1() #calling class A function
obj1.func2() #calling class B function  
#obj1.func3() #this will give error as class B object cannot access class C function

#Has a relationship
class D:
    def func4(self):
        print("This is function 4 from class D")    
class E:
    def func5(self):
        print("This is function 5 from class E")    
class F:

    def __init__(self):
        self.d = D()  #F has a relationship with D
        self.e = E()  #F has a relationship with E
    def func6(self):
        print("This is function 6 from class F")