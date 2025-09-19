from collections import Counter

cnt = Counter(['apple', 'banana', 'apple', 'orange', 'banana'])

print(cnt)               # Counter({'apple': 2, 'banana': 2, 'orange': 1})
print(cnt['apple'])      # 2

# Most common
print("Most common method ",cnt.most_common(1))  # [('apple', 2)]


#TODO Add more methods of counter
# Update counts
cnt.update(['apple', 'banana', 'banana'])
print(cnt)               # Counter({'banana': 3, 'apple': 3, 'orange': 1})
# Subtract counts
cnt.subtract(['apple', 'orange'])
print(cnt)               # Counter({'banana': 3, 'apple': 2, 'orange': 0})
# Elements
print(list(cnt.elements()))  # ['apple', 'apple', 'banana', 'banana', 'banana']
# Total count
print(sum(cnt.values()))    # 5
# Clear counts
cnt.clear()
print(cnt)                 # Counter()
# Arithmetic operations
cnt1 = Counter(a=3, b=1)
cnt2 = Counter(a=1, b=2)
print(cnt1 + cnt2)         # Counter({'a': 4, 'b': 3})
print(cnt1 - cnt2)         # Counter({'a': 2})  
print(cnt1 & cnt2)         # Counter({'a': 1, 'b': 1})
print(cnt1 | cnt2)         # Counter({'a': 3, 'b': 2})
# Convert to dictionary
d = dict(cnt1)



