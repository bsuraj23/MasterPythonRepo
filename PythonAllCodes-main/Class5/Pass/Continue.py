# Example 1: Skip printing number 3
# for i in range(1, 6):  #i=1,2,3
#     if i == 3:
#         print("I am inside if")
#         continue
#         print("I am after continue code may 10 lines but after continue")
       
#     print("I am out side if and for I am the end line ")

# Example 2: Skip vowels
# word = "Name"
# for letter in word:
#     if letter in "aeiou":
#         continue
#     print(letter)

# # Example 3: Skip even numbers
# for i in range(10):
#     if i % 2 != 0:
#         continue
#     print(i)

# # Example 4: Skip negative numbers
# numbers = [1, -2, 3, -4, 5]
# for num in numbers:
#     if num >0:
#         continue
#     print(num)

# # Example 5: Skip empty strings
words = ["apple", "", "banana", "", "cherry"]
for word in words:
    if word != "":
        continue
    print(word)
