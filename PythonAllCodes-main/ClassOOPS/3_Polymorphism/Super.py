class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
       
        print("Child constructor")
        super().__init__()  # Call the parent class constructor

obj = Child()

