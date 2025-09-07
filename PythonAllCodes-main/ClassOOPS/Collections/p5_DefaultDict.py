from collections import defaultdict

dd = defaultdict(int)  # default value = 0

dd['apple'] += 1
dd['banana'] += 2

print(dd)  # {'apple': 1, 'banana': 2}
print(dd['mango'])  # 0 (no KeyError!)
