# Local Variables
class Test:
    x=90
    def show(self):
        x = 10  # Local variable
        print(x)

    def otherFucntion():
        print("x value is",x)

print(x)