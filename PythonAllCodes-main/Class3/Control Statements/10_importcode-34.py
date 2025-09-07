import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
    print(user_paths)
except KeyError:
    user_paths = []
    print(user_paths)
# add more examples of command line arguments (without class) here
import sys
print(sys.argv) # command line arguments    
print(sys.executable) # path of the python interpreter
print(sys.version) # version of the python interpreter  
print(sys.platform) # platform of the python interpreter
print(sys.path) # list of directories that will be searched for modules
print(sys.modules) # dictionary of loaded modules
print(sys.maxsize) # maximum size of a Python int on this platform
print(sys.maxunicode) # maximum Unicode code point on this platform 