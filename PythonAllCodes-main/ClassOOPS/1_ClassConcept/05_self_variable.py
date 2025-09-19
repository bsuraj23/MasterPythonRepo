# Self Variable
class Student:
    i=90
    def show():
        print("self refers to:")
     

s = Student()
s.show()
s.j = 100
s.show()

s2 = Student()
s2.show()
s2.j = 200
s2.show()   
