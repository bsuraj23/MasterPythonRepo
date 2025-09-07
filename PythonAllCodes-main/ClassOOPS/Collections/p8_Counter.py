from collections import Counter

cnt = Counter(['apple', 'banana', 'apple', 'orange', 'banana'])

print(cnt)               # Counter({'apple': 2, 'banana': 2, 'orange': 1})
print(cnt['apple'])      # 2

# Most common
print(cnt.most_common(1))  # [('apple', 2)]
