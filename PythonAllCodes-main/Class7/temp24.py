import os

folder = "Class7/Module"
os.makedirs(folder, exist_ok=True)

files_content = {
    "modules.py": '''# MODULES
import math
print(math.pi)
''',

    "module_aliasing.py": '''# Renaming a Module at the time of import (Module Aliasing)
import math as m
print(m.sqrt(16))
''',

    "from_import.py": '''# from ... import
from math import sqrt, pi
print(sqrt(25), pi)
''',

    "import_possibilities.py": '''# Various Possibilities of import
import math
from math import sqrt
from math import *
''',

    "member_aliasing.py": '''# Member Aliasing
from math import sqrt as square_root
print(square_root(36))
''',

    "reloading_module.py": '''# Reloading a Module
import importlib
import math
importlib.reload(math)
''',

    "dir_function.py": '''# Finding Members of Module by using dir() Function
import math
print(dir(math))
''',

    "special_name.py": '''# The Special Variable __name__
def show():
    print("Module name:", __name__)
show()
''',

    "math_module.py": '''# Working with math Module
import math
print(math.factorial(5))
print(math.pow(2, 3))
print(math.ceil(2.3))
''',

    "random_module.py": '''# Working with random Module
import random
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))
print(random.random())
'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)