#code for multi level inheritance concept
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
obj2 = A()
obj2.func1() #calling class A function
#obj2.func2() #this will give error as class A object cannot access class B function
