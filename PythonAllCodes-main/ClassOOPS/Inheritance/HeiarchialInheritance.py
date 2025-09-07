class Parent:
    def parent_method(self):
        print("Parent Class")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()
c1.parent_method()
c2.parent_method()
