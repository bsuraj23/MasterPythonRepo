#MRO
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())

#more examples of MRO
class P: pass
class Q(P): pass
class R(Q): pass
print(R.mro())
class S(R): pass
print(S.mro())
class T(S): pass
print(T.mro())
class U(T): pass
print(U.mro())


#super function
class X:
    def func(self):
        print("This is function from class X")

class Y(X):
    def func(self):
        super().func()
        print("This is function from class Y")

class Z(Y):
    def func(self):
        super().func()
        print("This is function from class Z")

obj = Z()
obj.func()  #calling class Z function which will call super class function
obj1 = Y()
obj1.func() #calling class Y function which will call super class function  
obj2 = X()
obj2.func() #calling class X function
#obj2 = Y()
#obj2.func() #this will give error as class X object cannot access class Y function
#obj3 = Z() 
#obj3.func() #this will give error as class X object cannot access class Z function
#obj4 = X()
#obj4.func() #this will give error as class Y object cannot access class X function
#obj5 = Z()
#obj5.func() #this will give error as class Y object cannot access class Z function
#obj6 = X()
#obj6.func() #this will give error as class Z object cannot access class X function

#obj7 = Y()
#obj7.func() #this will give error as class Z object cannot access class Y function
#obj8 = Z()
#obj8.func() #this will give error as class Z object cannot access class Z function 
#obj9 = X()
#obj9.func() #this will give error as class Z object cannot access class X function 
#obj10 = Y()
#obj10.func() #this will give error as class Z object cannot access class Y function