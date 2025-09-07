# super() Method
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        super().show()
        print("Child")
c = Child()
c.show()
