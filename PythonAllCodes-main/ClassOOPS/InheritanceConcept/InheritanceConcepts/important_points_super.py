# Various Important Points about super()
# super() is used to call parent class methods
# Works with multiple inheritance and MRO
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        super().show()
        print("B")
b = B()
b.show()
