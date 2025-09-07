class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

objC = Child()


objP = Parent()



objC.greet()
objP.greet()


