# Finding mro(P) by using C3 Algorithm
class A: pass
class B(A): pass
class C(A): pass
class P(B, C): pass
print(P.mro())
