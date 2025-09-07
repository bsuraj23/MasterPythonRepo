# Overloading
# Python does not support method overloading directly
class Demo:
    def show(self, a=None, b=None):
        print(a, b)
d = Demo()
d.show()
d.show(1)
d.show(1, 2)
