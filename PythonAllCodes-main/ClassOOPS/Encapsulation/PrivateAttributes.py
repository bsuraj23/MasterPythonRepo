class Example:
    def __init__(self):
        self.__secret = 50

obj = Example()
print(obj._Example__secret)  # Accessing private attribute
