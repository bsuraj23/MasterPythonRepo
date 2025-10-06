class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person Name: {self.name}"

p = Person("John")
print(p)


#TODO Add more special methods like __repr__, __len__, __add__, etc. 
class Demo:
    def __str__(self):
        return "str called"
    def __repr__(self):
        return "repr called"
d = Demo()
print(str(d))
print(repr(d))
