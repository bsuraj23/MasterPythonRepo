import re

print(re.fullmatch(r'\d+', '12345'))
print(re.fullmatch(r'\w+', 'Python3'))
print(re.fullmatch(r'abc', 'abc'))
print(re.fullmatch(r'[a-z]+', 'hello'))
print(re.fullmatch(r'[A-Z][a-z]+', 'Python'))
print(re.fullmatch(r'.+', 'JustText'))
print(re.fullmatch(r'colou?r', 'color'))
