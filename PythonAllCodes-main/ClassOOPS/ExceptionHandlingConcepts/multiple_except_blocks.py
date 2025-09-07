# try with Multiple except Blocks
try:
    x = int("abc")
except ValueError:
    print("ValueError")
except TypeError:
    print("TypeError")
