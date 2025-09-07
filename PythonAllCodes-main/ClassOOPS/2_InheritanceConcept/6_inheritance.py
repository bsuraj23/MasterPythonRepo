#code for hierarchical inheritance concept
class B(A): pass
class C(B): pass
print(C.mro())

class D(A): pass
class E(A): pass
class F(B): pass