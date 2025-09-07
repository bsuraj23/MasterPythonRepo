# Types of Methods
# Instance, Class, and Static methods
class Demo:
    def instance_method(self): pass
    @classmethod
    def class_method(cls): pass
    @staticmethod
    def static_method(): pass


class Student:
    school = "ABC School"
    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("XYZ School")
print(Student.school)  # XYZ School