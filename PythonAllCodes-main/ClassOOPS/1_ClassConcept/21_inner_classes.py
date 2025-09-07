# Inner Classes
class Outer:
    class Inner:
        def show(self):
            print("Inner class method")
o = Outer()
i = Outer.Inner()
i.show()
