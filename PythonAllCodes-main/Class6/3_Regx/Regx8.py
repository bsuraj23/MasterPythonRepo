import re

print(re.findall(r'\d+', 'There are 3 cats and 4 dogs'))
print(re.findall(r'[A-Z]', 'Python Is Great'))
print(re.findall(r'colou?r', 'color and colour'))
print(re.findall(r'\b\w{4}\b', 'This text has four word size words'))
print(re.findall(r'\s', 'space here and there'))
print(re.findall(r'\w+', 'List all words here123'))
print(re.findall(r'[aeiou]', 'Count vowels in sentence'))
