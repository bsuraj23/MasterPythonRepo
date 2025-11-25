import re 

print(re.match(r'\d+', 'abc'))   
# print("\n")
print(re.match(r'\w+', 'Hello123'))


print(re.match(r'[A-Z]', 'Python3ajshjdsgasgdasudfgdhsss'))
print(re.match(r'[a-z]+', 'XYZabc'))




print(re.match(r'abcd', 'abcde'))
#explain this code  in one line
print("line 16")
print(re.match(r'^\d+', '33abc'))



print(re.match(r'^\d', '5days'))
print(re.match(r'.+', ''))
#some more explaination of regex
print(re.match(r'\d{3}', '4abc123333'))
print(re.match(r'\d{2,4}', '1abc'))
print(re.match(r'\d{2,4}', '12345abc'))





