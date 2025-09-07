class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person Name: {self.name}"

p = Person("John")
print(p)
