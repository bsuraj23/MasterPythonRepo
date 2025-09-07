import re

matches = re.finditer(r'\d+', 'Item 1 costs 20 and 30 more')
for m in matches:
    print(m.group())

matches = re.finditer(r'\w+', 'List all words here')
for m in matches:
    print(m.group())

matches = re.finditer(r'[A-Z]', 'Python Is Powerful')
for m in matches:
    print(m.group())

matches = re.finditer(r'colou?r', 'color or colour appears twice')
for m in matches:
    print(m.group())

matches = re.finditer(r'\b\w{3}\b', 'One two red blue')
for m in matches:
    print(m.group())

matches = re.finditer(r'\s', 'Multiple spaces exist here')
for m in matches:
    print('Space found at:', m.start())

matches = re.finditer(r'\d{2}', '12 34 56 78')
for m in matches:
    print(m.group())
