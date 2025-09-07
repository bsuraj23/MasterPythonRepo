# Types of Variables
# Instance, Static, and Local variables

class Demo:
    # Static variable (class variable)
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