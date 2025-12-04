# Instance Variable vs Static Variable

class Student:
    exam = 13
  
    def __init__(self, name):
        self.name = name
        a=90
    def display():
        print("hello")
      
        

s1 = Student("RamaKrishna")
s2 = Student("ayub")   #staic , instance ,   g              
print(s1.name)        # Instance variable
s2.name = "ali"  # Modifying instance variable for s1
print(s1.name)
print(s2.name)        # Instance variable  
print(Student.exam) # Static variable
print(s1.exam)     # Accessing static variable via instance   

Student.exam = 20   # This creates an instance variable for s1
print(s2.exam)  
print(s1.a)   
s1.a= 12
print(s1.a)
print(s2.a)  