# map() Function
numbers = [1, 2, 3, 4]
map(para1,para2)
squares = list(map(lambda x: x * x, numbers))
squares = [1,4,9,16]
print(squares)


# square the input from the user

def square(x):
    return x * x
user_inputs = [1, 2, 3, 4, 5]
squared_values = list(map(square, user_inputs))