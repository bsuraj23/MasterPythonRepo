import re

print(re.findall(r'\d+', 'Find 123 and 456'))
print(re.findall(r'\D+', 'Only words and spaces 123'))
print(re.findall(r'\s+', 'Spaces are \t included \n here'))
print(re.findall(r'\S+', 'Non-space characters only'))
print(re.findall(r'\w+', 'Words_and123numbers'))
print(re.findall(r'\W+', '!!@@##$$ symbols only'))
print(re.findall(r'^Hello', 'Hello there!'))
