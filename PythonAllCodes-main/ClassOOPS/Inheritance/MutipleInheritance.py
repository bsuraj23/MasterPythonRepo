class Grandparent:
    def show_gp(self):
        print("Grandparent Class")

class Parent(Grandparent):
    def show_p(self):
        print("Parent Class")

class Child(Parent):
    def show_c(self):
        print("Child Class")

obj = Child()
obj.show_gp()
obj.show_p()
obj.show_c()
