# How to Delete Static Variables of a Class
class Student:
    school = "ABC School"
print(Student.school)
del Student.school
print(Student.school)
