#code to demo assesrtion loggin in python
import logging  
logging.basicConfig(filename='app_assertion.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
def divide(a, b):
    logging.info(f"Dividing {a} by {b}")
    assert b != 0, "Denominator should not be zero"
    return a / b    
try:
    result = divide(10, 0)
    print("Result: ", result)
except AssertionError as e:
    logging.error(f"AssertionError: {e}")
try:
    result = divide(10, 2)
    print("Result: ", result)
except AssertionError as e:
    logging.error(f"AssertionError: {e}")


#code to demo logging with assertions without exceptions    

import logging  
logging.basicConfig(filename='app_assertion.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
def calculate_square_root(x):
    logging.info(f"Calculating square root of {x}")
    assert x >= 0, "Input should be non-negative"
    return x ** 0.5


#code to demo simple assertion logging
import logging
logging.basicConfig(filename='app_assertion.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
def check_positive(number):
    logging.info(f"Checking if {number} is positive")
    assert number > 0, "Number should be positive"
    logging.info(f"{number} is positive")
    return True 
