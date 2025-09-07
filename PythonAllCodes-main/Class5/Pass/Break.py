
# for i in range(6):      
#   # i=1,2,3     (1-5)
#     if i == 3:
#         continue
#         print("I am inside loop")
       
#     print(i)
# print("I am the end of line and not inside for loop")


# count = 0
# while True:
#     print("Count:", count)
#     count += 1
#     if count == 5:
#         break


# # Example 3: Stop searching after finding target
# numbers = [5,1, 3, 4, 7, 9]
# for num in numbers:
#     print(num)
#     if num == 5:
#         print("Found 5!")
#         break

# Example 4: Break if item exists in list
names = ["Tom", "Jerry", "Spike"]
for name in names:
    if name == "Jerry":
        print("Jerry found!")
        break

# # Example 5: Break in nested loop
# for i in range(1,21):   # i=0    (0-2)
#     for j in range(1,7): #  j=0        (0-2)
#         # if j == 2:
#         #     break
#          print(f"i={i}, j={j}")
