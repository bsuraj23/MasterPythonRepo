#code hybrid inheritance concept
class A:
    def func1(self):
        print("This is function 1 from class A")
class B(A):
    def func2(self):
        print("This is function 2 from class B")
class C(B):
    def func3(self):
        print("This is function 3 from class C")
obj = C()
obj.func1() #calling class A function
obj.func2() #calling class B function
obj.func3() #calling class C function