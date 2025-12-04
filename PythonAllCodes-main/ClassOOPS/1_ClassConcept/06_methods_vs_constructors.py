# Differences between Methods and Constructors
class Test:
    a=90
    def __init__(self): 
        a=90       
        print("Constructor")
    def show(self):
        
        print("Method")


object1= Test()   #creating object will call constructor


object1.show()



