from collections import namedtuple

-- cannot be changed after creation

Point = namedtuple('Point', ['x', 'y'])

p1 = Point(10, 20)

print(p1.x, p1.y)  # 10 20
print(p1)          # Point(x=10, y=20)

p2 = Point(x=30, y=40)
print(p2)          # Point(x=30, y=40)
# p1.x = 50  # This will raise AttributeError
# print(p1)

#TODO : Add more examples of namedtuple
p3 = Point(50, 60)
print(p3)          # Point(x=50, y=60)
p4 = Point(70, 80)
print(p4)          # Point(x=70, y=80)  
print(p1 == p2)   # False
print(p1 == p3)   # False
print(p1 == Point(10, 20))  # True
print(p1.x + p2.x)  # 40


