import os

folder = "InheritanceConcepts"
os.makedirs(folder, exist_ok=True)

files_content = {
    "inheritance.py": '''# Inheritance
class Parent:
    def show(self):
        print("Parent method")
class Child(Parent):
    pass
c = Child()
c.show()
''',

    "is_a_vs_has_a.py": '''# IS-A vs HAS-A Relationship
# IS-A: Inheritance
class Animal: pass
class Dog(Animal): pass

# HAS-A: Composition
class Engine: pass
class Car:
    def __init__(self):
        self.engine = Engine()
''',

    "composition_vs_aggregation.py": '''# Composition vs Aggregation
# Composition: Strong ownership
class Heart: pass
class Human:
    def __init__(self):
        self.heart = Heart()

# Aggregation: Weak ownership
class Department: pass
class Employee:
    def __init__(self, dept):
        self.dept = dept
''',

    "types_of_inheritance.py": '''# Types of Inheritance
class A: pass
class B(A): pass           # Single
class C(A, B): pass        # Multiple
class D(B): pass           # Multilevel
class E(A): pass           # Hierarchical
''',

    "mro.py": '''# Method Resolution Order (MRO)
class A: pass
class B(A): pass
class C(B): pass
print(C.mro())
''',

    "head_tail.py": '''# Head Element vs Tail Terminology
# Head: First class in inheritance chain
# Tail: Remaining classes
class A: pass
class B(A): pass
class C(B): pass
# Head: C, Tail: [B, A, object]
''',

    "how_to_find_merge.py": '''# How to find Merge?
# Merge is used in C3 linearization for MRO
# Example: See mro(P) by using C3 Algorithm
''',

    "finding_mro_c3.py": '''# Finding mro(P) by using C3 Algorithm
class A: pass
class B(A): pass
class C(A): pass
class P(B, C): pass
print(P.mro())
''',

    "super_method.py": '''# super() Method
class Parent:
    def show(self):
        print("Parent")
class Child(Parent):
    def show(self):
        super().show()
        print("Child")
c = Child()
c.show()
''',

    "call_superclass_method.py": '''# How to Call Method of a Particular Super Class?
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
''',

    "important_points_super.py": '''# Various Important Points about super()
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
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)