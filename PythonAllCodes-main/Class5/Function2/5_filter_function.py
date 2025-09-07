# filter() Function
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)


# Example with filter
words = ["apple", "banana", "cherry", "date"]
a_words = list(filter(lambda word: word.startswith('a'), words))
print(a_words)