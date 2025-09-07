# Method Resolution Order (MRO)
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())
