# # Factorial using recursion
def sampath(input):
    if input == 0:
        return 1
    return input * sampath(input - 1)

# factorial(1)

print(sampath(5))

# for temp in range(5):
#     print(temp)



# def add(x=0,y=0):  # function with default argument
#     c= x + y
#     return c,"Hellow World"
    

# # add() #calling function
# print(add())  # printing function return value
# print(add(10))  #
# first,second=add(10,20)














