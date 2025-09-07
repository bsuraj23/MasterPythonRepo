# How to find the Number of References of an Object
import sys
class Student: pass
s = Student()
print(sys.getrefcount(s))
