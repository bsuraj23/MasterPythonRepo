class Example:
    def __private_method(self):
        print("Private Method")

    def call_private(self):
        self.__private_method()

obj = Example()
 # This will raise an AttributeError
obj.call_private()

#TODO   check from all angles java way ..other module access check etc
