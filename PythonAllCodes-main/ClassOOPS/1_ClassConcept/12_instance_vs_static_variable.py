# Instance Variable vs Static Variable
class Student:
    school = "MET"
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")                 
print(s1.name)        # Instance variable
s1.name = "Charlie"  # Modifying instance variable for s1
print(s2.name)        # Instance variable  
print(Student.school) # Static variable
print(s1.school)     # Accessing static variable via instance   

s1.school = "XYZ School"  # This creates an instance variable for s1     
