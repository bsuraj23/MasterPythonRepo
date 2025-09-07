import re

pattern = re.compile(r'\d+')
print(" sashdsadfsagfd")                        
print(pattern.match('123abc'))

pattern2 = re.compile(r'\w+')
print(pattern2.search('abc123'))

pattern3 = re.compile(r'^Hello')
print(pattern3.match('Hello World'))

pattern4 = re.compile(r'end$')
print(pattern4.search('This is the end'))

pattern5 = re.compile(r'[A-Z]{4,}')
print(pattern5.search('abCDLKKK123'))

pattern6 = re.compile(r'.+')
print(pattern6.match('SomeText'))

pattern7 = re.compile(r'^\d')
print(pattern7.match('121212ssss978787787value'))


               
