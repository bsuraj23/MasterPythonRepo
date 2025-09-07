class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)
