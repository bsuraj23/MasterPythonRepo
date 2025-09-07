# Difference between str() and repr() Functions
class Demo:
    def __str__(self):
        return "str called"
    def __repr__(self):
        return "repr called"
d = Demo()
print(str(d))
print(repr(d))
