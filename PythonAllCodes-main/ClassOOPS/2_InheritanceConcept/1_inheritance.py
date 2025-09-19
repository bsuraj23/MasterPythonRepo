#code for inheritance concept
class Parent:
    a=90
    def func1(self):
        print("This is function 1 from Parent class")   
class Child(Parent):   #inheriting Parent class
    c=90
    def func2(self):
        print("This is function 2 from Child class")    
obj = Child()
obj.func1() #calling parent class function  
obj.func2() #calling child class function
obj1 = Parent()
obj1.func1() #calling parent class function
#obj1.func2() #this will give error as parent class object cannot access child class function
#obj1.func2() #this will give error as parent class object cannot access child class function   
