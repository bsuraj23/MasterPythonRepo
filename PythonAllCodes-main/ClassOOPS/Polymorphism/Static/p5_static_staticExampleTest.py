class MyCounter:
    count = 0  # class variable

    def __init__(self):
        MyCounter.count += 1

    @staticmethod
    def get_count():
        print("Static count:", MyCounter.count)

# Create 3 objects
a = MyCounter()
b = MyCounter()
c = MyCounter()

MyCounter.get_count()  # Static count: 3
