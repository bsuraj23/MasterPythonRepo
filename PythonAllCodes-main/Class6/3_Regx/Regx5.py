import re

m = re.search(r'(\d{3})-(\d{2})-(\d{4})', '123-45-6789')
print(m.group(1), m.group(2), m.group(3))

m = re.search(r'(\w+) (\w+)', 'Hello World')
print(m.group(0), m.group(1), m.group(2))

m = re.match(r'(abc)(\d+)', 'abc123')
print(m.group(1), m.group(2))

m = re.search(r'(Hi|Hello) (\w+)', 'Hello John')
print(m.group(1), m.group(2))

m = re.search(r'(colou?r)', 'color')
print(m.group(1))

m = re.search(r'(start).*(end)', 'start middle end')
print(m.group(1), m.group(2))

m = re.search(r'(\d{2}):(\d{2})', '12:30 PM')
print(m.group(1), m.group(2))
