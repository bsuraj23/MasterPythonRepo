# Cognizant Python Fresher Interview - Quick Reference Guide

## 🎯 Most Frequently Asked Questions

### 1. Basic Python Questions
**Q: What is Python? Why is it popular?**
- High-level, interpreted language
- Easy syntax, extensive libraries
- Cross-platform, strong community
- Used in web dev, data science, AI/ML

**Q: Python 2 vs Python 3 differences**
- Print statement vs function: `print "hello"` vs `print("hello")`
- Division: `5/2=2` vs `5/2=2.5`
- Unicode handling improved in Python 3

**Q: Python data types**
```python
# Numeric: int, float, complex
age = 25
price = 99.99
num = 1 + 2j

# Sequence: string, list, tuple
name = "John"
fruits = ['apple', 'banana']
coordinates = (10, 20)

# Collections: dict, set
person = {'name': 'John', 'age': 25}
unique_nums = {1, 2, 3, 4}
```

### 2. Data Structures

**Q: List vs Tuple vs Dictionary vs Set**
```python
# List - ordered, mutable, allows duplicates
fruits = ['apple', 'banana', 'apple']
fruits.append('orange')

# Tuple - ordered, immutable, allows duplicates
coordinates = (10, 20, 10)

# Dictionary - unordered, mutable, key-value pairs
student = {'name': 'John', 'grade': 'A'}

# Set - unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 4}
```

**Q: List methods**
```python
numbers = [1, 2, 3]
numbers.append(4)      # Add to end
numbers.insert(0, 0)   # Insert at index
numbers.remove(2)      # Remove first occurrence
popped = numbers.pop() # Remove and return last
```

### 3. Control Structures

**Q: Loops and conditionals**
```python
# If-else
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 3:
    print(count)
    count += 1
```

### 4. Functions

**Q: Function types**
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# Default arguments
def calculate(a, b=10):
    return a + b

# *args and **kwargs
def process(*args, **kwargs):
    print(args, kwargs)

# Lambda function
square = lambda x: x**2
```

### 5. Object-Oriented Programming

**Q: Class and Objects**
```python
class Employee:
    company = "Cognizant"  # Class variable
    
    def __init__(self, name, id):
        self.name = name      # Instance variable
        self.id = id
    
    def get_info(self):
        return f"{self.name} - {self.id}"

emp = Employee("John", 123)
print(emp.get_info())
```

**Q: Inheritance**
```python
class Developer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language
    
    def code(self):
        return f"Coding in {self.language}"
```

### 6. String Manipulation

**Q: Common string operations**
```python
text = "  Hello World  "
print(text.strip())      # Remove whitespace
print(text.upper())      # Convert to uppercase
print(text.lower())      # Convert to lowercase
print(text.split())      # Split into list
print(text.replace("Hello", "Hi"))  # Replace substring

# String formatting
name = "John"
age = 25
print(f"Name: {name}, Age: {age}")  # f-string (preferred)
print("Name: {}, Age: {}".format(name, age))  # format method
```

### 7. File Handling

**Q: File operations**
```python
# Writing to file
with open('file.txt', 'w') as f:
    f.write("Hello World")

# Reading from file
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

# Reading line by line
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())
```

### 8. Error Handling

**Q: Exception handling**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Cleanup code here")
```

### 9. Common Coding Problems

**Q: Reverse a string**
```python
def reverse_string(s):
    return s[::-1]

# Alternative
def reverse_manual(s):
    result = ""
    for char in s:
        result = char + result
    return result
```

**Q: Check palindrome**
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```

**Q: Factorial**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Iterative version
def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

**Q: FizzBuzz**
```python
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
```

**Q: Remove duplicates from list**
```python
def remove_duplicates(lst):
    return list(set(lst))  # Unordered

def remove_duplicates_ordered(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result
```

**Q: Find second largest number**
```python
def second_largest(numbers):
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]
```

### 10. Advanced Concepts (May be asked)

**Q: List comprehension**
```python
# Square of even numbers
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
```

**Q: Map, Filter, Reduce**
```python
numbers = [1, 2, 3, 4, 5]

# Map - apply function to each element
squared = list(map(lambda x: x**2, numbers))

# Filter - filter elements based on condition
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce - reduce list to single value
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
```

## 🎯 Interview Tips

### Technical Preparation
- ✅ Practice coding on paper/whiteboard
- ✅ Understand time/space complexity basics
- ✅ Know when to use which data structure
- ✅ Practice explaining your code

### Behavioral Questions
- **Why Cognizant?** Research company values, projects
- **Tell me about yourself:** Brief, relevant background
- **Strengths:** Technical skills relevant to job
- **Weaknesses:** Show self-improvement attitude

### During the Interview
- ✅ Think out loud while coding
- ✅ Ask clarifying questions
- ✅ Test your code with examples
- ✅ Consider edge cases
- ✅ Be honest about what you don't know

### Common Mistakes to Avoid
- ❌ Not testing code with examples
- ❌ Jumping to code without understanding problem
- ❌ Not considering edge cases
- ❌ Poor variable naming
- ❌ Not explaining approach

## 🎯 Sample Questions You Might Face

1. **Coding Round:**
   - Write a program to check if a number is prime
   - Find the missing number in an array
   - Count frequency of characters in a string
   - Print patterns (star patterns, number patterns)

2. **Technical Discussion:**
   - Explain your favorite project
   - What is the difference between `is` and `==`?
   - What are decorators?
   - How does memory management work in Python?

3. **Problem Solving:**
   - Given a scenario, design a simple system
   - Debug a piece of code
   - Optimize a given solution

## 🚀 Final Checklist

**Before Interview:**
- [ ] Practice coding problems for 1-2 weeks
- [ ] Review Python basics thoroughly
- [ ] Prepare project explanations
- [ ] Research Cognizant's recent projects/news
- [ ] Practice speaking about technical concepts

**Day of Interview:**
- [ ] Arrive 15 minutes early
- [ ] Carry multiple copies of resume
- [ ] Be ready for both technical and HR rounds
- [ ] Stay calm and think before answering
- [ ] Ask relevant questions about the role

**Good Luck! 🎉**