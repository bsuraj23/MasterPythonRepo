# Example code to demonstrate reading input in Python 3.x


#raw input code

value = int(input("Please enter an integer: "))
print("You entered:", value)

#raw input code
bool_value = bool(input("Please enter a boolean value (True/False): "))
print("You entered:", bool_value)
#raw input code     
string_value = str(input("Please enter a string: "))
print("You entered:", string_value)
#raw input code
float_value = float(input("Please enter a floating-point number: "))
print("You entered:", float_value)
# Observe the behavior of different data types with
# raw_input in Python 2.x and input in Python 3.x
# In Python 3.x, input() reads input as a string,       


    
# when you enter values like 10, 10.5, True, "Hello"
# in the input prompt.
# Note: In Python 2.x, raw_input() reads input as a string,
# while input() evaluates the input as a Python expression.     