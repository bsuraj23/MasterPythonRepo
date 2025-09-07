# Reverse a string
s = "Python"
print(s[::-1])  # nohtyP

# Palindrome check
word = "madam"
print(word == word[::-1])  # True

# Count vowels
s = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in s if char in vowels)
print(count)  # 3