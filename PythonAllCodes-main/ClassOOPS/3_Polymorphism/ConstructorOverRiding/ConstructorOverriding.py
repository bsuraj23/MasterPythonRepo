class Parent:
    def __init__(self):
        print("Parent constructor")
        c=89+9
        print(c)
    def add(self, a, b):
        print("i am add function ")

class Child(Parent):
    a=90

# obj = Child()
objP = Parent()
objP.add(12,3)

objC = Child()