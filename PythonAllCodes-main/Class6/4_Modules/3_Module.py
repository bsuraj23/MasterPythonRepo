#reloading module   
import importlib
import my_math_module as mm
importlib.reload(mm)
print("After reloading the module:")
print("Addition: ", mm.add(10, 5))          # Output: 15
print("Subtraction: ", mm.subtract(10, 5))  # Output: 5
print("Multiplication: ", mm.multiply(10, 5))  # Output: 50
print("Division: ", mm.divide(10, 0))       # Output    : Division by zero is not allowed
print("Power: ", mm.power(2, 3))            # Output: 8
print("Modulus: ", mm.modulus(10, 3))       # Output: 1
# End of Class6/4_Modules/3_Module.py
# You can run this file directly to test the functions from the module
# or you can import this module in another Python script to use the functions       


# Example of aliasing   
import my_math_module as mm
print(mm.add(10, 5))  # Output: 15

#code to demo printing module docstring
import my_math_module as mm
print(mm.__doc__)  # Output: None (since no docstring is defined in the module)


#code to demo internal properties of a module
import my_math_module as mm
print(mm.__name__)      # Output: my_math_module
print(mm.__file__)      # Output: Path to the module file   
print(mm.__package__)   # Output: None (since it's a top-level module)
print(mm.__loader__)    # Output: <_frozen_importlib_external.SourceFileLoader object at ...>
print(mm.__spec__)      # Output: ModuleSpec(name='my_math_module', loader=<_frozen_importlib_external.SourceFileLoader object at ...>, origin='...')       
# These properties provide information about the module and its loading mechanism
# You can use these properties for debugging and introspection purposes
# End of the module internal properties demonstration code

