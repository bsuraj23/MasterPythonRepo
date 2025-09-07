class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, user_string):
        name, age = user_string.split('-')
        return cls(name, int(age))

# Using constructor normally
u1 = User("Ravi", 25)

# Using class method to create object from string
u2 = User.from_string("Amit-30")

print(u1.name, u1.age)  # Ravi 25
print(u2.name, u2.age)  # Amit 30
