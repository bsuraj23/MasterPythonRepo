Mohan = [3, 1, 4]
Mohan.append(5)
print("After append ",Mohan)
Mohan.insert(2, 24)
print("After Insert ",Mohan)


Mohan.remove(4)
print("After remove ",Mohan)
Mohan.sort()
print("After sort ",Mohan)
Mohan.pop()  #has return type too
print("After pop ",Mohan)
#using index in pop
Mohan.pop()
print("After one more pop ",Mohan)
Mohan.clear()
print("After clear ",Mohan)

a= (1,2,3,4,"suraj")
print(a)


#reverse ,sort ,reverse default sorting order etc
Mohan.reverse()
print("After reverse ",Mohan)
Mohan.sort(reverse=True)
print("After sort in reverse order ",Mohan)

#sort
Mohan.sort()
print("After sort ",Mohan)
# reverse
Mohan.reverse()
print("After reverse ",Mohan)
#  default sorting order etc
Mohan.sort(reverse=True)
print("After sort in reverse order ",Mohan)


#add a new file on copy of list ..using slicing and copy 
Mohan = [3, 1, 4]
Mohan_copy1 = Mohan[:]  # using slicing
Mohan_copy2 = Mohan.copy()  # using copy method
print("Original List: ", Mohan) 
print("Copy using slicing: ", Mohan_copy1)
print("Copy using copy method: ", Mohan_copy2)


#Nested List and Matrix concept
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List: ", nested_list)
# Accessing elements
print("Element at (0,0): ", nested_list[0][0])  #
print("Element at (1,2): ", nested_list[1][2])  #
print("Element at (2,1): ", nested_list[2][1])  #
# Iterating through nested list
for sublist in nested_list:
    for item in sublist:
        print(item, end=' ')
    print()
# Matrix addition
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("Matrix Addition Result: ", result)
# Matrix multiplication
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]