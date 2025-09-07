# How to Call Method of a Particular Super Class?
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(B, A):
    def show(self):
        A.show(self)
        B.show(self)
c = C()
c.show()
