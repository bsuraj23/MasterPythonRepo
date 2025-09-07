import re

print(re.sub(r'\d+', 'X', 'Item 123 costs 456'))
print(re.sub(r'cat', 'dog', 'The cat sat on the mat'))
print(re.sub(r'\s+', '-', 'replace spaces with dash'))
print(re.sub(r'[^a-zA-Z0-9]', '', 'Remove@#Special!'))
print(re.sub(r'_', ' ', 'split_this_string'))
print(re.sub(r'(.)(?=\1)', '', 'aabbcc'))  # Remove consecutive duplicates
print(re.sub(r'^', 'Start-', 'line'))
