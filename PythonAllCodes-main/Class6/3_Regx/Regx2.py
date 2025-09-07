import re

print(re.search(r'\d+', 'abcxyz'))
print(re.search(r'is', 'The black cat is here.'))
print(re.search(r'[a-z]+', 'helloWorldTest'))
print(re.search(r'table$', 'This is the table'))
print(re.search(r'^\w+', '12 Start123 end'))
print(re.search(r'colou?r', 'The color is nice')) 
print(re.search(r'\s', 'vyvy here'))







