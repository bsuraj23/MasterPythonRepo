# Types of Variables
# Instance, Static, and Local variables

#self variable is default instance variable available in the class
#Instance variable is the variable which is declared inside the constructor using self keyword  
#Static variable is the variable which is declared inside the class but outside the constructor
#Local variable is the variable which is declared inside the method


class Demo:
    # Static variable (class variable)
    """example class for types of variables"""
    static_var = "I am static!"

    def __init__(self, value):
        # Instance variable
        self.instance_var = value

    def show(self):
        # Local variable
        local_var = "I am local!"
        print("Instance variable:", self.instance_var)
        print("Static variable:", Demo.static_var)
        print("Local variable:", local_var)

d = Demo("I am instance!")
d.show()