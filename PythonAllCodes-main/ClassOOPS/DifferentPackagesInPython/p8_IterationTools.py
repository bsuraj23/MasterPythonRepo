import itertools

# Count infinitely
# for i in itertools.count(1): print(i)

# Cycle through list
cyc = itertools.cycle([1, 2, 3,4,5])
print(next(cyc), next(cyc), next(cyc), next(cyc))  # 1 2 3

# # Combinations
# print(list(itertools.combinations('ABCD', 2)))
