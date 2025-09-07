# Public, Private and Protected Members
class Demo:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
    def show(self):
        print(self.public, self._protected, self.__private)
d = Demo()
d.show()
print(d.public)
print(d._protected)
# print(d.__private) # Error
print(d._Demo__private) # Access private
