class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

shapes = [Circle(), Square()]

for shape in shapes:
    print(shape.area())
