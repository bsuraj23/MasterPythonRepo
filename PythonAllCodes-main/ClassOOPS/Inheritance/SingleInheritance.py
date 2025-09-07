class Parent:
    def display(self):
        print("Parent Class")

class Child(Parent):
    def show(self):
        print("Child Class")

obj = Child()
obj.display()
obj.show()
