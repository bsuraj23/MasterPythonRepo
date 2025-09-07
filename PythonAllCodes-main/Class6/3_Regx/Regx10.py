import re

pattern = re.escape('a+b*c')
print(re.match(pattern, 'a+b*c'))

pattern = re.escape('1.5$')
print(re.match(pattern, '1.5$'))

pattern = re.escape('[a-z]+')
print(re.match(pattern, '[a-z]+'))

pattern = re.escape('(group)')
print(re.match(pattern, '(group)'))

pattern = re.escape('{1,3}')
print(re.match(pattern, '{1,3}'))

pattern = re.escape('special^chars$')
print(re.match(pattern, 'special^chars$'))

pattern = re.escape('^start')
print(re.match(pattern, '^start'))
