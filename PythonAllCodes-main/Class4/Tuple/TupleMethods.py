tup = (1, 2, 2,2, 3)
print(tup.count(2))


# print(tup.count(2))
# print(tup.index(2))

# # Remaining examples
# print(tup.count(10))
# print((5, 5, 5).index(5))
print(('a', 'b', 'c').count('d'))  # returns 0


print((1, 2, 3).index(2))


#cmp function
def compare_tuples(tup1, tup2):
    if tup1 < tup2:
        return -1
    elif tup1 > tup2:
        return 1
    else:
        return 0


#Mathematical operator + and * example for tuple - 119
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
print("Tuple Addition: ", tup1 + tup2)
print("Tuple Multiplication: ", tup1 * 3)


#Membership operator in and not in example for tuple - 120
print("In operator: ", 2 in tup1)
print("Not in operator: ", 5 not in tup1)

#Iteration through tuple using for loop - 121
for item in tup1:
    print("Iterating through tuple: ", item)

#Tuple unpacking - 122
a, b, c = tup1
print("Tuple Unpacking: ", a, b, c)
