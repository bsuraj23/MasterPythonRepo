class Example:
    def __private_method(self):
        print("Private Method")

    def call_private(self):
        self.__private_method()

obj = Example()
obj.call_private()
