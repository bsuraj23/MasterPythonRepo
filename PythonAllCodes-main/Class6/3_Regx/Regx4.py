import re

# 10100101 100101 1001010 Xsjsj-rint(re.split(r'\s+', 'Split these words'))
print(re.split(r'\d', 'item1price456'))
print(re.split(r'[,:]', 'apple,banana:cherry'))
print(re.split(r'[A-Z]', 'splitAtCapitals'))
print(re.split(r'_', 'split_this_string'))
print(re.split(r'-', '2025-07-15'))
print(re.split(r'\W+', 'Word1,Word2.Word3!$'))
