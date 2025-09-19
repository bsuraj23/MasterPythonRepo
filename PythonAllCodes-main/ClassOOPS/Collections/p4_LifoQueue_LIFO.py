from queue import LifoQueue

obj = LifoQueue()
#default size we get is infinite
#we can also set maxsize while creating object
obj.put('A')
obj.put('B')

print(obj.get())  # B
print(obj.get())  # A

obj.put('C')
print(obj.get())  # C
print(obj.empty())  # True
print(obj.full())   # False
print(obj.qsize())  # 0
print(obj.maxsize)  # 0 (0 means infinite size)


