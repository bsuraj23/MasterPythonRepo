import collections
print(dir(collections))  # Shows all collection classes


 
xya = {"a":1, "z":2, "w":3, "t":4, "y":5}
print(xya)
#sort it 
print(sorted(xya))  # Sorts by keys


# : Add more examples of w.rt. Thread Safety like Java Collections
#Examples of collections module
from collections import deque, Counter, defaultdict, OrderedDict, namedtuple    
# Deque (Double-Ended Queue)
dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to the left
dq.append(4)      # Add to the right
print("Deque:", dq)  # Output: Deque: deque([0, 1, 2, 3, 4])
# Counter
cnt = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print("Counter:", cnt)  # Output: Counter: Counter({'apple': 3, 'banana': 2, 'orange': 1})
# DefaultDict
dd = defaultdict(int)
dd['apple'] += 1
dd['banana'] += 2
print("DefaultDict:", dd)  # Output: DefaultDict: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})
# OrderedDict
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['orange'] = 3
print("OrderedDict:", od)  # Output: OrderedDict: OrderedDict([('apple', 1), ('banana', 2), ('orange', 3)])
# NamedTuple
Point = namedtuple('Point', ['x', 'y']) 
p = Point(10, 20)
print("NamedTuple:", p, "x:", p.x, "y:", p.y)
# Output: NamedTuple: Point(x=10, y=20) x: 10 y: 20
# More examples of collections
# ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = collections.ChainMap(dict1, dict2)
print("ChainMap:", chain)  # Output: ChainMap: ChainMap({'a':    1, 'b': 2}, {'b': 3, 'c': 4})
# UserDict
from collections import UserDict
class MyDict(UserDict):
    def __setitem__(self, key, value):
        print(f"Setting {key} to {value}")
        super().__setitem__(key, value)
my_dict = MyDict()
my_dict['a'] = 1  # Output: Setting a to 1
print("UserDict:", my_dict)  # Output: UserDict: {'a': 1}
# UserList
from collections import UserList
class MyList(UserList):
    def append(self, item):
        print(f"Appending {item}")
        super().append(item)
my_list = MyList()
my_list.append(1)  # Output: Appending 1
print("UserList:", my_list)  # Output: UserList: [1]
