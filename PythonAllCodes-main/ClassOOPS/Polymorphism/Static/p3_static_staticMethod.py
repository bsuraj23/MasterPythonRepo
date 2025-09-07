#Static Methods
#Don’t need access to instance (self) or class (cls).

#Use @staticmethod decorator.

#Behave like normal functions, just live inside a class.

class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

print(Calculator.add(10, 20))  # 30



