name = "Alice"
age = 30
print("My name is {} and age is {}".format(name, age))
print(f"My name is {name} and age is {age}")
#TODO:
#todo
#code for using int or float,decimal in format
height = 5.9
print("My name is {} and age is {} and height is {}".format(name, age, height))
print(f"My name is {name}, age is {age}, and height is {height}")
print("My name is {0}, age is {1}, and height is {2}".format(name, age, height))
print("My name is {n}, age is {a}, and height is {h}".format(n=name, a=age, h=height))
print(f"My name is {name}, age is {age}, and height is {height:.1f}")  # formatted to 1 decimal place
#print("My name is {}, age is {}, and height is {:.1f}".format(name, age, height))  # formatted to 1 decimal place
print("My name is {0}, age is {1}, and height is {2:.1f}".format(name, age, height))  # formatted to 1 decimal place
print("My name is {n}, age is {a}, and height is {h:.1f}".format(n=name, a=age, h=height))  # formatted to 1 decimal place


#TODO
#number formatting for signed numbers,decimals,floats etc
num = 1234.56789
print("Formatted number (default): {}".format(num))
print("Formatted number (2 decimal places): {:.2f}".format(num))
print("Formatted number (signed): {:+.2f}".format(num))
print("Formatted number (with thousands separator): {:,.2f}".format(num))