#Passing Members of One Class to Another Class
class A:
    def __init__(self, value):
        self.value = value
class B:
    def __init__(self, obj):
        self.obj = obj
a = A(10)
b = B(a)
print(b.obj.value)

