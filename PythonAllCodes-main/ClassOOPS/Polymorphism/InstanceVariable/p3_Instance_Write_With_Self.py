class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

print(car1.brand, car1.color)  # Toyota Red
print(car2.brand, car2.color)  # BMW Black
print(car1.__dict__)  # {'brand': 'Toyota', 'color': 'Red'}
print(car2.__dict__)  # {'brand': 'BMW', 'color': 'Black'}
