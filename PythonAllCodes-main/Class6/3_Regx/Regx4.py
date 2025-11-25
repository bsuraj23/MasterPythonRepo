import re

# 10100101 100101 1001010 Xsjsj-rint(re.split(r'\s+', 'Split these words'))
print(re.split(r'\d', 'Ayub1Aditya4Suraj5'))
print(re.split(r'[,:]', 'apple,banana:cherry'))
print(re.split(r'[A-Z]', 'splitAtCapitals'))
print(re.split(r'_', 'split_this_string'))
print(re.split(r'9', '2025-07-15'))
print(re.split(r'\W+', 'Word1,Word2.Word3!$'))


list =[]
for i in re.finditer(r'\d+', 'Item1 Item2 Item3 456 Item4 7890'):
    list.append(i.group())

print(list)
    