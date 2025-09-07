# Destructors
class Test:
    def __del__(self):
        print("Destructor called")
t = Test()
del t
