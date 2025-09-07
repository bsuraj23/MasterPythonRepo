# Destructors
class Test:
    def __del__(self):   #___init__ is constructor and __del__ is destructor
        print("Destructor called")
t = Test()
del t
