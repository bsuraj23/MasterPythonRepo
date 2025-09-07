# Types of Inheritance
class A: pass
class B(A): pass           # Single
class C(A, B): pass        # Multiple
class D(B): pass           # Multilevel
class E(A): pass           # Hierarchical
