"""
Cognizant Python Fresher Interview Questions & Answers
=====================================================

This file contains comprehensive Python interview questions commonly asked in
Cognizant fresher interviews, organized by difficulty and topic.
"""

print("=" * 60)
print("COGNIZANT PYTHON FRESHER INTERVIEW QUESTIONS")
print("=" * 60)

# ========================================
# SECTION 1: BASIC PYTHON CONCEPTS
# ========================================

print("\n1. BASIC PYTHON CONCEPTS")
print("-" * 40)

# Q1: What is Python? Why is it popular?
print("\nQ1: What is Python? Why is it popular?")
print("Answer:")
print("""
- Python is a high-level, interpreted programming language
- Easy to learn and read syntax
- Extensive standard library
- Cross-platform compatibility
- Strong community support
- Used in web development, data science, AI/ML, automation
""")

# Q2: Difference between Python 2 and Python 3
print("\nQ2: Key differences between Python 2 and Python 3")
print("Answer:")

# Python 2 vs 3 examples
print("Python 2:")
# print "Hello World"  # This would work in Python 2
print("Python 3:")
print("Hello World")  # This works in Python 3

print("Division:")
print("Python 2: 5/2 =", 5//2, "(integer division by default)")
print("Python 3: 5/2 =", 5/2, "(float division by default)")

# Q3: Python data types
print("\nQ3: Python Data Types with examples:")

# Numbers
integer_num = 42
float_num = 3.14
complex_num = 1 + 2j
print(f"Integer: {integer_num}, type: {type(integer_num)}")
print(f"Float: {float_num}, type: {type(float_num)}")
print(f"Complex: {complex_num}, type: {type(complex_num)}")

# Strings
string_example = "Hello, Cognizant!"
print(f"String: {string_example}, type: {type(string_example)}")

# Boolean
bool_example = True
print(f"Boolean: {bool_example}, type: {type(bool_example)}")

# Collections
list_example = [1, 2, 3, 'python']
tuple_example = (1, 2, 3, 'python')
dict_example = {'name': 'John', 'age': 25}
set_example = {1, 2, 3, 4}

print(f"List: {list_example}, type: {type(list_example)}")
print(f"Tuple: {tuple_example}, type: {type(tuple_example)}")
print(f"Dictionary: {dict_example}, type: {type(dict_example)}")
print(f"Set: {set_example}, type: {type(set_example)}")

# ========================================
# SECTION 2: CONTROL STRUCTURES
# ========================================

print("\n\n2. CONTROL STRUCTURES")
print("-" * 40)

# Q4: If-else statements
print("\nQ4: If-else statement example:")
age = 22
if age >= 21:
    print(f"Age {age}: Eligible for job")
elif age >= 18:
    print(f"Age {age}: Adult but may need more experience")
else:
    print(f"Age {age}: Too young")

# Q5: Loops
print("\nQ5: Loop examples:")

# For loop
print("For loop with range:")
for i in range(5):
    print(f"Number: {i}")

print("\nFor loop with list:")
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

# ========================================
# SECTION 3: FUNCTIONS
# ========================================

print("\n\n3. FUNCTIONS")
print("-" * 40)

# Q6: Function definition and types of arguments
print("\nQ6: Function examples:")

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Cognizant Candidate"))

# Function with default arguments
def calculate_total(price, tax=0.08):
    return price + (price * tax)

print(f"Total with default tax: ${calculate_total(100):.2f}")
print(f"Total with custom tax: ${calculate_total(100, 0.10):.2f}")

# Function with *args and **kwargs
def process_data(*args, **kwargs):
    print(f"Arguments: {args}")
    print(f"Keyword arguments: {kwargs}")
    return sum(args) if args else 0

result = process_data(1, 2, 3, name="John", department="IT")
print(f"Sum of numbers: {result}")

# Lambda function
square = lambda x: x ** 2
print(f"Lambda function - Square of 5: {square(5)}")

# ========================================
# SECTION 4: DATA STRUCTURES
# ========================================

print("\n\n4. DATA STRUCTURES")
print("-" * 40)

# Q7: List operations
print("\nQ7: List operations:")
numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# Common list methods
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

removed = numbers.pop()
print(f"After pop(): {numbers}, removed: {removed}")

numbers.remove(3)
print(f"After remove(3): {numbers}")

# List comprehension
squares = [x**2 for x in range(5)]
print(f"List comprehension squares: {squares}")

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Q8: Dictionary operations
print("\nQ8: Dictionary operations:")
employee = {
    'id': 101,
    'name': 'John Doe',
    'department': 'IT',
    'salary': 50000
}
print(f"Employee: {employee}")

# Dictionary methods
print(f"Keys: {list(employee.keys())}")
print(f"Values: {list(employee.values())}")
print(f"Items: {list(employee.items())}")

# Adding and updating
employee['email'] = 'john@cognizant.com'
employee.update({'salary': 55000, 'location': 'Chennai'})
print(f"Updated employee: {employee}")

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(f"Dictionary comprehension: {squared_dict}")

# Q9: Set operations
print("\nQ9: Set operations:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# ========================================
# SECTION 5: STRING MANIPULATION
# ========================================

print("\n\n5. STRING MANIPULATION")
print("-" * 40)

# Q10: String methods
print("\nQ10: String methods:")
text = "  Welcome to Cognizant Technology Solutions  "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Title: '{text.title()}'")

# String formatting
name = "Python Developer"
experience = 2
print(f"String formatting:")
print("Format method:", 'Hello, I am a {} with {} years experience'.format(name, experience))
print(f"f-string: 'Hello, I am a {name} with {experience} years experience'")

# String operations
sentence = "Python is awesome for data science"
print(f"Split: {sentence.split()}")
print(f"Replace: {sentence.replace('awesome', 'excellent')}")
print(f"Find: Position of 'is' = {sentence.find('is')}")
print(f"Count: 'a' appears {sentence.count('a')} times")

# ========================================
# SECTION 6: FILE HANDLING
# ========================================

print("\n\n6. FILE HANDLING")
print("-" * 40)

# Q11: File operations
print("\nQ11: File handling example:")

# Writing to file
try:
    with open('cognizant_test.txt', 'w') as file:
        file.write("Welcome to Cognizant!\n")
        file.write("Python programming interview\n")
        file.write("Good luck with your interview!")
    print("File written successfully")
    
    # Reading from file
    with open('cognizant_test.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
        
    # Reading line by line
    with open('cognizant_test.txt', 'r') as file:
        print("\nReading line by line:")
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")
            
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error: {e}")

# ========================================
# SECTION 7: ERROR HANDLING
# ========================================

print("\n\n7. ERROR HANDLING")
print("-" * 40)

# Q12: Exception handling
print("\nQ12: Exception handling examples:")

# Basic try-except
def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"
    except Exception as e:
        return f"Unexpected error: {e}"
    finally:
        print("Division operation completed")

print(f"10 / 2 = {safe_division(10, 2)}")
print(f"10 / 0 = {safe_division(10, 0)}")

# Custom exception
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative")
    if age > 120:
        raise CustomError("Age seems unrealistic")
    return "Valid age"

try:
    print(validate_age(25))
    print(validate_age(-5))
except CustomError as e:
    print(f"Custom error: {e}")

# ========================================
# SECTION 8: OBJECT-ORIENTED PROGRAMMING
# ========================================

print("\n\n8. OBJECT-ORIENTED PROGRAMMING")
print("-" * 40)

# Q13: Class and Objects
print("\nQ13: Class and Object example:")

class Employee:
    # Class variable
    company = "Cognizant"
    
    def __init__(self, name, employee_id, department):
        # Instance variables
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.projects = []
    
    # Instance method
    def add_project(self, project):
        self.projects.append(project)
    
    def get_info(self):
        return f"Employee: {self.name}, ID: {self.employee_id}, Dept: {self.department}"
    
    # Class method
    @classmethod
    def get_company(cls):
        return cls.company
    
    # Static method
    @staticmethod
    def is_valid_employee_id(emp_id):
        return len(str(emp_id)) == 6

# Creating objects
emp1 = Employee("Alice", 123456, "Software Development")
emp2 = Employee("Bob", 789012, "Data Analytics")

print(emp1.get_info())
print(emp2.get_info())

emp1.add_project("Web Application")
emp1.add_project("Mobile App")
print(f"{emp1.name}'s projects: {emp1.projects}")

print(f"Company: {Employee.get_company()}")
print(f"Valid ID check: {Employee.is_valid_employee_id(123456)}")

# Q14: Inheritance
print("\nQ14: Inheritance example:")

class Developer(Employee):
    def __init__(self, name, employee_id, department, programming_languages):
        super().__init__(name, employee_id, department)
        self.programming_languages = programming_languages
    
    def code(self, language):
        if language in self.programming_languages:
            return f"{self.name} is coding in {language}"
        return f"{self.name} doesn't know {language}"
    
    # Method overriding
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Languages: {', '.join(self.programming_languages)}"

dev = Developer("Charlie", 345678, "Software Development", ["Python", "Java", "JavaScript"])
print(dev.get_info())
print(dev.code("Python"))
print(dev.code("C++"))

# ========================================
# SECTION 9: ADVANCED CONCEPTS
# ========================================

print("\n\n9. ADVANCED CONCEPTS")
print("-" * 40)

# Q15: Decorators
print("\nQ15: Decorator example:")

def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Fibonacci(10) = {fibonacci(10)}")

# Q16: Generators
print("\nQ16: Generator example:")

def number_generator(n):
    for i in range(n):
        yield i ** 2

gen = number_generator(5)
print("Generator squares:")
for num in gen:
    print(num)

# Generator expression
squares_gen = (x**2 for x in range(5))
print(f"Generator expression: {list(squares_gen)}")

# Q17: Map, Filter, Reduce
print("\nQ17: Map, Filter, Reduce examples:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map
squared = list(map(lambda x: x**2, numbers))
print(f"Map (squares): {squared}")

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filter (evens): {evens}")

# Reduce
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
print(f"Reduce (sum): {sum_all}")

# ========================================
# SECTION 10: PRACTICAL CODING PROBLEMS
# ========================================

print("\n\n10. PRACTICAL CODING PROBLEMS")
print("-" * 40)

# Q18: Reverse a string
print("\nQ18: Reverse a string:")

def reverse_string(s):
    return s[::-1]

def reverse_string_manual(s):
    result = ""
    for char in s:
        result = char + result
    return result

text = "Cognizant"
print(f"Original: {text}")
print(f"Reversed (slicing): {reverse_string(text)}")
print(f"Reversed (manual): {reverse_string_manual(text)}")

# Q19: Check palindrome
print("\nQ19: Check palindrome:")

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
for test in test_strings:
    print(f"'{test}' is palindrome: {is_palindrome(test)}")

# Q20: Find factorial
print("\nQ20: Find factorial:")

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = 5
print(f"Factorial of {num} (recursive): {factorial_recursive(num)}")
print(f"Factorial of {num} (iterative): {factorial_iterative(num)}")

# Q21: FizzBuzz
print("\nQ21: FizzBuzz:")

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print("FizzBuzz for 1-15:")
fizzbuzz(15)

# Q22: Count vowels
print("\nQ22: Count vowels:")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

test_string = "Cognizant Technology Solutions"
print(f"Vowels in '{test_string}': {count_vowels(test_string)}")

# Q23: Remove duplicates from list
print("\nQ23: Remove duplicates:")

def remove_duplicates(lst):
    return list(set(lst))

def remove_duplicates_order(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
print(f"Original: {numbers_with_duplicates}")
print(f"No duplicates (set): {remove_duplicates(numbers_with_duplicates)}")
print(f"No duplicates (order preserved): {remove_duplicates_order(numbers_with_duplicates)}")

# Q24: Anagram check
print("\nQ24: Check anagram:")

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

word1, word2 = "listen", "silent"
print(f"'{word1}' and '{word2}' are anagrams: {are_anagrams(word1, word2)}")

# Q25: Second largest number
print("\nQ25: Find second largest:")

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        return None
    unique_numbers.sort()
    return unique_numbers[-2]

test_numbers = [1, 5, 3, 9, 2, 8, 9]
print(f"Numbers: {test_numbers}")
print(f"Second largest: {second_largest(test_numbers)}")

# ========================================
# SECTION 11: INTERVIEW TIPS
# ========================================

print("\n\n11. COGNIZANT INTERVIEW TIPS")
print("-" * 40)

print("""
TECHNICAL PREPARATION:
✓ Master Python basics (data types, control structures, functions)
✓ Understand OOP concepts (classes, inheritance, polymorphism)
✓ Practice coding problems (arrays, strings, basic algorithms)
✓ Know file handling and exception handling
✓ Understand decorators, generators, and lambda functions

COMMONLY ASKED TOPICS:
✓ Python vs other languages
✓ List vs Tuple vs Dictionary vs Set
✓ Mutable vs Immutable objects
✓ Memory management and garbage collection
✓ PEP 8 coding standards
✓ Virtual environments
✓ Modules and packages

CODING ROUND PREPARATION:
✓ Basic mathematical programs (factorial, fibonacci, prime numbers)
✓ String manipulation problems
✓ Array/List operations
✓ Sorting and searching algorithms
✓ Pattern printing programs

BEHAVIORAL QUESTIONS:
✓ Why do you want to join Cognizant?
✓ Tell me about yourself
✓ Strengths and weaknesses
✓ Career goals
✓ Teamwork experience

PROJECT DISCUSSION:
✓ Be ready to explain your projects in detail
✓ Know the technologies used
✓ Understand the problem your project solved
✓ Be prepared for technical questions about your project
""")

print("\n" + "=" * 60)
print("GOOD LUCK WITH YOUR COGNIZANT INTERVIEW!")
print("=" * 60)

if __name__ == "__main__":
    print("\nThis file contains comprehensive Python interview preparation material.")
    print("Run this script to see all examples in action!")