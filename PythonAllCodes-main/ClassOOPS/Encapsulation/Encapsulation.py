# Example 1: Public Variable
class Car:
    def __init__(self,name):
        self.color = "Red"
object = Car()




# Example 2: Private Variable
class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

# Example 3: Protected Variable
class Employee:
    def __init__(self):
        self._salary = 50000

# Example 4: Getter and Setter
class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, m):
        self.__marks = m

# Example 5: Using Property Decorator
class Laptop:
    def __init__(self):
        self.__price = 50000

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value
