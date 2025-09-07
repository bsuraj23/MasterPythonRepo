#code for single level inheritance concept
class A:
    def func1(self):
        print("This is function 1 from class A")
class B(A):   #inheriting class A
    def func2(self):
        print("This is function 2 from class B")
obj = B()
obj.func1() #calling class A function   
obj.func2() #calling class B function
obj1 = A()
obj1.func1() #calling class A function  
#obj1.func2() #this will give error as class A object cannot access class B function
