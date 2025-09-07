class Demo:
    def show(self, a=None, b=None):
        if a and b:
            print(a, b)
        elif a:
            print(a)
        else:
            print("No arguments")

obj = Demo()
obj.show()
obj.show(10)
obj.show(10, 20)
