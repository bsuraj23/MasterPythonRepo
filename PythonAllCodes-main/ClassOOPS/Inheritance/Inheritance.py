# Example 1: Single Inheritance
# class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     pass

# Example 2: Method Overriding
class Parent:
    def showP(self):
        print("Parent Method")
    def addP(self,a,b):
        c=a+b
        print("Parent Method add function",c)
    def onlytoParent(self):
        print("onlytoParent")

class Child(Parent):
    def showCh(self):
        print("Child Method")
    def addChild(self):
        print("Child Method add function")

# pObj = Parent()
# pobject2 = Parent()
# cObj =Child()

# # print(pObj)
# print(cObj.addP(23,34))




# Example 3: Multi-Level Inheritance
class A:
    pass

class B(A):
    pass

class C(B):
    pass

# Example 4: Multiple Inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# Example 5: Using super()
class Parent:    
    def add(self):
        print("Parent class")
    def multi(self):
        print("Parent class")
    def display(self):
        print("Parent class")
class Child(Parent):
    def display(self):
        # super().display()
        print("Child class")

dddd =Parent()
uuuu = Child()

dddd.display()
uuuu.display()