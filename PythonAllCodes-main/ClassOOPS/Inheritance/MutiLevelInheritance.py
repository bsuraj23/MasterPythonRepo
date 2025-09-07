class A:
    def methodA(self):
        print("Class A")

class B:
    def methodB(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.methodA()
obj.methodB()
