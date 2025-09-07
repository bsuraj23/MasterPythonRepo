class MyList:
    def __init__(self):
        self.data = []

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __iter__(self):
        return iter(self.data)

    def append(self, value):
        self.data.append(value)

    def __str__(self):
        return str(self.data)


# Testing MyList class
ml = MyList()
ml.append(10)
ml.append(20)
ml.append(30)

print(ml)           # [10, 20, 30] --> Uses __str__
print(ml[1])        # 20 --> Uses __getitem__

ml[1] = 99          # Uses __setitem__
print(ml)           # [10, 99, 30]

del ml[0]           # Uses __delitem__
print(ml)           # [99, 30]

for item in ml:     # Uses __iter__
    print(item)
