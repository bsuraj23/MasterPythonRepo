import os

folder = "ClassConcept"
os.makedirs(folder, exist_ok=True)

files_content = {
    "oop_part1.py": '''# OOP’s Part – 1
# Object-Oriented Programming introduces classes and objects in Python.
''',

    "what_is_class.py": '''# What is Class?
# A class is a blueprint for creating objects.
''',

    "define_class.py": '''# How to define a Class?
class Student:
    pass
''',

    "what_is_object.py": '''# What is Object?
# An object is an instance of a class.
class Student:
    pass
s = Student()
''',

    "reference_variable.py": '''# What is Reference Variable?
class Student:
    pass
s1 = Student()
s2 = s1  # s2 is a reference variable pointing to the same object as s1
''',

    "self_variable.py": '''# Self Variable
class Student:
    def show(self):
        print("self refers to:", self)
s = Student()
s.show()
''',

    "constructor_concept.py": '''# Constructor Concept
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Alice")
print(s.name)
''',

    "methods_vs_constructors.py": '''# Differences between Methods and Constructors
class Test:
    def __init__(self):
        print("Constructor")
    def show(self):
        print("Method")
t = Test()
t.show()
''',

    "types_of_variables.py": '''# Types of Variables
# Instance, Static, and Local variables
''',

    "declare_instance_variables.py": '''# Where we can declare Instance Variables
class Student:
    def __init__(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
''',

    "access_instance_variables.py": '''# How to Access Instance Variables
class Student:
    def __init__(self, name):
        self.name = name
s = Student("Bob")
print(s.name)
''',

    "delete_instance_variable.py": '''# How to delete Instance Variable from the Object
class Student:
    def __init__(self):
        self.name = "Tom"
s = Student()
del s.name
''',

    "static_variables.py": '''# Static Variables
class Student:
    school = "ABC School"
''',

    "instance_vs_static_variable.py": '''# Instance Variable vs Static Variable
class Student:
    school = "ABC School"
    def __init__(self, name):
        self.name = name
''',

    "declare_static_variables.py": '''# Various Places to declare Static Variables
class Student:
    school = "ABC School"  # Inside class
    def __init__(self):
        Student.school = "XYZ School"  # Inside constructor
    def set_school(self):
        Student.school = "New School"  # Inside method
''',

    "access_static_variables.py": '''# How to access Static Variables
class Student:
    school = "ABC School"
print(Student.school)
''',

    "modify_static_variable.py": '''# Where we can modify the Value of Static Variable
class Student:
    school = "ABC School"
    def change_school(self, new_name):
        Student.school = new_name
''',

    "delete_static_variable.py": '''# How to Delete Static Variables of a Class
class Student:
    school = "ABC School"
del Student.school
''',

    "local_variables.py": '''# Local Variables
class Test:
    def show(self):
        x = 10  # Local variable
        print(x)
''',

    "types_of_methods.py": '''# Types of Methods
# Instance, Class, and Static methods
class Demo:
    def instance_method(self): pass
    @classmethod
    def class_method(cls): pass
    @staticmethod
    def static_method(): pass
''',

    "setter_getter_methods.py": '''# Setter and Getter Methods
class Student:
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
''',

    "passing_members.py": '''# Passing Members of One Class to Another Class
class A:
    def __init__(self, value):
        self.value = value
class B:
    def __init__(self, obj):
        self.obj = obj
a = A(10)
b = B(a)
print(b.obj.value)
''',

    "inner_classes.py": '''# Inner Classes
class Outer:
    class Inner:
        def show(self):
            print("Inner class method")
o = Outer()
i = Outer.Inner()
i.show()
''',

    "garbage_collection.py": '''# Garbage Collection
import gc
print(gc.isenabled())
''',

    "enable_disable_gc.py": '''# How to enable and disable Garbage Collector in our Program
import gc
gc.disable()
gc.enable()
''',

    "destructors.py": '''# Destructors
class Test:
    def __del__(self):
        print("Destructor called")
t = Test()
del t
''',

    "number_of_references.py": '''# How to find the Number of References of an Object
import sys
class Student: pass
s = Student()
print(sys.getrefcount(s))
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)