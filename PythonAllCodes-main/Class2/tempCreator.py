import os

folder = "Class2/StringConcepts"
os.makedirs(folder, exist_ok=True)

files_content = {
    "string_data_type.py": '''s = "Hello, World!"
print(type(s))  # <class 'str'>''',

    "what_is_string.py": '''s = "Python is fun"
print(s)''',

    "multiline_string_literals.py": '''multi_line = """This is
a multi-line
string."""
print(multi_line)''',

    "access_characters.py": '''s = "Python"
print(s[0])    # P
print(s[-1])   # n''',

    "slice_operator.py": '''s = "Python"
print(s[1:4])  # yth
print(s[:2])   # Py
print(s[2:])   # thon''',

    "slice_operator_case_study.py": '''s = "Programming"
print(s[3:8])    # rammi
print(s[::-1])   # gnimmargorP''',

    "mathematical_operators.py": '''a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
print(a * 3)         # HelloHelloHello''',

    "len_function.py": '''s = "Python"
print(len(s))  # 6''',

    "checking_membership.py": '''s = "Python"
print("th" in s)     # True
print("abc" not in s) # True''',

    "comparison_of_strings.py": '''a = "apple"
b = "banana"
print(a == b)   # False
print(a < b)    # True (lexicographical)''',

    "removing_spaces.py": '''s = "  Hello World  "
print(s.strip())      # Hello World
print(s.lstrip())     # Hello World  
print(s.rstrip())     #   Hello World''',

    "finding_substrings.py": '''s = "Python programming"
print(s.find("gram"))   # 10
print(s.find("xyz"))    # -1''',

    "counting_substring.py": '''s = "banana"
print(s.count("a"))   # 3''',

    "replacing_string.py": '''s = "I like Java"
print(s.replace("Java", "Python"))  # I like Python''',

    "splitting_strings.py": '''s = "apple,banana,cherry"
print(s.split(","))   # ['apple', 'banana', 'cherry']''',

    "joining_strings.py": '''fruits = ["apple", "banana", "cherry"]
print(", ".join(fruits))  # apple, banana, cherry''',

    "changing_case.py": '''s = "Python Programming"
print(s.upper())   # PYTHON PROGRAMMING
print(s.lower())   # python programming
print(s.title())   # Python Programming
print(s.swapcase())# pYTHON pROGRAMMING''',

    "checking_start_end.py": '''s = "Hello World"
print(s.startswith("Hello"))  # True
print(s.endswith("World"))    # True''',

    "check_type_characters.py": '''s = "Python123"
print(s.isalpha())   # False
print(s.isdigit())   # False
print(s.isalnum())   # True
print(" ".isspace()) # True''',

    "formatting_strings.py": '''name = "Alice"
age = 30
print("My name is {} and age is {}".format(name, age))
print(f"My name is {name} and age is {age}")''',

    "important_programs.py": '''# Reverse a string
s = "Python"
print(s[::-1])  # nohtyP

# Palindrome check
word = "madam"
print(word == word[::-1])  # True

# Count vowels
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)  # 3'''
}

for filename, content in files_content.items():
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)