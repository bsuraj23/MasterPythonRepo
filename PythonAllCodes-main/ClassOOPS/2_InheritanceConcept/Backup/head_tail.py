# Head Element vs Tail Terminology
# Head: First class in inheritance chain
# Tail: Remaining classes
class A: pass
class B(A): pass
class C(B): pass
# Head: C, Tail: [B, A, object]
