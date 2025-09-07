# Various Places to declare Static Variables
class Student:
    school = "ABC School"  # Inside class
    def __init__(self):
        Student.school = "XYZ School"  # Inside constructor
    def set_school(self):
        Student.school = "New School"  # Inside method
