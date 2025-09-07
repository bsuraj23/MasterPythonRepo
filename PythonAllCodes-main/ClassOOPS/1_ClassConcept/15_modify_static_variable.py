# Where we can modify the Value of Static Variable
class Student:
    school = "ABC School"
    def change_school(self, new_name):
        Student.school = new_name


s1 = Student()
s2 = Student()  

print(Student.school)  # Accessing static variable via class
s1.change_school("MET")  # Modifying static variable via instance method     
print(Student.school)  # Accessing static variable via class    