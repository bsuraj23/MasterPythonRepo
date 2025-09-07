class Laptop:
    """kfhgdhfgdshfdsgfgdsfgdsdsgf"""
    def __init__(self, ram, storage, processor):
        self.ram = ram
        self.storage = storage
        self.processor = processor

surajLaptop = Laptop("8GB", "512GB SSD", "i5")
amitLaptop = Laptop("16GB", "1TB SSD", "i7")

print(surajLaptop.processor)  # i5
print(amitLaptop.processor)  # i7
print(amitLaptop.__doc__)