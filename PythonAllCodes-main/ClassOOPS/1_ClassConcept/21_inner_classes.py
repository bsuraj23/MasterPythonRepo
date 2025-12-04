# Inner Classes
class Outer:
    class Inner:
        def show(self):
            print("Inner class method")
o = Outer()
i = Outer.Inner()
i.show()


class A:
    var =90
    def function():
        print("Outer class method")
        w=89
    class B:
        def show(self):
            a=90
            print("Inner class method")

obj1 = A()
obj2 = A.B()

obj2.show()
