from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)

print(p1.x, p1.y)  # 10 20
print(p1)          # Point(x=10, y=20)
