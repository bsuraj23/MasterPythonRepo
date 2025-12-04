#Passing Members of One Class to Another Class
class A:
    """This is class is having clasmethod and calculator methods"""
    a=90
    def __init__(self, value):
        self.value = value
    def dispay(self):
        print("Value is", self.value)
    @classmethod
    def classMethod(cls):
        print("This is class method")

    @staticmethod
    def staticMethod():
        print("This is static method")

obj2 = A()
print(obj2.a)
obj2.dispay()
obj2.classMethod(B)
obj2.staticMethod()
print(obj2.__doc__)
print(obj2.__name__)
obj2.__class



    


class B:
    def __init__(self, obj):
        self.obj = obj
aobj = B("10")
# aobj.
# bObj = B(aobj)
# print(b.obj.value)


a=45


def add(a,b):
    return a+b

result = add();



