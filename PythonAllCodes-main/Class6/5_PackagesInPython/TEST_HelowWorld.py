
import HelowWorld
import math



result = HelowWorld.add(3, 5)
print("The sum is:", result)
result = HelowWorld.add(-1, 1)
print("The sum is:", result)
result = HelowWorld.add(0, 0)
print("The sum is:", result)
# one more test
result = HelowWorld.add(10.0, 20.89)
print("The sum is:", result)
result = HelowWorld.add()
print("The sum is:", result)

#TEst cases for plaindrome
test_strings = ["radar", "hello", "level", "world", "madam", "python"]
for str in test_strings:   
    if HelowWorld.is_palindrome(str):
        print(f'"{str}" is a palindrome.')
    else:
        print(f'"{str}" is not a palindrome.')    


