#>>> for n in range(2, 10):
#...     for x in range(2, n):
#...         if n % x == 0:
#...             print(n, 'equals', x, '*', n//x)
#...             break
#...     else:
#...         # loop fell through without finding a factor
#...         print(n, 'is a prime number')
#...
  


# Simple break and for loop example
for i in range(1, 10):
    if i == 6:
        print("Breaking the loop at", i)
        break
    print("Current value:", i)


for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print("%d equals %d * %d",(num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print  ("is a prime number")




# for num in range(10, 20): 
#  for i in range(2, num):  # i = 2
#         if num % i == 0:  # to determine the first factor
#             j = num // i  # use integer division
#             print(f"{num} equals {i} * {j}")
#             break  # move to the next number, the first FOR
# else:  # else part of the loop
#         print(f"{num} is a prime number")

# for Grand in range(1, 5):  #    num = 10   (10,19)
#     for parent in range(1, 30):  # i = 2   (2,10)
#         for child in range(1,11):
#              print(num,i,temp)


for outer in range(5):
   if outer ==3 :
      continue 
   print(outer)